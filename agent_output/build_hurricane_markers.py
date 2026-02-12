"""Build hurricane POI markers for 15 events and save to agent_hurricane.json"""
import json, math

def point_to_line_dist_km(plat, plon, slat, slon, elat, elon):
    """Approximate distance from point to line segment in km"""
    lat0 = math.radians((slat + elat) / 2)
    px = (plon - slon) * math.cos(lat0) * 111.32
    py = (plat - slat) * 111.32
    sx, sy = 0, 0
    ex = (elon - slon) * math.cos(lat0) * 111.32
    ey = (elat - slat) * 111.32
    dx, dy = ex - sx, ey - sy
    if dx == 0 and dy == 0:
        return math.sqrt(px**2 + py**2)
    t = max(0, min(1, ((px - sx) * dx + (py - sy) * dy) / (dx**2 + dy**2)))
    proj_x = sx + t * dx
    proj_y = sy + t * dy
    return math.sqrt((px - proj_x)**2 + (py - proj_y)**2)

output = {}

# 1. Hurricane Laura (20200826_18z) - Cameron LA
output['20200826_18z'] = {
    'suggested_sections': [
        {
            'label': 'S-N through-eye transect at landfall (perpendicular to motion)',
            'start': [28.0, -93.3],
            'end': [31.8, -93.3],
            'products': ['wind_speed', 'omega', 'moisture_transport'],
            'best_fhr': 12,
            'markers': [
                {'lat': 29.80, 'lon': -93.31, 'label': 'Landfall (Cameron)'},
                {'lat': 30.21, 'lon': -93.20, 'label': 'Lake Charles'}
            ]
        },
        {
            'label': 'W-E cross-eyewall transect',
            'start': [29.8, -95.0],
            'end': [29.8, -91.5],
            'products': ['wind_speed', 'cloud_total', 'vorticity'],
            'best_fhr': 12,
            'markers': [
                {'lat': 29.80, 'lon': -93.31, 'label': 'Cameron'}
            ]
        },
        {
            'label': 'SSE-NNW along-track transect (Gulf moisture feed to inland)',
            'start': [27.8, -92.5],
            'end': [31.5, -94.0],
            'products': ['moisture_transport', 'theta_e', 'omega'],
            'best_fhr': 10,
            'markers': [
                {'lat': 29.80, 'lon': -93.31, 'label': 'Landfall (Cameron)'},
                {'lat': 30.21, 'lon': -93.20, 'label': 'Lake Charles'}
            ]
        }
    ]
}

# 2. Hurricane Sally (20200916_00z) - Gulf Shores AL
output['20200916_00z'] = {
    'suggested_sections': [
        {
            'label': 'S-N through-eye transect at Gulf Shores landfall',
            'start': [28.5, -87.7],
            'end': [32.0, -87.7],
            'products': ['wind_speed', 'omega', 'moisture_transport'],
            'best_fhr': 10,
            'markers': [
                {'lat': 30.25, 'lon': -87.70, 'label': 'Landfall (Gulf Shores)'}
            ]
        },
        {
            'label': 'W-E rainfall/moisture transect across stalled storm',
            'start': [30.25, -89.5],
            'end': [30.25, -85.8],
            'products': ['moisture_transport', 'omega', 'q'],
            'best_fhr': 10,
            'markers': [
                {'lat': 30.25, 'lon': -87.70, 'label': 'Gulf Shores'},
                {'lat': 30.43, 'lon': -87.22, 'label': 'Pensacola'}
            ]
        },
        {
            'label': 'SSW-NNE Gulf moisture feed into AL/FL Panhandle',
            'start': [28.0, -88.5],
            'end': [32.0, -86.5],
            'products': ['theta_e', 'rh', 'moisture_transport'],
            'best_fhr': 8,
            'markers': [
                {'lat': 30.25, 'lon': -87.70, 'label': 'Landfall (Gulf Shores)'},
                {'lat': 30.43, 'lon': -87.22, 'label': 'Pensacola'}
            ]
        }
    ]
}

