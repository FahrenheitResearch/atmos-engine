"""
Oregon Cross-Section Transect Library — ~35 Presets

Precise lat/lon transect definitions targeting specific terrain features,
wind corridors, fire history paths, and WUI zones across 7 Oregon zones.

Each transect has:
    - start/end coordinates (lat, lon)
    - label (for cross-section titles)
    - description (terrain/fire context)
    - length_km (approximate)
    - orientation (E-W, N-S, NE-SW, etc.)
    - zone_id (which zone it belongs to)

Usage:
    from tools.agent_tools.data.oregon_transects import (
        OREGON_TRANSECTS,
        get_transect,
        get_zone_transects,
    )

    t = get_transect("GORGE-EW")
    print(t["start"], t["end"])

    zone_ts = get_zone_transects("OR-CENTCAS")
    for tid, t in zone_ts.items():
        print(f"{tid}: {t['label']}")
"""

OREGON_TRANSECTS: dict[str, dict] = {

    # =========================================================================
    # OR-GORGE — Columbia Gorge / North Central (4 transects)
    # =========================================================================

    "GORGE-EW": {
        "start": (45.70, -122.20),
        "end": (45.63, -120.80),
        "label": "Columbia Gorge Gap Wind Corridor (E-W)",
        "description": (
            "Full east-west transect through the Columbia River Gorge from "
            "Troutdale to The Dalles. Captures the pressure-gradient-driven "
            "gap wind corridor where Cascade Range funnels air through the "
            "only sea-level break in the mountain chain. Wind speeds routinely "
            "exceed 50 mph during east wind events."
        ),
        "length_km": 115,
        "orientation": "E-W",
        "zone_id": "OR-GORGE",
        "key_features": [
            "Crown Point narrows", "Hood River compression zone",
            "Rowena Gap acceleration", "The Dalles exit region",
        ],
    },

    "GORGE-NS": {
        "start": (45.80, -121.18),
        "end": (45.05, -121.10),
        "label": "Gorge to Grassland (N-S, Deschutes Canyon)",
        "description": (
            "North-south transect from the Columbia River at The Dalles "
            "southward through the Deschutes River canyon into the high-desert "
            "grasslands around Maupin. Captures terrain-channeled winds in the "
            "Deschutes canyon that drive grass fires."
        ),
        "length_km": 85,
        "orientation": "N-S",
        "zone_id": "OR-GORGE",
        "key_features": [
            "Columbia River floodplain", "Deschutes River canyon entrance",
            "Tygh Valley side canyon", "Maupin grass fire zone",
        ],
    },

    "HOODRIVER-VALLEY": {
        "start": (45.80, -121.58),
        "end": (45.35, -121.65),
        "label": "Hood River Valley (N-S)",
        "description": (
            "Hood River Valley from the Columbia River south toward Mt. Hood. "
            "Orchard and forest transition zone. Thermal belt creates complex "
            "wind patterns. Valley acts as funnel for east wind events."
        ),
        "length_km": 52,
        "orientation": "N-S",
        "zone_id": "OR-GORGE",
        "key_features": [
            "Hood River town center", "Upper Valley orchards",
            "Mt. Hood foothills", "Cooper Spur approach",
        ],
    },

    "DUFUR-MAUPIN": {
        "start": (45.46, -121.13),
        "end": (45.08, -121.03),
        "label": "Dufur-Maupin Grass Fire Corridor",
        "description": (
            "Northeast-trending grass fire corridor from Dufur through the "
            "wheatlands to Maupin. This terrain produces fast-moving grass "
            "fires when NW winds push through the Gorge. Continuous fine fuels "
            "with minimal firebreaks."
        ),
        "length_km": 44,
        "orientation": "N-S",
        "zone_id": "OR-GORGE",
        "key_features": [
            "Dufur wheatlands", "Tygh Ridge", "White River canyon",
            "Maupin approach",
        ],
    },

    # =========================================================================
    # OR-CENTCAS — Central Oregon Cascades (6 transects)
    # =========================================================================

    "CENTCAS-RAINSHADOW": {
        "start": (44.30, -122.10),
        "end": (44.25, -120.80),
        "label": "Cascade Rain Shadow (W-E through Sisters)",
        "description": (
            "West-to-east transect from the Cascade crest through Sisters to "
            "the high desert east of Redmond. Captures the dramatic rain shadow "
            "transition: 80+ inches of precipitation on the west slope to <12 "
            "inches at Redmond in just 50 miles. Ponderosa pine belt is the "
            "critical WUI zone."
        ),
        "length_km": 105,
        "orientation": "E-W",
        "zone_id": "OR-CENTCAS",
        "key_features": [
            "Cascade crest (5,200 ft)", "McKenzie Pass",
            "Sisters ponderosa belt", "Redmond high desert",
        ],
    },

    "BEND-WUI": {
        "start": (44.12, -121.55),
        "end": (44.00, -121.20),
        "label": "Bend WUI Western Approach",
        "description": (
            "West-to-east transect through Bend's most vulnerable WUI zone. "
            "From Deschutes National Forest through Shevlin Park, Skyline "
            "Forest, and Phil's Trail into the west-side neighborhoods. "
            "Two Bulls Fire (2014, 6,900 acres) burned through this corridor."
        ),
        "length_km": 30,
        "orientation": "E-W",
        "zone_id": "OR-CENTCAS",
        "key_features": [
            "Tumalo Creek drainage", "Shevlin Park",
            "Skyline Forest (Two Bulls 2014)", "West Bend residential",
        ],
    },

    "CENTURY-BACHELOR": {
        "start": (43.98, -121.69),
        "end": (44.05, -121.35),
        "label": "Century Drive / Mt. Bachelor Corridor",
        "description": (
            "Southwest-northeast transect along the Century Drive corridor "
            "from Mt. Bachelor toward Bend. Dead-end evacuation route through "
            "continuous national forest. 15,000+ recreation visitors on peak "
            "days with single-road egress."
        ),
        "length_km": 30,
        "orientation": "SW-NE",
        "zone_id": "OR-CENTCAS",
        "key_features": [
            "Mt. Bachelor base area", "Dutchman Flat",
            "Cascade Lakes Highway junction", "SW Bend approach",
        ],
    },

    "US97-CORRIDOR": {
        "start": (44.35, -121.19),
        "end": (43.55, -121.50),
        "label": "US-97 Fire Corridor (Redmond to Chemult)",
        "description": (
            "North-south transect along the US-97 corridor from Redmond "
            "through Bend, Sunriver, La Pine, and south toward Chemult. "
            "Continuous ponderosa pine/lodgepole forest along both sides of "
            "the highway. Fires crossing US-97 cut off evacuation routes for "
            "tens of thousands of residents."
        ),
        "length_km": 95,
        "orientation": "N-S",
        "zone_id": "OR-CENTCAS",
        "key_features": [
            "Redmond juniper belt", "Bend ponderosa",
            "Sunriver resort", "La Pine WUI", "Newberry Crater rim",
        ],
    },

    "SISTERS-CAMPSHERMAN": {
        "start": (44.29, -121.55),
        "end": (44.46, -121.65),
        "label": "Sisters to Camp Sherman Drainage",
        "description": (
            "South-to-north transect from Sisters through the Metolius "
            "River drainage to Camp Sherman. Old-growth ponderosa and "
            "mixed conifer with extremely limited road access. Camp Sherman "
            "has effectively one evacuation route (FR 14)."
        ),
        "length_km": 22,
        "orientation": "S-N",
        "zone_id": "OR-CENTCAS",
        "key_features": [
            "Sisters city limits", "Indian Ford Creek",
            "Metolius Basin", "Camp Sherman (single-road community)",
        ],
    },

    "NEWBERRY": {
        "start": (43.72, -121.25),
        "end": (43.65, -121.60),
        "label": "Newberry Volcanic Zone",
        "description": (
            "East-west transect across the Newberry Volcanic Monument area "
            "south of Bend. Lodgepole pine and pumice flats with high fire "
            "potential. Fires in this area threaten La Pine and southern "
            "Deschutes County."
        ),
        "length_km": 30,
        "orientation": "E-W",
        "zone_id": "OR-CENTCAS",
        "key_features": [
            "Newberry caldera rim", "Paulina Creek drainage",
            "Lodgepole pine flats", "La Pine approach from east",
        ],
    },

    # =========================================================================
    # OR-CASCREST — Cascade Crest Corridor (5 transects)
    # =========================================================================

    "NSANTIAM-CANYON": {
        "start": (44.75, -122.70),
        "end": (44.72, -121.90),
        "label": "North Santiam Canyon (Beachie Creek Fire Path)",
        "description": (
            "West-to-east transect through the N. Santiam Canyon following "
            "the path of the Beachie Creek Fire (2020, 193,573 acres). "
            "From Gates through Detroit to the Cascade crest. The fire "
            "destroyed 90% of Detroit and Gates in a single east wind event "
            "on September 7-8, 2020, traveling 15+ miles in 12 hours."
        ),
        "length_km": 65,
        "orientation": "E-W",
        "zone_id": "OR-CASCREST",
        "key_features": [
            "Gates (destroyed 2020)", "Detroit Lake reservoir",
            "Detroit town site (destroyed 2020)", "Breitenbush corridor",
            "Cascade crest",
        ],
    },

    "MCKENZIE-CANYON": {
        "start": (44.16, -122.70),
        "end": (44.20, -121.90),
        "label": "McKenzie Canyon (Holiday Farm Fire Path)",
        "description": (
            "West-to-east through the McKenzie River canyon following the "
            "Holiday Farm Fire (2020, 173,393 acres). The fire ran 30+ miles "
            "in a single night down-canyon from the Cascades to Springfield "
            "suburbs. Blue River and Vida were largely destroyed."
        ),
        "length_km": 65,
        "orientation": "E-W",
        "zone_id": "OR-CASCREST",
        "key_features": [
            "Vida community", "Blue River (destroyed 2020)",
            "McKenzie Bridge", "Clear Lake approach",
            "Cascade crest east of McKenzie Pass",
        ],
    },

    "MF-WILLAMETTE": {
        "start": (43.75, -122.70),
        "end": (43.72, -122.10),
        "label": "Middle Fork Willamette (Oakridge Corridor)",
        "description": (
            "West-to-east along the Middle Fork Willamette canyon from "
            "Oakridge east toward the Cascade crest at Willamette Pass. "
            "Narrow canyon with limited evacuation routes. Oakridge is "
            "surrounded by continuous national forest timber."
        ),
        "length_km": 50,
        "orientation": "E-W",
        "zone_id": "OR-CASCREST",
        "key_features": [
            "Oakridge town center", "Hills Creek Reservoir",
            "Salt Creek Falls area", "Willamette Pass approach",
        ],
    },

    "CASCREST-NS": {
        "start": (44.85, -122.10),
        "end": (43.60, -122.15),
        "label": "Cascade Crest N-S (Detroit to Diamond Peak)",
        "description": (
            "North-south transect along the Cascade crest from the "
            "Mt. Jefferson area south to Diamond Peak. Captures the "
            "ridge-top wind regime that drives east-side fire runs "
            "down western canyons during east wind events."
        ),
        "length_km": 140,
        "orientation": "N-S",
        "zone_id": "OR-CASCREST",
        "key_features": [
            "Mt. Jefferson (10,495 ft)", "Santiam Pass",
            "Three Sisters Wilderness", "Waldo Lake",
            "Diamond Peak", "Willamette Pass",
        ],
    },

    "LABORDAY-EW": {
        "start": (44.50, -123.00),
        "end": (44.50, -121.50),
        "label": "Labor Day East Wind Full Transect",
        "description": (
            "Full east-west transect from the Willamette Valley across "
            "the Cascades. Captures the complete atmospheric structure "
            "during east wind events like September 7-8, 2020, when fires "
            "burned from the crest to the valley in a single night. "
            "Shows the upper-level downslope wind jet."
        ),
        "length_km": 130,
        "orientation": "E-W",
        "zone_id": "OR-CASCREST",
        "key_features": [
            "Willamette Valley floor", "Western Cascade foothills",
            "Canyon entrances (Santiam/McKenzie)", "Cascade crest",
            "Upper-level downslope jet",
        ],
    },

    # =========================================================================
    # OR-ROGUE — Southern Oregon / Rogue Valley (5 transects)
    # =========================================================================

    "ROGUE-NS": {
        "start": (42.55, -122.87),
        "end": (42.10, -122.72),
        "label": "Rogue Valley N-S (Almeda Fire Corridor)",
        "description": (
            "North-south through the Rogue Valley along the Bear Creek / "
            "I-5 corridor. Follows the path of the Almeda Fire (2020, "
            "3,200 acres) which destroyed 2,500+ structures in Talent and "
            "Phoenix. The fire ran 13 miles in 8 hours driven by terrain- "
            "channeled north winds."
        ),
        "length_km": 52,
        "orientation": "N-S",
        "zone_id": "OR-ROGUE",
        "key_features": [
            "Grants Pass approach", "Gold Hill", "Central Point",
            "Medford", "Phoenix (destroyed 2020)", "Talent (destroyed 2020)",
            "Ashland foothills",
        ],
    },

    "SISKIYOU-I5": {
        "start": (42.25, -122.60),
        "end": (41.95, -122.55),
        "label": "Siskiyou Pass / I-5 Corridor",
        "description": (
            "South from Ashland over the Siskiyou Pass into California. "
            "Terrain funnels winds through the pass creating fire weather "
            "conditions. Critical transportation corridor — I-5 closure "
            "isolates southern Oregon from California."
        ),
        "length_km": 35,
        "orientation": "N-S",
        "zone_id": "OR-ROGUE",
        "key_features": [
            "Ashland watershed", "Emigrant Lake",
            "Siskiyou Summit (4,310 ft)", "I-5 corridor",
        ],
    },

    "BEARCREEK": {
        "start": (42.45, -122.95),
        "end": (42.18, -122.70),
        "label": "Bear Creek Corridor (Almeda Path Detail)",
        "description": (
            "Detailed transect of the Bear Creek corridor from north of "
            "Medford through Phoenix and Talent to Ashland. The exact "
            "path of the Almeda Fire. Urban-wildland intermix with "
            "continuous fuels along the creek."
        ),
        "length_km": 35,
        "orientation": "NW-SE",
        "zone_id": "OR-ROGUE",
        "key_features": [
            "Bear Creek greenway", "Phoenix mobile home parks",
            "Talent city center", "Ashland interface",
        ],
    },

    "APPLEGATE": {
        "start": (42.30, -123.40),
        "end": (42.05, -122.95),
        "label": "Applegate Valley",
        "description": (
            "Southwest-to-northeast through the Applegate Valley from "
            "Grants Pass area to Jacksonville. Wine country and rural "
            "residential in continuous oak/conifer fuels. Multiple "
            "historical fires in this valley."
        ),
        "length_km": 45,
        "orientation": "SW-NE",
        "zone_id": "OR-ROGUE",
        "key_features": [
            "Applegate River canyon", "Williams Creek",
            "Jacksonville historic district", "Ruch community",
        ],
    },

    "ROGUE-EW": {
        "start": (42.33, -123.50),
        "end": (42.33, -122.45),
        "label": "Rogue Valley E-W Cross-Valley",
        "description": (
            "Full east-west transect across the Rogue Valley from the "
            "Coast Range through Grants Pass, Medford, and into the "
            "Cascades. Shows the thermal trough that makes the Rogue "
            "Valley the hottest location in Oregon (115F record)."
        ),
        "length_km": 85,
        "orientation": "E-W",
        "zone_id": "OR-ROGUE",
        "key_features": [
            "Coast Range western slope", "Grants Pass",
            "Rogue River floodplain", "Medford central valley",
            "Cascade foothills east of Ashland",
        ],
    },

    # =========================================================================
    # OR-KLAMATH — Klamath Basin / High Desert (4 transects)
    # =========================================================================

    "KLAMATH-EW": {
        "start": (42.22, -122.30),
        "end": (42.20, -120.80),
        "label": "Klamath Basin E-W (Cascades to Desert)",
        "description": (
            "East-west transect from the eastern Cascades through Klamath "
            "Falls to the high desert beyond Bonanza. Captures the transition "
            "from mountain timber to basin grassland to desert sagebrush."
        ),
        "length_km": 120,
        "orientation": "E-W",
        "zone_id": "OR-KLAMATH",
        "key_features": [
            "Eastern Cascade slope", "Upper Klamath Lake",
            "Klamath Falls", "Bonanza grassland",
            "Langell Valley", "High desert transition",
        ],
    },

    "BOOTLEG-NS": {
        "start": (42.80, -121.20),
        "end": (42.10, -121.10),
        "label": "Bootleg Fire Zone N-S",
        "description": (
            "North-south through the Bootleg Fire (2021, 413,765 acres) "
            "zone from Chiloquin south to near Bonanza. The largest US fire "
            "of 2021 created its own weather (pyrocumulonimbus) and burned "
            "through juniper, sagebrush, and ponderosa pine."
        ),
        "length_km": 80,
        "orientation": "N-S",
        "zone_id": "OR-KLAMATH",
        "key_features": [
            "Chiloquin / Sprague River", "Sycan Marsh",
            "Bootleg Fire perimeter center", "Yamsay Mountain",
        ],
    },

    "SUMMERLAKE": {
        "start": (42.95, -120.80),
        "end": (42.35, -120.30),
        "label": "Summer Lake Grassland Corridor",
        "description": (
            "North-south through the Summer Lake and Paisley area. "
            "High-desert grassland with extreme fire weather potential. "
            "Continental climate with RH dropping below 5% in summer. "
            "Lightning-caused fires spread rapidly in continuous grass."
        ),
        "length_km": 75,
        "orientation": "N-S",
        "zone_id": "OR-KLAMATH",
        "key_features": [
            "Summer Lake playa", "Paisley community",
            "Winter Ridge escarpment", "Chewaucan River valley",
        ],
    },

    "KLAMATH-GORGE": {
        "start": (42.30, -122.15),
        "end": (42.05, -121.80),
        "label": "Klamath River Gorge",
        "description": (
            "Southwest through the Klamath River gorge south of "
            "Klamath Falls into the river canyon. Terrain channels "
            "winds along the river creating fire runs in steep, "
            "inaccessible terrain."
        ),
        "length_km": 40,
        "orientation": "NE-SW",
        "zone_id": "OR-KLAMATH",
        "key_features": [
            "Klamath Falls south", "Keno community",
            "Klamath River canyon", "John C. Boyle reservoir",
        ],
    },

    # =========================================================================
    # OR-BLUES — NE Oregon Blue Mountains (4 transects)
    # =========================================================================

    "BLUES-EW": {
        "start": (44.80, -119.20),
        "end": (44.80, -117.20),
        "label": "Blue Mountains E-W",
        "description": (
            "Full east-west transect through the Blue Mountains from "
            "the Ochoco country east to Baker City. Crosses the highest "
            "terrain in NE Oregon with heavy timber stands subject to "
            "lightning-caused fires. Remote terrain, limited access."
        ),
        "length_km": 160,
        "orientation": "E-W",
        "zone_id": "OR-BLUES",
        "key_features": [
            "Ochoco National Forest", "Aldrich Mountains",
            "John Day Valley", "Strawberry Mountain (9,038 ft)",
            "Elkhorn Range", "Baker City approach",
        ],
    },

    "GRANDERONDE": {
        "start": (45.50, -118.30),
        "end": (45.10, -117.90),
        "label": "Grande Ronde Valley",
        "description": (
            "North-south through the Grande Ronde Valley centered on "
            "La Grande. Surrounded by the Blue Mountains, this valley "
            "creates a thermal low that draws winds from surrounding "
            "canyons. Interface between agricultural land and forest."
        ),
        "length_km": 50,
        "orientation": "N-S",
        "zone_id": "OR-BLUES",
        "key_features": [
            "Mt. Emily (fire approach from north)", "La Grande city",
            "Grande Ronde River", "Catherine Creek drainage",
        ],
    },

    "WALLOWA": {
        "start": (45.55, -117.50),
        "end": (45.20, -117.05),
        "label": "Wallowa Mountains",
        "description": (
            "Northwest-southeast transect from Enterprise into the "
            "Wallowa Mountains. Remote wilderness terrain with the "
            "steepest, most glaciated mountains in Oregon. Lightning "
            "fires in backcountry; Joseph and Enterprise at WUI."
        ),
        "length_km": 50,
        "orientation": "NW-SE",
        "zone_id": "OR-BLUES",
        "key_features": [
            "Enterprise (gateway town)", "Joseph town",
            "Wallowa Lake moraines", "Eagle Cap Wilderness approach",
        ],
    },

    "JOHNDAY-OCHOCO": {
        "start": (44.42, -119.10),
        "end": (44.42, -118.30),
        "label": "John Day / Ochoco Country",
        "description": (
            "East-west transect through the John Day area and Ochoco "
            "Mountains. Canyon terrain with juniper woodlands transitioning "
            "to ponderosa pine. Multiple large fires in recent decades."
        ),
        "length_km": 65,
        "orientation": "E-W",
        "zone_id": "OR-BLUES",
        "key_features": [
            "Ochoco Mountains", "Mitchell community",
            "John Day town", "Canyon City", "Strawberry Range approach",
        ],
    },

    # =========================================================================
    # OR-COASTWV — Coast Range / Willamette Interface (3 transects)
    # =========================================================================

    "COASTRANGE-EW": {
        "start": (43.98, -124.00),
        "end": (44.00, -122.60),
        "label": "Coast Range E-W (Florence to Eugene)",
        "description": (
            "Full east-west transect from the Oregon coast through the "
            "Coast Range to the Willamette Valley. Shows the marine layer "
            "intrusion and how east wind events push dry air over the "
            "Coast Range, creating extreme fire danger in normally-wet "
            "timber. Tillamook Burns (1930s-50s) demonstrate the risk."
        ),
        "length_km": 115,
        "orientation": "E-W",
        "zone_id": "OR-COASTWV",
        "key_features": [
            "Florence coastal zone", "Siuslaw River corridor",
            "Coast Range summit", "Fern Ridge area",
            "Willamette Valley floor (Eugene/Springfield)",
        ],
    },

    "UMPQUA-VALLEY": {
        "start": (43.22, -123.80),
        "end": (43.22, -122.60),
        "label": "Umpqua Valley (Roseburg Corridor)",
        "description": (
            "East-west transect through the Umpqua Valley centered on "
            "Roseburg. Drier than the Willamette Valley, this is one of "
            "Oregon's more fire-prone west-side valleys. Terrain funnels "
            "hot air from the Rogue Valley through the Canyon Creek area."
        ),
        "length_km": 95,
        "orientation": "E-W",
        "zone_id": "OR-COASTWV",
        "key_features": [
            "Coast Range western slope", "Roseburg city center",
            "South Umpqua River", "Cow Creek canyon",
            "Diamond Lake approach",
        ],
    },

    "SWEETHOME-SSANTIAM": {
        "start": (44.40, -122.95),
        "end": (44.38, -122.20),
        "label": "Sweet Home / South Santiam Corridor",
        "description": (
            "East-west through the South Santiam canyon from Sweet Home "
            "toward the Cascades. Sweet Home sits at the canyon mouth "
            "where east winds accelerate into the Willamette Valley. "
            "Narrow canyon with continuous timber fuels."
        ),
        "length_km": 60,
        "orientation": "E-W",
        "zone_id": "OR-COASTWV",
        "key_features": [
            "Sweet Home town center", "Green Peter Reservoir",
            "Cascadia community", "South Santiam canyon narrows",
        ],
    },
}


# =============================================================================
# Helper functions
# =============================================================================

def get_transect(transect_id: str) -> dict:
    """Get a transect by ID. Raises KeyError if not found."""
    if transect_id not in OREGON_TRANSECTS:
        raise KeyError(
            f"Unknown transect '{transect_id}'. "
            f"Valid IDs: {list(OREGON_TRANSECTS.keys())}"
        )
    return OREGON_TRANSECTS[transect_id]


def get_zone_transects(zone_id: str) -> dict[str, dict]:
    """Get all transects for a specific zone."""
    return {
        tid: t for tid, t in OREGON_TRANSECTS.items()
        if t["zone_id"] == zone_id
    }


def list_transects() -> list[dict]:
    """List all transects with summary info."""
    return [
        {
            "id": tid,
            "label": t["label"],
            "zone_id": t["zone_id"],
            "orientation": t["orientation"],
            "length_km": t["length_km"],
        }
        for tid, t in OREGON_TRANSECTS.items()
    ]


def get_transect_coords(transect_id: str) -> tuple[tuple[float, float], tuple[float, float]]:
    """Get (start, end) coordinate tuples for a transect."""
    t = get_transect(transect_id)
    return (tuple(t["start"]), tuple(t["end"]))
