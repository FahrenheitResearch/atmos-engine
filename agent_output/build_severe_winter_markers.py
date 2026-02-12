"""
Build markers for 21 severe/winter/AR/other events.
Writes to agent_severe_winter.json incrementally.
Tests each section via the API.
"""
import json
import urllib.parse
import urllib.request
import os
import math

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent_severe_winter.json")
API_BASE = "http://localhost:5565/api/v1/cross-section"

def save(data):
    with open(OUTPUT, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"  Saved {len(data)} events to {OUTPUT}")

def distance_km(lat1, lon1, lat2, lon2):
    """Haversine distance in km"""
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return R * 2 * math.asin(math.sqrt(a))

def point_to_line_distance_km(plat, plon, slat, slon, elat, elon):
    """Approximate distance from point to line segment in km"""
    dx = elon - slon
    dy = elat - slat
    if dx == 0 and dy == 0:
        return distance_km(plat, plon, slat, slon)
    t = max(0, min(1, ((plon - slon) * dx + (plat - slat) * dy) / (dx*dx + dy*dy)))
    proj_lat = slat + t * dy
    proj_lon = slon + t * dx
    return distance_km(plat, plon, proj_lat, proj_lon)

def test_api(section, cycle_key, markers):
    """Test a cross-section API call with markers. Returns HTTP status code."""
    product = section["products"][0]
    fhr = section["best_fhr"]
    markers_json = json.dumps(markers)
    markers_encoded = urllib.parse.quote(markers_json)

    cycle_date = cycle_key[:8]
    cycle_hour = cycle_key[9:11]
    cycle_param = f"{cycle_date}_{cycle_hour}"

    url = (f"{API_BASE}?start_lat={section['start'][0]}&start_lon={section['start'][1]}"
           f"&end_lat={section['end'][0]}&end_lon={section['end'][1]}"
           f"&product={product}&cycle={cycle_param}&fhr={fhr}"
           f"&markers={markers_encoded}")

    try:
        req = urllib.request.Request(url, method='GET')
        req.add_header('User-Agent', 'agent-marker-test/1.0')
        resp = urllib.request.urlopen(req, timeout=30)
        code = resp.getcode()
        print(f"    API test: {code} - {product} fhr={fhr}")
        return code
    except urllib.error.HTTPError as e:
        print(f"    API test: {e.code} - {product} fhr={fhr}")
        return e.code
    except Exception as e:
        print(f"    API test: ERROR - {e}")
        return 0

def filter_markers_for_section(all_markers, section):
    """Return only markers within 50km of the section line."""
    valid = []
    slat, slon = section["start"]
    elat, elon = section["end"]
    for m in all_markers:
        d = point_to_line_distance_km(m["lat"], m["lon"], slat, slon, elat, elon)
        if d <= 50:
            valid.append(m)
            print(f"    Marker '{m['label']}' is {d:.1f}km from section line - INCLUDED")
        else:
            print(f"    Marker '{m['label']}' is {d:.1f}km from section line - excluded")
    return valid

# ============================================================
# ALL 21 EVENTS WITH MARKERS
# ============================================================

events = {}

# =============================================
# 1. 20210215_12z - Winter Storm Uri
# =============================================
print("\n=== 20210215_12z: Winter Storm Uri ===")
all_markers_uri = [
    {"lat": 32.78, "lon": -96.80, "label": "Dallas"},
    {"lat": 29.76, "lon": -95.37, "label": "Houston"},
    {"lat": 29.42, "lon": -98.49, "label": "San Antonio"},
    {"lat": 35.47, "lon": -97.52, "label": "OKC"},
]

uri_sections = [
    {
        "label": "N-S arctic air intrusion from OK to Gulf Coast",
        "start": [40.0, -96.8], "end": [28.0, -96.8],
        "products": ["temperature", "wind_speed", "theta_e"],
        "best_fhr": 6
    },
    {
        "label": "W-E across TX precipitation type boundary",
        "start": [32.8, -100.0], "end": [32.8, -93.0],
        "products": ["temperature", "wetbulb", "icing", "cloud_total"],
        "best_fhr": 10
    },
    {
        "label": "NW-SE arctic front from panhandle to Houston",
        "start": [35.5, -101.0], "end": [29.8, -95.4],
        "products": ["temperature", "theta_e", "frontogenesis"],
        "best_fhr": 4
    }
]

