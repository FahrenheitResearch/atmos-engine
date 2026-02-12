"""
Detailed near-surface analysis accounting for terrain.
The southern CRIT has very high terrain (surface pressure ~750-850 hPa).
We need to check conditions at the actual near-surface level more carefully.
"""
import urllib.request
import json
import math
import os

BASE_URL = "http://localhost:5565/api/v1/data"
CYCLE = "20260209_06z"
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

def fetch(product, fhr, transect):
    t = TRANSECTS[transect]
    url = (f"{BASE_URL}?model=hrrr&cycle={CYCLE}&fhr={fhr}&product={product}"
           f"&start_lat={t['start_lat']}&start_lon={t['start_lon']}"
           f"&end_lat={t['end_lat']}&end_lon={t['end_lon']}")
    resp = urllib.request.urlopen(url, timeout=30)
    return json.loads(resp.read())

def get_surface_index(pressures, sp_val):
    best_i = None
    for i, p in enumerate(pressures):
        if p <= sp_val + 5:
            if best_i is None or pressures[i] > pressures[best_i]:
                best_i = i
    return best_i

# Check the actual surface pressure distribution
for tname in ["north", "south"]:
    for fhr in [36, 39, 42]:
        d = fetch("rh", fhr, tname)
        sp = d["surface_pressure_hpa"]
        pressures = d["pressure_levels_hpa"]
        rh = d["rh_pct"]
        lons = d["lons"]
        n_pts = len(lons)

        print(f"\n=== {tname} FHR {fhr} ===")
        print(f"  Surface pressure range: {min(sp):.0f} - {max(sp):.0f} hPa")

        # Get actual near-surface RH (first level at or above surface)
        near_sfc_rh = []
        near_sfc_rh_details = []
        for j in range(n_pts):
            si = get_surface_index(pressures, sp[j])
            if si is not None:
                val = rh[si][j]
                near_sfc_rh.append(val)
                # Also check one level above
                above_val = rh[si+1][j] if si+1 < len(pressures) else None
                near_sfc_rh_details.append({
                    "lon": lons[j],
                    "sp": sp[j],
                    "sfc_level": pressures[si],
                    "rh_sfc": val,
                    "rh_above": above_val
                })

        valid = [v for v in near_sfc_rh if v is not None]
        below_15 = sum(1 for v in valid if v < 15)
        below_20 = sum(1 for v in valid if v < 20)
        below_25 = sum(1 for v in valid if v < 25)
        print(f"  Near-sfc RH: min={min(valid):.1f}%, max={max(valid):.1f}%, mean={sum(valid)/len(valid):.1f}%")
        print(f"  % below 15%: {100*below_15/len(valid):.1f}%")
        print(f"  % below 20%: {100*below_20/len(valid):.1f}%")
        print(f"  % below 25%: {100*below_25/len(valid):.1f}%")

        # Show driest points
        sorted_details = sorted(near_sfc_rh_details, key=lambda x: x["rh_sfc"] if x["rh_sfc"] is not None else 999)
        print(f"  5 driest points:")
        for d_item in sorted_details[:5]:
            print(f"    lon={d_item['lon']:.1f}, sp={d_item['sp']:.0f}hPa, level={d_item['sfc_level']}hPa, RH={d_item['rh_sfc']:.1f}%, RH_above={d_item['rh_above']:.1f}%")

        # Wind
        dw = fetch("wind_speed", fhr, tname)
        u = dw["u_wind_ms"]
        v = dw["v_wind_ms"]
        sp_w = dw["surface_pressure_hpa"]

        sfc_ws = []
        for j in range(n_pts):
            si = get_surface_index(pressures, sp_w[j])
            if si is not None:
                uu = u[si][j]; vv = v[si][j]
                if uu is not None and vv is not None:
                    sfc_ws.append(math.sqrt(uu*uu+vv*vv)*1.94384)
        valid_w = [v for v in sfc_ws if v is not None]
        above_25 = sum(1 for v in valid_w if v > 25)
        print(f"  Near-sfc wind: min={min(valid_w):.1f}kt, max={max(valid_w):.1f}kt, mean={sum(valid_w)/len(valid_w):.1f}kt")
        print(f"  % above 25kt: {100*above_25/len(valid_w):.1f}%")

        # VPD
        dv = fetch("vpd", fhr, tname)
        vpd_data = dv["vpd_hpa"]
        sp_vpd = dv["surface_pressure_hpa"]
        sfc_vpd = []
        for j in range(n_pts):
            si = get_surface_index(pressures, sp_vpd[j])
            if si is not None:
                sfc_vpd.append(vpd_data[si][j])
        valid_vpd = [v for v in sfc_vpd if v is not None]
        above_13 = sum(1 for v in valid_vpd if v > 13)
        above_20 = sum(1 for v in valid_vpd if v > 20)
        print(f"  Near-sfc VPD: min={min(valid_vpd):.1f}, max={max(valid_vpd):.1f}, mean={sum(valid_vpd)/len(valid_vpd):.1f} hPa")
        print(f"  % above 13hPa (extreme): {100*above_13/len(valid_vpd):.1f}%")
        print(f"  % above 20hPa (off-charts): {100*above_20/len(valid_vpd):.1f}%")
