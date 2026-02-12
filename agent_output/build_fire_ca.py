"""Build marker data for 14 California fire events."""
import json
import os

data = {}

# ==========================================
# 1. 20180723_12z - Carr Fire Ignition
# Ignition: SR 299 near Whiskeytown (40.64, -122.56)
# Redding: 40.587, -122.392
# ==========================================
data["20180723_12z"] = {
    "suggested_sections": [
        {
            "label": "W-E through Sacramento River Canyon wind corridor",
            "start": [40.64, -123.3],
            "end": [40.64, -121.9],
            "products": ["wind_speed", "fire_wx", "rh"],
            "best_fhr": 10,
            "markers": [
                {"lat": 40.64, "lon": -122.56, "label": "Whiskeytown (ignition)"},
                {"lat": 40.59, "lon": -122.39, "label": "Redding"},
            ],
        },
        {
            "label": "N-S across fire spread axis toward Redding",
            "start": [41.1, -122.4],
            "end": [40.2, -122.8],
            "products": ["temperature", "vpd", "smoke"],
            "best_fhr": 12,
            "markers": [
                {"lat": 40.64, "lon": -122.56, "label": "Whiskeytown"},
                {"lat": 40.59, "lon": -122.39, "label": "Redding"},
            ],
        },
        {
            "label": "SW-NE through canyon channeling and terrain acceleration",
            "start": [40.3, -123.0],
            "end": [41.0, -122.2],
            "products": ["omega", "wind_speed", "fire_wx"],
            "best_fhr": 14,
            "markers": [
                {"lat": 40.64, "lon": -122.56, "label": "Whiskeytown"},
                {"lat": 40.59, "lon": -122.39, "label": "Redding"},
            ],
        },
    ]
}

# ==========================================
# 2. 20181108_00z - Camp Fire
# Pulga (ignition PG&E line): 39.87, -121.49
# Paradise: 39.76, -121.62
# ==========================================
data["20181108_00z"] = {
    "suggested_sections": [
        {
            "label": "NE-SW through Feather River Canyon Jarbo Gap wind corridor",
            "start": [40.2, -121.0],
            "end": [39.4, -121.9],
            "products": ["wind_speed", "fire_wx", "rh"],
            "best_fhr": 15,
            "markers": [
                {"lat": 39.87, "lon": -121.49, "label": "Pulga (ignition)"},
                {"lat": 39.76, "lon": -121.62, "label": "Paradise"},
            ],
        },
        {
            "label": "N-S through Paradise showing terrain-driven wind descent",
            "start": [40.1, -121.6],
            "end": [39.5, -121.6],
            "products": ["temperature", "wind_speed", "omega"],
            "best_fhr": 16,
            "markers": [
                {"lat": 39.76, "lon": -121.62, "label": "Paradise"},
                {"lat": 39.87, "lon": -121.49, "label": "Pulga"},
            ],
        },
        {
            "label": "W-E across Sierra foothills capturing downslope acceleration",
            "start": [39.8, -122.2],
            "end": [39.8, -120.7],
            "products": ["wind_speed", "vpd", "dewpoint_dep"],
            "best_fhr": 14,
            "markers": [
                {"lat": 39.76, "lon": -121.62, "label": "Paradise"},
                {"lat": 39.87, "lon": -121.49, "label": "Pulga"},
            ],
        },
    ]
}

