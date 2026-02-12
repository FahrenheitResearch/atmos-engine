"""
Nevada Fire-Vulnerable City Profiles -- Research-Paper Quality
===============================================================
Enhanced profiles for 8 Nevada communities with extreme wildfire vulnerability.
Covers terrain, historical fires, evacuation routes, infrastructure, demographics,
and fire spread characteristics at depth suitable for academic/research use.

Sources include USFS Community Wildfire Protection Plans, InciWeb incident data,
US Census Bureau (2020), Nevada Division of Forestry, Washoe County / Douglas County
fire plans, RCI Nevada Community Wildfire Risk/Hazard Assessments, peer-reviewed
fire behavior studies, NOAA/NWS fire weather data, and local/regional journalism
(Nevada Appeal, Record-Courier, This Is Reno, KUNR, Tahoe Daily Tribune).

Key regional context:
- Caldor Fire (2021) was the first fire to cross the Sierra crest in modern recorded
  history, forcing complete evacuation of South Lake Tahoe (~22,000 residents + visitors)
- Tahoe Basin receives 15-25 million visitors annually; peak weekends exceed 100K visitors
- Washoe Drive Fire (2012) destroyed 29 homes in hours with 80+ mph Washoe Zephyr winds
- Davis Fire (2024) burned 5,824 acres in Washoe Valley, evacuated 12,000-14,000 people
- Nevada's Great Basin rangeland fires burn millions of acres; cheatgrass (Bromus tectorum)
  has doubled fire frequency in sagebrush steppe from 30-110 yr cycles to 3-10 yr cycles
- Martin Fire (2018) burned 435,000 acres in Elko County -- largest in NV history

Generated: 2026-02-09
"""

