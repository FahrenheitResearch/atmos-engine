"""Merge script: combines all enhanced CA profiles into california_profiles.py"""
import re, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', '..', 'tools', 'agent_tools', 'data')

# ============================================================
# Step 1: Extract city text blocks from source files
# ============================================================

sources = [
    ('norcal_terrain.py', 'ENHANCED_NORCAL_PROFILES'),
    ('la_basin_terrain.py', 'LA_BASIN_TERRAIN_PROFILES'),
    ('ventura_sb_terrain.py', 'ENHANCED_TERRAIN_PROFILES'),
    ('sd_sierra_terrain.py', 'ENHANCED_TERRAIN_PROFILES'),
    ('sierra_foothills_additions.py', 'SIERRA_FOOTHILLS_ADDITIONS'),
    ('lake_wine_country_additions.py', 'LAKE_WINE_COUNTRY_ADDITIONS'),
    ('socal_additions.py', 'SOCAL_ADDITIONS'),
    ('norcal_additions.py', 'NORCAL_ADDITIONS'),
]

def extract_with_comments(filepath):
    content = open(filepath, encoding='utf-8').read()
    lines = content.split('\n')

    pattern = r'^(\s{4}"[a-z_]+(?:_ca|_communities)":\s*\{)'
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
for fname, dictname in sources:
    fpath = os.path.join(BASE_DIR, fname)
    blocks = extract_with_comments(fpath)
    all_blocks.update(blocks)
    print(f"  {fname}: {len(blocks)} blocks")

print(f"Total blocks: {len(all_blocks)}")

# ============================================================
# Step 2: Organize by region
# ============================================================

regions = [
    ("FEATHER RIVER CANYON / CAMP FIRE CORRIDOR",
     ["paradise_ca", "magalia_ca", "paradise_satellite_communities"]),
    ("SIERRA FOOTHILLS (GOLD COUNTRY)",
     ["grass_valley_ca", "nevada_city_ca", "alta_sierra_ca", "colfax_ca",
      "foresthill_ca", "pollock_pines_ca", "georgetown_ca", "diamond_springs_ca"]),
    ("SONOMA / NAPA WINE COUNTRY",
     ["santa_rosa_ca", "sonoma_ca", "angwin_ca", "calistoga_ca", "kenwood_ca", "glen_ellen_ca"]),
    ("LAKE COUNTY / MENDOCINO",
     ["middletown_ca", "cobb_ca", "clearlake_ca", "lower_lake_ca", "ukiah_outskirts_ca", "willits_ca"]),
    ("FAR NORTHERN CA",
     ["redding_ca", "weed_ca", "dunsmuir_ca", "weaverville_ca", "hayfork_ca"]),
    ("CENTRAL SIERRA / YOSEMITE GATEWAY",
     ["mariposa_ca", "groveland_ca", "three_rivers_ca"]),
    ("SANTA CRUZ MOUNTAINS",
     ["boulder_creek_ca", "ben_lomond_ca", "felton_ca", "bonny_doon_ca", "san_lorenzo_valley_communities"]),
    ("LA BASIN / SAN GABRIEL FOOTHILLS",
     ["malibu_ca", "pacific_palisades_ca", "topanga_ca", "altadena_ca", "la_canada_flintridge_ca"]),
    ("VENTURA / SANTA BARBARA COAST",
     ["ojai_ca", "ventura_ca", "thousand_oaks_ca", "montecito_ca", "carpinteria_ca"]),
    ("SAN BERNARDINO MOUNTAINS",
     ["lake_arrowhead_ca", "crestline_ca", "running_springs_ca", "big_bear_lake_ca",
      "forest_falls_ca", "wrightwood_ca"]),
    ("RIVERSIDE COUNTY MOUNTAINS",
     ["idyllwild_ca", "mountain_center_ca"]),
    ("SAN DIEGO BACKCOUNTRY",
     ["julian_ca", "ramona_ca", "alpine_ca", "valley_center_ca", "fallbrook_ca", "pine_valley_ca"]),
    ("TEHACHAPI / KERN MOUNTAINS",
     ["frazier_park_ca", "pine_mountain_club_ca"]),
]

# ============================================================
# Step 3: Read original ignition + climatology + utilities
# ============================================================