# ==========================================
# 3. 20200817_12z - CA Lightning Siege - Outbreak
# LNU Complex area - Vacaville: 38.36, -121.99
# SCU Complex - San Jose: 37.34, -121.89
# Napa: 38.30, -122.29
# ==========================================
data["20200817_12z"] = {
    "suggested_sections": [
        {
            "label": "S-N through Bay Area/Napa lightning corridor (LNU Complex)",
            "start": [37.5, -122.3],
            "end": [39.5, -122.3],
            "products": ["theta_e", "omega", "rh"],
            "best_fhr": 4,
            "markers": [
                {"lat": 38.36, "lon": -121.99, "label": "Vacaville (LNU)"},
                {"lat": 38.30, "lon": -122.29, "label": "Napa"},
            ],
        },
        {
            "label": "SW-NE moisture plume from Tropical Storm Fausto remnants",
            "start": [35.5, -124.0],
            "end": [40.0, -120.0],
            "products": ["moisture_transport", "omega", "cloud_total"],
            "best_fhr": 2,
            "markers": [
                {"lat": 37.77, "lon": -122.42, "label": "San Francisco"},
                {"lat": 38.58, "lon": -121.49, "label": "Sacramento"},
            ],
        },
        {
            "label": "W-E through SCU Complex area across Central Valley to Sierra foothills",
            "start": [37.4, -122.8],
            "end": [37.4, -120.5],
            "products": ["temperature", "fire_wx", "vpd"],
            "best_fhr": 6,
            "markers": [
                {"lat": 37.40, "lon": -121.55, "label": "SCU Complex"},
                {"lat": 37.34, "lon": -121.89, "label": "San Jose"},
            ],
        },
    ]
}

# ==========================================
# 4. 20200818_12z - CA Lightning Siege - Expansion
# ==========================================
data["20200818_12z"] = {
    "suggested_sections": [
        {
            "label": "W-E through LNU Complex Napa/Sonoma fire zone",
            "start": [38.5, -123.0],
            "end": [38.5, -121.0],
            "products": ["wind_speed", "fire_wx", "smoke"],
            "best_fhr": 8,
            "markers": [
                {"lat": 38.30, "lon": -122.29, "label": "Napa"},
                {"lat": 38.36, "lon": -121.99, "label": "Vacaville"},
            ],
        },
        {
            "label": "N-S through multiple complexes (LNU to SCU corridor)",
            "start": [39.0, -121.8],
            "end": [37.2, -121.8],
            "products": ["rh", "temperature", "vpd"],
            "best_fhr": 10,
            "markers": [
                {"lat": 38.36, "lon": -121.99, "label": "Vacaville (LNU)"},
                {"lat": 37.34, "lon": -121.89, "label": "San Jose (SCU)"},
            ],
        },
        {
            "label": "SW-NE through CZU/Santa Cruz Mtns into Central Valley smoke plume",
            "start": [37.0, -122.5],
            "end": [38.0, -121.0],
            "products": ["smoke", "omega", "wind_speed"],
            "best_fhr": 12,
            "markers": [
                {"lat": 36.97, "lon": -122.03, "label": "Santa Cruz (CZU)"},
                {"lat": 37.34, "lon": -121.89, "label": "San Jose"},
            ],
        },
    ]
}

# ==========================================
# 5. 20200906_12z - Creek Fire Explosive Growth
# Shaver Lake: 37.10, -119.32
# Big Creek: 37.20, -119.25
# Mammoth Pool Reservoir: 37.35, -119.31
# ==========================================
data["20200906_12z"] = {
    "suggested_sections": [
        {
            "label": "W-E through Sierra fire zone capturing pyroCb convection",
            "start": [37.2, -120.0],
            "end": [37.2, -118.6],
            "products": ["smoke", "omega", "wind_speed"],
            "best_fhr": 10,
            "markers": [
                {"lat": 37.10, "lon": -119.32, "label": "Shaver Lake"},
                {"lat": 37.20, "lon": -119.25, "label": "Big Creek"},
            ],
        },
        {
            "label": "SW-NE pyroCb transect through San Joaquin drainage",
            "start": [36.8, -119.8],
            "end": [37.6, -118.8],
            "products": ["omega", "cloud_total", "theta_e"],
            "best_fhr": 12,
            "markers": [
                {"lat": 37.10, "lon": -119.32, "label": "Shaver Lake"},
                {"lat": 37.35, "lon": -119.31, "label": "Mammoth Pool"},
            ],
        },
        {
            "label": "S-N along Sierra crest through Big Creek fire progression",
            "start": [36.6, -119.3],
            "end": [37.8, -119.3],
            "products": ["fire_wx", "rh", "vpd"],
            "best_fhr": 11,
            "markers": [
                {"lat": 37.10, "lon": -119.32, "label": "Shaver Lake"},
                {"lat": 37.35, "lon": -119.31, "label": "Mammoth Pool"},
                {"lat": 37.20, "lon": -119.25, "label": "Big Creek"},
            ],
        },
    ]
}

