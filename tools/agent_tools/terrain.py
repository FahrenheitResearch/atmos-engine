"""
Terrain Analysis Module for AI Agents

Analyzes topographic complexity around a point to help agents understand
the REAL firefighting difficulty of an area -- not just point elevation.

Motivation: A firefighter reviewing our Amarillo fire weather report said:
"What this really fails to highlight is that it all looks like flat grassland,
but in the river valleys and canyon valleys, it's absolute hell to fight the
fires." The report highlighted East Amarillo but the real danger is North,
West, and SE where canyons and terrain make firefighting extremely difficult.

This module:
  1. Shoots 8 elevation profiles outward from a center point
  2. Computes relief, slope, valley count, and canyon features per direction
  3. Classifies terrain (flat_grassland, rolling_hills, mixed_canyon_grassland,
     canyon_country, mountainous)
  4. Generates fire behavior implications from terrain features
  5. Includes hardcoded expert knowledge for key fire-prone cities

Usage:
    from tools.agent_tools.terrain import (
        analyze_terrain_complexity,
        city_terrain_assessment,
        CITY_TERRAIN_PROFILES,
    )

    # Raw terrain analysis from elevation data
    result = analyze_terrain_complexity(35.22, -101.83, radius_km=15)
    print(result["summary"]["terrain_class"])
    print(result["fire_implications"])

    # Full city assessment with expert knowledge + elevation data
    assessment = city_terrain_assessment(35.22, -101.83, "Amarillo, TX")
    for quad, info in assessment["quadrants"].items():
        print(f"{quad}: {info['fire_difficulty']} - {info['terrain']}")
"""
import math
import logging
from typing import Optional

from tools.agent_tools.external_data import get_elevation, get_elevation_profile

logger = logging.getLogger(__name__)

# =============================================================================
# Constants
# =============================================================================

# Compass directions and their bearing offsets (degrees clockwise from north)
DIRECTIONS = {
    "N":  0,
    "NE": 45,
    "E":  90,
    "SE": 135,
    "S":  180,
    "SW": 225,
    "W":  270,
    "NW": 315,
}

# Thresholds for terrain feature detection
VALLEY_DROP_THRESHOLD_M = 30       # Min elevation drop to start a valley (meters)
VALLEY_RISE_THRESHOLD_M = 30       # Min elevation rise to close a valley (meters)
CANYON_SLOPE_THRESHOLD_DEG = 15    # Min slope on both sides to qualify as canyon
STEEP_SLOPE_THRESHOLD_DEG = 20     # Slope considered "steep"
FLAT_RELIEF_THRESHOLD_FT = 100     # Max relief (ft) to call a direction "flat"
ROLLING_RELIEF_THRESHOLD_FT = 300  # Max relief (ft) for "rolling hills"

M_TO_FT = 3.28084
FT_TO_M = 0.3048


# =============================================================================
# Geometry helpers
# =============================================================================

def _endpoint_from_bearing(lat: float, lon: float, bearing_deg: float,
                           distance_km: float) -> tuple:
    """Compute the lat/lon of a point at a given bearing and distance.

    Uses the Vincenty direct formula (spherical approximation) to find the
    destination point given a starting lat/lon, bearing, and distance.

    Args:
        lat: Starting latitude (degrees)
        lon: Starting longitude (degrees)
        bearing_deg: Bearing in degrees clockwise from north
        distance_km: Distance in kilometers

    Returns:
        (end_lat, end_lon) in degrees
    """
    R = 6371.0  # Earth radius in km
    lat_r = math.radians(lat)
    lon_r = math.radians(lon)
    bearing_r = math.radians(bearing_deg)
    d = distance_km / R  # angular distance

    end_lat_r = math.asin(
        math.sin(lat_r) * math.cos(d)
        + math.cos(lat_r) * math.sin(d) * math.cos(bearing_r)
    )
    end_lon_r = lon_r + math.atan2(
        math.sin(bearing_r) * math.sin(d) * math.cos(lat_r),
        math.cos(d) - math.sin(lat_r) * math.sin(end_lat_r),
    )

    return (math.degrees(end_lat_r), math.degrees(end_lon_r))


def _slope_degrees(elev_change_m: float, horizontal_m: float) -> float:
    """Compute slope angle in degrees from elevation change and horizontal distance."""
    if horizontal_m <= 0:
        return 0.0
    return math.degrees(math.atan(abs(elev_change_m) / horizontal_m))


# =============================================================================
# Profile analysis
# =============================================================================