orig_path = os.path.join(DATA_DIR, 'california_profiles.py')
orig = open(orig_path, encoding='utf-8').read()
orig_lines = orig.split('\n')

# Find CA_IGNITION_SOURCES section start
ign_line = None
for i, line in enumerate(orig_lines):
    if 'CA_IGNITION_SOURCES' in line and '=' in line and '{' in line:
        ign_line = i
        break

j = ign_line - 1
while j > 0 and (orig_lines[j].strip().startswith('#') or orig_lines[j].strip() == ''):
    j -= 1
ign_section_start = j + 1

rest_of_file = '\n'.join(orig_lines[ign_section_start:])

# ============================================================
# Step 4: Build the CITY_STATION_MAP extension
# ============================================================

# New city -> nearest ASOS station mappings
new_station_map = {
    # Sierra Foothills
    "alta_sierra_ca": "KAUN",
    "colfax_ca": "KAUN",
    "foresthill_ca": "KAUN",
    "pollock_pines_ca": "KPVF",  # Placerville
    "georgetown_ca": "KPVF",
    "diamond_springs_ca": "KPVF",
    # Lake County / Mendocino
    "middletown_ca": "KSTS",
    "cobb_ca": "KSTS",
    "clearlake_ca": "KSTS",
    "lower_lake_ca": "KSTS",
    "ukiah_outskirts_ca": "KUKI",
    "willits_ca": "KUKI",
    # Napa/Sonoma Wine Country
    "angwin_ca": "KAPC",
    "calistoga_ca": "KAPC",
    "kenwood_ca": "KSTS",
    "glen_ellen_ca": "KSTS",
    # Far Northern CA
    "weed_ca": "KSIS",  # Mt Shasta
    "dunsmuir_ca": "KSIS",
    "weaverville_ca": "KRDD",
    "hayfork_ca": "KRDD",
    # Central Sierra
    "mariposa_ca": "KMCE",  # Merced
    "groveland_ca": "KMCE",
    "three_rivers_ca": "KVIS",  # Visalia
    # Santa Cruz Mountains
    "boulder_creek_ca": "KWVI",  # Watsonville
    "ben_lomond_ca": "KWVI",
    "felton_ca": "KWVI",
    "bonny_doon_ca": "KWVI",
    "san_lorenzo_valley_communities": "KWVI",
    # SoCal additions
    "montecito_ca": "KSBA",
    "carpinteria_ca": "KSBA",
    "running_springs_ca": "KSBD",
    "big_bear_lake_ca": "KSBD",
    "forest_falls_ca": "KSBD",
    "idyllwild_ca": "KPSP",  # Palm Springs
    "mountain_center_ca": "KPSP",
    "alpine_ca": "KRNM",
    "valley_center_ca": "KRNM",
    "fallbrook_ca": "KRNM",
    "pine_valley_ca": "KRNM",
    "frazier_park_ca": "KWJF",
    "pine_mountain_club_ca": "KWJF",
    # Cluster
    "paradise_satellite_communities": "KOVE",
}

# ============================================================
# Step 5: Assemble the file
# ============================================================

# Build region doc lines
region_doc_lines = []
for rname, keys in regions:
    nice_names = []
    for k in keys:
        name = k.replace('_ca', '').replace('_', ' ').title()
        if 'communities' in k.lower():
            name = k.replace('_', ' ').title()
        nice_names.append(name)
    region_doc_lines.append(f"    {rname}:")
    for n in nice_names:
        region_doc_lines.append(f"        {n}")

city_list = '\n'.join(region_doc_lines)

