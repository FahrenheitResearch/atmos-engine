"""Extract numerical surface data along E-W and N-S transects at each FHR."""
import io, sys, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.path.insert(0, r'C:\Users\drew\hrrr-maps')

from tools.agent_tools.cross_section import CrossSectionTool

cs = CrossSectionTool(base_url='http://localhost:5565')
cycle = '20260209_18z'

# E-W transect
ew_start = (35.5, -99.5)
ew_end = (35.5, -95.0)

# N-S transect
ns_start = (37.0, -99.0)
ns_end = (34.5, -99.0)

products = ['wind_speed', 'rh', 'temperature', 'vpd', 'dewpoint_dep']
fhrs = [1, 2, 3, 4, 5, 6, 7, 8]

results = {'ew': {}, 'ns': {}}

print('='*80)
print('E-W TRANSECT SURFACE DATA: (35.5, -99.5) to (35.5, -95.0)')
print('='*80)

for product in products:
    results['ew'][product] = {}
    print(f'\n--- {product.upper()} ---')
    print(f'{"FHR":<6} {"Time CST":<12} {"Min":<12} {"Max":<12} {"Mean":<12}')
    print('-' * 54)
    for fhr in fhrs:
        try:
            data = cs.get_data(start=ew_start, end=ew_end, cycle=cycle, fhr=fhr, product=product)
            stats = data.surface_stats()
            hour_cst = 12 + fhr  # 18z = noon CST, so FHR+12 = CST hour (24h)
            time_str = f'{hour_cst}:00'
            if hour_cst >= 24:
                time_str = f'{hour_cst-24}:00+1'
            print(f'{fhr:<6} {time_str:<12} {stats["min"]:<12.1f} {stats["max"]:<12.1f} {stats["mean"]:<12.1f}')
            results['ew'][product][fhr] = stats
        except Exception as e:
            print(f'{fhr:<6} ERROR: {e}')

print('\n\n')
print('='*80)
print('N-S TRANSECT SURFACE DATA: (37.0, -99.0) to (34.5, -99.0)')
print('='*80)

for product in products:
    results['ns'][product] = {}
    print(f'\n--- {product.upper()} ---')
    print(f'{"FHR":<6} {"Time CST":<12} {"Min":<12} {"Max":<12} {"Mean":<12}')
    print('-' * 54)
    for fhr in fhrs:
        try:
            data = cs.get_data(start=ns_start, end=ns_end, cycle=cycle, fhr=fhr, product=product)
            stats = data.surface_stats()
            hour_cst = 12 + fhr
            time_str = f'{hour_cst}:00'
            if hour_cst >= 24:
                time_str = f'{hour_cst-24}:00+1'
            print(f'{fhr:<6} {time_str:<12} {stats["min"]:<12.1f} {stats["max"]:<12.1f} {stats["mean"]:<12.1f}')
            results['ns'][product][fhr] = stats
        except Exception as e:
            print(f'{fhr:<6} ERROR: {e}')

# Save raw results as JSON
out_path = r'C:\Users\drew\hrrr-maps\research\ok_prescribed_burn_20260209\surface_data.json'
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2)
print(f'\n\nRaw data saved to {out_path}')