NV_ENHANCED = {

    # =========================================================================
    # 1. RENO, NV -- "Biggest Little City" / Truckee Meadows WUI
    # =========================================================================
    "reno_nv": {
        "center": [39.5296, -119.8138],
        "terrain_notes": (
            "Reno (pop ~270,000; metro ~490,000 including Sparks) sits at approximately 4,505 ft "
            "elevation in the Truckee Meadows, a broad alluvial basin on the eastern flank of the "
            "Sierra Nevada. The city is bounded by the Carson Range of the Sierra Nevada to the "
            "west and southwest, with peaks exceeding 9,000 ft (Slide Mountain 9,698 ft, Mt. Rose "
            "10,778 ft) rising within 10-15 miles. The Virginia Range flanks the city to the east "
            "and northeast. The Truckee River bisects the city east-to-west, flowing from Lake Tahoe "
            "through downtown Reno and Sparks before terminating at Pyramid Lake 35 miles northeast. "
            "The western foothills contain some of the most fire-vulnerable WUI neighborhoods in the "
            "American West: Caughlin Ranch (5,096 residents, median income $112K), Galena Forest, "
            "Callahan Ranch, St. James Village, Juniper Hills, and the Mt. Rose corridor all push "
            "residential development deep into pinyon-juniper, sagebrush, and mixed-conifer terrain. "
            "South Reno extends toward Washoe Valley through Pleasant Valley -- a narrow corridor "
            "between the Carson Range and Virginia Range that acts as a wind tunnel during Washoe "
            "Zephyr events. Approximately 80% of homes in the Reno area face some level of wildfire "
            "risk per First Street Foundation assessments. The 2024 Davis Fire demonstrated this "
            "vulnerability starkly: an improperly extinguished campfire at Davis Creek grew to "
            "5,824 acres and forced evacuation of 12,000-14,000 people in September 2024. "
            "Human-caused ignitions account for the majority of Truckee Meadows wildfires."
        ),
        "key_features": [
            {"name": "Caughlin Ranch / Pinehaven", "bearing": "W", "type": "WUI_neighborhood",
             "notes": "Master-planned community in western foothills; 5,096 residents; mature trees and brush; Pinehaven Fire (2020) destroyed 5 homes here; ponderosa pine/sage interface"},
            {"name": "Mt. Rose / Galena Forest", "bearing": "SW", "type": "WUI_corridor",
             "notes": "SR-431 corridor from 4,500 ft to 8,911 ft summit; dense mixed conifer; scattered luxury homes; Davis Fire (2024) threatened this corridor; 2-lane mountain highway"},
            {"name": "Washoe Valley / Pleasant Valley", "bearing": "S", "type": "valley_corridor",
             "notes": "Narrow valley between Carson Range and Virginia Range; wind tunnel for Washoe Zephyr; site of Washoe Drive Fire (2012); US-395 corridor connects Reno to Carson City"},
            {"name": "Virginia Range", "bearing": "E/NE", "type": "mountain_range",
             "notes": "Semi-arid range east of Truckee Meadows; cheatgrass and sagebrush; wild horse habitat; fires spread rapidly in continuous grass fuels"},
            {"name": "Truckee River", "bearing": "E-W through city", "type": "river",
             "notes": "Primary waterway from Lake Tahoe through downtown; limited firebreak function due to narrow channel and extensive bridging; riparian corridor"},
            {"name": "Peavine Mountain", "bearing": "NW", "type": "mountain",
             "notes": "8,266 ft; north of city; BLM land with sagebrush/pinyon; popular recreation area; fires here would threaten north Reno/Stead neighborhoods"},
            {"name": "Humboldt-Toiyabe National Forest", "bearing": "W/SW", "type": "national_forest",
             "notes": "6.3 million acres (largest NF in lower 48); mixed conifer on Carson Range slopes; fuel loads increased by decades of fire suppression and drought-stressed trees"},
        ],
        "elevation_range_ft": [4400, 5600],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Davis Fire", "year": 2024, "acres": 5824,
             "details": (
                 "Ignited September 7 at Davis Creek Regional Park from improperly extinguished campfire. "
                 "Rapid growth in Washoe Valley; 14 structures destroyed; 12,000-14,000 people evacuated "
                 "from SW Reno, New Washoe City, and Mt. Rose corridor. Governor declared state of emergency. "
                 "Models predicted potential 3.5-7 mile northward expansion if forecasted 75 mph winds had "
                 "materialized on Sept 11. Contained September 25 after burning 5,824 acres."
             )},
            {"name": "Pinehaven Fire", "year": 2020, "acres": 512,
             "details": (
                 "Ignited November 17 near Caughlin Ranch from arcing power lines during high winds "
                 "(pre-existing campfire smoke created ionization between conductors). Destroyed 5 homes, "
                 "damaged 21 structures, injured 2 firefighters. Demonstrated vulnerability of west Reno "
                 "WUI neighborhoods even in late autumn. Mayor signed local state of emergency."
             )},
            {"name": "Washoe Drive Fire", "year": 2012, "acres": 3177,
             "details": (
                 "Ignited January 19 from improperly discarded hot fireplace ashes in northern Washoe Valley. "
                 "Washoe Zephyr winds exceeding 80 mph drove fire through Pleasant Valley. Destroyed 29 homes, "
                 "killed 1 person, injured 5 firefighters and 1 civilian. Over 10,000 people evacuated. "
                 "US-395 closed between Reno and Carson City. 98,300+ gallons of retardant dropped in first "
                 "3 days. Burned 3,177 acres. A transformative event for regional fire preparedness."
             )},
            {"name": "Caughlin Fire", "year": 2011, "acres": 1964,
             "details": (
                 "November wind-driven fire in southwest Reno near Caughlin Ranch. Destroyed 29 homes "
                 "and damaged 6 others. Demonstrated that Reno's western foothills are vulnerable to "
                 "rapid WUI fire runs even in the cold season. Caused by arcing power lines."
             )},
        ],
        "evacuation_routes": [
            {"route": "I-80 East (toward Sparks/Fernley)", "direction": "E", "lanes": 6,
             "bottleneck": "Sparks interchange congestion; merges with US-395 traffic",
             "risk": "Primary mass evacuation corridor; functional unless Virginia Range fires close it"},
            {"route": "I-80 West (toward Truckee/Sacramento)", "direction": "W", "lanes": 4,
             "bottleneck": "Truckee River canyon narrows I-80; winter chain controls; Donner Summit",
             "risk": "Sierra fires can close this corridor; smoke reduces visibility in canyon; single corridor west"},
            {"route": "US-395 South (toward Carson City)", "direction": "S", "lanes": 4,
             "bottleneck": "Pleasant Valley narrows between Carson Range and Virginia Range; single corridor south",
             "risk": "Washoe Drive Fire (2012) and Davis Fire (2024) both closed this route; wind tunnel terrain"},
            {"route": "US-395 North / I-580 (toward Stead/Lemmon Valley)", "direction": "N", "lanes": 4,
             "bottleneck": "Stead area traffic; limited destinations north (Susanville 85 mi)",
             "risk": "Leads into semi-arid rangeland; fewer services; Peavine Mountain fires could threaten"},
            {"route": "SR-431 Mt. Rose Highway (toward Incline Village)", "direction": "SW", "lanes": 2,
             "bottleneck": "Steep 2-lane mountain road; 8,911 ft summit; hairpin curves; heavy ski traffic",
             "risk": "Davis Fire closed this route in 2024; single road connecting Reno to north Lake Tahoe"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "The Washoe Zephyr -- a powerful downslope (foehn-type) wind from the Sierra Nevada -- "
                "is the dominant extreme fire weather driver. Southwest-to-northeast flow accelerates "
                "through the gap between the Carson Range and Virginia Range, reaching 60-100+ mph in "
                "Washoe Valley and Pleasant Valley. These events typically occur in autumn and winter "
                "but can strike in any season. Normal summer pattern features afternoon thermal winds "
                "15-25 mph from the west; overnight drainage flow reverses from canyons. The Truckee "
                "Meadows basin can trap smoke in inversions during light wind periods."
            ),
            "critical_corridors": [
                "Pleasant Valley / Washoe Valley -- wind tunnel between Carson and Virginia ranges; site of 2012 and 2024 fires",
                "Caughlin Ranch / Thomas Creek -- western foothills WUI with dense fuel loads directly above residential areas",
                "Mt. Rose corridor (SR-431) -- steep mixed-conifer terrain with scattered luxury homes; 2024 Davis Fire approach route",
                "Peavine Mountain slopes -- north Reno sagebrush/pinyon interface; BLM land with recreation-driven ignition risk",
                "Virginia Range east foothills -- cheatgrass-dominated rangeland fire can reach Sparks and Spanish Springs",
            ],
            "rate_of_spread_potential": (
                "Extreme during Washoe Zephyr events. Washoe Drive Fire moved 4+ miles in hours with "
                "80 mph winds. Grass/sage fuels on Virginia Range support 3-6 mph head fire spread; "
                "timber on Carson Range slopes can produce crown runs at 1-3 mph. Cheatgrass cures "
                "by late June, creating continuous fine fuels across Virginia Range. Davis Fire models "
                "predicted 3.5-7 mile expansion in a single wind event."
            ),
            "spotting_distance": (
                "0.5-2 miles in Washoe Zephyr events; extreme ember showers documented in Washoe Drive "
                "and Caughlin fires. Embers carried across US-395 into Pleasant Valley subdivisions. "
                "Pinyon-juniper stands produce intense spot fires with torching behavior."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Truckee Meadows Water Authority serves metro area from Truckee River diversions and "
                "groundwater wells. Urban core has adequate fire flow, but foothill WUI homes on "
                "smaller mains and dead-end roads (Caughlin Ranch, Galena, Callahan) may exceed "
                "system capacity during multi-structure fires. Hydrant coverage thins above 5,000 ft. "
                "Drought reduces Truckee River flows and reservoir levels."
            ),
            "power": (
                "NV Energy serves region; overhead transmission and distribution lines cross "
                "fire-prone foothills extensively. Both the 2020 Pinehaven Fire and 2011 Caughlin "
                "Fire were caused by arcing power lines during wind events. PSPS (Public Safety "
                "Power Shutoff) program implemented but creates secondary risks for medical equipment "
                "and communication systems. Grid vulnerable to multi-point failure during wind events."
            ),
            "communications": (
                "Good cellular coverage in Truckee Meadows proper; gaps in Washoe Valley and Mt. Rose "
                "corridor canyons. Cell towers on Peavine and Virginia Range ridgelines are fire-exposed. "
                "Washoe County CodeRED emergency notification system; WarnMe Nevada alerts. Davis Fire "
                "demonstrated communication challenges during rapid evacuation of 14,000 people."
            ),
            "medical": (
                "Renown Regional Medical Center (~800 beds, Level II Trauma), St. Mary's Regional "
                "Medical Center (~380 beds), and Northern Nevada Medical Center in Sparks provide "
                "robust capacity. Medical infrastructure not a limiting factor for city proper, but "
                "access to foothill neighborhoods can be cut during fires. Smoke events overwhelm "
                "respiratory care capacity -- 2024 Davis Fire smoke affected entire metro area."
            ),
        },
        "demographics_risk_factors": {
            "population": 270582,
            "seasonal_variation": (
                "University of Nevada, Reno adds ~21,000 students. Tourism brings ~5 million annual "
                "visitors; major events (Hot August Nights, Burning Man staging, Reno Air Races) "
                "concentrate tens of thousands of unfamiliar visitors during peak fire season. "
                "Lake Tahoe day-trip traffic surges on summer weekends."
            ),
            "elderly_percentage": "~15% over 65; higher in established foothill neighborhoods like Caughlin Ranch (median age 54)",
            "mobile_homes": (
                "Significant mobile home parks in Lemmon Valley, Sun Valley, and along US-395 "
                "corridor. Spanish Springs and Cold Springs have manufactured home concentrations. "
                "These areas face both direct fire threat and ember exposure from Virginia Range fires."
            ),
            "special_needs_facilities": (
                "Multiple assisted living and memory care facilities throughout metro area. UNR "
                "campus (21,000 students) within smoke impact zone. Washoe County jail (~1,200 "
                "capacity), homeless shelter populations along Truckee River corridor. VA Medical "
                "Center serves regional veteran population."
            ),
        },
    },

    # =========================================================================
    # 2. SOUTH LAKE TAHOE, CA/NV -- Caldor Fire Evacuation Zone
    # =========================================================================
    "south_lake_tahoe_nv": {
        "center": [38.9399, -119.9772],
        "terrain_notes": (
            "South Lake Tahoe (pop ~22,000 permanent; straddles CA/NV border) sits at 6,237 ft "
            "elevation on the southern shore of Lake Tahoe, surrounded on three sides by dense "
            "mixed-conifer forests of the Lake Tahoe Basin Management Unit (LTBMU). The city occupies "
            "a relatively narrow bench between the lake to the north and the Sierra crest to the "
            "south and west, with peaks exceeding 9,000-10,000 ft within 5-10 miles (Freel Peak "
            "10,886 ft, Mt. Tallac 9,738 ft, Echo Peak 8,895 ft). The Upper Truckee River and "
            "Trout Creek drain through the city from the Sierra crest to the lake. Forest density "
            "in the Tahoe Basin is approximately four times the historical average due to a century "
            "of fire suppression, creating extreme fuel loads of mixed red and white fir, Jeffrey "
            "pine, lodgepole pine, and dense understory. The Tahoe Basin has one of the highest "
            "wildfire ignition rates in the Sierra Nevada. The Caldor Fire (2021) was the first "
            "fire in modern recorded history to cross the Sierra crest, burning 221,835 acres from "
            "El Dorado County over the Crystal Range into the Tahoe Basin. The entire city of "
            "22,000+ residents was ordered to evacuate on August 30, 2021 -- the largest single-day "
            "evacuation in Lake Tahoe history. The 2007 Angora Fire destroyed 254 homes and 75 "
            "commercial structures just 3 miles from downtown, demonstrating that even small fires "
            "can be catastrophic in this terrain. Six roads lead in and out of the basin -- a "
            "critical evacuation constraint when 15-25 million annual visitors are factored in."
        ),
        "key_features": [
            {"name": "Lake Tahoe", "bearing": "N", "type": "lake",
             "notes": "Largest alpine lake in North America; 191 sq mi, max depth 1,645 ft; provides northern firebreak but constrains evacuation (no routes across the lake)"},
            {"name": "Sierra Crest / Crystal Range", "bearing": "SW/W", "type": "terrain",
             "notes": "10,000+ ft ridge; Caldor Fire crossed this barrier in 2021 -- first modern fire to do so; Echo Summit (7,382 ft) is the key pass on US-50"},
            {"name": "Angora Ridge", "bearing": "S", "type": "WUI_terrain",
             "notes": "Site of 2007 Angora Fire; dense residential/forest interface; 254 homes destroyed; fuel treatment demonstration area post-fire"},
            {"name": "Christmas Valley / Meyers", "bearing": "S/SW", "type": "community",
             "notes": "Gateway community at junction of US-50 and SR-89; first area impacted by Caldor Fire approach; USFS fuel treatments credited with saving structures"},
            {"name": "Heavenly Ski Resort", "bearing": "SE", "type": "terrain/infrastructure",
             "notes": "Straddles CA/NV border; steep forested terrain from 6,200 to 10,067 ft; gondola base in city center; ski runs serve as partial fuel breaks"},
            {"name": "Stateline / Casino Corridor", "bearing": "E", "type": "urban",
             "notes": "Dense hotel/casino development at NV state line; 10,000+ hotel rooms; massive population surge on weekends; limited parking lot refuge area"},
            {"name": "Upper Truckee River", "bearing": "S through city", "type": "river/drainage",
             "notes": "Primary drainage from Sierra crest through city to lake; riparian corridor provides limited firebreak; meadow areas used for fuel treatment"},
        ],
        "elevation_range_ft": [6225, 10900],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Caldor Fire", "year": 2021, "acres": 221835,
             "details": (
                 "Ignited August 14 near Pollock Pines; burned 69 days; 1,003 structures destroyed. "
                 "First modern fire to cross the Sierra Nevada crest, entering Tahoe Basin on August 29-30. "
                 "Entire city of South Lake Tahoe (22,000+ residents) ordered to evacuate at 10:59 AM "
                 "on August 30, creating massive traffic jams on US-50 eastbound. Over 50,000 people "
                 "evacuated from broader area. Decade of USFS fuel treatments in Christmas Valley and "
                 "Meyers credited with preventing total destruction. Cost: $287 million suppression."
             )},
            {"name": "Angora Fire", "year": 2007, "acres": 3100,
             "details": (
                 "Ignited June 24 from an illegal campfire; burned 3,100 acres in 2 days; destroyed "
                 "254 homes and 75 commercial structures; forced evacuation of 2,000+ people. Burned "
                 "within 3 miles of downtown South Lake Tahoe. Flame lengths exceeded 100 ft in dense "
                 "timber. Transformative event that catalyzed basin-wide fuel reduction programs. "
                 "Cost: $15.2 million suppression."
             )},
            {"name": "Gondola Fire", "year": 2002, "acres": 670,
             "details": (
                 "Burned near Heavenly Valley ski resort on the Nevada side; threatened Stateline casinos "
                 "and hotels. Demonstrated fire threat to the densely developed casino corridor."
             )},
            {"name": "Emerald Fire", "year": 2016, "acres": 200,
             "details": (
                 "Wind-driven fire near Emerald Bay on west shore; mandatory evacuations issued; "
                 "demonstrated vulnerability of SR-89 corridor and limited west-shore evacuation options."
             )},
        ],
        "evacuation_routes": [
            {"route": "US-50 East (toward Carson City via Spooner Summit)", "direction": "E/NE", "lanes": 2,
             "bottleneck": "Spooner Summit (7,146 ft) narrows to 2 lanes; single corridor east; massive gridlock during Caldor evacuation",
             "risk": "Primary evacuation route during Caldor Fire; 6+ hour delays reported; smoke and fire can close this route from south"},
            {"route": "US-50 West (toward Sacramento via Echo Summit)", "direction": "W", "lanes": 2,
             "bottleneck": "Echo Summit (7,382 ft); steep, winding 2-lane road; winter closures common",
             "risk": "Caldor Fire approached from this direction, closing westbound evacuation entirely"},
            {"route": "SR-89 North (West Shore to Tahoe City/Truckee)", "direction": "NW/N", "lanes": 2,
             "bottleneck": "Narrow 2-lane road hugging lakeshore cliffs; Emerald Bay narrows; no shoulder",
             "risk": "Single-lane sections; rockfall hazard; fires on west shore can close this corridor; long detour to I-80"},
            {"route": "SR-89 South (toward Luther Pass/Markleeville)", "direction": "S", "lanes": 2,
             "bottleneck": "Luther Pass (7,740 ft); narrow mountain road; limited destinations",
             "risk": "Leads toward Tamarack Fire (2021) area; remote 2-lane highway with few services"},
            {"route": "Kingsbury Grade (SR-207 to Gardnerville)", "direction": "SE", "lanes": 2,
             "bottleneck": "Steep grade (2,000 ft descent in 5 miles); tight switchbacks; 2-lane",
             "risk": "Narrow mountain road; can be closed by fire or winter weather; leads to Carson Valley"},
            {"route": "US-50 / SR-28 North (East Shore to Incline Village)", "direction": "NE", "lanes": 2,
             "bottleneck": "Cave Rock tunnel; narrow lakeshore road; connects to SR-431 (Mt. Rose Hwy)",
             "risk": "Long route around east shore; limited capacity; shares traffic with Incline Village evacuees"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Southwest flow dominates during fire weather events, driving fire upslope from the "
                "Sacramento Valley side of the Sierra, over the crest, and downslope into the Tahoe "
                "Basin -- exactly the Caldor Fire pattern. Afternoon thermal up-canyon winds push fire "
                "upslope at 10-20 mph along the Upper Truckee drainage. Foehn (Mono) winds from the "
                "east can drive fire from the Carson Range into the basin. Lake-effect breezes create "
                "complex, shifting local wind patterns. Inversions trap smoke in the basin for days."
            ),
            "critical_corridors": [
                "Upper Truckee River drainage -- SW-to-NE fire corridor from Sierra crest directly into city center",
                "Angora Ridge / Fallen Leaf -- dense timber WUI; 2007 fire destroyed 254 homes; still heavily developed",
                "Christmas Valley / Meyers -- gateway community on US-50; first line of defense against crest-crossing fires",
                "Heavenly Creek / Burke Creek -- steep east-facing drainages above Stateline casinos with dense fuel",
                "Echo Creek drainage -- US-50 corridor approach; funnels fire toward Echo Summit and down into basin",
            ],
            "rate_of_spread_potential": (
                "Extreme in wind-driven crown fire events. Caldor Fire made 15-mile runs on multiple "
                "days in heavy timber. Angora Fire destroyed 254 homes in approximately 48 hours over "
                "only 3,100 acres -- demonstrating that small, fast fires are equally catastrophic in "
                "dense WUI. Steep terrain (30-60% slopes) produces rapid uphill spread rates of "
                "2-4 mph in timber. Crown fire transitions are frequent due to ladder fuels."
            ),
            "spotting_distance": (
                "1-3 miles documented during Caldor Fire; extreme spotting from bark beetle-killed "
                "standing dead trees. Angora Fire produced 0.5-1 mile spot fires into residential "
                "areas. Dense canopy fuels generate intense convection columns that loft firebrands. "
                "Short-range ember showers (100-500 ft) are the primary home ignition mechanism."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "South Tahoe Public Utility District serves the California side; Kingsbury and Round "
                "Hill general improvement districts serve the Nevada side. Lake Tahoe provides "
                "theoretically unlimited water supply, but distribution infrastructure is the "
                "constraint -- aging mains, pressure zones, and limited hydrant density in "
                "residential-forest interface areas. Caldor Fire pre-positioning included portable "
                "pumps staged at the lake for structure protection."
            ),
            "power": (
                "Liberty Utilities (California) and NV Energy (Nevada) serve the area. Overhead "
                "power lines through dense forest are extremely vulnerable to fire damage and tree "
                "fall. Extended power outages during Caldor Fire complicated evacuation communications. "
                "No local power generation; all electricity imported via transmission lines through "
                "fire-prone corridors."
            ),
            "communications": (
                "Cell coverage adequate in town but degraded during mass evacuation (network overload). "
                "Cell towers on ridgelines are fire-exposed. Emergency alerts via Wireless Emergency "
                "Alert (WEA) system proved critical during Caldor evacuation. Limited landline backup. "
                "Tahoe Basin multi-jurisdictional communications complicated by CA/NV border -- "
                "different dispatch centers, frequencies, and mutual aid protocols."
            ),
            "medical": (
                "Barton Memorial Hospital (~62 beds) is the sole hospital; limited surge capacity. "
                "During Caldor evacuation, hospital was partially evacuated. Nearest Level II trauma "
                "is Renown Regional in Reno (~60 miles via Mt. Rose Hwy) or Carson Tahoe Regional "
                "in Carson City (~30 miles via Spooner Summit). Air ambulance critical but grounded "
                "during smoke events. Medical infrastructure is a significant limiting factor."
            ),
        },
        "demographics_risk_factors": {
            "population": 22158,
            "seasonal_variation": (
                "Lake Tahoe Basin receives 15-25 million visitors annually. Peak summer weekends bring "
                "100,000+ visitors to the south shore alone -- a 5x population surge. Winter ski season "
                "brings comparable crowds. Stateline casinos house 10,000+ hotel rooms. Most visitors "
                "are unfamiliar with evacuation routes and wildfire behavior. The Caldor Fire evacuation "
                "was complicated by tourists with no knowledge of local geography."
            ),
            "elderly_percentage": "~18% over 65; significant retiree population; many seasonal residents",
            "mobile_homes": (
                "Several older mobile home parks in Al Tahoe and Bijou neighborhoods near the lake. "
                "Manufactured homes with minimal defensible space in forested settings. These "
                "represent the highest-vulnerability housing stock in the basin."
            ),
            "special_needs_facilities": (
                "Barton Memorial Hospital, multiple assisted living facilities, Lake Tahoe Unified "
                "School District schools. Large transient visitor population with no local knowledge. "
                "Significant seasonal workforce (hospitality/casino) living in dense employee housing. "
                "Homeless population concentrated near commercial areas."
            ),
        },
    },

    # =========================================================================
    # 3. CARSON CITY, NV -- State Capital / Waterfall Fire
    # =========================================================================
    "carson_city_nv": {
        "center": [39.1638, -119.7674],
        "terrain_notes": (
            "Carson City (pop ~58,600), Nevada's state capital, occupies Eagle Valley at approximately "
            "4,802 ft elevation on the eastern edge of the Carson Range, a spur of the Sierra Nevada. "
            "The city is an independent city (consolidated city-county) with limits extending from "
            "the valley floor to the Sierra crest, encompassing terrain from 4,700 ft to Snow Valley "
            "Peak at 9,214 ft. The Carson Range rises dramatically to the west, with Kings Canyon, "
            "Ash Canyon, and Vicee Canyon cutting deeply into the mountain front and channeling both "
            "wind and fire directly toward residential neighborhoods. The 9,041-acre Carson City "
            "municipal watershed lies entirely within this steep, forested terrain -- and 63% of it "
            "(5,705 acres) burned in the 2004 Waterfall Fire. The Virginia Range flanks the city to "
            "the east with lower, sagebrush-covered slopes. The Carson River flows through the "
            "southwestern corner. Prison Hill (a prominent BLM-managed butte) sits in the southeast "
            "part of the city. The city has invested heavily in wildland fuels management since the "
            "Waterfall Fire, with the Carson City Wildland Fuels Division conducting prescribed burns "
            "and mechanical fuel treatments throughout the western foothills. Despite these efforts, "
            "continued WUI development up canyon drainages on the western edge maintains extreme "
            "fire exposure."
        ),
        "key_features": [
            {"name": "Kings Canyon", "bearing": "W", "type": "canyon/WUI",
             "notes": "Deep drainage cutting into Carson Range; origin of 2004 Waterfall Fire (illegal campfire at waterfall); residential development extends up-canyon; 10 homes lost in 2004"},
            {"name": "Ash Canyon", "bearing": "NW", "type": "canyon/WUI",
             "notes": "Parallel drainage north of Kings Canyon; residential development in canyon mouth; steep terrain with ponderosa pine/manzanita fuel beds; historic fire pathway into city"},
            {"name": "Vicee Canyon", "bearing": "W/NW", "type": "canyon/watershed",
             "notes": "Northern watershed canyon; part of the 63% burned in 2004; mixed conifer; USFS fuel treatment demonstration area"},
            {"name": "Carson Range / Sierra Crest", "bearing": "W", "type": "mountain_range",
             "notes": "Rises from 4,800 ft to 9,214 ft (Snow Valley Peak) within city limits; dense mixed conifer; steep east-facing slopes above residential areas"},
            {"name": "Prison Hill", "bearing": "SE", "type": "BLM_terrain",
             "notes": "Prominent sagebrush butte in SE Carson City; popular recreation area; grass/sage fires here threaten southern neighborhoods and Nevada State Prison site"},
            {"name": "Virginia Range", "bearing": "E", "type": "mountain_range",
             "notes": "Lower semi-arid range east of city; cheatgrass-invaded sagebrush; wild horse habitat; fires spread rapidly in continuous fine fuels"},
            {"name": "Carson River", "bearing": "SW", "type": "river",
             "notes": "Flows through southwestern Carson City; cottonwood riparian corridor; limited firebreak function; adjacent to residential development"},
        ],
        "elevation_range_ft": [4700, 9214],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Waterfall Fire", "year": 2004, "acres": 8799,
             "details": (
                 "Ignited July 14 at 3:15 AM from an illegal, abandoned campfire near the waterfall "
                 "in Kings Canyon. Drought conditions and high winds drove fire through western Carson "
                 "City. Burned 8,799 acres over 7 days; destroyed 18 homes (10 in Kings Canyon, 8 in "
                 "Timberline); 1,075 homes and businesses threatened; over 1,000 homes evacuated. "
                 "66 structures damaged or destroyed total. 2,000+ firefighters deployed; 3 fire "
                 "apparatus lost; 5 firefighters and 1 civilian injured. 98,300+ gallons of retardant "
                 "dropped in first 3 days. Suppression cost: $8 million. Burned 63% of the city's "
                 "municipal watershed (5,705 of 9,041 acres), causing post-fire erosion and flooding."
             )},
            {"name": "Voltaire Canyon Fire", "year": 2004, "acres": 180,
             "details": (
                 "Burned during same period as Waterfall Fire in Voltaire Canyon south of Kings Canyon. "
                 "Required evacuation of canyon residents. Demonstrated multi-front fire potential."
             )},
            {"name": "Carson City brush fires (recurring)", "year": 2022, "acres": 50,
             "details": (
                 "Multiple small fires near Prison Hill and along Highway 50 corridor. Quickly "
                 "suppressed but demonstrate ongoing ignition risk from recreation, vehicles, and "
                 "powerlines in the urban-wildland interface."
             )},
        ],
        "evacuation_routes": [
            {"route": "US-395 North (toward Reno)", "direction": "N", "lanes": 4,
             "bottleneck": "Pleasant Valley / Washoe Valley narrows; shared with Washoe Valley evacuees",
             "risk": "Washoe Drive Fire (2012) closed this route; wind tunnel terrain; same corridor threatened by Davis Fire (2024)"},
            {"route": "US-395 / I-580 South (toward Gardnerville/Minden)", "direction": "S", "lanes": 4,
             "bottleneck": "Jack's Valley Road intersection; Douglas County traffic merge",
             "risk": "Leads toward Carson Valley; functional unless Sierra fires cross into valley"},
            {"route": "US-50 East (toward Dayton/Stagecoach)", "direction": "E", "lanes": 4,
             "bottleneck": "Virginia Range pass; narrows east of city",
             "risk": "Crosses fire-prone Virginia Range sagebrush terrain; smoke can reduce visibility"},
            {"route": "US-50 West (toward Lake Tahoe via Spooner Summit)", "direction": "W", "lanes": 2,
             "bottleneck": "Spooner Summit (7,146 ft); steep 2-lane climb through Sierra forest",
             "risk": "Climbing into the fire zone; west side fires (Caldor pattern) make this an evacuation toward danger"},
            {"route": "SR-28 via US-50 to Incline Village", "direction": "NW", "lanes": 2,
             "bottleneck": "Mountain roads; indirect route via Spooner Summit and east shore",
             "risk": "Long, circuitous route with limited capacity; shares traffic with Tahoe evacuees"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Strong westerly downslope winds accelerate through Kings Canyon, Ash Canyon, and "
                "Vicee Canyon drainages, creating chimney effects that drive fire from the Sierra "
                "crest directly into western residential neighborhoods. Washoe Zephyr events can "
                "produce sustained winds of 40-60 mph with gusts exceeding 80 mph in canyon mouths. "
                "Afternoon thermal winds from the west at 10-20 mph during summer create daily fire "
                "weather windows. Diurnal canyon drainage winds reverse overnight but are typically lighter."
            ),
            "critical_corridors": [
                "Kings Canyon -- direct fire pathway from Sierra crest to city center; 2004 Waterfall Fire corridor",
                "Ash Canyon -- parallel drainage north of Kings; residential development at canyon mouth",
                "Vicee Canyon -- northern watershed canyon; steep terrain with heavy fuel loads",
                "Western foothills (Lakeview to Timberline) -- continuous WUI zone along entire Carson Range front",
                "Prison Hill corridor -- sagebrush terrain connecting Virginia Range fires to southern neighborhoods",
            ],
            "rate_of_spread_potential": (
                "Extreme in canyon-channeled wind events. Waterfall Fire grew from campfire to 8,799 "
                "acres in 7 days with explosive initial growth during first 24 hours. Steep east-facing "
                "slopes (30-50% grade) above residential areas produce rapid downhill fire runs during "
                "Zephyr winds. Manzanita and mountain mahogany understory creates extremely hot, "
                "fast-moving surface fire with easy transition to crown fire in pine/fir overstory."
            ),
            "spotting_distance": (
                "0.5-1.5 miles documented during Waterfall Fire. Canyon winds loft embers from "
                "Sierra forests into residential neighborhoods. Pinyon-juniper and manzanita produce "
                "intense spotting. Timberline neighborhood (8 homes lost) received ember showers "
                "from Kings Canyon fire front."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Carson City municipal water comes from wells and Marlette Lake/Hobart Reservoir "
                "system via pipeline from the Sierra. The 2004 Waterfall Fire burned 63% of the "
                "municipal watershed, causing post-fire erosion that compromised water quality for "
                "years. Fire flow capacity adequate in valley floor but western canyon subdivisions "
                "have dead-end water mains with pressure limitations. Drought reduces system capacity."
            ),
            "power": (
                "NV Energy serves Carson City; overhead distribution lines throughout western foothills "
                "are vulnerable to fire damage and tree fall. Transmission lines from Sierra corridors "
                "can be interrupted by fire. State government buildings have backup generators but "
                "residential areas do not. Power restoration after canyon fires can take days."
            ),
            "communications": (
                "Good cellular and landline coverage in Eagle Valley. Cell towers on Sierra ridges are "
                "fire-exposed. Carson City Emergency Management uses CodeRED mass notification system. "
                "As state capital, Carson City has robust government communication infrastructure "
                "including backup systems at the Legislature and Governor's office."
            ),
            "medical": (
                "Carson Tahoe Regional Medical Center (~100 beds) is the primary hospital. Limited "
                "surge capacity for mass casualty events. Level II trauma at Renown Regional in Reno "
                "(30 miles north). Smoke events during fire season stress respiratory care services. "
                "Multiple assisted living and nursing facilities in the city."
            ),
        },
        "demographics_risk_factors": {
            "population": 58639,
            "seasonal_variation": (
                "As state capital, Carson City has a large government workforce (8,000+ state employees) "
                "that commutes from surrounding areas. Tourism to the Nevada State Museum, Railroad Museum, "
                "and historic downtown is moderate. Lake Tahoe day-trip traffic passes through on US-50. "
                "Seasonal recreation in Sierra foothills (hiking, mountain biking) increases ignition risk."
            ),
            "elderly_percentage": "~20% over 65 (higher than state average); significant retiree population in western foothills",
            "mobile_homes": (
                "Several mobile home parks along US-395 south corridor and in eastern Carson City. "
                "Silver City (unincorporated, south of Carson) has significant manufactured housing. "
                "Mobile homes represent highest-vulnerability housing in ember exposure zones."
            ),
            "special_needs_facilities": (
                "Nevada State Prison (closed 2012, site redevelopment), state government offices, "
                "Carson City School District schools, multiple assisted living facilities. "
                "Warm Springs Correctional Center (medium security, ~600 inmates) on the south side. "
                "Large elderly population in western foothill neighborhoods requires targeted evacuation planning."
            ),
        },
    },

    # =========================================================================
    # 4. INCLINE VILLAGE, NV -- North Lake Tahoe / Extreme WUI
    # =========================================================================
    "incline_village_nv": {
        "center": [39.2516, -119.9530],
        "terrain_notes": (
            "Incline Village (pop ~9,000 permanent; census-designated place in Washoe County) sits "
            "at approximately 6,225 ft elevation on the northeast shore of Lake Tahoe, nestled into "
            "a steep amphitheater of forested slopes that rise 2,500-3,500 ft above the community "
            "on three sides. The community occupies a triangular bench between the lake to the south, "
            "the Diamond Peak / Mt. Rose corridor to the north and east, and dense USFS forest to "
            "the west. Topography consists of steep slopes generally exceeding 30% grade, with "
            "canyons and drainages that would create chimney effects during a wildfire, drawing fire "
            "through the canyons and into the community. Incline Village has been classified in the "
            "EXTREME hazard category by Nevada's Community Wildfire Risk/Hazard Assessment, with "
            "the score attributed primarily to inadequate defensible space, combustible building "
            "materials (many homes retain wood shake roofs), heavy fuel loadings, and steep slopes. "
            "Of the hundreds of homes assessed, only 20 met the defensible space landscape "
            "requirement to minimize damage during a wildfire. The community is one of the wealthiest "
            "in Nevada (median home value exceeding $1M), with large homes built deep into dense "
            "forest. State Route 431 (Mt. Rose Highway) is the primary -- and effectively sole -- "
            "evacuation route to Reno, climbing to 8,911 ft over a narrow, winding 2-lane mountain "
            "road. The 2024 Davis Fire closed this highway, stranding Incline Village with only "
            "the circuitous lakeshore route as an alternative."
        ),
        "key_features": [
            {"name": "Diamond Peak Ski Resort", "bearing": "NE", "type": "terrain/infrastructure",
             "notes": "Ski area rising from community to 8,540 ft; ski runs provide limited fuel breaks; dense forest surrounds access road and base area"},
            {"name": "Mt. Rose (10,778 ft)", "bearing": "N/NE", "type": "mountain",
             "notes": "Dominant peak above Incline Village; Mt. Rose Ski Tahoe on north slopes; SR-431 traverses summit area at 8,911 ft; Davis Fire climbed toward summit in 2024"},
            {"name": "Third Creek / Incline Creek", "bearing": "N through community", "type": "drainages",
             "notes": "Steep mountain drainages cutting through residential areas; create chimney effects channeling wind and fire into community from upper slopes"},
            {"name": "Lake Tahoe", "bearing": "S", "type": "lake",
             "notes": "Provides southern firebreak but also constrains evacuation to lakeshore routes only; no ferry or water evacuation capability for mass transit"},
            {"name": "Tunnel Creek Road area", "bearing": "E", "type": "WUI/recreation",
             "notes": "Popular mountain biking/hiking access; homes built into dense Jeffrey pine and white fir forest with minimal defensible space; single-access roads"},
            {"name": "Crystal Bay", "bearing": "W", "type": "community",
             "notes": "Adjacent community on CA/NV border; shares fire risk; SR-28 connects through narrow lakeshore road; additional ~1,000 residents"},
        ],
        "elevation_range_ft": [6225, 8900],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Davis Fire (threat)", "year": 2024, "acres": 5824,
             "details": (
                 "While the Davis Fire burned primarily in Washoe Valley, it climbed Mt. Rose slopes "
                 "and closed SR-431, cutting off the primary evacuation route from Incline Village to "
                 "Reno. Incline Village was not evacuated but the closure demonstrated the community's "
                 "extreme vulnerability to being isolated during a fire event. If the forecasted 75 mph "
                 "winds had materialized, the fire could have crested Mt. Rose and directly threatened "
                 "Incline Village."
             )},
            {"name": "Martis Fire", "year": 2001, "acres": 600,
             "details": (
                 "Burned northwest of Lake Tahoe near Northstar; demonstrated fire potential in the "
                 "north Tahoe region. Forced evacuations of recreational areas."
             )},
            {"name": "Incline Village area prescribed burns", "year": 2020, "acres": 200,
             "details": (
                 "USFS LTBMU and Nevada Division of Forestry conduct prescribed burns in Incline Village "
                 "area as part of basin-wide fuel reduction. Nearly 100,000 acres treated across Tahoe "
                 "Basin, but pace of treatment cannot keep up with fuel accumulation."
             )},
        ],
        "evacuation_routes": [
            {"route": "SR-431 (Mt. Rose Highway) to Reno", "direction": "NE", "lanes": 2,
             "bottleneck": "Steep 2-lane road; 8,911 ft summit; hairpin curves; 7%+ grades; heavy ski/recreation traffic",
             "risk": "SOLE direct route to Reno; closed by Davis Fire (2024); fire on Mt. Rose slopes cuts off the only fast evacuation"},
            {"route": "SR-28 West (toward Tahoe City via Crystal Bay)", "direction": "W", "lanes": 2,
             "bottleneck": "Narrow lakeshore road; tight curves; Crystal Bay section is single-lane in spots",
             "risk": "Long route (25+ miles to Tahoe City, then 15 miles to I-80); extremely slow; shares with west shore traffic"},
            {"route": "SR-28 South (East Shore to US-50)", "direction": "S", "lanes": 2,
             "bottleneck": "Cave Rock tunnel; narrow road; long route to South Lake Tahoe (30 miles)",
             "risk": "Circuitous; leads to another trapped community (South Lake Tahoe); not a true evacuation route"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Downslope Washoe Zephyr winds from the northeast drive fire from upper Mt. Rose "
                "slopes down toward the lake and community. Southwest winds during fire weather events "
                "push fire upslope from the lake through the community into upper terrain. Canyon "
                "drainages (Third Creek, Incline Creek) create chimney effects amplifying wind speed "
                "and fire intensity. Diurnal lake breezes create complex, shifting local wind patterns "
                "that complicate fire prediction."
            ),
            "critical_corridors": [
                "Third Creek / Incline Creek drainages -- chimney-effect fire corridors through densest residential areas",
                "Diamond Peak access road -- single-lane road through dense forest; fire here isolates upper-elevation homes",
                "Mt. Rose corridor (SR-431) -- fire in this corridor cuts evacuation while threatening community from above",
                "Lakeshore Drive / SR-28 -- narrow road that is both the urban core and the only alternative evacuation route",
            ],
            "rate_of_spread_potential": (
                "Extreme given steep slopes (>30%), dense fuels, and canyon channeling. The combination "
                "of heavy fuel loads (dense Jeffrey pine, white fir, lodgepole) with steep terrain "
                "and wind-channeling drainages can produce rapid crown fire runs. Slopes above the "
                "community could produce fire runs reaching the town boundary in under 1 hour from "
                "ignition at upper elevations during wind events."
            ),
            "spotting_distance": (
                "0.5-2 miles expected in wind-driven crown fire through dense canopy. Wood shake "
                "roofs (still present on many homes) dramatically increase receptivity to ember "
                "ignition. Dense tree canopy adjacent to structures creates near-zero defensible "
                "space, allowing structure ignition from radiant heat alone."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Incline Village General Improvement District (IVGID) water system serves the "
                "community from wells and treated lake water. Fire hydrant coverage is adequate in "
                "core areas but upper-elevation homes on dead-end roads may exceed system capacity "
                "during multi-structure fires. Water pressure limitations on steep terrain."
            ),
            "power": (
                "NV Energy serves the area; overhead distribution lines through dense forest are "
                "extremely vulnerable to fire damage. SR-431 corridor carries both power and "
                "communications infrastructure -- fire closing this corridor can isolate the "
                "community electrically as well as physically. No local generation capacity."
            ),
            "communications": (
                "Cell coverage adequate in town center; degraded in upper-elevation residential areas "
                "and drainages. Cell towers on Diamond Peak and Mt. Rose ridgeline are fire-exposed. "
                "North Lake Tahoe Fire Protection District emergency notification system. Multi-state "
                "jurisdiction (NV/CA border at Crystal Bay) complicates coordinated alerts."
            ),
            "medical": (
                "No hospital in Incline Village. Nearest hospital is Tahoe Forest Hospital in Truckee "
                "(~25 miles via SR-28 and I-80) or Renown in Reno (~35 miles via SR-431). If SR-431 "
                "is closed, the medical evacuation route is 60+ miles via lakeshore roads. North Lake "
                "Tahoe Fire Protection District operates 2 fire stations with paramedic capability."
            ),
        },
        "demographics_risk_factors": {
            "population": 9405,
            "seasonal_variation": (
                "Population effectively doubles or triples on peak weekends. Diamond Peak and Mt. Rose "
                "ski areas draw winter crowds; summer brings lake recreation visitors. Vacation rental "
                "properties (Airbnb/VRBO) mean many homes are occupied by unfamiliar visitors with "
                "no fire preparedness. Many homes are second residences occupied irregularly -- "
                "unmaintained defensible space and unresponsive to evacuation alerts."
            ),
            "elderly_percentage": "~22% over 65; wealthy retiree community; many seasonal residents",
            "mobile_homes": (
                "Very few mobile homes due to high property values and zoning. However, older "
                "homes (1960s-1970s construction) with wood shake roofs and no defensible space "
                "represent comparable vulnerability."
            ),
            "special_needs_facilities": (
                "Incline Village elementary and middle schools. Several vacation resort complexes. "
                "No hospital or major institutional facilities. Significant absentee-owner population "
                "means many homes lack occupants to respond during fire events."
            ),
        },
    },

    # =========================================================================
    # 5. VIRGINIA CITY, NV -- Historic Mining Town / Extreme Fire History
    # =========================================================================
    "virginia_city_nv": {
        "center": [39.3096, -119.6497],
        "terrain_notes": (
            "Virginia City (pop ~800; Storey County seat) sits at approximately 6,000 ft elevation "
            "on the eastern slopes of the Virginia Range, midslope on generally east-facing aspects "
            "above the Comstock Lode -- one of the richest silver deposits ever discovered. The town "
            "was established in 1859 and at its 1870s peak had ~25,000 residents. The townsite "
            "occupies a narrow bench on steep terrain (Sun Mountain / Mt. Davidson, 7,864 ft) with "
            "limited buildable area. Most surviving Comstock-era buildings are wooden frame "
            "construction -- the same building type that fueled the catastrophic Great Fire of 1875. "
            "Surrounding terrain is semi-arid with sagebrush, rabbitbrush, and scattered pinyon-juniper "
            "at higher elevations, transitioning to cheatgrass-invaded rangeland at lower elevations. "
            "The Virginia Range receives less precipitation than the nearby Carson Range, creating "
            "rapid fuel curing by early summer. Virginia City has been classified in the HIGH hazard "
            "category (75 points) by Nevada's Community Wildfire Risk/Hazard Assessment. Many "
            "Comstock-era buildings lie in the wildland-urban interface and are at risk of permanent "
            "loss in a wildfire. The town's historic status (National Historic Landmark District) "
            "complicates fuel mitigation -- clearing vegetation around irreplaceable 1860s-1870s "
            "structures must balance fire safety against historic preservation. Modern development "
            "in Virginia Highlands (residential area north of town) adds contemporary WUI exposure."
        ),
        "key_features": [
            {"name": "Mt. Davidson / Sun Mountain", "bearing": "W", "type": "mountain",
             "notes": "7,864 ft; immediately above town; steep slopes with sage/pinyon; fire here would run downslope into historic district; iconic location of 1860s mining claims"},
            {"name": "Comstock Historic District", "bearing": "center", "type": "historic",
             "notes": "National Historic Landmark; C Street commercial district with irreplaceable 1860s-1870s wooden buildings; fire would cause permanent cultural loss"},
            {"name": "Six Mile Canyon", "bearing": "N/NE", "type": "canyon",
             "notes": "Deep drainage northeast of town; sage/rabbitbrush fuels; fire can channel upslope from lower elevations into Virginia Highlands residential area"},
            {"name": "Gold Hill", "bearing": "S", "type": "community",
             "notes": "Historic mining settlement south of Virginia City; wooden structures; connected by SR-342; shares fire risk with Virginia City proper"},
            {"name": "Virginia Highlands", "bearing": "N", "type": "residential",
             "notes": "Modern residential development north of historic town; WUI exposure with sagebrush/pinyon interface; Volunteer Fire Department serves this area"},
            {"name": "Lousetown / American Flat", "bearing": "W/SW", "type": "terrain",
             "notes": "Open terrain west and south of town; old mine tailings and disturbed land interspersed with brush; limited vegetation management"},
        ],
        "elevation_range_ft": [5800, 7864],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Great Fire of 1875", "year": 1875, "acres": 0,
             "details": (
                 "October 26, 1875, at 5:15 AM: a coal oil lamp knocked over in a boarding house "
                 "ignited the largest fire in Virginia City's history. Strong winds spread flames "
                 "through 33 blocks over 9 hours. Approximately 2,000 structures destroyed -- roughly "
                 "75% of the city -- at the height of the Comstock Lode's economic apex. Hundreds left "
                 "homeless. The fire destroyed mining infrastructure, commercial buildings, churches, "
                 "and residences. Virginia City was largely rebuilt in brick and stone, but many wooden "
                 "structures remain from the reconstruction era and earlier buildings on the periphery."
             )},
            {"name": "Various Comstock-era fires", "year": 1863, "acres": 0,
             "details": (
                 "Virginia City experienced multiple devastating fires throughout its boom years -- "
                 "1863, 1866, 1869, and 1875 being the most destructive. Wooden construction, narrow "
                 "streets, and persistent wind made the town a serial fire victim. The 1875 fire was "
                 "simply the largest in a pattern of conflagrations."
             )},
            {"name": "Storey County brush fires (recurring)", "year": 2020, "acres": 500,
             "details": (
                 "Recurring sagebrush and grass fires in Virginia Range around Virginia City. Rapid "
                 "spread in cheatgrass and dried native grass. Most quickly contained but demonstrate "
                 "ongoing ignition risk from recreation, vehicles, and power lines."
             )},
        ],
        "evacuation_routes": [
            {"route": "SR-341 South (toward Carson City via Gold Hill)", "direction": "S/SW", "lanes": 2,
             "bottleneck": "Steep, winding descent through Gold Hill; narrow road cut into mountainside; limited turnouts",
             "risk": "Fire on western slopes of Virginia Range could close this route; smoke in canyon reduces visibility"},
            {"route": "SR-342 West (Geiger Grade toward Reno)", "direction": "W/NW", "lanes": 2,
             "bottleneck": "Geiger Grade -- extremely steep, winding descent; 2,000+ ft drop in ~7 miles; tight switchbacks",
             "risk": "Primary Reno access; fire on either side of the grade traps traffic; no alternative routes on this corridor"},
            {"route": "SR-341 North / SR-342 to US-50 (toward Dayton)", "direction": "E", "lanes": 2,
             "bottleneck": "Narrow roads through canyon terrain; limited capacity",
             "risk": "Leads to sparsely populated Dayton/Stagecoach area; limited services and onward evacuation options"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Strong westerly and southwesterly winds dominate fire weather events, driving fire "
                "upslope from lower Virginia Range terrain toward the town. The Washoe Zephyr affects "
                "this area with less intensity than Washoe Valley but still produces 40-60 mph gusts. "
                "Canyon drainages (Six Mile, Gold, Lousetown) channel winds and create localized "
                "acceleration. Diurnal upslope winds in afternoon heat push fire from lower sagebrush "
                "into pinyon-juniper zone near town."
            ),
            "critical_corridors": [
                "Six Mile Canyon -- NE drainage channeling fire from rangeland into Virginia Highlands residential area",
                "Mt. Davidson western slopes -- steep sage/pinyon terrain directly above historic district; fire runs downslope into C Street",
                "Geiger Grade (SR-342) -- fire in this corridor cuts primary Reno evacuation while threatening town from west",
                "Gold Hill / American Flat -- southern approach through disturbed mining terrain with patchy but flammable brush",
            ],
            "rate_of_spread_potential": (
                "High in sagebrush and cheatgrass fuels: 2-5 mph head fire spread on moderate slopes "
                "with wind. The 1875 Great Fire demonstrated that once fire enters the wooden-building "
                "district, conflagration spread is nearly unstoppable -- 33 blocks in 9 hours. Modern "
                "structure-to-structure spread risk remains high due to narrow lot spacing, wooden "
                "construction, and limited defensible space. Pinyon-juniper torching adds spotting risk."
            ),
            "spotting_distance": (
                "0.25-0.75 miles in sage/pinyon fuels with wind. The greater risk is ember ignition "
                "of wooden Comstock-era structures, which can spread fire building-to-building through "
                "the historic district. Narrow streets and shared walls in the commercial district "
                "replicate the conditions that allowed the 1875 conflagration."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Virginia City water historically sourced from the Marlette Lake water system (1870s "
                "engineering marvel). Modern system serves a small population but has limited fire "
                "flow capacity. Hydrant spacing in the historic district may be inadequate for "
                "multi-structure defense. Water pressure issues on steep terrain above C Street."
            ),
            "power": (
                "NV Energy serves the area; overhead lines through sagebrush/pinyon terrain are "
                "fire-exposed. Limited backup power for the small community. Power outage during "
                "fire event would eliminate communications for many residents."
            ),
            "communications": (
                "Limited cell coverage due to mountainous terrain and small population. Storey County "
                "Emergency Management and Local Emergency Planning Committee coordinate alerts. "
                "Virginia City Volunteer Fire Department and Virginia Highlands VFD provide local "
                "response but rely on mutual aid from Carson City and Truckee Meadows for larger events."
            ),
            "medical": (
                "No hospital or clinic in Virginia City. Nearest emergency medical care is in Carson "
                "City (~15 miles) or Reno (~25 miles via Geiger Grade). Storey County Fire Department "
                "provides EMS. Remote location means extended response times for mutual aid. "
                "Air ambulance is the best option but grounded during smoke events."
            ),
        },
        "demographics_risk_factors": {
            "population": 800,
            "seasonal_variation": (
                "Tourism drives major population surges. Virginia City is a popular historic tourism "
                "destination attracting hundreds of thousands of visitors annually for events, shops, "
                "saloons, and mine tours. Peak weekends can bring 5,000-10,000 visitors to a town "
                "of 800 residents. Most visitors are unfamiliar with the limited evacuation options."
            ),
            "elderly_percentage": "~25% over 65; aging resident population; many long-term residents in older homes",
            "mobile_homes": (
                "Some manufactured housing in Virginia Highlands and lower Gold Hill area. "
                "Older Comstock-era homes with wooden construction are comparably or more vulnerable "
                "than mobile homes to fire."
            ),
            "special_needs_facilities": (
                "Virginia City elementary school (one of Nevada's oldest). Storey County Courthouse. "
                "No institutional facilities. Small, aging population with limited personal "
                "transportation options. Tourist population with no local knowledge complicates "
                "evacuation scenarios."
            ),
        },
    },

    # =========================================================================
    # 6. GARDNERVILLE / MINDEN, NV -- Carson Valley / Tamarack Fire Corridor
    # =========================================================================
    "gardnerville_minden_nv": {
        "center": [38.9413, -119.7499],
        "terrain_notes": (
            "Gardnerville (pop ~6,200) and Minden (pop ~3,400) are adjacent unincorporated towns "
            "in Douglas County's Carson Valley, sitting at approximately 4,700-4,750 ft elevation "
            "on the broad valley floor between the Carson Range / Sierra Nevada to the west and the "
            "Pine Nut Mountains to the east. The communities serve as the commercial and government "
            "center of Carson Valley (Minden is the county seat). The Sierra escarpment rises "
            "dramatically from the valley floor, gaining 4,000-5,000 ft in just a few miles to "
            "peaks like Jobs Peak (10,633 ft) and Freel Peak (10,886 ft). The Humboldt-Toiyabe "
            "National Forest covers the Sierra slopes above the valley. The Tamarack Fire (2021) "
            "demonstrated the direct threat to these communities: a lightning-caused fire in the "
            "Humboldt-Toiyabe NF crossed the Sierra crest from Alpine County, California, burned "
            "68,637 acres, and entered Nevada before being contained. The 2020 Numbers Fire burned "
            "18,380 acres along US-395 south of Gardnerville, destroying 40 structures including "
            "3 homes and closing a 15-mile stretch of Highway 395 -- the valley's primary north-south "
            "artery. The Pine Nut Mountains to the east are lower and drier, with cheatgrass-invaded "
            "sagebrush that burns rapidly. The Carson River flows through the western portion of "
            "the valley. Douglas County's population has grown significantly, pushing residential "
            "development closer to the WUI on both the Sierra and Pine Nut Mountain sides."
        ),
        "key_features": [
            {"name": "Jobs Peak / Sierra Escarpment", "bearing": "W", "type": "mountain",
             "notes": "10,633 ft; dramatic 5,000+ ft rise above valley floor; dense mixed conifer on eastern slopes; Tamarack Fire (2021) burned toward this escarpment"},
            {"name": "Pine Nut Mountains", "bearing": "E", "type": "mountain_range",
             "notes": "Lower semi-arid range (7,000-8,000 ft); pinyon-juniper woodland over sagebrush; cheatgrass invasion; fires from east can threaten valley communities"},
            {"name": "US-395 corridor", "bearing": "N-S through valley", "type": "highway",
             "notes": "Primary north-south route; Numbers Fire (2020) closed 15-mile stretch; critical evacuation and supply corridor; Carson Valley's lifeline"},
            {"name": "Carson River", "bearing": "W/NW through valley", "type": "river",
             "notes": "Flows from Alpine County through western Carson Valley; cottonwood/willow riparian; limited firebreak; flood risk in post-fire watershed conditions"},
            {"name": "Kingsbury Grade (SR-207)", "bearing": "W/NW", "type": "mountain_pass",
             "notes": "Steep grade from valley floor (4,750 ft) to Daggett Pass (7,334 ft) and Lake Tahoe; 2-lane; connects valley to south shore Tahoe"},
            {"name": "Foothill Road / Sierra foothills WUI", "bearing": "W", "type": "WUI_corridor",
             "notes": "Residential development along base of Sierra escarpment; ranch properties and newer subdivisions pushing into NF interface; primary WUI exposure zone"},
            {"name": "Spring Valley", "bearing": "S", "type": "community",
             "notes": "Residential area south of Gardnerville along US-395; 2024 fire threatened homes here; pinyon-juniper and sagebrush terrain; remote with limited road access"},
        ],
        "elevation_range_ft": [4700, 5200],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Tamarack Fire", "year": 2021, "acres": 68637,
             "details": (
                 "Lightning-caused fire reported July 4 in Mokelumne Wilderness, Alpine County, CA. "
                 "Initially left to burn as a natural fire but exploded on July 16 when high winds "
                 "and dry fuels drove it 21,000 acres in a single day. Crossed Sierra crest into "
                 "Nevada by July 21. Burned 68,637 acres total across Alpine County (CA), Douglas "
                 "County (NV), and Lyon County (NV). Destroyed 23 structures. Forced evacuation of "
                 "2,439 people from Markleeville, Alpine Village, Woodfords, and other communities. "
                 "Carson Valley suffered extremely poor air quality with smoke and ashfall for weeks. "
                 "Alpine County evacuation center relocated to Douglas County Senior Center in Gardnerville."
             )},
            {"name": "Numbers Fire", "year": 2020, "acres": 18380,
             "details": (
                 "Ignited July 6 from a semi-tractor trailer's failing exhaust system on US-395 "
                 "south of Gardnerville. Burned 18,380 acres in cheatgrass and sagebrush along the "
                 "highway corridor. Destroyed 40 structures including 3 homes. Mandatory evacuations "
                 "of Pine View Estates and Bodie Flats. Closed 15-mile stretch of US-395 -- the "
                 "valley's primary transportation artery. 98% contained by July 13."
             )},
            {"name": "Spring Valley Fire", "year": 2024, "acres": 264,
             "details": (
                 "Fast-moving brush fire south of Gardnerville in July 2024; threatened Spring Valley "
                 "homes; residents evacuated; 1 residence destroyed. Demonstrated ongoing fire threat "
                 "to communities along US-395 corridor. Quickly suppressed at 264 acres."
             )},
        ],
        "evacuation_routes": [
            {"route": "US-395 North (toward Carson City)", "direction": "N", "lanes": 4,
             "bottleneck": "Jack's Valley Road area; merges with Carson City traffic",
             "risk": "Primary evacuation corridor; functional unless fire is between Gardnerville and Carson City"},
            {"route": "US-395 / SR-208 South (toward Topaz Lake / US-395 Alt)", "direction": "S", "lanes": 2,
             "bottleneck": "Narrows to 2 lanes south of town; rural highway; Numbers Fire closed this",
             "risk": "Numbers Fire (2020) demonstrated this corridor's vulnerability; cheatgrass fuels on both sides of road"},
            {"route": "SR-88 West (toward Woodfords / Carson Pass)", "direction": "W", "lanes": 2,
             "bottleneck": "Mountain road climbing to Carson Pass (8,574 ft); narrow; winter closures",
             "risk": "Leads toward Tamarack Fire (2021) area; climbing into fire zone during Sierra events; seasonal closure"},
            {"route": "Kingsbury Grade (SR-207) to Lake Tahoe", "direction": "NW", "lanes": 2,
             "bottleneck": "Very steep 2-lane grade; tight switchbacks; heavy recreation traffic",
             "risk": "Climbing into potential fire zone; connects to trapped Lake Tahoe basin"},
            {"route": "SR-756 / Foothill Road (local)", "direction": "N/S along foothills", "lanes": 2,
             "bottleneck": "Local road; limited capacity; dead-end segments",
             "risk": "Runs along base of Sierra foothills -- the WUI corridor; fire on Sierra slopes would cut this road"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Strong westerly downslope winds from the Sierra crest can drive fire from high-elevation "
                "forest down the escarpment into the Carson Valley in hours. The Tamarack Fire demonstrated "
                "this west-to-east pattern. East winds (less common but documented) can push Pine Nut "
                "Mountain rangeland fires toward the valley communities. Afternoon thermal winds from "
                "the west at 10-20 mph are the normal summer pattern. Valley floor winds can shift "
                "rapidly due to differential heating between the Sierra and Pine Nut ranges."
            ),
            "critical_corridors": [
                "Sierra escarpment drainages -- steep canyons above Foothill Road funnel fire from NF into valley WUI",
                "US-395 corridor south -- cheatgrass/sage fuels; Numbers Fire demonstrated rapid spread along highway",
                "Pine Nut Mountains east approach -- rangeland fires can race across valley floor from east",
                "Carson River riparian -- cottonwood corridor can carry low-intensity fire through valley",
                "Kingsbury Grade corridor -- fire on this slope cuts Lake Tahoe access and threatens upper-elevation homes",
            ],
            "rate_of_spread_potential": (
                "Extreme in rangeland fuels: Numbers Fire burned 18,380 acres in one week along US-395 "
                "corridor. Cheatgrass fuels support 3-6 mph head fire spread rates. Sierra escarpment "
                "fires can produce rapid downhill runs during wind events -- Tamarack Fire moved 21,000 "
                "acres in a single day. Valley floor grass/sage fires spread fast with minimal terrain "
                "resistance."
            ),
            "spotting_distance": (
                "0.5-1 mile in rangeland winds; longer during Sierra escarpment crown fire events. "
                "Pinyon-juniper torching on Pine Nut Mountain slopes produces intense spotting. "
                "Ember transport across US-395 into subdivisions is the primary structure ignition "
                "mechanism during highway-corridor fires."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Gardnerville-Ranchos General Improvement District and Minden-Gardnerville Sanitation "
                "District serve the communities. Water from wells and Carson River system. Fire flow "
                "generally adequate in town centers but rural properties on valley margins and foothills "
                "often rely on private wells with no fire hydrant access. Post-fire watershed impacts "
                "(erosion, sedimentation) from Sierra fires can compromise water quality."
            ),
            "power": (
                "NV Energy serves the area; transmission lines from California cross Sierra passes "
                "and are vulnerable to fire damage. Overhead distribution throughout valley. Extended "
                "outages possible during major Sierra fire events. Agricultural operations (dairy, "
                "alfalfa) require power for irrigation and livestock."
            ),
            "communications": (
                "Good cell coverage in valley floor; degraded in Pine Nut Mountains and Sierra "
                "foothills. Douglas County Emergency Management coordinates alerts. Record-Courier "
                "newspaper and local radio provide community information. Douglas County Sheriff's "
                "office handles evacuation coordination."
            ),
            "medical": (
                "Carson Valley Medical Center in Gardnerville (~30 beds) provides emergency care. "
                "Limited surge capacity. Level II trauma at Renown Regional in Reno (~50 miles). "
                "Served as staging area for Tamarack Fire evacuees from Alpine County. Smoke events "
                "from Sierra fires create prolonged respiratory health impacts for valley residents."
            ),
        },
        "demographics_risk_factors": {
            "population": 9611,
            "seasonal_variation": (
                "Carson Valley tourism is growing, with agritourism, winery visits, and outdoor "
                "recreation. Seasonal ranch workers during agricultural season. Lake Tahoe overflow "
                "lodging brings visitors unfamiliar with local fire risk. Hot air balloon events "
                "and fall harvest festivals draw crowds. Tamarack Fire evacuees from Alpine County "
                "were relocated to Douglas County facilities."
            ),
            "elderly_percentage": "~22% over 65; significant retiree population attracted to valley climate; many on fixed incomes",
            "mobile_homes": (
                "Scattered mobile home parks in Gardnerville Ranchos and along US-395 south corridor. "
                "Manufactured homes in Pine View Estates (evacuated during Numbers Fire). Higher "
                "concentration of lower-income and elderly mobile home residents in rural areas."
            ),
            "special_needs_facilities": (
                "Douglas County Senior Center (used as Tamarack Fire evacuation center). Douglas "
                "County schools. Carson Valley Medical Center. Douglas County Fairgrounds (livestock "
                "evacuation staging). Several assisted living facilities in Gardnerville area. "
                "Washoe Tribe of Nevada and California facilities in Dresslerville."
            ),
        },
    },

    # =========================================================================
    # 7. GENOA, NV -- Nevada's Oldest Settlement / Sierra Base WUI
    # =========================================================================
    "genoa_nv": {
        "center": [39.0024, -119.8492],
        "terrain_notes": (
            "Genoa (pop ~300; unincorporated CDP in Douglas County) is Nevada's oldest permanent "
            "settlement, founded in 1851 as Mormon Station -- a trading post on the Overland "
            "Emigrant Trail. The town sits at approximately 4,806 ft elevation at the base of the "
            "Sierra Nevada escarpment, 7 miles northwest of Minden. The Sierra Carson Range rises "
            "steeply to the west, with Genoa Peak (9,005 ft) looming 4,200 ft above the town "
            "within approximately 3 miles horizontal distance. This produces some of the steepest "
            "and most dramatic WUI terrain in Nevada: dense mixed-conifer forest on 30-50%+ slopes "
            "transitioning abruptly to the tiny historic town at the base. The town's setting in a "
            "narrow bench between the Sierra wall and the Carson Valley floor means fire from the "
            "mountains can reach the town rapidly with almost no buffer. Genoa Canyon and adjacent "
            "drainages cut into the Sierra above the town, creating chimney-effect corridors. David "
            "Walley's Hot Springs Resort (1862) sits 1 mile south of town at the canyon mouth. "
            "A 2022 wildfire behind Genoa Cemetery (2-3 acres) forced resident evacuations, "
            "demonstrating that even tiny fires at the WUI interface threaten this settlement. "
            "Historic structures from the 1850s-1860s (wooden frame construction, some adobe) are "
            "irreplaceable cultural heritage. The Genoa Candy Dance (annual since 1919) draws "
            "thousands to the tiny town. Jacks Valley Road connects Genoa to US-395."
        ),
        "key_features": [
            {"name": "Genoa Peak", "bearing": "W", "type": "mountain",
             "notes": "9,005 ft; rises 4,200 ft above town in ~3 miles; dense forest on steep east-facing slopes; fire here would descend directly into town"},
            {"name": "Sierra Nevada Escarpment", "bearing": "W", "type": "terrain",
             "notes": "Near-vertical rise of 4,000+ ft from valley floor to Sierra crest; the most dramatic WUI transition in western Nevada; continuous fuel from ridgeline to town"},
            {"name": "Genoa Canyon", "bearing": "W/NW", "type": "canyon",
             "notes": "Primary drainage above town; chimney-effect fire corridor; trail access into Humboldt-Toiyabe NF; recreational use creates ignition risk"},
            {"name": "David Walley's Hot Springs", "bearing": "S", "type": "resort/infrastructure",
             "notes": "Historic resort (est. 1862) at canyon mouth south of town; has burned and been rebuilt multiple times; resort guests add to evacuation population"},
            {"name": "Genoa Cemetery", "bearing": "E", "type": "landmark",
             "notes": "2022 wildfire forced evacuations in this area; brush/grass transition between town and open valley; fire indicator for town exposure"},
            {"name": "Mormon Station State Historic Park", "bearing": "center", "type": "historic",
             "notes": "Replica of 1851 trading post; surrounded by mature trees; town's historic core includes irreplaceable 1850s-1860s wooden structures"},
        ],
        "elevation_range_ft": [4750, 5000],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Genoa Cemetery Fire", "year": 2022, "acres": 3,
             "details": (
                 "Small wildfire behind Genoa Cemetery forced evacuations of Trail and Holden Court "
                 "residents. Though only 2-3 acres, it demonstrated the hair-trigger WUI exposure "
                 "at the Sierra base. Quick response prevented spread into the historic town."
             )},
            {"name": "Tamarack Fire (regional impact)", "year": 2021, "acres": 68637,
             "details": (
                 "While the Tamarack Fire burned primarily to the south, Genoa experienced hazardous "
                 "smoke and ash for weeks. The fire's pattern -- crossing the Sierra crest from "
                 "California into Nevada -- represents the exact scenario that would threaten Genoa: "
                 "a fire descending the escarpment from the west."
             )},
            {"name": "Sierra escarpment fires (historical)", "year": 1900, "acres": 0,
             "details": (
                 "The Sierra slopes above Genoa have a long fire history predating modern records. "
                 "Early settlers noted frequent fires in the canyons. Fire suppression since the "
                 "early 1900s has allowed fuel accumulation far exceeding historical norms on the "
                 "steep slopes directly above the town."
             )},
        ],
        "evacuation_routes": [
            {"route": "Jacks Valley Road East (to US-395 / Minden)", "direction": "E/SE", "lanes": 2,
             "bottleneck": "2-lane rural road; single access from town to valley floor; 3-4 miles to US-395",
             "risk": "Only paved route out; fire between town and US-395 would trap residents; brush/grass along road"},
            {"route": "Genoa Lane / Foothill Road (local roads)", "direction": "N/S", "lanes": 2,
             "bottleneck": "Narrow rural lanes along base of Sierra; dead-end segments; limited capacity",
             "risk": "Runs along the WUI interface; fire on Sierra slopes would close these roads; not viable for mass evacuation"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Powerful downslope winds from the Sierra crest are the critical fire weather driver. "
                "Genoa sits at the base of one of the steepest Sierra escarpments in Nevada -- winds "
                "accelerating down the 4,000+ ft slope can exceed 60-80 mph during foehn events. "
                "Canyon drainages above the town focus and amplify these winds. Afternoon thermal "
                "upslope winds push fire up-canyon during the day; evening downslope drainage reversal "
                "can drive fire toward the valley floor and town."
            ),
            "critical_corridors": [
                "Genoa Canyon -- primary chimney corridor from Sierra forest directly into town",
                "Sierra escarpment face -- continuous fuel from 9,000 ft ridgeline to 4,800 ft town; near-vertical fire run",
                "Walley's Hot Springs drainage -- southern approach from canyon mouth toward resort and town",
                "Jacks Valley Road corridor -- only escape route; brush on both sides; fire can cut evacuation",
            ],
            "rate_of_spread_potential": (
                "Extreme on the Sierra escarpment: 30-50%+ slopes with dense conifer fuel produce "
                "the most intense fire behavior possible in this region. A fire on Genoa Peak could "
                "reach the town boundary in under 30 minutes during downslope wind events. The "
                "vertical relief (4,200 ft in 3 miles) creates natural upslope draft that accelerates "
                "fire spread independent of ambient wind. Crown fire transitions are inevitable in "
                "the dense, overstocked forest above the town."
            ),
            "spotting_distance": (
                "1-3 miles possible from Sierra escarpment crown fire. Ember showers from 9,000 ft "
                "elevation would rain down on the town at 4,800 ft with wind-assisted trajectory. "
                "Wooden historic structures with no defensible space are extremely receptive to "
                "ember ignition. Structure-to-structure fire spread in the historic core would be "
                "rapid in wind conditions."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Small community water system; limited fire flow capacity. No municipal hydrant "
                "system comparable to larger cities. Fire suppression would depend heavily on "
                "tanker shuttle operations. Water supply is a critical limiting factor for "
                "structure defense in Genoa."
            ),
            "power": (
                "NV Energy overhead distribution; extremely vulnerable to fire and tree fall on "
                "the forested Sierra slopes above town. Power outage likely in any significant "
                "fire event. No backup generation for the community."
            ),
            "communications": (
                "Limited cell coverage; shadow zone at base of Sierra escarpment. Douglas County "
                "emergency alerts via CodeRED. Small community relies on word-of-mouth and "
                "neighbor-to-neighbor communication. No local emergency services -- dependent "
                "on Douglas County Fire and East Fork Fire Protection District response."
            ),
            "medical": (
                "No medical facilities in Genoa. Nearest hospital: Carson Valley Medical Center "
                "in Gardnerville (~7 miles). EMS response from East Fork Fire Protection District. "
                "Elderly and mobility-limited population; no shelter-in-place capability for "
                "wildfire. Evacuation of David Walley's Resort guests adds to medical/transport burden."
            ),
        },
        "demographics_risk_factors": {
            "population": 300,
            "seasonal_variation": (
                "Genoa Candy Dance (September) draws 10,000-15,000 visitors to a town of 300 -- "
                "a 30x-50x population surge during peak fire season. David Walley's Hot Springs "
                "Resort brings year-round visitors. Historic tourism (Mormon Station, Genoa "
                "Courthouse Museum) adds seasonal foot traffic. Peak crowds far exceed evacuation "
                "capacity of 2-lane Jacks Valley Road."
            ),
            "elderly_percentage": "~30% over 65; small, aging resident population; many long-term residents",
            "mobile_homes": (
                "Few if any mobile homes; mostly historic single-family homes and ranch properties. "
                "Older wooden construction is comparably vulnerable to fire. Some ranch outbuildings "
                "and structures along Jacks Valley Road."
            ),
            "special_needs_facilities": (
                "Genoa Elementary School (one of Nevada's oldest schools). Mormon Station State "
                "Historic Park. David Walley's Resort guests. No institutional facilities. "
                "Extremely small population but many elderly and mobility-limited residents."
            ),
        },
    },

    # =========================================================================
    # 8. ELKO, NV -- Great Basin Rangeland Fire Corridor
    # =========================================================================
    "elko_nv": {
        "center": [40.8324, -115.7631],
        "terrain_notes": (
            "Elko (pop ~20,600; metro ~55,000 including Spring Creek) sits at approximately 5,060 ft "
            "elevation in the high desert of the Great Basin, at the western foot of the Ruby Mountains "
            "along the Humboldt River corridor. Unlike the Sierra Nevada communities in western Nevada, "
            "Elko's fire regime is dominated by rangeland fire in cheatgrass-invaded sagebrush steppe -- "
            "the fuel type that has produced the largest fires in Nevada history. The Martin Fire (2018) "
            "burned 435,000 acres north of Elko, the largest wildfire in Nevada's recorded history. "
            "The Adobe Range flanks the city to the west and north, with peaks reaching 8,134 ft. The "
            "Ruby Mountains rise to 11,387 ft (Ruby Dome) approximately 25 miles southeast, mostly "
            "within the Humboldt-Toiyabe National Forest. The Humboldt River flows through the city "
            "east-to-west before continuing toward the Humboldt Sink. Interstate 80 is the sole major "
            "east-west transportation corridor through northeastern Nevada. Spring Creek, a bedroom "
            "community of ~13,800 residents 6 miles south of Elko, pushes WUI development into "
            "sagebrush rangeland at the base of the Ruby Mountain foothills. Elko County has "
            "experienced catastrophic rangeland fire: approximately 1 million acres burned in 2006 "
            "alone. The Jakes Fire (2025) burned 82,217 acres from lightning in eastern Elko County. "
            "Cheatgrass has transformed the fire regime from 30-110 year return intervals to 3-10 "
            "years, preventing sagebrush recovery and creating a permanent grass-fire cycle. The BLM "
            "Elko Field Office, USFS, and Nevada Division of Forestry have constructed fuelbreaks and "
            "greenstrips around numerous WUI communities throughout Elko County."
        ),
        "key_features": [
            {"name": "Ruby Mountains", "bearing": "SE", "type": "mountain_range",
             "notes": "11,387 ft (Ruby Dome); 'Alps of Nevada'; Humboldt-Toiyabe NF; Lamoille Canyon; mixed conifer at elevation; sagebrush interface with rangeland below"},
            {"name": "Adobe Range", "bearing": "W/NW", "type": "mountain_range",
             "notes": "8,134 ft; flanks west side of Elko; sagebrush/pinyon; fires from this range threaten western neighborhoods; I-80 passes through gap"},
            {"name": "Humboldt River", "bearing": "E-W through city", "type": "river",
             "notes": "Major Great Basin river; cottonwood riparian corridor; limited firebreak; flows through downtown Elko; I-80 parallels the river"},
            {"name": "Spring Creek", "bearing": "S", "type": "community",
             "notes": "Bedroom community of 13,805; sagebrush/grass WUI interface; BLM fuelbreaks constructed; residential development expanding into rangeland"},
            {"name": "Lamoille Valley", "bearing": "SE", "type": "valley/community",
             "notes": "Small rural community at base of Lamoille Canyon (Ruby Mountains); surrounded by sagebrush rangeland; limited access roads"},
            {"name": "South Fork Reservoir", "bearing": "S", "type": "water/recreation",
             "notes": "State recreation area south of Spring Creek; sagebrush-surrounded; popular camping with ignition risk; fire in this area would approach Spring Creek"},
        ],
        "elevation_range_ft": [5060, 5400],
        "wui_exposure": "moderate",
        "historical_fires": [
            {"name": "Martin Fire", "year": 2018, "acres": 435000,
             "details": (
                 "Largest wildfire in Nevada history. Burned 435,000 acres of sagebrush steppe "
                 "north of Elko in the Owyhee Desert toward the Idaho border. Destroyed some of the "
                 "West's finest intact sagebrush habitat. Devastated ranches and sage-grouse habitat. "
                 "Demonstrated the catastrophic scale possible in Great Basin rangeland fire. "
                 "Fire spread was driven by continuous cheatgrass fuels and wind."
             )},
            {"name": "Jakes Fire", "year": 2025, "acres": 82217,
             "details": (
                 "Lightning-caused fire ignited August 1, 2025, in eastern Elko County. Burned "
                 "82,217 acres of rangeland. Continued the pattern of mega-fires in Great Basin "
                 "sagebrush country driven by cheatgrass fuel continuity."
             )},
            {"name": "Elko County 2006 fire season", "year": 2006, "acres": 1000000,
             "details": (
                 "Approximately 1 million acres burned across Elko County in 2006 -- one of the most "
                 "destructive rangeland fire seasons in the county's history. Multiple large fires "
                 "burned simultaneously in sagebrush steppe. Devastated ranching operations and "
                 "permanently converted sagebrush habitat to annual grassland."
             )},
            {"name": "South Fork Fire", "year": 2018, "acres": 25000,
             "details": (
                 "Burned south of Spring Creek in sagebrush rangeland near South Fork Reservoir. "
                 "Threatened Spring Creek residential areas. Prompted fuelbreak construction around "
                 "the community. Demonstrated direct WUI threat to Elko's largest suburb."
             )},
        ],
        "evacuation_routes": [
            {"route": "I-80 West (toward Winnemucca / Battle Mountain)", "direction": "W", "lanes": 4,
             "bottleneck": "Long distances between towns (73 miles to Winnemucca); rangeland fire can close highway",
             "risk": "Smoke from rangeland fires reduces visibility to near-zero on I-80; multiple fire closures documented"},
            {"route": "I-80 East (toward Wells / West Wendover)", "direction": "E", "lanes": 4,
             "bottleneck": "Long distances (62 miles to Wells); remote desert terrain",
             "risk": "Same rangeland fire risk; limited services along route; extreme temperatures in summer"},
            {"route": "SR-225 North (toward Owyhee / Mountain City)", "direction": "N", "lanes": 2,
             "bottleneck": "Remote 2-lane highway; 80+ miles to Idaho border; minimal services",
             "risk": "Martin Fire burned along this corridor in 2018; leads into even more fire-prone rangeland"},
            {"route": "SR-228 / Lamoille Highway South", "direction": "S", "lanes": 2,
             "bottleneck": "2-lane road to Lamoille and Spring Creek; limited capacity; single access",
             "risk": "Sagebrush on both sides of road; fire can cut Spring Creek access from Elko"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Great Basin wind patterns feature strong afternoon westerlies (15-30 mph) driven by "
                "pressure gradients between the Sierra and the interior. Thunderstorm outflow winds "
                "from dry lightning events produce chaotic, gusty winds that ignite and spread multiple "
                "fires simultaneously. Cold front passages in late summer and early fall generate "
                "sustained 30-50 mph winds that drive massive rangeland fire runs across hundreds of "
                "thousands of acres. Diurnal mountain-valley circulation creates local wind patterns "
                "around the Ruby Mountains and Adobe Range."
            ),
            "critical_corridors": [
                "Humboldt River valley -- I-80 corridor; smoke/fire closures affect transcontinental traffic and commerce",
                "Spring Creek south -- sagebrush rangeland fire approach from South Fork / Pine Valley area",
                "Adobe Range west -- fires from western rangeland driven by prevailing westerlies toward Elko",
                "North Elko / SR-225 -- Martin Fire corridor; vast cheatgrass-dominated terrain with no natural firebreaks",
                "Lamoille Valley -- narrow approach road through sagebrush; community can be isolated by rangeland fire",
            ],
            "rate_of_spread_potential": (
                "Extreme in cheatgrass-dominated rangeland. Head fire spread rates of 4-8 mph are "
                "common in wind-driven sagebrush/cheatgrass fires. The Martin Fire covered 435,000 "
                "acres -- an area roughly 25x20 miles -- demonstrating fire runs of 10+ miles in "
                "single burning periods. Continuous fine fuels (cheatgrass matures and cures by "
                "mid-June) provide virtually uninterrupted fire spread across the landscape. "
                "Sagebrush adds crown fire intensity above the grass understory."
            ),
            "spotting_distance": (
                "0.25-1 mile typical in grass/sage; sagebrush torch events produce intense but "
                "short-lived spotting. The primary threat is not long-range spotting but the "
                "continuous, fast-moving fire front that can overtake structures and vehicles. "
                "I-80 vehicles have been trapped by rapidly advancing rangeland fire fronts."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Elko municipal water from wells and Humboldt River system. Adequate for city proper "
                "but Spring Creek on separate system with limited fire flow in outer subdivisions. "
                "Rural ranches on private wells have no fire hydrant access. Post-fire erosion from "
                "rangeland burns can contaminate surface water sources."
            ),
            "power": (
                "NV Energy / Idaho Power serve different portions of the region. Long-distance "
                "transmission lines cross vast expanses of fire-prone rangeland -- extremely "
                "vulnerable to fire damage. Power restoration after rangeland fires can take "
                "days due to remote locations and damage to multiple poles/spans simultaneously. "
                "Mining operations (Elko County is major gold mining region) have industrial backup power."
            ),
            "communications": (
                "Cell coverage adequate in Elko and Spring Creek; rapidly degrades in surrounding "
                "rangeland. Vast distances between cell towers mean fires can create large communication "
                "dead zones. Elko County Emergency Management coordinates with BLM dispatch center. "
                "Mining industry radio networks provide backup communication in some areas."
            ),
            "medical": (
                "Northeastern Nevada Regional Hospital (~75 beds) provides Level IV trauma care. "
                "Elko is a regional medical hub for northeastern NV -- nearest comparable facility "
                "is in Twin Falls, Idaho (115 miles) or Salt Lake City (230 miles). Smoke events "
                "from rangeland fires affect air quality for weeks. Medical capacity adequate for "
                "normal operations but surge events would require air transport."
            ),
        },
        "demographics_risk_factors": {
            "population": 20564,
            "seasonal_variation": (
                "National Cowboy Poetry Gathering (January) brings ~10,000 visitors. Summer brings "
                "recreation tourists to Ruby Mountains, Lamoille Canyon, and South Fork Reservoir. "
                "Mining workforce fluctuates with gold prices -- Elko County is one of the world's "
                "top gold-producing regions. I-80 transient traffic adds population that may be "
                "unfamiliar with rangeland fire behavior (many travelers are from coastal states and "
                "do not understand how fast grass fires move)."
            ),
            "elderly_percentage": "~12% over 65 (younger demographic due to mining/ranching workforce)",
            "mobile_homes": (
                "Significant manufactured housing in Elko and Spring Creek -- mobile home parks "
                "along Idaho Street corridor and in Spring Creek outer areas. Mining workforce "
                "housing includes temporary and manufactured structures. These represent the "
                "highest-vulnerability housing for ember exposure and direct fire contact."
            ),
            "special_needs_facilities": (
                "Great Basin College campus. Elko County School District schools. Northeastern Nevada "
                "Regional Hospital. Elko County jail. Western Folklife Center. Multiple mining camp "
                "accommodations in surrounding county. Spring Creek residential area includes "
                "several assisted living facilities."
            ),
        },
    },

}
