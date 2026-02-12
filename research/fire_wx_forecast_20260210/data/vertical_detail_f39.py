"""
Detailed vertical structure analysis at FHR 39 for both transects.
Focus on the vertical extent of dry/unstable conditions.
"""
import urllib.request
import json
import math
import os

BASE_URL = "http://localhost:5565/api/v1/data"
CYCLE = "20260209_06z"
FHR = 39
OUTDIR = os.path.dirname(os.path.abspath(__file__))

TRANSECTS = {
    "north": {
        "start_lat": 47.0, "start_lon": -113.0,
        "end_lat": 47.0, "end_lon": -103.0
    },
    "south": {
        "start_lat": 35.0, "start_lon": -113.0,
        "end_lat": 35.0, "end_lon": -105.0
    }
}

def fetch(product, transect):
    t = TRANSECTS[transect]
    url = (f"{BASE_URL}?model=hrrr&cycle={CYCLE}&fhr={FHR}&product={product}"
           f"&start_lat={t['start_lat']}&start_lon={t['start_lon']}"
           f"&end_lat={t['end_lat']}&end_lon={t['end_lon']}")
    resp = urllib.request.urlopen(url, timeout=30)
    return json.loads(resp.read())

results = {}

for tname in ["north", "south"]:
    print(f"\n=== {tname.upper()} - Vertical Profile Detail ===")
    res = {}

    d_rh = fetch("rh", tname)
    pressures = d_rh["pressure_levels_hpa"]
    sp = d_rh["surface_pressure_hpa"]
    rh = d_rh["rh_pct"]
    lons = d_rh["lons"]
    n_pts = len(lons)

    # For each pressure level, compute the mean RH across the transect
    # (only for points where that level is above surface)
    level_means_rh = {}
    for i, p in enumerate(pressures):
        if p > 500:  # only below 500 hPa
            vals = []
            for j in range(n_pts):
                if p <= sp[j] + 5 and rh[i][j] is not None:
                    vals.append(rh[i][j])
            if vals:
                level_means_rh[p] = {
                    "mean": round(sum(vals)/len(vals), 1),
                    "min": round(min(vals), 1),
                    "max": round(max(vals), 1),
                    "n_valid": len(vals)
                }

    print("  Pressure | Mean RH | Min RH | Max RH | N")
    for p in sorted(level_means_rh.keys(), reverse=True):
        v = level_means_rh[p]
        flag = " ***DRY***" if v["mean"] < 20 else (" *dry*" if v["mean"] < 30 else "")
        print(f"  {p:7.0f}  | {v['mean']:6.1f}% | {v['min']:6.1f}% | {v['max']:6.1f}% | {v['n_valid']}{flag}")

    res["rh_by_level"] = level_means_rh

    # Lapse rate by level
    d_lr = fetch("lapse_rate", tname)
    lr = d_lr["lapse_rate_c_km"]

    level_means_lr = {}
    for i, p in enumerate(pressures):
        if p > 400:
            vals = []
            for j in range(n_pts):
                if p <= sp[j] + 5 and lr[i][j] is not None:
                    vals.append(lr[i][j])
            if vals:
                level_means_lr[p] = {
                    "mean": round(sum(vals)/len(vals), 2),
                    "min": round(min(vals), 2),
                    "max": round(max(vals), 2)
                }

    print("\n  Pressure | Mean LR  | Min LR   | Max LR")
    for p in sorted(level_means_lr.keys(), reverse=True):
        v = level_means_lr[p]
        flag = " ***UNSTABLE***" if v["mean"] > 8 else (" *steep*" if v["mean"] > 7 else "")
        absflag = " !!!ABSOLUTE!!!" if v["max"] > 9.8 else ""
        print(f"  {p:7.0f}  | {v['mean']:6.2f}   | {v['min']:6.2f}   | {v['max']:6.2f}{flag}{absflag}")

    res["lapse_rate_by_level"] = level_means_lr

    # Temperature profile (for computing 850-500 hPa lapse rate)
    d_t = fetch("temperature", tname)
    temp = d_t["temperature_c"]

    # Compute 850-500 hPa lapse rate
    i850 = next(i for i, p in enumerate(pressures) if abs(p-850) < 2)
    i700 = next(i for i, p in enumerate(pressures) if abs(p-700) < 2)
    i500 = next(i for i, p in enumerate(pressures) if abs(p-500) < 2)

    lapse_850_500 = []
    lapse_850_700 = []
    lapse_700_500 = []
    for j in range(n_pts):
        if sp[j] >= 845:  # 850 hPa must be above surface
            t850 = temp[i850][j]
            t700 = temp[i700][j]
            t500 = temp[i500][j]
            if t850 is not None and t500 is not None:
                # Standard atmosphere: 850 hPa ~ 1500m, 500 hPa ~ 5500m, delta = ~4000m = 4 km
                # 700 hPa ~ 3000m
                lr_val = (t850 - t500) / 4.0  # approximate
                lapse_850_500.append(lr_val)
            if t850 is not None and t700 is not None:
                lr_val = (t850 - t700) / 1.5  # approximate 1.5 km layer
                lapse_850_700.append(lr_val)
            if t700 is not None and t500 is not None:
                lr_val = (t700 - t500) / 2.5
                lapse_700_500.append(lr_val)

    if lapse_850_500:
        res["lapse_850_500_mean"] = round(sum(lapse_850_500)/len(lapse_850_500), 2)
        res["lapse_850_500_max"] = round(max(lapse_850_500), 2)
        print(f"\n  850-500 hPa lapse rate: mean {res['lapse_850_500_mean']:.2f}, max {res['lapse_850_500_max']:.2f} C/km")
    if lapse_850_700:
        res["lapse_850_700_mean"] = round(sum(lapse_850_700)/len(lapse_850_700), 2)
        res["lapse_850_700_max"] = round(max(lapse_850_700), 2)
        print(f"  850-700 hPa lapse rate: mean {res['lapse_850_700_mean']:.2f}, max {res['lapse_850_700_max']:.2f} C/km")
    if lapse_700_500:
        res["lapse_700_500_mean"] = round(sum(lapse_700_500)/len(lapse_700_500), 2)
        res["lapse_700_500_max"] = round(max(lapse_700_500), 2)
        print(f"  700-500 hPa lapse rate: mean {res['lapse_700_500_mean']:.2f}, max {res['lapse_700_500_max']:.2f} C/km")

    # Find the level where mean RH first drops below 20%
    for p in sorted(level_means_rh.keys(), reverse=True):
        if level_means_rh[p]["mean"] < 20:
            res["first_dry_level_hPa"] = p
            print(f"\n  First level with mean RH<20%: {p} hPa")
            break

    results[tname] = res

outpath = os.path.join(OUTDIR, "vertical_detail_f39.json")
with open(outpath, "w") as f:
    json.dump(results, f, indent=2, default=str)
print(f"\nSaved to {outpath}")
