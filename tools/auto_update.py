#!/usr/bin/env python3
"""
Auto-Update Script for Cross-Section Dashboard (Multi-Model)

Continuously monitors for new model cycles and progressively downloads
forecast hours as they become available on NOAA servers.

Supports HRRR, GFS, RRFS, NAM, RAP, and NAM-Nest models.

Usage:
    python tools/auto_update.py                              # Default: HRRR only
    python tools/auto_update.py --models hrrr,gfs            # HRRR + GFS
    python tools/auto_update.py --models hrrr,gfs,rrfs       # Core models
    python tools/auto_update.py --models hrrr,nam,rap        # HRRR + mesoscale
    python tools/auto_update.py --interval 3                  # Check every 3 minutes
    python tools/auto_update.py --once                        # Run once and exit
    python tools/auto_update.py --max-hours 18                # Download up to F18 (HRRR)
"""

import argparse
import json
import logging
import os
import sys
import time
import signal
import shutil
from collections import deque
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from pathlib import Path
from datetime import datetime, timedelta, timezone

sys.path.insert(0, str(Path(__file__).parent.parent))

from model_config import (
    get_model_registry, get_model_config, get_model_fhr_list,
    get_model_availability_lag, SYNOPTIC_HOURS,
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

running = True
_PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUTS_BASE = Path(os.environ.get('XSECT_OUTPUTS_DIR', str(_PROJECT_DIR / 'outputs')))
import tempfile
STATUS_FILE = Path(tempfile.gettempdir()) / "auto_update_status.json"

# ---------------------------------------------------------------------------
# All model-specific config is imported from model_config.py (single source
# of truth). Build lookup dicts from the registry for backward compatibility.
# ---------------------------------------------------------------------------
_registry = get_model_registry()

MODEL_REQUIRED_PATTERNS = {
    name: cfg.grib_required_patterns or ['*.grib2']
    for name, cfg in _registry.models.items()
}
MODEL_FILE_TYPES = {
    name: cfg.grib_file_types or ['pressure']
    for name, cfg in _registry.models.items()
}
MODEL_FORECAST_HOURS = {
    name: cfg.base_fhr_list or list(range(19))
    for name, cfg in _registry.models.items()
}
MODEL_DEFAULT_MAX_FHR = {
    name: cfg.get_max_forecast_hour(0)
    for name, cfg in _registry.models.items()
}
MODEL_AVAILABILITY_LAG = {
    name: cfg.availability_lag_minutes
    for name, cfg in _registry.models.items()
}


def write_status(status_dict):
    """Atomically write auto-update status to JSON file for dashboard to read."""
    try:
        tmp = STATUS_FILE.with_suffix('.tmp')
        tmp.write_text(json.dumps(status_dict))
        tmp.rename(STATUS_FILE)
    except Exception:
        pass  # Best-effort, don't disrupt downloads


def clear_status():
    """Write idle status (no active downloads)."""
    write_status({"ts": time.time(), "models": {}})


def signal_handler(sig, frame):
    global running
    logger.info("Shutting down...")
    running = False


def get_base_dir(model):
    """Get output directory for a model."""
    return OUTPUTS_BASE / model


def get_latest_cycles(model='hrrr', count=2):
    """Determine the latest N expected cycles based on current UTC time.

    Returns list of (date_str, hour) tuples, newest first.
    """
    registry = get_model_registry()
    model_config = registry.get_model(model)
    if not model_config:
        return []

    now = datetime.now(timezone.utc)
    lag_minutes = MODEL_AVAILABILITY_LAG.get(model, 60)
    latest_possible = now - timedelta(minutes=lag_minutes)

    valid_hours = set(model_config.forecast_cycles)

    cycles = []
    for offset in range(0, 48):  # Look back up to 48 hours (GFS runs only 4x/day)
        cycle_time = latest_possible - timedelta(hours=offset)
        if cycle_time.hour in valid_hours:
            date_str = cycle_time.strftime("%Y%m%d")
            hour = cycle_time.hour
            cycles.append((date_str, hour))
            if len(cycles) >= count:
                break

    return cycles


def get_model_fhrs(model, max_fhr=None):
    """Get the list of FHRs this model should download."""
    fhrs = MODEL_FORECAST_HOURS.get(model, list(range(19)))
    if max_fhr is not None:
        fhrs = [f for f in fhrs if f <= max_fhr]
    return fhrs


def get_downloaded_fhrs(model, date_str, hour, max_fhr=None):
    """Check which forecast hours are already downloaded for a cycle.

    Uses per-model required patterns to determine completeness.
    """
    base_dir = get_base_dir(model)
    run_dir = base_dir / date_str / f"{hour:02d}z"
    patterns = MODEL_REQUIRED_PATTERNS.get(model, ['*.grib2'])

    fhrs_to_check = get_model_fhrs(model, max_fhr)
    downloaded = []
    min_grib_size = 500_000  # 500KB — valid GRIBs are always >1MB
    for fhr in fhrs_to_check:
        fhr_dir = run_dir / f"F{fhr:02d}"
        if not fhr_dir.exists():
            continue
        # All required patterns must have at least one match AND files must be large enough
        all_ok = True
        for p in patterns:
            matches = list(fhr_dir.glob(p))
            if not matches:
                all_ok = False
                break
            # Check that all matched files are above minimum size
            if any(f.stat().st_size < min_grib_size for f in matches):
                all_ok = False
                break
        if all_ok:
            downloaded.append(fhr)
    return downloaded


def get_latest_synoptic_cycle(model='hrrr'):
    """Find the most recent synoptic cycle (00/06/12/18z) that should be available.

    Uses per-model availability lag to determine what's likely published.
    Returns (date_str, hour) or None.
    """
    now = datetime.now(timezone.utc)
    lag = MODEL_AVAILABILITY_LAG.get(model, 50)
    latest_possible = now - timedelta(minutes=lag)

    for offset in range(0, 24):
        cycle_time = latest_possible - timedelta(hours=offset)
        if cycle_time.hour in SYNOPTIC_HOURS:
            return (cycle_time.strftime("%Y%m%d"), cycle_time.hour)
    return None


def download_missing_fhrs(model, date_str, hour, max_hours=18):
    """Download any missing forecast hours for a cycle.

    Returns number of newly downloaded hours.
    """
    from smart_hrrr.orchestrator import download_gribs_parallel
    from smart_hrrr.io import create_output_structure

    target_fhrs = get_model_fhrs(model, max_fhr=max_hours)
    downloaded = get_downloaded_fhrs(model, date_str, hour, max_fhr=max_hours)
    downloaded_set = set(downloaded)
    needed = [f for f in target_fhrs if f not in downloaded_set]

    if not needed:
        return 0

    logger.info(f"[{model.upper()}] Cycle {date_str}/{hour:02d}z: have {len(downloaded)} FHRs, "
                f"need {len(needed)} (F{needed[0]:02d}-F{needed[-1]:02d})")

    # Create output structure
    create_output_structure(model, date_str, hour)

    # Download missing forecast hours
    file_types = MODEL_FILE_TYPES.get(model, ['pressure'])
    results = download_gribs_parallel(
        model=model,
        date_str=date_str,
        cycle_hour=hour,
        forecast_hours=needed,
        max_threads=4,
        file_types=file_types,
    )

    new_count = sum(1 for ok in results.values() if ok)
    if new_count > 0:
        logger.info(f"  [{model.upper()}] Downloaded {new_count}/{len(needed)} new hours for {date_str}/{hour:02d}z")

    return new_count


def get_pending_work(model, max_hours=None):
    """Get list of (date_str, hour, fhr) tuples that need downloading for a model.

    Returns items sorted by cycle (newest first), then FHR ascending.
    """
    if max_hours is None:
        max_hours = MODEL_DEFAULT_MAX_FHR.get(model, 18)

    # Probe multiple recent cycles to find available data.
    # RRFS lag=0 needs more probing (data publishes ~120min after init).
    # Models with longer lags (GFS 180min) already skip stale cycles.
    CYCLES_TO_PROBE = {'rrfs': 4}  # All others default to 2
    n_cycles = CYCLES_TO_PROBE.get(model, 2)
    cycles = get_latest_cycles(model, count=n_cycles)
    if not cycles:
        return []

    # Build per-cycle needed lists
    per_cycle = []  # list of [(date_str, hour, fhr), ...]
    for date_str, hour in cycles:
        target_fhrs = get_model_fhrs(model, max_fhr=max_hours)
        downloaded = set(get_downloaded_fhrs(model, date_str, hour, max_fhr=max_hours))
        needed = [(date_str, hour, f) for f in target_fhrs if f not in downloaded]
        if needed:
            per_cycle.append(needed)

    # Probe-then-focus ordering: interleave only F00 across cycles so parallel
    # slots probe different cycles simultaneously (fail-fast finds available ones
    # in ~1s). After probing, focus all slots on the newest available cycle first.
    # Example: [02z-F00, 01z-F00, 00z-F00, 23z-F00, 01z-F01..F18, 00z-F01..F18, 23z-F01..F18]
    # When 02z-F00 fails → prunes all 02z → both slots focus on 01z until done.
    work = []
    # Phase 1: probe — one F00 per cycle for parallel availability detection
    for cycle_items in per_cycle:
        if cycle_items:
            work.append(cycle_items[0])
    # Phase 2: focus — remaining FHRs grouped by cycle (newest first)
    for cycle_items in per_cycle:
        work.extend(cycle_items[1:])

    # Extended synoptic FHRs: append beyond base range for latest extended cycle
    # Uses model_config to determine which models have extended cycles and their FHR lists
    cfg = get_model_config(model)
    if cfg and cfg.has_extended_cycles():
        syn = get_latest_synoptic_cycle(model)
        if syn:
            syn_date, syn_hour = syn
            ext_fhrs = cfg.get_extended_only_fhrs()
            run_dir = get_base_dir(model) / syn_date / f"{syn_hour:02d}z"
            patterns = MODEL_REQUIRED_PATTERNS.get(model, ['*.grib2'])
            work_set = {(d, h, f) for d, h, f in work}
            for fhr in ext_fhrs:
                fhr_dir = run_dir / f"F{fhr:02d}"
                if fhr_dir.exists() and all(list(fhr_dir.glob(p)) for p in patterns):
                    continue  # Already downloaded
                if (syn_date, syn_hour, fhr) not in work_set:
                    work.append((syn_date, syn_hour, fhr))

    return work


def download_single_fhr(model, date_str, hour, fhr):
    """Download a single forecast hour for a model/cycle.

    Returns True if successfully downloaded, False otherwise.
    """
    from smart_hrrr.orchestrator import download_forecast_hour
    from smart_hrrr.io import create_output_structure, get_forecast_hour_dir

    run_dir = create_output_structure(model, date_str, hour)['run']
    fhr_dir = get_forecast_hour_dir(run_dir, fhr)
    file_types = MODEL_FILE_TYPES.get(model, ['pressure'])
    return download_forecast_hour(
        model=model,
        date_str=date_str,
        cycle_hour=hour,
        forecast_hour=fhr,
        output_dir=fhr_dir,
        file_types=file_types,
    )


DISK_LIMIT_GB = int(os.environ.get('XSECT_DISK_LIMIT_GB', '500'))
DISK_META_FILE = Path(__file__).parent.parent / 'data' / 'disk_meta.json'
# Max date folders to keep per model (e.g. 2 means keep today + yesterday)
MAX_DATE_FOLDERS = int(os.environ.get('XSECT_MAX_DATE_FOLDERS', '3'))

def get_disk_usage_gb(model='hrrr'):
    """Get total disk usage of a model's data directory in GB."""
    base_dir = get_base_dir(model)
    if not base_dir.exists():
        return 0
    total = sum(f.stat().st_size for f in base_dir.rglob("*") if f.is_file())
    return total / (1024 ** 3)

def load_disk_meta():
    if DISK_META_FILE.exists():
        try:
            with open(DISK_META_FILE) as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_disk_meta(meta):
    DISK_META_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DISK_META_FILE, 'w') as f:
        json.dump(meta, f, indent=2)

