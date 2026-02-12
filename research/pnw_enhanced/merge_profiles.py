"""Merge script: combines all enhanced PNW/Rockies profiles into pnw_rockies_profiles.py"""
import re, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', '..', 'tools', 'agent_tools', 'data')

# ============================================================
# Step 1: Extract city text blocks from source files
# ============================================================

sources = [
    ('oregon_profiles.py', 'PNW_OREGON_ENHANCED'),
    ('washington_profiles.py', 'PNW_WASHINGTON_ENHANCED'),
    ('idaho_profiles.py', 'PNW_IDAHO_ENHANCED'),
    ('montana_profiles.py', 'PNW_MONTANA_ENHANCED'),
]

def extract_with_comments(filepath):
    content = open(filepath, encoding='utf-8').read()
    lines = content.split('\n')

    pattern = r'^(\s{4}"[a-z_]+(?:_or|_wa|_id|_mt)":\s*\{)'
    matches = list(re.finditer(pattern, content, re.MULTILINE))

    blocks = {}
    for idx, match in enumerate(matches):
        key = re.search(r'"([^"]+)"', match.group(1)).group(1)
        line_start = content[:match.start()].count('\n')

        # Look backwards for comment lines
        comment_start = line_start
        while comment_start > 0 and lines[comment_start - 1].strip().startswith('#'):
            comment_start -= 1

        # Find end: count braces to find closing }
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
    # Parse for validation
    ns = {}
    exec(open(fpath, encoding='utf-8').read(), ns)
    d = ns.get(dictname, {})
    all_profiles.update(d)
    # Extract text blocks
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

or_keys = sorted(k for k in all_blocks if k.endswith('_or'))
wa_keys = sorted(k for k in all_blocks if k.endswith('_wa'))
id_keys = sorted(k for k in all_blocks if k.endswith('_id'))
mt_keys = sorted(k for k in all_blocks if k.endswith('_mt'))

regions = [
    ("OREGON", or_keys),
    ("WASHINGTON", wa_keys),
    ("IDAHO", id_keys),
    ("MONTANA", mt_keys),
]

# ============================================================
# Step 3: Read original ignition + climatology + utilities
# ============================================================

orig_path = os.path.join(DATA_DIR, 'pnw_rockies_profiles.py')
orig = open(orig_path, encoding='utf-8').read()
orig_lines = orig.split('\n')

# Find PNW_IGNITION_SOURCES section start
ign_line = None
for i, line in enumerate(orig_lines):
    if 'PNW_IGNITION_SOURCES' in line and '=' in line and '{' in line:
        ign_line = i
        break

j = ign_line - 1
while j > 0 and (orig_lines[j].strip().startswith('#') or orig_lines[j].strip() == ''):
    j -= 1
ign_section_start = j + 1

rest_of_file = '\n'.join(orig_lines[ign_section_start:])

# ============================================================
# Step 4: Build station map for new cities
# ============================================================

# Original station map entries are in PNW_STATION_CITY_MAP in the rest_of_file
# We'll add new entries to it

new_station_mappings = {
    # Oregon additions
    "detroit_or": "KSLE",  # Salem (closest ASOS)
    "gates_or": "KSLE",
    "blue_river_or": "KEUG",  # Eugene
    "talent_or": "KMFR",  # Medford
    "phoenix_or": "KMFR",
    "oakridge_or": "KEUG",
    "sunriver_or": "KRDM",  # Redmond/Bend
    "camp_sherman_or": "KRDM",
    # Washington additions
    "winthrop_wa": "KOMK",  # Omak
    "twisp_wa": "KOMK",
    "pateros_wa": "KOMK",
    "entiat_wa": "KEAT",  # Wenatchee
    "cle_elum_wa": "KELN",  # Ellensburg
    "manson_wa": "KEAT",
    "roslyn_wa": "KELN",
    "omak_okanogan_wa": "KOMK",
    # Idaho additions
    "ketchum_sun_valley_id": "KSUN",  # Hailey/Sun Valley
    "hailey_id": "KSUN",
    "cascade_id": "KDIJ",  # Donnelly
    "garden_valley_id": "KBOI",  # Boise
    "stanley_id": "KSUN",
    "salmon_id": "KSMN",
    "lowman_id": "KBOI",
    "featherville_pine_id": "KBOI",
    # Montana additions
    "hamilton_mt": "KHLN",  # Hamilton doesn't have ASOS, use Helena or Missoula
    "seeley_lake_mt": "KMSO",
    "stevensville_mt": "KMSO",
    "superior_mt": "KMSO",
    "west_yellowstone_mt": "KWYS",
    "red_lodge_mt": "KBIL",  # Billings
    "lincoln_mt": "KHLN",
    "lolo_mt": "KMSO",
}