def _analyze_single_profile(profile: list) -> dict:
    """Analyze a single elevation profile for terrain features.

    Args:
        profile: List of dicts from get_elevation_profile(), each containing
                 {lat, lon, elevation_m, distance_km}

    Returns:
        Dict with max_elev_ft, min_elev_ft, relief_ft, max_slope_deg,
        valley_count, canyon_features, avg_slope_deg, steep_segments
    """
    if not profile or len(profile) < 3:
        return {
            "max_elev_ft": 0, "min_elev_ft": 0, "relief_ft": 0,
            "max_slope_deg": 0.0, "avg_slope_deg": 0.0,
            "valley_count": 0, "canyon_features": [], "steep_segments": 0,
        }

    elevations_m = [p["elevation_m"] for p in profile]
    distances_km = [p["distance_km"] for p in profile]

    max_elev_m = max(elevations_m)
    min_elev_m = min(elevations_m)
    relief_m = max_elev_m - min_elev_m

    # Compute point-to-point slopes
    slopes_deg = []
    for i in range(1, len(profile)):
        dz = elevations_m[i] - elevations_m[i - 1]
        dx_km = distances_km[i] - distances_km[i - 1]
        dx_m = dx_km * 1000.0
        if dx_m > 0:
            slope = _slope_degrees(dz, dx_m)
            slopes_deg.append(slope)
        else:
            slopes_deg.append(0.0)

    max_slope = max(slopes_deg) if slopes_deg else 0.0
    avg_slope = sum(slopes_deg) / len(slopes_deg) if slopes_deg else 0.0
    steep_segments = sum(1 for s in slopes_deg if s >= STEEP_SLOPE_THRESHOLD_DEG)

    # Detect valleys: elevation drops > threshold then rises > threshold
    valleys = []
    canyon_features = []

    i = 0
    while i < len(elevations_m) - 2:
        # Look for a descent
        descent_start = i
        descent_start_elev = elevations_m[i]

        # Walk forward while descending or roughly flat
        j = i + 1
        local_min_elev = elevations_m[i]
        local_min_idx = i
        while j < len(elevations_m):
            if elevations_m[j] < local_min_elev:
                local_min_elev = elevations_m[j]
                local_min_idx = j
            # If we've risen significantly above the local minimum, stop
            if elevations_m[j] - local_min_elev > VALLEY_RISE_THRESHOLD_M:
                break
            j += 1

        if j >= len(elevations_m):
            break

        drop = descent_start_elev - local_min_elev
        rise = elevations_m[j] - local_min_elev

        if drop >= VALLEY_DROP_THRESHOLD_M and rise >= VALLEY_RISE_THRESHOLD_M:
            # Found a valley
            valley_bottom_km = distances_km[local_min_idx]
            valley_width_km = distances_km[j] - distances_km[descent_start]

            # Compute descent and ascent slopes -- both average and max
            # Average slope (total drop / total distance)
            descent_dx_m = (distances_km[local_min_idx] - distances_km[descent_start]) * 1000.0
            ascent_dx_m = (distances_km[j] - distances_km[local_min_idx]) * 1000.0
            descent_slope = _slope_degrees(drop, descent_dx_m) if descent_dx_m > 0 else 0.0
            ascent_slope = _slope_degrees(rise, ascent_dx_m) if ascent_dx_m > 0 else 0.0

            # Max point-to-point slope within descent and ascent segments
            # This catches steep canyon walls even when the overall valley is wide
            max_descent_slope = 0.0
            for k in range(descent_start, local_min_idx):
                if k < len(slopes_deg):
                    max_descent_slope = max(max_descent_slope, slopes_deg[k])
            max_ascent_slope = 0.0
            for k in range(local_min_idx, min(j, len(slopes_deg))):
                if k < len(slopes_deg):
                    max_ascent_slope = max(max_ascent_slope, slopes_deg[k])

            valley_info = {
                "center_km": round(valley_bottom_km, 1),
                "depth_ft": round(min(drop, rise) * M_TO_FT),
                "width_km": round(valley_width_km, 1),
                "descent_slope_deg": round(descent_slope, 1),
                "ascent_slope_deg": round(ascent_slope, 1),
                "max_descent_slope_deg": round(max_descent_slope, 1),
                "max_ascent_slope_deg": round(max_ascent_slope, 1),
            }
            valleys.append(valley_info)

            # Check if this qualifies as a canyon (steep on both sides)
            # Use EITHER average slope OR max point-to-point slope
            effective_descent = max(descent_slope, max_descent_slope)
            effective_ascent = max(ascent_slope, max_ascent_slope)
            if (effective_descent >= CANYON_SLOPE_THRESHOLD_DEG
                    and effective_ascent >= CANYON_SLOPE_THRESHOLD_DEG):
                canyon_features.append({
                    "center_km": round(valley_bottom_km, 1),
                    "depth_ft": round(min(drop, rise) * M_TO_FT),
                    "width_km": round(valley_width_km, 1),
                    "left_slope_deg": round(descent_slope, 1),
                    "right_slope_deg": round(ascent_slope, 1),
                    "type": "narrow_canyon" if valley_width_km < 2.0 else "wide_canyon",
                })

            i = j  # Continue past this valley
        else:
            i += 1

    return {
        "max_elev_ft": round(max_elev_m * M_TO_FT),
        "min_elev_ft": round(min_elev_m * M_TO_FT),
        "relief_ft": round(relief_m * M_TO_FT),
        "max_slope_deg": round(max_slope, 1),
        "avg_slope_deg": round(avg_slope, 1),
        "valley_count": len(valleys),
        "valleys": valleys,
        "canyon_features": canyon_features,
        "steep_segments": steep_segments,
    }


# =============================================================================
# Terrain classification
# =============================================================================

def _classify_terrain(profiles: dict) -> str:
    """Classify overall terrain from analyzed profile data.

    Args:
        profiles: Dict mapping direction names to profile analysis results

    Returns:
        One of: "flat_grassland", "rolling_hills", "mixed_canyon_grassland",
        "canyon_country", "mountainous"
    """
    total_canyons = sum(len(p.get("canyon_features", [])) for p in profiles.values())
    total_valleys = sum(p.get("valley_count", 0) for p in profiles.values())
    reliefs_ft = [p.get("relief_ft", 0) for p in profiles.values()]
    max_slopes = [p.get("max_slope_deg", 0) for p in profiles.values()]

    max_relief = max(reliefs_ft) if reliefs_ft else 0
    overall_max_slope = max(max_slopes) if max_slopes else 0
    flat_count = sum(1 for r in reliefs_ft if r <= FLAT_RELIEF_THRESHOLD_FT)
    canyon_dirs = sum(1 for p in profiles.values() if p.get("canyon_features"))

    # Mountainous: extreme relief and slopes
    if max_relief > 3000 and overall_max_slope > 25:
        return "mountainous"

    # Canyon country: canyons in 4+ directions
    if canyon_dirs >= 4:
        return "canyon_country"

    # Mixed: some canyons + some flat
    if total_canyons > 0 and flat_count >= 2:
        return "mixed_canyon_grassland"

    # Canyon country: lots of canyons even without flat
    if total_canyons >= 3:
        return "canyon_country"

    # Rolling hills: moderate relief, no canyons
    if max_relief > FLAT_RELIEF_THRESHOLD_FT and total_canyons == 0:
        return "rolling_hills"

    # Mostly flat
    if flat_count >= 6:
        return "flat_grassland"

    # Default: rolling hills if there's moderate terrain variation
    if max_relief > ROLLING_RELIEF_THRESHOLD_FT or total_valleys > 2:
        return "rolling_hills"

    return "flat_grassland"