for s in uri_sections:
    filtered = filter_markers_for_section(all_markers_uri, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20210215_12z", filtered)

events["20210215_12z"] = {
    "name": "Winter Storm Uri",
    "category": "winter",
    "suggested_sections": uri_sections
}
save(events)

# =============================================
# 2. 20210428_18z - Hondo TX Record Hail
# =============================================
print("\n=== 20210428_18z: Hondo TX Record Hail ===")
all_markers_hondo = [
    {"lat": 29.35, "lon": -99.14, "label": "Hondo"},
    {"lat": 29.42, "lon": -98.49, "label": "San Antonio"},
]

hondo_sections = [
    {
        "label": "SW-NE across dryline into supercell environment",
        "start": [28.5, -100.5], "end": [30.5, -97.5],
        "products": ["theta_e", "shear", "lapse_rate"],
        "best_fhr": 6
    },
    {
        "label": "W-E through Hondo supercell path",
        "start": [29.35, -100.5], "end": [29.35, -97.8],
        "products": ["omega", "wind_speed", "temperature"],
        "best_fhr": 7
    },
    {
        "label": "N-S instability axis through south-central TX",
        "start": [30.8, -99.14], "end": [28.0, -99.14],
        "products": ["lapse_rate", "theta_e", "shear"],
        "best_fhr": 5
    }
]

for s in hondo_sections:
    filtered = filter_markers_for_section(all_markers_hondo, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20210428_18z", filtered)

events["20210428_18z"] = {
    "name": "Hondo TX Record Hail 6.42in",
    "category": "hail",
    "suggested_sections": hondo_sections
}
save(events)

# =============================================
# 3. 20210628_12z - PNW Heat Dome (Portland day)
# =============================================
print("\n=== 20210628_12z: PNW Heat Dome ===")
all_markers_hd1 = [
    {"lat": 45.52, "lon": -122.68, "label": "Portland"},
    {"lat": 44.94, "lon": -123.04, "label": "Salem"},
    {"lat": 47.61, "lon": -122.33, "label": "Seattle"},
]

hd1_sections = [
    {
        "label": "W-E subsidence inversion through Portland",
        "start": [45.5, -125.0], "end": [45.5, -118.0],
        "products": ["temperature", "omega", "rh"],
        "best_fhr": 10
    },
    {
        "label": "N-S ridge axis from WA through OR",
        "start": [48.5, -122.5], "end": [42.0, -122.5],
        "products": ["temperature", "theta_e", "vpd"],
        "best_fhr": 10
    },
    {
        "label": "W-E at Salem latitude showing subsidence/lapse rate",
        "start": [44.9, -124.5], "end": [44.9, -119.0],
        "products": ["omega", "lapse_rate", "temperature"],
        "best_fhr": 8
    }
]

for s in hd1_sections:
    filtered = filter_markers_for_section(all_markers_hd1, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20210628_12z", filtered)

events["20210628_12z"] = {
    "name": "PNW Heat Dome",
    "category": "other",
    "suggested_sections": hd1_sections
}
save(events)

# =============================================
# 4. 20210629_12z - PNW Heat Dome Peak (Lytton day)
# =============================================
print("\n=== 20210629_12z: PNW Heat Dome Peak ===")
all_markers_hd2 = [
    {"lat": 50.23, "lon": -121.58, "label": "Lytton"},
    {"lat": 45.52, "lon": -122.68, "label": "Portland"},
    {"lat": 47.61, "lon": -122.33, "label": "Seattle"},
]

hd2_sections = [
    {
        "label": "W-E subsidence through Fraser Canyon (Lytton) at peak",
        "start": [50.2, -124.0], "end": [50.2, -119.0],
        "products": ["temperature", "omega", "rh"],
        "best_fhr": 8
    },
    {
        "label": "N-S ridge axis from BC interior to OR",
        "start": [51.0, -122.0], "end": [44.0, -122.0],
        "products": ["temperature", "theta_e", "omega"],
        "best_fhr": 6
    }
]

for s in hd2_sections:
    filtered = filter_markers_for_section(all_markers_hd2, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20210629_12z", filtered)

events["20210629_12z"] = {
    "name": "PNW Heat Dome Peak",
    "category": "other",
    "suggested_sections": hd2_sections
}
save(events)

# =============================================
# 5. 20211114_00z - PNW Atmospheric River
# =============================================
print("\n=== 20211114_00z: PNW Atmospheric River ===")
all_markers_pnwar = [
    {"lat": 49.05, "lon": -122.32, "label": "Abbotsford"},
    {"lat": 47.61, "lon": -122.33, "label": "Seattle"},
    {"lat": 49.28, "lon": -123.12, "label": "Vancouver"},
]

pnwar_sections = [
    {
        "label": "SW-NE AR moisture plume into WA Cascades",
        "start": [44.0, -126.0], "end": [49.5, -120.0],
        "products": ["moisture_transport", "omega", "q"],
        "best_fhr": 12
    },
    {
        "label": "W-E Cascades orographic lift transect",
        "start": [47.5, -125.0], "end": [47.5, -120.0],
        "products": ["omega", "cloud_total", "q", "isentropic_ascent"],
        "best_fhr": 14
    },
    {
        "label": "W-E Fraser Valley flooding corridor",
        "start": [49.1, -123.5], "end": [49.1, -120.5],
        "products": ["moisture_transport", "omega", "rh"],
        "best_fhr": 10
    }
]

for s in pnwar_sections:
    filtered = filter_markers_for_section(all_markers_pnwar, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20211114_00z", filtered)

events["20211114_00z"] = {
    "name": "PNW Atmospheric River",
    "category": "ar",
    "suggested_sections": pnwar_sections
}
save(events)

# =============================================
# 6. 20221118_00z - Buffalo Lake Effect 81in
# =============================================
print("\n=== 20221118_00z: Buffalo Lake Effect ===")
all_markers_buffalo = [
    {"lat": 42.72, "lon": -78.83, "label": "Hamburg"},
    {"lat": 42.76, "lon": -78.74, "label": "Orchard Park"},
    {"lat": 42.89, "lon": -78.88, "label": "Buffalo"},
]

buffalo_sections = [
    {
        "label": "W-E lake-effect band from Lake Erie through Buffalo southtowns",
        "start": [42.88, -80.5], "end": [42.88, -77.5],
        "products": ["temperature", "cloud_total", "omega", "q"],
        "best_fhr": 12
    },
    {
        "label": "N-S across lake-effect convergence zone",
        "start": [43.5, -78.88], "end": [42.2, -78.88],
        "products": ["wind_speed", "q", "omega"],
        "best_fhr": 14
    },
    {
        "label": "WSW-ENE along Lake Erie fetch axis (upwind shore to Hamburg)",
        "start": [42.4, -81.5], "end": [42.95, -78.5],
        "products": ["temperature", "cloud_total", "moisture_transport"],
        "best_fhr": 10
    }
]

for s in buffalo_sections:
    filtered = filter_markers_for_section(all_markers_buffalo, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20221118_00z", filtered)

events["20221118_00z"] = {
    "name": "Buffalo Lake Effect 81in",
    "category": "winter",
    "suggested_sections": buffalo_sections
}
save(events)

# =============================================
# 7. 20221223_06z - Winter Storm Elliott
# =============================================
print("\n=== 20221223_06z: Winter Storm Elliott ===")
all_markers_elliott = [
    {"lat": 42.89, "lon": -78.88, "label": "Buffalo"},
    {"lat": 42.72, "lon": -78.83, "label": "Hamburg"},
    {"lat": 41.50, "lon": -81.69, "label": "Cleveland"},
    {"lat": 43.15, "lon": -77.61, "label": "Rochester"},
]

elliott_sections = [
    {
        "label": "SW-NE through bomb cyclone center (MO Valley to Ontario)",
        "start": [38.0, -86.0], "end": [45.0, -76.0],
        "products": ["omega", "wind_speed", "frontogenesis"],
        "best_fhr": 8
    },
    {
        "label": "W-E across Lake Erie into Buffalo blizzard zone",
        "start": [42.6, -81.5], "end": [42.6, -77.5],
        "products": ["temperature", "cloud_total", "wind_speed", "q"],
        "best_fhr": 14
    },
    {
        "label": "N-S arctic front and temperature crash",
        "start": [46.0, -80.0], "end": [38.0, -80.0],
        "products": ["temperature", "theta_e", "frontogenesis"],
        "best_fhr": 6
    }
]

for s in elliott_sections:
    filtered = filter_markers_for_section(all_markers_elliott, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20221223_06z", filtered)

events["20221223_06z"] = {
    "name": "Winter Storm Elliott",
    "category": "winter",
    "suggested_sections": elliott_sections
}
save(events)

# =============================================
# 8. 20230104_12z - CA AR Strongest Storm
# =============================================
print("\n=== 20230104_12z: CA AR Strongest Storm ===")
all_markers_caar = [
    {"lat": 38.69, "lon": -120.07, "label": "Kirkwood"},
    {"lat": 38.94, "lon": -119.98, "label": "Lake Tahoe"},
    {"lat": 36.97, "lon": -122.03, "label": "Santa Cruz"},
    {"lat": 38.58, "lon": -121.49, "label": "Sacramento"},
]

caar_sections = [
    {
        "label": "SW-NE Pineapple Express plume into NorCal",
        "start": [34.0, -126.0], "end": [40.0, -119.0],
        "products": ["moisture_transport", "omega", "q"],
        "best_fhr": 14
    },
    {
        "label": "W-E Sierra Nevada orographic ascent at Tahoe latitude",
        "start": [39.0, -123.0], "end": [39.0, -119.0],
        "products": ["omega", "wind_speed", "cloud_total"],
        "best_fhr": 16
    },
    {
        "label": "NW-SE along bomb cyclone approach path",
        "start": [42.0, -127.0], "end": [36.0, -120.0],
        "products": ["wind_speed", "moisture_transport", "omega"],
        "best_fhr": 10
    }
]

for s in caar_sections:
    filtered = filter_markers_for_section(all_markers_caar, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20230104_12z", filtered)

events["20230104_12z"] = {
    "name": "CA AR Strongest Storm",
    "category": "ar",
    "suggested_sections": caar_sections
}
save(events)

# =============================================
# 9. 20230109_00z - CA AR Peak Flooding
# =============================================
print("\n=== 20230109_00z: CA AR Peak Flooding ===")
all_markers_cafl = [
    {"lat": 34.44, "lon": -119.63, "label": "Montecito"},
    {"lat": 34.42, "lon": -119.70, "label": "Santa Barbara"},
    {"lat": 36.75, "lon": -119.77, "label": "Fresno"},
    {"lat": 34.05, "lon": -118.25, "label": "Los Angeles"},
]

cafl_sections = [
    {
        "label": "SW-NE AR plume into SoCal coast (IVT axis)",
        "start": [32.0, -123.0], "end": [38.0, -119.0],
        "products": ["moisture_transport", "omega", "q"],
        "best_fhr": 10
    },
    {
        "label": "W-E orographic forcing Santa Ynez Mtns at Montecito",
        "start": [34.4, -121.5], "end": [34.4, -117.5],
        "products": ["omega", "cloud_total", "isentropic_ascent"],
        "best_fhr": 12
    },
    {
        "label": "NW-SE Central Valley flooding corridor",
        "start": [37.5, -121.0], "end": [35.0, -118.5],
        "products": ["moisture_transport", "q", "rh"],
        "best_fhr": 8
    }
]

for s in cafl_sections:
    filtered = filter_markers_for_section(all_markers_cafl, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20230109_00z", filtered)

events["20230109_00z"] = {
    "name": "CA AR Peak Flooding",
    "category": "ar",
    "suggested_sections": cafl_sections
}
save(events)

# =============================================
# 10. 20230621_18z - Red Rocks CO Hail + 36 Tornadoes
# =============================================
print("\n=== 20230621_18z: Red Rocks CO Hail + 36 Tornadoes ===")
all_markers_rr = [
    {"lat": 39.66, "lon": -105.20, "label": "Red Rocks"},
    {"lat": 40.16, "lon": -103.21, "label": "Akron"},
    {"lat": 39.74, "lon": -104.99, "label": "Denver"},
]

rr_sections = [
    {
        "label": "W-E across Front Range into eastern CO plains",
        "start": [39.66, -106.5], "end": [39.66, -102.5],
        "products": ["shear", "omega", "theta_e"],
        "best_fhr": 6
    },
    {
        "label": "SW-NE through Washington County tornado zone",
        "start": [39.0, -104.0], "end": [40.5, -102.0],
        "products": ["vorticity", "shear", "wind_speed"],
        "best_fhr": 5
    },
    {
        "label": "N-S dryline and instability axis eastern CO",
        "start": [41.0, -103.5], "end": [38.0, -103.5],
        "products": ["lapse_rate", "theta_e", "omega"],
        "best_fhr": 4
    }
]

for s in rr_sections:
    filtered = filter_markers_for_section(all_markers_rr, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20230621_18z", filtered)

events["20230621_18z"] = {
    "name": "Red Rocks CO Hail + 36 Tornadoes",
    "category": "hail",
    "suggested_sections": rr_sections
}
save(events)

# =============================================
# 11. 20240204_06z - Pineapple Express LA
# =============================================
print("\n=== 20240204_06z: Pineapple Express LA ===")
all_markers_pe = [
    {"lat": 34.08, "lon": -118.45, "label": "Bel-Air"},
    {"lat": 34.05, "lon": -118.25, "label": "Los Angeles"},
    {"lat": 34.17, "lon": -118.35, "label": "San Gabriel Mtns"},
]

pe_sections = [
    {
        "label": "SW-NE Pineapple Express plume into SoCal",
        "start": [30.0, -124.0], "end": [36.5, -117.0],
        "products": ["moisture_transport", "omega", "q"],
        "best_fhr": 12
    },
    {
        "label": "W-E orographic forcing across LA Basin",
        "start": [34.1, -119.5], "end": [34.1, -117.0],
        "products": ["omega", "cloud_total", "isentropic_ascent"],
        "best_fhr": 14
    },
    {
        "label": "S-N through San Gabriel Mtns showing orographic cap",
        "start": [33.5, -118.0], "end": [35.0, -118.0],
        "products": ["omega", "q", "wind_speed"],
        "best_fhr": 10
    }
]

for s in pe_sections:
    filtered = filter_markers_for_section(all_markers_pe, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20240204_06z", filtered)

events["20240204_06z"] = {
    "name": "Pineapple Express LA",
    "category": "ar",
    "suggested_sections": pe_sections
}
save(events)

# =============================================
# 12. 20240314_18z - DFW Hailstorm
# =============================================
print("\n=== 20240314_18z: DFW Hailstorm ===")
all_markers_dfw = [
    {"lat": 33.14, "lon": -97.07, "label": "Corinth"},
    {"lat": 32.78, "lon": -96.80, "label": "Dallas"},
    {"lat": 32.76, "lon": -97.33, "label": "Fort Worth"},
    {"lat": 33.21, "lon": -97.13, "label": "Denton"},
]

dfw_sections = [
    {
        "label": "SW-NE through DFW supercell corridor",
        "start": [32.2, -97.8], "end": [33.8, -96.2],
        "products": ["shear", "omega", "theta_e"],
        "best_fhr": 5
    },
    {
        "label": "W-E across warm front convergence zone",
        "start": [33.0, -98.5], "end": [33.0, -95.5],
        "products": ["lapse_rate", "wind_speed", "moisture_transport"],
        "best_fhr": 6
    },
    {
        "label": "S-N Gulf moisture feed into DFW",
        "start": [31.0, -97.0], "end": [34.5, -97.0],
        "products": ["theta_e", "omega", "shear"],
        "best_fhr": 4
    }
]

for s in dfw_sections:
    filtered = filter_markers_for_section(all_markers_dfw, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20240314_18z", filtered)

events["20240314_18z"] = {
    "name": "DFW Hailstorm",
    "category": "hail",
    "suggested_sections": dfw_sections
}
save(events)

# =============================================
# 13. 20240528_18z - South Plains DVD-Size Hail
# =============================================
print("\n=== 20240528_18z: South Plains DVD-Size Hail ===")
all_markers_sp = [
    {"lat": 33.60, "lon": -102.61, "label": "Whiteface"},
    {"lat": 33.59, "lon": -102.37, "label": "Levelland"},
    {"lat": 33.58, "lon": -101.85, "label": "Lubbock"},
    {"lat": 35.17, "lon": -103.72, "label": "Tucumcari"},
]

sp_sections = [
    {
        "label": "NW-SE supercell track from NM into TX South Plains",
        "start": [35.0, -104.0], "end": [32.5, -101.0],
        "products": ["shear", "omega", "wind_speed"],
        "best_fhr": 12
    },
    {
        "label": "W-E across dryline through Whiteface hail zone",
        "start": [33.59, -104.0], "end": [33.59, -101.0],
        "products": ["lapse_rate", "theta_e", "omega"],
        "best_fhr": 11
    },
    {
        "label": "S-N through Caprock instability axis",
        "start": [32.0, -102.5], "end": [35.0, -102.5],
        "products": ["theta_e", "shear", "vorticity"],
        "best_fhr": 10
    }
]

for s in sp_sections:
    filtered = filter_markers_for_section(all_markers_sp, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20240528_18z", filtered)

events["20240528_18z"] = {
    "name": "South Plains DVD-Size Hail",
    "category": "hail",
    "suggested_sections": sp_sections
}
save(events)

# =============================================
# 14. 20240531_00z - Denver Midnight Hail
# =============================================
print("\n=== 20240531_00z: Denver Midnight Hail ===")
all_markers_den = [
    {"lat": 39.92, "lon": -105.09, "label": "Broomfield"},
    {"lat": 39.84, "lon": -104.90, "label": "Commerce City"},
    {"lat": 39.73, "lon": -104.83, "label": "Aurora"},
    {"lat": 39.74, "lon": -104.99, "label": "Denver"},
]

den_sections = [
    {
        "label": "W-E through Denver metro hail swath",
        "start": [39.81, -105.8], "end": [39.81, -104.0],
        "products": ["omega", "shear", "lapse_rate"],
        "best_fhr": 10
    },
    {
        "label": "SW-NE Broomfield to Commerce City hail track",
        "start": [39.5, -105.3], "end": [40.1, -104.5],
        "products": ["wind_speed", "theta_e", "omega"],
        "best_fhr": 9
    },
    {
        "label": "S-N Palmer Divide convergence to hail zone",
        "start": [38.8, -104.9], "end": [40.5, -104.9],
        "products": ["theta_e", "shear", "temperature"],
        "best_fhr": 8
    }
]

for s in den_sections:
    filtered = filter_markers_for_section(all_markers_den, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20240531_00z", filtered)

events["20240531_00z"] = {
    "name": "Denver Midnight Hail",
    "category": "hail",
    "suggested_sections": den_sections
}
save(events)

# =============================================
# 15. 20240602_18z - Vigo Park TX 7in Hail
# =============================================
print("\n=== 20240602_18z: Vigo Park TX 7in Hail ===")
all_markers_vp = [
    {"lat": 34.65, "lon": -101.50, "label": "Vigo Park"},
    {"lat": 34.20, "lon": -101.71, "label": "Tulia"},
    {"lat": 35.22, "lon": -101.83, "label": "Amarillo"},
]

vp_sections = [
    {
        "label": "W-E across dryline through Vigo Park supercell",
        "start": [34.39, -103.0], "end": [34.39, -100.0],
        "products": ["lapse_rate", "shear", "theta_e"],
        "best_fhr": 11
    },
    {
        "label": "SW-NE through Panhandle supercell corridor",
        "start": [33.5, -102.5], "end": [35.5, -100.5],
        "products": ["omega", "wind_speed", "vorticity"],
        "best_fhr": 12
    },
    {
        "label": "S-N Caprock to Panhandle instability gradient",
        "start": [33.0, -101.49], "end": [36.0, -101.49],
        "products": ["theta_e", "lapse_rate", "shear"],
        "best_fhr": 9
    }
]

for s in vp_sections:
    filtered = filter_markers_for_section(all_markers_vp, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20240602_18z", filtered)

events["20240602_18z"] = {
    "name": "Vigo Park TX 7in Hail",
    "category": "hail",
    "suggested_sections": vp_sections
}
save(events)

# =============================================
# 16. 20241107_00z - Colorado Blizzard
# =============================================
print("\n=== 20241107_00z: Colorado Blizzard ===")
all_markers_cobliz = [
    {"lat": 39.86, "lon": -104.67, "label": "DIA"},
    {"lat": 37.17, "lon": -104.50, "label": "Trinidad"},
    {"lat": 38.27, "lon": -104.62, "label": "Pueblo"},
    {"lat": 38.83, "lon": -104.82, "label": "Colo Springs"},
]

cobliz_sections = [
    {
        "label": "W-E upslope flow transect through SE CO blizzard zone",
        "start": [37.8, -107.0], "end": [37.8, -102.0],
        "products": ["omega", "cloud_total", "q", "wind_speed"],
        "best_fhr": 12
    },
    {
        "label": "N-S from Denver through Trinidad along I-25 corridor",
        "start": [40.0, -104.8], "end": [37.0, -104.8],
        "products": ["temperature", "wetbulb", "moisture_transport"],
        "best_fhr": 8
    },
    {
        "label": "NE-SW through closed low center and Sangre de Cristo Mtns",
        "start": [39.0, -102.5], "end": [37.0, -106.0],
        "products": ["omega", "frontogenesis", "wind_speed"],
        "best_fhr": 16
    }
]

for s in cobliz_sections:
    filtered = filter_markers_for_section(all_markers_cobliz, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20241107_00z", filtered)

events["20241107_00z"] = {
    "name": "Colorado Blizzard",
    "category": "winter",
    "suggested_sections": cobliz_sections
}
save(events)

# =============================================
# 17. 20241119_12z - PNW Bomb Cyclone
# =============================================
print("\n=== 20241119_12z: PNW Bomb Cyclone ===")
all_markers_pnwbc = [
    {"lat": 47.61, "lon": -122.33, "label": "Seattle"},
    {"lat": 47.61, "lon": -122.20, "label": "Bellevue"},
    {"lat": 47.44, "lon": -122.30, "label": "Tacoma"},
]

pnwbc_sections = [
    {
        "label": "W-E from offshore low through Puget Sound to Cascades",
        "start": [47.6, -126.0], "end": [47.6, -120.0],
        "products": ["wind_speed", "pv", "omega"],
        "best_fhr": 8
    },
    {
        "label": "N-S through western WA wind damage corridor",
        "start": [49.0, -122.33], "end": [46.0, -122.33],
        "products": ["wind_speed", "frontogenesis", "vorticity"],
        "best_fhr": 8
    },
    {
        "label": "SW-NE through pressure gradient zone (coast to Cascades)",
        "start": [46.5, -124.5], "end": [48.5, -120.5],
        "products": ["pv", "moisture_transport", "wind_speed"],
        "best_fhr": 7
    }
]

for s in pnwbc_sections:
    filtered = filter_markers_for_section(all_markers_pnwbc, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20241119_12z", filtered)

events["20241119_12z"] = {
    "name": "PNW Bomb Cyclone",
    "category": "bomb_cyclone",
    "suggested_sections": pnwbc_sections
}
save(events)

# =============================================
# 18. 20250121_06z - Gulf Coast Blizzard Enzo
# =============================================
print("\n=== 20250121_06z: Gulf Coast Blizzard Enzo ===")
all_markers_enzo = [
    {"lat": 29.95, "lon": -90.07, "label": "New Orleans"},
    {"lat": 30.44, "lon": -87.21, "label": "Pensacola"},
    {"lat": 30.69, "lon": -88.04, "label": "Mobile"},
    {"lat": 30.45, "lon": -91.19, "label": "Baton Rouge"},
]

enzo_sections = [
    {
        "label": "N-S arctic air depth from Great Lakes to Gulf Coast",
        "start": [40.0, -90.0], "end": [28.0, -90.0],
        "products": ["temperature", "theta_e", "wind_speed"],
        "best_fhr": 6
    },
    {
        "label": "W-E across Gulf Coast snow band (LA through FL Panhandle)",
        "start": [30.5, -93.0], "end": [30.5, -85.5],
        "products": ["wetbulb", "cloud_total", "omega", "q"],
        "best_fhr": 12
    },
    {
        "label": "NW-SE overrunning snow production (arctic air vs Gulf moisture)",
        "start": [34.0, -93.0], "end": [29.0, -88.0],
        "products": ["temperature", "moisture_transport", "frontogenesis"],
        "best_fhr": 8
    }
]

for s in enzo_sections:
    filtered = filter_markers_for_section(all_markers_enzo, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20250121_06z", filtered)

events["20250121_06z"] = {
    "name": "Gulf Coast Blizzard Enzo",
    "category": "winter",
    "suggested_sections": enzo_sections
}
save(events)

# =============================================
# 19. 20250526_18z - Menard TX 5.87in Hail
# =============================================
print("\n=== 20250526_18z: Menard TX 5.87in Hail ===")
all_markers_menard = [
    {"lat": 30.92, "lon": -99.79, "label": "Menard"},
    {"lat": 31.46, "lon": -100.44, "label": "San Angelo"},
]

menard_sections = [
    {
        "label": "W-E across Edwards Plateau through Menard",
        "start": [30.92, -101.5], "end": [30.92, -98.0],
        "products": ["lapse_rate", "shear", "omega"],
        "best_fhr": 3
    },
    {
        "label": "SW-NE along dryline through supercell environment",
        "start": [30.0, -100.8], "end": [32.0, -98.8],
        "products": ["theta_e", "dewpoint_dep", "wind_speed"],
        "best_fhr": 4
    },
    {
        "label": "S-N Gulf moisture feed into central TX",
        "start": [29.5, -99.79], "end": [32.5, -99.79],
        "products": ["theta_e", "omega", "shear"],
        "best_fhr": 3
    }
]

for s in menard_sections:
    filtered = filter_markers_for_section(all_markers_menard, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20250526_18z", filtered)

events["20250526_18z"] = {
    "name": "Menard TX 5.87in Hail",
    "category": "hail",
    "suggested_sections": menard_sections
}
save(events)

# =============================================
# 20. 20250704_00z - TX MCV Flooding
# =============================================
print("\n=== 20250704_00z: TX MCV Flooding ===")
all_markers_mcv = [
    {"lat": 30.07, "lon": -99.34, "label": "Hunt"},
    {"lat": 30.05, "lon": -99.14, "label": "Kerrville"},
    {"lat": 30.01, "lon": -99.37, "label": "Camp Mystic"},
]

mcv_sections = [
    {
        "label": "SW-NE through MCV circulation and Guadalupe River headwaters",
        "start": [29.0, -100.5], "end": [31.0, -98.0],
        "products": ["omega", "vorticity", "moisture_transport"],
        "best_fhr": 8
    },
    {
        "label": "W-E through Hunt/Kerrville flooding zone",
        "start": [30.1, -100.5], "end": [30.1, -97.5],
        "products": ["moisture_transport", "q", "omega"],
        "best_fhr": 10
    },
    {
        "label": "S-N Gulf moisture feed into Hill Country (tropical moisture plume)",
        "start": [27.0, -98.5], "end": [32.0, -99.5],
        "products": ["moisture_transport", "theta_e", "q"],
        "best_fhr": 6
    }
]

for s in mcv_sections:
    filtered = filter_markers_for_section(all_markers_mcv, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20250704_00z", filtered)

events["20250704_00z"] = {
    "name": "TX MCV Flooding",
    "category": "other",
    "suggested_sections": mcv_sections
}
save(events)

# =============================================
# 21. 20251210_12z - PNW Mega-AR Cat 5
# =============================================
print("\n=== 20251210_12z: PNW Mega-AR Cat 5 ===")
all_markers_megaar = [
    {"lat": 47.98, "lon": -122.20, "label": "Snohomish"},
    {"lat": 48.42, "lon": -122.34, "label": "Mt Vernon"},
    {"lat": 47.61, "lon": -122.33, "label": "Seattle"},
]

megaar_sections = [
    {
        "label": "SW-NE AR plume from Pacific into WA Cascades",
        "start": [43.0, -128.0], "end": [50.0, -120.0],
        "products": ["moisture_transport", "omega", "q"],
        "best_fhr": 12
    },
    {
        "label": "W-E Cascades orographic forcing at Snohomish latitude",
        "start": [48.0, -125.0], "end": [48.0, -120.5],
        "products": ["omega", "cloud_total", "isentropic_ascent"],
        "best_fhr": 14
    },
    {
        "label": "N-S through Skagit-Snohomish flood zone",
        "start": [49.0, -122.0], "end": [47.0, -122.0],
        "products": ["moisture_transport", "q", "wind_speed"],
        "best_fhr": 10
    }
]

for s in megaar_sections:
    filtered = filter_markers_for_section(all_markers_megaar, s)
    s["markers"] = filtered
    if filtered:
        test_api(s, "20251210_12z", filtered)

events["20251210_12z"] = {
    "name": "PNW Mega-AR Cat 5",
    "category": "ar",
    "suggested_sections": megaar_sections
}
save(events)

# Final summary
print(f"\n{'='*60}")
print(f"COMPLETE: {len(events)} events processed")
total_sections = sum(len(e["suggested_sections"]) for e in events.values())
total_markers = sum(len(s.get("markers", [])) for e in events.values() for s in e["suggested_sections"])
print(f"Total sections: {total_sections}")
print(f"Total markers placed: {total_markers}")
print(f"Output: {OUTPUT}")
