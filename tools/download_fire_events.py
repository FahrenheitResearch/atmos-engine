#!/usr/bin/env python3
"""
Download HRRR archive data for notable fire weather events.

Downloads GRIB files from AWS, then converts them to mmap cache for instant
cross-section rendering. Each event gets a single init cycle at 3-hourly FHRs
(F00, F03, F06, F09, F12, F15, F18) with smoke (wrfnat) included.

Usage:
    # Dry run — show what would be downloaded
    python tools/download_fire_events.py --dry-run

    # Download all events (8 threads, AWS)
    python tools/download_fire_events.py

    # Download + convert to mmap cache
    python tools/download_fire_events.py --convert

    # Download specific events by index (0-based)
    python tools/download_fire_events.py --events 0 5 12

    # Skip download, just convert already-downloaded GRIBs to mmap
    python tools/download_fire_events.py --convert-only
"""

import argparse
import logging
import os
import sys
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, str(Path(__file__).parent.parent))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)
logger = logging.getLogger(__name__)

# ─── Fire weather events ────────────────────────────────────────────────────
# Each tuple: (date_YYYYMMDD, init_hour, description)
FIRE_EVENTS = [
    ('20200817', 12, 'CA lightning outbreak / Aug 2020 lightning siege'),
    ('20200818', 12, 'CA lightning-siege rapid expansion day'),
    ('20200906', 12, 'Creek Fire explosive growth / pyroCb'),
    ('20200907', 18, 'Pacific NW Labor Day windstorm onset'),
    ('20200908',  0, 'Pacific NW windstorm continuation / catastrophic spread'),
    ('20200927',  0, 'NorCal Diablo-wind critical fire weather (Glass Fire)'),
    ('20201021', 12, 'CO East Troublesome wind-driven blowup'),
    ('20201026',  0, 'SoCal Santa Ana extreme winds (Silverado/Blue Ridge)'),
    ('20210629', 12, 'Pacific NW heat dome peak'),
    ('20210804', 12, 'Dixie Fire major run into Greenville'),
    ('20211230',  6, 'Marshall Fire downslope windstorm'),
    ('20220422', 12, 'Hermits Peak/Calf Canyon extreme fire weather'),
    ('20220906', 12, 'CA extreme heat wave + Mosquito Fire start'),
    ('20220909', 18, 'OR east-wind Red Flag day (Cedar Creek)'),
    ('20240226', 12, 'TX Panhandle Smokehouse Creek ignition'),
    ('20240227', 12, 'TX Panhandle continued wind-driven growth'),
    ('20240725', 12, 'Park Fire first full burn period'),
    ('20250107',  0, 'LA-area Santa Ana outbreak (Palisades/Eaton)'),
    ('20250702', 18, 'Madre Fire onset + explosive growth'),
    ('20250801', 18, 'Gifford Fire ignition (large 2025 CA fire)'),
]

FHRS = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
FILE_TYPES = ['pressure', 'surface', 'native']  # native = wrfnat for smoke
OUTPUT_DIR = Path(os.environ.get('XSECT_ARCHIVE_DIR', '/mnt/hrrr/hrrr-archive-events'))
CACHE_DIR = Path(os.environ.get('XSECT_CACHE_DIR',
                 str(Path(__file__).resolve().parent.parent / 'cache' / 'xsect'))) / 'hrrr'


def download_events(events, threads=8, dry_run=False):
    """Download GRIB files for selected events."""
    from tools.bulk_download import download_init, count_existing, estimate_size

    total_fhrs = len(events) * len(FHRS)
    est_gb = estimate_size(total_fhrs, include_smoke=True)

    print("=" * 70)
    print("  HRRR Fire Weather Archive Downloader")
    print("=" * 70)
    print(f"  Events:      {len(events)}")
    print(f"  FHRs/event:  {', '.join(f'F{f:02d}' for f in FHRS)} ({len(FHRS)} per event)")
    print(f"  File types:  {', '.join(FILE_TYPES)} (includes smoke)")
    print(f"  Output:      {OUTPUT_DIR}")
    print(f"  Threads:     {threads}")
    print(f"  Total FHRs:  {total_fhrs}")
    print(f"  Est. size:   ~{est_gb:.1f} GB")
    print("=" * 70)

    if dry_run:
        print("\nDry run — listing events:")
        for i, (date, hour, desc) in enumerate(events):
            existing = count_existing(OUTPUT_DIR, date, hour, FHRS, FILE_TYPES)
            status = f"({existing}/{len(FHRS)} exist)" if existing > 0 else ""
            print(f"  [{i:2d}] {date} {hour:02d}z  {desc}  {status}")
        print(f"\nTotal estimated: ~{est_gb:.1f} GB")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    overall_start = time.time()
    total_success = 0
    total_skipped = 0
    total_failed = 0

    for i, (date, hour, desc) in enumerate(events):
        existing = count_existing(OUTPUT_DIR, date, hour, FHRS, FILE_TYPES)
        label = f"{date} {hour:02d}z"

        if existing == len(FHRS):
            total_skipped += len(FHRS)
            logger.info(f"[{i+1}/{len(events)}] {label} — all FHRs exist, skipping ({desc})")
            continue

        logger.info(f"[{i+1}/{len(events)}] {label} — downloading ({desc})...")
        cycle_start = time.time()

        success, skipped, failed = download_init(
            OUTPUT_DIR, date, hour, FHRS, FILE_TYPES, threads, aws_only=True
        )

        dur = time.time() - cycle_start
        total_success += success
        total_skipped += skipped
        total_failed += failed
        logger.info(f"  Done: {success} ok, {skipped} skipped, {failed} failed ({dur:.0f}s)")

        # Auto-symlink into hrrr-live so dashboard can find it
        live_link = Path(os.environ.get('XSECT_LIVE_DIR', '/mnt/hrrr/hrrr-live')) / date
        archive_dir = OUTPUT_DIR / date
        if not live_link.exists() and archive_dir.exists():
            try:
                live_link.symlink_to(archive_dir)
                logger.info(f"  Symlinked {date} into hrrr-live")
            except OSError as e:
                logger.warning(f"  Failed to symlink {date}: {e}")

    elapsed = time.time() - overall_start
    print(f"\nComplete: {total_success} downloaded, {total_skipped} skipped, {total_failed} failed ({elapsed:.0f}s)")
    return total_failed == 0