# 3. Hurricane Delta (20201009_12z) - Creole LA
output['20201009_12z'] = {
    'suggested_sections': [
        {
            'label': 'S-N through-eye transect near Creole at landfall',
            'start': [28.0, -93.1],
            'end': [31.5, -93.1],
            'products': ['wind_speed', 'omega', 'moisture_transport'],
            'best_fhr': 11,
            'markers': [
                {'lat': 29.76, 'lon': -93.10, 'label': 'Landfall (Creole)'},
                {'lat': 30.21, 'lon': -93.20, 'label': 'Lake Charles'}
            ]
        },
        {
            'label': 'W-E cross-eyewall transect',
            'start': [29.7, -94.8],
            'end': [29.7, -91.5],
            'products': ['wind_speed', 'cloud_total', 'vorticity'],
            'best_fhr': 11,
            'markers': [
                {'lat': 29.76, 'lon': -93.10, 'label': 'Creole'}
            ]
        },
        {
            'label': 'Along-track SSE-NNW through Gulf into LA',
            'start': [27.5, -92.0],
            'end': [31.5, -94.0],
            'products': ['moisture_transport', 'theta_e', 'omega'],
            'best_fhr': 9,
            'markers': [
                {'lat': 29.76, 'lon': -93.10, 'label': 'Landfall (Creole)'},
                {'lat': 30.21, 'lon': -93.20, 'label': 'Lake Charles'}
            ]
        }
    ]
}

# 4. Hurricane Zeta (20201028_12z) - Cocodrie LA
output['20201028_12z'] = {
    'suggested_sections': [
        {
            'label': 'S-N through-eye transect at Cocodrie landfall',
            'start': [27.5, -90.65],
            'end': [31.5, -90.65],
            'products': ['wind_speed', 'omega', 'moisture_transport'],
            'best_fhr': 9,
            'markers': [
                {'lat': 29.25, 'lon': -90.66, 'label': 'Landfall (Cocodrie)'}
            ]
        },
        {
            'label': 'W-E cross-eyewall transect across SE Louisiana',
            'start': [29.25, -92.0],
            'end': [29.25, -89.0],
            'products': ['wind_speed', 'vorticity', 'cloud_total'],
            'best_fhr': 9,
            'markers': [
                {'lat': 29.25, 'lon': -90.66, 'label': 'Cocodrie'}
            ]
        },
        {
            'label': 'SW-NE along fast inland track (LA to MS to AL)',
            'start': [28.0, -91.5],
            'end': [33.0, -87.5],
            'products': ['wind_speed', 'omega', 'theta_e'],
            'best_fhr': 12,
            'markers': [
                {'lat': 29.25, 'lon': -90.66, 'label': 'Landfall (Cocodrie)'},
                {'lat': 29.95, 'lon': -90.08, 'label': 'New Orleans'}
            ]
        }
    ]
}

# 5. Tropical Storm Eta (20201108_18z) - FL Keys
output['20201108_18z'] = {
    'suggested_sections': [
        {
            'label': 'SW-NE through Florida Keys crossing',
            'start': [24.0, -82.0],
            'end': [26.5, -79.5],
            'products': ['wind_speed', 'moisture_transport', 'omega'],
            'best_fhr': 10,
            'markers': [
                {'lat': 24.86, 'lon': -80.72, 'label': 'Landfall (Matecumbe Key)'},
                {'lat': 25.76, 'lon': -80.19, 'label': 'Miami'}
            ]
        },
        {
            'label': 'W-E across South Florida rainfall zone',
            'start': [25.8, -82.0],
            'end': [25.8, -79.5],
            'products': ['moisture_transport', 'omega', 'rh'],
            'best_fhr': 12,
            'markers': [
                {'lat': 25.76, 'lon': -80.19, 'label': 'Miami'}
            ]
        },
        {
            'label': 'S-N moisture feed from Caribbean into FL',
            'start': [23.5, -81.0],
            'end': [27.5, -80.5],
            'products': ['theta_e', 'q', 'moisture_transport'],
            'best_fhr': 8,
            'markers': [
                {'lat': 24.86, 'lon': -80.72, 'label': 'Landfall (Matecumbe Key)'}
            ]
        }
    ]
}

