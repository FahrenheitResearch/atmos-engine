#!/usr/bin/env python
"""
Archive Rebuild: Download all 88 events from AWS, convert to mmap cache with
full surface field extraction, organize by theme on SSDs.

Wipe mode (--wipe) only deletes cache/xsect/hrrr/ directories on the SSDs.
It does NOT format or reformat any drives.

Usage:
    python tools/rebuild_archive.py                       # Process all 88 events
    python tools/rebuild_archive.py --ssd H               # Process only H: drive events
    python tools/rebuild_archive.py --event 20181108_00z   # Process single event
    python tools/rebuild_archive.py --wipe                 # Wipe existing caches first
    python tools/rebuild_archive.py --dry-run              # Show plan without executing
    python tools/rebuild_archive.py --skip-download        # Convert existing GRIBs only
    python tools/rebuild_archive.py --skip-move            # Don't move GRIBs to D:
    python tools/rebuild_archive.py --status               # Show rebuild progress
"""

import sys
import os
import json
import time
import shutil
import logging
import argparse
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
from concurrent.futures.process import BrokenProcessPool
from datetime import datetime

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SSD_ASSIGNMENTS = {
    'H': {
        'drive': 'H:',
        'label': 'Fire Weather',
        'categories': ['fire-ca', 'fire-pnw', 'fire-sw', 'fire-co'],
    },
    'F': {
        'drive': 'F:',
        'label': 'Severe Convective',
        'categories': ['tornado', 'derecho', 'hail'],
    },
    'E': {
        'drive': 'E:',
        'label': 'Tropical + Winter + Other',
        'categories': ['hurricane', 'winter', 'ar', 'bomb_cyclone', 'other'],
    },
}

# Priority order for processing (smallest SSD first)
SSD_ORDER = ['H', 'E', 'F']

GRIB_COLD_STORAGE = Path('D:/hrrr-grib')
EVENTS_FILE = PROJECT_ROOT / 'events.json'
PROGRESS_FILE = PROJECT_ROOT / 'rebuild_progress.json'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
)
logger = logging.getLogger('rebuild')

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def parse_event_key(key):
    """Parse '20181108_00z' -> ('20181108', 0)."""
    parts = key.split('_')
    date_str = parts[0]
    cycle_hour = int(parts[1].replace('z', ''))
    return date_str, cycle_hour


def get_ssd_for_category(category):
    """Return SSD letter for a category, or None if unknown."""
    for letter, info in SSD_ASSIGNMENTS.items():
        if category in info['categories']:
            return letter
    return None


def get_grib_dir(ssd_letter, date_str, cycle_hour):
    """GRIB output directory on SSD: {drive}/hrrr-archive/grib/hrrr/{date}/{HH}z."""
    drive = SSD_ASSIGNMENTS[ssd_letter]['drive']
    return Path(f"{drive}/hrrr-archive/grib/hrrr/{date_str}/{cycle_hour:02d}z")


def get_cache_dir(ssd_letter):
    """Mmap cache directory on SSD: {drive}/hrrr-archive/cache/xsect/hrrr."""
    drive = SSD_ASSIGNMENTS[ssd_letter]['drive']
    return Path(f"{drive}/hrrr-archive/cache/xsect/hrrr")