header = '"""\nCalifornia Fire-Vulnerable City Profiles\n'
header += '=' * 41 + '\n\n'
header += 'Comprehensive terrain, evacuation, fire behavior, infrastructure, and demographic\n'
header += 'data for 62 fire-vulnerable cities, towns, and community clusters across California.\n'
header += 'Profiles are derived from NIST case studies, CAL FIRE incident reports, county\n'
header += 'after-action reviews, CWPP documents, and post-fire infrastructure assessments.\n\n'
header += 'Usage:\n'
header += '    from tools.agent_tools.data.california_profiles import (\n'
header += '        CA_TERRAIN_PROFILES,\n'
header += '        CA_IGNITION_SOURCES,\n'
header += '        CA_CLIMATOLOGY,\n'
header += '    )\n\n'
header += f'Cities covered (62 entries across 13 regions):\n{city_list}\n\n'
header += 'Sources:\n'
header += '    - NIST Technical Notes 2135, 2252 (Camp Fire case study & timeline)\n'
header += '    - Lareau et al. 2018 (GRL): Carr Fire pyrotornadogenesis\n'
header += '    - CAL FIRE incident reports (Camp, Tubbs, Nuns, Glass, Carr, Zogg, Fawn,\n'
header += '      Woolsey, Palisades, Eaton, Thomas, Cedar, Witch Creek, CZU, Rim, etc.)\n'
header += '    - Sonoma County AAR (June 2018): October 2017 Complex Fires\n'
header += '    - Sonoma County CWPP 2023 Update (Fire Safe Sonoma)\n'
header += '    - Paradise Irrigation District water quality reports (2019-2020)\n'
header += '    - Butte County Grand Jury 2008 evacuation findings\n'
header += '    - NWS Sacramento post-event summaries (Jarbo Gap wind events)\n'
header += '    - San Diego County post-fire analyses (2003, 2007)\n'
header += '    - Santa Cruz County CZU Lightning Complex AAR\n'
header += '    - Lake County Valley Fire AAR (2015)\n'
header += '    - NOAA/NWS ISD normals, IEM ASOS archive, WRCC climate summaries\n'
header += '"""\n\n'

terrain_start = '# =============================================================================\n'
terrain_start += '# TERRAIN PROFILES -- 62 entries organized by 13 regions\n'
terrain_start += '# =============================================================================\n\n'
terrain_start += 'CA_TERRAIN_PROFILES = {\n'

terrain_body = ''
for rname, keys in regions:
    terrain_body += '\n'
    terrain_body += '    # ' + '=' * 73 + '\n'
    terrain_body += f'    # {rname}\n'
    terrain_body += '    # ' + '=' * 73 + '\n'
    for key in keys:
        if key in all_blocks:
            block = all_blocks[key]
            terrain_body += '\n' + block + '\n'
        else:
            terrain_body += f'\n    # WARNING: missing block for {key}\n'

terrain_end = '\n}\n\n\n'

# Update CITY_STATION_MAP in rest_of_file
# Find and replace the CITY_STATION_MAP section
station_map_new = '\nCITY_STATION_MAP = {\n'
# Original mappings
orig_mappings = {
    "paradise_ca": "KOVE", "magalia_ca": "KOVE",
    "santa_rosa_ca": "KSTS", "sonoma_ca": "KSTS",
    "malibu_ca": "KCMA", "pacific_palisades_ca": "KCMA", "topanga_ca": "KCMA",
    "altadena_ca": "KBUR", "la_canada_flintridge_ca": "KBUR",
    "redding_ca": "KRDD", "ojai_ca": "KOXR", "ventura_ca": "KOXR",
    "lake_arrowhead_ca": "KSBD", "crestline_ca": "KSBD",
    "julian_ca": "KRNM", "ramona_ca": "KRNM",
    "grass_valley_ca": "KAUN", "nevada_city_ca": "KAUN",
    "wrightwood_ca": "KWJF", "thousand_oaks_ca": "KCMA",
}
all_mappings = {**orig_mappings, **new_station_map}
for k in sorted(all_mappings.keys()):
    station_map_new += f'    "{k}": "{all_mappings[k]}",\n'
station_map_new += '}\n'

# Replace old CITY_STATION_MAP in rest_of_file
rest_updated = re.sub(
    r'CITY_STATION_MAP\s*=\s*\{[^}]+\}',
    station_map_new.strip(),
    rest_of_file
)

# Also update the docstring comment about number of cities
rest_updated = rest_updated.replace(
    'Cities covered (18):',
    'Cities covered (62):'
)

# Assemble
output = header + terrain_start + terrain_body + terrain_end + rest_updated

# Write
outpath = os.path.join(DATA_DIR, 'california_profiles.py')
with open(outpath, 'w', encoding='utf-8') as f:
    f.write(output)

lines = output.count('\n')
print(f"\nWritten {len(output):,} chars ({lines:,} lines) to california_profiles.py")
print(f"Terrain profiles: 62 entries")
print(f"Station mappings: {len(all_mappings)}")
