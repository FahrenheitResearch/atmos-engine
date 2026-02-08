#!/usr/bin/env python3
"""
Download HRRR archive data for notable weather events (all categories).

Downloads GRIB files from AWS to external HDD. No mmap conversion —
that happens later via "stage to NVMe on demand" when a user requests an event.

Usage:
    # Dry run
    python tools/download_weather_archive.py --dry-run

    # Download all (6 threads, GRIB-only to external HDD)
    python tools/download_weather_archive.py --threads 6

    # Download specific categories
    python tools/download_weather_archive.py --categories hurricane tornado

    # Download specific events by index
    python tools/download_weather_archive.py --events 0 5 12
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

# ─── FHR templates by category ─────────────────────────────────────────────
FHRS_48H_3HR = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]  # 17 FHRs, needs synoptic init
FHRS_12H_1HR = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # 13 FHRs

# ─── Master event list ──────────────────────────────────────────────────────
# Each: (date, hour, fhrs, category, description)
EVENTS = [
    # === HURRICANES (48h @ 3hr) — all synoptic inits ===
    ('20200826', 18, FHRS_48H_3HR, 'hurricane', 'Hurricane Laura Cat 4 — 150mph Cameron LA'),
    ('20200916',  0, FHRS_48H_3HR, 'hurricane', 'Hurricane Sally Cat 2 — stalled, 30in rain'),
    ('20201009', 12, FHRS_48H_3HR, 'hurricane', 'Hurricane Delta Cat 2 — same area as Laura'),
    ('20201028', 12, FHRS_48H_3HR, 'hurricane', 'Hurricane Zeta Cat 3 — fast mover'),
    ('20201108', 18, FHRS_48H_3HR, 'hurricane', 'Tropical Storm Eta — 12th US landfall of 2020'),
    ('20210829',  6, FHRS_48H_3HR, 'hurricane', 'Hurricane Ida Cat 4 — 150mph, Katrina anniversary'),
    ('20210913', 18, FHRS_48H_3HR, 'hurricane', 'Hurricane Nicholas Cat 1 — Houston rain'),
    ('20220928', 12, FHRS_48H_3HR, 'hurricane', 'Hurricane Ian Cat 4 — $110B, near-Cat 5'),
    ('20221110',  0, FHRS_48H_3HR, 'hurricane', 'Hurricane Nicole Cat 1 — rare Nov hurricane'),
    ('20230830',  0, FHRS_48H_3HR, 'hurricane', 'Hurricane Idalia Cat 3 — rapid intensification'),
    ('20230916',  6, FHRS_48H_3HR, 'hurricane', 'Hurricane Lee post-tropical — Maine near-miss'),
    ('20240708',  0, FHRS_48H_3HR, 'hurricane', 'Hurricane Beryl Cat 1 — earliest Cat 5 in history'),
    ('20240805',  0, FHRS_48H_3HR, 'hurricane', 'Hurricane Debby Cat 1 — stalled, 20-30in SC'),
    ('20240926', 18, FHRS_48H_3HR, 'hurricane', 'Hurricane Helene Cat 4 — catastrophic NC flooding'),
    ('20241009', 12, FHRS_48H_3HR, 'hurricane', 'Hurricane Milton Cat 3 — extreme RI to Cat 5'),

    # === TORNADOES (12h @ 1hr) ===
    ('20200303',  3, FHRS_12H_1HR, 'tornado', 'Nashville TN EF3/EF4 — nocturnal, 25 dead'),
    ('20200412', 18, FHRS_12H_1HR, 'tornado', 'Easter 2020 Outbreak — 141 tors, Bassfield EF4'),
    ('20210126',  2, FHRS_12H_1HR, 'tornado', 'Fultondale AL EF3 — nocturnal, 150mph'),
    ('20210325', 15, FHRS_12H_1HR, 'tornado', 'Birmingham/Eagle Point AL EF3 — 80mi track'),
    ('20210327',  1, FHRS_12H_1HR, 'tornado', 'Newnan GA EF4 — nocturnal, 170mph'),
    ('20211211',  0, FHRS_12H_1HR, 'tornado', 'Quad-State Mayfield KY EF4 — 250mi, 57 dead'),
    ('20211210', 23, FHRS_12H_1HR, 'tornado', 'Edwardsville IL Amazon EF3 — 6 dead'),
    ('20220305', 18, FHRS_12H_1HR, 'tornado', 'Winterset IA EF4 — 70mi track, QLCS transition'),
    ('20220429', 22, FHRS_12H_1HR, 'tornado', 'Andover KS EF3 — 155mph, 0 fatalities'),
    ('20230324', 22, FHRS_12H_1HR, 'tornado', 'Rolling Fork MS EF4 — 195mph, 17 dead'),
    ('20230621', 22, FHRS_12H_1HR, 'tornado', 'Matador TX EF3 — small town devastated'),
    ('20231209', 15, FHRS_12H_1HR, 'tornado', 'Dec 2023 TN Outbreak — 39 tors, EF3 Clarksville'),
    ('20240426', 18, FHRS_12H_1HR, 'tornado', 'Elkhorn-Blair NE EF4 — Omaha metro, 170mph'),
    ('20240428',  1, FHRS_12H_1HR, 'tornado', 'Sulphur/Marietta OK EF3-EF4 — first OK violent in 8yr'),
    ('20240506', 23, FHRS_12H_1HR, 'tornado', 'Barnsdall OK EF4 — 180mph, 40mi track'),
    ('20240521', 17, FHRS_12H_1HR, 'tornado', 'Greenfield IA EF4 — DOW 309-318mph, 5 dead'),
    ('20240526',  0, FHRS_12H_1HR, 'tornado', 'Valley View TX EF3 — nocturnal, I-35, 7 dead'),
    ('20250315', 14, FHRS_12H_1HR, 'tornado', 'Kentwood-Carson LA/MS EF4 — 67mi, 6 dead'),
    ('20250516', 17, FHRS_12H_1HR, 'tornado', 'St. Louis MO EF3 — urban, $1.6B, first since 1959'),
    ('20250517',  1, FHRS_12H_1HR, 'tornado', 'Somerset-London KY EF4 — 60mi, 19 dead'),

    # === DERECHOS (12h @ 1hr) ===
    ('20200810', 12, FHRS_12H_1HR, 'derecho', 'Iowa Derecho — $11B, 140mph, costliest tstorm ever'),
    ('20211215', 18, FHRS_12H_1HR, 'derecho', 'December Midwest Derecho — first-ever Dec derecho'),
    ('20220512', 16, FHRS_12H_1HR, 'derecho', 'May SD Derecho — 107mph, haboob'),
    ('20220613', 18, FHRS_12H_1HR, 'derecho', 'Ohio Valley Derecho — 98mph Ft Wayne record'),
    ('20230629', 12, FHRS_12H_1HR, 'derecho', 'June Midwest Derecho — 600mi, 100mph IL'),
    ('20240516', 18, FHRS_12H_1HR, 'derecho', 'Houston Derecho — 100mph downtown, 8 dead'),
    ('20240715', 18, FHRS_12H_1HR, 'derecho', 'July Chicago Derecho — 32 tors, 105mph'),
    ('20250429', 17, FHRS_12H_1HR, 'derecho', 'Pennsylvania Derecho — 120mph, 700mi path'),
    ('20250620', 18, FHRS_12H_1HR, 'derecho', 'N Plains Derecho + Enderlin EF5 — first EF5 since 2013'),
    ('20250728', 18, FHRS_12H_1HR, 'derecho', 'July N Plains Derecho — 99mph Sioux Center'),
    ('20241119', 12, FHRS_12H_1HR, 'derecho', 'PNW Bomb Cyclone — 942mb, 85mph, 600K outages'),

    # === HAIL (12h @ 1hr) ===
    ('20210428', 18, FHRS_12H_1HR, 'hail', 'Hondo TX Record Hail 6.42in — $1.4B'),
    ('20230621', 18, FHRS_12H_1HR, 'hail', 'Red Rocks CO Hail + 36 Tornadoes — CO record'),
    ('20240314', 18, FHRS_12H_1HR, 'hail', 'DFW Hailstorm — record 106 reports of 2in+'),
    ('20240528', 18, FHRS_12H_1HR, 'hail', 'South Plains DVD-Size Hail — 4-5in Lubbock'),
    ('20240531',  0, FHRS_12H_1HR, 'hail', 'Denver Midnight Hail — $1B+, nocturnal'),
    ('20240602', 18, FHRS_12H_1HR, 'hail', 'Vigo Park TX 7in Hail — possible state record'),
    ('20250526', 18, FHRS_12H_1HR, 'hail', 'Menard TX 5.87in Hail — near-record'),

    # === ATMOSPHERIC RIVERS (48h @ 3hr) — all synoptic inits ===
    ('20211114',  0, FHRS_48H_3HR, 'ar', 'PNW AR — Coquihalla Hwy collapse, WA/BC emergency'),
    ('20230104', 12, FHRS_48H_3HR, 'ar', 'CA AR Strongest Storm — 100mph Tahoe, 9 consecutive ARs'),
    ('20230109',  0, FHRS_48H_3HR, 'ar', 'CA AR Peak Flooding — IVT 750-1000, Montecito evac'),
    ('20240204',  6, FHRS_48H_3HR, 'ar', 'Pineapple Express LA — wettest LA day since 2003'),
    ('20251210', 12, FHRS_48H_3HR, 'ar', 'PNW Mega-AR Cat 5 — all-time flood records'),

    # === WINTER STORMS (12h @ 1hr) ===
    ('20210215', 12, FHRS_12H_1HR, 'winter', 'Winter Storm Uri — TX grid near-collapse, 246 dead'),
    ('20221118',  0, FHRS_12H_1HR, 'winter', 'Buffalo Lake Effect 81in — 66in in one day'),
    ('20221223',  6, FHRS_12H_1HR, 'winter', 'Winter Storm Elliott — bomb cyclone, 47 dead Buffalo'),
    ('20250121',  6, FHRS_12H_1HR, 'winter', 'Gulf Coast Blizzard Enzo — 8in snow New Orleans'),
    ('20241107',  0, FHRS_12H_1HR, 'winter', 'Colorado Blizzard — 42in SE CO, 90hr snow'),

    # === OTHER ===
    ('20210628', 12, FHRS_12H_1HR, 'other', 'PNW Heat Dome — Portland 116F, 1400 dead'),
    ('20250704',  0, FHRS_12H_1HR, 'other', 'TX MCV Flooding — Guadalupe R 26ft in 45min, 135 dead'),
]

FILE_TYPES = ['pressure', 'surface', 'native']
OUTPUT_DIR = Path(os.environ.get('XSECT_ARCHIVE_DIR', '/mnt/hrrr/hrrr-archive-events'))


def download_events(events, threads=6, dry_run=False):
    """Download GRIB files for selected events."""
    from tools.bulk_download import download_init, count_existing, estimate_size

    total_fhrs = sum(len(fhrs) for _, _, fhrs, _, _ in events)
    est_gb = total_fhrs * 1.17  # ~1.17 GB per FHR (wrfprs + wrfsfc + wrfnat)

    print("=" * 70)
    print("  HRRR Weather Archive Downloader")
    print("=" * 70)
    print(f"  Events:      {len(events)}")
    print(f"  Total FHRs:  {total_fhrs}")
    print(f"  Est. size:   ~{est_gb:.0f} GB")
    print(f"  Output:      {OUTPUT_DIR}")
    print(f"  Threads:     {threads}")
    print("=" * 70)

    # Category summary
    cats = {}
    for _, _, fhrs, cat, _ in events:
        cats.setdefault(cat, [0, 0])
        cats[cat][0] += 1
        cats[cat][1] += len(fhrs)
    for cat, (n, f) in sorted(cats.items()):
        print(f"  {cat:12s}: {n:2d} events, {f:4d} FHRs, ~{f*1.17:.0f} GB")
    print()

    if dry_run:
        print("Dry run — listing events:")
        for i, (date, hour, fhrs, cat, desc) in enumerate(events):
            existing = count_existing(OUTPUT_DIR, date, hour, fhrs, FILE_TYPES)
            status = f"({existing}/{len(fhrs)} exist)" if existing > 0 else ""
            print(f"  [{i:2d}] {date} {hour:02d}z [{cat:9s}] F00-F{fhrs[-1]:02d} ({len(fhrs)} fhrs) {desc}  {status}")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    overall_start = time.time()
    total_success = 0
    total_skipped = 0
    total_failed = 0

    for i, (date, hour, fhrs, cat, desc) in enumerate(events):
        existing = count_existing(OUTPUT_DIR, date, hour, fhrs, FILE_TYPES)
        label = f"{date} {hour:02d}z"

        if existing == len(fhrs):
            total_skipped += len(fhrs)
            logger.info(f"[{i+1}/{len(events)}] {label} — all {len(fhrs)} FHRs exist, skipping ({desc})")
            continue

        logger.info(f"[{i+1}/{len(events)}] {label} [{cat}] — downloading {len(fhrs)} FHRs ({desc})...")
        cycle_start = time.time()

        success, skipped, failed = download_init(
            OUTPUT_DIR, date, hour, fhrs, FILE_TYPES, threads, aws_only=True
        )

        dur = time.time() - cycle_start
        total_success += success
        total_skipped += skipped
        total_failed += failed
        logger.info(f"  Done: {success} ok, {skipped} skipped, {failed} failed ({dur:.0f}s)")

        # Symlink into hrrr-live so dashboard can find it
        live_link = Path(os.environ.get('XSECT_LIVE_DIR', '/mnt/hrrr/hrrr-live')) / date
        archive_dir = OUTPUT_DIR / date
        if not live_link.exists() and archive_dir.exists():
            try:
                live_link.symlink_to(archive_dir)
                logger.info(f"  Symlinked {date} into hrrr-live")
            except OSError as e:
                logger.warning(f"  Failed to symlink {date}: {e}")

    elapsed = time.time() - overall_start
    hours = elapsed / 3600
    print(f"\nComplete: {total_success} downloaded, {total_skipped} skipped, {total_failed} failed ({hours:.1f}h)")


def main():
    parser = argparse.ArgumentParser(
        description='Download HRRR archive data for notable weather events',
    )
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--threads', type=int, default=6)
    parser.add_argument('--events', type=int, nargs='+',
                        help='Event indices (0-based)')
    parser.add_argument('--categories', nargs='+',
                        help='Filter by category (hurricane, tornado, derecho, hail, ar, winter, other)')
    parser.add_argument('--list', action='store_true')
    args = parser.parse_args()

    selected = EVENTS

    if args.categories:
        selected = [e for e in selected if e[3] in args.categories]

    if args.events is not None:
        selected = [EVENTS[i] for i in args.events if 0 <= i < len(EVENTS)]

    if args.list:
        print("Weather archive events:")
        for i, (date, hour, fhrs, cat, desc) in enumerate(EVENTS):
            marker = "*" if (date, hour, fhrs, cat, desc) in selected else " "
            print(f" {marker}[{i:2d}] {date} {hour:02d}z [{cat:9s}] F00-F{fhrs[-1]:02d} ({len(fhrs):2d} fhrs) {desc}")
        return

    if not selected:
        print("No events selected.")
        return

    download_events(selected, threads=args.threads, dry_run=args.dry_run)


if __name__ == '__main__':
    main()