def cleanup_disk_if_needed(model='hrrr'):
    """Evict least-popular cycles if disk usage exceeds limit.

    Never evicts cycles from the latest 2 init hours or anything accessed
    in the last 2 hours.
    """
    base_dir = get_base_dir(model)
    usage = get_disk_usage_gb(model)
    if usage <= DISK_LIMIT_GB:
        return

    target = DISK_LIMIT_GB * 0.85
    meta = load_disk_meta()
    now = time.time()
    recent_cutoff = now - 7200  # 2 hours

    # Get latest 2 cycle keys (auto-update targets) - never evict these
    latest = get_latest_cycles(model, count=2)
    protected = {f"{d}_{h:02d}z" for d, h in latest}

    disk_cycles = []
    if not base_dir.exists():
        return
    for date_dir in base_dir.iterdir():
        if not date_dir.is_dir() or not date_dir.name.isdigit():
            continue
        for hour_dir in date_dir.iterdir():
            if not hour_dir.is_dir() or not hour_dir.name.endswith('z'):
                continue
            hour = hour_dir.name.replace('z', '')
            cycle_key = f"{date_dir.name}_{hour}z"
            if cycle_key in protected:
                continue
            last_access = meta.get(cycle_key, {}).get('last_accessed', 0)
            if last_access > recent_cutoff:
                continue
            disk_cycles.append((last_access, cycle_key, hour_dir))

    disk_cycles.sort()  # Oldest access first

    for last_access, cycle_key, hour_dir in disk_cycles:
        if get_disk_usage_gb(model) <= target:
            break
        logger.info(f"[{model.upper()}] Disk evict: {cycle_key} (last accessed {int((now - last_access)/3600)}h ago)")
        try:
            shutil.rmtree(hour_dir)
            parent = hour_dir.parent
            if parent.exists() and not any(parent.iterdir()):
                parent.rmdir()
            meta.pop(cycle_key, None)
        except Exception as e:
            logger.warning(f"Evict failed for {cycle_key}: {e}")

    save_disk_meta(meta)