def load_events(include_secondary=True):
    """Load events.json and build per-event task list.

    Each event produces one primary task using optimal_cycle if present
    (otherwise the event key's cycle). If include_secondary is True,
    secondary_cycles produce additional tasks with their own FHR lists.
    """
    with open(EVENTS_FILE, encoding='utf-8') as f:
        events = json.load(f)

    result = []
    for key, evt in events.items():
        category = evt.get('category', 'other')
        ssd = get_ssd_for_category(category)
        if ssd is None:
            logger.warning(f"Event {key} has unknown category '{category}', assigning to E:")
            ssd = 'E'

        # Full FHR set = essential + trimmable
        essential = evt.get('essential_fhrs') or []
        trimmable = evt.get('trimmable_fhrs') or []
        fhrs = sorted(set(essential + trimmable))

        if not fhrs:
            # Fallback: best_fhrs + buildup_fhrs from timing block
            best = evt.get('timing', {}).get('best_fhrs') or []
            buildup = evt.get('timing', {}).get('buildup_fhrs') or []
            fhrs = sorted(set(best + buildup))

        # Use optimal_cycle if present, otherwise use the event key
        download_key = evt.get('optimal_cycle', key)
        date_str, cycle_hour = parse_event_key(download_key)

        if not fhrs:
            # Last fallback: F00 through cycle's max FHR
            max_fhr = 48 if cycle_hour in (0, 6, 12, 18) else 18
            fhrs = list(range(0, max_fhr + 1))
            logger.info(f"Event {key} has no FHR metadata, using F00-F{max_fhr:02d}")

        display_name = evt.get('name', key)
        if 'optimal_cycle' in evt:
            display_name += f" [cycle: {download_key}]"

        result.append({
            'key': key,
            'name': display_name,
            'category': category,
            'ssd': ssd,
            'date_str': date_str,
            'cycle_hour': cycle_hour,
            'fhrs': fhrs,
            'essential_fhrs': essential,
            'is_secondary': False,
        })

        # Add secondary cycles as separate tasks
        if include_secondary:
            for sc in evt.get('secondary_cycles', []):
                sc_key = sc.get('cycle', '')
                sc_fhrs = sc.get('fhrs', [])
                if not sc_key or not sc_fhrs:
                    continue  # skip if no cycle or no FHRs specified
                sc_date, sc_hour = parse_event_key(sc_key)
                result.append({
                    'key': f"{key}_sec_{sc_key}",
                    'name': f"{evt.get('name', key)} [secondary: {sc_key}]",
                    'category': category,
                    'ssd': ssd,
                    'date_str': sc_date,
                    'cycle_hour': sc_hour,
                    'fhrs': sorted(sc_fhrs),
                    'essential_fhrs': sorted(sc_fhrs),
                    'is_secondary': True,
                })

    # Sort: SSD priority order, then chronological within each SSD
    ssd_rank = {letter: i for i, letter in enumerate(SSD_ORDER)}
    result.sort(key=lambda e: (ssd_rank.get(e['ssd'], 99), e['key']))
    return result


def load_progress():
    """Load rebuild progress from disk."""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {}


def save_progress(progress):
    """Save rebuild progress atomically."""
    tmp = Path(str(PROGRESS_FILE) + '.tmp')
    with open(tmp, 'w') as f:
        json.dump(progress, f, indent=2)
    tmp.replace(PROGRESS_FILE)


# ---------------------------------------------------------------------------
# Phase 0: Wipe caches (NOT drive format!)
# ---------------------------------------------------------------------------


def wipe_caches(ssd_letters=None):
    """Delete cache/xsect/hrrr/ directories on specified SSDs.

    This only removes the mmap cache subdirectories. It does NOT format,
    reformat, or otherwise touch the drive itself.
    """
    if ssd_letters is None:
        ssd_letters = list(SSD_ASSIGNMENTS.keys())

    for letter in ssd_letters:
        cache = get_cache_dir(letter)
        if cache.exists():
            # Measure size before deleting
            total_bytes = 0
            try:
                for f in cache.rglob('*'):
                    if f.is_file():
                        total_bytes += f.stat().st_size
            except Exception:
                pass
            size_gb = total_bytes / (1024 ** 3)
            logger.info(f"Wiping {letter}: {cache} ({size_gb:.1f} GB)")

            # On Windows, mmap-locked files can't be deleted. Track failures
            # and warn instead of crashing -- rebuild will overwrite them.
            skip_count = [0]

            def _on_rm_error(func, path, exc_info):
                # On Windows, mmap-locked files and their parent dirs
                # can't be removed. Skip and let rebuild overwrite them.
                skip_count[0] += 1

            shutil.rmtree(cache, onexc=_on_rm_error)

            if skip_count[0]:
                logger.warning(f"  {skip_count[0]} items locked (mmap?), "
                               f"skipped -- rebuild will overwrite")
            cache.mkdir(parents=True, exist_ok=True)
            logger.info(f"  Done -- {size_gb:.1f} GB freed")
        else:
            cache.mkdir(parents=True, exist_ok=True)
            logger.info(f"  {letter}: cache dir created (was empty)")


# ---------------------------------------------------------------------------
# Phase 1: Download GRIBs from AWS
# ---------------------------------------------------------------------------