# ==========================================
# 6. 20200927_00z - Glass Fire (Diablo Winds)
# Deer Park (ignition): 38.53, -122.47
# Calistoga: 38.58, -122.58
# Angwin: 38.58, -122.45
# Napa: 38.30, -122.29
# ==========================================
data["20200927_00z"] = {
    "suggested_sections": [
        {
            "label": "NE-SW through Diablo wind corridor into Napa Valley",
            "start": [39.0, -121.8],
            "end": [38.1, -123.1],
            "products": ["wind_speed", "fire_wx", "rh"],
            "best_fhr": 12,
            "markers": [
                {"lat": 38.53, "lon": -122.47, "label": "Deer Park (ignition)"},
                {"lat": 38.58, "lon": -122.58, "label": "Calistoga"},
            ],
        },
        {
            "label": "W-E across Coast Range gap channeling into Napa/Sonoma",
            "start": [38.56, -123.3],
            "end": [38.56, -121.6],
            "products": ["wind_speed", "omega", "vpd"],
            "best_fhr": 14,
            "markers": [
                {"lat": 38.53, "lon": -122.47, "label": "Deer Park"},
                {"lat": 38.58, "lon": -122.45, "label": "Angwin"},
            ],
        },
        {
            "label": "N-S through Napa Valley fire progression (Calistoga to Sonoma)",
            "start": [38.9, -122.5],
            "end": [38.2, -122.5],
            "products": ["temperature", "dewpoint_dep", "smoke"],
            "best_fhr": 16,
            "markers": [
                {"lat": 38.58, "lon": -122.58, "label": "Calistoga"},
                {"lat": 38.53, "lon": -122.47, "label": "Deer Park"},
                {"lat": 38.30, "lon": -122.29, "label": "Napa"},
            ],
        },
    ]
}

# ==========================================
# 7. 20201026_00z - SoCal Santa Ana Silverado/Blue Ridge
# Silverado Canyon (ignition): 33.76, -117.68
# Irvine: 33.67, -117.82
# Yorba Linda (Blue Ridge): 33.89, -117.81
# ==========================================
data["20201026_00z"] = {
    "suggested_sections": [
        {
            "label": "NE-SW through Santiago Canyon Santa Ana wind corridor",
            "start": [34.1, -117.1],
            "end": [33.4, -118.2],
            "products": ["wind_speed", "fire_wx", "rh"],
            "best_fhr": 16,
            "markers": [
                {"lat": 33.76, "lon": -117.68, "label": "Silverado (ignition)"},
                {"lat": 33.67, "lon": -117.82, "label": "Irvine"},
            ],
        },
        {
            "label": "W-E across Santa Ana Mountains terrain gap channeling",
            "start": [33.74, -118.3],
            "end": [33.74, -117.0],
            "products": ["wind_speed", "omega", "vpd"],
            "best_fhr": 18,
            "markers": [
                {"lat": 33.76, "lon": -117.68, "label": "Silverado Canyon"},
                {"lat": 33.67, "lon": -117.82, "label": "Irvine"},
            ],
        },
        {
            "label": "N-S from high desert through Santa Ana Canyon to coast",
            "start": [34.2, -117.5],
            "end": [33.3, -117.8],
            "products": ["temperature", "dewpoint_dep", "fire_wx"],
            "best_fhr": 15,
            "markers": [
                {"lat": 33.89, "lon": -117.81, "label": "Yorba Linda"},
                {"lat": 33.76, "lon": -117.68, "label": "Silverado"},
            ],
        },
    ]
}