def cleanup_old_date_folders(model='hrrr'):
    """Delete date folders older than MAX_DATE_FOLDERS most recent.

    Simple, aggressive cleanup: if outputs/hrrr/ has 20260205/, 20260206/,
    20260207/, 20260208/ and MAX_DATE_FOLDERS=2, deletes 20260205/ and 20260206/.
    """
    base_dir = get_base_dir(model)
    if not base_dir.exists():
        return
    date_dirs = sorted(
        [d for d in base_dir.iterdir() if d.is_dir() and d.name.isdigit()],
        reverse=True,
    )
    if len(date_dirs) <= MAX_DATE_FOLDERS:
        return
    for old_dir in date_dirs[MAX_DATE_FOLDERS:]:
        try:
            size_gb = sum(f.stat().st_size for f in old_dir.rglob("*") if f.is_file()) / (1024**3)
            shutil.rmtree(old_dir)
            logger.info(f"[{model.upper()}] Deleted old date folder {old_dir.name} ({size_gb:.1f} GB)")
        except Exception as e:
            logger.warning(f"Failed to delete {old_dir}: {e}")


def cleanup_old_extended(model='hrrr'):
    """Keep only 2 most recent synoptic runs with extended FHRs.

    Deletes extended FHR dirs from older synoptic cycles. Uses model_config to
    determine which models have extended cycles and what the extended FHRs are.
    """
    cfg = get_model_config(model)
    if not cfg or not cfg.has_extended_cycles():
        return

    ext_only = cfg.get_extended_only_fhrs()
    if not ext_only:
        return

    base_dir = get_base_dir(model)
    if not base_dir.exists():
        return

    synoptic_with_extended = []
    for date_dir in sorted(base_dir.iterdir(), reverse=True):
        if not date_dir.is_dir() or not date_dir.name.isdigit():
            continue
        for hour_dir in sorted(date_dir.iterdir(), reverse=True):
            if not hour_dir.is_dir() or not hour_dir.name.endswith('z'):
                continue
            hour = int(hour_dir.name.replace('z', ''))
            if not cfg.is_extended_cycle(hour):
                continue
            has_extended = any((hour_dir / f"F{f:02d}").exists() for f in ext_only[:5])
            if has_extended:
                synoptic_with_extended.append(hour_dir)

    # Keep newest 2 with extended data, delete extended FHRs from the rest
    for old_dir in synoptic_with_extended[2:]:
        for fhr in ext_only:
            fhr_dir = old_dir / f"F{fhr:02d}"
            if fhr_dir.exists():
                try:
                    shutil.rmtree(fhr_dir)
                    logger.info(f"Cleaned extended F{fhr:02d} from {old_dir}")
                except Exception as e:
                    logger.warning(f"Failed to clean {fhr_dir}: {e}")