def _generate_fire_implications(profiles: dict, summary: dict) -> list:
    """Generate fire behavior implications from terrain analysis.

    Args:
        profiles: Dict mapping direction names to profile analysis results
        summary: The summary dict from analyze_terrain_complexity

    Returns:
        List of plain-English fire implication strings
    """
    implications = []
    terrain_class = summary.get("terrain_class", "flat_grassland")
    canyon_dirs = summary.get("canyon_directions", [])
    flat_dirs = summary.get("flat_directions", [])

    if canyon_dirs:
        dirs_str = "/".join(canyon_dirs)
        implications.append(
            f"Canyon terrain to {dirs_str} creates channeled winds and extreme fire behavior"
        )
        implications.append(
            "River valleys act as natural chimneys accelerating fire spread upslope"
        )
        implications.append(
            "Canyon rim communities face extreme exposure from below"
        )
        implications.append(
            "Suppression in canyon bottoms is nearly impossible -- "
            "crews cannot safely position in narrow drainages"
        )

    if flat_dirs:
        dirs_str = "/".join(flat_dirs)
        implications.append(
            f"Flat grassland to {dirs_str} supports rapid but predictable "
            "wind-driven spread"
        )

    if canyon_dirs and flat_dirs:
        implications.append(
            "Fire starting on flat terrain can become uncontrollable if it reaches "
            "canyon breaks -- terrain transitions are critical watch points"
        )

    if terrain_class == "mountainous":
        implications.append(
            "Steep mountainous terrain creates erratic fire behavior with "
            "upslope/downslope wind reversals"
        )
        implications.append(
            "Elevation-driven fuels changes (grass to timber) alter fire character"
        )

    if terrain_class == "rolling_hills":
        implications.append(
            "Rolling terrain creates localized wind acceleration over ridges "
            "and sheltered areas in draws"
        )

    # Check for especially deep canyons
    for direction, profile in profiles.items():
        for canyon in profile.get("canyon_features", []):
            depth = canyon.get("depth_ft", 0)
            if depth > 500:
                implications.append(
                    f"Deep canyon feature ({depth} ft) to {direction} -- "
                    "extreme chimney effect possible with aligned winds"
                )

    # Steep slope warnings
    steep_dirs = [d for d, p in profiles.items()
                  if p.get("max_slope_deg", 0) > 25]
    if steep_dirs:
        dirs_str = "/".join(steep_dirs)
        implications.append(
            f"Very steep slopes (>25 deg) found to {dirs_str} -- "
            "fires spread 2-4x faster upslope"
        )

    # If there are no canyon features and terrain is flat
    if terrain_class == "flat_grassland" and not canyon_dirs:
        implications.append(
            "Uniformly flat terrain -- fire behavior dominated by wind speed "
            "and fuel continuity, not terrain effects"
        )
        implications.append(
            "Suppression access generally good in all directions on flat terrain"
        )

    return implications


# =============================================================================
# Main analysis function
# =============================================================================

def analyze_terrain_complexity(
    lat: float,
    lon: float,
    radius_km: float = 15,
    n_points: int = 50,
) -> dict:
    """Analyze terrain complexity around a point by shooting 8 radial profiles.

    Sends 8 elevation profile requests outward from center (N, NE, E, SE, S,
    SW, W, NW), each `radius_km` long. For each profile computes relief, slope,
    valley count, and canyon features.

    Args:
        lat: Center latitude
        lon: Center longitude
        radius_km: Radius of analysis in km (default 15)
        n_points: Number of elevation samples per profile (default 50)

    Returns:
        Dict with keys:
          - center: {lat, lon, elevation_ft}
          - profiles: {direction: {max_elev_ft, min_elev_ft, relief_ft,
                       max_slope_deg, valley_count, canyon_features, ...}}
          - summary: {total_relief_ft, most_complex_direction,
                      canyon_directions, flat_directions, terrain_class}
          - fire_implications: list of plain-English fire behavior statements
    """
    # Get center elevation
    try:
        center_elev = get_elevation(lat, lon)
        center_elev_ft = center_elev.get("elevation_ft", 0)
    except Exception as e:
        logger.warning("Failed to get center elevation: %s", e)
        center_elev_ft = 0

    # Fetch and analyze profiles in each direction
    profiles = {}
    all_elevations_ft = []

    for direction, bearing in DIRECTIONS.items():
        end_lat, end_lon = _endpoint_from_bearing(lat, lon, bearing, radius_km)

        try:
            raw_profile = get_elevation_profile(
                lat, lon, end_lat, end_lon, n_points=n_points
            )
            analysis = _analyze_single_profile(raw_profile)
        except Exception as e:
            logger.warning("Failed to get profile %s: %s", direction, e)
            analysis = {
                "max_elev_ft": 0, "min_elev_ft": 0, "relief_ft": 0,
                "max_slope_deg": 0.0, "avg_slope_deg": 0.0,
                "valley_count": 0, "valleys": [], "canyon_features": [],
                "steep_segments": 0, "error": str(e),
            }

        profiles[direction] = analysis
        all_elevations_ft.extend([analysis["max_elev_ft"], analysis["min_elev_ft"]])

    # Compute summary statistics
    total_max = max(all_elevations_ft) if all_elevations_ft else 0
    total_min = min(all_elevations_ft) if all_elevations_ft else 0
    total_relief = total_max - total_min

    # Find most complex direction (by canyon count + valley count + relief)
    complexity_scores = {}
    for direction, profile in profiles.items():
        score = (
            len(profile.get("canyon_features", [])) * 3
            + profile.get("valley_count", 0) * 2
            + profile.get("relief_ft", 0) / 100.0
            + profile.get("max_slope_deg", 0) / 5.0
            + profile.get("steep_segments", 0)
        )
        complexity_scores[direction] = score

    most_complex = max(complexity_scores, key=complexity_scores.get) if complexity_scores else "N"

    # Categorize directions
    canyon_directions = [
        d for d, p in profiles.items() if p.get("canyon_features")
    ]
    flat_directions = [
        d for d, p in profiles.items()
        if p.get("relief_ft", 0) <= FLAT_RELIEF_THRESHOLD_FT
        and not p.get("canyon_features")
    ]

    terrain_class = _classify_terrain(profiles)

    summary = {
        "total_relief_ft": total_relief,
        "most_complex_direction": most_complex,
        "canyon_directions": canyon_directions,
        "flat_directions": flat_directions,
        "terrain_class": terrain_class,
    }

    fire_implications = _generate_fire_implications(profiles, summary)

    return {
        "center": {
            "lat": lat,
            "lon": lon,
            "elevation_ft": center_elev_ft,
        },
        "profiles": profiles,
        "summary": summary,
        "fire_implications": fire_implications,
    }


