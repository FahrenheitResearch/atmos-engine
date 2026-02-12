"""
Enhanced Fire-Vulnerable City Profiles: Sierra Foothills & San Diego Backcountry
=================================================================================

Deep-research terrain profiles for 5 small mountain/foothill communities that
represent some of California's most dangerous wildfire evacuation scenarios.
These are communities where limited road access, steep terrain, and heavy
fuel loading create potential mass-casualty events during wind-driven fires.

Cities covered (5):
    Sierra Foothills:
        Grass Valley (Nevada County, pop ~14,000)
        Nevada City (Nevada County, pop ~3,150)

    San Diego Backcountry:
        Julian (San Diego County, pop ~1,500-1,800)
        Ramona (San Diego County, pop ~21,500)

    San Gabriel Mountains:
        Wrightwood (San Bernardino County, pop ~4,700)

Research sources:
    - Cedar Fire (2003): CAL FIRE incident report; San Diego Union-Tribune
      Firestorm 2003 investigation; NWS Southern CA Service Assessment;
      Colorado Firecamp CDF sequence of events
    - Witch Creek Fire (2007): CAL FIRE; City of San Diego post-incident;
      San Diego Union-Tribune "Searing Lessons" retrospective (2017)
    - 49er Fire (1988): Nevada County historical records; The Union archives;
      YubaNet 25th anniversary retrospective; Washington Post (Sep 15, 1988)
    - Jones Fire (2020): CAL FIRE; ABC10; The Union; YubaNet
    - Bridge Fire (2024): CAL FIRE incident updates; Victor Valley News;
      San Gabriel Valley Tribune; San Bernardino County Fire
    - Blue Cut Fire (2016): CAL FIRE; NBC Los Angeles; LAist
    - Caltrans SR-49 Grass Valley Wildfire Evacuation Project (2025)
    - Nevada County CWPP (2025): Nevada County Board of Supervisors
    - Julian CWPP (2023): San Diego County Fire Safe Council
    - SDG&E fire-hardening program: SDG&E NewsCenter
    - USGS Wrightwood paleoseismic site: Weldon et al. (2004);
      Scharer et al. (2007)
    - Nevada City Downtown Historic District: National Register #85002520
    - Wrightwood Fire Safe Council: Bridge Fire after-action
    - PG&E PSPS program: Nevada County OES advisories
    - Caltrans District 3: SR-49 Wildfire Evacuation Route Project (2025)
    - SANDAG: SR-67 Ramona widening study
"""

# =============================================================================
# ENHANCED TERRAIN PROFILES
# =============================================================================