def run_update_cycle_for_model(model, max_hours=None):
    """Run one update pass for a single model.

    Returns total number of newly downloaded FHRs.
    """
    if max_hours is None:
        max_hours = MODEL_DEFAULT_MAX_FHR.get(model, 18)

    cycles = get_latest_cycles(model, count=2)
    if not cycles:
        logger.info(f"[{model.upper()}] No cycles available yet")
        return 0

    total_new = 0
    for date_str, hour in cycles:
        try:
            new_count = download_missing_fhrs(model, date_str, hour, max_hours)
            total_new += new_count
        except Exception as e:
            logger.warning(f"[{model.upper()}] Failed to update {date_str}/{hour:02d}z: {e}")

    # Extended FHRs: download beyond base range for the latest extended cycle
    cfg = get_model_config(model)
    if cfg and cfg.has_extended_cycles():
        ext_fhr_list = cfg.get_extended_only_fhrs()
        max_ext_fhr = cfg.extended_fhr_list[-1] if cfg.extended_fhr_list else 0
        syn = get_latest_synoptic_cycle(model)
        if syn:
            syn_date, syn_hour = syn
            try:
                existing = get_downloaded_fhrs(model, syn_date, syn_hour, max_fhr=max_ext_fhr)
                extended_needed = [f for f in ext_fhr_list if f not in existing]
                if extended_needed:
                    logger.info(f"[{model.upper()}] Extended: {syn_date}/{syn_hour:02d}z needs "
                                f"F{extended_needed[0]:02d}-F{extended_needed[-1]:02d}")
                    new_ext = download_missing_fhrs(model, syn_date, syn_hour, max_hours=max_ext_fhr)
                    total_new += new_ext
            except Exception as e:
                logger.warning(f"[{model.upper()}] Extended download failed for {syn_date}/{syn_hour:02d}z: {e}")

    # Cleanup
    cleanup_disk_if_needed(model)
    cleanup_old_extended(model)

    return total_new


