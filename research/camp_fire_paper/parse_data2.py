import json, math, os
import sys
sys.stdout.reconfigure(encoding='utf-8')

base = 'C:/Users/drew/hrrr-maps/research/camp_fire_paper'

# Shear data
print('=== SHEAR DATA (CANYON PATH, FHR 15) ===')
fname = os.path.join(base, 'data_shear_f15.json')
with open(fname, encoding='utf-8') as f:
    data = json.load(f)

plevs = data['pressure_levels_hpa']
lats = data['lats']
lons = data['lons']
sfc_p = data['surface_pressure_hpa']

if 'shear_1e3_s' in data:
    vals = data['shear_1e3_s']
    shear_levels = [975, 950, 925, 900, 875, 850]
    print(f'{"Level (hPa)":<15} {"Max Shear (1e-3/s)":<20} {"Location":<25}')
    print('-' * 60)
    for lvl in shear_levels:
        if lvl in plevs:
            idx = plevs.index(lvl)
            max_val = max(vals[idx])
            max_loc = vals[idx].index(max_val)
            print(f'{lvl:<15} {max_val:<20.1f} {lats[max_loc]:.2f}N, {lons[max_loc]:.2f}W')

# Perpendicular path data
print('\n=== PERPENDICULAR PATH WIND (FHR 15) ===')
fname = os.path.join(base, 'data_perp_f15.json')
with open(fname, encoding='utf-8') as f:
    data = json.load(f)

u = data['u_wind_ms']
v = data['v_wind_ms']
plevs = data['pressure_levels_hpa']
sfc_p = data['surface_pressure_hpa']
lats = data['lats']
lons = data['lons']

print(f'{"Pt":<4} {"Lat":<8} {"Lon":<10} {"SfcP":<8} {"SfcWind":<10} {"900hPa":<10} {"875hPa":<10}')
print('-' * 60)

for j in range(0, len(lats), 5):
    sp = sfc_p[j]
    sfc_ws = 0
    for i, p in enumerate(plevs):
        if p <= sp:
            uu = u[i][j]
            vv = v[i][j]
            sfc_ws = math.sqrt(uu**2 + vv**2) * 1.944
            break

    ws900 = 0
    if 900 in plevs:
        idx = plevs.index(900)
        uu = u[idx][j]
        vv = v[idx][j]
        ws900 = math.sqrt(uu**2 + vv**2) * 1.944

    ws875 = 0
    if 875 in plevs:
        idx = plevs.index(875)
        uu = u[idx][j]
        vv = v[idx][j]
        ws875 = math.sqrt(uu**2 + vv**2) * 1.944

    print(f'{j:<4} {lats[j]:<8.2f} {lons[j]:<10.2f} {sp:<8.0f} {sfc_ws:<10.1f} {ws900:<10.1f} {ws875:<10.1f}')

# Channeling analysis
max_sfc = 0
min_sfc = 999
max_875 = 0
min_875 = 999
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

    if 875 in plevs:
        idx = plevs.index(875)
        uu = u[idx][j]
        vv = v[idx][j]
        ws = math.sqrt(uu**2 + vv**2) * 1.944
        if ws > max_875:
            max_875 = ws
            max_875_j = j
        if ws < min_875:
            min_875 = ws
            min_875_j = j

print(f'\nMax sfc wind: {max_sfc:.1f} kt at {lats[max_sfc_j]:.2f}N, {lons[max_sfc_j]:.2f}W (sfc_p={sfc_p[max_sfc_j]:.0f})')
print(f'Min sfc wind: {min_sfc:.1f} kt at {lats[min_sfc_j]:.2f}N, {lons[min_sfc_j]:.2f}W (sfc_p={sfc_p[min_sfc_j]:.0f})')
print(f'Channeling ratio (sfc): {max_sfc/min_sfc:.1f}x')
print(f'\nMax 875 wind: {max_875:.1f} kt at {lats[max_875_j]:.2f}N, {lons[max_875_j]:.2f}W')
print(f'Min 875 wind: {min_875:.1f} kt at {lats[min_875_j]:.2f}N, {lons[min_875_j]:.2f}W')
print(f'Channeling ratio (875): {max_875/min_875:.1f}x')

# Compute mean non-canyon vs canyon wind for better ratio
# NW quarter = first ~12 points, SE quarter = last ~12 points, canyon = middle
nw_winds = []
se_winds = []
mid_winds = []
for j in range(len(lats)):
    sp = sfc_p[j]
    for i, p in enumerate(plevs):
        if p <= sp:
            uu = u[i][j]
            vv = v[i][j]
            ws = math.sqrt(uu**2 + vv**2) * 1.944
            if j < 12:
                nw_winds.append(ws)
            elif j > 38:
                se_winds.append(ws)
            else:
                mid_winds.append(ws)
            break

print(f'\nMean NW ridge sfc wind: {sum(nw_winds)/len(nw_winds):.1f} kt')
print(f'Mean SE terrain sfc wind: {sum(se_winds)/len(se_winds):.1f} kt')
print(f'Mean canyon sfc wind: {sum(mid_winds)/len(mid_winds):.1f} kt')
outside_mean = (sum(nw_winds) + sum(se_winds)) / (len(nw_winds) + len(se_winds))
canyon_mean = sum(mid_winds) / len(mid_winds)
print(f'Mean outside: {outside_mean:.1f} kt, Mean canyon: {canyon_mean:.1f} kt')
print(f'Amplification: {canyon_mean/outside_mean:.1f}x')
