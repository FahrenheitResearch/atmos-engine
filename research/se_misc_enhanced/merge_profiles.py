"""Merge script: combines enhanced SE/Misc profiles into southeast_misc_profiles.py"""
import re, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', '..', 'tools', 'agent_tools', 'data')

# ============================================================
# Step 1: Extract city text blocks from source file
# ============================================================

sources = [
    ('se_misc_profiles.py', 'SE_MISC_ENHANCED'),
]

# Match all state suffixes used in SE/Misc region
STATE_SUFFIXES = r'(?:_hi|_tn|_nc|_ga|_fl|_sd|_mo|_mn)'

def extract_with_comments(filepath):
    content = open(filepath, encoding='utf-8').read()
    lines = content.split('\n')

    pattern = r'^(\s{4}"[a-z_]+' + STATE_SUFFIXES + r'":\s*\{)'
    matches = list(re.finditer(pattern, content, re.MULTILINE))

    blocks = {}
    for idx, match in enumerate(matches):
        key = re.search(r'"([^"]+)"', match.group(1)).group(1)
        line_start = content[:match.start()].count('\n')

        comment_start = line_start
        while comment_start > 0 and lines[comment_start - 1].strip().startswith('#'):
            comment_start -= 1

        rest = content[match.start():]
        depth = 0
        pos = 0
        for ch in rest:
            if ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    pos += 1
                    break
            pos += 1
        abs_end = match.start() + pos
        end_line = content[:abs_end].count('\n') + 1

        block_lines = lines[comment_start:end_line]
        block = '\n'.join(block_lines)
        if not block.rstrip().endswith(','):
            block = block.rstrip() + ','
        blocks[key] = block

    return blocks

all_blocks = {}
all_profiles = {}
for fname, dictname in sources:
    fpath = os.path.join(BASE_DIR, fname)
    if not os.path.exists(fpath):
        print(f"  SKIP {fname}: not found yet")
        continue
    ns = {}
    exec(open(fpath, encoding='utf-8').read(), ns)
    d = ns.get(dictname, {})
    all_profiles.update(d)
    blocks = extract_with_comments(fpath)
    all_blocks.update(blocks)
    print(f"  {fname}: {len(d)} profiles, {len(blocks)} blocks")

print(f"Total profiles: {len(all_profiles)}, blocks: {len(all_blocks)}")

if len(all_profiles) == 0:
    print("No profiles found - agents may still be running")
    exit(1)

# ============================================================
# Step 2: Organize by state/region
# ============================================================

hi_keys = sorted(k for k in all_blocks if k.endswith('_hi'))
tn_keys = sorted(k for k in all_blocks if k.endswith('_tn'))
nc_keys = sorted(k for k in all_blocks if k.endswith('_nc'))
ga_keys = sorted(k for k in all_blocks if k.endswith('_ga'))
fl_keys = sorted(k for k in all_blocks if k.endswith('_fl'))
sd_keys = sorted(k for k in all_blocks if k.endswith('_sd'))
mo_keys = sorted(k for k in all_blocks if k.endswith('_mo'))
mn_keys = sorted(k for k in all_blocks if k.endswith('_mn'))

regions = [
    ("HAWAII", hi_keys),
    ("TENNESSEE", tn_keys),
    ("NORTH CAROLINA", nc_keys),
    ("GEORGIA", ga_keys),
    ("FLORIDA", fl_keys),
    ("SOUTH DAKOTA (BLACK HILLS)", sd_keys),
    ("MISSOURI (OZARKS)", mo_keys),
    ("MINNESOTA", mn_keys),
]

# ============================================================
# Step 3: Read original ignition + climatology
# ============================================================

orig_path = os.path.join(DATA_DIR, 'southeast_misc_profiles.py')
orig = open(orig_path, encoding='utf-8').read()
orig_lines = orig.split('\n')

ign_line = None
for i, line in enumerate(orig_lines):
    if 'SE_MISC_IGNITION_SOURCES' in line and '=' in line and '{' in line:
        ign_line = i
        break

j = ign_line - 1
while j > 0 and (orig_lines[j].strip().startswith('#') or orig_lines[j].strip() == ''):
    j -= 1
ign_section_start = j + 1

rest_of_file = '\n'.join(orig_lines[ign_section_start:])

# ============================================================
# Step 4: Assemble the file
# ============================================================

total_cities = len(all_profiles)

header = '"""Southeast, Black Hills, Midwest & Hawaii Fire-Vulnerable City Profiles\n'
header += '=' * 63 + '\n\n'
header += f'Comprehensive terrain, evacuation, fire behavior, infrastructure, and demographic\n'
header += f'data for {total_cities} fire-vulnerable cities across the Southeast US, Black Hills,\n'
header += 'Midwest, and Hawaii.\n\n'
header += 'Usage:\n'
header += '    from tools.agent_tools.data.southeast_misc_profiles import (\n'
header += '        SE_MISC_TERRAIN_PROFILES,\n'
header += '        SE_MISC_IGNITION_SOURCES,\n'
header += '        SE_MISC_CLIMATOLOGY,\n'
header += '    )\n\n'
header += f'Cities covered ({total_cities} entries across 8 states):\n'
for rname, keys in regions:
    if keys:
        header += f'    {rname} ({len(keys)} cities):\n'
        for k in keys:
            nice = k.rsplit('_', 1)[0].replace('_', ' ').title()
            header += f'        {nice}\n'
header += '\nSources:\n'
header += '    - NIST Chimney Tops 2 Fire investigation\n'
header += '    - USFA/FEMA 2023 Maui Wildfire After-Action Report\n'
header += '    - USGS Jasper Fire fuels data\n'
header += '    - SD Wildland Fire Division historical records\n'
header += '    - NCFS wildfire statistics\n'
header += '    - WRCC / IEM / ASOS climatology archives\n'
header += '"""\n\n'

terrain_start = '# =============================================================================\n'
terrain_start += f'# TERRAIN PROFILES -- {total_cities} entries organized by state\n'
terrain_start += '# =============================================================================\n\n'
terrain_start += 'SE_MISC_TERRAIN_PROFILES = {\n'

terrain_body = ''
for rname, keys in regions:
    if not keys:
        continue
    terrain_body += '\n'
    terrain_body += '    # ' + '=' * 73 + '\n'
    terrain_body += f'    # {rname} ({len(keys)} cities)\n'
    terrain_body += '    # ' + '=' * 73 + '\n'
    for key in keys:
        if key in all_blocks:
            block = all_blocks[key]
            terrain_body += '\n' + block + '\n'
        else:
            terrain_body += f'\n    # WARNING: missing block for {key}\n'

terrain_end = '\n}\n\n\n'

output = header + terrain_start + terrain_body + terrain_end + rest_of_file

outpath = os.path.join(DATA_DIR, 'southeast_misc_profiles.py')
with open(outpath, 'w', encoding='utf-8') as f:
    f.write(output)

lines = output.count('\n')
print(f"\nWritten {len(output):,} chars ({lines:,} lines) to southeast_misc_profiles.py")
print(f"Terrain profiles: {total_cities} entries")