# ==========================================
# 8. 20210804_12z - Dixie Fire Greenville Run
# Greenville: 40.14, -120.95
# Dixie Fire ignition (Cresta Dam): 39.82, -121.42
# ==========================================
data["20210804_12z"] = {
    "suggested_sections": [
        {
            "label": "SW-NE through Indian Valley wind channeling into Greenville",
            "start": [39.8, -121.4],
            "end": [40.5, -120.5],
            "products": ["wind_speed", "fire_wx", "rh"],
            "best_fhr": 12,
            "markers": [
                {"lat": 40.14, "lon": -120.95, "label": "Greenville"},
                {"lat": 39.82, "lon": -121.42, "label": "Ignition (Cresta)"},
            ],
        },
        {
            "label": "W-E across northern Sierra terrain and fire perimeter",
            "start": [40.14, -121.8],
            "end": [40.14, -120.1],
            "products": ["temperature", "vpd", "omega"],
            "best_fhr": 14,
            "markers": [
                {"lat": 40.14, "lon": -120.95, "label": "Greenville"},
            ],
        },
        {
            "label": "N-S through Dixie Fire active progression corridor",
            "start": [40.6, -121.0],
            "end": [39.7, -121.0],
            "products": ["smoke", "wind_speed", "fire_wx"],
            "best_fhr": 10,
            "markers": [
                {"lat": 40.14, "lon": -120.95, "label": "Greenville"},
                {"lat": 39.82, "lon": -121.42, "label": "Cresta Dam"},
            ],
        },
    ]
}

# ==========================================
# 9. 20220906_12z - CA Heat Wave + Mosquito Fire
# Mosquito Fire ignition (Oxbow Reservoir): 39.006, -120.745
# Foresthill: 39.02, -120.82
# Sacramento (116F record): 38.58, -121.49
# ==========================================
data["20220906_12z"] = {
    "suggested_sections": [
        {
            "label": "W-E through American River Canyon fire zone and heat dome",
            "start": [39.01, -121.5],
            "end": [39.01, -119.9],
            "products": ["temperature", "fire_wx", "vpd"],
            "best_fhr": 14,
            "markers": [
                {"lat": 39.01, "lon": -120.75, "label": "Ignition (Oxbow)"},
                {"lat": 39.02, "lon": -120.82, "label": "Foresthill"},
            ],
        },
        {
            "label": "SW-NE from Central Valley into Sierra foothills heat gradient",
            "start": [38.5, -121.5],
            "end": [39.5, -120.0],
            "products": ["rh", "omega", "wind_speed"],
            "best_fhr": 16,
            "markers": [
                {"lat": 38.58, "lon": -121.49, "label": "Sacramento (116F)"},
                {"lat": 39.01, "lon": -120.75, "label": "Mosquito Fire"},
            ],
        },
        {
            "label": "N-S through Placer/El Dorado County fire spread corridor",
            "start": [39.5, -120.74],
            "end": [38.5, -120.74],
            "products": ["smoke", "fire_wx", "temperature"],
            "best_fhr": 18,
            "markers": [
                {"lat": 39.01, "lon": -120.75, "label": "Ignition (Oxbow)"},
                {"lat": 39.02, "lon": -120.82, "label": "Foresthill"},
            ],
        },
    ]
}

