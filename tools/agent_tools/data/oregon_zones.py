"""
Oregon WFO Coverage Zones — 7 Zones, ~40 Towns

Each zone defines: towns with coordinates, METAR/RAWS stations, NWS WFOs,
transect IDs (referencing oregon_transects.py), and geographic bounds.

Usage:
    from tools.agent_tools.data.oregon_zones import OREGON_ZONES, get_zone

    zone = get_zone("OR-CENTCAS")
    for town, (lat, lon) in zone.towns.items():
        print(f"{town}: {lat}, {lon}")
"""
from tools.agent_tools.wfo_swarm.config import ZoneConfig


# =============================================================================
# Zone definitions
# =============================================================================

OREGON_ZONES: dict[str, ZoneConfig] = {

    # =========================================================================
    # OR-GORGE — Columbia Gorge / North Central Oregon
    # =========================================================================
    "OR-GORGE": ZoneConfig(
        zone_id="OR-GORGE",
        name="Columbia Gorge / North Central",
        description=(
            "Columbia River Gorge gap wind corridor and north-central Oregon "
            "grasslands. Dramatic pressure-gradient-driven winds through the Gorge "
            "create extreme fire weather. Terrain transitions from Gorge cliffs to "
            "Deschutes River canyon to high-desert grassland."
        ),
        towns={
            "Hood River":   (45.7054, -121.5215),
            "The Dalles":   (45.5946, -121.1787),
            "Mosier":       (45.6837, -121.3997),
            "Maupin":       (45.1754, -121.0795),
            "Dufur":        (45.4571, -121.1292),
            "Grass Valley": (45.3054, -120.7534),
        },
        wfos=["PDX", "PQR"],
        metar_stations=["KDLS", "S21", "4S2"],
        raws_search_points=[
            (45.65, -121.35, 50),  # mid-Gorge
            (45.30, -121.10, 40),  # Dufur/Maupin area
        ],
        transect_ids=[
            "GORGE-EW", "GORGE-NS", "HOODRIVER-VALLEY", "DUFUR-MAUPIN",
        ],
        priority_transects=["GORGE-EW", "DUFUR-MAUPIN"],
        bounds={"n": 45.80, "s": 45.05, "e": -120.50, "w": -121.80},
    ),

    # =========================================================================
    # OR-CENTCAS — Central Oregon Cascades
    # =========================================================================
    "OR-CENTCAS": ZoneConfig(
        zone_id="OR-CENTCAS",
        name="Central Oregon Cascades",
        description=(
            "Cascade Range rain shadow zone from Sisters to La Pine. Extensive "
            "WUI exposure in ponderosa pine. Bend is Oregon's largest WUI city. "
            "US-97 corridor creates continuous fire risk from Redmond to Chemult."
        ),
        towns={
            "Bend":         (44.0582, -121.3153),
            "Sisters":      (44.2907, -121.5493),
            "Camp Sherman": (44.4640, -121.6510),
            "La Pine":      (43.6804, -121.5036),
            "Sunriver":     (43.8840, -121.4350),
            "Redmond":      (44.2726, -121.1739),
        },
        wfos=["PDX", "BOI"],
        metar_stations=["KRDM", "KBDN", "6S0"],
        raws_search_points=[
            (44.10, -121.40, 40),  # Bend area
            (44.30, -121.55, 30),  # Sisters area
            (43.80, -121.50, 30),  # La Pine / Sunriver
        ],
        transect_ids=[
            "CENTCAS-RAINSHADOW", "BEND-WUI", "CENTURY-BACHELOR",
            "US97-CORRIDOR", "SISTERS-CAMPSHERMAN", "NEWBERRY",
        ],
        priority_transects=["CENTCAS-RAINSHADOW", "BEND-WUI", "US97-CORRIDOR"],
        bounds={"n": 44.55, "s": 43.55, "e": -121.00, "w": -121.90},
    ),

    # =========================================================================
    # OR-CASCREST — Cascade Crest Corridor (2020 fire zones)
    # =========================================================================
    "OR-CASCREST": ZoneConfig(
        zone_id="OR-CASCREST",
        name="Cascade Crest Corridor",
        description=(
            "Western Cascade foothills canyon communities devastated by 2020 Labor "
            "Day fires. Canyon wind tunnels (N. Santiam, McKenzie, M.F. Willamette) "
            "create extreme fire runs during east wind events. Detroit, Blue River, "
            "and Vida were largely destroyed in September 2020."
        ),
        towns={
            "Detroit":          (44.7352, -122.1531),
            "Gates":            (44.7502, -122.4069),
            "Blue River":       (44.1626, -122.3398),
            "Oakridge":         (43.7465, -122.4610),
            "McKenzie Bridge":  (44.1826, -122.1260),
            "Vida":             (44.1196, -122.5136),
        },
        wfos=["PQR", "MFR"],
        metar_stations=["KEUG", "KRBG", "KSLE"],
        raws_search_points=[
            (44.74, -122.15, 30),  # Detroit area
            (44.16, -122.30, 30),  # Blue River / McKenzie
            (43.75, -122.46, 30),  # Oakridge
        ],
        transect_ids=[
            "NSANTIAM-CANYON", "MCKENZIE-CANYON", "MF-WILLAMETTE",
            "CASCREST-NS", "LABORDAY-EW",
        ],
        priority_transects=["NSANTIAM-CANYON", "MCKENZIE-CANYON", "LABORDAY-EW"],
        bounds={"n": 44.85, "s": 43.60, "e": -121.90, "w": -122.80},
    ),

    # =========================================================================
    # OR-ROGUE — Southern Oregon / Rogue Valley
    # =========================================================================
    "OR-ROGUE": ZoneConfig(
        zone_id="OR-ROGUE",
        name="Southern Oregon / Rogue Valley",
        description=(
            "Rogue Valley heat corridor from Grants Pass to Ashland. The Almeda "
            "Fire (2020) destroyed most of Talent and Phoenix, racing 13 miles "
            "along Bear Creek / I-5 corridor in 8 hours. Siskiyou Pass creates "
            "terrain-channeled north winds. Hottest, driest summer climate in Oregon."
        ),
        towns={
            "Medford":      (42.3265, -122.8756),
            "Ashland":      (42.1946, -122.7095),
            "Talent":       (42.2457, -122.7878),
            "Phoenix":      (42.2751, -122.8189),
            "Grants Pass":  (42.4390, -123.3284),
            "Jacksonville": (42.3134, -122.9668),
        },
        wfos=["MFR"],
        metar_stations=["KMFR", "3S4", "KOTH"],
        raws_search_points=[
            (42.30, -122.85, 40),  # Medford area
            (42.44, -123.33, 30),  # Grants Pass
            (42.20, -122.71, 20),  # Ashland
        ],
        transect_ids=[
            "ROGUE-NS", "SISKIYOU-I5", "BEARCREEK", "APPLEGATE", "ROGUE-EW",
        ],
        priority_transects=["ROGUE-NS", "BEARCREEK", "SISKIYOU-I5"],
        bounds={"n": 42.55, "s": 42.05, "e": -122.45, "w": -123.50},
    ),

    # =========================================================================
    # OR-KLAMATH — Klamath Basin / High Desert
    # =========================================================================
    "OR-KLAMATH": ZoneConfig(
        zone_id="OR-KLAMATH",
        name="Klamath Basin / High Desert",
        description=(
            "Klamath Basin east of the Cascades: high-desert terrain with extreme "
            "lightning-fire risk. Bootleg Fire (2021, 413,765 acres) was the largest "
            "US fire that year. Summer Lake grassland corridor. Continental climate "
            "with low humidity and high wind events."
        ),
        towns={
            "Klamath Falls": (42.2249, -121.7817),
            "Lakeview":      (42.1888, -120.3455),
            "Chiloquin":     (42.5779, -121.8667),
            "Bonanza":       (42.1962, -121.4077),
            "Bly":           (42.3971, -120.9977),
            "Paisley":       (42.6912, -120.5427),
        },
        wfos=["MFR", "BOI"],
        metar_stations=["KLMT", "KLKV"],
        raws_search_points=[
            (42.22, -121.78, 50),  # Klamath Falls
            (42.40, -120.99, 40),  # Bly / Bootleg area
            (42.19, -120.35, 40),  # Lakeview
        ],
        transect_ids=[
            "KLAMATH-EW", "BOOTLEG-NS", "SUMMERLAKE", "KLAMATH-GORGE",
        ],
        priority_transects=["KLAMATH-EW", "BOOTLEG-NS"],
        bounds={"n": 42.80, "s": 42.05, "e": -120.10, "w": -122.10},
    ),

    # =========================================================================
    # OR-BLUES — NE Oregon Blue Mountains
    # =========================================================================
    "OR-BLUES": ZoneConfig(
        zone_id="OR-BLUES",
        name="NE Oregon Blue Mountains",
        description=(
            "Blue Mountains and high valleys of NE Oregon. Remote timber country "
            "with limited evacuation routes. Wallowa Mountains, Grande Ronde Valley, "
            "and John Day/Ochoco country. Continental climate with afternoon "
            "thunderstorms driving lightning-caused fires in backcountry."
        ),
        towns={
            "Pendleton":   (45.6721, -118.7886),
            "La Grande":   (45.3246, -118.0878),
            "Baker City":  (44.7749, -117.8344),
            "Enterprise":  (45.4268, -117.2788),
            "Joseph":      (45.3543, -117.2296),
            "John Day":    (44.4160, -118.9530),
            "Canyon City": (44.3907, -118.9498),
            "Prairie City": (44.4571, -118.7124),
        },
        wfos=["PDT", "BOI"],
        metar_stations=["KPDT", "KLGD", "KBKE", "KEJO"],
        raws_search_points=[
            (45.33, -118.09, 40),  # La Grande
            (44.78, -117.83, 40),  # Baker City
            (45.40, -117.25, 40),  # Enterprise/Joseph
            (44.42, -118.95, 40),  # John Day
        ],
        transect_ids=[
            "BLUES-EW", "GRANDERONDE", "WALLOWA", "JOHNDAY-OCHOCO",
        ],
        priority_transects=["BLUES-EW", "WALLOWA"],
        bounds={"n": 45.80, "s": 44.25, "e": -117.00, "w": -119.20},
    ),

    # =========================================================================
    # OR-COASTWV — Coast Range / Willamette Valley Interface
    # =========================================================================
    "OR-COASTWV": ZoneConfig(
        zone_id="OR-COASTWV",
        name="Coast Range / Willamette Interface",
        description=(
            "Coast Range to Willamette Valley transition. Marine layer intrusion "
            "usually suppresses fire, but east wind events (especially Sept/Oct) "
            "can produce extreme fire behavior in Coast Range timber. Roseburg is "
            "in the dry Umpqua Valley. Sweet Home and Cottage Grove sit at canyon "
            "mouths feeding from the Cascades."
        ),
        towns={
            "Sweet Home":    (44.3968, -122.7351),
            "Roseburg":      (43.2165, -123.3417),
            "Florence":      (43.9826, -124.0998),
            "Cottage Grove": (43.7976, -123.0595),
            "Drain":         (43.6590, -123.3184),
            "Myrtle Creek":  (42.9957, -123.2917),
        },
        wfos=["PQR", "MFR"],
        metar_stations=["KRBG", "KEUG", "6S2", "KONP"],
        raws_search_points=[
            (44.40, -122.74, 30),  # Sweet Home
            (43.22, -123.34, 40),  # Roseburg
            (43.98, -124.10, 30),  # Florence / coast
        ],
        transect_ids=[
            "COASTRANGE-EW", "UMPQUA-VALLEY", "SWEETHOME-SSANTIAM",
        ],
        priority_transects=["COASTRANGE-EW", "UMPQUA-VALLEY"],
        bounds={"n": 44.55, "s": 42.85, "e": -122.50, "w": -124.20},
    ),
}