def download_event(event, skip_download=False, max_threads=8):
    """Download GRIB files for one event. Returns {fhr: success} dict."""
    os.chdir(PROJECT_ROOT)
    from smart_hrrr.orchestrator import download_gribs_parallel

    grib_dir = get_grib_dir(event['ssd'], event['date_str'], event['cycle_hour'])
    grib_dir.mkdir(parents=True, exist_ok=True)

    if skip_download:
        logger.info(f"  Skipping download (--skip-download)")
        cold_dir = GRIB_COLD_STORAGE / event['date_str'] / f"{event['cycle_hour']:02d}z"
        results = {}
        for fhr in event['fhrs']:
            fhr_dir = grib_dir / f"F{fhr:02d}"
            prs = fhr_dir / f"hrrr.t{event['cycle_hour']:02d}z.wrfprsf{fhr:02d}.grib2"
            cold_prs = cold_dir / f"F{fhr:02d}" / prs.name
            results[fhr] = prs.exists() or cold_prs.exists()
        found = sum(1 for v in results.values() if v)
        logger.info(f"  Found {found}/{len(event['fhrs'])} existing GRIBs")
        return results

    total = len(event['fhrs'])
    completed = [0]

    def on_complete(fhr, ok):
        completed[0] += 1
        status = "OK" if ok else "FAIL"
        done = completed[0]
        bar = '#' * done + '.' * (total - done)
        print(f"\r    Download: [{bar}] {done}/{total} F{fhr:02d} {status}  ",
              end='', flush=True)

    logger.info(f"  Downloading {total} FHRs -> {grib_dir}")

    results = download_gribs_parallel(
        model='hrrr',
        date_str=event['date_str'],
        cycle_hour=event['cycle_hour'],
        forecast_hours=event['fhrs'],
        output_base_dir=grib_dir,
        max_threads=max_threads,
        source_preference=['aws', 'pando', 'nomads'],
        on_complete=on_complete,
    )
    print()  # newline after progress bar

    ok = sum(1 for v in results.values() if v)
    logger.info(f"  Downloaded {ok}/{total} FHRs")
    return results


# ---------------------------------------------------------------------------
# Phase 2: Convert GRIBs to mmap cache
# ---------------------------------------------------------------------------


def _convert_single_fhr(grib_path_str, cache_dir_str, forecast_hour):
    """Convert one FHR from GRIB to mmap cache.  Runs in a subprocess.

    Returns (grib_path, fhr, success, has_surface_fields, message).
    """
    import sys
    from pathlib import Path

    project_root = Path(__file__).resolve().parent.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    os.chdir(project_root)

    from core.cross_section_interactive import InteractiveCrossSection

    xsect = InteractiveCrossSection(
        cache_dir=cache_dir_str,
        grib_backend='auto',
    )
    # Disable cache eviction -- bulk rebuild will exceed the default 1 TB limit
    xsect.CACHE_LIMIT_GB = 10_000

    try:
        success = xsect.load_forecast_hour(grib_path_str, forecast_hour)
    except Exception as e:
        return (grib_path_str, forecast_hour, False, False, str(e))

    if success:
        stem = xsect._get_cache_stem(grib_path_str)
        if stem:
            cache_entry = Path(cache_dir_str) / stem
            has_t2m = (cache_entry / 't2m.npy').exists()
            has_refc = (cache_entry / 'refc.npy').exists()
            if not has_t2m or not has_refc:
                return (grib_path_str, forecast_hour, True, False,
                        "Missing surface fields (t2m/refc)")
            return (grib_path_str, forecast_hour, True, True, "OK")

    return (grib_path_str, forecast_hour, False, False, "Conversion failed")