# ==========================================
# 10. 20240725_12z - Park Fire
# Bidwell Park ignition (Alligator Hole): 39.76, -121.73
# Chico: 39.73, -121.84
# Ishi Wilderness: 40.02, -121.55
# ==========================================
data["20240725_12z"] = {
    "suggested_sections": [
        {
            "label": "W-E from Sacramento Valley into Sierra foothills fire progression",
            "start": [39.78, -122.6],
            "end": [39.78, -120.9],
            "products": ["fire_wx", "wind_speed", "temperature"],
            "best_fhr": 10,
            "markers": [
                {"lat": 39.73, "lon": -121.84, "label": "Chico"},
                {"lat": 39.76, "lon": -121.73, "label": "Bidwell Pk (ignition)"},
            ],
        },
        {
            "label": "S-N through Butte County from Chico into Ishi Wilderness/Lassen NF",
            "start": [39.4, -121.5],
            "end": [40.3, -121.8],
            "products": ["vpd", "smoke", "rh"],
            "best_fhr": 14,
            "markers": [
                {"lat": 39.73, "lon": -121.84, "label": "Chico"},
                {"lat": 39.76, "lon": -121.73, "label": "Ignition"},
            ],
        },
        {
            "label": "SW-NE along fire spread corridor through canyon terrain",
            "start": [39.5, -122.2],
            "end": [40.1, -121.3],
            "products": ["wind_speed", "omega", "fire_wx"],
            "best_fhr": 12,
            "markers": [
                {"lat": 39.76, "lon": -121.73, "label": "Bidwell Pk (ignition)"},
                {"lat": 40.02, "lon": -121.55, "label": "Ishi Wilderness"},
            ],
        },
    ]
}

# ==========================================
# 11. 20250107_00z - LA Santa Ana (Palisades/Eaton)
# Palisades Fire ignition (Skull Rock): 34.05, -118.55
# Altadena (Eaton Fire impact): 34.19, -118.13
# Eaton Canyon: 34.20, -118.10
# ==========================================
data["20250107_00z"] = {
    "suggested_sections": [
        {
            "label": "NE-SW Santa Ana wind corridor from Great Basin to LA coast",
            "start": [34.6, -117.5],
            "end": [33.7, -118.8],
            "products": ["wind_speed", "fire_wx", "rh"],
            "best_fhr": 20,
            "markers": [
                {"lat": 34.19, "lon": -118.13, "label": "Altadena (Eaton)"},
                {"lat": 34.05, "lon": -118.55, "label": "Palisades Fire"},
            ],
        },
        {
            "label": "N-S through San Gabriel Mountains to LA Basin (Eaton Canyon corridor)",
            "start": [34.8, -118.2],
            "end": [33.8, -118.2],
            "products": ["wind_speed", "omega", "vpd"],
            "best_fhr": 22,
            "markers": [
                {"lat": 34.20, "lon": -118.10, "label": "Eaton Canyon"},
                {"lat": 34.19, "lon": -118.13, "label": "Altadena"},
            ],
        },
        {
            "label": "W-E through Santa Monica Mountains to Palisades fire zone",
            "start": [34.05, -118.8],
            "end": [34.05, -117.6],
            "products": ["fire_wx", "dewpoint_dep", "temperature"],
            "best_fhr": 19,
            "markers": [
                {"lat": 34.05, "lon": -118.55, "label": "Palisades (ignition)"},
                {"lat": 34.19, "lon": -118.13, "label": "Altadena"},
            ],
        },
    ]
}

# ==========================================
# 12. 20250107_18z - Eaton Fire Onset
# Eaton Canyon ignition: 34.21, -118.10
# Altadena: 34.19, -118.13
# Pasadena: 34.15, -118.14
# ==========================================
data["20250107_18z"] = {
    "suggested_sections": [
        {
            "label": "N-S through Eaton Canyon from San Gabriel Mtns into Altadena/Pasadena",
            "start": [34.5, -118.1],
            "end": [33.9, -118.1],
            "products": ["wind_speed", "fire_wx", "omega"],
            "best_fhr": 10,
            "markers": [
                {"lat": 34.21, "lon": -118.10, "label": "Eaton Cyn (ignition)"},
                {"lat": 34.19, "lon": -118.13, "label": "Altadena"},
            ],
        },
        {
            "label": "NE-SW along Santa Ana wind corridor through San Gabriel passes",
            "start": [34.5, -117.6],
            "end": [33.9, -118.6],
            "products": ["wind_speed", "rh", "vpd"],
            "best_fhr": 12,
            "markers": [
                {"lat": 34.21, "lon": -118.10, "label": "Eaton Canyon"},
                {"lat": 34.19, "lon": -118.13, "label": "Altadena"},
            ],
        },
        {
            "label": "W-E across LA Basin capturing wind acceleration zones",
            "start": [34.19, -118.7],
            "end": [34.19, -117.5],
            "products": ["fire_wx", "dewpoint_dep", "temperature"],
            "best_fhr": 14,
            "markers": [
                {"lat": 34.19, "lon": -118.13, "label": "Altadena"},
                {"lat": 34.15, "lon": -118.14, "label": "Pasadena"},
            ],
        },
    ]
}