# 6. Hurricane Ida (20210829_06z) - Port Fourchon LA
output['20210829_06z'] = {
    'suggested_sections': [
        {
            'label': 'S-N through-eye transect at Port Fourchon landfall',
            'start': [27.5, -90.1],
            'end': [31.0, -90.1],
            'products': ['wind_speed', 'omega', 'moisture_transport'],
            'best_fhr': 11,
            'markers': [
                {'lat': 29.11, 'lon': -90.19, 'label': 'Landfall (Port Fourchon)'},
                {'lat': 29.95, 'lon': -90.08, 'label': 'New Orleans'}
            ]
        },
        {
            'label': 'W-E cross-eyewall transect across SE Louisiana',
            'start': [29.1, -91.5],
            'end': [29.1, -88.5],
            'products': ['wind_speed', 'cloud_total', 'vorticity'],
            'best_fhr': 11,
            'markers': [
                {'lat': 29.11, 'lon': -90.19, 'label': 'Port Fourchon'}
            ]
        },
        {
            'label': 'SSE-NNW along-track from Gulf through LA interior',
            'start': [27.0, -89.5],
            'end': [31.5, -90.8],
            'products': ['moisture_transport', 'theta_e', 'omega'],
            'best_fhr': 9,
            'markers': [
                {'lat': 29.11, 'lon': -90.19, 'label': 'Landfall (Port Fourchon)'},
                {'lat': 29.95, 'lon': -90.08, 'label': 'New Orleans'}
            ]
        }
    ]
}

# 7. Hurricane Nicholas (20210913_18z) - Matagorda Peninsula TX
output['20210913_18z'] = {
    'suggested_sections': [
        {
            'label': 'S-N through-eye transect at Matagorda Peninsula landfall',
            'start': [27.0, -95.6],
            'end': [30.5, -95.6],
            'products': ['wind_speed', 'omega', 'moisture_transport'],
            'best_fhr': 12,
            'markers': [
                {'lat': 28.83, 'lon': -95.66, 'label': 'Landfall (Sargent Beach)'},
                {'lat': 29.75, 'lon': -95.36, 'label': 'Houston'}
            ]
        },
        {
            'label': 'W-E rainfall transect across Houston metro',
            'start': [29.5, -97.0],
            'end': [29.5, -94.0],
            'products': ['moisture_transport', 'omega', 'rh'],
            'best_fhr': 14,
            'markers': [
                {'lat': 29.75, 'lon': -95.36, 'label': 'Houston'}
            ]
        },
        {
            'label': 'SSW-NNE moisture feed from Gulf into SE Texas',
            'start': [27.0, -96.5],
            'end': [30.5, -94.5],
            'products': ['theta_e', 'q', 'moisture_transport'],
            'best_fhr': 10,
            'markers': [
                {'lat': 28.83, 'lon': -95.66, 'label': 'Landfall (Sargent Beach)'},
                {'lat': 29.75, 'lon': -95.36, 'label': 'Houston'}
            ]
        }
    ]
}

