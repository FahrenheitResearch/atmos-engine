"""Get hourly point surface conditions at Woodward for FHR 0-8."""
import sys, io, json, traceback
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.path.insert(0, r'C:\Users\drew\hrrr-maps')

from tools.agent_tools.external_data import get_point_surface_conditions

lat, lon = 36.43, -99.39
cycle = "20260209_18z"

print(f"Getting hourly surface conditions at Woodward OK ({lat}, {lon})")
print(f"Cycle: {cycle} (18z = noon CST)")
print(f"FHR 0 = 18z (12:00 CST), FHR 1 = 19z (1:00 PM CST), etc.")
print()

results = []
for fhr in range(0, 13):
    utc_hr = 18 + fhr
    cst_hr = utc_hr - 6
    ampm = "AM" if cst_hr < 12 else "PM"
    display_hr = cst_hr if cst_hr <= 12 else cst_hr - 12
    if display_hr == 0:
        display_hr = 12
    time_str = f"{display_hr}:00 {ampm} CST"
    if cst_hr >= 24:
        cst_hr -= 24
        time_str = f"{cst_hr}:00 AM CST (Feb 10)"

    print(f"FHR {fhr} ({time_str})...", end=" ")
    try:
        data = get_point_surface_conditions(lat, lon, cycle=cycle, fhr=fhr, base_url="http://localhost:5565")
        data['fhr'] = fhr
        data['time_cst'] = time_str
        results.append(data)
        print(f"T={data.get('temperature_c', '?')}C  RH={data.get('rh_pct', '?')}%  "
              f"Wind={data.get('wind_speed_kt', '?')}kt  Td={data.get('dewpoint_c', '?')}C  "
              f"VPD={data.get('vpd_hpa', '?')}hPa")
    except Exception as e:
        print(f"FAILED: {e}")
        results.append({"fhr": fhr, "time_cst": time_str, "error": str(e)})

# Also get Gage and Elk City at a few key hours
print("\n\n--- Gage OK comparison at key hours ---")
gage_results = []
for fhr in [0, 2, 4, 6, 8]:
    utc_hr = 18 + fhr
    cst_hr = utc_hr - 6
    print(f"Gage FHR {fhr} ({cst_hr}:00 CST)...", end=" ")
    try:
        data = get_point_surface_conditions(36.31, -99.76, cycle=cycle, fhr=fhr, base_url="http://localhost:5565")
        data['fhr'] = fhr
        gage_results.append(data)
        print(f"T={data.get('temperature_c', '?')}C  RH={data.get('rh_pct', '?')}%  "
              f"Wind={data.get('wind_speed_kt', '?')}kt")
    except Exception as e:
        print(f"FAILED: {e}")
        gage_results.append({"fhr": fhr, "error": str(e)})

all_results = {
    "woodward_hourly": results,
    "gage_key_hours": gage_results,
}

with open(r'C:\Users\drew\hrrr-maps\research\ok_prescribed_burn_20260209\data\hourly_conditions_raw.json', 'w') as f:
    json.dump(all_results, f, indent=2, default=str)
print(f"\nSaved hourly conditions to data/hourly_conditions_raw.json")