ENHANCED_TERRAIN_PROFILES = {

    # =========================================================================
    # SIERRA FOOTHILLS — Nevada County
    # =========================================================================

    "grass_valley_ca": {
        "center": (39.2193, -121.0610),
        "elevation_ft": 2411,
        "terrain_notes": (
            "Sierra foothills city (pop 14,016, 2020 census) in Nevada County "
            "at 2,411 ft elevation. Widely considered one of the most vulnerable "
            "communities in California — same topographic profile as Paradise "
            "(ridge-top settlement above deep canyons with limited escape routes). "
            "63% of incorporated area classified as WUI. Dense mixed pine/oak "
            "forest with decades of fire-suppression-driven fuel accumulation: "
            "heavy ladder fuels, dense understory, continuous canopy throughout "
            "residential areas. Underlying geology is granitic (quartz diorite "
            "under downtown core) with metavolcanic rock and diabase on margins; "
            "ultramafic soils near Nevada County Golf Course support sparser "
            "vegetation but surrounding areas are heavily forested. "
            "\n\n"
            "The city is bracketed by three major canyon systems: South Yuba "
            "River Canyon (north, 5 mi), Bear River drainage (south, 3 mi), "
            "and Wolf Creek (east, running directly through WUI). Any fire "
            "entering these canyons gains rapid upslope momentum toward "
            "populated ridges. The 49er Fire (1988) proved this conclusively: "
            "ignited by a man burning toilet paper near Hwy 49, it destroyed "
            "312 structures (144 homes, 219 outbuildings, 89 vehicles, 17 "
            "boats/trailers) across 33,700 acres in 5 days, driven by severe "
            "drought and strong dry winds. Estimated damage: $22.7 million "
            "(1988 dollars). Fire impinged on Lake Wildwood, Rough and Ready, "
            "and Smartsville. Jones Fire (2020) burned 712 acres in South "
            "Yuba River Canyon after lightning ignition, forcing evacuation "
            "of 4,000 residents with 11,600 more under warnings. Highway 49 "
            "was closed between Newtown and Tyler Foote during the incident. "
            "\n\n"
            "Caltrans has recognized the evacuation crisis: the $107.4 million "
            "SR-49 Grass Valley Wildfire Evacuation Route Project (SB 1 funds "
            "plus Nevada County Transportation Commission) will widen shoulders "
            "and add a center two-way left-turn lane from Wolf Road/Combie Road "
            "to Ponderosa Pines Way. Construction anticipated fall 2027 through "
            "end of 2030 — meaning the community remains highly vulnerable for "
            "at least several more fire seasons."
        ),
        "population": {
            "total_2020_census": 14016,
            "density_per_sq_mi": 2670,
            "median_age": None,
            "note": (
                "Population has grown significantly in recent decades. "
                "42.6% single-person households; 25.5% single-person "
                "aged 65+, creating evacuation vulnerability for elderly "
                "living alone."
            ),
        },
        "danger_quadrants": ["north", "northeast", "east", "southeast"],
        "safe_quadrants": ["west"],
        "key_features": [
            {
                "name": "South Yuba River Canyon",
                "bearing": "N/NE",
                "distance_mi": 5,
                "type": "major_canyon",
                "notes": (
                    "Deep, heavily forested canyon — the primary fire corridor "
                    "threatening Grass Valley and Nevada City from the north. "
                    "Jones Fire (2020) burned 712 acres here, ignited by "
                    "lightning. Heavy recreational use (swimming holes, hiking, "
                    "camping) creates ignition risk in summer. Sierra Nevada "
                    "Conservancy prescribed burn projects ongoing to reduce "
                    "fuel loads in the canyon. Steep slopes with dense "
                    "understory channel fire uphill toward populated ridges."
                ),
            },
            {
                "name": "Bear River drainage",
                "bearing": "S",
                "distance_mi": 3,
                "type": "river_valley",
                "notes": (
                    "Canyon terrain to south of city. Combined with South "
                    "Yuba Canyon to the north, Grass Valley sits on a ridge "
                    "between two major drainages — the same topographic "
                    "configuration that made Paradise so vulnerable. Fire "
                    "approaching from either canyon gains upslope acceleration."
                ),
            },
            {
                "name": "Wolf Creek",
                "bearing": "E",
                "distance_mi": 2,
                "type": "canyon",
                "notes": (
                    "Local canyon running directly through the WUI. The SR-49 "
                    "evacuation improvement project begins at the Wolf Road/"
                    "Combie Road intersection specifically because fire entering "
                    "Wolf Creek could cut off eastbound evacuation. Dense "
                    "residential development along canyon margins."
                ),
            },
            {
                "name": "SR-49 corridor",
                "bearing": "N-S",
                "type": "access_route",
                "notes": (
                    "Primary evacuation route — narrow, winding 2-lane highway "
                    "through Gold Country. Closed during Jones Fire 2020. "
                    "Caltrans $107.4M widening project (2027-2030) will add "
                    "shoulders and center turn lane from Wolf/Combie to Ponderosa "
                    "Pines Way. Until then, severe bottleneck during mass "
                    "evacuation. Connects to Nevada City (4 mi north) creating "
                    "combined evacuation demand of ~17,000+ people on same roads."
                ),
            },
            {
                "name": "SR-20 corridor",
                "bearing": "E-W",
                "type": "access_route",
                "notes": (
                    "East-west escape route, also narrow 2-lane mountain road. "
                    "Provides alternate evacuation toward I-80 (east) or Penn "
                    "Valley/Marysville (west). Limited capacity. During mass "
                    "evacuation both SR-49 and SR-20 would carry combined "
                    "traffic from Grass Valley and Nevada City."
                ),
            },
        ],
        "evacuation": {
            "primary_routes": ["SR-49 south to Auburn/I-80", "SR-20 west to Penn Valley"],
            "secondary_routes": ["SR-49 north toward Downieville", "SR-20 east to I-80 via Emigrant Gap"],
            "bottlenecks": [
                "SR-49/SR-20 intersection in town",
                "Wolf Road/Combie Road intersection",
                "Narrow shoulders prevent pullover for emergency vehicles",
            ],
            "capacity_notes": (
                "Combined Grass Valley + Nevada City evacuation demand: ~17,000+ "
                "people on 2-lane roads. During Jones Fire 2020, 4,000 evacuated "
                "with 11,600 under warning. Evacuation centers established at "
                "Magnolia School (22431 Kingston Lane), Cottage Hill Elementary, "
                "Ready Springs School (Penn Valley), Nevada County Fairgrounds "
                "(animals). Full-community evacuation would overwhelm road "
                "capacity within minutes."
            ),
            "caltrans_project": (
                "SR-49 Grass Valley Wildfire Evacuation Route Project: $107.4M "
                "(SB 1 + NCTC funds). Widen shoulders, add center TWLTL from "
                "Wolf/Combie to Ponderosa Pines Way. Construction: fall 2027 "
                "to end 2030. Draft environmental document published Jan 2026."
            ),
        },
        "infrastructure": {
            "utility": "PG&E",
            "psps_exposure": "EXTREME",
            "psps_notes": (
                "Nevada County is one of the most PSPS-impacted counties in "
                "California. A single event can affect 43,000+ PG&E customers "
                "countywide. PSPS criteria: RH below 20%, sustained winds >25 "
                "mph, gusts >45 mph, Red Flag Warning, dry fuels. Shutoffs "
                "create secondary hazards: residents use generators (fire risk) "
                "and warming fires. In one 2019 event a generator caused a "
                "brush fire during a PSPS shutoff. Access and Functional Needs "
                "populations lose medication refrigeration, life-sustaining "
                "device charging, dialysis access. Community Resource Centers "
                "activated at 400 Idaho Maryland Rd for charging, ice, WiFi."
            ),
            "water_system": "NID (Nevada Irrigation District) municipal supply",
            "cell_coverage": (
                "87.6% land area covered by wireless service but canyon terrain "
                "creates dead zones. Poor cellular coverage documented as "
                "dangerous for emergency alerts — residents in canyons may "
                "miss evacuation orders. Nevada County OES identified "
                "communication gaps as critical vulnerability."
            ),
        },
        "community_preparedness": {
            "cwpp": (
                "2025 Nevada County CWPP adopted by Board of Supervisors Feb "
                "2025 after 2+ years of planning. Includes City of Grass "
                "Valley annex with place-based solutions for fuels reduction."
            ),
            "firewise": (
                "Fire Safe Council of Nevada County coordinates 107 Firewise "
                "USA communities countywide (as of Jan 2025). Western Nevada "
                "County Firewise coordinator covers Grass Valley, Nevada City, "
                "Penn Valley, South County, North San Juan, Hwy 174 corridor."
            ),
            "fuel_reduction": (
                "CAL FIRE planning 1,802-acre fire break in SW Nevada County "
                "in terrain that hasn't burned in a century, protecting both "
                "Grass Valley and Nevada City. Prescribed burn programs in "
                "South Yuba Canyon ongoing through Sierra Nevada Conservancy."
            ),
        },
        "historical_fires": [
            "49er Fire 1988 (312 structures, 144 homes, 33,700 acres, $22.7M damage, "
            "caused by burning toilet paper near Hwy 49, driven by drought/wind)",
            "Jones Fire 2020 (712 acres, South Yuba Canyon, lightning ignition, "
            "4,000 evacuated, 11,600 warned, Hwy 49 closed, 4 homes destroyed)",
            "River Fire 2021 (2,619 acres, nearby Colfax area, Bear River corridor)",
        ],
        "wui_class": "extreme",
        "compound_hazards": [
            "PG&E infrastructure failure (same aging lines that caused Camp Fire)",
            "PSPS shutoffs create secondary ignition risk from generators",
            "Combined evacuation demand with Nevada City on shared roads",
            "Diablo wind events (same pattern that drives Butte County fires)",
            "Terrain trap: ridge between two deep canyons mirrors Paradise geometry",
        ],
    },

    "nevada_city_ca": {
        "center": (39.2615, -121.0164),
        "elevation_ft": 2525,
        "terrain_notes": (
            "Historic Gold Rush city (pop 3,152, 2020 census; median age 49.4) "
            "at 2,525 ft in Nevada County, 4 miles northeast of Grass Valley. "
            "Nevada City is arguably the most fire-vulnerable historic district "
            "in California: the downtown core is a National Register Historic "
            "District (16 acres, 70 contributing buildings, listed 1985) with "
            "dense wooden Gold Rush-era structures, narrow steep streets, and "
            "heavy urban tree canopy pressed directly against commercial and "
            "residential buildings. The city has been destroyed by fire "
            "repeatedly in its history: the first great fire leveled the town "
            "in March 1851, and the worst catastrophe struck July 19, 1856, "
            "destroying 400+ buildings including the new courthouse and all "
            "county records, killing 10 people. By 1859, the city had been "
            "rebuilt and releveled by fire four additional times. Fire companies "
            "were finally formed in 1860 and two firehouses built by 1861. "
            "\n\n"
            "The National Exchange Hotel on Broad Street — the oldest "
            "continuously-operated hotel in California — was built in three "
            "brick buildings and opened August 1856 immediately after the "
            "great fire. In less than a month after the 1856 fire, 65 new "
            "frame buildings were erected and a half-dozen brick ones begun. "
            "Many of these 1850s-era wooden structures remain standing today, "
            "creating a downtown that looks authentic but is catastrophically "
            "vulnerable to fire. "
            "\n\n"
            "Modern wildfire risk comes from the surrounding terrain: dense "
            "forest presses against the city on all sides. Deer Creek runs "
            "through/near town creating a local fire corridor. South Yuba "
            "River Canyon is 3 miles north. Steep hillsides, narrow "
            "residential streets, ancient wooden homes, and thick urban tree "
            "canopy make this a textbook WUI ignition scenario. The "
            "Washington Post (2018) described the community as 'living under "
            "a time bomb.' Nevada City ran a 'Goat Fund Me' campaign raising "
            "$25,000 to hire goat farmers to graze brush on 450+ acres of "
            "city-owned greenbelt — creative but indicative of the scale of "
            "the fuel problem."
        ),
        "population": {
            "total_2020_census": 3152,
            "median_age": 49.4,
            "note": (
                "Small population but very high tourist traffic. Broad Street "
                "draws visitors year-round. Combined with Grass Valley (14,016) "
                "total evacuation demand on shared road network is ~17,000+."
            ),
        },
        "danger_quadrants": ["north", "northeast", "east", "south"],
        "safe_quadrants": ["west", "southwest"],
        "key_features": [
            {
                "name": "South Yuba River Canyon",
                "bearing": "N",
                "distance_mi": 3,
                "type": "major_canyon",
                "notes": (
                    "Primary fire corridor from the north. Terrain hasn't burned "
                    "in a century in some areas (CAL FIRE 1,802-acre fire break "
                    "planned for SW Nevada County). Jones Fire 2020 burned 712 "
                    "acres in this canyon. Prescribed burns ongoing through "
                    "Sierra Nevada Conservancy. Deep canyon with heavy recreational "
                    "use — swimming holes, hiking trails — creating summer "
                    "ignition risk."
                ),
            },
            {
                "name": "Deer Creek drainage",
                "bearing": "S",
                "distance_mi": 1,
                "type": "canyon",
                "notes": (
                    "Runs through/near town, creating a local fire corridor "
                    "that could carry fire directly into the city. Riparian "
                    "vegetation along creek is surrounded by residential "
                    "development. Fire in Deer Creek drainage could reach "
                    "downtown within minutes given upslope terrain."
                ),
            },
            {
                "name": "Historic Downtown (Broad Street)",
                "bearing": "center",
                "type": "structure_vulnerability",
                "notes": (
                    "National Register Historic District: 16 acres, 70 "
                    "contributing buildings (NR #85002520, listed 1985). "
                    "Dense wooden buildings from 1850s-1880s, many with "
                    "roofed balconies, verandas, and shed canopies. The "
                    "National Exchange Hotel (1856), Firehouse No. 1, and "
                    "numerous wood-frame commercial buildings. Narrow streets "
                    "with continuous fuel connections between structures. "
                    "One ember shower on downtown could recreate the 1856 "
                    "conflagration."
                ),
            },
            {
                "name": "SR-49 / SR-20 corridors",
                "bearing": "multiple",
                "type": "access_route",
                "notes": (
                    "Both routes are narrow 2-lane mountain roads with limited "
                    "capacity. SR-49 runs through downtown on narrow historic "
                    "streets. During mass evacuation, Nevada City traffic merges "
                    "with Grass Valley traffic on same roads. Jones Fire 2020 "
                    "closed SR-49. No 4-lane evacuation route exists. Community "
                    "is functionally a dead-end if fire cuts SR-49 to the south "
                    "and SR-20 to the west simultaneously."
                ),
            },
        ],
        "evacuation": {
            "primary_routes": ["SR-49 south through Grass Valley to Auburn/I-80"],
            "secondary_routes": ["SR-20 west to Penn Valley", "SR-49 north (limited)"],
            "critical_vulnerability": (
                "Nevada City sits upstream of Grass Valley on the road network. "
                "During evacuation, Nevada City traffic must flow THROUGH or "
                "around Grass Valley to reach I-80. If Grass Valley is also "
                "evacuating simultaneously, the combined 17,000+ people on "
                "2-lane roads creates an extremely dangerous scenario similar "
                "to the Camp Fire gridlock on Skyway in Paradise."
            ),
        },
        "infrastructure": {
            "utility": "PG&E",
            "psps_exposure": "EXTREME",
            "psps_notes": (
                "Same PG&E PSPS impacts as Grass Valley. 43,000+ customers "
                "affected countywide during events. Aging PG&E infrastructure "
                "throughout forested terrain. City sent formal letter of "
                "concern to CPUC (jointly with Grass Valley and Nevada County) "
                "detailing PSPS impacts on the community."
            ),
            "cell_coverage": (
                "Canyon topography creates significant dead zones. The Union "
                "(local newspaper) reported that poor cellular coverage is "
                "'not just inconvenient, it's dangerous' — residents in rural "
                "areas may miss evacuation alerts or be unable to make 911 "
                "calls. Nevada County OES identified communication gaps as "
                "critical emergency management vulnerability."
            ),
        },
        "community_preparedness": {
            "cwpp": (
                "2025 Nevada County CWPP includes City of Nevada City annex. "
                "Nevada City CWPP also available on city website. Focus on "
                "hazardous fuel reduction and community preparedness."
            ),
            "firewise": (
                "Part of Fire Safe Council of Nevada County's 107-community "
                "Firewise USA network. Nevada City Wildfire Preparedness "
                "program through city government."
            ),
            "creative_programs": (
                "Goat Fund Me campaign raised $25,000 to hire goat farmers "
                "to graze brush on 450+ acres of city-owned greenbelt. "
                "Creative approach but illustrates the massive scale of the "
                "fuel management challenge."
            ),
        },
        "historical_fires": [
            "1851 great fire (first major fire, leveled the town)",
            "1856 catastrophe (July 19 — 400+ buildings destroyed, courthouse + all "
            "county records lost, 10 killed; rebuilt within a month: 65 frame + 6 brick)",
            "1856-1859 (four additional fires leveled the city; fire companies formed 1860)",
            "49er Fire 1988 (33,700 acres, 312 structures, burned through western Nevada County, "
            "caused by burning toilet paper near Hwy 49)",
            "Jones Fire 2020 (712 acres, South Yuba Canyon, lightning ignition, "
            "SR-49 closed, 4,000 evacuated)",
        ],
        "wui_class": "extreme",
        "compound_hazards": [
            "Historic wooden downtown: one ember shower could destroy irreplaceable "
            "Gold Rush-era structures (National Register district, 70 buildings)",
            "Dead-end road geometry: must evacuate through Grass Valley",
            "PG&E infrastructure failure risk (same aging system as Camp Fire cause)",
            "Diablo wind events accelerate fires from east/northeast",
            "Terrain-channeled fire from Deer Creek or South Yuba Canyon",
            "Tourist traffic inflates road demand beyond resident population",
        ],
    },

    # =========================================================================
    # SAN DIEGO BACKCOUNTRY — Cedar Fire / Witch Creek Fire corridor
    # =========================================================================

    "julian_ca": {
        "center": (33.0787, -116.6020),
        "elevation_ft": 4235,
        "terrain_notes": (
            "Small mountain town (pop 1,768 at 2020 census; ~1,490 estimated "
            "2023; median age 55.6) in San Diego backcountry at 4,235 ft in "
            "the Cuyamaca/Volcan Mountains within the Peninsular Ranges. Julian "
            "is a Gold Rush-era town (gold discovered 1869) now famous for "
            "apple orchards and tourism — during October apple season, the town "
            "bakes 10,000 apple pies per week and thousands of Southern "
            "California tourists flood the narrow mountain roads, potentially "
            "tripling or quadrupling the effective population on any given "
            "fall weekend. This creates a catastrophic evacuation scenario: "
            "1,500 residents plus thousands of tourists on 2-lane mountain "
            "highways during peak Santa Ana fire season. "
            "\n\n"
            "The town is surrounded by Cleveland National Forest with heavy "
            "chaparral and mixed-conifer fuels across diverse ecosystems from "
            "4,000 to 6,500 ft elevation (oak woodlands, conifer forests, "
            "meadows). Cedar Fire (2003) — the worst wildfire disaster in "
            "San Diego County history — burned 273,246 acres, destroyed 2,820 "
            "structures, killed 15 people (including 1 firefighter in Julian "
            "on Orchard Lane overrun by a flaming front on Oct 29), and moved "
            "at 3,600 acres/hour at peak, reaching 6,000 acres/hour during "
            "the most extreme conditions. The fire spread 2 acres per second "
            "and traveled 30+ miles southwest in under 10 hours, reaching "
            "Lakeside at 15 mph. On October 28, firefighters fired out along "
            "Hwy 78/79 from Pine Hills Road to Santa Ysabel (~7 miles) to "
            "keep the fire south of the highway. Julian itself narrowly "
            "survived. Witch Creek Fire (2007) forced full evacuation of "
            "Julian; the fire started in the Santa Ysabel area NW of town "
            "and burned 197,990 acres. "
            "\n\n"
            "Banner Grade (SR-78 east of Julian descending into the desert "
            "toward Shelter Valley and Earthquake Valley) is a critical "
            "terrain feature: extremely steep, winding descent with no "
            "shoulder, dropping from 4,200 ft to below 2,000 ft in just a "
            "few miles. This route provides the only eastbound escape but is "
            "also a potential fire corridor where desert winds funnel upslope."
        ),
        "population": {
            "total_2020_census": 1768,
            "estimated_2023": 1490,
            "median_age": 55.6,
            "tourist_peak": (
                "October apple season: 10,000 pies/week baked. Thousands of "
                "tourists from San Diego and LA flood SR-78/SR-79 on weekends. "
                "Effective daytime population may reach 5,000-8,000+ during "
                "peak apple festival weekends — during peak Santa Ana season."
            ),
        },
        "danger_quadrants": ["east", "southeast", "south", "northwest"],
        "safe_quadrants": [],
        "key_features": [
            {
                "name": "Cuyamaca Mountains",
                "bearing": "S/SE",
                "distance_mi": 5,
                "type": "mountain",
                "notes": (
                    "Cedar Fire (2003) destroyed entire community of Cuyamaca. "
                    "Heavy conifer forest with chronic drought stress. Cuyamaca "
                    "Peak (6,512 ft) creates terrain-driven fire acceleration. "
                    "Post-Cedar Fire landscape has regenerated significant "
                    "chaparral, creating new fuel loads."
                ),
            },
            {
                "name": "Cleveland National Forest",
                "bearing": "all",
                "type": "wildland",
                "notes": (
                    "Completely surrounds Julian. Both Cedar Fire and Witch "
                    "Creek Fire burned through CNF. Heavy recreational use "
                    "(camping, hiking, equestrian) creates ignition risk. "
                    "Cedar Fire was started by a lost hunter lighting a "
                    "signal fire in the CNF south of Ramona."
                ),
            },
            {
                "name": "Santa Ysabel Valley",
                "bearing": "NW",
                "distance_mi": 5,
                "type": "valley",
                "notes": (
                    "Witch Creek Fire (2007) started in the Santa Ysabel area. "
                    "Open grassland/chaparral valley that connects Julian to "
                    "Ramona via SR-78/79. Santa Ana winds accelerate through "
                    "this corridor."
                ),
            },
            {
                "name": "Banner Grade (SR-78 east)",
                "bearing": "E",
                "distance_mi": 3,
                "type": "terrain_trap",
                "notes": (
                    "Extremely steep, winding descent from Julian (4,200 ft) "
                    "into the Anza-Borrego desert toward Shelter Valley and "
                    "Earthquake Valley (below 2,000 ft). Only eastbound escape "
                    "route but also a fire corridor — desert Santa Ana winds "
                    "funnel upslope through this grade. Narrow, no shoulder, "
                    "dangerous at speed. A fire on Banner Grade would "
                    "eliminate the only eastbound evacuation option."
                ),
            },
            {
                "name": "Volcan Mountain",
                "bearing": "N",
                "distance_mi": 3,
                "type": "mountain",
                "notes": (
                    "Volcan Mountain (5,353 ft) north of Julian. Brush fire "
                    "incidents documented in steep, inaccessible terrain on "
                    "its slopes. Fires can approach Julian from the north "
                    "through this corridor."
                ),
            },
            {
                "name": "SR-78/SR-79 junction (center of town)",
                "bearing": "center",
                "type": "access_route",
                "notes": (
                    "Only major roads through town — both 2-lane mountain "
                    "highways. During Cedar Fire, sheriff's deputies and CHP "
                    "blocked traffic on Hwy 78 in Santa Ysabel and Hwy 79 "
                    "south of Cuyamaca for fire operations. The highways "
                    "served as both firebreaks and evacuation routes — "
                    "conflicting uses during a major fire. Cedar Fire jumped "
                    "the intersection of Hwys 78/79, creating a dire situation."
                ),
            },
        ],
        "evacuation": {
            "primary_routes": [
                "SR-79 south toward Cuyamaca/Descanso/I-8",
                "SR-78/79 west toward Santa Ysabel/Ramona",
            ],
            "secondary_routes": [
                "SR-78 east down Banner Grade toward Scissors Crossing/S2",
                "SR-79 north toward Warner Springs",
            ],
            "bottlenecks": [
                "SR-78/79 junction in center of town (single intersection)",
                "Banner Grade (steep, narrow, no shoulder)",
                "Santa Ysabel corridor (Witch Creek Fire origin zone)",
            ],
            "critical_vulnerability": (
                "During peak apple season (October = peak Santa Ana season), "
                "thousands of tourists are on narrow mountain roads. A fire "
                "blocking SR-78/79 to the west and SR-79 to the south would "
                "leave Banner Grade (steep, dangerous descent) as the only "
                "escape route for potentially 5,000+ people. All routes are "
                "2-lane mountain highways with no widening planned."
            ),
        },
        "infrastructure": {
            "utility": "SDG&E",
            "fire_hardening": (
                "SDG&E replaced wood poles with fire-resistant steel poles "
                "rated to 85 mph winds (some to 111 mph) in the Julian area. "
                "Strategic undergrounding project along Banner Road (SR-78) "
                "and Cape Horn Avenue east of downtown Julian to reduce "
                "wildfire risk and keep critical facilities powered during "
                "PSPS shutoffs. Facilities benefiting: post office, county "
                "library, Julian Union High School, Julian Charter School, "
                "Julian Elementary School, CAL FIRE Station."
            ),
            "water_system": (
                "Small community water system. During Witch Creek Fire 2007, "
                "power lines connecting water pumps burned, leaving residents "
                "without water for a week even after returning home."
            ),
            "cell_coverage": (
                "Mountain terrain creates coverage gaps. Remote location "
                "means limited tower density. Emergency communication "
                "reliability is a concern during fire events."
            ),
        },
        "community_preparedness": {
            "cwpp": (
                "Julian 2023 Community Wildfire Protection Plan published "
                "by San Diego County Fire Safe Council. Identifies specific "
                "fuel treatment priorities and evacuation improvements."
            ),
            "fire_safe_council": (
                "Julian Fire Safe Council (part of Backcountry Communities "
                "Thriving initiative) cooperates with CAL FIRE and SD County "
                "Fire. Promotes Firewise activities, structural hardening "
                "to meet/exceed County Building and Fire Code requirements."
            ),
        },
        "historical_fires": [
            "Cedar Fire 2003 (273,246 acres, 2,820 structures, 15 killed incl. 1 "
            "firefighter on Orchard Lane in Julian. Spread rate: 3,600-6,000 "
            "acres/hr, 2 acres/sec at peak. 30+ mi in <10 hrs. Started by "
            "lost hunter signaling with fire in CNF.)",
            "Witch Creek Fire 2007 (197,990 acres, 1,650 structures, 2 killed. "
            "Full evacuation of Julian. Started in Santa Ysabel area.)",
        ],
        "wui_class": "extreme",
        "compound_hazards": [
            "Tourist/resident evacuation conflict: peak apple season = peak fire season",
            "Banner Grade terrain trap: only eastbound escape is steep/dangerous",
            "Water system depends on power lines through fire zone",
            "Winter ice storms close SR-78/SR-79 (snow closures documented Feb 2019, "
            "2023) — compound hazard if ice precedes late-season fire",
            "5.2 magnitude earthquake struck near Julian April 2025 — seismic risk",
            "Remote location: fire response times measured in tens of minutes",
            "All evacuation routes are also potential fire corridors",
        ],
    },

    "ramona_ca": {
        "center": (33.0422, -116.8681),
        "elevation_ft": 1394,
        "terrain_notes": (
            "Large unincorporated community (pop 21,468 at 2020 census; ~22,800 "
            "estimated 2023; planning area 84,000+ acres / 130+ sq mi) in San "
            "Diego County backcountry at 1,394 ft elevation. Population has "
            "nearly doubled over the past 35 years, with continued development "
            "pushing into chaparral-covered hillsides. Ramona sits in a valley "
            "surrounded by chaparral hills with the Cuyamaca Mountains and "
            "Cleveland National Forest to the east. The entire area outside "
            "the Town Center is classified as fire-vulnerable, and all "
            "adjacent undeveloped areas are similarly at risk. California "
            "has proposed raising fire severity ratings from medium/high to "
            "'very high' for much of the Ramona planning area. "
            "\n\n"
            "Ramona's fire history is among the worst in California: the "
            "Cedar Fire (2003) burned ~50 sq mi on the south side of the "
            "community and killed 12 people in the Wildcat Canyon area "
            "southeast of town. Eight of those 12 died on Strange Way — a "
            "remote road off Wildcat Canyon Road that doesn't appear on "
            "official maps — with little or no warning that the fire was "
            "approaching. Victims included a mechanic and his wife fleeing "
            "in their car, a Walmart cashier with her 17-year-old daughter "
            "and relative at home, and a 77-year-old retired gardener. "
            "Firefighters were stymied by the difficult canyon terrain. "
            "\n\n"
            "The Witch Creek Fire (2007) was even more devastating locally: "
            "it swept over the east, north, and west sides of Ramona, "
            "burning nearly 70 sq mi. Combined with the simultaneous "
            "Guejito Fire, 1,141 homes and 509 outbuildings were destroyed "
            "in Ramona, Poway, Rancho Bernardo, Escondido, Del Dios, and "
            "Rancho Santa Fe. Ramona was ordered evacuated the first night, "
            "causing gridlock on SR-67 and SR-78 — evacuees spent hours on "
            "the two main routes with some drivers running out of gas en "
            "route. Power lines connecting water pumps burned, leaving "
            "residents without drinking water for a week after returning."
        ),
        "population": {
            "total_2020_census": 21468,
            "combined_area_2010": 30301,
            "estimated_2023": 22800,
            "growth_note": (
                "Population nearly doubled in 35 years. Continued rural "
                "residential development pushes WUI boundary deeper into "
                "chaparral. Many outlying residents not served by Ramona "
                "Municipal Water District, depend on wells."
            ),
        },
        "danger_quadrants": ["east", "northeast", "southeast", "north"],
        "safe_quadrants": ["west"],
        "key_features": [
            {
                "name": "Wildcat Canyon",
                "bearing": "SE",
                "distance_mi": 3,
                "type": "canyon",
                "notes": (
                    "Cedar Fire death zone: 12 of 15 total Cedar Fire "
                    "fatalities occurred in Wildcat Canyon/Muth Valley area. "
                    "8 died on Strange Way, a remote road off Wildcat Canyon "
                    "Road not shown on official maps. Serpentine road from "
                    "Ramona through Indian reservation into Lakeside. Extreme "
                    "fire behavior in canyon terrain — firefighters could not "
                    "reach victims due to terrain and fire intensity."
                ),
            },
            {
                "name": "Cleveland National Forest",
                "bearing": "E/NE",
                "distance_mi": 5,
                "type": "wildland",
                "notes": (
                    "Fire source zone during Santa Ana events. Both Cedar "
                    "and Witch Creek fires originated east of Ramona and "
                    "burned through CNF. Continuous wildland fuel from "
                    "mountains to town with no fire break."
                ),
            },
            {
                "name": "San Vicente Reservoir / San Diego River headwaters",
                "bearing": "S/SW",
                "distance_mi": 5,
                "type": "water_feature",
                "notes": (
                    "San Diego River headwaters originate in the chaparral-"
                    "filled valleys east of Ramona. Reservoir area provides "
                    "some break in fuels to the south but surrounding terrain "
                    "is heavily vegetated chaparral."
                ),
            },
            {
                "name": "Ramona Airport (KRNM)",
                "bearing": "E",
                "distance_mi": 2,
                "type": "infrastructure",
                "notes": (
                    "CAL FIRE air tanker base, critical for aerial fire "
                    "suppression in San Diego backcountry. Ramona Air Attack "
                    "Base supports initial attack on fires throughout the "
                    "region. Airport itself surrounded by chaparral."
                ),
            },
            {
                "name": "SR-67 corridor",
                "bearing": "SW",
                "type": "access_route",
                "notes": (
                    "Primary route to San Diego metro (Lakeside, El Cajon). "
                    "Currently 2 lanes through most of Ramona area. During "
                    "Witch Creek Fire 2007, evacuees spent hours gridlocked "
                    "on SR-67, some running out of gas. SANDAG budgeted $21M "
                    "for design/EIR to widen SR-67 to 4 lanes from Highland "
                    "Valley Road to Mapleview Street in Lakeside. Project "
                    "not yet constructed as of 2026."
                ),
            },
            {
                "name": "SR-78 corridor",
                "bearing": "E-W",
                "type": "access_route",
                "notes": (
                    "East-west route connecting Ramona to Julian (east) and "
                    "Escondido/I-15 (west). Also gridlocked during Witch "
                    "Creek Fire evacuation. Combined SR-67/SR-78 traffic "
                    "during mass evacuation overwhelms road capacity."
                ),
            },
        ],
        "evacuation": {
            "primary_routes": [
                "SR-67 south toward Lakeside/El Cajon/San Diego",
                "SR-78 west toward Escondido/I-15",
            ],
            "secondary_routes": [
                "SR-78 east toward Julian (uphill, into fire zone during Santa Ana events)",
                "Highland Valley Road, Mussey Grade Road (narrow rural roads)",
            ],
            "bottlenecks": [
                "SR-67 through Lakeside (2-lane, winding)",
                "SR-67/SR-78 junction in Ramona",
                "All routes funnel through limited chokepoints",
            ],
            "critical_vulnerability": (
                "21,000+ residents (30,000+ with San Diego Country Estates) "
                "on two 2-lane highways. Witch Creek Fire 2007 proved this "
                "is insufficient: hours of gridlock, drivers running out of "
                "gas. SR-67 widening ($21M SANDAG design study) not yet "
                "constructed. Community leaders describe evacuation routes "
                "as 'limited' and widening as 'urgent' for emergency safety."
            ),
            "sr67_widening": (
                "SANDAG budgeted $21M toward design and EIR for SR-67 "
                "widening to 4 lanes between Highland Valley Road (Ramona) "
                "and Mapleview Street (Lakeside). Ramona community leaders "
                "advocate urgently but project remains in planning phase."
            ),
        },
        "infrastructure": {
            "utility": "SDG&E",
            "fire_hardening": (
                "SDG&E replaced 34,000 wood poles with fire-resistant steel "
                "poles in backcountry since 2007 (Ramona, Julian, Descanso). "
                "SDG&E Fire Science & Climate Adaptation Dept employs 6 "
                "full-time meteorologists monitoring fire weather. Technosylva "
                "fire behavior modeling integrated into grid management."
            ),
            "water_system": (
                "Ramona Municipal Water District serves core area. Many "
                "outlying/rural residents depend on wells. Highland Valley "
                "area has separate agricultural water system for avocado "
                "groves. During Witch Creek Fire 2007, power lines connecting "
                "water pumps burned — residents without water for a week "
                "after returning home. Well-dependent households especially "
                "vulnerable (electric pumps fail during PSPS or fire-caused "
                "power outage)."
            ),
        },
        "community_preparedness": {
            "fire_safe_council": (
                "Ramona West End Fire Safe Council active in community "
                "education and fuel management. Focus on defensible space "
                "and structural hardening in the expanding WUI."
            ),
            "lessons_learned": (
                "2003 and 2007 fires transformed community awareness. "
                "San Diego Union-Tribune 'Searing Lessons' retrospective "
                "(2017) documented how the fires changed building codes, "
                "evacuation planning, and utility practices. SDG&E's "
                "post-2007 steel pole replacement program was a direct "
                "response to Witch Creek Fire infrastructure failures."
            ),
        },
        "historical_fires": [
            "Cedar Fire 2003 (273,246 total acres, 15 killed — 12 in Wildcat Canyon "
            "near Ramona. ~50 sq mi burned on south side of community. Fire moved "
            "at 3,600-6,000 acres/hr, 2 acres/sec at peak. 30+ mi in <10 hrs.)",
            "Witch Creek Fire 2007 (197,990 acres, 1,650 structures, 2 killed. "
            "Swept over east/north/west sides of Ramona, ~70 sq mi. Combined with "
            "Guejito Fire: 1,141 homes + 509 outbuildings destroyed across region. "
            "Ramona evacuees gridlocked on SR-67/SR-78 for hours.)",
        ],
        "wui_class": "extreme",
        "compound_hazards": [
            "Rapid population growth into fire-prone chaparral (doubled in 35 yrs)",
            "Evacuation routes proven inadequate in 2007 (gridlock, fuel exhaustion)",
            "SR-67 widening still not constructed despite SANDAG $21M allocation",
            "Well-dependent rural households lose water during power outages",
            "Power line/water pump interdependency (both failed in 2007)",
            "Wildcat Canyon terrain trap (12 Cedar Fire deaths in canyon with no escape)",
            "All surrounding areas are fire-vulnerable (no defensible buffer zone)",
            "Upwind of San Diego metro: fires starting here threaten 3+ million people",
        ],
    },

    # =========================================================================
    # SAN GABRIEL MOUNTAINS — Wrightwood
    # =========================================================================

    "wrightwood_ca": {
        "center": (34.3608, -117.6334),
        "elevation_ft": 5935,
        "terrain_notes": (
            "Mountain community (pop 4,720 at 2020 census, up from 4,525 in "
            "2010) in the San Gabriel Mountains at 5,935-6,208 ft elevation, "
            "situated in Swarthout Valley — a pine-forested valley on the "
            "north slope of the San Gabriel Mountains. Wrightwood sits "
            "directly on the San Andreas Fault — the USGS Wrightwood "
            "paleoseismic site (at Swarthout Creek, 3 km NW of town) has "
            "documented 14 large earthquakes in the past 1,500 years with "
            "a mean recurrence interval of 105 years and mean slip of 3.2 m "
            "per event. The 1812 Wrightwood earthquake produced up to 170 km "
            "of surface rupture along the Mojave segment. This creates a "
            "compound hazard virtually unique in California: a community "
            "simultaneously at extreme risk from wildfire AND a major "
            "earthquake, where one event could trigger or compound the other "
            "(earthquake rupturing gas lines during fire season, or fire "
            "destroying infrastructure before earthquake strikes). "
            "\n\n"
            "The community is surrounded by Angeles National Forest on the "
            "south and west with extremely steep terrain on all sides — fire "
            "agencies describe it as 'some of the most extreme terrain crews "
            "have fought fire in the state.' Mt. Baldy (10,064 ft) rises to "
            "the west/southwest. Cajon Pass (east, 8 mi) funnels Santa Ana "
            "winds through the I-15 corridor, creating extreme fire weather. "
            "The mountains have been uplifted so rapidly along the San Andreas "
            "that erosion hasn't fully reduced slopes to stable geometries — "
            "bridges and drainages are built to contain rocky debris flows. "
            "\n\n"
            "Bridge Fire (Sep 2024) demonstrated the vulnerability: the fire "
            "'exploded' from ~4,000 to 34,000+ acres in hours on Sep 10, "
            "growing another 13,000 acres overnight. Evacuation order issued "
            "4:44 PM Sep 10 for all of Wrightwood. SR-2 fully closed from "
            "SR-138 to west of Big Pines. The fire destroyed 81 buildings "
            "and damaged 19 more (20 homes in Mt Baldy Village, 3 in "
            "Wrightwood, 6 wilderness cabins). Wrightwood's strong community "
            "preparedness proved critical: out of 2,000+ residences, only "
            "13 were destroyed (99%+ survival rate). The Wrightwood Fire "
            "Safe Council attributed this to years of defensible space "
            "advocacy — most homes had pruned grasses, saplings, and lower "
            "limbs. Mountain High Ski Resort structures all survived. "
            "\n\n"
            "Blue Cut Fire (Aug 2016) was even larger: 36,274 acres, 105 "
            "structures destroyed, 82,000 people evacuated across the region "
            "including Wrightwood, Swarthout Canyon, Lone Pine Canyon, West "
            "Cajon Valley, and Lytle Creek. I-15 (the main route between "
            "LA and Las Vegas) was fully closed through Cajon Pass. "
            "Wrightwood is a popular ski community with Mountain High Resort "
            "immediately west in Big Pines, creating significant seasonal "
            "population swings — winter ski weekends can flood the roads with "
            "LA visitors."
        ),
        "population": {
            "total_2020_census": 4720,
            "seasonal_note": (
                "Winter ski season (Mountain High Resort) brings thousands of "
                "LA-area visitors on weekends. Summer hikers and campers. "
                "Effective population can surge well beyond 4,700 residents "
                "during peak recreation periods."
            ),
        },
        "danger_quadrants": ["south", "southwest", "southeast", "west", "east"],
        "safe_quadrants": [],
        "key_features": [
            {
                "name": "San Andreas Fault",
                "bearing": "through town",
                "type": "seismic_hazard",
                "notes": (
                    "Wrightwood sits directly on the San Andreas Fault. "
                    "USGS paleoseismic site at Swarthout Creek (3 km NW) "
                    "documents 14 large earthquakes in 1,500 years (mean "
                    "recurrence 105 yrs, mean slip 3.2 m). 1812 earthquake: "
                    "up to 170 km surface rupture. Compound hazard: earthquake "
                    "could rupture gas lines during fire season, or fire could "
                    "destroy infrastructure before earthquake. Mountains "
                    "uplifted along fault so rapidly that slopes are inherently "
                    "unstable — debris flows, rockslides, and mudslides are "
                    "chronic. Post-Bridge Fire, rain caused debris/mud flows "
                    "on Hwy 2 requiring shelter-in-place orders."
                ),
            },
            {
                "name": "San Gabriel Mountains / Mt Baldy",
                "bearing": "W/SW",
                "distance_mi": 10,
                "type": "mountain",
                "notes": (
                    "Mt Baldy (10,064 ft) — highest peak in San Gabriel "
                    "Mountains. Extremely steep terrain. Bridge Fire burned "
                    "through this area Sep 2024, destroying 20 homes in "
                    "Mt Baldy Village. Fire travels upslope toward Wrightwood "
                    "from the south/southwest on extremely steep, heavily "
                    "forested slopes."
                ),
            },
            {
                "name": "Cajon Pass",
                "bearing": "E",
                "distance_mi": 8,
                "type": "wind_gap",
                "notes": (
                    "Major pass funneling Santa Ana winds from the Mojave "
                    "Desert through the I-15 corridor. Wind acceleration "
                    "through the pass creates extreme fire weather — gusts "
                    "frequently exceed 60 kt during Santa Ana events. Blue "
                    "Cut Fire (2016) burned 36,274 acres through the pass, "
                    "forcing closure of I-15 in both directions (main LA-"
                    "Vegas route). Lone Pine Canyon connects Cajon Pass to "
                    "Wrightwood — fire road gate at canyon crest."
                ),
            },
            {
                "name": "Swarthout Valley / Canyon",
                "bearing": "NW",
                "distance_mi": 1,
                "type": "valley",
                "notes": (
                    "Pine-forested valley where Wrightwood is situated. "
                    "Swarthout Creek crosses the San Andreas Fault (USGS "
                    "paleoseismic trench site). Valley is bounded by steep "
                    "mountain slopes on all sides. Early ski enthusiasts "
                    "discovered the north-facing slopes above Swarthout "
                    "Valley; Mountain High Resort developed here. Blue Cut "
                    "Fire evacuation orders included Swarthout Canyon."
                ),
            },
            {
                "name": "Angeles National Forest",
                "bearing": "S/W",
                "type": "wildland",
                "notes": (
                    "Surrounds community on south and west. Bridge Fire "
                    "(2024, 56,030 acres), Bobcat Fire (2020, 115,796 acres), "
                    "and Sheep Fire (2022) all burned in ANF near Wrightwood. "
                    "Station Fire (2009, 160,577 acres) burned farther west "
                    "in ANF. The forest has an extensive fire history with "
                    "major fires every few years."
                ),
            },
            {
                "name": "SR-2 (Angeles Crest Highway)",
                "bearing": "W",
                "type": "access_route",
                "notes": (
                    "Primary westbound route connecting Wrightwood to LA via "
                    "mountain highway. Fully closed during Bridge Fire 2024 "
                    "(from SR-138 to west of Big Pines). Frequently closed "
                    "by fire, snow, rockslides, and debris flows. Narrow "
                    "mountain road — not designed for mass evacuation. After "
                    "Bridge Fire, rain caused debris/mud flows that again "
                    "closed SR-2 and triggered shelter-in-place for Wrightwood."
                ),
            },
            {
                "name": "Big Pines Highway / Lone Pine Canyon Road",
                "bearing": "S/E",
                "type": "access_route",
                "notes": (
                    "Secondary routes. Big Pines Hwy runs south toward Big "
                    "Pines and Mountain High Resort. Lone Pine Canyon Road "
                    "connects to I-15 via Cajon Pass — goes through some of "
                    "the worst burn areas from previous fires, with scarred "
                    "hills on both sides. Both are narrow mountain roads with "
                    "limited capacity."
                ),
            },
        ],
        "evacuation": {
            "primary_routes": [
                "SR-2 west toward La Canada Flintridge / LA",
                "Lone Pine Canyon Road east to I-15 at Cajon Pass",
            ],
            "secondary_routes": [
                "Big Pines Highway south",
                "SR-2 east toward SR-138 / Palmdale",
            ],
            "bottlenecks": [
                "SR-2 is a single narrow mountain road (closed by fire, snow, debris)",
                "Lone Pine Canyon Road goes through burn scars, narrow",
                "All routes are mountain roads with no 4-lane alternatives",
            ],
            "critical_vulnerability": (
                "During Bridge Fire 2024, SR-2 was fully closed — the primary "
                "westbound route. With 4,700+ residents plus ski/recreation "
                "visitors, all routes are narrow mountain roads. Community is "
                "effectively surrounded by terrain that has burned repeatedly "
                "(Bridge 2024, Blue Cut 2016, Bobcat 2020, Sheep 2022). "
                "Post-fire debris flows add compound risk — rain after the "
                "Bridge Fire closed roads again with mud/debris. Winter "
                "ski traffic on weekends coincides with potential late-season "
                "fires and avalanche/debris risk."
            ),
        },
        "infrastructure": {
            "utility": "SCE (Southern California Edison)",
            "psps_notes": (
                "SCE implements PSPS shutoffs in the San Gabriel Mountains. "
                "Mountain community vulnerable to extended outages. Community "
                "Services District provides local governance."
            ),
            "water_system": "Wrightwood Community Services District",
            "debris_flow_infrastructure": (
                "Bridges and drainages throughout area built to contain "
                "rocky floods and debris flows from unstable slopes along "
                "San Andreas Fault zone. Post-fire hydrophobic soils "
                "dramatically increase debris flow risk — demonstrated "
                "after Bridge Fire when rain triggered shelter-in-place."
            ),
        },
        "community_preparedness": {
            "fire_safe_council": (
                "Wrightwood Fire Safe Council (501(c)(3), founded 2003). "
                "Monthly meetings third Tuesday at Community Building, "
                "1275 Hwy 2. Advocated defensible space, evacuation planning. "
                "Bridge Fire 2024 validated their work: out of 2,000+ "
                "residences, only 13 destroyed (99%+ survival rate). Most "
                "homes had defensible space per FSC recommendations. All "
                "Mountain High Resort structures survived."
            ),
            "regional_coordination": (
                "Mountain Rim Fire Safe Council Regional Project covers "
                "Wrightwood, Mt. Baldy, and Lytle Creek communities. "
                "Wildfire & Disaster Awareness Day events held at community "
                "building for education."
            ),
            "success_story": (
                "The Wrightwood Fire Safe Council is a national model for "
                "community fire preparedness. Their 20-year effort (2003-2024) "
                "to promote defensible space directly saved the community "
                "during the Bridge Fire. Media coverage (Yahoo News, local "
                "outlets) highlighted how community action prevented "
                "catastrophic losses."
            ),
        },
        "historical_fires": [
            "Bridge Fire 2024 (56,030 acres. Exploded from ~4,000 to 34,000+ acres "
            "in hours Sep 10. Evacuation order 4:44 PM. SR-2 fully closed. "
            "81 buildings destroyed, 19 damaged. Wrightwood: only 13 of 2,000+ "
            "residences destroyed thanks to defensible space program.)",
            "Blue Cut Fire 2016 (36,274 acres, 105 structures, 82,000 evacuated "
            "incl. Wrightwood/Swarthout/Lone Pine Canyons. I-15 closed through "
            "Cajon Pass. Started on Blue Cut hiking trail in San Bernardino NF.)",
            "Bobcat Fire 2020 (115,796 acres in ANF, evacuation warnings for Wrightwood)",
            "Sheep Fire 2022 (nearby in ANF, evacuation warnings)",
            "Station Fire 2009 (160,577 acres, largest in modern LA County ANF history)",
        ],
        "wui_class": "extreme",
        "compound_hazards": [
            "San Andreas Fault: 14 major earthquakes in 1,500 years at this site; "
            "mean recurrence 105 years. Community sits ON the fault. Earthquake "
            "could rupture gas lines and water mains during fire season.",
            "Post-fire debris flows: Bridge Fire burn scar + rain = mud/debris on SR-2, "
            "shelter-in-place orders. Repeat of this pattern likely after any future fire.",
            "Winter storm/fire overlap: ski community with heavy snow can have late-season "
            "fires. Snow-blocked roads + fire = no evacuation route.",
            "Cajon Pass wind acceleration: 60+ kt gusts during Santa Ana events funnel "
            "through pass directly toward community.",
            "SR-2 closure dependency: primary route frequently closed by fire, snow, "
            "rockslides, debris flows. No redundant 4-lane evacuation route exists.",
            "Seasonal population surge: Mountain High ski resort brings thousands of "
            "LA visitors on winter weekends, overwhelming mountain road capacity.",
            "Terrain instability: San Andreas uplift faster than erosion = unstable "
            "slopes, chronic rockslide and debris flow risk independent of fire.",
        ],
    },
}