# =============================================================================
# City terrain profiles -- hardcoded expert knowledge
# =============================================================================

CITY_TERRAIN_PROFILES = {
    # -------------------------------------------------------------------------
    # Texas / Oklahoma / New Mexico (fire-vulnerable towns in regional data files)
    # Kept: tucumcari_nm (not in any regional file yet)
    # -------------------------------------------------------------------------
    "tucumcari_nm": {
        "center": (35.17, -103.73),
        "terrain_notes": (
            "Mesa and canyon country. Canadian River valley to N. Mesa "
            "Tucumcari prominent landmark. Mixed terrain with flat stretches "
            "between mesas and canyon breaks."
        ),
        "danger_quadrants": ["north", "west"],
        "safe_quadrants": [],
        "key_features": [
            {"name": "Canadian River", "bearing": "N", "type": "river_canyon",
             "notes": "Deep canyon with eroded breaks, fire channeling"},
            {"name": "Mesa Tucumcari", "bearing": "S", "type": "mesa",
             "notes": "Prominent flat-topped mesa, 4,956 ft"},
            {"name": "I-40 corridor", "bearing": "E-W", "type": "ignition_corridor"},
        ],
    },

    # -------------------------------------------------------------------------
    # Colorado (fire-vulnerable towns in regional data files)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # California (metro areas -- specific fire-vulnerable towns in regional data files)
    # -------------------------------------------------------------------------
    "los_angeles_ca": {
        "center": (34.05, -118.24),
        "terrain_notes": (
            "Mountain-ringed basin. Santa Ana winds from NE push fire from "
            "mountains into populated canyons and WUI areas. Major canyons "
            "(Topanga, Malibu, etc.) on W side funnel fire to coast."
        ),
        "danger_quadrants": ["north", "northeast", "west"],
        "safe_quadrants": [],
        "key_features": [
            {"name": "San Gabriel Mountains", "bearing": "N", "type": "mountain",
             "notes": "10,000+ ft mountains, steep canyons drain into LA basin"},
            {"name": "Santa Monica Mountains", "bearing": "W/NW", "type": "mountain",
             "notes": "Malibu, Topanga, Pacific Palisades -- extreme WUI fire risk"},
            {"name": "Verdugo Mountains", "bearing": "N/NW", "type": "mountain"},
            {"name": "I-5 / Grapevine corridor", "bearing": "N", "type": "ignition_corridor"},
        ],
    },
    "san_diego_ca": {
        "center": (32.72, -117.16),
        "terrain_notes": (
            "Coastal city with deep canyons throughout urban area. Santa Ana "
            "winds push fire from mountains W to coast. 2003 Cedar Fire and "
            "2007 Witch Creek Fire caused massive destruction. Urban canyons "
            "act as fire corridors."
        ),
        "danger_quadrants": ["northeast", "east"],
        "safe_quadrants": ["west"],
        "key_features": [
            {"name": "East County mountains", "bearing": "E/NE", "type": "mountain",
             "notes": "Cuyamaca, Laguna Mountains -- fire origin zones for Santa Anas"},
            {"name": "Urban canyons", "bearing": "throughout", "type": "canyon",
             "notes": "Deep canyons throughout San Diego act as fire corridors"},
            {"name": "I-8 corridor", "bearing": "E", "type": "ignition_corridor"},
        ],
    },

    # -------------------------------------------------------------------------
    # Arizona (fire-vulnerable towns in regional data files)
    # -------------------------------------------------------------------------
}

# ---------------------------------------------------------------------------
# Merge regional city profiles from data/ directory
# ---------------------------------------------------------------------------
def _merge_regional_terrain():
    """Load and merge all regional terrain profiles into CITY_TERRAIN_PROFILES."""
    _regional_modules = [
        ("agent_tools.data.california_profiles", "CA_TERRAIN_PROFILES"),
        ("agent_tools.data.pnw_rockies_profiles", "PNW_TERRAIN_PROFILES"),
        ("agent_tools.data.colorado_basin_profiles", "CO_BASIN_TERRAIN_PROFILES"),
        ("agent_tools.data.southwest_profiles", "SW_TERRAIN_PROFILES"),
        ("agent_tools.data.southern_plains_profiles", "PLAINS_TERRAIN_PROFILES"),
        ("agent_tools.data.southeast_misc_profiles", "SE_MISC_TERRAIN_PROFILES"),
    ]
    count = 0
    for mod_name, attr_name in _regional_modules:
        try:
            mod = __import__(mod_name, fromlist=[attr_name])
            profiles = getattr(mod, attr_name, {})
            for key, val in profiles.items():
                if key not in CITY_TERRAIN_PROFILES:
                    # Normalize: some regions use 'coords' instead of 'center'
                    if "center" not in val and "coords" in val:
                        val["center"] = val["coords"]
                    # Normalize: some use 'terrain_class' instead of 'terrain_notes'
                    if "terrain_notes" not in val:
                        notes_parts = []
                        city_label = val.get("city", key.replace("_", " ").title())
                        elev = val.get("elevation_ft", "")
                        tc = val.get("terrain_class", "").replace("_", " ")
                        if tc:
                            notes_parts.append(f"{city_label} ({tc}, {elev}ft)")
                        if val.get("vegetation"):
                            notes_parts.append(f"Vegetation: {val['vegetation'][:150]}")
                        if val.get("wui_exposure"):
                            notes_parts.append(val["wui_exposure"][:200])
                        if val.get("terrain_description"):
                            notes_parts.append(val["terrain_description"][:200])
                        if val.get("fire_behavior_notes"):
                            notes_parts.append(val["fire_behavior_notes"][:200])
                        val["terrain_notes"] = ". ".join(notes_parts) if notes_parts else "No terrain notes available"
                    # Normalize: some use 'terrain_features' instead of 'key_features'
                    if "key_features" not in val and "terrain_features" in val:
                        val["key_features"] = val["terrain_features"]
                    # Normalize: extract danger_quadrants from terrain_features if missing
                    if "danger_quadrants" not in val and "terrain_features" in val:
                        val["danger_quadrants"] = []
                    CITY_TERRAIN_PROFILES[key] = val
                    count += 1
        except ImportError:
            pass
    return count

