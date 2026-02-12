"""
Enhanced California Fire-Vulnerable City Profiles
===================================================
Ventura County + San Bernardino Mountains corridor

Cities: Ojai, Ventura, Thousand Oaks, Lake Arrowhead, Crestline

These profiles contain deep operational intelligence focused on:
  - Evacuation route constraints (the #1 killer in California wildfires)
  - Fire spread rates and behavior documented from actual incidents
  - Infrastructure vulnerabilities (power lines, water systems, roads)
  - Population/demographic factors affecting evacuation
  - Terrain micro-features that channel winds and fire
  - Historical fire behavior with specific tactical details

Sources:
  - Thomas Fire (2017): VCFD cause determination; CAL FIRE; SCE CPUC investigation;
    DOJ $80M settlement (2024); Noozhawk Matilija Canyon reporting
  - Woolsey Fire (2018): CPUC investigation; LA County After-Action Review;
    NPS Santa Monica Mountains NRA damage assessment
  - Old Fire (2003): CAL FIRE; San Bernardino Sun retrospective; arson trial records
  - Grass Valley Fire (2007): USFS Research Paper (Maranghides & Mell);
    USGS Open-File Report 2008-1045
  - Slide Fire (2007): CAL FIRE incident report
  - Line Fire (2024): CAL FIRE incident updates; SB County evacuation orders
  - Wheeler Fire (1985): CAL FIRE; Santa Barbara Bucket Brigade archive
  - Sundowner winds: Cannon et al. (2017); NWS LOX; UCSB climatology
  - Census: US Census Bureau 2020 decennial; ACS 5-year estimates
  - Water: Casitas MWD; Crestline-Lake Arrowhead Water Agency (CLAWA)
"""