# 8. Hurricane Ian (20220928_12z) - Cayo Costa FL
output['20220928_12z'] = {
    'suggested_sections': [
        {
            'label': 'SW-NE through-eye transect at Cayo Costa landfall',
            'start': [25.0, -83.5],
            'end': [28.5, -80.5],
            'products': ['wind_speed', 'omega', 'cloud_total'],
            'best_fhr': 7,
            'markers': [
                {'lat': 26.67, 'lon': -82.25, 'label': 'Landfall (Cayo Costa)'},
                {'lat': 26.45, 'lon': -81.95, 'label': 'Fort Myers Beach'}
            ]
        },
        {
            'label': 'W-E cross-peninsula transect through Fort Myers',
            'start': [26.6, -83.5],
            'end': [26.6, -80.0],
            'products': ['wind_speed', 'moisture_transport', 'rh'],
            'best_fhr': 7,
            'markers': [
                {'lat': 26.67, 'lon': -82.25, 'label': 'Cayo Costa'},
                {'lat': 26.45, 'lon': -81.95, 'label': 'Fort Myers Beach'}
            ]
        },
        {
            'label': 'S-N along-track from Gulf approach through FL interior',
            'start': [24.8, -82.5],
            'end': [29.0, -81.5],
            'products': ['moisture_transport', 'vorticity', 'theta_e'],
            'best_fhr': 6,
            'markers': [
                {'lat': 26.67, 'lon': -82.25, 'label': 'Landfall (Cayo Costa)'},
                {'lat': 26.56, 'lon': -81.95, 'label': 'Cape Coral'}
            ]
        }
    ]
}

# 9. Hurricane Nicole (20221110_00z) - Vero Beach FL
output['20221110_00z'] = {
    'suggested_sections': [
        {
            'label': 'W-E through-eye transect at Vero Beach landfall (from Atlantic approach)',
            'start': [27.6, -82.0],
            'end': [27.6, -78.5],
            'products': ['wind_speed', 'omega', 'moisture_transport'],
            'best_fhr': 8,
            'markers': [
                {'lat': 27.60, 'lon': -80.40, 'label': 'Landfall (Vero Beach)'}
            ]
        },
        {
            'label': 'S-N along FL Atlantic coast (wind field/erosion transect)',
            'start': [25.5, -80.2],
            'end': [30.0, -80.8],
            'products': ['wind_speed', 'cloud_total', 'omega'],
            'best_fhr': 8,
            'markers': [
                {'lat': 27.60, 'lon': -80.40, 'label': 'Landfall (Vero Beach)'}
            ]
        },
        {
            'label': 'NE-SW cross-peninsula moisture feed',
            'start': [29.0, -79.0],
            'end': [26.0, -82.0],
            'products': ['theta_e', 'moisture_transport', 'rh'],
            'best_fhr': 6,
            'markers': [
                {'lat': 27.60, 'lon': -80.40, 'label': 'Landfall (Vero Beach)'}
            ]
        }
    ]
}

# 10. Hurricane Idalia (20230830_00z) - Keaton Beach FL
output['20230830_00z'] = {
    'suggested_sections': [
        {
            'label': 'S-N through-eye transect at Keaton Beach landfall',
            'start': [27.8, -83.6],
            'end': [31.8, -83.6],
            'products': ['wind_speed', 'omega', 'cloud_total'],
            'best_fhr': 12,
            'markers': [
                {'lat': 29.82, 'lon': -83.59, 'label': 'Landfall (Keaton Beach)'},
                {'lat': 30.11, 'lon': -83.58, 'label': 'Perry'}
            ]
        },
        {
            'label': 'W-E cross-eyewall transect across Big Bend',
            'start': [29.8, -85.5],
            'end': [29.8, -81.5],
            'products': ['wind_speed', 'vorticity', 'moisture_transport'],
            'best_fhr': 12,
            'markers': [
                {'lat': 29.82, 'lon': -83.59, 'label': 'Keaton Beach'}
            ]
        },
        {
            'label': 'SSW-NNE along-track from Gulf approach through GA',
            'start': [27.5, -84.5],
            'end': [32.0, -82.5],
            'products': ['moisture_transport', 'theta_e', 'omega'],
            'best_fhr': 10,
            'markers': [
                {'lat': 29.82, 'lon': -83.59, 'label': 'Landfall (Keaton Beach)'},
                {'lat': 30.11, 'lon': -83.58, 'label': 'Perry'}
            ]
        }
    ]
}

