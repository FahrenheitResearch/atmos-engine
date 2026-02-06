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

# Per-model: default max FHR for non-synoptic cycles
MODEL_DEFAULT_MAX_FHR = {
    'hrrr': 18,
    'gfs':  48,   # We only grab first 48h for cross-sections (full run is 384h)
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


def get_latest_two_cycles(model='hrrr'):
    """Determine the latest 2 expected cycles based on current UTC time.

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
            if len(cycles) >= 2:
                break

    return cycles


def get_downloaded_fhrs(model, date_str, hour, max_fhr=18):
    """Check which forecast hours are already downloaded for a cycle.

    Uses per-model required patterns to determine completeness.
    """
    base_dir = get_base_dir(model)
    run_dir = base_dir / date_str / f"{hour:02d}z"
    patterns = MODEL_REQUIRED_PATTERNS.get(model, ['*.grib2'])

    downloaded = []
    for fhr in range(max_fhr + 1):
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

    downloaded = get_downloaded_fhrs(model, date_str, hour, max_fhr=max_hours)
    needed = [f for f in range(max_hours + 1) if f not in downloaded]

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
    latest = get_latest_two_cycles(model)
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

    cycles = get_latest_two_cycles(model)
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

    while running:
        try:
            total_new = 0
            for model in models:
                cycles = get_latest_two_cycles(model)
                if cycles:
                    logger.info(f"[{model.upper()}] Tracking: {', '.join(f'{d}/{h:02d}z' for d, h in cycles)}")

                mfhr = args.max_hours if (args.max_hours and model == 'hrrr') else None
                new = run_update_cycle_for_model(model, mfhr)
                total_new += new

            if total_new > 0:
                logger.info(f"Total new downloads this pass: {total_new}")
            else:
                logger.info("All models up to date")

        except Exception as e:
            logger.exception(f"Update failed: {e}")

        # Sleep in 1-second increments so we can respond to signals
        for _ in range(args.interval * 60):
            if not running:
                break
            time.sleep(1)

    logger.info("Auto-update service stopped")


if __name__ == "__main__":
    main()