# ============================================================
# Step 5: Assemble the file
# ============================================================

total_cities = len(all_profiles)

header = f'"""PNW & Northern Rockies Fire-Vulnerable City Profiles\n'
header += '=' * 55 + '\n\n'
header += f'Comprehensive terrain, evacuation, fire behavior, infrastructure, and demographic\n'
header += f'data for {total_cities} fire-vulnerable cities across Oregon, Washington, Idaho, and Montana.\n'
header += 'Profiles derived from CWPP documents, InciWeb records, NWCG incident reports,\n'
header += 'state forestry data, and post-fire assessments.\n\n'
header += 'Usage:\n'
header += '    from tools.agent_tools.data.pnw_rockies_profiles import (\n'
header += '        PNW_TERRAIN_PROFILES,\n'
header += '        PNW_IGNITION_SOURCES,\n'
header += '        PNW_CLIMATOLOGY,\n'
header += '    )\n\n'
header += f'Cities covered ({total_cities} entries across 4 states):\n'
for rname, keys in regions:
    header += f'    {rname} ({len(keys)} cities):\n'
    for k in keys:
        nice = k.rsplit('_', 1)[0].replace('_', ' ').title()
        header += f'        {nice}\n'
header += '\nSources:\n'
header += '    - Oregon CWPP documents, ODF incident reports\n'
header += '    - Washington DNR fire records, WADNR CWPP data\n'
header += '    - Idaho Dept of Lands fire history, USFS incident reports\n'
header += '    - Montana DNRC fire records, Flathead/Missoula County CWPPs\n'
header += '    - InciWeb, NIFC, NWCG incident data\n'
header += '    - WRCC / IEM / ASOS climatology archives\n'
header += '    - Wikipedia fire articles with citations\n'
header += '"""\n\n'

terrain_start = '# =============================================================================\n'
terrain_start += f'# TERRAIN PROFILES -- {total_cities} entries organized by state\n'
terrain_start += '# =============================================================================\n\n'
terrain_start += 'PNW_TERRAIN_PROFILES = {\n'

terrain_body = ''
for rname, keys in regions:
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

# Update station map in rest_of_file
# Find PNW_STATION_CITY_MAP and extend it
station_map_pattern = r'PNW_STATION_CITY_MAP\s*=\s*\{[^}]+\}'
station_match = re.search(station_map_pattern, rest_of_file)
if station_match:
    old_map = station_match.group(0)
    # Parse existing entries
    existing = dict(re.findall(r'"([^"]+)":\s*"([^"]+)"', old_map))
    # Merge
    all_mappings = {**existing, **new_station_mappings}
    new_map = 'PNW_STATION_CITY_MAP = {\n'
    for k in sorted(all_mappings.keys()):
        new_map += f'    "{k}": "{all_mappings[k]}",\n'
    new_map += '}'
    rest_of_file = rest_of_file.replace(old_map, new_map)
    print(f"Station map: {len(existing)} existing + {len(new_station_mappings)} new = {len(all_mappings)} total")

# Assemble
output = header + terrain_start + terrain_body + terrain_end + rest_of_file

# Write
outpath = os.path.join(DATA_DIR, 'pnw_rockies_profiles.py')
with open(outpath, 'w', encoding='utf-8') as f:
    f.write(output)

lines = output.count('\n')
print(f"\nWritten {len(output):,} chars ({lines:,} lines) to pnw_rockies_profiles.py")
print(f"Terrain profiles: {total_cities} entries")