_merge_regional_terrain()


# =============================================================================
# City terrain assessment
# =============================================================================

# Map 8-direction compass to city quadrant labels
_DIR_TO_QUADRANT = {
    "N": "north",
    "NE": "northeast",
    "E": "east",
    "SE": "southeast",
    "S": "south",
    "SW": "southwest",
    "W": "west",
    "NW": "northwest",
}

# Simplified quadrant groupings (8 directions -> 5 quadrants)
_DIR_TO_SIMPLE_QUADRANT = {
    "N": "north",
    "NE": "northeast",
    "E": "east",
    "SE": "southeast",
    "S": "south",
    "SW": "southwest",
    "W": "west",
    "NW": "northwest",
}


def _fire_difficulty_from_profile(profile: dict) -> str:
    """Rate fire suppression difficulty from a terrain profile analysis.

    Args:
        profile: Analysis dict from _analyze_single_profile()

    Returns:
        One of: "low", "moderate", "high", "extreme"
    """
    canyons = len(profile.get("canyon_features", []))
    relief = profile.get("relief_ft", 0)
    max_slope = profile.get("max_slope_deg", 0)
    valleys = profile.get("valley_count", 0)

    if canyons >= 2 or (canyons >= 1 and max_slope > 25):
        return "extreme"
    if canyons >= 1 or max_slope > 20 or relief > 1000:
        return "high"
    if valleys >= 2 or max_slope > 10 or relief > 300:
        return "moderate"
    return "low"


def _terrain_description_from_profile(profile: dict) -> str:
    """Generate a human-readable terrain description from profile analysis."""
    parts = []
    relief = profile.get("relief_ft", 0)
    canyons = profile.get("canyon_features", [])
    valleys = profile.get("valley_count", 0)
    max_slope = profile.get("max_slope_deg", 0)

    if canyons:
        depths = [c.get("depth_ft", 0) for c in canyons]
        max_depth = max(depths) if depths else 0
        if max_depth > 500:
            parts.append(f"deep canyon terrain ({max_depth} ft cuts)")
        else:
            parts.append(f"canyon breaks ({len(canyons)} features)")
    elif valleys > 0:
        parts.append(f"{valleys} valley/draw features")

    if relief > 1000:
        parts.append(f"high relief ({relief} ft)")
    elif relief > 300:
        parts.append(f"moderate relief ({relief} ft)")

    if max_slope > 25:
        parts.append("very steep slopes")
    elif max_slope > 15:
        parts.append("steep slopes")

    if not parts:
        if relief < 100:
            parts.append("flat terrain")
        else:
            parts.append("gently rolling terrain")

    return ", ".join(parts)


def _suppression_notes_from_profile(profile: dict, difficulty: str) -> str:
    """Generate suppression difficulty notes from profile analysis."""
    if difficulty == "extreme":
        return (
            "Canyon terrain channels winds, nearly impossible suppression "
            "in canyon bottoms. Crews must fight from rim. Very limited "
            "escape routes."
        )
    if difficulty == "high":
        return (
            "Steep terrain limits equipment access. Fire spreads rapidly "
            "upslope. Anchor points difficult to establish."
        )
    if difficulty == "moderate":
        return (
            "Terrain creates localized fire behavior variations. Draws and "
            "valleys may channel wind. Generally accessible for ground crews."
        )
    return (
        "Open terrain allows wind-driven grass fires but accessible for "
        "suppression. Engines and dozers can operate effectively."
    )


def _find_city_profile(lat: float, lon: float, city_name: str) -> Optional[dict]:
    """Find matching city terrain profile from hardcoded database.

    Matches by city name substring first, then by proximity (within 30km).

    Args:
        lat: Latitude
        lon: Longitude
        city_name: City name string

    Returns:
        Matching CITY_TERRAIN_PROFILES entry or None
    """
    # Try name match first
    city_lower = city_name.lower().replace(",", "").replace(" ", "_")
    for key, profile in CITY_TERRAIN_PROFILES.items():
        if key in city_lower or city_lower.startswith(key.rsplit("_", 1)[0]):
            return profile

    # Try coordinate proximity (within 30km)
    for key, profile in CITY_TERRAIN_PROFILES.items():
        plat, plon = profile["center"]
        dlat = math.radians(plat - lat)
        dlon = math.radians(plon - lon)
        a = (math.sin(dlat / 2) ** 2
             + math.cos(math.radians(lat))
             * math.cos(math.radians(plat))
             * math.sin(dlon / 2) ** 2)
        dist_km = 6371 * 2 * math.asin(math.sqrt(a))
        if dist_km < 30:
            return profile

    return None


