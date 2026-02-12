"""Merge script: combines enhanced Plains profiles into southern_plains_profiles.py"""
import re, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', '..', 'tools', 'agent_tools', 'data')

# ============================================================
# Step 1: Extract city text blocks from source file
# ============================================================

sources = [
    ('texas_ok_ks_profiles.py', 'PLAINS_ENHANCED'),
]

def extract_with_comments(filepath):
    content = open(filepath, encoding='utf-8').read()
    lines = content.split('\n')

    pattern = r'^(\s{4}"[a-z_]+(?:_tx|_ok|_ks)":\s*\{)'
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
# Step 2: Organize by state
# ============================================================

tx_keys = sorted(k for k in all_blocks if k.endswith('_tx'))
ok_keys = sorted(k for k in all_blocks if k.endswith('_ok'))
ks_keys = sorted(k for k in all_blocks if k.endswith('_ks'))

regions = [
    ("TEXAS", tx_keys),
    ("OKLAHOMA", ok_keys),
    ("KANSAS", ks_keys),
]

# ============================================================
# Step 3: Read original ignition + climatology + coords
# ============================================================

orig_path = os.path.join(DATA_DIR, 'southern_plains_profiles.py')
orig = open(orig_path, encoding='utf-8').read()
orig_lines = orig.split('\n')

ign_line = None
for i, line in enumerate(orig_lines):
    if 'PLAINS_IGNITION_SOURCES' in line and '=' in line and '{' in line:
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

header = '"""Texas, Oklahoma & Kansas Fire-Vulnerable City Profiles\n'
header += '=' * 52 + '\n\n'
header += f'Comprehensive terrain, evacuation, fire behavior, infrastructure, and demographic\n'
header += f'data for {total_cities} fire-vulnerable cities across the Southern Plains.\n'
header += 'Winter grass fire regime (Nov-Mar), extreme wind events, dryline dynamics,\n'
header += 'cold front passages, and hidden canyon/breaks terrain.\n\n'
header += 'Usage:\n'
header += '    from tools.agent_tools.data.southern_plains_profiles import (\n'
header += '        PLAINS_TERRAIN_PROFILES,\n'
header += '        PLAINS_IGNITION_SOURCES,\n'
header += '        PLAINS_CLIMATOLOGY,\n'
header += '    )\n\n'
header += f'Cities covered ({total_cities} entries across 3 states):\n'
for rname, keys in regions:
    header += f'    {rname} ({len(keys)} cities):\n'
    for k in keys:
        nice = k.rsplit('_', 1)[0].replace('_', ' ').title()
        header += f'        {nice}\n'
header += '\nSources:\n'
header += '    - NOAA Climate.gov: Feb 2024 megafire outbreak context\n'
header += '    - Texas Tribune: Smokehouse Creek, Eastland Complex coverage\n'
header += '    - Texas A&M Forest Service: Historical Fire Statistics\n'
header += '    - Oklahoma Forestry Services: Fire Situation Reports\n'
header += '    - NWS Amarillo, NWS Lubbock, NWS Dodge City\n'
header += '    - NASA Earth Observatory: East Amarillo Complex\n'
header += '    - WRCC / IEM / ASOS climatology archives\n'
header += '"""\n\n'

terrain_start = '# =============================================================================\n'
terrain_start += f'# TERRAIN PROFILES -- {total_cities} entries organized by state\n'
terrain_start += '# =============================================================================\n\n'
terrain_start += 'PLAINS_TERRAIN_PROFILES = {\n'

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

outpath = os.path.join(DATA_DIR, 'southern_plains_profiles.py')
with open(outpath, 'w', encoding='utf-8') as f:
    f.write(output)

lines = output.count('\n')
print(f"\nWritten {len(output):,} chars ({lines:,} lines) to southern_plains_profiles.py")
print(f"Terrain profiles: {total_cities} entries")
