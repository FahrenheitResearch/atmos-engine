#!/usr/bin/env python3
"""
Auto-Update Script for Cross-Section Dashboard (Multi-Model)

Continuously monitors for new model cycles and progressively downloads
forecast hours as they become available on NOAA servers.

Supports HRRR, GFS, and RRFS models.

Usage:
    python tools/auto_update.py                              # Default: HRRR only
    python tools/auto_update.py --models hrrr,gfs            # HRRR + GFS
    python tools/auto_update.py --models hrrr,gfs,rrfs       # All models
    python tools/auto_update.py --interval 3                  # Check every 3 minutes
    python tools/auto_update.py --once                        # Run once and exit
    python tools/auto_update.py --max-hours 18                # Download up to F18 (HRRR)
"""

import argparse
import json
import logging
import sys
import time
import signal
import shutil
from pathlib import Path
from datetime import datetime, timedelta, timezone

sys.path.insert(0, str(Path(__file__).parent.parent))

from model_config import get_model_registry

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

running = True
OUTPUTS_BASE = Path("outputs")

SYNOPTIC_HOURS = {0, 6, 12, 18}

# Per-model: which GRIB file patterns confirm a complete FHR download
MODEL_REQUIRED_PATTERNS = {
    'hrrr': ['*wrfprs*.grib2', '*wrfnat*.grib2'],
    'gfs':  ['*pgrb2.0p25*'],
    'rrfs': ['*prslev*.grib2'],
}

# Per-model: which file_types to request from the orchestrator
MODEL_FILE_TYPES = {
    'hrrr': ['pressure', 'surface', 'native'],  # wrfprs, wrfsfc, wrfnat
    'gfs':  ['pressure'],                        # pgrb2.0p25 (has surface data in it)
    'rrfs': ['pressure'],                        # prslev (has surface data in it)
}

# Per-model: which FHRs to download
MODEL_FORECAST_HOURS = {
    'hrrr': list(range(19)),                          # F00-F18 every hour (synoptic extends to F48)
    'gfs':  list(range(0, 385, 6)),                   # F00-F384 every 6 hours (65 FHRs)
    'rrfs': list(range(19)),                          # F00-F18 every hour
}
MODEL_DEFAULT_MAX_FHR = {
    'hrrr': 18,
    'gfs':  384,
    'rrfs': 18,
}

# Per-model: data availability lag (minutes after init time)
MODEL_AVAILABILITY_LAG = {
    'hrrr': 50,
    'gfs':  240,   # GFS takes ~4 hours to start publishing
    'rrfs': 120,   # RRFS takes ~2 hours
}


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
    for fhr in fhrs_to_check:
        fhr_dir = run_dir / f"F{fhr:02d}"
        if not fhr_dir.exists():
            continue
        # All required patterns must have at least one match
        if all(list(fhr_dir.glob(p)) for p in patterns):
            downloaded.append(fhr)
    return downloaded


def get_latest_synoptic_cycle():
    """Find the most recent synoptic cycle (00/06/12/18z) that should be available.

    Returns (date_str, hour) or None. Only used for HRRR extended forecasts.
    """
    now = datetime.now(timezone.utc)
    latest_possible = now - timedelta(minutes=50)

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

    # HRRR: 2 latest cycles (current + previous for base FHRs)
    # GFS/RRFS: only latest cycle — no handoff
    n_cycles = 2 if model == 'hrrr' else 1
    cycles = get_latest_cycles(model, count=n_cycles)
    if not cycles:
        return []

    work = []
    for date_str, hour in cycles:
        target_fhrs = get_model_fhrs(model, max_fhr=max_hours)
        downloaded = set(get_downloaded_fhrs(model, date_str, hour, max_fhr=max_hours))
        needed = [f for f in target_fhrs if f not in downloaded]
        for fhr in needed:
            work.append((date_str, hour, fhr))

    # Extended HRRR: F19-F48 for latest synoptic cycle (lower priority, appended after base)
    if model == 'hrrr':
        syn = get_latest_synoptic_cycle()
        if syn:
            syn_date, syn_hour = syn
            existing = set(get_downloaded_fhrs(model, syn_date, syn_hour, max_fhr=48))
            # Deduplicate: only add FHRs not already in work list
            work_set = {(d, h, f) for d, h, f in work}
            extended_needed = [f for f in range(19, 49) if f not in existing]
            for fhr in extended_needed:
                if (syn_date, syn_hour, fhr) not in work_set:
                    work.append((syn_date, syn_hour, fhr))

    return work