def run_download_pass_concurrent(work_queues, slot_limits, hrrr_max_fhr=None, refresh_intervals=None):
    """Run one concurrent download pass.

    Uses per-model slot limits (e.g., HRRR=3, GFS=1, RRFS=1) so slow RRFS
    transfers no longer block HRRR/GFS progress.
    """
    global running

    # Keep only models with work and at least one slot
    queues = {
        model: deque(items)
        for model, items in work_queues.items()
        if items and slot_limits.get(model, 0) > 0
    }
    if not queues:
        return 0

    active_by_model = {m: 0 for m in slot_limits}
    in_flight = {}
    total_new = 0
    # Per-model queue refresh intervals (seconds). Low values reduce publish-detect latency.
    model_refresh_interval = refresh_intervals or {
        'hrrr': 2, 'gfs': 10, 'rrfs': 2,
        'nam': 10, 'rap': 5, 'nam_nest': 10,
    }
    last_model_refresh = {m: 0.0 for m in slot_limits}
    # Track consecutive all-fail refresh cycles per model. When a model's cycle
    # isn't published yet, back off the refresh interval to avoid hammering NOMADS.
    model_consecutive_fails = {m: 0 for m in slot_limits}
    FAIL_BACKOFF_INTERVAL = 60  # seconds between retries when cycle isn't available

    # Prefer scheduling HRRR first, then others in name order.
    model_order = sorted(slot_limits.keys(), key=lambda m: (m != 'hrrr', m))
    base_slot_limits = dict(slot_limits)  # Save original allocation
    total_workers = sum(max(0, slot_limits.get(m, 0)) for m in model_order)
    if total_workers <= 0:
        return 0

    # ── HRRR-first dynamic slot rebalancing ──
    # When HRRR has fresh work (first 6 FHRs of a new cycle), temporarily steal
    # slots from RRFS/GFS to minimize HRRR first-arrival latency.
    HRRR_PRIORITY_FHRS = 6  # Boost until this many FHRs are downloaded
    hrrr_boost_active = False

    def _rebalance_slots():
        """Check if HRRR needs priority slots and adjust allocation."""
        nonlocal hrrr_boost_active
        hrrr_q = queues.get('hrrr')
        if not hrrr_q:
            if hrrr_boost_active:
                # HRRR queue empty — restore normal slots
                slot_limits.update(base_slot_limits)
                hrrr_boost_active = False
                logger.info(f"[SLOTS] HRRR queue empty — restored normal: {dict(slot_limits)}")
            return

        # Check if HRRR still has early FHRs (F00-F05) in queue
        has_early = any(fhr < HRRR_PRIORITY_FHRS for _, _, fhr in hrrr_q)
        if has_early and not hrrr_boost_active:
            # Steal slots from other models for HRRR
            stolen = 0
            for donor in sorted(m for m in base_slot_limits if m != 'hrrr'):
                give = max(0, base_slot_limits.get(donor, 0) - 1)  # Keep at least 1
                if give > 0:
                    slot_limits[donor] = base_slot_limits[donor] - give
                    stolen += give
            if stolen > 0:
                slot_limits['hrrr'] = base_slot_limits.get('hrrr', 4) + stolen
                hrrr_boost_active = True
                logger.info(f"[SLOTS] HRRR priority boost! {dict(slot_limits)}")
        elif not has_early and hrrr_boost_active:
            # Early FHRs done — restore normal allocation
            slot_limits.update(base_slot_limits)
            hrrr_boost_active = False
            logger.info(f"[SLOTS] HRRR early FHRs done — restored: {dict(slot_limits)}")

    # --- Per-model progress tracking for status file ---
    # Track cycle, totals, completions, in-flight FHRs, and last results per model
    model_status = {}
    for model, items in work_queues.items():
        if items and slot_limits.get(model, 0) > 0:
            # Determine cycle(s) — use the first item's cycle as primary
            d0, h0, _ = items[0]
            model_status[model] = {
                "cycle": f"{d0}/{h0:02d}z",
                "total": len(items),
                "done": 0,
                "in_flight": [],
                "last_ok": None,
                "last_fail": None,
            }
    pass_start = time.time()

    def _flush_status():
        write_status({"ts": time.time(), "started": pass_start, "models": model_status})

    def _update_in_flight():
        """Rebuild in_flight lists from the actual in_flight futures dict."""
        flying = {}
        for fut, (mn, ds, hr, fhr, ts) in in_flight.items():
            flying.setdefault(mn, []).append(f"F{fhr:02d}")
        for m in model_status:
            model_status[m]["in_flight"] = sorted(flying.get(m, []))

    def _drop_if_empty(model_name):
        q = queues.get(model_name)
        if q is not None and not q:
            queues.pop(model_name, None)

    def _schedule(model_name, pool):
        q = queues.get(model_name)
        if not q:
            return

        limit = max(0, slot_limits.get(model_name, 0))
        while running and q and active_by_model.get(model_name, 0) < limit:
            date_str, hour, fhr = q.popleft()
            future = pool.submit(download_single_fhr, model_name, date_str, hour, fhr)
            in_flight[future] = (model_name, date_str, hour, fhr, time.time())
            active_by_model[model_name] = active_by_model.get(model_name, 0) + 1
            logger.info(
                f"[{model_name.upper()}] Downloading {date_str}/{hour:02d}z F{fhr:02d} "
                f"(queued={len(q)}, active={active_by_model[model_name]}/{limit})"
            )
        _drop_if_empty(model_name)

    _flush_status()

    with ThreadPoolExecutor(max_workers=total_workers) as pool:
        while running and (queues or in_flight):
            # Refresh queues for any model whose queue is empty and has no
            # in-flight downloads, so newly published FHRs can start without
            # waiting for the outer loop (which may be blocked by other models).
            for refresh_model in model_order:
                if (
                    slot_limits.get(refresh_model, 0) > 0
                    and refresh_model not in queues
                    and active_by_model.get(refresh_model, 0) == 0
                ):
                    now = time.time()
                    # Use longer interval when cycle isn't available yet (all recent attempts failed)
                    if model_consecutive_fails.get(refresh_model, 0) >= 2:
                        interval = FAIL_BACKOFF_INTERVAL
                    else:
                        interval = model_refresh_interval.get(refresh_model, 120)
                    if now - last_model_refresh.get(refresh_model, 0) >= interval:
                        last_model_refresh[refresh_model] = now
                        mfhr = hrrr_max_fhr if refresh_model == 'hrrr' else None
                        refreshed = get_pending_work(refresh_model, mfhr)
                        if refreshed:
                            queues[refresh_model] = deque(refreshed)
                            logger.info(f"[{refresh_model.upper()}] Refreshed pending queue: {len(refreshed)} FHRs")
                            if refresh_model in model_status:
                                model_status[refresh_model]['total'] += len(refreshed)
                            else:
                                d0, h0, _ = refreshed[0]
                                model_status[refresh_model] = {
                                    "cycle": f"{d0}/{h0:02d}z",
                                    "total": len(refreshed),
                                    "done": 0,
                                    "in_flight": [],
                                    "last_ok": None,
                                    "last_fail": None,
                                }

            _rebalance_slots()
            for model_name in model_order:
                _schedule(model_name, pool)

            _update_in_flight()
            _flush_status()

            if not in_flight:
                break

            done, _ = wait(set(in_flight.keys()), return_when=FIRST_COMPLETED)
            for fut in done:
                model_name, date_str, hour, fhr, start_ts = in_flight.pop(fut)
                active_by_model[model_name] = max(0, active_by_model.get(model_name, 0) - 1)
                dur = time.time() - start_ts

                ok = False
                try:
                    ok = fut.result()
                except Exception as e:
                    logger.warning(f"[{model_name.upper()}] Failed {date_str}/{hour:02d}z F{fhr:02d}: {e}")

                if model_name in model_status:
                    model_status[model_name]["done"] += 1

                if ok:
                    total_new += 1
                    model_consecutive_fails[model_name] = 0  # Reset backoff on success
                    logger.info(f"[{model_name.upper()}] F{fhr:02d} complete ({dur:.1f}s)")
                    if model_name in model_status:
                        model_status[model_name]["last_ok"] = f"F{fhr:02d}"
                else:
                    logger.info(f"[{model_name.upper()}] F{fhr:02d} unavailable/failed ({dur:.1f}s)")
                    if model_name in model_status:
                        model_status[model_name]["last_fail"] = f"F{fhr:02d}"
                    # Fail-fast: if Fxx isn't available, higher FHRs in same cycle
                    # are generally not available either. Prune them and let the
                    # refresh loop retry later when they're published.
                    if model_name in queues:
                        before = len(queues[model_name])
                        queues[model_name] = deque(
                            (d, h, f)
                            for d, h, f in queues[model_name]
                            if not (d == date_str and h == hour and f > fhr)
                        )
                        pruned = before - len(queues[model_name])
                        if pruned > 0:
                            logger.info(
                                f"[{model_name.upper()}] Pruned {pruned} higher FHRs after unavailable "
                                f"{date_str}/{hour:02d}z F{fhr:02d}"
                            )
                            if model_name in model_status:
                                model_status[model_name]['total'] -= pruned
                        _drop_if_empty(model_name)
                    # Track consecutive all-fail rounds for backoff.
                    # If model has no remaining queue and no in-flight, the
                    # cycle isn't available — back off on refresh.
                    if (
                        model_name not in queues
                        and active_by_model.get(model_name, 0) <= 1  # this was the last one
                    ):
                        model_consecutive_fails[model_name] = \
                            model_consecutive_fails.get(model_name, 0) + 1
                        if model_consecutive_fails[model_name] >= 2:
                            logger.info(
                                f"[{model_name.upper()}] Cycle not available — "
                                f"backing off refresh to {FAIL_BACKOFF_INTERVAL}s"
                            )

            _update_in_flight()
            _flush_status()

    clear_status()
    return total_new


