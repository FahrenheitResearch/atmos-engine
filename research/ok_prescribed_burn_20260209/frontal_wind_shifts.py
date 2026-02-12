"""Detect wind shifts at Woodward and Gage OK."""
import sys, io, json, traceback
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.path.insert(0, r'C:\Users\drew\hrrr-maps')

from tools.agent_tools.frontal_analysis import detect_wind_shifts

SITES = {
    "Woodward OK": (36.43, -99.39),
    "Gage OK": (36.31, -99.76),
    "Elk City OK": (35.41, -99.40),
}

results = {}
for name, (lat, lon) in SITES.items():
    print(f"\n{'='*60}")
    print(f"Detecting wind shifts at {name} ({lat}, {lon})...")
    print(f"{'='*60}")
    try:
        data = detect_wind_shifts(lat, lon, model="hrrr", cycle="20260209_18z", base_url="http://localhost:5565")
        results[name] = data
        print(f"\n--- Wind Shifts ---")
        if 'wind_shifts' in data:
            for ws in data['wind_shifts']:
                print(f"  Shift: {json.dumps(ws, indent=2, default=str)}")
        elif 'error' in data:
            print(f"  ERROR: {data['error']}")

        print(f"\n--- Wind Evolution (sample) ---")
        if 'wind_evolution' in data:
            for i, entry in enumerate(data['wind_evolution'][:12]):
                print(f"  FHR {entry.get('fhr', i)}: dir={entry.get('wind_dir_deg','?')}deg spd={entry.get('wind_speed_kt','?')}kt")

        print(f"\n--- RH Evolution (sample) ---")
        if 'rh_evolution' in data:
            for i, entry in enumerate(data['rh_evolution'][:12]):
                print(f"  FHR {entry.get('fhr', i)}: RH={entry.get('rh_pct','?')}%")

        print(f"\n--- Full result keys: {list(data.keys())}")
    except Exception as e:
        print(f"  FAILED: {e}")
        traceback.print_exc()
        results[name] = {"error": str(e)}

# Save raw results
with open(r'C:\Users\drew\hrrr-maps\research\ok_prescribed_burn_20260209\data\wind_shifts_raw.json', 'w') as f:
    json.dump(results, f, indent=2, default=str)
print(f"\nSaved raw results to data/wind_shifts_raw.json")