def convert_event(event, download_results=None, max_workers=8):
    """Convert downloaded GRIBs to mmap cache for one event."""
    grib_dir = get_grib_dir(event['ssd'], event['date_str'], event['cycle_hour'])
    cache_dir = get_cache_dir(event['ssd'])
    cache_dir.mkdir(parents=True, exist_ok=True)

    # Decide which FHRs still need conversion
    fhrs_to_convert = []
    for fhr in event['fhrs']:
        fhr_subdir = grib_dir / f"F{fhr:02d}"
        prs_file = fhr_subdir / f"hrrr.t{event['cycle_hour']:02d}z.wrfprsf{fhr:02d}.grib2"

        if not prs_file.exists():
            # Fallback: check cold storage (D:\hrrr-grib) for already-moved GRIBs
            cold_dir = GRIB_COLD_STORAGE / event['date_str'] / f"{event['cycle_hour']:02d}z"
            cold_prs = cold_dir / f"F{fhr:02d}" / prs_file.name
            if cold_prs.exists():
                prs_file = cold_prs
            else:
                continue  # no GRIB available

        # Already converted with surface fields?
        stem = (f"{event['date_str']}_{event['cycle_hour']:02d}z_F{fhr:02d}"
                f"_hrrr.t{event['cycle_hour']:02d}z.wrfprsf{fhr:02d}")
        cache_entry = cache_dir / stem
        if ((cache_entry / '_complete').exists()
                and (cache_entry / 't2m.npy').exists()
                and (cache_entry / 'refc.npy').exists()):
            continue

        fhrs_to_convert.append((fhr, str(prs_file)))

    if not fhrs_to_convert:
        logger.info(f"  All FHRs already converted with surface fields")
        return []

    total = len(fhrs_to_convert)
    logger.info(f"  Converting {total} FHRs -> {cache_dir}")

    results = []
    completed = [0]
    pool = None
    try:
        pool = ProcessPoolExecutor(max_workers=max_workers)
        futures = {}
        for fhr, grib_path in fhrs_to_convert:
            fut = pool.submit(_convert_single_fhr, grib_path, str(cache_dir), fhr)
            futures[fut] = fhr

        for future in as_completed(futures):
            fhr = futures[future]
            try:
                result = future.result(timeout=600)  # 10 min per FHR
                results.append(result)
                completed[0] += 1
                _, _, success, has_sfc, _ = result
                tag = "OK+sfc" if has_sfc else ("OK" if success else "FAIL")
            except Exception as e:
                completed[0] += 1
                results.append((None, fhr, False, False, str(e)))
                tag = "ERR"

            done = completed[0]
            bar = '#' * done + '.' * (total - done)
            print(f"\r    Convert:  [{bar}] {done}/{total} F{fhr:02d} {tag}   ",
                  end='', flush=True)

    except BrokenProcessPool:
        logger.error("  Worker pool crashed (eccodes segfault?) -- partial results")
    finally:
        if pool:
            pool.shutdown(wait=True, cancel_futures=True)

    print()
    ok = sum(1 for r in results if r[2])
    sfc = sum(1 for r in results if r[3])
    logger.info(f"  Converted {ok}/{total} FHRs ({sfc} with surface fields)")
    return results


# ---------------------------------------------------------------------------
# Phase 3: Move GRIBs to cold storage (D:)
# ---------------------------------------------------------------------------


def move_gribs_to_cold(event, skip_move=False):
    """Move GRIBs from SSD to D:\\hrrr-grib cold storage."""
    if skip_move:
        logger.info(f"  Skipping GRIB move (--skip-move)")
        return True

    grib_dir = get_grib_dir(event['ssd'], event['date_str'], event['cycle_hour'])
    if not grib_dir.exists():
        return True  # nothing to move

    dst = GRIB_COLD_STORAGE / event['date_str'] / f"{event['cycle_hour']:02d}z"

    try:
        dst.mkdir(parents=True, exist_ok=True)

        # Move each FHR sub-directory
        moved_count = 0
        for fhr_dir in sorted(grib_dir.iterdir()):
            if not fhr_dir.is_dir():
                continue
            target = dst / fhr_dir.name
            if target.exists():
                # Merge: move individual files into existing dir
                for f in fhr_dir.iterdir():
                    shutil.move(str(f), str(target / f.name))
                fhr_dir.rmdir()
            else:
                shutil.move(str(fhr_dir), str(target))
            moved_count += 1

        # Remove empty parent dirs on SSD (cycle -> date -> hrrr -> grib)
        for parent in [grib_dir, grib_dir.parent, grib_dir.parent.parent,
                       grib_dir.parent.parent.parent]:
            try:
                parent.rmdir()
            except OSError:
                break  # not empty, stop climbing

        logger.info(f"  Moved {moved_count} FHR dirs -> {dst}")
        return True
    except Exception as e:
        logger.error(f"  Failed to move GRIBs: {e}")
        return False


# ---------------------------------------------------------------------------
# Full per-event pipeline
# ---------------------------------------------------------------------------