# 11. Hurricane Lee Post-Tropical (20230916_06z) - Maine near-miss
output['20230916_06z'] = {
    'suggested_sections': [
        {
            'label': 'SW-NE across Maine coast as Lee passes offshore',
            'start': [42.0, -70.0],
            'end': [46.0, -65.0],
            'products': ['wind_speed', 'omega', 'vorticity'],
            'best_fhr': 10,
            'markers': [
                {'lat': 44.91, 'lon': -67.00, 'label': 'Eastport'}
            ]
        },
        {
            'label': 'W-E from inland Maine through wind field to offshore center',
            'start': [44.5, -70.5],
            'end': [44.5, -64.5],
            'products': ['wind_speed', 'moisture_transport', 'pv'],
            'best_fhr': 10,
            'markers': [
                {'lat': 44.91, 'lon': -67.00, 'label': 'Eastport'}
            ]
        },
        {
            'label': 'S-N extratropical transition cross-section (MA to NB)',
            'start': [41.0, -68.0],
            'end': [47.0, -66.0],
            'products': ['theta_e', 'omega', 'cloud_total'],
            'best_fhr': 12,
            'markers': [
                {'lat': 44.91, 'lon': -67.00, 'label': 'Eastport'}
            ]
        }
    ]
}

# 12. Hurricane Beryl (20240708_00z) - Matagorda TX
output['20240708_00z'] = {
    'suggested_sections': [
        {
            'label': 'S-N through-eye transect at Matagorda landfall',
            'start': [27.0, -95.9],
            'end': [30.5, -95.9],
            'products': ['wind_speed', 'omega', 'moisture_transport'],
            'best_fhr': 9,
            'markers': [
                {'lat': 28.69, 'lon': -95.97, 'label': 'Landfall (Matagorda)'}
            ]
        },
        {
            'label': 'W-E across Houston metro rainfall zone',
            'start': [29.5, -97.5],
            'end': [29.5, -94.0],
            'products': ['moisture_transport', 'omega', 'rh'],
            'best_fhr': 12,
            'markers': [
                {'lat': 29.75, 'lon': -95.36, 'label': 'Houston'}
            ]
        },
        {
            'label': 'SSW-NNE Gulf moisture feed into Texas coast',
            'start': [26.5, -96.5],
            'end': [30.5, -94.5],
            'products': ['theta_e', 'q', 'moisture_transport'],
            'best_fhr': 8,
            'markers': [
                {'lat': 29.75, 'lon': -95.36, 'label': 'Houston'}
            ]
        }
    ]
}

# 13. Hurricane Debby (20240805_00z) - Steinhatchee FL
output['20240805_00z'] = {
    'suggested_sections': [
        {
            'label': 'S-N through-eye transect at Steinhatchee landfall',
            'start': [27.7, -83.4],
            'end': [31.7, -83.4],
            'products': ['wind_speed', 'omega', 'moisture_transport'],
            'best_fhr': 11,
            'markers': [
                {'lat': 29.67, 'lon': -83.39, 'label': 'Landfall (Steinhatchee)'}
            ]
        },
        {
            'label': 'W-E across FL Big Bend rainfall zone',
            'start': [29.7, -85.5],
            'end': [29.7, -81.5],
            'products': ['moisture_transport', 'omega', 'rh'],
            'best_fhr': 11,
            'markers': [
                {'lat': 29.67, 'lon': -83.39, 'label': 'Steinhatchee'}
            ]
        },
        {
            'label': 'SSW-NNE Gulf moisture feed from Gulf into FL',
            'start': [27.5, -84.5],
            'end': [32.0, -82.0],
            'products': ['theta_e', 'q', 'moisture_transport'],
            'best_fhr': 9,
            'markers': [
                {'lat': 29.67, 'lon': -83.39, 'label': 'Landfall (Steinhatchee)'}
            ]
        }
    ]
}

