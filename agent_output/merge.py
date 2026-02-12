"""Merge agent output files back into events.json.

Each agent writes a JSON file like:
{
  "20181108_00z": {
    "suggested_sections": [... updated sections with markers ...],
    // optionally other fields to update
  },
  ...
}

This script merges the suggested_sections (with markers) back into events.json,
preserving all other fields.
"""
import json
import glob
import os
import shutil
from datetime import datetime

EVENTS_FILE = os.path.join(os.path.dirname(__file__), '..', 'events.json')
OUTPUT_DIR = os.path.dirname(__file__)

def merge():
    # Load current events.json
    with open(EVENTS_FILE, 'r', encoding='utf-8') as f:
        events = json.load(f)

    # Backup
    backup = EVENTS_FILE + f'.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    shutil.copy2(EVENTS_FILE, backup)
    print(f"Backed up to {backup}")

    # Find all agent output files
    pattern = os.path.join(OUTPUT_DIR, 'agent_*.json')
    files = glob.glob(pattern)
    print(f"Found {len(files)} agent output files")

    updated = 0
    errors = []

    for fpath in sorted(files):
        fname = os.path.basename(fpath)
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                agent_data = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            errors.append(f"{fname}: {e}")
            continue

        for cycle_key, updates in agent_data.items():
            if cycle_key not in events:
                errors.append(f"{fname}: Unknown event {cycle_key}")
                continue

            evt = events[cycle_key]

            # Update suggested_sections with markers
            if 'suggested_sections' in updates:
                if 'coordinates' not in evt:
                    evt['coordinates'] = {}
                evt['coordinates']['suggested_sections'] = updates['suggested_sections']
                updated += 1

            # Update other optional fields
            for field in ['hero_fhr', 'hero_product', 'quad_products', 'evaluation_notes']:
                if field in updates:
                    evt[field] = updates[field]

    # Write updated events.json
    with open(EVENTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(events, f, indent=2, ensure_ascii=True)

    print(f"\nMerge complete: {updated} events updated")
    if errors:
        print(f"Errors ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")

    return updated, errors

if __name__ == '__main__':
    merge()
