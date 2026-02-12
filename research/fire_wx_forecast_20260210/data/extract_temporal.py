"""
Extract temporal fire weather profiles from HRRR data API for both CRIT areas.
Products: rh, wind_speed, temperature, vpd
FHRs: 24, 27, 30, 33, 36, 39, 42, 45, 48
"""
import urllib.request
import json
import math
import os

BASE_URL = "http://localhost:5565/api/v1/data"
CYCLE = "20260209_06z"
FHRS = [24, 27, 30, 33, 36, 39, 42, 45, 48]
PRODUCTS = ["rh", "wind_speed", "temperature", "vpd"]

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

# Data key mapping
DATA_KEYS = {
    "rh": "rh_pct",
    "temperature": "temperature_c",
    "vpd": "vpd_hpa",
}

def fetch_data(product, fhr, transect):
    t = TRANSECTS[transect]
    url = (f"{BASE_URL}?model=hrrr&cycle={CYCLE}&fhr={fhr}&product={product}"
           f"&start_lat={t['start_lat']}&start_lon={t['start_lon']}"
           f"&end_lat={t['end_lat']}&end_lon={t['end_lon']}")
    try:
        resp = urllib.request.urlopen(url, timeout=30)
        return json.loads(resp.read())
    except Exception as e:
        print(f"  ERROR fetching {product} fhr={fhr} {transect}: {e}")
        return None

def find_level_index(pressures, target):
    """Find index of pressure level closest to target."""
    best_idx = 0
    best_diff = abs(pressures[0] - target)
    for i, p in enumerate(pressures):
        diff = abs(p - target)
        if diff < best_diff:
            best_diff = diff
            best_idx = i
    return best_idx

def get_surface_values(data_2d, pressures, surface_pressures):
    """Get values at the surface level for each grid point (accounting for terrain)."""
    n_points = len(data_2d[0])
    values = []
    for j in range(n_points):
        sp = surface_pressures[j]
        # Find the highest pressure level that is <= surface pressure
        best_i = None
        for i, p in enumerate(pressures):
            if p <= sp + 5:  # small tolerance
                if best_i is None or pressures[i] > pressures[best_i]:
                    best_i = i
        if best_i is not None:
            val = data_2d[best_i][j]
            if val is not None and not math.isnan(val):
                values.append(val)
    return values

def get_level_values(data_2d, pressures, target_hpa, surface_pressures=None):
    """Get values at a specific pressure level, only where level is below surface."""
    idx = find_level_index(pressures, target_hpa)
    n_points = len(data_2d[0])
    values = []
    for j in range(n_points):
        if surface_pressures is not None:
            if pressures[idx] > surface_pressures[j] + 5:
                continue  # this level is underground
        val = data_2d[idx][j]
        if val is not None and not math.isnan(val):
            values.append(val)
    return values

def get_column_min_below(data_2d, pressures, surface_pressures, top_hpa):
    """Get minimum value in the column from surface down to top_hpa for each point, then return overall min."""
    n_points = len(data_2d[0])
    col_mins = []
    for j in range(n_points):
        sp = surface_pressures[j]
        vals = []
        for i, p in enumerate(pressures):
            if top_hpa <= p <= sp + 5:
                val = data_2d[i][j]
                if val is not None and not math.isnan(val):
                    vals.append(val)
        if vals:
            col_mins.append(min(vals))
    return min(col_mins) if col_mins else None

def get_column_max_below(data_2d, pressures, surface_pressures, top_hpa):
    """Get maximum value in the column from surface down to top_hpa for each point, then return overall max."""
    n_points = len(data_2d[0])
    col_maxs = []
    for j in range(n_points):
        sp = surface_pressures[j]
        vals = []
        for i, p in enumerate(pressures):
            if top_hpa <= p <= sp + 5:
                val = data_2d[i][j]
                if val is not None and not math.isnan(val):
                    vals.append(val)
        if vals:
            col_maxs.append(max(vals))
    return max(col_maxs) if col_maxs else None

def compute_wind_speed(u_arr, v_arr):
    """Compute wind speed from u,v components. Returns 2D array in knots."""
    result = []
    for i in range(len(u_arr)):
        row = []
        for j in range(len(u_arr[i])):
            u = u_arr[i][j]
            v = v_arr[i][j]
            if u is not None and v is not None:
                spd_ms = math.sqrt(u*u + v*v)
                spd_kt = spd_ms * 1.94384  # m/s to knots
                row.append(spd_kt)
            else:
                row.append(None)
        result.append(row)
    return result

