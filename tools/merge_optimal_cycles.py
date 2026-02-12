#!/usr/bin/env python3
"""
Merge optimal cycle recommendations into events.json.

For events where the recommended init cycle changed:
  - Sets optimal_cycle to the new YYYYMMDD_HHz key
  - Updates essential_fhrs, trimmable_fhrs, timing.best_fhrs, timing.buildup_fhrs
  - Adds secondary_cycles array
  - Keeps original key as the event identifier (preserves existing references)

For events where the cycle didn't change:
  - Updates FHR lists from the optimal analysis (may be refined)
  - Adds secondary_cycles if any were recommended
"""

import json
from pathlib import Path

ROOT = Path(r"C:\Users\drew\hrrr-maps")

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  Saved {path}")

def main():
    events = load_json(ROOT / "events.json")
    print(f"Loaded events.json with {len(events)} events")

    # Load all 5 optimal cycle files
    optimal_files = [
        ROOT / "optimal_cycles_fire_ca.json",
        ROOT / "optimal_cycles_fire_other.json",
        ROOT / "optimal_cycles_hurricane.json",
        ROOT / "optimal_cycles_tornado.json",
        ROOT / "optimal_cycles_severe_winter.json",
    ]

    all_recommendations = []
    for f in optimal_files:
        data = load_json(f)
        recs = data.get("events", [])
        all_recommendations.extend(recs)
        print(f"  {f.name}: {len(recs)} events")

    print(f"\nTotal recommendations: {len(all_recommendations)}")

    # Build lookup: original_key -> recommendation
    rec_by_key = {}
    for rec in all_recommendations:
        key = rec["original_key"]
        if key in rec_by_key:
            print(f"  WARNING: duplicate recommendation for {key}")
        rec_by_key[key] = rec

    # Track stats
    changed = 0
    unchanged = 0
    fhr_updated = 0
    secondary_added = 0
    missing = 0
    key_changes = []

    for event_key in list(events.keys()):
        rec = rec_by_key.get(event_key)
        if not rec:
            missing += 1
            continue

        evt = events[event_key]
        recommended_key = rec["recommended_key"]
        is_changed = rec.get("changed", False)

        # Update FHR lists from optimal analysis
        if "essential_fhrs" in rec:
            old_essential = evt.get("essential_fhrs", [])
            evt["essential_fhrs"] = rec["essential_fhrs"]
            if old_essential != rec["essential_fhrs"]:
                fhr_updated += 1

        if "trimmable_fhrs" in rec:
            evt["trimmable_fhrs"] = rec["trimmable_fhrs"]

        # Update timing.best_fhrs and timing.buildup_fhrs
        rec_timing = rec.get("timing", {})
        if "timing" not in evt:
            evt["timing"] = {}

        if "best_fhrs" in rec_timing:
            evt["timing"]["best_fhrs"] = rec_timing["best_fhrs"]
        if "buildup_fhrs" in rec_timing:
            evt["timing"]["buildup_fhrs"] = rec_timing["buildup_fhrs"]

        # Handle cycle change
        if is_changed and recommended_key != event_key:
            evt["optimal_cycle"] = recommended_key
            changed += 1
            key_changes.append(f"  {event_key} -> {recommended_key} ({evt.get('name', '?')})")

            # Update hero_fhr based on new cycle offset
            # Parse old and new cycle hours
            old_hour = int(event_key.split("_")[1].replace("z", ""))
            new_date_part = recommended_key.split("_")[0]
            new_hour = int(recommended_key.split("_")[1].replace("z", ""))
            old_date_part = event_key.split("_")[0]

            # Calculate hour offset (new cycle - old cycle)
            # If dates differ, account for that
            from datetime import datetime
            old_dt = datetime.strptime(f"{old_date_part}{old_hour:02d}", "%Y%m%d%H")
            new_dt = datetime.strptime(f"{new_date_part}{new_hour:02d}", "%Y%m%d%H")
            hour_diff = int((new_dt - old_dt).total_seconds() / 3600)

            # New hero_fhr = old hero_fhr - hour_diff
            old_hero = evt.get("hero_fhr")
            if old_hero is not None:
                new_hero = old_hero - hour_diff
                if new_hero >= 0:
                    evt["hero_fhr"] = new_hero

            # Update best_fhr in suggested_sections too
            if "coordinates" in evt and "suggested_sections" in evt.get("coordinates", {}):
                for section in evt["coordinates"]["suggested_sections"]:
                    if "best_fhr" in section:
                        old_bf = section["best_fhr"]
                        new_bf = old_bf - hour_diff
                        if new_bf >= 0:
                            section["best_fhr"] = new_bf
        else:
            unchanged += 1

        # Add secondary cycles
        sec_cycles = rec.get("secondary_cycles", [])
        if sec_cycles:
            # Normalize secondary cycle format
            normalized = []
            for sc in sec_cycles:
                entry = {}
                # Handle different key names across agent outputs
                entry["cycle"] = sc.get("key") or sc.get("cycle", "")
                entry["rationale"] = sc.get("rationale") or sc.get("reason", "")
                if "fhrs" in sc:
                    entry["fhrs"] = sc["fhrs"]
                if "landfall_fhr" in sc:
                    entry["landfall_fhr"] = sc["landfall_fhr"]
                normalized.append(entry)
            evt["secondary_cycles"] = normalized
            secondary_added += 1

        # Store rationale
        if "rationale" in rec:
            evt["cycle_rationale"] = rec["rationale"]

    print(f"\n=== Merge Results ===")
    print(f"  Changed cycles: {changed}")
    print(f"  Unchanged cycles: {unchanged}")
    print(f"  FHR lists updated: {fhr_updated}")
    print(f"  Secondary cycles added: {secondary_added}")
    print(f"  Events without recommendation: {missing}")

    if key_changes:
        print(f"\n=== Cycle Changes ===")
        for kc in key_changes:
            print(kc)

    # Save updated events.json
    save_json(ROOT / "events.json", events)
    print(f"\nDone! Updated {len(events)} events in events.json")

    # Print summary of all events with optimal_cycle for rebuild script
    print(f"\n=== Events with new optimal cycles ===")
    for key, evt in events.items():
        if "optimal_cycle" in evt:
            print(f"  {key} -> {evt['optimal_cycle']} ({evt.get('name', '?')})")

if __name__ == "__main__":
    main()