def _find_analog_cities(
    lat: float, lon: float, elevation_ft: float = 0, max_results: int = 3
) -> list:
    """Find the most similar profiled cities to an unknown location.

    Scores similarity using geographic proximity, elevation match, and
    shared terrain characteristics. Returns the best analogs with their
    fire history as cautionary context.

    Args:
        lat: Target latitude
        lon: Target longitude
        elevation_ft: Target elevation (0 = unknown, will match by distance only)
        max_results: Number of analogs to return (default 3)

    Returns:
        List of dicts with: key, city_name, distance_km, elevation_diff_ft,
        similarity_score, terrain_notes, historical_fires, evacuation_warning
    """
    candidates = []

    for key, profile in CITY_TERRAIN_PROFILES.items():
        center = profile.get("center")
        if not center:
            continue
        plat, plon = center[0], center[1]

        # Geographic distance
        dlat = math.radians(plat - lat)
        dlon = math.radians(plon - lon)
        a = (math.sin(dlat / 2) ** 2
             + math.cos(math.radians(lat))
             * math.cos(math.radians(plat))
             * math.sin(dlon / 2) ** 2)
        dist_km = 6371 * 2 * math.asin(math.sqrt(a))

        # Skip cities more than 500km away -- not useful analogs
        if dist_km > 500:
            continue

        # Elevation from profile
        elev_range = profile.get("elevation_range_ft")
        profile_elev = 0
        if elev_range and isinstance(elev_range, (tuple, list)) and len(elev_range) >= 2:
            profile_elev = (elev_range[0] + elev_range[1]) / 2
        elif profile.get("elevation_ft"):
            profile_elev = profile["elevation_ft"]

        elev_diff = abs(elevation_ft - profile_elev) if elevation_ft > 0 and profile_elev > 0 else 0

        # Similarity score: lower = more similar
        # Distance weight: 1 point per km (dominant factor)
        # Elevation weight: 1 point per 100ft difference
        # Regional bonus: same state gets -50 penalty reduction
        score = dist_km + (elev_diff / 100.0)

        # State proximity bonus: extract state suffix
        state = key.rsplit("_", 1)[-1] if "_" in key else ""

        candidates.append({
            "key": key,
            "distance_km": round(dist_km, 1),
            "elevation_diff_ft": round(elev_diff),
            "profile_elev_ft": round(profile_elev),
            "state": state,
            "score": score,
            "profile": profile,
        })

    # Sort by score (most similar first)
    candidates.sort(key=lambda x: x["score"])

    # Build result -- take top N, preferring geographic diversity
    results = []
    seen_states = set()
    for c in candidates:
        if len(results) >= max_results:
            break

        profile = c["profile"]
        terrain_notes = profile.get("terrain_notes", "")

        # Extract historical fires summary
        fires = profile.get("historical_fires", [])
        fire_summary = []
        for f in fires[:3]:  # Top 3 fires
            if isinstance(f, dict):
                name = f.get("name", "Unknown")
                year = f.get("year", "")
                acres = f.get("acres", 0)
                structures = f.get("structures_destroyed", 0)
                fatalities = f.get("fatalities", 0)
                parts = [f"{name} ({year})"]
                if acres:
                    parts.append(f"{acres:,} ac")
                if structures:
                    parts.append(f"{structures:,} structures")
                if fatalities:
                    parts.append(f"{fatalities} fatalities")
                fire_summary.append(" — ".join(parts))
            elif isinstance(f, str):
                fire_summary.append(f[:100])

        # Extract evacuation warning
        evac_routes = profile.get("evacuation_routes", [])
        evac_warning = ""
        for route in evac_routes:
            if isinstance(route, dict):
                risk = route.get("risk", "")
                if risk and ("single" in risk.lower() or "only" in risk.lower()
                             or "blocked" in risk.lower()):
                    evac_warning = risk
                    break

        # City display name
        key = c["key"]
        display_name = profile.get("city", key.rsplit("_", 1)[0].replace("_", " ").title())
        state_abbr = c["state"].upper()

        results.append({
            "key": key,
            "city_name": f"{display_name}, {state_abbr}",
            "distance_km": c["distance_km"],
            "elevation_ft": c["profile_elev_ft"],
            "elevation_diff_ft": c["elevation_diff_ft"],
            "similarity_score": round(c["score"], 1),
            "terrain_summary": terrain_notes[:300] + "..." if len(terrain_notes) > 300 else terrain_notes,
            "historical_fires": fire_summary,
            "evacuation_warning": evac_warning,
            "wui_exposure": profile.get("wui_exposure", ""),
            "fire_spread": str(profile.get("fire_spread_characteristics", ""))[:200] if profile.get("fire_spread_characteristics") else "",
        })
        seen_states.add(c["state"])

    return results


def _generate_worst_case(city_profile: Optional[dict], terrain_result: dict) -> str:
    """Generate worst-case fire scenario from terrain and expert knowledge."""
    if city_profile:
        danger_quads = city_profile.get("danger_quadrants", [])
        features = city_profile.get("key_features", [])
        canyon_features = [f for f in features if f["type"] in
                          ("major_canyon", "river_canyon", "canyon")]

        if canyon_features and danger_quads:
            feature_names = [f["name"] for f in canyon_features[:2]]
            quad_str = ", ".join(danger_quads[:3])
            return (
                f"Fire approaching from upwind pushed by prevailing winds enters "
                f"canyon terrain on {quad_str} sides "
                f"({', '.join(feature_names)}) -- channeled winds amplify spread, "
                f"suppression nearly impossible in canyon bottoms, communities on "
                f"canyon rims face extreme exposure from below"
            )

    # Fall back to terrain analysis
    summary = terrain_result.get("summary", {})
    canyon_dirs = summary.get("canyon_directions", [])
    flat_dirs = summary.get("flat_directions", [])

    if canyon_dirs:
        return (
            f"Fire driven by wind across flat terrain ({'/'.join(flat_dirs or ['open'])}) "
            f"reaches canyon breaks ({'/'.join(canyon_dirs)}) where terrain-channeled "
            f"winds create extreme, unpredictable fire behavior"
        )

    return (
        "Wind-driven grassfire with continuous fuels and limited barriers. "
        "Rate of spread determined primarily by wind speed and fuel moisture."
    )


