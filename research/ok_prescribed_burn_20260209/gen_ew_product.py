"""Generate E-W product comparison cross-sections at key FHRs."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.path.insert(0, r'C:\Users\drew\hrrr-maps')

from tools.agent_tools.cross_section import CrossSectionTool

cs = CrossSectionTool(base_url='http://localhost:5565')
cycle = '20260209_18z'
start = (35.5, -99.5)
end = (35.5, -95.0)
fig_dir = r'C:\Users\drew\hrrr-maps\research\ok_prescribed_burn_20260209\figures'

# Product comparison at peak afternoon (FHR 3 = 3pm CST) and evening (FHR 8 = 8pm CST)
for fhr in [1, 3, 5, 8]:
    out = f'{fig_dir}/ew_products_fhr{fhr}.png'
    print(f'Generating E-W product comparison at FHR {fhr}...')
    try:
        result = cs.generate_comparison(
            start=start, end=end,
            mode='product',
            products='wind_speed,rh,vpd',
            cycle=cycle,
            fhr=fhr,
            y_top=300,
            output_path=out
        )
        print(f'  -> {result}')
    except Exception as e:
        print(f'  ERROR: {e}')

# Also generate product comparison for N-S transect at peak
for fhr in [1, 3, 5, 8]:
    out = f'{fig_dir}/ns_products_fhr{fhr}.png'
    print(f'Generating N-S product comparison at FHR {fhr}...')
    try:
        result = cs.generate_comparison(
            start=(37.0, -99.0), end=(34.5, -99.0),
            mode='product',
            products='wind_speed,rh,vpd',
            cycle=cycle,
            fhr=fhr,
            y_top=300,
            output_path=out
        )
        print(f'  -> {result}')
    except Exception as e:
        print(f'  ERROR: {e}')

print('\nDone with product comparisons.')
