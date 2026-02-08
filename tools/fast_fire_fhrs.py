#!/usr/bin/env python3
"""Fast parallel download + convert of missing fire event FHRs.

Downloads wrfprs+wrfsfc only (skips 650MB wrfnat). All FHRs across all
events download in parallel. Converts immediately after downloads.
"""
import sys, os, time, logging, socket, urllib.request
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, str(Path(__file__).parent.parent))
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(message)s')
logger = logging.getLogger(__name__)

CACHE_DIR = Path(os.environ.get('XSECT_CACHE_DIR',
                 str(Path(__file__).resolve().parent.parent / 'cache' / 'xsect'))) / 'hrrr'
OUTPUT_DIR = Path(os.environ.get('XSECT_ARCHIVE_DIR', '/mnt/hrrr/hrrr-archive-events'))

# HRRR extended FHRs: pre-2021 only went to F36, 2021+ goes to F48
FHRS_36 = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
FHRS_48 = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

FIRE_EVENTS = [
    ('20200817', 12, FHRS_36), ('20200818', 12, FHRS_36),
    ('20200906', 12, FHRS_36), ('20200907', 18, FHRS_36),
    ('20200908',  0, FHRS_36), ('20200927',  0, FHRS_36),
    ('20201021', 12, FHRS_36), ('20201026',  0, FHRS_36),
    ('20210629', 12, FHRS_48), ('20210804', 12, FHRS_48),
    ('20211230',  6, FHRS_48), ('20220422', 12, FHRS_48),
    ('20220906', 12, FHRS_48), ('20220909', 18, FHRS_48),
    ('20240226', 12, FHRS_48), ('20240227', 12, FHRS_48),
    ('20240725', 12, FHRS_48), ('20250107',  0, FHRS_48),
    ('20250702', 18, FHRS_48), ('20250801', 18, FHRS_48),
]

AWS_URL = "https://noaa-hrrr-bdp-pds.s3.amazonaws.com/hrrr.{date}/conus/hrrr.t{hour:02d}z.{ftype}f{fhr:02d}.grib2"

def download_one_file(date, hour, fhr, ftype_key, ftype_name):
    """Download one GRIB file. Returns True on success."""
    fhr_dir = OUTPUT_DIR / date / f"{hour:02d}z" / f"F{fhr:02d}"
    fhr_dir.mkdir(parents=True, exist_ok=True)
    fname = f"hrrr.t{hour:02d}z.{ftype_name}f{fhr:02d}.grib2"
    dest = fhr_dir / fname
    if dest.exists() and dest.stat().st_size > 1000:
        return True
    url = AWS_URL.format(date=date, hour=hour, ftype=ftype_name, fhr=fhr)
    partial = Path(str(dest) + '.partial')
    try:
        import shutil
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=300) as resp:
            with open(partial, 'wb') as f:
                shutil.copyfileobj(resp, f)
        partial.rename(dest)
        return True
    except Exception:
        partial.unlink(missing_ok=True)
        return False

def download_fhr(date, hour, fhr):
    """Download wrfprs + wrfsfc for one FHR. Returns (date, hour, fhr, ok)."""
    ok_prs = download_one_file(date, hour, fhr, 'pressure', 'wrfprs')
    if not ok_prs:
        return (date, hour, fhr, False)
    ok_sfc = download_one_file(date, hour, fhr, 'surface', 'wrfsfc')
    return (date, hour, fhr, ok_prs and ok_sfc)