def _generate_recommended_transects(
    lat: float, lon: float, city_profile: Optional[dict],
    terrain_result: dict, radius_km: float = 20,
) -> list:
    """Generate recommended cross-section transects for fire weather analysis.

    Args:
        lat: Center latitude
        lon: Center longitude
        city_profile: Matching hardcoded city profile or None
        terrain_result: Result from analyze_terrain_complexity
        radius_km: How far transects should extend

    Returns:
        List of recommended transect dicts with label, start, end, product
    """
    transects = []
    summary = terrain_result.get("summary", {})
    canyon_dirs = summary.get("canyon_directions", [])
    most_complex = summary.get("most_complex_direction", None)

    # Always include through-center transects for the most complex direction
    if most_complex:
        bearing = DIRECTIONS.get(most_complex, 0)
        opposite_bearing = (bearing + 180) % 360
        start_lat, start_lon = _endpoint_from_bearing(lat, lon, opposite_bearing, radius_km)
        end_lat, end_lon = _endpoint_from_bearing(lat, lon, bearing, radius_km)
        transects.append({
            "label": f"Through {most_complex} (most complex terrain)",
            "start": [round(start_lat, 4), round(start_lon, 4)],
            "end": [round(end_lat, 4), round(end_lon, 4)],
            "product": "fire_wx",
        })

    # Add transects for each canyon direction
    for direction in canyon_dirs:
        if direction == most_complex:
            continue  # Already covered
        bearing = DIRECTIONS.get(direction, 0)
        opposite_bearing = (bearing + 180) % 360
        start_lat, start_lon = _endpoint_from_bearing(lat, lon, opposite_bearing, radius_km)
        end_lat, end_lon = _endpoint_from_bearing(lat, lon, bearing, radius_km)
        transects.append({
            "label": f"Through {direction} canyon terrain",
            "start": [round(start_lat, 4), round(start_lon, 4)],
            "end": [round(end_lat, 4), round(end_lon, 4)],
            "product": "wind_speed",
        })

    # Add expert-knowledge transects from city profile
    if city_profile:
        features = city_profile.get("key_features", [])
        for feat in features:
            if feat["type"] in ("major_canyon", "river_canyon", "canyon", "escarpment"):
                bearing_str = feat.get("bearing", "")
                distance_mi = feat.get("distance_mi", radius_km * 0.62)
                # Parse bearing string (e.g., "S/SE" -> average of S and SE)
                bearing_vals = []
                for part in bearing_str.replace("/", " ").split():
                    if part in DIRECTIONS:
                        bearing_vals.append(DIRECTIONS[part])
                if not bearing_vals:
                    continue
                avg_bearing = sum(bearing_vals) / len(bearing_vals)
                dist_km = distance_mi * 1.609
                end_lat, end_lon = _endpoint_from_bearing(
                    lat, lon, avg_bearing, dist_km + 5
                )
                transects.append({
                    "label": f"Toward {feat['name']} ({feat.get('bearing', '')})",
                    "start": [round(lat, 4), round(lon, 4)],
                    "end": [round(end_lat, 4), round(end_lon, 4)],
                    "product": "fire_wx",
                })

    return transects[:6]  # Limit to 6 transects