# 14. Hurricane Helene (20240926_18z) - Big Bend FL + WNC flooding
output['20240926_18z'] = {
    'suggested_sections': [
        {
            'label': 'S-N landfall to WNC inland flooding (full Helene transect)',
            'start': [28.0, -84.3],
            'end': [36.0, -82.6],
            'products': ['wind_speed', 'moisture_transport', 'omega'],
            'best_fhr': 12,
            'markers': [
                {'lat': 30.00, 'lon': -83.70, 'label': 'Landfall (Perry)'},
                {'lat': 35.60, 'lon': -82.55, 'label': 'Asheville'}
            ]
        },
        {
            'label': 'W-E across Big Bend FL at landfall',
            'start': [29.9, -86.0],
            'end': [29.9, -81.8],
            'products': ['wind_speed', 'cloud_total', 'vorticity'],
            'best_fhr': 9,
            'markers': [
                {'lat': 30.00, 'lon': -83.70, 'label': 'Landfall (Perry)'}
            ]
        },
        {
            'label': 'SW-NE WNC orographic rainfall transect (Asheville focus)',
            'start': [34.0, -84.5],
            'end': [36.5, -81.5],
            'products': ['omega', 'moisture_transport', 'theta_e'],
            'best_fhr': 18,
            'markers': [
                {'lat': 35.60, 'lon': -82.55, 'label': 'Asheville'}
            ]
        }
    ]
}

# 15. Hurricane Milton (20241009_12z) - Siesta Key FL
output['20241009_12z'] = {
    'suggested_sections': [
        {
            'label': 'W-E landfall transect across FL peninsula through Siesta Key',
            'start': [27.2, -84.5],
            'end': [27.2, -80.0],
            'products': ['wind_speed', 'omega', 'cloud_total'],
            'best_fhr': 12,
            'markers': [
                {'lat': 27.27, 'lon': -82.55, 'label': 'Landfall (Siesta Key)'},
                {'lat': 27.34, 'lon': -82.53, 'label': 'Sarasota'}
            ]
        },
        {
            'label': 'SW-NE approach path from Gulf to landfall',
            'start': [25.5, -85.0],
            'end': [28.5, -81.0],
            'products': ['wind_speed', 'moisture_transport', 'vorticity'],
            'best_fhr': 10,
            'markers': [
                {'lat': 27.27, 'lon': -82.55, 'label': 'Landfall (Siesta Key)'},
                {'lat': 27.96, 'lon': -82.46, 'label': 'Tampa'}
            ]
        },
        {
            'label': 'S-N tornado outbreak zone (SE FL ahead of storm)',
            'start': [25.5, -80.5],
            'end': [29.0, -80.5],
            'products': ['shear', 'vorticity', 'theta_e'],
            'best_fhr': 8,
            'markers': [
                {'lat': 25.76, 'lon': -80.19, 'label': 'Miami'}
            ]
        }
    ]
}

# Validate all markers within 50km of section lines
warnings = []
for cycle_key, event in output.items():
    for section in event['suggested_sections']:
        slat, slon = section['start']
        elat, elon = section['end']
        for marker in section.get('markers', []):
            dist = point_to_line_dist_km(marker['lat'], marker['lon'], slat, slon, elat, elon)
            if dist > 50:
                warnings.append(
                    f"WARNING: {cycle_key} section \"{section['label'][:50]}\" "
                    f"marker \"{marker['label']}\" is {dist:.1f}km from line"
                )

if warnings:
    for w in warnings:
        print(w)
else:
    print("All markers within 50km of their section lines.")

total_markers = sum(
    len(m.get('markers', []))
    for e in output.values()
    for m in e['suggested_sections']
)
print(f"Total events: {len(output)}")
print(f"Total sections: {sum(len(e['suggested_sections']) for e in output.values())}")
print(f"Total markers: {total_markers}")

with open('C:/Users/drew/hrrr-maps/agent_output/agent_hurricane.json', 'w') as f:
    json.dump(output, f, indent=2)
print("Saved to agent_output/agent_hurricane.json")