def main():
    # Find all missing FHRs across all events
    missing = []
    for date, hour, fhrs in FIRE_EVENTS:
        ck = f"{date}_{hour:02d}z"
        for fhr in fhrs:
            prs_stem = f"hrrr.t{hour:02d}z.wrfprsf{fhr:02d}"
            cache_subdir = CACHE_DIR / f"{ck}_F{fhr:02d}_{prs_stem}"
            if (cache_subdir / '_complete').exists():
                continue
            missing.append((date, hour, fhr))

    logger.info(f"{len(missing)} FHRs to download+convert")
    if not missing:
        logger.info("All cached!")
        return

    # Show per-event summary
    by_event = {}
    for d, h, f in missing:
        by_event.setdefault(f"{d}_{h:02d}z", []).append(f)
    for ck in sorted(by_event):
        fhrs = by_event[ck]
        logger.info(f"  {ck}: {len(fhrs)} — F{',F'.join(f'{f:02d}' for f in fhrs)}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Phase 1: Download ALL FHRs in parallel (8 threads across all events)
    logger.info(f"\n=== Downloading {len(missing)} FHRs (8 threads, wrfprs+wrfsfc) ===")
    dl_start = time.time()
    downloaded = []
    failed_dl = 0

    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(download_fhr, d, h, f): (d, h, f) for d, h, f in missing}
        for i, future in enumerate(as_completed(futures)):
            d, h, f, ok = future.result()
            n = i + 1
            if ok:
                downloaded.append((d, h, f))
                if n % 10 == 0 or n == len(missing):
                    logger.info(f"  [{n}/{len(missing)}] {len(downloaded)} ok, {failed_dl} failed")
            else:
                failed_dl += 1
                logger.info(f"  [{n}/{len(missing)}] FAILED {d}/{h:02d}z/F{f:02d}")

    dl_time = time.time() - dl_start
    logger.info(f"Downloads: {len(downloaded)} ok, {failed_dl} failed ({dl_time:.0f}s)")

    # Symlink all event dates into hrrr-live
    live_base = Path(os.environ.get('XSECT_LIVE_DIR', '/mnt/hrrr/hrrr-live'))
    for date, hour, _ in FIRE_EVENTS:
        live_link = live_base / date
        archive_dir = OUTPUT_DIR / date
        if not live_link.exists() and archive_dir.exists():
            try:
                live_link.symlink_to(archive_dir)
            except OSError:
                pass

    if not downloaded:
        logger.info("No downloads succeeded, skipping conversion")
        return

    # Phase 2: Convert ALL to mmap (4 workers)
    logger.info(f"\n=== Converting {len(downloaded)} FHRs to mmap (4 workers) ===")
    os.environ.setdefault('XSECT_GRIB_BACKEND', 'auto')
    from core.cross_section_interactive import InteractiveCrossSection

    def sfc_resolver(prs_path):
        p = Path(prs_path)
        sfc = p.parent / p.name.replace('wrfprs', 'wrfsfc')
        return str(sfc) if sfc.exists() else prs_path

    xsect = InteractiveCrossSection(
        cache_dir=str(CACHE_DIR),
        grib_backend=os.environ.get('XSECT_GRIB_BACKEND', 'auto'),
        sfc_resolver=sfc_resolver,
    )

    to_convert = []
    for d, h, f in downloaded:
        prs_name = f"hrrr.t{h:02d}z.wrfprsf{f:02d}.grib2"
        prs_path = OUTPUT_DIR / d / f"{h:02d}z" / f"F{f:02d}" / prs_name
        if prs_path.exists():
            to_convert.append((str(prs_path), f, f"{d}/{h:02d}z/F{f:02d}"))

    cv_start = time.time()
    converted = 0
    cv_failed = 0

    def _convert(item):
        path, fhr, label = item
        try:
            return label, xsect.load_forecast_hour(path, fhr)
        except Exception as e:
            logger.error(f"Convert failed {label}: {e}")
            return label, False

    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(_convert, item): item for item in to_convert}
        for i, future in enumerate(as_completed(futures)):
            label, ok = future.result()
            if ok:
                converted += 1
            else:
                cv_failed += 1
            n = i + 1
            if n % 10 == 0 or n == len(to_convert):
                logger.info(f"  [{n}/{len(to_convert)}] {converted} ok, {cv_failed} failed")

    cv_time = time.time() - cv_start
    total_time = time.time() - dl_start
    logger.info(f"\nDone! {len(downloaded)} downloaded ({dl_time:.0f}s) + {converted} converted ({cv_time:.0f}s) = {total_time:.0f}s total")


if __name__ == '__main__':
    main()