def stats(values):
    if not values:
        return {"min": None, "max": None, "mean": None}
    return {
        "min": round(min(values), 2),
        "max": round(max(values), 2),
        "mean": round(sum(values)/len(values), 2)
    }

results = {}

for transect_name in ["north", "south"]:
    results[transect_name] = {
        "label": TRANSECTS[transect_name]["label"],
        "fhrs": {}
    }

    for fhr in FHRS:
        valid_time_utc = f"2026-02-10 {6+fhr:02d}Z" if fhr < 18 else f"2026-02-{10 + (6+fhr)//24:02d} {(6+fhr)%24:02d}Z"
        utc_hour = (6 + fhr) % 24
        utc_day = 10 + (6 + fhr) // 24
        valid_str = f"2026-02-{utc_day:02d} {utc_hour:02d}Z"

        print(f"Processing {transect_name} FHR {fhr} (valid {valid_str})...")
        fhr_data = {"valid_time_utc": valid_str}

        # RH
        d = fetch_data("rh", fhr, transect_name)
        if d:
            pressures = d["pressure_levels_hpa"]
            sp = d["surface_pressure_hpa"]
            rh = d["rh_pct"]

            sfc_vals = get_surface_values(rh, pressures, sp)
            fhr_data["rh_surface"] = stats(sfc_vals)

            lev850 = get_level_values(rh, pressures, 850, sp)
            fhr_data["rh_850hPa"] = stats(lev850)

            lev700 = get_level_values(rh, pressures, 700, sp)
            fhr_data["rh_700hPa"] = stats(lev700)

            col_min = get_column_min_below(rh, pressures, sp, 500)
            fhr_data["rh_min_below_500hPa"] = round(col_min, 2) if col_min is not None else None

        # Wind speed
        d = fetch_data("wind_speed", fhr, transect_name)
        if d:
            pressures = d["pressure_levels_hpa"]
            sp = d["surface_pressure_hpa"]
            ws = compute_wind_speed(d["u_wind_ms"], d["v_wind_ms"])

            sfc_vals = get_surface_values(ws, pressures, sp)
            fhr_data["wind_surface_kt"] = stats(sfc_vals)

            lev850 = get_level_values(ws, pressures, 850, sp)
            fhr_data["wind_850hPa_kt"] = stats(lev850)

            lev700 = get_level_values(ws, pressures, 700, sp)
            fhr_data["wind_700hPa_kt"] = stats(lev700)

            col_max = get_column_max_below(ws, pressures, sp, 700)
            fhr_data["wind_max_below_700hPa_kt"] = round(col_max, 2) if col_max is not None else None

        # Temperature
        d = fetch_data("temperature", fhr, transect_name)
        if d:
            pressures = d["pressure_levels_hpa"]
            sp = d["surface_pressure_hpa"]
            temp = d["temperature_c"]

            sfc_vals = get_surface_values(temp, pressures, sp)
            fhr_data["temp_surface_C"] = stats(sfc_vals)

            lev850 = get_level_values(temp, pressures, 850, sp)
            fhr_data["temp_850hPa_C"] = stats(lev850)

            lev700 = get_level_values(temp, pressures, 700, sp)
            fhr_data["temp_700hPa_C"] = stats(lev700)

        # VPD
        d = fetch_data("vpd", fhr, transect_name)
        if d:
            pressures = d["pressure_levels_hpa"]
            sp = d["surface_pressure_hpa"]
            vpd = d["vpd_hpa"]

            sfc_vals = get_surface_values(vpd, pressures, sp)
            fhr_data["vpd_surface_hPa"] = stats(sfc_vals)

            lev850 = get_level_values(vpd, pressures, 850, sp)
            fhr_data["vpd_850hPa"] = stats(lev850)

            col_max = get_column_max_below(vpd, pressures, sp, 500)
            fhr_data["vpd_max_below_500hPa"] = round(col_max, 2) if col_max is not None else None

        results[transect_name]["fhrs"][str(fhr)] = fhr_data

# Save results
outpath = os.path.join(os.path.dirname(__file__), "temporal_profiles.json")
with open(outpath, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved temporal profiles to {outpath}")