def main():
    global running

    parser = argparse.ArgumentParser(description="Multi-Model Auto-Update - Progressive Download")
    parser.add_argument("--models", type=str, default="hrrr",
                        help="Comma-separated models to update (default: hrrr)")
    parser.add_argument("--interval", type=int, default=2,
                        help="Check interval in minutes (default: 2)")
    parser.add_argument("--once", action="store_true", help="Run once and exit")
    parser.add_argument("--max-hours", type=int, default=None,
                        help="Max forecast hours for HRRR (default: per-model)")
    parser.add_argument("--no-cleanup", action="store_true", help="Don't clean up old data")
    parser.add_argument("--hrrr-slots", type=int, default=4,
                        help="Concurrent HRRR FHR downloads (default: 4)")
    parser.add_argument("--gfs-slots", type=int, default=2,
                        help="Concurrent GFS FHR downloads (default: 2)")
    parser.add_argument("--rrfs-slots", type=int, default=4,
                        help="Concurrent RRFS FHR downloads (default: 4)")
    parser.add_argument("--nam-slots", type=int, default=2,
                        help="Concurrent NAM FHR downloads (default: 2)")
    parser.add_argument("--rap-slots", type=int, default=2,
                        help="Concurrent RAP FHR downloads (default: 2)")
    parser.add_argument("--nam-nest-slots", type=int, default=2,
                        help="Concurrent NAM-Nest FHR downloads (default: 2)")
    parser.add_argument("--idle-sleep-seconds", type=int, default=2,
                        help="Idle sleep when up-to-date (default: 2)")
    parser.add_argument("--between-pass-seconds", type=int, default=2,
                        help="Pause between passes (default: 2)")
    parser.add_argument("--hrrr-refresh-seconds", type=int, default=2,
                        help="In-pass queue refresh interval for HRRR (default: 2)")
    parser.add_argument("--gfs-refresh-seconds", type=int, default=10,
                        help="In-pass queue refresh interval for GFS (default: 10)")
    parser.add_argument("--rrfs-refresh-seconds", type=int, default=2,
                        help="In-pass queue refresh interval for RRFS (default: 2)")
    parser.add_argument("--nam-refresh-seconds", type=int, default=10,
                        help="In-pass queue refresh interval for NAM (default: 10)")
    parser.add_argument("--rap-refresh-seconds", type=int, default=5,
                        help="In-pass queue refresh interval for RAP (default: 5)")
    parser.add_argument("--nam-nest-refresh-seconds", type=int, default=10,
                        help="In-pass queue refresh interval for NAM-Nest (default: 10)")

    args = parser.parse_args()
    models = [m.strip().lower() for m in args.models.split(',')]
    slot_limits = {
        'hrrr': max(0, args.hrrr_slots),
        'gfs': max(0, args.gfs_slots),
        'rrfs': max(0, args.rrfs_slots),
        'nam': max(0, args.nam_slots),
        'rap': max(0, args.rap_slots),
        'nam_nest': max(0, args.nam_nest_slots),
    }

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    hrrr_max_fhr = args.max_hours if args.max_hours else None
    refresh_intervals = {
        'hrrr': max(1, args.hrrr_refresh_seconds),
        'gfs': max(1, args.gfs_refresh_seconds),
        'rrfs': max(1, args.rrfs_refresh_seconds),
        'nam': max(1, args.nam_refresh_seconds),
        'rap': max(1, args.rap_refresh_seconds),
        'nam_nest': max(1, args.nam_nest_refresh_seconds),
    }

    logger.info("=" * 60)
    logger.info(f"Multi-Model Auto-Update Service")
    logger.info(f"Models: {', '.join(m.upper() for m in models)}")
    logger.info(f"Legacy check interval: {args.interval} min (compat)")
    logger.info(f"Idle sleep: {args.idle_sleep_seconds}s | Between-pass sleep: {args.between_pass_seconds}s")
    refresh_parts = [f"{m.upper()}={refresh_intervals.get(m, 5)}s" for m in models]
    logger.info(f"Queue refresh: {', '.join(refresh_parts)}")
    for m in models:
        mfhr = args.max_hours if (args.max_hours and m == 'hrrr') else MODEL_DEFAULT_MAX_FHR.get(m, 18)
        slots = slot_limits.get(m, 2)
        logger.info(f"  {m.upper()}: F00-F{mfhr:02d} (base), slots={slots}")
    logger.info("=" * 60)

    if args.once:
        total = 0
        for model in models:
            mfhr = args.max_hours if (args.max_hours and model == 'hrrr') else None
            total += run_update_cycle_for_model(model, mfhr)
        logger.info(f"Downloaded {total} new forecast hours total")
        return

    # --------------- Concurrent slot-based download loop ---------------
    # Each model gets dedicated concurrency slots so slow RRFS/GFS transfers
    # cannot block HRRR progression.

    while running:
        try:
            # Build work queues per model
            work_queues = {}
            for model in models:
                if slot_limits.get(model, 0) <= 0:
                    continue
                mfhr = hrrr_max_fhr if model == 'hrrr' else None
                pending = get_pending_work(model, mfhr)
                if pending:
                    work_queues[model] = pending
                    cycles_str = set(f"{d}/{h:02d}z" for d, h, _ in pending)
                    logger.info(f"[{model.upper()}] Pending: {len(pending)} FHRs across {', '.join(sorted(cycles_str))}")

            if not work_queues:
                logger.info("All models up to date")
                clear_status()
                # Sleep briefly and re-check to keep publish-detect latency low.
                for _ in range(max(1, args.idle_sleep_seconds)):
                    if not running:
                        break
                    time.sleep(1)
                continue

            total_new = run_download_pass_concurrent(
                work_queues=work_queues,
                slot_limits=slot_limits,
                hrrr_max_fhr=hrrr_max_fhr,
                refresh_intervals=refresh_intervals,
            )

            if total_new > 0:
                logger.info(f"Total new downloads this pass: {total_new}")

            # Run cleanup after each pass
            for model in models:
                cleanup_old_date_folders(model)
                cleanup_disk_if_needed(model)
                cleanup_old_extended(model)

        except Exception as e:
            logger.exception(f"Update failed: {e}")

        # Brief pause before re-scanning.
        for _ in range(max(1, args.between_pass_seconds)):
            if not running:
                break
            time.sleep(1)

    clear_status()
    logger.info("Auto-update service stopped")


if __name__ == "__main__":
    # Self-restart wrapper: if main() crashes for any reason, restart immediately.
    # This ensures auto_update never stays down — critical for being first to
    # download new model runs.
    MAX_RESTART_DELAY = 30  # seconds, cap for exponential backoff
    restart_count = 0
    while True:
        try:
            main()
            break  # Clean exit (e.g., --once mode or SIGINT)
        except KeyboardInterrupt:
            logger.info("Interrupted by user — exiting")
            break
        except SystemExit:
            break
        except Exception:
            restart_count += 1
            delay = min(2 ** min(restart_count, 5), MAX_RESTART_DELAY)
            logger.exception(
                f"CRASH #{restart_count} — restarting in {delay}s"
            )
            try:
                clear_status()
            except Exception:
                pass
            time.sleep(delay)
            # Reset the global running flag so main() loop works again
            running = True
            logger.info(f"=== AUTO-RESTART #{restart_count} ===")
            continue