# =============================================================================
# Helper functions
# =============================================================================

def get_zone(zone_id: str) -> ZoneConfig:
    """Get a zone config by ID. Raises KeyError if not found."""
    if zone_id not in OREGON_ZONES:
        raise KeyError(
            f"Unknown zone '{zone_id}'. Valid zones: {list(OREGON_ZONES.keys())}"
        )
    return OREGON_ZONES[zone_id]


def list_zones() -> list[dict]:
    """List all zones with summary info."""
    return [
        {
            "zone_id": z.zone_id,
            "name": z.name,
            "town_count": z.town_count,
            "transect_count": z.transect_count,
            "towns": list(z.towns.keys()),
        }
        for z in OREGON_ZONES.values()
    ]


def get_all_towns() -> dict[str, tuple[float, float]]:
    """Get all towns across all zones with coordinates."""
    towns = {}
    for zone in OREGON_ZONES.values():
        for town, coords in zone.towns.items():
            towns[f"{town} ({zone.zone_id})"] = coords
    return towns


def get_zone_for_town(town_name: str) -> ZoneConfig | None:
    """Find which zone a town belongs to (case-insensitive search)."""
    town_lower = town_name.lower()
    for zone in OREGON_ZONES.values():
        for t in zone.towns:
            if t.lower() == town_lower:
                return zone
    return None
