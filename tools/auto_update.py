#!/usr/bin/env python3
"""
Auto-Update Script for HRRR Dashboard

Monitors for new HRRR cycles and automatically:
1. Downloads the latest data
2. Processes all map products
3. Pre-caches for cross-sections
4. Signals the dashboard to reload

Usage:
    python tools/auto_update.py --interval 15  # Check every 15 minutes
    python tools/auto_update.py --once         # Run once and exit
"""

import argparse
import logging
import sys
import time
import subprocess
import signal
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

# Track current state
current_cycle = None
running = True


def signal_handler(sig, frame):
    global running
    logger.info("Shutting down...")
    running = False


def get_latest_available_cycle():
    """Get the latest available HRRR cycle."""
    try:
        from smart_hrrr.availability import get_latest_cycle
        cycle, cycle_time = get_latest_cycle('hrrr')
        if cycle:
            return cycle, cycle_time
    except Exception as e:
        logger.error(f"Error checking availability: {e}")
    return None, None


def download_cycle(date_str: str, hour: int, forecast_hours: list = None):
    """Download HRRR data for a cycle."""
    if forecast_hours is None:
        forecast_hours = list(range(19))  # F00-F18

    logger.info(f"Downloading {date_str} {hour:02d}Z F00-F{max(forecast_hours):02d}...")

    try:
        from smart_hrrr.downloader import download_grib_parallel

        success = download_grib_parallel(
            model='hrrr',
            date=date_str,
            hour=hour,
            forecast_hours=forecast_hours,
            max_workers=4,
        )

        return success
    except Exception as e:
        logger.error(f"Download failed: {e}")
        return False


def process_cycle(date_str: str, hour: int, forecast_hours: list = None, workers: int = 4):
    """Process map products for a cycle."""
    if forecast_hours is None:
        forecast_hours = list(range(19))

    logger.info(f"Processing maps for {date_str} {hour:02d}Z...")

    try:
        from smart_hrrr.orchestrator import process_model_run

        results = process_model_run(
            model='hrrr',
            date=date_str,
            hour=hour,
            forecast_hours=forecast_hours,
            max_workers=workers,
        )

        successful = sum(1 for r in results if r.get('success'))
        logger.info(f"Processed {successful}/{len(forecast_hours)} hours")
        return successful > 0

    except Exception as e:
        logger.error(f"Processing failed: {e}")
        return False


def precache_xsect(run_dir: str, max_hours: int = 6):
    """Pre-cache cross-section data."""
    logger.info(f"Pre-caching cross-section data...")

    try:
        from core.cross_section_interactive import InteractiveCrossSection

        ixs = InteractiveCrossSection(cache_dir='cache/dashboard/xsect')
        loaded = ixs.load_run(run_dir, max_hours=max_hours, workers=1)

        logger.info(f"Pre-cached {loaded} hours for cross-sections")
        return loaded > 0

    except Exception as e:
        logger.error(f"Pre-cache failed: {e}")
        return False


def run_update_cycle(forecast_hours: list = None, process: bool = True, cache: bool = True):
    """Run a full update cycle."""
    global current_cycle

    # Check for new cycle
    cycle, cycle_time = get_latest_available_cycle()

    if cycle is None:
        logger.warning("No available cycles found")
        return False

    if cycle == current_cycle:
        logger.info(f"Still on cycle {cycle}, no update needed")
        return True

    logger.info(f"New cycle available: {cycle}")
    date_str = cycle_time.strftime("%Y%m%d")
    hour = cycle_time.hour

    # Download
    if not download_cycle(date_str, hour, forecast_hours):
        logger.error("Download failed, skipping this cycle")
        return False

    # Process maps
    if process:
        if not process_cycle(date_str, hour, forecast_hours):
            logger.warning("Processing had errors")

    # Pre-cache cross-sections
    if cache:
        run_dir = f"outputs/hrrr/{date_str}/{hour:02d}z"
        precache_xsect(run_dir, max_hours=min(6, len(forecast_hours or range(19))))

    current_cycle = cycle
    logger.info(f"Update complete for {cycle}")

    return True


def main():
    global running

    parser = argparse.ArgumentParser(description="Auto-Update for HRRR Dashboard")
    parser.add_argument("--interval", type=int, default=15, help="Check interval in minutes")
    parser.add_argument("--once", action="store_true", help="Run once and exit")
    parser.add_argument("--hours", type=str, default="0-18", help="Forecast hours to download")
    parser.add_argument("--no-process", action="store_true", help="Skip map processing")
    parser.add_argument("--no-cache", action="store_true", help="Skip cross-section caching")

    args = parser.parse_args()

    # Parse forecast hours
    if '-' in args.hours:
        start, end = map(int, args.hours.split('-'))
        forecast_hours = list(range(start, end + 1))
    else:
        forecast_hours = [int(h) for h in args.hours.split(',')]

    # Setup signal handler
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    logger.info("=" * 60)
    logger.info("HRRR Auto-Update Service")
    logger.info(f"Interval: {args.interval} minutes")
    logger.info(f"Forecast hours: F{min(forecast_hours):02d}-F{max(forecast_hours):02d}")
    logger.info("=" * 60)

    if args.once:
        run_update_cycle(
            forecast_hours=forecast_hours,
            process=not args.no_process,
            cache=not args.no_cache,
        )
        return

    while running:
        try:
            run_update_cycle(
                forecast_hours=forecast_hours,
                process=not args.no_process,
                cache=not args.no_cache,
            )
        except Exception as e:
            logger.exception(f"Update cycle failed: {e}")

        # Wait for next interval
        logger.info(f"Sleeping for {args.interval} minutes...")
        for _ in range(args.interval * 60):
            if not running:
                break
            time.sleep(1)

    logger.info("Auto-update service stopped")


if __name__ == "__main__":
    main()