def process_event(event, progress, *,
                  skip_download=False, skip_move=False,
                  max_download_threads=8, max_convert_workers=8):
    """Download -> Convert -> Move GRIBs for one event."""
    key = event['key']
    evt_progress = progress.get(key, {})

    if evt_progress.get('status') == 'complete':
        # Verify surface fields are actually complete
        conv = evt_progress.get('converted_fhrs', [])
        sfc = evt_progress.get('surface_fhrs', [])
        if len(sfc) >= len(conv) and len(conv) > 0:
            logger.info(f"  Already complete ({len(sfc)}/{len(conv)} sfc), skipping")
            return
        else:
            logger.info(f"  Incomplete surface fields ({len(sfc)}/{len(conv)}), reconverting")

    start_time = time.time()

    # Phase 1: Download
    evt_progress['status'] = 'downloading'
    progress[key] = evt_progress
    save_progress(progress)

    download_results = download_event(
        event, skip_download=skip_download, max_threads=max_download_threads)
    evt_progress['downloaded_fhrs'] = sorted(
        fhr for fhr, ok in download_results.items() if ok)

    # Phase 2: Convert
    evt_progress['status'] = 'converting'
    save_progress(progress)

    convert_results = convert_event(
        event, download_results, max_workers=max_convert_workers)
    evt_progress['converted_fhrs'] = sorted(r[1] for r in convert_results if r[2])
    evt_progress['surface_fhrs'] = sorted(r[1] for r in convert_results if r[3])

    # Phase 3: Move GRIBs
    evt_progress['status'] = 'moving_gribs'
    save_progress(progress)

    moved = move_gribs_to_cold(event, skip_move=skip_move)
    evt_progress['moved'] = moved

    # Done
    elapsed = time.time() - start_time
    evt_progress['status'] = 'complete'
    evt_progress['completed_at'] = datetime.now().isoformat()
    evt_progress['elapsed_seconds'] = round(elapsed)
    progress[key] = evt_progress
    save_progress(progress)

    logger.info(f"  Complete in {elapsed / 60:.1f} min")


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------


def print_plan(events):
    """Show dry-run plan: event -> SSD mapping, FHR counts, estimated sizes."""
    print("\n=== Archive Rebuild Plan ===\n")

    total_fhrs_all = 0
    for letter in SSD_ORDER:
        info = SSD_ASSIGNMENTS[letter]
        ssd_events = [e for e in events if e['ssd'] == letter]
        if not ssd_events:
            continue
        total_fhrs = sum(len(e['fhrs']) for e in ssd_events)
        total_fhrs_all += total_fhrs
        est_cache_gb = total_fhrs * 2.8
        est_grib_gb = total_fhrs * 1.17

        print(f"SSD {letter}: {info['drive']} -- {info['label']}")
        print(f"  {len(ssd_events)} events, {total_fhrs} FHRs")
        print(f"  ~{est_cache_gb:.0f} GB cache, ~{est_grib_gb:.0f} GB GRIB download\n")

        # Group by category
        cats = {}
        for e in ssd_events:
            cats.setdefault(e['category'], []).append(e)

        for cat, cat_events in cats.items():
            primary = [e for e in cat_events if not e.get('is_secondary')]
            secondary = [e for e in cat_events if e.get('is_secondary')]
            cat_fhrs = sum(len(e['fhrs']) for e in cat_events)
            print(f"  {cat}: {len(primary)} events (+{len(secondary)} secondary), {cat_fhrs} FHRs")
            for e in cat_events:
                fhr_range = f"F{min(e['fhrs']):02d}-F{max(e['fhrs']):02d}"
                tag = " [sec]" if e.get('is_secondary') else ""
                dl_info = f" dl={e['date_str']}_{e['cycle_hour']:02d}z"
                print(f"    {e['key']}{tag} {e['name']} ({len(e['fhrs'])} FHRs: {fhr_range}{dl_info})")
        print()

    print(f"Total: {len(events)} events, {total_fhrs_all} FHRs")
    print(f"Est. cache:    ~{total_fhrs_all * 2.8:.0f} GB")
    print(f"Est. download: ~{total_fhrs_all * 1.17:.0f} GB")
    print(f"Cold storage:  {GRIB_COLD_STORAGE}\n")


