import json, math, os

base = 'C:/Users/drew/hrrr-maps/research/camp_fire_paper'

target_levels = [900, 875, 850]

def compute_wind_speed(u_data, v_data, pressure_levels, target_hpa):
    idx = pressure_levels.index(target_hpa)
    max_ws = 0
    max_loc = 0
    for j in range(len(u_data[idx])):
        u = u_data[idx][j]
        v = v_data[idx][j]
        ws = math.sqrt(u**2 + v**2) * 1.944
        if ws > max_ws:
            max_ws = ws
            max_loc = j
    return max_ws, max_loc

def compute_wind_at_point(u_data, v_data, pressure_levels, target_hpa, point_idx):
    idx = pressure_levels.index(target_hpa)
    u = u_data[idx][point_idx]
    v = v_data[idx][point_idx]
    ws = math.sqrt(u**2 + v**2) * 1.944
    wdir = (270 - math.degrees(math.atan2(v, u))) % 360
    return ws, wdir

fhrs = [15, 18, 20, 24, 30]
valid_times = {15: '15z (7AM)', 18: '18z (10AM)', 20: '20z (Noon)', 24: '00z+1 (4PM)', 30: '06z+1 (10PM)'}

print('=== CANYON PATH WIND SPEED TABLE ===')
print(f'{"FHR":<6} {"Valid Time":<18} {"900 hPa (kt)":<15} {"875 hPa (kt)":<15} {"850 hPa (kt)":<15} {"Max Near-Sfc (kt)":<18}')
print('-' * 90)

for fhr in fhrs:
    fname = os.path.join(base, f'data_canyon_f{fhr}.json')
    with open(fname) as f:
        data = json.load(f)

    u = data['u_wind_ms']
    v = data['v_wind_ms']
    plevs = data['pressure_levels_hpa']
    sfc_p = data['surface_pressure_hpa']
    lats = data['lats']
    lons = data['lons']

    results = {}
    for lvl in target_levels:
        ws, loc = compute_wind_speed(u, v, plevs, lvl)
        results[lvl] = (ws, loc, lats[loc], lons[loc])

    # Max near-surface
    max_sfc_ws = 0
    for j in range(len(sfc_p)):
        sp = sfc_p[j]
        for i, p in enumerate(plevs):
            if p <= sp:
                uu = u[i][j]
                vv = v[i][j]
                ws = math.sqrt(uu**2 + vv**2) * 1.944
                if ws > max_sfc_ws:
                    max_sfc_ws = ws
                break

    print(f'{fhr:<6} {valid_times[fhr]:<18} {results[900][0]:<15.1f} {results[875][0]:<15.1f} {results[850][0]:<15.1f} {max_sfc_ws:<18.1f}')

    _, _, lat875, lon875 = results[875]
    print(f'       875 hPa max at: {lat875:.2f}N, {lon875:.2f}W')

# Detailed analysis at FHR 15 for the jet structure section
print('\n=== DETAILED JET STRUCTURE (FHR 15, CANYON PATH) ===')
fname = os.path.join(base, 'data_canyon_f15.json')
with open(fname) as f:
    data = json.load(f)

u = data['u_wind_ms']
v = data['v_wind_ms']
plevs = data['pressure_levels_hpa']
lats = data['lats']
lons = data['lons']

all_levels = [925, 900, 875, 850, 825, 800, 775, 750]
print(f'{"Level (hPa)":<15} {"Max Wind (kt)":<15} {"Location":<25} {"Direction":<10}')
print('-' * 65)
for lvl in all_levels:
    ws, loc = compute_wind_speed(u, v, plevs, lvl)
    ws_pt, wdir = compute_wind_at_point(u, v, plevs, lvl, loc)
    print(f'{lvl:<15} {ws:<15.1f} {lats[loc]:.2f}N, {lons[loc]:.2f}W        {wdir:.0f}')

# Shear data
print('\n=== SHEAR DATA (CANYON PATH, FHR 15) ===')
fname = os.path.join(base, 'data_shear_f15.json')
with open(fname) as f:
    data = json.load(f)

print('Keys:', list(data.keys()))
fields = data.get('metadata', {}).get('fields', [])
print('Fields:', fields)

# Get the shear data array
for field in fields:
    key = field['key']
    if key in data:
        vals = data[key]
        plevs = data['pressure_levels_hpa']
        lats = data['lats']

        shear_levels = [975, 950, 925, 900, 875, 850]
        print(f'\nShear field: {key} ({field["units"]})')
        print(f'{"Level (hPa)":<15} {"Max Shear":<15} {"Location":<25}')
        print('-' * 55)
        for lvl in shear_levels:
            if lvl in plevs:
                idx = plevs.index(lvl)
                max_val = max(vals[idx])
                max_loc = vals[idx].index(max_val)
                print(f'{lvl:<15} {max_val:<15.4f} {lats[max_loc]:.2f}N, {data["lons"][max_loc]:.2f}W')

# Perpendicular path data
print('\n=== PERPENDICULAR PATH WIND (FHR 15) ===')
fname = os.path.join(base, 'data_perp_f15.json')
with open(fname) as f:
    data = json.load(f)

u = data['u_wind_ms']
v = data['v_wind_ms']
plevs = data['pressure_levels_hpa']
sfc_p = data['surface_pressure_hpa']
lats = data['lats']
lons = data['lons']

print(f'{"Point":<5} {"Lat":<8} {"Lon":<10} {"Sfc P (hPa)":<12} {"Sfc Wind (kt)":<15} {"900 hPa (kt)":<15} {"875 hPa (kt)":<15}')
print('-' * 80)

# Sample every 5th point
for j in range(0, len(lats), 5):
    sp = sfc_p[j]
    # Near-surface wind
    sfc_ws = 0
    for i, p in enumerate(plevs):
        if p <= sp:
            uu = u[i][j]
            vv = v[i][j]
            sfc_ws = math.sqrt(uu**2 + vv**2) * 1.944
            break

    # 900 hPa
    ws900 = 0
    if 900 in plevs:
        idx = plevs.index(900)
        uu = u[idx][j]
        vv = v[idx][j]
        ws900 = math.sqrt(uu**2 + vv**2) * 1.944

    # 875 hPa
    ws875 = 0
    if 875 in plevs:
        idx = plevs.index(875)
        uu = u[idx][j]
        vv = v[idx][j]
        ws875 = math.sqrt(uu**2 + vv**2) * 1.944

    print(f'{j:<5} {lats[j]:<8.2f} {lons[j]:<10.2f} {sp:<12.1f} {sfc_ws:<15.1f} {ws900:<15.1f} {ws875:<15.1f}')

# Find max and min surface wind to compute channeling ratio
max_sfc = 0
min_sfc = 999
for j in range(len(lats)):
    sp = sfc_p[j]
    for i, p in enumerate(plevs):
        if p <= sp:
            uu = u[i][j]
            vv = v[i][j]
            ws = math.sqrt(uu**2 + vv**2) * 1.944
            if ws > max_sfc:
                max_sfc = ws
                max_sfc_j = j
            if ws < min_sfc:
                min_sfc = ws
                min_sfc_j = j
            break

print(f'\nMax surface wind: {max_sfc:.1f} kt at {lats[max_sfc_j]:.2f}N, {lons[max_sfc_j]:.2f}W')
print(f'Min surface wind: {min_sfc:.1f} kt at {lats[min_sfc_j]:.2f}N, {lons[min_sfc_j]:.2f}W')
print(f'Channeling ratio: {max_sfc/min_sfc:.1f}x')