def convert_events(events, workers=4):
    """Convert downloaded GRIBs to mmap cache for instant loading."""
    from core.cross_section_interactive import InteractiveCrossSection
    from pathlib import Path as P
    import os

    grib_backend = os.environ.get('XSECT_GRIB_BACKEND', 'auto')

    # Resolvers: given a wrfprs path, find the matching wrfsfc/wrfnat in same dir
    def sfc_resolver(prs_path):
        p = P(prs_path)
        sfc = p.parent / p.name.replace('wrfprs', 'wrfsfc')
        return str(sfc) if sfc.exists() else prs_path

    def nat_resolver(prs_path):
        p = P(prs_path)
        nat = p.parent / p.name.replace('wrfprs', 'wrfnat')
        return str(nat) if nat.exists() else None

    ixs = InteractiveCrossSection(
        cache_dir=str(CACHE_DIR),
        grib_backend=grib_backend,
        sfc_resolver=sfc_resolver,
        nat_resolver=nat_resolver,
    )

    # Build list of (grib_path, fhr, label) for all events
    from model_config import get_model_registry
    registry = get_model_registry()
    model = registry.get_model('hrrr')

    to_convert = []
    already_cached = 0

    for date, hour, desc in events:
        for fhr in FHRS:
            # Check if mmap cache already exists
            cycle_key = f"{date}_{hour:02d}z"
            prs_filename = model.get_filename(hour, 'pressure', fhr)
            cache_subdir = CACHE_DIR / f"{cycle_key}_F{fhr:02d}_{prs_filename}"

            if (cache_subdir / '_complete').exists():
                already_cached += 1
                continue

            # Check if GRIB exists
            fhr_dir = OUTPUT_DIR / date / f"{hour:02d}z" / f"F{fhr:02d}"
            prs_path = fhr_dir / prs_filename
            if not prs_path.exists():
                logger.warning(f"  GRIB not found: {prs_path}")
                continue

            to_convert.append((
                str(prs_path),
                fhr,
                f"{date} {hour:02d}z F{fhr:02d} ({desc})",
            ))

    total = len(to_convert) + already_cached
    print(f"\nMmap conversion: {len(to_convert)} to convert, {already_cached} already cached ({total} total)")

    if not to_convert:
        print("Nothing to convert.")
        return

    converted = 0
    failed = 0
    start = time.time()

    def _convert_one(item):
        prs_path, fhr, label = item
        try:
            ok = ixs.load_forecast_hour(prs_path, fhr)
            return label, ok
        except Exception as e:
            logger.error(f"  Failed {label}: {e}")
            return label, False

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(_convert_one, item): item for item in to_convert}
        for future in as_completed(futures):
            label, ok = future.result()
            if ok:
                converted += 1
                logger.info(f"  [{converted + failed}/{len(to_convert)}] Converted {label}")
            else:
                failed += 1
                logger.warning(f"  [{converted + failed}/{len(to_convert)}] FAILED {label}")

    elapsed = time.time() - start
    print(f"\nConversion complete: {converted} ok, {failed} failed ({elapsed:.0f}s)")


def main():
    parser = argparse.ArgumentParser(
        description='Download HRRR archive data for notable fire weather events',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would be downloaded without downloading')
    parser.add_argument('--convert', action='store_true',
                        help='Also convert downloaded GRIBs to mmap cache after download')
    parser.add_argument('--convert-only', action='store_true',
                        help='Skip download, just convert existing GRIBs to mmap cache')
    parser.add_argument('--events', type=int, nargs='+',
                        help='Event indices to process (0-based, default: all)')
    parser.add_argument('--threads', type=int, default=8,
                        help='Download threads (default: 8)')
    parser.add_argument('--grib-workers', type=int, default=4,
                        help='GRIB-to-mmap conversion workers (default: 4)')
    parser.add_argument('--list', action='store_true',
                        help='List all events with indices')
    args = parser.parse_args()

    if args.list:
        print("Fire weather events:")
        for i, (date, hour, desc) in enumerate(FIRE_EVENTS):
            print(f"  [{i:2d}] {date} {hour:02d}z  {desc}")
        return

    # Select events
    if args.events is not None:
        events = [FIRE_EVENTS[i] for i in args.events if 0 <= i < len(FIRE_EVENTS)]
    else:
        events = FIRE_EVENTS

    if args.convert_only:
        convert_events(events, workers=args.grib_workers)
        return

    if not args.dry_run:
        ok = download_events(events, threads=args.threads)
    else:
        download_events(events, dry_run=True)
        return

    if args.convert:
        convert_events(events, workers=args.grib_workers)


if __name__ == '__main__':
    main()