def print_status(events, progress):
    """Show current rebuild progress per SSD and event."""
    print("\n=== Rebuild Status ===\n")

    for letter in SSD_ORDER:
        info = SSD_ASSIGNMENTS[letter]
        ssd_events = [e for e in events if e['ssd'] == letter]
        if not ssd_events:
            continue
        complete = sum(1 for e in ssd_events
                       if progress.get(e['key'], {}).get('status') == 'complete')

        print(f"SSD {letter}: {info['drive']} -- {info['label']}")
        print(f"  {complete}/{len(ssd_events)} events complete\n")

        for e in ssd_events:
            p = progress.get(e['key'], {})
            status = p.get('status', 'pending')
            if status == 'complete':
                sfc = len(p.get('surface_fhrs', []))
                mins = p.get('elapsed_seconds', 0) // 60
                print(f"  + {e['key']} {e['name']} ({sfc} sfc, {mins}m)")
            elif status == 'failed':
                print(f"  X {e['key']} {e['name']} (FAILED: {p.get('error', '?')})")
            elif status == 'pending':
                print(f"  . {e['key']} {e['name']} ({len(e['fhrs'])} FHRs)")
            else:
                print(f"  > {e['key']} {e['name']} ({status})")
        print()

    total = len(events)
    done = sum(1 for e in events
               if progress.get(e['key'], {}).get('status') == 'complete')
    failed = sum(1 for e in events
                 if progress.get(e['key'], {}).get('status') == 'failed')
    print(f"Overall: {done}/{total} complete" +
          (f", {failed} failed" if failed else ""))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description='Rebuild archive caches with surface fields',
        epilog='NOTE: --wipe only deletes cache/xsect/hrrr/ dirs, NOT drive reformats!',
    )
    parser.add_argument('--ssd', choices=['H', 'F', 'E'],
                        help='Process only one SSD')
    parser.add_argument('--event',
                        help='Process single event (e.g. 20181108_00z)')
    parser.add_argument('--wipe', action='store_true',
                        help='Delete cache/xsect/hrrr/ dirs before rebuild')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show plan without executing')
    parser.add_argument('--skip-download', action='store_true',
                        help='Convert existing GRIBs only (no AWS download)')
    parser.add_argument('--skip-move', action='store_true',
                        help="Don't move GRIBs to D: cold storage")
    parser.add_argument('--status', action='store_true',
                        help='Show rebuild progress')
    parser.add_argument('--download-threads', type=int, default=8,
                        help='Parallel download threads (default 8)')
    parser.add_argument('--convert-workers', type=int, default=4,
                        help='Parallel GRIB conversion workers (default 4, keep low to avoid eccodes OOM)')
    parser.add_argument('--no-secondary', action='store_true',
                        help='Skip secondary cycles (primary only)')
    args = parser.parse_args()

    # Load events and progress
    events = load_events(include_secondary=not args.no_secondary)
    progress = load_progress()

    if args.status:
        print_status(events, progress)
        return

    # Filter events
    if args.event:
        events = [e for e in events if e['key'] == args.event]
        if not events:
            print(f"Event '{args.event}' not found in events.json")
            return
    elif args.ssd:
        events = [e for e in events if e['ssd'] == args.ssd]

    if args.dry_run:
        print_plan(events)
        return

    # Wipe caches (cache subdirs only -- not a drive format!)
    if args.wipe:
        ssd_letters = [args.ssd] if args.ssd else None
        wipe_caches(ssd_letters)

    # Ensure cold storage dir exists
    if not args.skip_move:
        GRIB_COLD_STORAGE.mkdir(parents=True, exist_ok=True)

    # Process events
    print(f"\n=== Archive Rebuild: {len(events)} events ===")

    for i, event in enumerate(events):
        ssd_info = SSD_ASSIGNMENTS[event['ssd']]
        print(f"\n{'=' * 60}")
        print(f"[{i + 1}/{len(events)}] {event['key']} -- {event['name']}")
        print(f"  SSD {event['ssd']}: {ssd_info['drive']} ({ssd_info['label']})")
        print(f"  Category: {event['category']}")
        print(f"  FHRs: {len(event['fhrs'])} "
              f"(F{min(event['fhrs']):02d}-F{max(event['fhrs']):02d})")

        try:
            process_event(
                event, progress,
                skip_download=args.skip_download,
                skip_move=args.skip_move,
                max_download_threads=args.download_threads,
                max_convert_workers=args.convert_workers,
            )
        except KeyboardInterrupt:
            logger.info("\nInterrupted -- progress saved. Re-run to resume.")
            save_progress(progress)
            sys.exit(1)
        except Exception as e:
            logger.error(f"  Event failed: {e}")
            import traceback
            traceback.print_exc()
            progress.setdefault(event['key'], {})
            progress[event['key']]['status'] = 'failed'
            progress[event['key']]['error'] = str(e)
            save_progress(progress)

    # Final summary
    done = sum(1 for e in events
               if progress.get(e['key'], {}).get('status') == 'complete')
    failed = sum(1 for e in events
                 if progress.get(e['key'], {}).get('status') == 'failed')
    print(f"\n{'=' * 60}")
    print(f"Done: {done}/{len(events)} complete" +
          (f", {failed} failed" if failed else ""))

    if failed:
        print("\nFailed events:")
        for e in events:
            p = progress.get(e['key'], {})
            if p.get('status') == 'failed':
                print(f"  {e['key']} -- {p.get('error', 'unknown')}")


if __name__ == '__main__':
    main()