def download_single_fhr(model, date_str, hour, fhr):
    """Download a single forecast hour for a model/cycle.

    Returns True if successfully downloaded, False otherwise.
    """
    from smart_hrrr.orchestrator import download_gribs_parallel
    from smart_hrrr.io import create_output_structure

    create_output_structure(model, date_str, hour)
    file_types = MODEL_FILE_TYPES.get(model, ['pressure'])
    results = download_gribs_parallel(
        model=model,
        date_str=date_str,
        cycle_hour=hour,
        forecast_hours=[fhr],
        max_threads=4,
        file_types=file_types,
    )
    return results.get(fhr, False)


DISK_LIMIT_GB = 500
DISK_META_FILE = Path(__file__).parent.parent / 'data' / 'disk_meta.json'

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


def cleanup_old_extended(model='hrrr'):
    """Keep only 2 most recent synoptic runs with extended FHRs (F19-F48).

    Only applies to HRRR. Deletes F19+ directories from older synoptic cycles.
    """
    if model != 'hrrr':
        return

    base_dir = get_base_dir(model)
    synoptic_with_extended = []
    if not base_dir.exists():
        return

    for date_dir in sorted(base_dir.iterdir(), reverse=True):
        if not date_dir.is_dir() or not date_dir.name.isdigit():
            continue
        for hour_dir in sorted(date_dir.iterdir(), reverse=True):
            if not hour_dir.is_dir() or not hour_dir.name.endswith('z'):
                continue
            hour = int(hour_dir.name.replace('z', ''))
            if hour not in SYNOPTIC_HOURS:
                continue
            has_extended = any((hour_dir / f"F{f:02d}").exists() for f in range(19, 49))
            if has_extended:
                synoptic_with_extended.append(hour_dir)

    # Keep newest 2 with extended data, delete F19+ from the rest
    for old_dir in synoptic_with_extended[2:]:
        for fhr in range(19, 49):
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

    # Extended HRRR: download F19-F48 for the most recent synoptic cycle
    if model == 'hrrr':
        syn = get_latest_synoptic_cycle()
        if syn:
            syn_date, syn_hour = syn
            try:
                existing = get_downloaded_fhrs(model, syn_date, syn_hour, max_fhr=48)
                extended_needed = [f for f in range(19, 49) if f not in existing]
                if extended_needed:
                    logger.info(f"[HRRR] Extended: {syn_date}/{syn_hour:02d}z needs "
                                f"F{extended_needed[0]:02d}-F{extended_needed[-1]:02d}")
                    new_ext = download_missing_fhrs(model, syn_date, syn_hour, max_hours=48)
                    total_new += new_ext
            except Exception as e:
                logger.warning(f"[HRRR] Extended download failed for {syn_date}/{syn_hour:02d}z: {e}")

    # Cleanup
    cleanup_disk_if_needed(model)
    cleanup_old_extended(model)

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

    args = parser.parse_args()
    models = [m.strip().lower() for m in args.models.split(',')]

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    logger.info("=" * 60)
    logger.info(f"Multi-Model Auto-Update Service")
    logger.info(f"Models: {', '.join(m.upper() for m in models)}")
    logger.info(f"Check interval: {args.interval} min")
    for m in models:
        mfhr = args.max_hours if (args.max_hours and m == 'hrrr') else MODEL_DEFAULT_MAX_FHR.get(m, 18)
        logger.info(f"  {m.upper()}: F00-F{mfhr:02d} (base)")
    logger.info("=" * 60)

    if args.once:
        total = 0
        for model in models:
            mfhr = args.max_hours if (args.max_hours and model == 'hrrr') else None
            total += run_update_cycle_for_model(model, mfhr)
        logger.info(f"Downloaded {total} new forecast hours total")
        return

    # --------------- Interleaved priority download loop ---------------
    # Instead of blocking on each model sequentially, we interleave
    # downloads one FHR at a time with HRRR getting priority:
    #   - Refresh HRRR work queue after every non-HRRR download
    #   - HRRR always goes first when it has pending work
    #   - Other models share remaining bandwidth round-robin
    # This ensures HRRR never waits for slow GFS/RRFS downloads.

    HRRR_BATCH_SIZE = 5  # Download this many HRRR FHRs, then give other models a turn
    hrrr_max_fhr = args.max_hours if args.max_hours else None

    while running:
        try:
            # Build work queues per model
            work_queues = {}
            for model in models:
                mfhr = hrrr_max_fhr if model == 'hrrr' else None
                pending = get_pending_work(model, mfhr)
                if pending:
                    work_queues[model] = pending
                    cycles_str = set(f"{d}/{h:02d}z" for d, h, _ in pending)
                    logger.info(f"[{model.upper()}] Pending: {len(pending)} FHRs across {', '.join(sorted(cycles_str))}")

            if not work_queues:
                logger.info("All models up to date")
                # Sleep and re-check
                for _ in range(args.interval * 60):
                    if not running:
                        break
                    time.sleep(1)
                continue

            total_new = 0
            other_models = [m for m in models if m != 'hrrr']
            other_idx = 0  # Round-robin index for non-HRRR models

            while running and work_queues:
                # --- HRRR batch: download up to N FHRs, then yield to others ---
                if 'hrrr' in work_queues:
                    hrrr_batch = 0
                    while 'hrrr' in work_queues and hrrr_batch < HRRR_BATCH_SIZE and running:
                        date_str, hour, fhr = work_queues['hrrr'].pop(0)
                        logger.info(f"[HRRR] Downloading {date_str}/{hour:02d}z F{fhr:02d} "
                                    f"({len(work_queues['hrrr'])} remaining)")
                        try:
                            ok = download_single_fhr('hrrr', date_str, hour, fhr)
                            if ok:
                                total_new += 1
                            else:
                                # FHR not available yet — skip remaining from this cycle
                                # (higher FHRs won't be available either)
                                logger.info(f"[HRRR] F{fhr:02d} not available, yielding to other models")
                                work_queues['hrrr'] = [
                                    (d, h, f) for d, h, f in work_queues.get('hrrr', [])
                                    if not (d == date_str and h == hour and f > fhr)
                                ]
                                if not work_queues['hrrr']:
                                    del work_queues['hrrr']
                                break  # Yield to GFS/RRFS immediately
                        except Exception as e:
                            logger.warning(f"[HRRR] Failed {date_str}/{hour:02d}z F{fhr:02d}: {e}")
                            break  # Yield on error too
                        hrrr_batch += 1
                        if not work_queues.get('hrrr'):
                            if 'hrrr' in work_queues:
                                del work_queues['hrrr']
                            # Re-check HRRR — new FHRs may have appeared on NOMADS
                            new_hrrr = get_pending_work('hrrr', hrrr_max_fhr)
                            if new_hrrr:
                                work_queues['hrrr'] = new_hrrr
                                logger.info(f"[HRRR] Refreshed: {len(new_hrrr)} new pending FHRs")

                # --- Non-HRRR: one FHR per model (round-robin) ---
                # When HRRR is idle, this runs every iteration = full bandwidth to GFS/RRFS
                has_other_work = False
                if other_models:
                    tried = 0
                    while tried < len(other_models) and running:
                        model = other_models[other_idx % len(other_models)]
                        other_idx += 1
                        tried += 1
                        if model not in work_queues:
                            continue

                        has_other_work = True
                        date_str, hour, fhr = work_queues[model].pop(0)
                        logger.info(f"[{model.upper()}] Downloading {date_str}/{hour:02d}z F{fhr:02d} "
                                    f"({len(work_queues[model])} remaining)")
                        try:
                            ok = download_single_fhr(model, date_str, hour, fhr)
                            if ok:
                                total_new += 1
                        except Exception as e:
                            logger.warning(f"[{model.upper()}] Failed {date_str}/{hour:02d}z F{fhr:02d}: {e}")
                        if not work_queues[model]:
                            del work_queues[model]

                # Nothing left anywhere
                if not work_queues:
                    break

            if total_new > 0:
                logger.info(f"Total new downloads this pass: {total_new}")

            # Run cleanup after each pass
            for model in models:
                cleanup_disk_if_needed(model)
                cleanup_old_extended(model)

        except Exception as e:
            logger.exception(f"Update failed: {e}")

        # Brief pause before re-scanning (much shorter since we're interleaved)
        for _ in range(30):  # 30 seconds between passes
            if not running:
                break
            time.sleep(1)

    logger.info("Auto-update service stopped")


if __name__ == "__main__":
    main()
