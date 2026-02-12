"""Analyze frontal impact on fire behavior at Woodward."""
import sys, io, json, traceback
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.path.insert(0, r'C:\Users\drew\hrrr-maps')

from tools.agent_tools.frontal_analysis import analyze_frontal_impact_on_fires

SITES = {
    "Woodward OK": (36.43, -99.39),
    "Gage OK": (36.31, -99.76),
}

results = {}
for name, (lat, lon) in SITES.items():
    print(f"\n{'='*60}")
    print(f"Analyzing frontal fire impact at {name} ({lat}, {lon})...")
    print(f"{'='*60}")
    try:
        data = analyze_frontal_impact_on_fires(lat, lon, model="hrrr", cycle="20260209_18z", base_url="http://localhost:5565")
        results[name] = data
        print(f"  Current spread: {json.dumps(data.get('current_spread', {}), default=str, indent=2)}")
        print(f"  Post-shift spread: {json.dumps(data.get('post_shift_spread', {}), default=str, indent=2)}")
        print(f"  Tactical window: {json.dumps(data.get('tactical_window', {}), default=str, indent=2)}")
        print(f"  Post-frontal conditions: {json.dumps(data.get('post_frontal_conditions', {}), default=str, indent=2)}")
        print(f"  Full keys: {list(data.keys())}")
        # Print any extra keys
        known = {'current_spread', 'post_shift_spread', 'tactical_window', 'post_frontal_conditions'}
        for k, v in data.items():
            if k not in known:
                print(f"  {k}: {json.dumps(v, default=str, indent=2) if isinstance(v, (dict, list)) else v}")
    except Exception as e:
        print(f"  FAILED: {e}")
        traceback.print_exc()
        results[name] = {"error": str(e)}

with open(r'C:\Users\drew\hrrr-maps\research\ok_prescribed_burn_20260209\data\fire_impact_raw.json', 'w') as f:
    json.dump(results, f, indent=2, default=str)
print(f"\nSaved raw results to data/fire_impact_raw.json")