def city_terrain_assessment(
    lat: float,
    lon: float,
    city_name: str,
    radius_km: float = 20,
    n_points: int = 50,
    skip_api: bool = False,
) -> dict:
    """Full terrain assessment for a city, combining elevation API data with
    hardcoded expert knowledge.

    Runs analyze_terrain_complexity() and then maps terrain features to city
    quadrants. If the city matches a CITY_TERRAIN_PROFILES entry, expert
    knowledge is layered on top of the computed terrain data.

    Args:
        lat: City center latitude
        lon: City center longitude
        city_name: City name (e.g., "Amarillo, TX")
        radius_km: Radius of terrain analysis in km (default 20)
        n_points: Elevation samples per radial profile (default 50)
        skip_api: If True, skip elevation API calls and use only hardcoded
                  profiles (useful when API is unavailable)

    Returns:
        Dict with keys:
          - city: city name string
          - center: {lat, lon, elevation_ft}
          - quadrants: {direction: {terrain, fire_difficulty, notes}}
          - worst_case_scenario: string
          - recommended_transects: list of transect specs
          - terrain_analysis: full analyze_terrain_complexity result (if API used)
          - expert_profile: matching CITY_TERRAIN_PROFILES entry (if found)
    """
    # Look up hardcoded expert knowledge
    city_profile = _find_city_profile(lat, lon, city_name)

    # Run elevation API analysis unless skipped
    terrain_result = None
    if not skip_api:
        try:
            terrain_result = analyze_terrain_complexity(
                lat, lon, radius_km=radius_km, n_points=n_points
            )
        except Exception as e:
            logger.warning("Terrain analysis API failed: %s", e)
            terrain_result = None

    # Build quadrant assessments
    quadrants = {}
    for direction, quadrant_name in _DIR_TO_QUADRANT.items():
        quad_info = {"terrain": "", "fire_difficulty": "moderate", "notes": ""}

        # Start with computed terrain data
        if terrain_result and direction in terrain_result.get("profiles", {}):
            profile = terrain_result["profiles"][direction]
            quad_info["terrain"] = _terrain_description_from_profile(profile)
            quad_info["fire_difficulty"] = _fire_difficulty_from_profile(profile)
            quad_info["notes"] = _suppression_notes_from_profile(
                profile, quad_info["fire_difficulty"]
            )

        # Overlay expert knowledge if available
        if city_profile:
            danger_quads = city_profile.get("danger_quadrants", [])
            safe_quads = city_profile.get("safe_quadrants", [])
            features = city_profile.get("key_features", [])

            # Check if this quadrant is in a danger/safe zone
            if quadrant_name in danger_quads or "all" in danger_quads:
                # Upgrade fire difficulty if expert says it's dangerous
                if quad_info["fire_difficulty"] in ("low", "moderate"):
                    quad_info["fire_difficulty"] = "high"
            if quadrant_name in safe_quads:
                # Only downgrade if computed as moderate or lower
                if quad_info["fire_difficulty"] in ("moderate", "low"):
                    quad_info["fire_difficulty"] = "moderate"

            # Find features relevant to this quadrant
            for feat in features:
                bearing_str = feat.get("bearing", "").upper()
                # Check if feature's bearing relates to this direction
                bearing_parts = bearing_str.replace("/", " ").replace("-", " ").split()
                if direction in bearing_parts or quadrant_name.upper() in bearing_parts:
                    feat_name = feat["name"]
                    feat_notes = feat.get("notes", "")
                    if feat_name not in quad_info["terrain"]:
                        if quad_info["terrain"]:
                            quad_info["terrain"] += f"; {feat_name}"
                        else:
                            quad_info["terrain"] = feat_name
                    if feat_notes and feat_notes not in quad_info["notes"]:
                        if quad_info["notes"]:
                            quad_info["notes"] += f" {feat_notes}"
                        else:
                            quad_info["notes"] = feat_notes

        # Fallback if we have no terrain description
        if not quad_info["terrain"]:
            quad_info["terrain"] = "Terrain data unavailable"

        quadrants[quadrant_name] = quad_info

    # Determine center elevation
    center_elev_ft = 0
    if terrain_result:
        center_elev_ft = terrain_result.get("center", {}).get("elevation_ft", 0)
    elif city_profile:
        # Try to get from profile center coordinates
        try:
            elev = get_elevation(*city_profile["center"])
            center_elev_ft = elev.get("elevation_ft", 0)
        except Exception:
            pass

    # If we don't have terrain_result but have a city_profile, build a
    # minimal terrain_result for downstream functions
    if terrain_result is None:
        terrain_result = {
            "center": {"lat": lat, "lon": lon, "elevation_ft": center_elev_ft},
            "profiles": {},
            "summary": {
                "total_relief_ft": 0,
                "most_complex_direction": None,
                "canyon_directions": [],
                "flat_directions": [],
                "terrain_class": "unknown",
            },
            "fire_implications": [],
        }

    worst_case = _generate_worst_case(city_profile, terrain_result)
    recommended_transects = _generate_recommended_transects(
        lat, lon, city_profile, terrain_result, radius_km=radius_km
    )

    # Compile fire implications from both sources
    fire_implications = terrain_result.get("fire_implications", [])
    if city_profile:
        terrain_notes = city_profile.get("terrain_notes", "")
        if terrain_notes:
            fire_implications.insert(0, f"Expert assessment: {terrain_notes}")

    result = {
        "city": city_name,
        "center": {
            "lat": lat,
            "lon": lon,
            "elevation_ft": center_elev_ft,
        },
        "quadrants": quadrants,
        "worst_case_scenario": worst_case,
        "recommended_transects": recommended_transects,
        "fire_implications": fire_implications,
    }

    if terrain_result and terrain_result["summary"].get("terrain_class") != "unknown":
        result["terrain_analysis"] = terrain_result

    if city_profile:
        result["expert_profile"] = city_profile
    else:
        # No exact match -- find analog cities for context
        analogs = _find_analog_cities(lat, lon, elevation_ft=center_elev_ft)
        if analogs:
            result["analog_cities"] = analogs
            # Add analog context to fire implications
            analog_names = [a["city_name"] for a in analogs[:2]]
            analog_fires = []
            for a in analogs[:2]:
                for f in a.get("historical_fires", [])[:1]:
                    analog_fires.append(f)
            if analog_fires:
                fire_implications.append(
                    f"No exact profile for this location. Nearest comparable communities: "
                    f"{', '.join(analog_names)}. Relevant fire history from analogs: "
                    + "; ".join(analog_fires)
                )
            else:
                fire_implications.append(
                    f"No exact profile for this location. Nearest comparable communities: "
                    f"{', '.join(analog_names)}."
                )

    return result


# =============================================================================
# Utility: quick lookup for known cities
# =============================================================================

def list_known_cities() -> list:
    """List all cities with hardcoded terrain profiles.

    Returns:
        List of dicts with key, center coordinates, and terrain notes snippet.
    """
    return [
        {
            "key": key,
            "center": profile["center"],
            "terrain_summary": profile["terrain_notes"][:100] + "...",
            "danger_quadrants": profile.get("danger_quadrants", []),
        }
        for key, profile in CITY_TERRAIN_PROFILES.items()
    ]


def quick_terrain_check(lat: float, lon: float, city_name: str = "") -> dict:
    """Quick terrain check using only hardcoded profiles (no API calls).

    Useful for fast lookups during forecast generation. If the city is in
    CITY_TERRAIN_PROFILES, returns expert knowledge immediately. Otherwise
    returns a placeholder indicating no terrain data is available.

    Args:
        lat: Latitude
        lon: Longitude
        city_name: Optional city name for matching

    Returns:
        Dict with terrain summary, danger quadrants, key features
    """
    profile = _find_city_profile(lat, lon, city_name)

    if profile:
        return {
            "found": True,
            "terrain_notes": profile["terrain_notes"],
            "danger_quadrants": profile.get("danger_quadrants", []),
            "safe_quadrants": profile.get("safe_quadrants", []),
            "key_features": profile.get("key_features", []),
            "center": profile["center"],
        }

    # No exact match -- find analog cities
    analogs = _find_analog_cities(lat, lon, max_results=3)
    analog_summary = ""
    if analogs:
        parts = []
        for a in analogs:
            fires_str = ""
            if a["historical_fires"]:
                fires_str = f" (fire history: {a['historical_fires'][0]})"
            parts.append(
                f"{a['city_name']} ({a['distance_km']}km away, "
                f"{a['elevation_ft']}ft){fires_str}"
            )
        analog_summary = (
            f"No exact profile for ({lat:.2f}, {lon:.2f}). "
            f"Nearest comparable communities: " + "; ".join(parts) + ". "
            "Use these as reference for terrain, fire behavior, and evacuation patterns. "
            "Run analyze_terrain_complexity() for API-based terrain analysis of this specific location."
        )

    return {
        "found": False,
        "terrain_notes": analog_summary or (
            f"No hardcoded terrain profile for ({lat}, {lon}). "
            "Run analyze_terrain_complexity() for API-based analysis."
        ),
        "danger_quadrants": [],
        "safe_quadrants": [],
        "key_features": [],
        "analog_cities": analogs,
    }
