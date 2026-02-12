"""
Task 2 & 3: Fire Weather Threshold Analysis at FHR 39 and Regional Comparison.
Also fetch lapse_rate and omega for comparison table.
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
        "label": "Northern CRIT (MT)",
        "start_lat": 47.0, "start_lon": -113.0,
        "end_lat": 47.0, "end_lon": -103.0
    },
    "south": {
        "label": "Southern CRIT (AZ/NM)",
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

def compute_wind_speed_2d(u_arr, v_arr):
    """m/s to knots, 2D"""
    result = []
    for i in range(len(u_arr)):
        row = []
        for j in range(len(u_arr[i])):
            u = u_arr[i][j]; v = v_arr[i][j]
            if u is not None and v is not None:
                row.append(math.sqrt(u*u + v*v) * 1.94384)
            else:
                row.append(None)
        result.append(row)
    return result

def get_surface_index(pressures, sp_val):
    """Find highest pressure level <= surface pressure + tolerance."""
    best_i = None
    for i, p in enumerate(pressures):
        if p <= sp_val + 5:
            if best_i is None or pressures[i] > pressures[best_i]:
                best_i = i
    return best_i

results = {}

for tname in ["north", "south"]:
    print(f"\n=== {tname.upper()} transect, FHR {FHR} ===")
    res = {"label": TRANSECTS[tname]["label"]}

    # --- RH ---
    d_rh = fetch("rh", tname)
    pressures = d_rh["pressure_levels_hpa"]
    sp = d_rh["surface_pressure_hpa"]
    rh = d_rh["rh_pct"]
    dists = d_rh["distances_km"]
    lons = d_rh["lons"]
    n_pts = len(dists)

    # Surface RH for each point
    sfc_rh = []
    for j in range(n_pts):
        si = get_surface_index(pressures, sp[j])
        if si is not None:
            sfc_rh.append(rh[si][j])
        else:
            sfc_rh.append(None)

    # % of transect with RH < 15% (Red Flag)
    valid_rh = [v for v in sfc_rh if v is not None]
    rh_below_15 = sum(1 for v in valid_rh if v < 15)
    pct_rh_red_flag = round(100.0 * rh_below_15 / len(valid_rh), 1) if valid_rh else 0
    rh_below_8 = sum(1 for v in valid_rh if v < 8)
    pct_rh_extreme = round(100.0 * rh_below_8 / len(valid_rh), 1) if valid_rh else 0
    min_sfc_rh = min(v for v in valid_rh) if valid_rh else None
    mean_sfc_rh = round(sum(valid_rh)/len(valid_rh), 2) if valid_rh else None

    res["sfc_rh_min"] = round(min_sfc_rh, 2) if min_sfc_rh is not None else None
    res["sfc_rh_mean"] = mean_sfc_rh
    res["pct_transect_rh_below_15"] = pct_rh_red_flag
    res["pct_transect_rh_below_8"] = pct_rh_extreme
    print(f"  Surface RH min: {min_sfc_rh:.1f}%, mean: {mean_sfc_rh:.1f}%")
    print(f"  % transect RH<15%: {pct_rh_red_flag}%, RH<8%: {pct_rh_extreme}%")

    # Depth of critically dry layer (RH<20%) from surface upward
    dry_depths = []
    for j in range(n_pts):
        sp_j = sp[j]
        si = get_surface_index(pressures, sp_j)
        if si is None:
            continue
        # Go from surface upward (decreasing pressure)
        top_p = pressures[si]
        for i in range(si, len(pressures)):
            if rh[i][j] is not None and rh[i][j] >= 20:
                top_p = pressures[i]
                break
            top_p = pressures[i]
        # Depth in hPa
        depth = pressures[si] - top_p
        dry_depths.append(depth)
    max_dry_depth = max(dry_depths) if dry_depths else 0
    mean_dry_depth = round(sum(dry_depths)/len(dry_depths), 1) if dry_depths else 0
    res["dry_layer_depth_max_hPa"] = round(max_dry_depth, 1)
    res["dry_layer_depth_mean_hPa"] = mean_dry_depth
    print(f"  Dry layer (RH<20%) depth: max {max_dry_depth:.0f} hPa, mean {mean_dry_depth:.0f} hPa")

    # --- Wind ---
    d_ws = fetch("wind_speed", tname)
    ws = compute_wind_speed_2d(d_ws["u_wind_ms"], d_ws["v_wind_ms"])
    sp_w = d_ws["surface_pressure_hpa"]

    sfc_ws = []
    for j in range(n_pts):
        si = get_surface_index(pressures, sp_w[j])
        if si is not None:
            sfc_ws.append(ws[si][j])
        else:
            sfc_ws.append(None)

    valid_ws = [v for v in sfc_ws if v is not None]
    ws_above_25 = sum(1 for v in valid_ws if v > 25)
    pct_ws_red_flag = round(100.0 * ws_above_25 / len(valid_ws), 1) if valid_ws else 0
    max_sfc_ws = max(v for v in valid_ws) if valid_ws else None
    mean_sfc_ws = round(sum(valid_ws)/len(valid_ws), 2) if valid_ws else None

    res["sfc_wind_max_kt"] = round(max_sfc_ws, 2) if max_sfc_ws is not None else None
    res["sfc_wind_mean_kt"] = mean_sfc_ws
    res["pct_transect_wind_above_25kt"] = pct_ws_red_flag
    print(f"  Surface wind max: {max_sfc_ws:.1f} kt, mean: {mean_sfc_ws:.1f} kt")
    print(f"  % transect wind>25kt: {pct_ws_red_flag}%")

    # Max wind below 700 hPa
    max_wind_below_700 = 0
    for j in range(n_pts):
        for i, p in enumerate(pressures):
            if 700 <= p <= sp_w[j] + 5:
                if ws[i][j] is not None and ws[i][j] > max_wind_below_700:
                    max_wind_below_700 = ws[i][j]
    res["max_wind_below_700_kt"] = round(max_wind_below_700, 2)

    # --- VPD ---
    d_vpd = fetch("vpd", tname)
    vpd = d_vpd["vpd_hpa"]
    sp_v = d_vpd["surface_pressure_hpa"]

    sfc_vpd = []
    vpd_lons = []
    for j in range(n_pts):
        si = get_surface_index(pressures, sp_v[j])
        if si is not None:
            sfc_vpd.append(vpd[si][j])
            vpd_lons.append(lons[j])
        else:
            sfc_vpd.append(None)
            vpd_lons.append(None)

    valid_vpd = [(v, vpd_lons[i]) for i, v in enumerate(sfc_vpd) if v is not None]
    max_vpd_val = max(v for v, _ in valid_vpd) if valid_vpd else None
    max_vpd_lon = None
    for v, lon in valid_vpd:
        if v == max_vpd_val:
            max_vpd_lon = lon
            break
    mean_vpd = round(sum(v for v, _ in valid_vpd)/len(valid_vpd), 2) if valid_vpd else None

    vpd_above_13 = sum(1 for v, _ in valid_vpd if v > 13)
    pct_vpd_extreme = round(100.0 * vpd_above_13 / len(valid_vpd), 1) if valid_vpd else 0
    vpd_above_20 = sum(1 for v, _ in valid_vpd if v > 20)
    pct_vpd_offcharts = round(100.0 * vpd_above_20 / len(valid_vpd), 1) if valid_vpd else 0

    res["vpd_max_hPa"] = round(max_vpd_val, 2) if max_vpd_val is not None else None
    res["vpd_max_lon"] = round(max_vpd_lon, 2) if max_vpd_lon is not None else None
    res["vpd_mean_hPa"] = mean_vpd
    res["pct_vpd_above_13"] = pct_vpd_extreme
    res["pct_vpd_above_20"] = pct_vpd_offcharts
    print(f"  VPD max: {max_vpd_val:.2f} hPa at lon {max_vpd_lon:.1f}")
    print(f"  VPD mean: {mean_vpd:.2f} hPa")
    print(f"  % transect VPD>13: {pct_vpd_extreme}%, VPD>20: {pct_vpd_offcharts}%")

    # --- Lapse Rate ---
    d_lr = fetch("lapse_rate", tname)
    lr = d_lr["lapse_rate_c_km"]
    sp_lr = d_lr["surface_pressure_hpa"]

    # Max lapse rate below 500 hPa
    max_lr = 0
    for j in range(n_pts):
        for i, p in enumerate(pressures):
            if 500 <= p <= sp_lr[j] + 5:
                if lr[i][j] is not None and lr[i][j] > max_lr:
                    max_lr = lr[i][j]
    # Mean surface lapse rate
    sfc_lr = []
    for j in range(n_pts):
        si = get_surface_index(pressures, sp_lr[j])
        if si is not None and lr[si][j] is not None:
            sfc_lr.append(lr[si][j])
    mean_lr = round(sum(sfc_lr)/len(sfc_lr), 2) if sfc_lr else None

    res["lapse_rate_max_c_km"] = round(max_lr, 2)
    res["lapse_rate_mean_c_km"] = mean_lr
    print(f"  Lapse rate max: {max_lr:.2f} C/km, mean: {mean_lr:.2f} C/km")

    # --- Omega (subsidence) ---
    d_om = fetch("omega", tname)
    omega = d_om["omega_hpa_hr"]
    sp_om = d_om["surface_pressure_hpa"]

    # Max positive omega (subsidence = positive omega in hPa/hr convention)
    # Actually in meteorology, omega>0 = sinking, omega<0 = rising
    max_omega = None
    min_omega = None
    for j in range(n_pts):
        for i, p in enumerate(pressures):
            if 500 <= p <= sp_om[j] + 5:
                val = omega[i][j]
                if val is not None:
                    if max_omega is None or val > max_omega:
                        max_omega = val
                    if min_omega is None or val < min_omega:
                        min_omega = val

    res["omega_max_subsidence_hPa_hr"] = round(max_omega, 2) if max_omega is not None else None
    res["omega_max_ascent_hPa_hr"] = round(min_omega, 2) if min_omega is not None else None
    print(f"  Omega max subsidence: {max_omega:.1f} hPa/hr")
    print(f"  Omega max ascent: {min_omega:.1f} hPa/hr")

    # --- Multi-threshold check ---
    # Points meeting BOTH RH<15 AND wind>25kt
    multi_count = 0
    for j in range(n_pts):
        rh_ok = sfc_rh[j] is not None and sfc_rh[j] < 15
        ws_ok = sfc_ws[j] is not None and sfc_ws[j] > 25
        if rh_ok and ws_ok:
            multi_count += 1

    # Points meeting RH<15 AND VPD>13
    multi_rh_vpd = 0
    for j in range(n_pts):
        rh_ok = sfc_rh[j] is not None and sfc_rh[j] < 15
        vpd_ok = sfc_vpd[j] is not None and sfc_vpd[j] > 13
        if rh_ok and vpd_ok:
            multi_rh_vpd += 1

    res["multi_rh15_wind25_count"] = multi_count
    res["multi_rh15_wind25_pct"] = round(100.0 * multi_count / n_pts, 1)
    res["multi_rh15_vpd13_count"] = multi_rh_vpd
    res["multi_rh15_vpd13_pct"] = round(100.0 * multi_rh_vpd / n_pts, 1)
    print(f"  Multi-threshold (RH<15 & wind>25kt): {multi_count} pts ({res['multi_rh15_wind25_pct']}%)")
    print(f"  Multi-threshold (RH<15 & VPD>13): {multi_rh_vpd} pts ({res['multi_rh15_vpd13_pct']}%)")

    results[tname] = res

# Save
outpath = os.path.join(OUTDIR, "threshold_analysis_f39.json")
with open(outpath, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved threshold analysis to {outpath}")