ENHANCED_TERRAIN_PROFILES = {

    # =========================================================================
    # OJAI — Thomas Fire corridor, Sundowner wind trap, single-exit valley
    # =========================================================================
    "ojai_ca": {
        "center": (34.4480, -119.2429),
        "elevation_ft": 746,
        "population": 7637,
        "population_year": 2020,
        "median_age": 49.7,
        "demographic_notes": (
            "Population 7,637 (2020 Census). Median age 49.7 years — one of the "
            "oldest communities in Ventura County. 27.2% of residents are 65+, "
            "and the city has 19 senior living/nursing facilities for a town of "
            "under 8,000. This elderly-heavy demographic critically slows "
            "evacuation response times. Artist/retirement community character "
            "with many residents who have limited mobility or no personal vehicle. "
            "Chain stores prohibited by city ordinance — small-town character "
            "but also means limited commercial infrastructure for shelter/staging."
        ),
        "terrain_notes": (
            "Small city (pop ~7,600) in the Ojai Valley, a bowl-shaped depression "
            "surrounded by mountains on three sides: Topatopa Mountains (6,300+ ft) "
            "to the north, Sulphur Mountain to the south, and Black Mountain/"
            "Nordhoff Ridge to the east. The valley is essentially a terrain trap — "
            "mountains funnel hot, dry air from the interior during both Santa Ana "
            "and Sundowner wind events. Thomas Fire (2017) nearly encircled the "
            "city, burning through Matilija Canyon from the north and wrapping "
            "around both flanks. By December 13, 2017 the fire had completely "
            "surrounded the Ojai Valley including Lake Casitas. Only SR-33 (north "
            "through canyon) and SR-150 (east toward Santa Paula / west toward "
            "Carpinteria) provide access — effectively TWO roads for 7,600+ people "
            "plus tourists. During Thomas Fire, SR-150 to Santa Paula was closed "
            "by CHP and the evacuation queue on remaining routes stretched for "
            "miles. The valley floor sits at 746 ft but is immediately bounded by "
            "terrain rising to 4,000-6,000+ ft, creating extreme fire behavior "
            "amplification through slope-driven convection. Los Padres National "
            "Forest borders the city on N/NE/E with hundreds of thousands of "
            "acres of unmanaged wildland fuel."
        ),
        "evacuation_analysis": {
            "routes": [
                {
                    "name": "SR-33 (Maricopa Highway)",
                    "direction": "N/S through valley",
                    "lanes": 2,
                    "constraints": (
                        "Primary route. Runs through narrow canyon north of Ojai — "
                        "both sides were on fire during Thomas Fire with flames and "
                        "embers crossing the highway in the Wheeler Canyon area. "
                        "Single two-lane road with no shoulder in canyon sections. "
                        "Closed during Thomas Fire for firefighter access."
                    ),
                },
                {
                    "name": "SR-150 (east toward Santa Paula)",
                    "direction": "E",
                    "lanes": 2,
                    "constraints": (
                        "CHP closed this route during Thomas Fire as fire "
                        "burned along both sides. Thomas Fire ignition point at "
                        "Anlauf Canyon was directly adjacent to this road near "
                        "Santa Paula. When closed, Ojai is effectively cut off "
                        "from the east."
                    ),
                },
                {
                    "name": "SR-150 (west toward Carpinteria/US-101)",
                    "direction": "W",
                    "lanes": 2,
                    "constraints": (
                        "Winding mountain road over Casitas Pass. Narrow, "
                        "two-lane, steep grades. Viable escape if fire approaches "
                        "from N/E but extremely slow under heavy traffic. Single "
                        "accident blocks entire route."
                    ),
                },
            ],
            "estimated_evacuation_time_hours": 3.0,
            "worst_case_scenario": (
                "Fire approaching from N (Matilija Canyon) and E (Santa Paula) "
                "simultaneously — exactly what happened during Thomas Fire. "
                "SR-33 closed by fire in Wheeler Gorge, SR-150 east closed by "
                "fire near Santa Paula. Only exit is SR-150 west over Casitas "
                "Pass: single two-lane mountain road for 7,600+ residents plus "
                "tourists. With 27% elderly population, evacuation compliance "
                "and speed are severely degraded. Thomas Fire demonstrated this "
                "exact scenario is not hypothetical."
            ),
        },
        "wind_regimes": {
            "sundowner": (
                "Sundowner winds are the most dangerous fire weather for Ojai. "
                "Unlike Santa Anas (NE downslope from Great Basin), Sundowners "
                "are northerly downslope winds off the Santa Ynez Mountains that "
                "intensify around sunset — hence the name. Air descends rapidly, "
                "compresses, heats, and dries. Gale force (40-60 mph) hot dry "
                "winds funnel through canyons into the Ojai Valley. Sundowners "
                "have driven every major Ojai-area fire. Critical layer formation "
                "with height in the lower troposphere reflects gravity wave "
                "energy to the surface, amplifying downslope wind speed."
            ),
            "santa_ana": (
                "Classic NE foehn winds also funnel through Ojai Valley. "
                "Thomas Fire was driven by Santa Anas gusting to 70 mph on "
                "ridgelines, 35-45 mph sustained in the valleys."
            ),
        },
        "danger_quadrants": ["north", "east", "west", "northwest"],
        "safe_quadrants": [],
        "key_features": [
            {
                "name": "Matilija Canyon",
                "bearing": "N",
                "distance_mi": 5,
                "type": "major_canyon",
                "notes": (
                    "Deep, steep-walled canyon extending into Los Padres NF. "
                    "Thomas Fire devastated this entire canyon — the lower "
                    "section was burned out overnight. Extremely remote and "
                    "rugged terrain with rock outcrops, crumbling slopes, and "
                    "steep side-canyons filled with dense brush. North Fork "
                    "Matilija Creek provides fuel-laden drainage directly toward "
                    "Ojai Valley. Matilija Wilderness area is 29,600 acres of "
                    "unmanaged fuel. Wheeler Fire (1985) also burned through "
                    "this canyon with winds pushing fire through Matilija and "
                    "over the Santa Ynez Mountains."
                ),
            },
            {
                "name": "Wheeler Gorge / Wheeler Canyon",
                "bearing": "NW",
                "distance_mi": 8,
                "type": "canyon",
                "notes": (
                    "Deep gorge along SR-33 north of Ojai. Wheeler Fire (1985) "
                    "ignited here by arsonist — burned 119,361 acres. Thomas "
                    "Fire burned through upper Wheeler Canyon with flames and "
                    "embers crossing SR-33 on both sides. Wheeler Gorge "
                    "Campground damaged. Canyon channeling accelerates winds "
                    "and firebrands directly toward Ojai Valley."
                ),
            },
            {
                "name": "Topatopa Mountains",
                "bearing": "N/NE",
                "distance_mi": 3,
                "type": "mountain",
                "notes": (
                    "6,300+ ft mountains directly above Ojai Valley. "
                    "4,500+ ft elevation gain from valley floor creates "
                    "extreme slope-driven fire runs. Topatopa Bluff (6,367 ft) "
                    "is the dominant terrain feature."
                ),
            },
            {
                "name": "Los Padres National Forest",
                "bearing": "N/E",
                "distance_mi": 2,
                "type": "wildland",
                "notes": (
                    "Massive undeveloped wildland — 1.75 million acres total. "
                    "Thomas Fire burned 150,000+ acres of LPNF lands. Fuel "
                    "loads include heavy chaparral, coastal sage scrub, and "
                    "mixed oak-conifer at higher elevations. DOJ recovered "
                    "$80M from SCE for LPNF damage alone."
                ),
            },
            {
                "name": "Sulphur Mountain",
                "bearing": "S",
                "distance_mi": 2,
                "type": "mountain",
                "notes": (
                    "Forms southern wall of Ojai Valley. Sulphur Mountain Road "
                    "is a narrow canyon road and fire corridor. Chaparral-covered "
                    "slopes face north into valley."
                ),
            },
            {
                "name": "Lake Casitas",
                "bearing": "SW",
                "distance_mi": 4,
                "type": "water_feature",
                "notes": (
                    "Primary water supply for Ojai via Casitas Municipal Water "
                    "District. Thomas Fire forced evacuation of Casitas MWD "
                    "water treatment facility staff, resulting in boil-water "
                    "advisory for Ojai and Ventura. Fire completely surrounded "
                    "Lake Casitas by Dec 13. Critical single-point water "
                    "infrastructure vulnerability."
                ),
            },
            {
                "name": "SR-33 / Maricopa Highway",
                "bearing": "N/S",
                "type": "access_route",
                "notes": (
                    "Primary route through canyon north of Ojai. Two-lane, "
                    "no shoulder in canyon sections. Both sides on fire during "
                    "Thomas Fire. Only viable north-south corridor."
                ),
            },
            {
                "name": "SR-150 / Ojai-Santa Paula Road",
                "bearing": "E",
                "type": "access_route",
                "notes": (
                    "Eastern access to Santa Paula and US-101. Thomas Fire "
                    "ignition point (Anlauf Canyon, SCE power lines) was "
                    "adjacent to this road. Closed by CHP during Thomas Fire. "
                    "Two-lane road through agricultural/foothill terrain."
                ),
            },
        ],
        "infrastructure_vulnerabilities": [
            {
                "type": "power_lines",
                "operator": "Southern California Edison (SCE)",
                "detail": (
                    "Thomas Fire had TWO ignition points, both caused by SCE "
                    "equipment: (1) Anlauf Canyon north of Santa Paula — power "
                    "lines contacted each other in high winds, dropping heated "
                    "material onto dry vegetation; (2) Koenigstein Road in "
                    "Upper Ojai — transformer failure caused energized line to "
                    "fall to ground. SCE paid $80M to US government (2024) and "
                    "$550M in CPUC penalties for Thomas, Woolsey, and other fires. "
                    "SCE infrastructure runs throughout canyon terrain surrounding "
                    "Ojai with lines exposed to Sundowner and Santa Ana winds."
                ),
            },
            {
                "type": "water_supply",
                "operator": "Casitas Municipal Water District",
                "detail": (
                    "Single water treatment facility serving Ojai, Upper Ojai, "
                    "Casitas Springs, and parts of Ventura. Thomas Fire forced "
                    "staff evacuation from treatment plant, causing system "
                    "depressurization and boil-water advisory. Lake Casitas is "
                    "fed by Ventura River diversions and surrounding drainages — "
                    "all within Thomas Fire burn area. Post-fire debris flows "
                    "threaten water quality for years."
                ),
            },
        ],
        "historical_fires": [
            {
                "name": "Thomas Fire",
                "year": 2017,
                "acres": 281893,
                "structures_destroyed": 1063,
                "deaths": 2,
                "detail": (
                    "Nearly encircled Ojai. Two SCE-caused ignition points on "
                    "Dec 4. Spread at rate of one football field per second on "
                    "Dec 5 morning. Fire traveled 12 miles from ignition to "
                    "Ventura coast in hours. Burned 150,000+ acres of Los Padres "
                    "NF. Lower Matilija Canyon burned out overnight. Completely "
                    "surrounded Ojai Valley and Lake Casitas by Dec 13. Largest "
                    "fire in California recorded history at the time. Santa Ana "
                    "winds gusted to 70 mph on ridgelines. SCE settled for $80M. "
                    "$2.2 billion total damages."
                ),
            },
            {
                "name": "Wheeler Fire",
                "year": 1985,
                "acres": 119361,
                "structures_destroyed": 19,
                "deaths": 0,
                "detail": (
                    "Arson ignition in Wheeler Gorge, 15 mi NW of Ojai. "
                    "Expanded to 45,000 acres in just two days. Winds pushed "
                    "fire through Matilija Canyon and over Santa Ynez Mountains "
                    "into Santa Barbara watershed. 119,361 acres, 19 homes, "
                    "37 buildings, 32 vehicles, $3M in orchards. Largest fire "
                    "ever handled by a single incident management team at that "
                    "time. Required 30,000-acre backfire to control."
                ),
            },
            {
                "name": "Matilija Fire",
                "year": 1932,
                "acres": 220000,
                "structures_destroyed": None,
                "deaths": 0,
                "detail": (
                    "Massive wildfire in Matilija Canyon/Los Padres NF area. "
                    "Demonstrated the canyon's potential for extreme fire runs "
                    "decades before modern development increased exposure."
                ),
            },
        ],
        "fire_behavior_notes": (
            "The Ojai Valley is one of California's most dangerous terrain traps "
            "for wildfire. The bowl-shaped valley channels both Sundowner and "
            "Santa Ana winds, creating extreme fire weather amplification. Thomas "
            "Fire demonstrated the worst case: fire approaching from multiple "
            "quadrants simultaneously, cutting evacuation routes, threatening "
            "water supply, and nearly encircling 7,600+ residents (27% elderly) "
            "with only narrow two-lane mountain roads for escape. The Matilija "
            "Canyon-to-Ojai axis is a proven fire run corridor — fire races "
            "down-canyon driven by gravity winds and channeled by steep canyon "
            "walls, emerging into the populated valley at high speed."
        ),
        "wui_class": "extreme",
    },

    # =========================================================================
    # VENTURA — Thomas Fire coastal terminus, Santa Clara River corridor
    # =========================================================================
    "ventura_ca": {
        "center": (34.2746, -119.2290),
        "elevation_ft": 115,
        "population": 110763,
        "population_year": 2020,
        "median_age": 36.0,
        "demographic_notes": (
            "Population 110,763 (2020 Census). Major coastal city and Ventura "
            "County seat. Density 5,061/sq mi. 35.1% Hispanic/Latino. Unlike "
            "Ojai, Ventura has a younger, more diverse population with better "
            "transportation infrastructure. However, the eastern hillside "
            "neighborhoods (Clearpoint, Ondulando, Skyline, Foothill Heights) "
            "that face the highest fire risk are among the older, more affluent "
            "residential areas with narrow winding streets on steep terrain."
        ),
        "terrain_notes": (
            "Coastal city (pop ~111,000) where Thomas Fire (2017) first struck "
            "urban areas. Fire raced from the mountains NE of Santa Paula to "
            "the coast in hours, driven by 60-70 mph Santa Ana winds. Eastern "
            "hillside neighborhoods along Foothill Road — Clearpoint, Ondulando, "
            "Skyline, Foothill Heights — suffered the heaviest damage with 538 "
            "structures destroyed in the city of Ventura alone (half the Thomas "
            "Fire's total structure loss). City is bounded by mountains to N/NE "
            "with multiple canyon drainages that act as fire funnels into the "
            "urban interface. The Santa Clara River corridor (Hwy 126) provides "
            "a broad fire approach vector from the east. The Ventura River "
            "corridor channels fire from the mountains directly to the coast. "
            "Coastal plain elevation ~50-150 ft but terrain rises steeply to "
            "N and NE."
        ),
        "evacuation_analysis": {
            "routes": [
                {
                    "name": "US-101 Freeway",
                    "direction": "E-W (coastal)",
                    "lanes": 6,
                    "constraints": (
                        "Primary evacuation route. Thomas Fire came within "
                        "striking distance of 101 corridor. During Woolsey Fire "
                        "(2018), the 101 was jumped by fire in neighboring "
                        "Ventura County communities. High-capacity but also "
                        "serves as primary route for all of coastal Ventura "
                        "County — gridlock during regional evacuations."
                    ),
                },
                {
                    "name": "SR-126 (toward Santa Clarita/I-5)",
                    "direction": "E",
                    "lanes": 4,
                    "constraints": (
                        "Runs through Santa Clara River valley. Thomas Fire "
                        "approached along this corridor from Santa Paula. "
                        "Provides access to I-5 but is also a fire approach "
                        "vector — fire and evacuation route conflict."
                    ),
                },
                {
                    "name": "SR-33 (toward Ojai)",
                    "direction": "N",
                    "lanes": 2,
                    "constraints": (
                        "Two-lane road into mountains. Not viable evacuation "
                        "route during most fire scenarios — leads toward fire "
                        "source terrain."
                    ),
                },
            ],
            "estimated_evacuation_time_hours": 2.0,
            "worst_case_scenario": (
                "Fire from NE cuts SR-126, limiting eastern evacuation. 101 "
                "becomes sole corridor for 110,000+ residents and surrounding "
                "communities (Oxnard, Camarillo also evacuating). Thomas Fire "
                "demonstrated that fire can reach Ventura's urban core from "
                "Santa Paula in under 6 hours with strong Santa Ana winds."
            ),
        },
        "danger_quadrants": ["north", "northeast", "east"],
        "safe_quadrants": ["south", "southwest"],
        "key_features": [
            {
                "name": "Santa Clara River corridor / Hwy 126",
                "bearing": "E",
                "distance_mi": 0,
                "type": "river_valley",
                "notes": (
                    "Broad valley running E-W from Santa Clarita to coast. "
                    "Thomas Fire approached along this corridor from Santa "
                    "Paula ignition point. River bottom vegetation provides "
                    "continuous fuel. Santa Ana winds align with valley "
                    "orientation, accelerating fire westward toward Ventura. "
                    "Additional fires have ignited in river bottom vegetation "
                    "within city limits."
                ),
            },
            {
                "name": "Ventura River corridor",
                "bearing": "N",
                "distance_mi": 0,
                "type": "river_valley",
                "notes": (
                    "Drainage from Ojai Valley to coast, passing through "
                    "Ventura's western neighborhoods. Fire corridor from "
                    "mountains to coast. Riparian vegetation along river."
                ),
            },
            {
                "name": "Foothill Road hillside neighborhoods",
                "bearing": "N/NE",
                "distance_mi": 2,
                "type": "wui_interface",
                "notes": (
                    "Clearpoint, Ondulando, Skyline, Foothill Heights — "
                    "residential neighborhoods built on steep hillsides at "
                    "the urban-wildland boundary. Thomas Fire destroyed homes "
                    "here as fire descended from mountains. Narrow winding "
                    "streets, heavy ornamental vegetation, difficult access "
                    "for fire apparatus. 538 structures destroyed in Ventura "
                    "during Thomas Fire — concentrated in these neighborhoods."
                ),
            },
            {
                "name": "Two Trees / hills above downtown",
                "bearing": "N",
                "distance_mi": 1,
                "type": "escarpment",
                "notes": (
                    "Steep hills immediately above downtown Ventura. Thomas "
                    "Fire reached these hills, destroying apartment buildings "
                    "and homes above the downtown core. Fire reached the "
                    "interface between foothill rangeland and developed areas."
                ),
            },
            {
                "name": "Anlauf Canyon (Thomas Fire ignition)",
                "bearing": "NE",
                "distance_mi": 12,
                "type": "canyon",
                "notes": (
                    "Canyon north of Santa Paula where Thomas Fire first "
                    "ignited at 6:30 PM on Dec 4, 2017. SCE power lines "
                    "contacted each other in high winds. Fire ran 12 miles "
                    "from this point to Ventura coast in hours."
                ),
            },
            {
                "name": "US-101 Freeway",
                "bearing": "E-W",
                "type": "access_route",
                "notes": (
                    "Major coastal evacuation route. 6-lane freeway but "
                    "serves as primary corridor for all of coastal Ventura "
                    "County. Thomas Fire burned to within 1 mile of 101 in "
                    "several locations."
                ),
            },
        ],
        "infrastructure_vulnerabilities": [
            {
                "type": "power_lines",
                "operator": "Southern California Edison (SCE)",
                "detail": (
                    "Thomas Fire was caused by two SCE equipment failures. "
                    "Anlauf Canyon: lines contacted in wind, dropped heated "
                    "material. Koenigstein Road: transformer failure, energized "
                    "line fell. $80M DOJ settlement, $550M CPUC penalties. "
                    "SCE distribution and transmission lines serve all Ventura "
                    "hillside neighborhoods."
                ),
            },
            {
                "type": "water_supply",
                "operator": "Ventura Water / Casitas MWD",
                "detail": (
                    "Thomas Fire forced Casitas MWD treatment facility "
                    "evacuation, causing boil-water advisory for entire city "
                    "of Ventura. Foster Park pump station lost pressure. Water "
                    "system depressurization meant fire hydrants in hillside "
                    "neighborhoods had reduced or zero pressure during active "
                    "structure defense."
                ),
            },
        ],
        "historical_fires": [
            {
                "name": "Thomas Fire",
                "year": 2017,
                "acres": 281893,
                "structures_destroyed": 1063,
                "structures_in_ventura": 538,
                "deaths": 2,
                "detail": (
                    "Ignited Dec 4 near Santa Paula from SCE equipment. "
                    "Reached Ventura coast within hours. Spread at one football "
                    "field per second on morning of Dec 5. 104,607 residents "
                    "evacuated. Santa Ana gusts to 70 mph on ridgelines. "
                    "Destroyed Clearpoint, Ondulando, Skyline neighborhoods. "
                    "$2.2 billion total damages. Largest CA fire at that time."
                ),
            },
            {
                "name": "Woolsey Fire",
                "year": 2018,
                "acres": 96949,
                "structures_destroyed": 1643,
                "deaths": 3,
                "detail": (
                    "Burned in SE Ventura County / LA County. Demonstrated "
                    "that fire can jump US-101 freeway — the primary Ventura "
                    "evacuation route. 295,000 people evacuated across the "
                    "region."
                ),
            },
        ],
        "fire_behavior_notes": (
            "Thomas Fire demonstrated the extreme fire run potential from "
            "interior mountains to the Ventura coast. The fire traveled 12 "
            "miles in hours under Santa Ana conditions, reaching Ventura's "
            "hillside neighborhoods before most residents could evacuate. The "
            "spread rate of one football field per second (approximately 36 mph "
            "linear advance) illustrates the futility of late evacuation in "
            "Santa Ana conditions. The Santa Clara River and Ventura River "
            "corridors provide broad, fuel-laden approach vectors from the "
            "interior. Hillside neighborhoods on the WUI boundary absorbed "
            "half the fire's total structure loss."
        ),
        "wui_class": "high",
    },

    # =========================================================================
    # THOUSAND OAKS — Woolsey Fire corridor, Conejo Valley, 101 vulnerability
    # =========================================================================
    "thousand_oaks_ca": {
        "center": (34.1706, -118.8376),
        "elevation_ft": 900,
        "population": 126966,
        "population_year": 2020,
        "median_age": 44.5,
        "demographic_notes": (
            "Population 126,966 (2020 Census). Affluent suburban city forming "
            "the central core of the Conejo Valley. Median age 44.5. "
            "68.3% White, 19.9% Hispanic. City is characterized by 50,000-60,000 "
            "oak trees within city limits. Major employment center with numerous "
            "corporate offices that evacuated during Woolsey Fire. Large "
            "commuter population — many residents away during daytime fires but "
            "creating return-traffic conflicts during evacuation."
        ),
        "terrain_notes": (
            "City of 127,000 in the Conejo Valley, a broad basin bounded by "
            "the Santa Monica Mountains (chaparral-covered, 2,000-3,000 ft) "
            "to the south, Simi Hills to the east/northeast, Conejo Mountains "
            "and Mount Clef Ridge to the north. Woolsey Fire (2018) demonstrated "
            "the city's extreme vulnerability: fire raced from Santa Susana "
            "Field Laboratory in the Simi Hills through Oak Park, jumped the "
            "101 Freeway at multiple points near Liberty Canyon with a 14-mile-"
            "long fireline, and continued through the Santa Monica Mountains "
            "to the coast, burning 80% of the Santa Monica Mountains National "
            "Recreation Area. The fire was driven by 50-70 mph Santa Ana winds "
            "and jumped the 101 Freeway — a presumed firebreak — at several "
            "points. Conejo Grade (US-101) between Thousand Oaks and Camarillo "
            "is a key wind acceleration point where terrain compression "
            "increases wind velocity. The Santa Monica Mountains chaparral has "
            "a natural fire return interval of 30-100 years, but fires now "
            "occur every 5-20 years due to human ignition, preventing full "
            "ecosystem recovery and creating type-converted grass/annual fuels "
            "that burn even more frequently."
        ),
        "evacuation_analysis": {
            "routes": [
                {
                    "name": "US-101 Freeway (westbound toward Camarillo/Ventura)",
                    "direction": "W",
                    "lanes": 6,
                    "constraints": (
                        "Primary evacuation route. Woolsey Fire CLOSED a "
                        "4-mile stretch from Las Virgenes Road to Kanan Road. "
                        "All lanes shut from Las Virgenes Canyon Rd (Calabasas) "
                        "to Adobe Rd (Agoura Hills). Also closed southbound "
                        "from Hwy 23 in Thousand Oaks to Hwy 34 in Camarillo. "
                        "When fire jumps 101, the presumed primary escape route "
                        "becomes impassable."
                    ),
                },
                {
                    "name": "US-101 Freeway (eastbound toward LA)",
                    "direction": "E",
                    "lanes": 6,
                    "constraints": (
                        "Woolsey Fire jumped 101 at Liberty Canyon, cutting "
                        "eastbound evacuation. Fire crossed at multiple points "
                        "along a 14-mile front."
                    ),
                },
                {
                    "name": "SR-23 (northbound toward Moorpark/Simi Valley)",
                    "direction": "N",
                    "lanes": 4,
                    "constraints": (
                        "Viable evacuation north through Conejo Grade if fire "
                        "is approaching from S/SE (Santa Monica Mountains). "
                        "However, Woolsey Fire originated from Simi Hills to "
                        "the NE — this route led TOWARD fire origin."
                    ),
                },
                {
                    "name": "Westlake Blvd / Kanan Rd / other surface streets",
                    "direction": "various",
                    "lanes": 2,
                    "constraints": (
                        "Surface streets through suburban neighborhoods. "
                        "Gridlocked during Woolsey Fire evacuations. Many lead "
                        "into Santa Monica Mountains — toward fire."
                    ),
                },
            ],
            "estimated_evacuation_time_hours": 2.5,
            "worst_case_scenario": (
                "Woolsey Fire demonstrated the worst case: fire approached "
                "from NE (Simi Hills), jumped 101 at multiple points cutting "
                "both east and west freeway evacuation, and burned south through "
                "Santa Monica Mountains. 295,000 people evacuated across the "
                "region. Bell Canyon, Oak Park, Agoura Hills, Malibu — all "
                "required total evacuation. Corporate offices in Thousand Oaks "
                "added to daytime evacuation traffic. For a city of 127,000, "
                "the freeway-dependent evacuation model fails when fire crosses "
                "the freeway."
            ),
        },
        "danger_quadrants": ["east", "northeast", "south", "southeast"],
        "safe_quadrants": ["west", "northwest"],
        "key_features": [
            {
                "name": "Santa Monica Mountains",
                "bearing": "S/SE",
                "distance_mi": 3,
                "type": "mountain",
                "notes": (
                    "Woolsey Fire burned 80% of the 156,000-acre Santa Monica "
                    "Mountains National Recreation Area. Dense chaparral, steep "
                    "canyons. Natural fire return interval 30-100 years but now "
                    "burning every 5-20 years. When chaparral burns too frequently "
                    "(< 10 years), seed banks are consumed and non-native grasses "
                    "colonize, creating grass-fire type conversion that burns "
                    "even more often."
                ),
            },
            {
                "name": "Simi Hills / Santa Susana Field Laboratory",
                "bearing": "E/NE",
                "distance_mi": 5,
                "type": "mountain",
                "notes": (
                    "Woolsey Fire ignited at Santa Susana Field Laboratory "
                    "(SSFL) — a former rocket testing and nuclear research "
                    "facility with known soil contamination. Fire burned 80% "
                    "of the 2,850-acre site. SSFL contains residual radioactive "
                    "and chemical contamination from a 1959 partial nuclear "
                    "meltdown. Studies detected radioactive microparticles "
                    "(thorium) in ash deposited up to 15 km from SSFL during "
                    "Woolsey Fire. Oak Park, Bell Canyon communities are "
                    "directly downwind."
                ),
            },
            {
                "name": "Liberty Canyon (101 Freeway crossing)",
                "bearing": "SE",
                "distance_mi": 5,
                "type": "canyon",
                "notes": (
                    "Location where Woolsey Fire jumped the 101 Freeway. "
                    "14-mile-long fireline crossed the freeway at multiple "
                    "points near Liberty Canyon, driven by 50-60 mph winds. "
                    "Liberty Canyon is also a key wildlife corridor connecting "
                    "Santa Monica Mountains to Simi Hills."
                ),
            },
            {
                "name": "Conejo Grade (US-101 between TO and Camarillo)",
                "bearing": "W/SW",
                "distance_mi": 3,
                "type": "mountain_pass",
                "notes": (
                    "Steep grade on US-101. Terrain compression accelerates "
                    "wind through this gap. Hill Fire (same day as Woolsey) "
                    "jumped 101 at Conejo Grade, burning thousands of acres. "
                    "Wind funneling effect creates extreme fire weather."
                ),
            },
            {
                "name": "Oak Park",
                "bearing": "E",
                "distance_mi": 3,
                "type": "community",
                "notes": (
                    "Residential community hit first by Woolsey Fire as it "
                    "moved from Simi Hills south. Total evacuation ordered. "
                    "Homes destroyed on Churchwood Dr, Wembly Ave, Symphony "
                    "Lane. Community sits directly below SSFL contaminated site."
                ),
            },
            {
                "name": "Bell Canyon",
                "bearing": "E",
                "distance_mi": 8,
                "type": "community",
                "notes": (
                    "Gated community in narrow canyon — total evacuation during "
                    "Woolsey Fire. Single access road. Directly in fire path "
                    "from SSFL."
                ),
            },
            {
                "name": "US-101 / SR-23 intersection",
                "bearing": "center",
                "type": "access_route",
                "notes": (
                    "Major evacuation hub. Both routes were impacted during "
                    "Woolsey Fire. 101 closed in multiple sections, SR-23 "
                    "led toward fire origin."
                ),
            },
        ],
        "infrastructure_vulnerabilities": [
            {
                "type": "power_lines",
                "operator": "Southern California Edison (SCE)",
                "detail": (
                    "SCE infrastructure throughout Simi Hills and Santa Monica "
                    "Mountains. CPUC investigation found SCE equipment "
                    "associated with Woolsey Fire ignition at SSFL. Part of "
                    "$550M CPUC penalty package."
                ),
            },
            {
                "type": "contaminated_site",
                "operator": "Boeing / DOE / NASA",
                "detail": (
                    "Santa Susana Field Laboratory contains radioactive and "
                    "chemical contamination from decades of rocket testing and "
                    "a 1959 partial nuclear meltdown. Woolsey Fire burned 80% "
                    "of the site, potentially mobilizing contaminants in smoke "
                    "and ash. Radioactive microparticles detected in ash up to "
                    "15 km away. This adds a hazmat dimension to any fire "
                    "originating from or burning through SSFL."
                ),
            },
        ],
        "historical_fires": [
            {
                "name": "Woolsey Fire",
                "year": 2018,
                "acres": 96949,
                "structures_destroyed": 1643,
                "deaths": 3,
                "detail": (
                    "Ignited Nov 8 at Santa Susana Field Laboratory. Driven by "
                    "50-70 mph Santa Ana winds. Jumped 101 Freeway at Liberty "
                    "Canyon with 14-mile fireline. Burned 80% of Santa Monica "
                    "Mountains NRA. 295,000 evacuated from 105,000 residences. "
                    "Total evacuation of Bell Canyon, Oak Park, Malibu, Agoura "
                    "Hills. Radioactive microparticles from SSFL detected in "
                    "ash deposits."
                ),
            },
            {
                "name": "Hill Fire",
                "year": 2018,
                "acres": 4531,
                "structures_destroyed": 4,
                "deaths": 0,
                "detail": (
                    "Ignited same day as Woolsey Fire. Jumped 101 at Conejo "
                    "Grade. Demonstrated that the 101 freeway is NOT a reliable "
                    "firebreak in Santa Ana conditions."
                ),
            },
            {
                "name": "Easy Fire",
                "year": 2019,
                "acres": 1860,
                "structures_destroyed": 0,
                "deaths": 0,
                "detail": (
                    "Burned in Simi Valley/Moorpark area, forcing evacuations. "
                    "Demonstrated continued fire threat from Simi Hills corridor."
                ),
            },
            {
                "name": "Springs Fire",
                "year": 2013,
                "acres": 24251,
                "structures_destroyed": 15,
                "deaths": 0,
                "detail": (
                    "Burned in Santa Monica Mountains near Camarillo. "
                    "Demonstrated regional fire potential."
                ),
            },
        ],
        "fire_behavior_notes": (
            "The Woolsey Fire fundamentally changed the risk assessment for "
            "Thousand Oaks and the Conejo Valley. Before 2018, the 101 Freeway "
            "was considered a de facto firebreak separating the chaparral-covered "
            "Santa Monica Mountains from suburban development. Woolsey Fire "
            "proved this assumption catastrophically wrong: driven by 50-70 mph "
            "Santa Ana winds, a 14-mile-long fireline jumped the 101 at multiple "
            "points near Liberty Canyon, continuing south through the Santa "
            "Monica Mountains to the Pacific Ocean. The fire destroyed 1,643 "
            "structures and required evacuation of 295,000 people. The "
            "contaminated origin site (SSFL) adds a unique hazmat dimension — "
            "radioactive and chemical contaminants were mobilized in smoke and "
            "ash. Santa Monica Mountains chaparral fire cycle has shortened from "
            "30-100 years to 5-20 years, meaning Thousand Oaks will face this "
            "threat repeatedly within a single generation."
        ),
        "wui_class": "extreme",
    },

    # =========================================================================
    # LAKE ARROWHEAD — Mountain island, limited escape, population surge
    # =========================================================================
    "lake_arrowhead_ca": {
        "center": (34.2580, -117.1890),
        "elevation_ft": 5174,
        "population": 12401,
        "population_year": 2020,
        "seasonal_population_peak": 40000,
        "seasonal_population_notes": (
            "Permanent population 12,401 (2020 Census). Approximately 4,000 "
            "homes occupied full-time by ~10,000 permanent residents. An "
            "additional 6,000 second/vacation homes are used on weekends, "
            "holidays, and summer. On a summer holiday weekend, population "
            "swells to 40,000 — quadrupling the permanent count. The area "
            "hosts 2.4 million visitors per year. Tourism contributes $78M "
            "annually. This seasonal population surge is an evacuation "
            "nightmare: 40,000 people, many unfamiliar with mountain roads, "
            "trying to descend via two-lane highways with hairpin turns."
        ),
        "median_age": None,
        "demographic_notes": (
            "Mountain resort community with extreme seasonal population "
            "variation. Mix of retirees, vacation homeowners, and service "
            "workers. Many seasonal visitors are unfamiliar with evacuation "
            "routes and mountain driving. Second-home owners may not receive "
            "or monitor local emergency alerts. 90% weekend/holiday occupancy "
            "vs 45% weekday occupancy means fire risk peaks correlate with "
            "maximum population exposure."
        ),
        "terrain_notes": (
            "Mountain resort community in the San Bernardino Mountains at "
            "5,174 ft elevation. Sits on a forested plateau atop the steep "
            "southern escarpment of the San Bernardino Mountains — a 4,000+ ft "
            "near-vertical drop to the San Bernardino Valley floor. The community "
            "is effectively a populated island on top of a mountain, accessible "
            "only by narrow, winding mountain roads. Dense conifer forest "
            "(ponderosa pine, sugar pine, incense cedar, white fir) with extreme "
            "fuel loading from decades of fire suppression and bark beetle "
            "mortality. The 2003 Old Fire climbed the southern escarpment from "
            "Waterman Canyon, forcing evacuation of 80,000+ from all mountain "
            "communities. The 2007 Grass Valley Fire destroyed 176 structures "
            "in a 'domino effect' where burning homes ignited adjacent homes "
            "without the wildfire as a factor. The 2024 Line Fire again forced "
            "evacuations, with Highway 18 closed northbound (inbound) while "
            "only southbound (outbound) traffic allowed. Lake Arrowhead "
            "reservoir provides a limited fire break at the community's center "
            "but is privately owned (Arrowhead Lake Association) and not "
            "accessible to the general public."
        ),
        "evacuation_analysis": {
            "routes": [
                {
                    "name": "SR-18 / Rim of the World Drive (south toward SB)",
                    "direction": "S/SW",
                    "lanes": 2,
                    "constraints": (
                        "Primary escape route. Two-lane road with hairpin turns "
                        "clinging to the rim of a 4,000 ft escarpment. No "
                        "shoulder in many sections. Single accident or downed "
                        "tree blocks entire route. Old Fire breached fire lines "
                        "along Rim of the World Hwy near Skyforest and burned "
                        "into Cedar Glen. During Line Fire (2024), SR-18 was "
                        "closed northbound — only outbound (downhill) traffic "
                        "allowed. Descent takes 30-45 min under normal "
                        "conditions; hours during mass evacuation."
                    ),
                },
                {
                    "name": "SR-18 east (toward Big Bear via Running Springs)",
                    "direction": "E",
                    "lanes": 2,
                    "constraints": (
                        "Connects to Running Springs, then Big Bear. During "
                        "Line Fire (2024), SR-18 was closed from Kuffel Canyon "
                        "to Big Bear Dam. Running Springs was under mandatory "
                        "evacuation. This route leads to ANOTHER mountain "
                        "community, not to safety at the valley floor. Only "
                        "useful if descending via SR-38 to Redlands (east side), "
                        "adding 60+ minutes."
                    ),
                },
                {
                    "name": "SR-138 (north toward Hesperia/I-15)",
                    "direction": "N",
                    "lanes": 2,
                    "constraints": (
                        "Northern escape route descending to high desert. "
                        "Connects to Crestline and then descends to I-15 via "
                        "Cajon Pass area. Two-lane, winding. During Old Fire, "
                        "SR-138 was slow-going but the best route to I-15 — "
                        "until the fire burned the east side below Cedarpines "
                        "Park and closed I-15. Back route through Silverwood "
                        "Lake area."
                    ),
                },
                {
                    "name": "SR-330 (south via Highland/Running Springs)",
                    "direction": "S",
                    "lanes": 2,
                    "constraints": (
                        "Alternative southern descent via Highland. During "
                        "Line Fire (2024), SR-330 was closed from Highland Ave "
                        "to SR-18 in Running Springs — completely severed. "
                        "Steep, narrow, winding. Known for accidents and "
                        "closures in winter (ice/snow)."
                    ),
                },
            ],
            "estimated_evacuation_time_hours": 5.0,
            "worst_case_scenario": (
                "Fire approaching from south (San Bernardino Valley floor) "
                "climbs the 4,000 ft escarpment — exactly as Old Fire (2003) "
                "did. SR-18 south and SR-330 are cut by fire on the southern "
                "face. SR-138 north is the only remaining route but passes "
                "through Crestline (also evacuating 11,650+ people). On a "
                "summer holiday weekend, 40,000 people are attempting to "
                "descend on a single two-lane mountain road (SR-138) through "
                "Crestline to I-15. An Arrowbear Lake resident during the "
                "2024 Line Fire reported it took nearly 7 HOURS to reach the "
                "evacuation center in Highland after turning back for a camera. "
                "This is a mass-casualty evacuation scenario for a mountain-"
                "top community with no helicopter pad capacity for 40,000."
            ),
        },
        "danger_quadrants": ["south", "southwest", "west"],
        "safe_quadrants": [],
        "key_features": [
            {
                "name": "San Bernardino Mountain southern escarpment",
                "bearing": "S/SW",
                "distance_mi": 1,
                "type": "escarpment",
                "notes": (
                    "Near-vertical 4,000+ ft drop from mountain communities "
                    "to San Bernardino Valley floor (elevation ~1,000 ft). "
                    "Old Fire (2003) climbed this face from Waterman Canyon "
                    "at over 1,000 acres/hour. Extreme slope-driven convection "
                    "creates flame lengths exceeding 100 ft. Santa Ana winds "
                    "compress against the mountain face, creating turbulent "
                    "upslope winds with long-range spotting capability — "
                    "embers launched miles ahead of the fire front."
                ),
            },
            {
                "name": "Grass Valley drainage",
                "bearing": "W",
                "distance_mi": 1,
                "type": "canyon",
                "notes": (
                    "Drainage one mile west of Lake Arrowhead where the 2007 "
                    "Grass Valley Fire started. Fire moved south through "
                    "drainage, then showered residential development with "
                    "firebrands at 0930. The USFS post-fire study documented "
                    "the 'domino effect': burning homes ignited adjacent homes "
                    "through radiant heat and ember showers, destroying 176 "
                    "structures independent of the wildfire's direct flame "
                    "front. Homes with wood shake roofs, pine litter in gutters, "
                    "and ornamental vegetation touching siding were the primary "
                    "ignition vectors."
                ),
            },
            {
                "name": "Rim of the World Drive (SR-18)",
                "bearing": "E-W",
                "type": "access_route",
                "notes": (
                    "Primary mountain road running along the rim of the "
                    "southern escarpment. Two-lane, hairpin turns, no shoulder. "
                    "Only route connecting Lake Arrowhead to Running Springs "
                    "and west to Crestline. Old Fire breached fire lines along "
                    "this road near Skyforest, allowing fire into Cedar Glen. "
                    "Road was designed for scenic tourism, not mass evacuation."
                ),
            },
            {
                "name": "SR-138 (toward Crestline / I-15)",
                "bearing": "W/N",
                "type": "access_route",
                "notes": (
                    "Connects Lake Arrowhead to Crestline and descends to "
                    "high desert. Two-lane, winding. Serves as backup "
                    "evacuation route when southern routes are cut."
                ),
            },
            {
                "name": "Cedar Glen",
                "bearing": "S",
                "distance_mi": 2,
                "type": "community",
                "notes": (
                    "Small mountain community on a single access road. Old "
                    "Fire (2003) destroyed 324 homes in Cedar Glen when fire "
                    "breached Rim of the World Hwy fire lines near Skyforest. "
                    "Community still recovering 20+ years later."
                ),
            },
            {
                "name": "Lake Arrowhead reservoir",
                "bearing": "center",
                "type": "water_feature",
                "notes": (
                    "184-acre private lake owned by Arrowhead Lake Association. "
                    "Provides limited fire break at community center and "
                    "emergency water supply for firefighting. However, lake "
                    "is not accessible to general public — gated access limits "
                    "its utility as a shelter-in-place refuge."
                ),
            },
            {
                "name": "Waterman Canyon / Old Waterman Canyon Rd",
                "bearing": "SW",
                "distance_mi": 5,
                "type": "canyon",
                "notes": (
                    "Canyon on southern face where Old Fire (2003) ignited "
                    "via arson. Steep terrain, dense chaparral. Fire ran "
                    "upslope from canyon through Arrowhead Springs and Del Rosa "
                    "neighborhoods before climbing to mountain communities."
                ),
            },
        ],
        "infrastructure_vulnerabilities": [
            {
                "type": "water_supply",
                "operator": "Lake Arrowhead CSD / CLAWA",
                "detail": (
                    "Water imported via Crestline-Lake Arrowhead Water Agency "
                    "(CLAWA) from Lake Silverwood via State Water Project — "
                    "pipeline runs through fire-prone terrain. Local "
                    "distribution system has aging steel mains with documented "
                    "leak problems (30,000-gallon leak in steel main, 216,000-"
                    "gallon leak on two-inch steel line). 420 fire hydrants "
                    "maintained by LACSD but flow rates vary — some hydrants "
                    "color-coded for GPM rating. Mountain terrain means gravity-"
                    "fed pressure is limited and pumping stations are vulnerable "
                    "to power loss during fire events."
                ),
            },
            {
                "type": "roads",
                "detail": (
                    "All access roads are two-lane mountain highways designed "
                    "for scenic tourism, not mass evacuation. SR-18 clings to "
                    "the rim of a 4,000 ft escarpment. No alternative routes. "
                    "Tree-fall from dead/beetle-killed conifers can block "
                    "roads with no detour options. Winter ice/snow closures "
                    "demonstrate the roads' vulnerability to any obstruction."
                ),
            },
            {
                "type": "power",
                "operator": "SCE / Bear Valley Electric",
                "detail": (
                    "Power lines run through dense forest on mountain roads. "
                    "Tree-fall onto lines is a constant ignition risk. Power "
                    "shutoffs (PSPS) during fire weather leave mountain "
                    "communities without power for pumping water, communications, "
                    "and medical equipment."
                ),
            },
        ],
        "historical_fires": [
            {
                "name": "Old Fire",
                "year": 2003,
                "acres": 91281,
                "structures_destroyed": 993,
                "deaths": 6,
                "detail": (
                    "Arson ignition in Waterman Canyon (Old Waterman Canyon Rd "
                    "at SR-18) on Oct 25, 2003. Driven by 50+ mph Santa Ana "
                    "winds. Spread exceeded 1,000 acres/hour initially. "
                    "Long-range spotting several miles ahead of flame front. "
                    "Forced evacuation of 80,000+ from ALL mountain communities "
                    "(Lake Arrowhead, Crestline, Running Springs, Cedar Glen). "
                    "Destroyed 324 homes in Cedar Glen alone when fire breached "
                    "Rim of the World Hwy fire lines. Part of 2003 Fire Siege "
                    "(15 simultaneous fires across SoCal). Arsonist Rickie Lee "
                    "Fowler convicted of murder, sentenced to death. Six deaths — "
                    "all from heart attacks caused by physical/emotional strain."
                ),
            },
            {
                "name": "Grass Valley Fire",
                "year": 2007,
                "acres": 1247,
                "structures_destroyed": 176,
                "deaths": 0,
                "detail": (
                    "Ignited Oct 22, 2007, one mile west of Lake Arrowhead. "
                    "Human-caused. Only 1,247 acres but destroyed 176 structures "
                    "and damaged 25 more. USFS study documented the 'domino "
                    "effect': firebrands ignited a few homes, then burning homes "
                    "ignited adjacent homes via radiant heat without the "
                    "wildfire front as a factor. Homes with wood shake roofs "
                    "and pine litter in gutters were primary ignition points. "
                    "Demonstrates that even a small fire in mountain community "
                    "dense housing can cause catastrophic structure loss."
                ),
            },
            {
                "name": "Slide Fire",
                "year": 2007,
                "acres": 12759,
                "structures_destroyed": 272,
                "deaths": 0,
                "detail": (
                    "Same day as Grass Valley Fire (Oct 22, 2007). Ignited "
                    "near Green Valley Lake/Running Springs. Destroyed 272 "
                    "homes and 3 outbuildings. Combined with Grass Valley Fire: "
                    "~450 structures destroyed in San Bernardino Mountains in "
                    "a single day."
                ),
            },
            {
                "name": "Line Fire",
                "year": 2024,
                "acres": 36539,
                "structures_destroyed": 35,
                "deaths": 0,
                "detail": (
                    "Ignited Sep 5, 2024 along Baseline Rd in Highland. "
                    "Grew to 36,000+ acres in San Bernardino National Forest. "
                    "Mandatory evacuation for Running Springs and Arrowbear "
                    "Lake; warnings for Lake Arrowhead, Crestline, Cedar Glen, "
                    "Valley of Enchantment. SR-18 closed northbound (inbound), "
                    "SR-330 closed entirely from Highland to Running Springs. "
                    "38,002 structures threatened (8,800 under evacuation "
                    "orders, 29,200 under warnings). One evacuee reported 7-hour "
                    "trip to reach evacuation center due to road congestion."
                ),
            },
        ],
        "fire_behavior_notes": (
            "Lake Arrowhead represents one of California's most dangerous "
            "evacuation scenarios: a mountain-top community of 12,000-40,000 "
            "(depending on season) accessible only by narrow two-lane mountain "
            "roads with hairpin turns, perched atop a 4,000 ft escarpment that "
            "amplifies fire behavior. The Old Fire (2003) demonstrated that "
            "fire can climb this escarpment at over 1,000 acres/hour with "
            "spotting miles ahead of the flame front. The Grass Valley Fire "
            "(2007) demonstrated that even a small fire can destroy hundreds "
            "of structures through the domino effect in dense mountain housing. "
            "The Line Fire (2024) demonstrated that evacuation takes HOURS — "
            "one resident reported 7 hours to descend. On a summer holiday "
            "weekend with 40,000 people on the mountain, mass evacuation via "
            "two-lane roads is functionally impossible in the time available "
            "when a wind-driven fire climbs the escarpment."
        ),
        "wui_class": "extreme",
    },

    # =========================================================================
    # CRESTLINE — Western rim, first in line, evacuation bottleneck
    # =========================================================================
    "crestline_ca": {
        "center": (34.2420, -117.2856),
        "elevation_ft": 4642,
        "population": 11650,
        "population_year": 2020,
        "seasonal_population_peak": 25000,
        "seasonal_population_notes": (
            "Permanent population 11,650 (2020 Census). Like Lake Arrowhead, "
            "significant vacation home and weekend visitor population. Centered "
            "around man-made Lake Gregory. Combined with adjacent communities "
            "(Cedarpines Park ~1,000, Valley of Enchantment, Twin Peaks), the "
            "western mountain rim communities total approximately 20,000+ "
            "permanent residents, swelling to 25,000+ on summer weekends. "
            "All share the same limited road network for evacuation."
        ),
        "median_age": None,
        "demographic_notes": (
            "Year-round mountain community — less seasonal than Lake Arrowhead "
            "but still significant visitor influx. Mix of retirees, families, "
            "and service workers. Many homes date to 1920s-1960s subdivisions "
            "(Cedarpines Park, Valley of Enchantment developed in 1920s) with "
            "construction that predates modern fire codes — wood frame, wood "
            "shake roofs, no defensible space. Lower-income demographic than "
            "Lake Arrowhead, with older housing stock more vulnerable to "
            "ember ignition."
        ),
        "terrain_notes": (
            "Mountain community (pop 11,650) on the WESTERN rim of the San "
            "Bernardino Mountains at 4,642 ft elevation. Sits on the very edge "
            "of the Rim of the World — dramatic 3,500+ ft escarpment dropping "
            "to San Bernardino Valley directly to the south. This is the FIRST "
            "mountain community that fire encounters when climbing the southern "
            "face from the San Bernardino Valley — it was hit before Lake "
            "Arrowhead during the Old Fire (2003). Dense pine/cedar forest with "
            "decades of fuel accumulation and extensive bark beetle mortality "
            "creating standing dead fuel. Crestline is also the critical "
            "evacuation BOTTLENECK for all mountain communities to the east — "
            "Lake Arrowhead, Running Springs, and Big Bear evacuees using "
            "SR-138 must pass THROUGH Crestline to reach I-15. If Crestline's "
            "roads are blocked, communities to the east are trapped."
        ),
        "evacuation_analysis": {
            "routes": [
                {
                    "name": "SR-138 (west/south toward I-15 / Cajon Pass)",
                    "direction": "W/S",
                    "lanes": 2,
                    "constraints": (
                        "Primary escape route descending to I-15 and the "
                        "high desert. Two-lane, winding mountain road. During "
                        "Old Fire (2003), the fire burned the east side below "
                        "Cedarpines Park and threatened to close I-15 at Cajon "
                        "Pass, leaving evacuees stranded on the north side of "
                        "the mountains. This is THE bottleneck for all western "
                        "mountain community evacuation."
                    ),
                },
                {
                    "name": "SR-18 (east toward Lake Arrowhead)",
                    "direction": "E",
                    "lanes": 2,
                    "constraints": (
                        "Rim of the World Drive connecting to Lake Arrowhead "
                        "and Running Springs. Two-lane. Goes DEEPER into "
                        "mountain communities, not toward safety. Only useful "
                        "if fire is approaching from west and eastern routes "
                        "(SR-18 east to Big Bear, SR-38 south to Redlands) are "
                        "still open — adding 60+ minutes to evacuation."
                    ),
                },
                {
                    "name": "Lake Drive / local surface streets",
                    "direction": "various",
                    "lanes": 2,
                    "constraints": (
                        "Narrow residential streets, many unpaved or poorly "
                        "maintained. Single-lane in some sections. Dead-end "
                        "streets throughout. Not viable for mass evacuation."
                    ),
                },
            ],
            "estimated_evacuation_time_hours": 4.0,
            "worst_case_scenario": (
                "Fire climbing southern escarpment from San Bernardino Valley "
                "(as in Old Fire 2003). Crestline, sitting on the western rim, "
                "is hit first. SR-138 down to I-15 is the only escape. But "
                "simultaneously, ALL mountain communities to the east — Lake "
                "Arrowhead (12,000-40,000), Running Springs, Cedar Glen, Twin "
                "Peaks — are also evacuating westward through Crestline. "
                "Combined evacuation demand: 30,000-60,000 people on a single "
                "two-lane mountain road. Old Fire forced evacuation of 80,000+ "
                "from all mountain communities. During Line Fire (2024), "
                "Crestline was under evacuation warning while Running Springs "
                "and Arrowbear Lake were under mandatory orders — creating "
                "bidirectional traffic conflicts on SR-18/SR-138."
            ),
        },
        "danger_quadrants": ["south", "southwest", "west"],
        "safe_quadrants": [],
        "key_features": [
            {
                "name": "San Bernardino Mountain western rim / escarpment",
                "bearing": "S",
                "distance_mi": 0.5,
                "type": "escarpment",
                "notes": (
                    "Extreme southern escarpment — 3,500+ ft vertical relief "
                    "from San Bernardino Valley floor to Crestline. Fire climbs "
                    "this face rapidly via slope-driven convection. Crestline "
                    "is literally on the rim — some properties sit within "
                    "hundreds of feet of the escarpment edge. Old Fire (2003) "
                    "climbed this face from Waterman Canyon at 1,000+ acres/hr. "
                    "The escarpment acts as a natural chimney, accelerating "
                    "fire upslope and launching embers onto the mountain-top "
                    "communities."
                ),
            },
            {
                "name": "Cedarpines Park",
                "bearing": "SW",
                "distance_mi": 1,
                "type": "community",
                "notes": (
                    "Adjacent community (~1,000 residents) on SR-138 below "
                    "Crestline. 1920s subdivision development predating fire "
                    "codes. Dense pine forest, narrow lots. Old Fire burned "
                    "the east side below Cedarpines Park. Community sits on "
                    "the evacuation route — if fire reaches Cedarpines Park, "
                    "the escape route (SR-138) is compromised."
                ),
            },
            {
                "name": "Valley of Enchantment",
                "bearing": "W",
                "distance_mi": 2,
                "type": "community",
                "notes": (
                    "Small community reached via SR-138 / Knapps Cut Off. "
                    "1920s subdivision development. Under evacuation warning "
                    "during Line Fire (2024). Limited access via narrow "
                    "mountain roads."
                ),
            },
            {
                "name": "Lake Gregory",
                "bearing": "center",
                "type": "water_feature",
                "notes": (
                    "Man-made lake (reservoir) at center of Crestline. Created "
                    "in late 1930s by damming Houston Creek. Provides a limited "
                    "fire break and emergency water source. County park "
                    "surrounds it — potential evacuation assembly point but "
                    "limited capacity. Not large enough to serve as meaningful "
                    "shelter-in-place buffer for the community."
                ),
            },
            {
                "name": "SR-138 / SR-18 junction",
                "bearing": "center",
                "type": "access_route",
                "notes": (
                    "Critical intersection connecting western mountain "
                    "evacuation route (SR-138 to I-15) with Rim of the World "
                    "Drive (SR-18 east to Lake Arrowhead). Bottleneck point "
                    "where traffic from multiple communities converges. Single "
                    "point of failure for entire western mountain evacuation."
                ),
            },
            {
                "name": "I-15 / Cajon Pass (destination)",
                "bearing": "W",
                "distance_mi": 12,
                "type": "freeway",
                "notes": (
                    "Destination freeway for evacuees descending SR-138. "
                    "Cajon Pass itself is a fire corridor — the Cajon Fire "
                    "has historically burned in this wind gap. If I-15 is "
                    "closed by fire at Cajon Pass (as nearly happened during "
                    "Old Fire), mountain evacuees have nowhere to go."
                ),
            },
        ],
        "infrastructure_vulnerabilities": [
            {
                "type": "water_supply",
                "operator": "Crestline-Lake Arrowhead Water Agency (CLAWA)",
                "detail": (
                    "Water imported from Lake Silverwood via State Water "
                    "Project pipeline running through fire-prone terrain. "
                    "Crestline Sanitation District manages local distribution. "
                    "Mountain terrain limits gravity-fed pressure. Power loss "
                    "during fire events (or PSPS shutoffs) disables pumping "
                    "stations, reducing hydrant pressure when it's needed most."
                ),
            },
            {
                "type": "roads",
                "detail": (
                    "SR-138 is the primary evacuation route and the critical "
                    "bottleneck for the entire western mountain zone. Two-lane, "
                    "winding, steep grades. No alternative routes. Many "
                    "residential streets are single-lane, unpaved, or dead-end. "
                    "1920s-era subdivisions (Cedarpines Park, Valley of "
                    "Enchantment) were platted without fire evacuation in mind."
                ),
            },
            {
                "type": "housing_stock",
                "detail": (
                    "Many homes built in 1920s-1960s before modern fire codes. "
                    "Wood frame construction, wood shake roofs, no ember-"
                    "resistant vents. Pine litter accumulation in gutters and "
                    "on roofs creates ignition pathways. USFS Grass Valley Fire "
                    "study (2007) documented the 'domino effect' in similar "
                    "mountain housing — burning homes ignite adjacent homes "
                    "through radiant heat. This building stock vulnerability "
                    "applies directly to Crestline's housing."
                ),
            },
        ],
        "historical_fires": [
            {
                "name": "Old Fire",
                "year": 2003,
                "acres": 91281,
                "structures_destroyed": 993,
                "deaths": 6,
                "detail": (
                    "Arson ignition in Waterman Canyon Oct 25, 2003. 50+ mph "
                    "Santa Ana winds. Forced evacuation of 80,000+ from ALL "
                    "mountain communities. One victim (Chad Leo Williams, 70) "
                    "died in Crestline from heart attack during evacuation. "
                    "Fire burned below Cedarpines Park, threatening SR-138 "
                    "evacuation route. Breached Rim of the World Hwy fire "
                    "lines near Skyforest, destroying 324 homes in Cedar Glen. "
                    "Part of 2003 Fire Siege. $1.2 billion damages."
                ),
            },
            {
                "name": "Slide Fire",
                "year": 2007,
                "acres": 12759,
                "structures_destroyed": 272,
                "deaths": 0,
                "detail": (
                    "Ignited Oct 22, 2007 near Green Valley Lake / Running "
                    "Springs area — adjacent to Crestline. Destroyed 272 homes. "
                    "Same day as Grass Valley Fire near Lake Arrowhead — "
                    "mountain communities hit by two fires simultaneously."
                ),
            },
            {
                "name": "Line Fire",
                "year": 2024,
                "acres": 36539,
                "structures_destroyed": 35,
                "deaths": 0,
                "detail": (
                    "Sep 2024. Crestline under evacuation WARNING while Running "
                    "Springs and Arrowbear Lake under mandatory orders. "
                    "Demonstrated that mountain evacuation creates cascading "
                    "traffic on SR-138 through Crestline even when Crestline "
                    "itself is not directly threatened."
                ),
            },
        ],
        "fire_behavior_notes": (
            "Crestline's fire vulnerability is defined by two compounding "
            "factors: (1) its position on the western rim of the escarpment "
            "makes it the FIRST community fire reaches when climbing from the "
            "San Bernardino Valley, and (2) its position on SR-138 makes it "
            "the evacuation BOTTLENECK for all communities to the east. A fire "
            "climbing the southern escarpment threatens Crestline directly "
            "while simultaneously forcing 20,000-40,000 people from Lake "
            "Arrowhead, Running Springs, and other eastern communities to "
            "evacuate THROUGH Crestline. The Old Fire (2003) demonstrated "
            "this exact scenario: fire on the escarpment below Crestline while "
            "80,000 mountain residents fled via limited routes. The 1920s-era "
            "housing stock, dense forest, bark beetle mortality, and decades "
            "of fuel accumulation create extreme structure ignition risk. A "
            "summer weekend fire during Santa Ana conditions represents a "
            "mass-casualty scenario with no adequate evacuation solution."
        ),
        "wui_class": "extreme",
    },
}
