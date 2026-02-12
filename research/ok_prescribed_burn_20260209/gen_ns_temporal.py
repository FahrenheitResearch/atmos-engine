"""Generate N-S temporal comparison cross-sections for fire weather products."""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.path.insert(0, r'C:\Users\drew\hrrr-maps')

from tools.agent_tools.cross_section import CrossSectionTool

cs = CrossSectionTool(base_url='http://localhost:5565')
cycle = '20260209_18z'
start = (37.0, -99.0)
end = (34.5, -99.0)
fhrs = '1,3,5,8'
fig_dir = r'C:\Users\drew\hrrr-maps\research\ok_prescribed_burn_20260209\figures'

products = ['wind_speed', 'rh', 'vpd', 'dewpoint_dep', 'temperature', 'lapse_rate', 'theta']

for product in products:
    out = f'{fig_dir}/ns_temporal_{product}.png'
    print(f'Generating N-S temporal {product}...')
    try:
        result = cs.generate_comparison(
            start=start, end=end,
            mode='temporal',
            fhrs=fhrs,
            cycle=cycle,
            product=product,
            y_top=300,
            output_path=out
        )
        print(f'  -> {result}')
    except Exception as e:
        print(f'  ERROR: {e}')

print('\nDone with N-S temporal comparisons.')
