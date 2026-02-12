"""Classify overnight conditions at each site."""
import sys, io, json, traceback
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.path.insert(0, r'C:\Users\drew\hrrr-maps')

from tools.agent_tools.frontal_analysis import classify_overnight_conditions

SITES = {
    "Woodward OK": (36.43, -99.39),
    "Gage OK": (36.31, -99.76),
    "Elk City OK": (35.41, -99.40),
}

results = {}
for name, (lat, lon) in SITES.items():
    print(f"\n{'='*60}")
    print(f"Classifying overnight conditions at {name} ({lat}, {lon})...")
    print(f"{'='*60}")
    try:
        data = classify_overnight_conditions(lat, lon, model="hrrr", cycle="20260209_18z", base_url="http://localhost:5565")
        results[name] = data
        print(f"  Classification: {data.get('classification', '?')}")
        print(f"  Overnight RH range: {data.get('overnight_rh_range_pct', '?')}%")
        print(f"  Overnight wind range: {data.get('overnight_wind_range_kt', '?')} kt")
        print(f"  Full keys: {list(data.keys())}")
        # Print all key-value pairs
        for k, v in data.items():
            if k not in ('classification', 'overnight_rh_range_pct', 'overnight_wind_range_kt'):
                print(f"  {k}: {json.dumps(v, default=str) if isinstance(v, (dict, list)) else v}")
    except Exception as e:
        print(f"  FAILED: {e}")
        traceback.print_exc()
        results[name] = {"error": str(e)}

with open(r'C:\Users\drew\hrrr-maps\research\ok_prescribed_burn_20260209\data\overnight_raw.json', 'w') as f:
    json.dump(results, f, indent=2, default=str)
print(f"\nSaved raw results to data/overnight_raw.json")
