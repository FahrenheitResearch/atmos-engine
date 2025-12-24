#!/usr/bin/env python3
"""Test interactive map generation with real HRRR data."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from processor_base import HRRRProcessor
from core.interactive_map import create_interactive_map


def main():
    # Find a GRIB file to test with
    outputs_dir = Path("outputs/hrrr")
    grib_files = list(outputs_dir.glob("**/F00/*.grib2"))

    if not grib_files:
        print("No GRIB files found. Run processor first.")
        return

    # Use the first pressure file found
    prs_file = None
    for f in grib_files:
        if "wrfprs" in f.name:
            prs_file = f
            break

    if not prs_file:
        print("No pressure GRIB file found.")
        return

    print(f"Using GRIB file: {prs_file}")

    # Initialize processor
    processor = HRRRProcessor()

    # Load a simple field - 2m temperature
    field_name = "t2m"
    field_config = processor.registry.get_field(field_name)

    if not field_config:
        print(f"Field config not found for {field_name}")
        return

    print(f"Loading {field_name}...")
    data = processor.load_field_data(str(prs_file), field_name, field_config)

    if data is None:
        print("Failed to load data")
        return

    print(f"Data shape: {data.shape}")
    print(f"Data range: {float(data.min()):.1f} to {float(data.max()):.1f}")

    # Create interactive map
    output_dir = Path("outputs/interactive_test")
    print(f"Creating interactive map in {output_dir}...")

    output_path = create_interactive_map(
        data=data,
        field_name=field_name,
        field_config=field_config,
        cycle="20251224_19Z",
        forecast_hour=0,
        output_dir=output_dir,
        colormap=field_config.get('colormap', 'RdBu_r'),
    )

    if output_path:
        print(f"Created: {output_path}")
        print(f"Open in browser: file://{output_path.absolute()}")
    else:
        print("Failed to create interactive map")


if __name__ == "__main__":
    main()