# ==========================================
# 13. 20250702_18z - Madre Fire
# Ignition on Hwy 166: 35.01, -119.98
# New Cuyama: 34.95, -119.69
# ==========================================
data["20250702_18z"] = {
    "suggested_sections": [
        {
            "label": "W-E through Cuyama Valley wind corridor along Highway 166",
            "start": [35.1, -120.8],
            "end": [35.1, -119.2],
            "products": ["wind_speed", "fire_wx", "vpd"],
            "best_fhr": 6,
            "markers": [
                {"lat": 35.01, "lon": -119.98, "label": "Ignition (Hwy 166)"},
                {"lat": 34.95, "lon": -119.69, "label": "New Cuyama"},
            ],
        },
        {
            "label": "S-N from Santa Barbara coast through Los Padres terrain to SLO",
            "start": [34.5, -120.0],
            "end": [35.7, -120.0],
            "products": ["temperature", "rh", "omega"],
            "best_fhr": 4,
            "markers": [
                {"lat": 35.01, "lon": -119.98, "label": "Ignition (Hwy 166)"},
            ],
        },
        {
            "label": "SW-NE through fire progression corridor and downslope wind zone",
            "start": [34.7, -120.5],
            "end": [35.5, -119.5],
            "products": ["fire_wx", "smoke", "wind_speed"],
            "best_fhr": 8,
            "markers": [
                {"lat": 35.01, "lon": -119.98, "label": "Ignition"},
                {"lat": 34.95, "lon": -119.69, "label": "New Cuyama"},
            ],
        },
    ]
}

# ==========================================
# 14. 20250801_18z - Gifford Fire
# Gifford Trailhead (ignition): 35.11, -120.08
# New Cuyama: 34.95, -119.69
# ==========================================
data["20250801_18z"] = {
    "suggested_sections": [
        {
            "label": "W-E through Highway 166 canyon corridor and Los Padres terrain",
            "start": [35.11, -120.9],
            "end": [35.11, -119.3],
            "products": ["wind_speed", "fire_wx", "vpd"],
            "best_fhr": 6,
            "markers": [
                {"lat": 35.11, "lon": -120.08, "label": "Gifford TH (ignition)"},
                {"lat": 34.95, "lon": -119.69, "label": "New Cuyama"},
            ],
        },
        {
            "label": "S-N from Santa Barbara coast through Sierra Madre Mountains",
            "start": [34.5, -120.1],
            "end": [35.7, -120.1],
            "products": ["temperature", "rh", "omega"],
            "best_fhr": 8,
            "markers": [
                {"lat": 35.11, "lon": -120.08, "label": "Gifford TH (ignition)"},
            ],
        },
        {
            "label": "SW-NE through fire progression from coast to interior valleys",
            "start": [34.7, -120.6],
            "end": [35.5, -119.6],
            "products": ["fire_wx", "smoke", "wind_speed"],
            "best_fhr": 10,
            "markers": [
                {"lat": 35.11, "lon": -120.08, "label": "Gifford TH"},
                {"lat": 34.95, "lon": -119.69, "label": "New Cuyama"},
            ],
        },
    ]
}

# Write the output file
output_path = "C:/Users/drew/hrrr-maps/agent_output/agent_fire_ca.json"
with open(output_path, "w") as f:
    json.dump(data, f, indent=2)

print(f"Wrote {len(data)} events to {output_path}")
for key in sorted(data.keys()):
    sections = data[key]["suggested_sections"]
    total_markers = sum(len(s.get("markers", [])) for s in sections)
    print(f"  {key}: {len(sections)} sections, {total_markers} markers")
