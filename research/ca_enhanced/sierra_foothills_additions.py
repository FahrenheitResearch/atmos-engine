"""
Sierra Foothills Fire-Vulnerable City Additions
================================================

Research-paper-quality profiles for 7 additional fire-vulnerable communities
in California's Sierra Foothills region. These supplement the existing database
which already contains: Paradise, Magalia, Grass Valley, Nevada City, Wrightwood.

Data sourced from:
    - U.S. Census Bureau 2020 decennial census
    - CAL FIRE incident reports (River Fire 2021, Mosquito Fire 2022, Caldor Fire
      2021, King Fire 2014, Camp Fire 2018, North Complex/Bear Fire 2020)
    - NIST Camp Fire case study (TN 2135)
    - Butte County / El Dorado County / Placer County hazard mitigation plans
    - Georgetown Divide Public Utility District infrastructure assessments
    - Nevada Irrigation District (NID) Alta Sierra Reservoir replacement project docs
    - Foresthill Public Utility District service area documentation
    - CapRadio / SFChronicle / ABC10 investigative reporting
    - Cal Fire FHSZ (Fire Hazard Severity Zone) mapping
    - Caltrans highway lane inventories
    - USGS / topographic-map.com elevation data
    - Washington Post / CapRadio Sierra Foothills vulnerability reporting (2018-2019)
    - Yankee Hill Fire Safe Council annex to Butte County LHMP (2024)
"""

SIERRA_FOOTHILLS_ADDITIONS = {

    # =========================================================================
    # 1. ALTA SIERRA, CA -- PRIORITY TARGET
    #    "One of the most likely to burn down" per fire weather meteorologists
    # =========================================================================
    "alta_sierra_ca": {
        "center": [39.1416, -121.0538],
        "terrain_notes": (
            "Census-designated place (pop. 7,204, 2020 census) on a forested ridge "
            "between the Bear River drainage to the south and Greenhorn Creek to the "
            "north/east, in western Nevada County. Elevation averages ~2,300 ft with "
            "the ridge crest near 2,500 ft, dropping 400-600 ft into surrounding "
            "drainages. Dense mixed conifer and hardwood forest (ponderosa pine, "
            "Douglas fir, incense cedar, black oak, live oak) with heavy understory "
            "fuel loading -- much of the area has not experienced fire in 50+ years. "
            "The community was built in the 1960s-1980s as a subdivision carved into "
            "continuous forest, with winding roads, cul-de-sacs, and homes set among "
            "dense tree canopy. The road network is labyrinthine: crooked foothill "
            "roads wind through the forested neighborhood, and it is easy to become "
            "disoriented even without smoke. Fire weather meteorologists have "
            "specifically identified Alta Sierra as 'one of the most likely to burn "
            "down' communities in the Sierra Foothills -- it shares the same fire "
            "weather regime, vegetation type, and WUI geometry as pre-2018 Paradise "
            "but sits on an even narrower ridge with fewer evacuation options. "
            "Nevada County conducted emergency evacuation drills here in 2019, "
            "identifying it as one of the two most vulnerable communities in the "
            "county (along with Lake Wildwood). PG&E Public Safety Power Shutoffs "
            "(PSPS) affect the area multiple times per fire season, and mobile home "
            "park residents on master meters do not receive individual PSPS "
            "notifications -- a critical communication gap identified by local "
            "reporting."
        ),
        "key_features": [
            "Forested ridge between Bear River and Greenhorn Creek drainages",
            "Labyrinthine subdivision roads with cul-de-sacs carved into dense forest",
            "Same fire weather regime as Paradise (NE foehn/Diablo-like winds)",
            "No recent fire history -- heavy fuel accumulation over 50+ years",
            "NID (Nevada Irrigation District) water supply with aging infrastructure",
            "Alta Sierra Reservoir (1976) with deteriorating Hypalon liner",
            "PG&E PSPS notification gap for mobile home park master-meter residents",
            "Identified by Nevada County OES as one of top 2 vulnerable communities",
            "Dense mixed conifer/hardwood canopy closes over roads creating ember tunnels",
            "Proximity to Grass Valley/Nevada City fire corridor but isolated access",
        ],
        "elevation_range_ft": [1800, 2500],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "49 Fire",
                "year": 2009,
                "acres": 80,
                "details": (
                    "Grass fire near Highway 49 and Alta Sierra Drive that "
                    "demonstrated the rapid spread potential in the area's "
                    "dry grass and brush. Quickly contained but served as a "
                    "warning for the community."
                ),
            },
            {
                "name": "River Fire",
                "year": 2021,
                "acres": 2619,
                "details": (
                    "Burned near Bear River west of Colfax, 10 mi south of Alta "
                    "Sierra. Destroyed 142 structures. Same Bear River drainage "
                    "system; demonstrated fire spread potential in the corridor."
                ),
            },
            {
                "name": "Jones Fire",
                "year": 2015,
                "acres": 305,
                "details": (
                    "Burned in Nevada County near Grass Valley. Forced evacuations "
                    "in the greater Grass Valley area. Demonstrated vulnerability "
                    "of the broader Nevada County foothill communities."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Alta Sierra Drive to SR 49",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "Primary egress. Narrow, winding 2-lane road through dense "
                    "forest for ~3 miles to Highway 49. No shoulders, no turnouts. "
                    "During an active fire, this road would be flanked by burning "
                    "forest on both sides. Merge onto SR 49 is a T-intersection, "
                    "not an interchange -- creates bottleneck under mass evacuation."
                ),
                "risk": (
                    "Extreme. Single primary route for 7,000+ residents. Road "
                    "winds through continuous forest canopy that would create "
                    "ember tunnels and radiant heat exposure during fire."
                ),
            },
            {
                "route": "Dog Bar Road / You Bet Road",
                "direction": "S/SE",
                "lanes": 2,
                "bottleneck": (
                    "Secondary escape via narrow mountain roads dropping south "
                    "toward Bear River and eventually Colfax/I-80. Extremely "
                    "steep, winding, and narrow -- not suitable for mass evacuation. "
                    "Portions are single-lane with pullouts."
                ),
                "risk": (
                    "High. These roads drop into the Bear River canyon, which "
                    "is itself a fire corridor. Evacuees heading south into the "
                    "canyon could drive directly into a fire approaching from "
                    "the south or southwest."
                ),
            },
            {
                "route": "Local subdivision roads to Grass Valley",
                "direction": "N/NW",
                "lanes": 2,
                "bottleneck": (
                    "Network of winding residential streets connecting north "
                    "toward Grass Valley via various routes. Confusing network "
                    "of unnamed roads and cul-de-sacs. Residents unfamiliar "
                    "with alternative routes may become trapped."
                ),
                "risk": (
                    "Moderate to high. Routes are circuitous and unsigned. "
                    "In smoke conditions, navigation would be extremely difficult. "
                    "Color-coded evacuation route signs were proposed in 2019 but "
                    "implementation has been slow."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "NE foehn winds (Diablo-like). Dry northeasterly flow from the "
                "Great Basin descends the western Sierra slope, warming and drying "
                "adiabatically. At Alta Sierra's 2,300 ft elevation, these events "
                "produce sustained winds of 25-40 mph with gusts to 55+ mph, RH "
                "dropping below 10%, and temperatures spiking 10-15F above normal. "
                "Events most common Oct-Dec but can occur Sep-Jan."
            ),
            "critical_corridors": [
                "Bear River Canyon (S/SW approach -- upslope fire runs toward ridge)",
                "Greenhorn Creek drainage (N/NE approach -- wind-driven during foehn events)",
                "Highway 49 corridor (grass/brush fires can climb from roadside into forest)",
                "Wolf Creek drainage (SE approach connecting to broader American River watershed)",
            ],
            "rate_of_spread_potential": (
                "Extreme in grass/brush fuels at lower elevations (80-150 chains/hr "
                "in Diablo wind events). Moderate to high in continuous mixed conifer "
                "canopy (20-60 chains/hr) with potential for crown fire runs on steep "
                "slopes above Bear River. Ember transport distances of 0.5-2 mi "
                "expected given terrain-channeled winds."
            ),
            "spotting_distance": (
                "0.5-2.0 miles in moderate wind events; up to 3+ miles in extreme "
                "NE wind events given the terrain channeling through Bear River and "
                "Greenhorn Creek drainages. Dense conifer canopy provides abundant "
                "firebrands (bark plates, pine cones) for long-range spotting."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Served by Nevada Irrigation District (NID). The Alta Sierra "
                "Reservoir (3 million gallon capacity, built 1976) has a deteriorating "
                "Hypalon liner nearing end of useful life, with increasing risk of "
                "contamination from leaks. NID has allocated funding for a reservoir "
                "replacement project but construction timeline extends years out. "
                "Distribution system relies on gravity-fed pressure from the "
                "reservoir; if the reservoir fails or is compromised by fire, water "
                "pressure for firefighting drops to zero. No backup supply."
            ),
            "power": (
                "PG&E overhead distribution lines through dense forest canopy. "
                "Subject to frequent PSPS de-energization during fire weather events "
                "(multiple times per fire season). Potential PSPS events can affect "
                "~7,345 customers across Nevada County. Mobile home parks on master "
                "meters receive NO individual PG&E notification of shutoffs -- "
                "residents may lose power without warning. Medical baseline customers "
                "may not be reached for in-person notification."
            ),
            "communications": (
                "Limited cell coverage in canyon areas surrounding the ridge. "
                "PG&E PSPS events knock out cell towers without backup generators. "
                "Nevada County has invested in AlertWildfire camera network but "
                "notification systems depend on cell/internet connectivity that may "
                "be unavailable during combined fire + PSPS events."
            ),
            "medical": (
                "No medical facilities within the community. Nearest hospital is "
                "Sierra Nevada Memorial Hospital in Grass Valley, ~7 miles by road. "
                "Significant elderly population with mobility limitations. During a "
                "fire, the evacuation route to the hospital would likely be through "
                "or near the fire zone."
            ),
        },
        "demographics_risk_factors": {
            "population": 7204,
            "seasonal_variation": (
                "Modest summer increase from vacation properties and seasonal "
                "residents. Population fairly stable year-round as primarily a "
                "residential/retirement community."
            ),
            "elderly_percentage": "~22% age 65+",
            "mobile_homes": (
                "Multiple mobile home parks within the CDP, housing a significant "
                "portion of the elderly population. Mobile homes are extremely "
                "vulnerable to ember intrusion and radiant heat. Master-meter "
                "billing means residents are invisible to PG&E's PSPS notification "
                "system -- a documented and unresolved safety gap."
            ),
            "special_needs_facilities": (
                "No dedicated senior care facilities within Alta Sierra. Elderly "
                "residents dependent on home medical equipment (oxygen concentrators, "
                "CPAP, etc.) are at extreme risk during PSPS events and evacuations."
            ),
        },
    },

    # =========================================================================
    # 2. COLFAX, CA -- I-80 Corridor, Steep Ravines
    # =========================================================================
    "colfax_ca": {
        "center": [39.1007, -120.9533],
        "terrain_notes": (
            "Small city (pop. 1,995, 2020 census) at the crossroads of Interstate 80 "
            "and State Route 174 in Placer County, where I-80 begins its climb into "
            "the Sierra Nevada. Elevation ~2,425 ft. The town sits on a narrow ridge "
            "between steep ravines cut by the Bear River to the south, Canyon Creek, "
            "and numerous smaller drainages. The surrounding terrain is deeply "
            "dissected -- ravines drop 500-800 ft within a mile of the town center. "
            "Vegetation transitions from grass/oak woodland at lower elevations to "
            "mixed conifer (ponderosa pine, Douglas fir, black oak) on the ridge and "
            "in the ravines. The I-80 corridor through Colfax narrows to what locals "
            "call the 'Colfax Narrows' -- a constricted section where the freeway, "
            "rail corridor (historic Central Pacific / Union Pacific mainline), and "
            "town are squeezed onto the ridge between canyons. This concentration of "
            "infrastructure on a narrow ridge above steep, fuel-laden ravines creates "
            "extreme vulnerability. The 2021 River Fire demonstrated this: igniting "
            "at a campground on the Bear River west of town, it burned 2,619 acres "
            "and destroyed 142 structures before containment, forcing evacuation of "
            "the entire city and 7,000+ people across Nevada and Placer counties."
        ),
        "key_features": [
            "I-80 / SR 174 crossroads on narrow ridge between deep ravines",
            "Bear River canyon to south -- 2021 River Fire origin point",
            "Canyon Creek and Long Ravine flank the town on multiple sides",
            "Historic railroad corridor (Union Pacific mainline) through town center",
            "Colfax Fire Station documented 22 vegetation fires along I-80 corridor",
            "Hot-summer Mediterranean climate: 90F+ July/Aug with very low RH",
            "Rollins Lake Road provides secondary access to SR 174",
            "Gateway between Sacramento Valley and Sierra Nevada -- wind funnel",
        ],
        "elevation_range_ft": [1600, 2600],
        "wui_exposure": "high",
        "historical_fires": [
            {
                "name": "River Fire",
                "year": 2021,
                "acres": 2619,
                "details": (
                    "Ignited Aug 4 at Bear River campground west of Colfax. Human-caused. "
                    "Burned 2,619 acres in Placer and Nevada counties. Destroyed 142 "
                    "structures (102 single-family homes, 1 commercial, 39 outbuildings), "
                    "damaged 21 more. Forced evacuation of entire city of Colfax and "
                    "7,000+ people. Terrain and drought-stressed fuels enabled rapid "
                    "uphill spread from the Bear River canyon toward the ridge-top town. "
                    "Contained Aug 13."
                ),
            },
            {
                "name": "Lowell Fire",
                "year": 2015,
                "acres": 2038,
                "details": (
                    "Burned in Nevada County near Rollins Lake, just north of Colfax. "
                    "Forced evacuations in the SR 174 corridor. Demonstrated fire spread "
                    "potential in the ravine systems connecting Colfax to surrounding "
                    "wildlands."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Interstate 80 westbound",
                "direction": "W",
                "lanes": 4,
                "bottleneck": (
                    "Primary evacuation route toward Auburn and Sacramento. I-80 is "
                    "4 lanes (2 each direction) through the Colfax area but narrows "
                    "at the Colfax Narrows where the freeway, railroad, and town "
                    "are compressed onto the ridge. During River Fire, I-80 was "
                    "used for evacuation but traffic congestion was severe."
                ),
                "risk": (
                    "Moderate. I-80 provides high-capacity evacuation but the "
                    "Colfax Narrows constrain capacity. A fire burning from the "
                    "Bear River canyon to the south could push smoke and flames "
                    "directly across or adjacent to I-80."
                ),
            },
            {
                "route": "Interstate 80 eastbound",
                "direction": "E",
                "lanes": 4,
                "bottleneck": (
                    "Eastbound toward Emigrant Gap and Donner Pass. Gains elevation "
                    "rapidly. During winter, chains may be required, but fire season "
                    "this route is viable. Leads further into forest, which may not "
                    "be advisable during a large fire."
                ),
                "risk": (
                    "Moderate. Route climbs into denser forest and higher elevations, "
                    "potentially driving evacuees into worse fire conditions."
                ),
            },
            {
                "route": "SR 174 northbound to Grass Valley",
                "direction": "N",
                "lanes": 2,
                "bottleneck": (
                    "Two-lane highway running 13 miles north through the western "
                    "Sierra foothills to Grass Valley/SR 20/SR 49 junction. Follows "
                    "the old Lincoln Highway alignment. Narrow, winding, no shoulders "
                    "for most of its length. Passes through forest and rural areas."
                ),
                "risk": (
                    "High. Narrow 2-lane road through forest with no alternative "
                    "if blocked by fire. During River Fire, this corridor was "
                    "threatened. Connects to additional at-risk communities "
                    "(Grass Valley, Nevada City, Alta Sierra)."
                ),
            },
            {
                "route": "Rollins Lake Road / Canyon Way",
                "direction": "N/NW",
                "lanes": 2,
                "bottleneck": (
                    "Local roads providing alternative access to SR 174 corridor. "
                    "Narrow, rural, no capacity for mass evacuation. Drops into "
                    "ravines before climbing back to the ridge."
                ),
                "risk": (
                    "High. Roads pass through canyons with heavy fuel loads. "
                    "Could be cut off by fire simultaneously with SR 174."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Terrain-channeled upslope/downslope winds through Bear River and "
                "Canyon Creek ravines. During NE foehn events, winds accelerate "
                "through the ravine systems and up the steep canyon walls toward the "
                "ridge-top town. Afternoon upslope thermal winds during summer create "
                "daily fire weather windows (1400-1800 PDT) with RH below 15%."
            ),
            "critical_corridors": [
                "Bear River canyon (S -- upslope fire runs directly at town, as in River Fire 2021)",
                "Canyon Creek / Long Ravine (W/NW -- steep-sided ravines channeling fire toward I-80 corridor)",
                "I-80 right-of-way (ignition risk from vehicles, sparks from railroad, power lines)",
                "SR 174 corridor toward Rollins Lake (N -- continuous forest fuel bed)",
            ],
            "rate_of_spread_potential": (
                "Extreme in grass/brush fuels on canyon slopes (100-200 chains/hr "
                "during wind events). The 2021 River Fire demonstrated rapid upslope "
                "runs from the Bear River canyon bottom to the ridge in drought-stressed "
                "fuels. Moderate in mixed conifer (30-60 chains/hr). The steep terrain "
                "geometry (500-800 ft ravines) creates a chimney effect amplifying "
                "upslope spread rates by 2-3x."
            ),
            "spotting_distance": (
                "0.5-1.5 miles typical. Embers lofted from ravine fires land on the "
                "ridge top, igniting structures. The 2021 River Fire produced extensive "
                "spotting ahead of the main front."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "City of Colfax municipal water system. Limited storage capacity "
                "for a simultaneous structure protection and civilian supply scenario. "
                "System depends on treated water from limited reservoir capacity."
            ),
            "power": (
                "PG&E overhead distribution and transmission lines through forest "
                "and along I-80 corridor. Subject to PSPS de-energization. Union "
                "Pacific railroad mainline creates additional spark/ignition risk "
                "during dry conditions."
            ),
            "communications": (
                "Adequate cell coverage along I-80 corridor but degraded in "
                "surrounding ravines. Canyon terrain creates radio shadows. During "
                "River Fire, communications were strained by volume of 911 calls "
                "and evacuation notifications."
            ),
            "medical": (
                "No hospital in Colfax. Nearest hospital is Sutter Auburn Faith "
                "Hospital in Auburn, ~18 miles west on I-80. Fire station in town "
                "but limited staffing for simultaneous fire suppression and EMS."
            ),
        },
        "demographics_risk_factors": {
            "population": 1995,
            "seasonal_variation": (
                "Modest increase during summer recreation season due to Rollins Lake "
                "visitors and campground use along Bear River. Campground-related "
                "ignitions are a documented risk (River Fire origin)."
            ),
            "elderly_percentage": "~18% age 65+",
            "mobile_homes": (
                "Mobile home parks present in and around Colfax. Structures are "
                "vulnerable to ember intrusion and radiant heat. Low-income residents "
                "may lack resources for evacuation or hardening."
            ),
            "special_needs_facilities": (
                "No dedicated senior care or special needs facilities. Small-town "
                "resources are limited for assisting mobility-impaired residents "
                "during rapid evacuation."
            ),
        },
    },

    # =========================================================================
    # 3. FORESTHILL, CA -- Remote Peninsula Ridge Above American River
    # =========================================================================
    "foresthill_ca": {
        "center": [39.0202, -120.8180],
        "terrain_notes": (
            "Unincorporated community (pop. 1,692, 2020 census) perched on a broad "
            "ridge -- the Foresthill Divide -- between the North Fork and Middle Fork "
            "of the American River in Placer County. Elevation ~3,228 ft. The "
            "community sits on an ancient gold-bearing river gravel bed atop a "
            "geological peninsula: the ridge narrows and drops off steeply on three "
            "sides into canyons with 2,000+ ft of relief. Access is essentially via a "
            "single road -- Foresthill Road -- which runs 17 miles west from the "
            "community to Auburn and I-80, crossing the 730-ft-high Auburn-Foresthill "
            "Bridge over the North Fork American River. This bridge, the tallest in "
            "California, is the critical lifeline: if Foresthill Road or the bridge "
            "is closed by fire, the only alternatives are two dirt roads through steep "
            "canyon terrain -- essentially impassable for mass evacuation. The 2022 "
            "Mosquito Fire (76,788 acres, largest CA fire of 2022) burned out of the "
            "Middle Fork American River canyon and threatened Foresthill directly, "
            "forcing evacuation of ~11,000 people from Foresthill, Georgetown, and "
            "surrounding communities. The fire destroyed 78 structures in the area "
            "and took 46 days to contain. Firefighters described 'extremely steep and "
            "inaccessible terrain' in the canyon systems. The community has multiple "
            "mobile home parks (4+ parks with 40-134 sites each, oldest dating to "
            "1960) housing vulnerable populations."
        ),
        "key_features": [
            "Geological peninsula ridge -- steep drop-offs on 3 sides into 2,000+ ft canyons",
            "Single paved access: Foresthill Road (17 mi to Auburn/I-80)",
            "Auburn-Foresthill Bridge: tallest bridge in CA (730 ft), critical lifeline",
            "North Fork American River canyon to north (2,000+ ft relief)",
            "Middle Fork American River canyon to south (2,500+ ft relief)",
            "2022 Mosquito Fire origin: Oxbow Reservoir on Middle Fork",
            "Ancient gold mining area -- deep gravel beds, altered hydrology",
            "Multiple mobile home parks (4+, 40-134 sites each, 1960s vintage)",
            "Foresthill Public Utility District -- 2,034 water connections",
            "Dense mixed conifer forest: ponderosa pine, Douglas fir, white fir, incense cedar",
        ],
        "elevation_range_ft": [2800, 3600],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Mosquito Fire",
                "year": 2022,
                "acres": 76788,
                "details": (
                    "Largest California wildfire of 2022. Ignited Sep 6 on north shore "
                    "of Oxbow Reservoir in Middle Fork American River drainage. Burned "
                    "76,788 acres in Placer and El Dorado counties across Tahoe and "
                    "Eldorado National Forests. Destroyed 78 structures in Michigan "
                    "Bluff, Foresthill, and Volcanoville. Forced evacuation of ~11,000 "
                    "residents. Burned in 'extremely steep and inaccessible terrain' "
                    "for 46 days before full containment on Oct 22. Jumped the American "
                    "River and advanced on Foresthill from the south."
                ),
            },
            {
                "name": "Bridge Fire",
                "year": 2021,
                "acres": 411,
                "details": (
                    "Burned directly under the Auburn-Foresthill Bridge in Sep 2021. "
                    "Arson-caused. Demonstrated the vulnerability of the single "
                    "critical access point -- a fire at the bridge effectively cuts "
                    "off Foresthill from any high-capacity evacuation route. Burned "
                    "411 acres and caused temporary road closures."
                ),
            },
            {
                "name": "Foresthill Fire (Trailhead Fire)",
                "year": 2016,
                "acres": 130,
                "details": (
                    "Wildfire near Foresthill that prompted evacuations. Demonstrated "
                    "the rapid response challenges given the remote single-road access."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Foresthill Road westbound to Auburn / I-80",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "THE critical evacuation route. 17-mile, 2-lane mountain road "
                    "winding along the ridge to Auburn, crossing the 730-ft-high "
                    "Auburn-Foresthill Bridge. No shoulders for most of its length. "
                    "Steep grades, sharp curves, and forest canopy on both sides. "
                    "If fire reaches Foresthill Road at any point along its 17-mile "
                    "length, the community is cut off from its only viable evacuation "
                    "route. During the 2022 Mosquito Fire, residents were escorted "
                    "by law enforcement on Foresthill Road subject to fire conditions."
                ),
                "risk": (
                    "Extreme. Single point of failure. 1,692+ residents dependent "
                    "on one 17-mile, 2-lane road. The bridge itself is a choke point: "
                    "the 2021 Bridge Fire burned directly beneath it, demonstrating "
                    "that an arson or accidental fire could simultaneously cut off "
                    "evacuation and destroy critical infrastructure."
                ),
            },
            {
                "route": "Mosquito Ridge Road / secondary dirt roads",
                "direction": "E/NE",
                "lanes": 1,
                "bottleneck": (
                    "Narrow dirt/gravel forest roads leading east deeper into the "
                    "Sierra Nevada (toward French Meadows, Hell Hole Reservoir). "
                    "Single-lane, steep, winding, no services. Essentially unusable "
                    "for mass evacuation -- leads further from civilization into "
                    "National Forest. Only viable for individual vehicles with "
                    "high clearance and local knowledge."
                ),
                "risk": (
                    "Extreme. These roads lead into the wilderness, not toward "
                    "safety. Evacuees would be driving deeper into forest with "
                    "no services, cell coverage, or population centers."
                ),
            },
            {
                "route": "Yankee Jims Road to canyon bottom",
                "direction": "N",
                "lanes": 1,
                "bottleneck": (
                    "Steep, narrow, partially unpaved road dropping into the North "
                    "Fork American River canyon. Historic gold mining road. Not "
                    "suitable for standard vehicles or mass evacuation. Gains/loses "
                    "2,000 ft of elevation in a few miles."
                ),
                "risk": (
                    "Extreme. Canyon-bottom roads are death traps during fire. "
                    "This route would only be used as an absolute last resort."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Complex terrain-driven winds. Canyon winds from both the North Fork "
                "and Middle Fork drainages create convergent upslope flow on the "
                "Foresthill Divide ridge during afternoon heating. NE foehn events "
                "produce strong downslope winds channeling through the American River "
                "canyons. The deep canyons (2,000+ ft) create extreme pre-heating "
                "on steep slopes, enabling explosive upslope fire runs from canyon "
                "bottoms to the ridge top."
            ),
            "critical_corridors": [
                "Middle Fork American River canyon (S -- Mosquito Fire approach vector 2022)",
                "North Fork American River canyon (N -- Bridge Fire 2021 approach)",
                "Foresthill Road corridor (W -- single evacuation route, flanked by forest)",
                "Oxbow Reservoir / Volcanoville drainage (SE -- fire approach from Eldorado NF)",
            ],
            "rate_of_spread_potential": (
                "Extreme on steep canyon slopes (100-300 chains/hr during upslope "
                "runs). The Mosquito Fire demonstrated multi-day runs through "
                "'extremely steep and inaccessible terrain' where direct attack "
                "was impossible. Crown fire potential is high in the dense mixed "
                "conifer stands on the ridge. Moderate to high along the ridge top "
                "(20-50 chains/hr in timber fuels). The 2,000+ ft of canyon relief "
                "creates massive pre-heating zones that can accelerate fire spread "
                "rates far beyond flat-ground predictions."
            ),
            "spotting_distance": (
                "1-3 miles. The deep canyons create powerful convection columns "
                "that loft firebrands to extreme heights. Embers carried by terrain-"
                "channeled winds can cross the 1-2 mile wide ridge and ignite spots "
                "on the opposite canyon slope. During Mosquito Fire, fire jumped the "
                "entire American River canyon."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Foresthill Public Utility District (FPUD), formed 1950, operates "
                "2,034 water service connections. Water treatment and distribution "
                "depend on infrastructure that is 50+ years old in places. System "
                "capacity is limited for simultaneous firefighting water demand and "
                "civilian supply. Remote location means mutual aid response times "
                "are long (30+ min from Auburn)."
            ),
            "power": (
                "PG&E overhead lines along Foresthill Road -- the single power "
                "supply corridor mirrors the single road access. A fire along "
                "Foresthill Road could simultaneously cut power and evacuation "
                "route. Subject to PSPS de-energization during fire weather."
            ),
            "communications": (
                "Limited cell coverage on the Divide; effectively zero in surrounding "
                "canyons. Satellite phone or ham radio may be the only communication "
                "during a combined fire + power outage. AlertWildfire cameras provide "
                "remote monitoring but local notification depends on cell/internet."
            ),
            "medical": (
                "No hospital, no urgent care. Foresthill Fire Protection District "
                "provides first response but is a volunteer/paid-call department "
                "with limited resources. Nearest hospital is Sutter Auburn Faith "
                "in Auburn, 20+ miles and 30+ minutes away via Foresthill Road -- "
                "assuming the road is open."
            ),
        },
        "demographics_risk_factors": {
            "population": 1692,
            "seasonal_variation": (
                "Significant summer increase from recreation visitors to American "
                "River canyon, Foresthill Divide trails, and OHV areas. French "
                "Meadows and Hell Hole reservoirs draw campers through Foresthill "
                "on the single access road."
            ),
            "elderly_percentage": "~23% age 65+",
            "mobile_homes": (
                "Four or more mobile home parks totaling 200+ sites, with the "
                "oldest dating to 1960-1962. Mobile homes constitute a significant "
                "fraction of local housing stock. These structures are highly "
                "vulnerable to ember intrusion and have limited structural resistance "
                "to radiant heat. Many elderly residents live in these parks."
            ),
            "special_needs_facilities": (
                "No dedicated senior care, assisted living, or special needs "
                "facilities. Remote location and single-road access make "
                "emergency medical transport extremely challenging."
            ),
        },
    },

    # =========================================================================
    # 4. POLLOCK PINES, CA -- Highway 50 Corridor, El Dorado NF
    # =========================================================================
    "pollock_pines_ca": {
        "center": [38.7614, -120.5891],
        "terrain_notes": (
            "Census-designated place (pop. 7,112, 2020 census) straddling U.S. "
            "Highway 50 in El Dorado County, approximately 13 miles east of "
            "Placerville and 58 miles east of Sacramento. Elevation ~3,980 ft. "
            "The community is embedded within the Eldorado National Forest at the "
            "transition from Sierra foothill woodland to montane conifer forest. "
            "Terrain is moderately steep, with the South Fork American River drainage "
            "to the north and the Cosumnes River headwaters to the south. Pollock "
            "Pines has been threatened or directly impacted by two of California's "
            "most significant wildfires: the 2014 King Fire (97,717 acres, arson-caused, "
            "$100M+ suppression cost) and the 2021 Caldor Fire (221,835 acres), which "
            "forced mandatory evacuation of the entire community. During Caldor, the "
            "fire burned to within 2 miles of Pollock Pines before prescribed burn "
            "treatments on the 'Fire Adapted 50' project area slowed its advance and "
            "protected the community. Highway 50 is the lifeline and the bottleneck: "
            "it narrows from a 4-lane divided highway west of Placerville to a 2-lane "
            "undivided highway through the Pollock Pines area, creating extreme "
            "congestion during evacuations. During Caldor, a nearly 50-mile closure "
            "of Highway 50 from Sly Park Road to Meyers stranded communities east of "
            "the fire."
        ),
        "key_features": [
            "Highway 50 corridor: 4-lane divided W of Placerville, 2-lane through Pollock Pines",
            "Embedded within Eldorado National Forest -- surrounded by continuous forest",
            "Sly Park Reservoir (Jenkinson Lake) -- major recreation/water supply 3 mi S",
            "Fire Adapted 50 fuel treatment project -- proved effective during Caldor Fire",
            "Transition zone: foothill woodland to montane conifer forest at 4,000 ft",
            "King Fire (2014) burned 97,717 acres from arson ignition at King of the Mountain Road",
            "Caldor Fire (2021) burned 221,835 acres, forced full evacuation of community",
            "Multiple mobile home parks (9.6% of housing stock)",
            "El Dorado County Fire Protection District coverage",
        ],
        "elevation_range_ft": [3400, 4400],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Caldor Fire",
                "year": 2021,
                "acres": 221835,
                "details": (
                    "Ignited Aug 14 near Little Mountain, south of Pollock Pines. "
                    "Burned 221,835 acres across El Dorado, Amador, and Alpine "
                    "counties. On Aug 17, mandatory evacuations were ordered for "
                    "Pollock Pines, Sly Park, Grizzly Flats, and Somerset. Fire "
                    "grew from 6,500 acres to 30,000 acres in a single day driven "
                    "by high winds. By Aug 20, fire reached Highway 50, forcing "
                    "its closure. Fire eventually crossed Highway 50 near Kyburz and "
                    "advanced to within 5 miles of South Lake Tahoe. The Fire Adapted "
                    "50 prescribed burn project is credited with slowing the fire's "
                    "advance and protecting Pollock Pines structures. Caldor destroyed "
                    "over 1,000 structures overall, including the near-total destruction "
                    "of Grizzly Flats (pop. ~1,200). Contained Oct 21."
                ),
            },
            {
                "name": "King Fire",
                "year": 2014,
                "acres": 97717,
                "details": (
                    "Arson fire ignited Sep 13 along King of the Mountain Road in "
                    "Pollock Pines. Burned 97,717 acres primarily in Eldorado National "
                    "Forest. Suppression cost exceeded $100 million and engaged 8,000+ "
                    "personnel at peak. Most of the forest burned had no recent fire "
                    "history, with the last major fire being the 1992 Cleveland Fire "
                    "(22,500 acres). King Fire forced evacuations along the Highway 50 "
                    "corridor and demonstrated the extreme fire behavior possible in "
                    "these fuel-heavy forests."
                ),
            },
            {
                "name": "Cleveland Fire",
                "year": 1992,
                "acres": 22500,
                "details": (
                    "Last major fire in the area before the King Fire. Burned ~22,500 "
                    "acres in the Eldorado National Forest, establishing the baseline "
                    "for 22+ years of fuel accumulation that made the King Fire so "
                    "devastating."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "US Highway 50 westbound toward Placerville/Sacramento",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "Primary evacuation route. Highway 50 is only 2 lanes (undivided) "
                    "through the Pollock Pines area, expanding to 4-lane divided west "
                    "of Placerville. This lane reduction is the critical bottleneck: "
                    "7,000+ residents plus highway through-traffic compress into 2 "
                    "lanes. During Caldor Fire, evacuation traffic from Pollock Pines "
                    "traveled westbound on Highway 50 with severe congestion."
                ),
                "risk": (
                    "Extreme. The 2-lane section creates a severe capacity constraint. "
                    "During Caldor, Highway 50 was eventually closed entirely (Sly Park "
                    "Road to Meyers, ~50 miles) as fire crossed the highway."
                ),
            },
            {
                "route": "Sly Park Road southbound to Mormon Emigrant Trail / Hwy 88",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Secondary evacuation route. 2-lane road running 5 miles south to "
                    "Mormon Emigrant Trail (Iron Mountain Road), then to Highway 88 via "
                    "a 30+ mile winding mountain route. Narrow, steep, and slow. "
                    "Used as official detour when Highway 50 was closed during Caldor."
                ),
                "risk": (
                    "High. Long, winding detour through forest. The Caldor Fire burned "
                    "across portions of this route. Not viable for rapid mass evacuation "
                    "-- adds 2+ hours to reach Sacramento compared to Highway 50 direct."
                ),
            },
            {
                "route": "US Highway 50 eastbound toward Tahoe",
                "direction": "E",
                "lanes": 2,
                "bottleneck": (
                    "Eastbound escape toward Kyburz, Echo Summit, and South Lake Tahoe. "
                    "2 lanes, mountain grades, and during Caldor Fire, this route was "
                    "completely closed as fire burned across Highway 50 near Kyburz. "
                    "Driving east during a Caldor-type event means driving toward "
                    "the fire."
                ),
                "risk": (
                    "Extreme during major fires. Route leads deeper into National "
                    "Forest and toward higher elevations with no alternative roads."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Afternoon upslope thermal winds from the Sacramento Valley drive "
                "fire spread from SW to NE up the Highway 50 corridor during summer. "
                "NE foehn (Diablo-like) events in fall produce strong downslope winds "
                "that can push fire rapidly from E to W. The Caldor Fire's explosive "
                "growth was driven by a combination of low humidity, high temperatures, "
                "and terrain-channeled winds through the South Fork American River and "
                "Cosumnes River drainages."
            ),
            "critical_corridors": [
                "Highway 50 corridor (E-W axis -- fire can approach from either direction)",
                "South Fork American River drainage (N -- deep canyon channeling winds)",
                "Cosumnes River headwaters (S -- Caldor Fire approach vector)",
                "Sly Park / Jenkinson Lake drainage (S -- secondary fire approach corridor)",
            ],
            "rate_of_spread_potential": (
                "Extreme. Caldor Fire grew from 6,500 to 30,000 acres in 24 hours. "
                "King Fire expanded rapidly through fuel-heavy forest with no recent "
                "fire history. In continuous conifer forest at this elevation, crown "
                "fire runs of 50-100 chains/hr are possible during wind events. The "
                "Fire Adapted 50 treatments demonstrated that fuel reduction can "
                "reduce spread rates to manageable levels (surface fire vs. crown fire)."
            ),
            "spotting_distance": (
                "1-3 miles in terrain-channeled winds. King Fire produced extensive "
                "spotting through continuous conifer canopy. Caldor Fire's spotting "
                "across Highway 50 demonstrated 1+ mile ember transport."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "El Dorado Irrigation District (EID) serves the community. Sly Park "
                "Reservoir (Jenkinson Lake, ~41,000 acre-feet) provides both water "
                "supply and recreation. Distribution system is adequate for normal "
                "operations but may be overwhelmed by simultaneous wildfire suppression "
                "demand. Fire can damage exposed water infrastructure (above-ground "
                "pipes, pump stations) along the Highway 50 corridor."
            ),
            "power": (
                "PG&E overhead distribution lines through continuous forest. Subject "
                "to PSPS de-energization. Power lines along Highway 50 are vulnerable "
                "to fire damage. The King Fire was ignited near power infrastructure. "
                "Extended PSPS events can last days, affecting medical equipment users."
            ),
            "communications": (
                "Cell coverage along Highway 50 corridor is adequate but degrades "
                "rapidly in side drainages and forest. During Caldor Fire, emergency "
                "communications were challenged by the volume and pace of evacuations. "
                "Loss of power (PSPS or fire damage) can take down cell towers."
            ),
            "medical": (
                "No hospital in Pollock Pines. Nearest is Marshall Medical Center in "
                "Placerville, 13 miles west on Highway 50. During fire events when "
                "Highway 50 is congested or closed, medical transport times increase "
                "dramatically. Multiple mobile home parks house elderly residents "
                "with medical needs."
            ),
        },
        "demographics_risk_factors": {
            "population": 7112,
            "seasonal_variation": (
                "Significant summer recreation population from Sly Park Reservoir "
                "(Jenkinson Lake) visitors, campgrounds in Eldorado National Forest, "
                "and Highway 50 through-traffic to Lake Tahoe. Summer population "
                "can effectively double on peak weekends."
            ),
            "elderly_percentage": "~19% age 65+",
            "mobile_homes": (
                "Mobile homes account for 9.6% of housing (328 units). Multiple "
                "mobile home parks including senior (55+) communities. These "
                "structures are highly vulnerable to ember attack and radiant heat. "
                "Parks include Bonanza MHP, Ponderosa Estates, and Dogwood MHP."
            ),
            "special_needs_facilities": (
                "55+ senior mobile home communities with elderly residents. No "
                "dedicated medical or assisted living facilities. Elderly residents "
                "on medical equipment are at extreme risk during PSPS events."
            ),
        },
    },

    # =========================================================================
    # 5. GEORGETOWN, CA -- Georgetown Divide, Limited Access
    # =========================================================================
    "georgetown_ca": {
        "center": [38.9068, -120.8385],
        "terrain_notes": (
            "Census-designated place (pop. 2,580, 2023 estimate; 2,255 per 2020 "
            "census) situated on the Georgetown Divide, a broad ridge between the "
            "Middle Fork and South Fork of the American River in El Dorado County. "
            "Elevation ~2,654 ft with the surrounding Georgetown Divide reaching "
            "3,409 ft. The community is the northeastern-most town in the California "
            "Mother Lode and is surrounded by Eldorado National Forest. The Georgetown "
            "Divide Public Utility District (GDPUD) serves 3,800 connections across "
            "72,000 acres (112.5 sq mi) of unincorporated western El Dorado County, "
            "serving ~10,000 residents across Georgetown, Garden Valley, Kelsey, and "
            "surrounding areas. Access is limited: Highway 193 from Placerville is "
            "the primary route (2-lane, winding, 15 miles), with Wentworth Springs "
            "Road, Marshall Road, and Greenwood Road providing narrow secondary access. "
            "The 2022 Mosquito Fire (76,788 acres) forced evacuation of Georgetown and "
            "surrounding communities when the fire jumped the American River and "
            "advanced from the north. In 2024, the Crozier Fire (1,960 acres) burned "
            "between the Caldor and Mosquito Fire scars, again forcing evacuations in "
            "the Georgetown Divide area."
        ),
        "key_features": [
            "Georgetown Divide ridge between Middle Fork and South Fork American River",
            "GDPUD serves 72,000 acres (112.5 sq mi) of unincorporated western El Dorado County",
            "Highway 193 is primary access -- 2-lane, winding, 15 mi from Placerville",
            "Surrounded by Eldorado National Forest on three sides",
            "2022 Mosquito Fire forced full evacuation of Georgetown area",
            "2024 Crozier Fire burned between Caldor and Mosquito Fire scars nearby",
            "GDPUD water infrastructure damaged by Mosquito Fire (flume, stream gages, levee roads)",
            "Stumpy Meadows Reservoir (21,206 acre-feet) is cornerstone water supply",
            "Walton Lake water treatment plant (built 1974) serves Georgetown proper",
            "Garden Valley, Kelsey, Volcanoville are satellite communities on the Divide",
        ],
        "elevation_range_ft": [1800, 3500],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Mosquito Fire",
                "year": 2022,
                "acres": 76788,
                "details": (
                    "Largest CA wildfire of 2022. Ignited Sep 6 at Oxbow Reservoir on "
                    "Middle Fork American River. Burned 76,788 acres in Placer and El "
                    "Dorado counties. Jumped the American River and advanced on "
                    "Georgetown from the north. Forced evacuation of ~11,000 residents "
                    "across Foresthill and Georgetown areas. Destroyed 78 structures "
                    "in Michigan Bluff, Foresthill, and Volcanoville. Directly damaged "
                    "GDPUD water infrastructure: destroyed 3 stream gages, charred the "
                    "wooden flume covering at a tunnel entrance, damaged levee roads. "
                    "GDPUD declared emergency. Contained Oct 22."
                ),
            },
            {
                "name": "Crozier Fire",
                "year": 2024,
                "acres": 1960,
                "details": (
                    "Ignited Aug 7 near Slate Mountain, northwest of Placerville. Burned "
                    "1,960 acres between the Caldor and Mosquito Fire burn scars. Forced "
                    "evacuations in Georgetown, Garden Valley, Volcanoville, Mosquito, "
                    "and Quintet areas. Arson-caused (man convicted). No structures "
                    "destroyed, but demonstrated the ongoing fire risk in the Georgetown "
                    "Divide even in areas adjacent to recent burn scars."
                ),
            },
            {
                "name": "Georgetown Fire",
                "year": 2016,
                "acres": 75,
                "details": (
                    "Small wildfire near Georgetown that prompted evacuations and "
                    "demonstrated response challenges given limited access routes."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 193 southwest to Placerville / US 50",
                "direction": "SW",
                "lanes": 2,
                "bottleneck": (
                    "Primary evacuation route. 2-lane, winding highway running ~15 "
                    "miles through forest and rural areas from Georgetown to "
                    "Placerville and Highway 50. Narrow, steep sections with no "
                    "shoulders. Passes through Garden Valley and Kelsey. Becomes "
                    "congested during evacuations when 10,000+ Divide residents "
                    "attempt to use the single highway simultaneously."
                ),
                "risk": (
                    "High. A fire between Georgetown and Placerville could cut "
                    "the primary evacuation route. The Crozier Fire demonstrated "
                    "this risk, burning near the Highway 193 corridor."
                ),
            },
            {
                "route": "Wentworth Springs Road northeast",
                "direction": "NE",
                "lanes": 2,
                "bottleneck": (
                    "Secondary route leading northeast deeper into the Sierra "
                    "and Eldorado National Forest. Narrow, winding mountain road. "
                    "Leads toward Stumpy Meadows Reservoir and eventually dead-ends "
                    "in the forest. Not a viable mass evacuation route."
                ),
                "risk": (
                    "High. Route leads deeper into National Forest, not toward "
                    "safety. Only useful for escaping a fire approaching from the "
                    "southwest if the route itself is not threatened."
                ),
            },
            {
                "route": "Marshall Road / Greenwood Road south",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Narrow rural roads connecting Georgetown area south through "
                    "Garden Valley to SR 193. These provide alternative routing "
                    "but are narrow (no shoulders), slow, and pass through "
                    "forested areas with heavy fuel loads."
                ),
                "risk": (
                    "High. Narrow roads through continuous forest. Not designed "
                    "for mass evacuation. Provides some redundancy to Highway 193 "
                    "but can be simultaneously threatened by the same fire."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Complex terrain-driven winds from American River canyon systems. "
                "Afternoon upslope flow from both the Middle Fork and South Fork "
                "drainages creates convergent wind patterns on the Georgetown Divide. "
                "NE foehn events produce strong downslope winds through the canyon "
                "systems. The deep canyons (1,500-2,500 ft) create massive pre-heating "
                "zones and channel winds toward the ridge-top community."
            ),
            "critical_corridors": [
                "Middle Fork American River canyon (N -- Mosquito Fire approach vector)",
                "South Fork American River canyon (S -- fire approach from Caldor Fire territory)",
                "Highway 193 corridor (SW -- connects fire threat to evacuation route)",
                "Volcanoville / Michigan Bluff drainage (NE -- direct path to Georgetown)",
            ],
            "rate_of_spread_potential": (
                "Extreme on steep canyon slopes. The Mosquito Fire demonstrated "
                "multi-mile runs through canyon terrain at rates exceeding 100 "
                "chains/hr. On the Divide ridge, spread rates moderate in timber "
                "fuels (20-50 chains/hr) but crown fire potential remains high in "
                "untreated areas. The 2024 Crozier Fire growth showed that even in "
                "areas adjacent to recent burn scars, sufficient fuel exists for "
                "rapid fire spread."
            ),
            "spotting_distance": (
                "1-3 miles. The Mosquito Fire jumped the entire American River "
                "canyon, demonstrating spotting distances of 1+ mile across deep "
                "terrain. Terrain-channeled winds through the canyon systems can "
                "transport embers onto the Georgetown Divide from fires burning "
                "in canyon bottoms."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Georgetown Divide Public Utility District (GDPUD). Cornerstone "
                "supply is Stumpy Meadows Reservoir (21,206 acre-feet). Walton Lake "
                "treatment plant (built 1974) serves Georgetown, Garden Valley, and "
                "part of Greenwood. The 2022 Mosquito Fire directly damaged GDPUD "
                "infrastructure: destroyed 3 stream gages, charred wooden flume "
                "covering at tunnel entrance, damaged levee roads used for "
                "maintenance access. GDPUD declared emergency and has received "
                "$1.5M for Water Reliability and Fire Resiliency Storage Tank Project "
                "but reconstruction is ongoing. Raw water conveyance system "
                "includes exposed flumes and tunnels vulnerable to fire."
            ),
            "power": (
                "PG&E overhead distribution through forest canopy. Subject to "
                "PSPS de-energization. Power infrastructure in remote areas of "
                "the Divide is particularly vulnerable to fire and wind damage. "
                "Extended outages common during fire weather events."
            ),
            "communications": (
                "Limited cell coverage across the Divide, especially in canyon "
                "areas and remote communities like Volcanoville. During Mosquito "
                "Fire, communications were strained. Georgetown Divide Fire Safe "
                "Council has worked to improve community notification systems."
            ),
            "medical": (
                "No hospital on the Georgetown Divide. Nearest is Marshall Medical "
                "Center in Placerville, 15+ miles via Highway 193. Garden Valley "
                "and Georgetown fire stations provide first response. During fire "
                "events with Highway 193 congested or closed, medical access is "
                "severely compromised for 10,000 Divide residents."
            ),
        },
        "demographics_risk_factors": {
            "population": 2580,
            "seasonal_variation": (
                "Summer recreation visitors to Stumpy Meadows Reservoir, Georgetown "
                "OHV trail system, and surrounding National Forest. Small increase "
                "compared to year-round population."
            ),
            "elderly_percentage": "~20% age 65+",
            "mobile_homes": (
                "Mobile and manufactured homes present throughout the Divide, "
                "particularly in unincorporated areas around Georgetown and Garden "
                "Valley. Limited building code enforcement in rural county areas."
            ),
            "special_needs_facilities": (
                "No dedicated senior care or medical facilities on the Divide. "
                "Elderly and mobility-impaired residents are dependent on private "
                "transportation for evacuation. Georgetown Divide's remote location "
                "means ambulance response times are 20-30+ minutes."
            ),
        },
    },

    # =========================================================================
    # 6. PLACERVILLE OUTSKIRTS / DIAMOND SPRINGS, CA -- WUI Edge along El Dorado NF
    # =========================================================================
    "diamond_springs_ca": {
        "center": [38.6946, -120.8149],
        "terrain_notes": (
            "Census-designated place (pop. ~11,000; 11,037 per 2010 census, ~12,600 "
            "estimated 2023) in El Dorado County, immediately south and east of "
            "Placerville along the Highway 49 and Pleasant Valley Road corridors. "
            "Elevation ~1,791 ft, at the lower boundary of the Sierra foothill "
            "woodland zone transitioning into the Eldorado National Forest. Diamond "
            "Springs is the quintessential WUI edge community: residential "
            "development directly abuts wildland fuels (grass, oak woodland, "
            "mixed conifer) along the El Dorado National Forest boundary. The Diamond "
            "Springs-El Dorado Fire Protection District serves ~11,731 residents "
            "across 65.5 square miles of semi-urban and rural terrain. The area's "
            "fire history reflects its position at the NF boundary: the 2014 Sand "
            "Fire (3,800 acres) burned near Highway 49 at the Amador-El Dorado "
            "county line, destroying 13 homes and forcing 1,083 evacuations. The "
            "2024 Crozier Fire (1,960 acres) burned northeast of Diamond Springs "
            "toward Georgetown. More ominously, the 2021 Caldor Fire (221,835 acres) "
            "and 2014 King Fire (97,717 acres) burned in the forests just east of "
            "Diamond Springs, and a westward-running fire of similar magnitude would "
            "directly threaten the community."
        ),
        "key_features": [
            "WUI edge community: residential development directly abutting El Dorado NF",
            "Diamond Springs-El Dorado Fire Protection District: 65.5 sq mi, ~11,731 residents",
            "Highway 49 and Pleasant Valley Road corridors provide primary access",
            "Elevation ~1,800 ft -- lower foothill zone with grass/oak/conifer transition",
            "Proximity to Caldor Fire (2021, 221,835 acres) and King Fire (2014, 97,717 acres) burn areas",
            "2014 Sand Fire burned near Highway 49 at county line",
            "2024 Crozier Fire burned northeast toward Georgetown",
            "Semi-urban density transitions rapidly to rural/wildland within 1-2 miles",
            "El Dorado County government services concentrated in Placerville/Diamond Springs",
            "Gateway community for Highway 50 corridor eastbound to Pollock Pines and Tahoe",
        ],
        "elevation_range_ft": [1500, 2200],
        "wui_exposure": "high",
        "historical_fires": [
            {
                "name": "Sand Fire",
                "year": 2014,
                "acres": 3800,
                "details": (
                    "Ignited near Highway 49 and Sand Ridge Road at the Amador-El "
                    "Dorado county line. Burned 3,800 acres of grassland and timber. "
                    "Destroyed 13 homes and 38 outbuildings. Forced 606 voluntary "
                    "and 477 mandatory evacuations (1,083 total). Demonstrated fire "
                    "spread potential in the dry grass and oak woodland fuels at the "
                    "lower-elevation WUI edge."
                ),
            },
            {
                "name": "Crozier Fire",
                "year": 2024,
                "acres": 1960,
                "details": (
                    "Arson fire ignited Aug 7 near Slate Mountain. Burned 1,960 acres "
                    "between the Caldor and Mosquito Fire burn scars northeast of "
                    "Diamond Springs. Forced evacuations in Garden Valley, Georgetown, "
                    "and surrounding areas. No structures destroyed. Diamond Springs "
                    "El Dorado County shelter at 6435 Capitol Ave was activated."
                ),
            },
            {
                "name": "Caldor Fire (nearby threat)",
                "year": 2021,
                "acres": 221835,
                "details": (
                    "Burned 221,835 acres east of Diamond Springs in El Dorado, "
                    "Amador, and Alpine counties. While Diamond Springs was not directly "
                    "in the fire's path, the fire burned within 15-20 miles of the "
                    "community and a westward shift in wind could have pushed the fire "
                    "toward the Placerville/Diamond Springs area. Forced extended "
                    "closure of Highway 50, affecting Diamond Springs as a gateway "
                    "community."
                ),
            },
            {
                "name": "King Fire (nearby threat)",
                "year": 2014,
                "acres": 97717,
                "details": (
                    "Arson fire that burned 97,717 acres in the Eldorado National "
                    "Forest east of Diamond Springs. While burning mostly in NF "
                    "lands, the fire demonstrated the potential for large, fast-moving "
                    "fires in the forests immediately upslope of the community."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 49 / Pleasant Valley Road to Highway 50",
                "direction": "W/NW",
                "lanes": 2,
                "bottleneck": (
                    "Primary route connecting Diamond Springs to Highway 50 and "
                    "Placerville. 2-lane in Diamond Springs area with moderate "
                    "traffic volume. Merges with Highway 50 which provides 4-lane "
                    "divided highway access westbound toward Sacramento. Intersection "
                    "congestion during peak evacuation."
                ),
                "risk": (
                    "Moderate. Route is at lower elevation and passes through less "
                    "densely forested terrain. However, grass fires along Highway 49 "
                    "could threaten the corridor, as demonstrated by the Sand Fire."
                ),
            },
            {
                "route": "Highway 49 southbound toward Plymouth / Amador County",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "2-lane highway heading south through El Dorado and Amador "
                    "counties. Winding, rural road through grass and oak woodland. "
                    "Lower traffic volume but limited capacity."
                ),
                "risk": (
                    "Moderate. Passes through fire-prone grass/oak terrain. The "
                    "Sand Fire burned near this corridor in 2014."
                ),
            },
            {
                "route": "Highway 50 westbound from Placerville",
                "direction": "W",
                "lanes": 4,
                "bottleneck": (
                    "4-lane divided highway from Placerville westbound toward "
                    "El Dorado Hills and Sacramento. Primary high-capacity "
                    "evacuation route. Accessible via surface streets through "
                    "Placerville (~3 miles from Diamond Springs center)."
                ),
                "risk": (
                    "Low to moderate. Highway 50 west of Placerville provides "
                    "good capacity and leads away from the forest. However, the "
                    "3-mile surface street connection through Placerville can "
                    "congest during mass evacuation."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Afternoon upslope thermal winds from the Sacramento Valley push "
                "fire from SW to NE, from the lower grass/oak zone into the forest "
                "zone. NE foehn events reverse the pattern, pushing fire from the "
                "forest downslope toward Diamond Springs. The lower-elevation "
                "position (~1,800 ft) means Diamond Springs is in the path of "
                "downslope-driven fires running out of the Eldorado NF."
            ),
            "critical_corridors": [
                "Highway 49 corridor (N-S -- grass/oak fire spread axis)",
                "Weber Creek drainage (N -- connects forest fuels to town edge)",
                "Eldorado NF boundary (E -- continuous forest fuel bed within 1-2 mi)",
                "Pleasant Valley (S/SE -- open grassland enabling rapid spread toward community)",
            ],
            "rate_of_spread_potential": (
                "Very high in grass/oak fuels at this elevation (80-200 chains/hr "
                "in wind-driven grass fires). The 2014 Sand Fire demonstrated rapid "
                "spread through this fuel type. Lower in mixed conifer (20-50 "
                "chains/hr) but crown fire potential exists on steeper slopes to "
                "the east. The primary risk is a fast-moving grass fire from the "
                "south/southeast or a forest fire running downslope from the east."
            ),
            "spotting_distance": (
                "0.5-1.5 miles in grass/brush fuels. Longer (1-3 miles) from "
                "timber fires running downslope from the Eldorado NF. The WUI "
                "edge position means ember showers from forest fires can reach "
                "residential structures even if the main fire front is still in "
                "the forest."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "El Dorado Irrigation District (EID) serves Diamond Springs. "
                "Adequate water infrastructure for normal operations. District "
                "headquarters and animal services shelter are located in Diamond "
                "Springs, making it a hub for emergency operations."
            ),
            "power": (
                "PG&E distribution with overhead lines in rural/WUI areas. Subject "
                "to PSPS de-energization. Lower-elevation location means less "
                "frequent PSPS than higher-elevation communities but still affected "
                "during major wind events."
            ),
            "communications": (
                "Good cell and internet coverage in the semi-urban Diamond Springs "
                "area. Degrades in rural areas east of town toward the NF boundary. "
                "El Dorado County emergency notification systems cover the area."
            ),
            "medical": (
                "Marshall Medical Center in Placerville (~3 miles) provides "
                "hospital-level care. Diamond Springs Fire Protection District "
                "stations at 501 Pleasant Valley Rd and other locations provide "
                "rapid first response. Better medical access than most foothill "
                "communities."
            ),
        },
        "demographics_risk_factors": {
            "population": 11037,
            "seasonal_variation": (
                "Modest variation. Diamond Springs functions primarily as a "
                "residential/commercial area for Placerville commuters. Some "
                "increase from Highway 50 corridor recreation traffic in summer."
            ),
            "elderly_percentage": "~18% age 65+",
            "mobile_homes": (
                "Mobile and manufactured homes present, particularly in rural "
                "areas at the WUI edge. These homes are most vulnerable to ember "
                "attack from wildland fires approaching from the east."
            ),
            "special_needs_facilities": (
                "El Dorado County services in Placerville/Diamond Springs area "
                "include senior services and the county shelter. Better "
                "institutional support than most foothill communities due to "
                "proximity to Placerville county seat."
            ),
        },
    },

    # =========================================================================
    # 7. PARADISE SATELLITE COMMUNITIES -- Feather River Canyon Fire Corridor
    #    Concow, Berry Creek, Stirling City, Yankee Hill
    # =========================================================================
    "paradise_satellite_communities": {
        "center": [39.73, -121.49],
        "terrain_notes": (
            "Cluster of four tiny, remote communities in the Feather River Canyon "
            "fire corridor of Butte County, all within 15 miles of Paradise and all "
            "devastated by the 2018 Camp Fire and/or the 2020 North Complex (Bear) "
            "Fire. These communities share extreme vulnerability: minimal population, "
            "single-road access via narrow winding mountain roads, heavy fuel loading "
            "in continuous mixed conifer and oak woodland, and direct exposure to the "
            "Jarbo Gap NE foehn wind regime that drives the most destructive fires in "
            "this corridor. Combined population ~2,000-2,500 (pre-fire; significantly "
            "reduced post-fire). These communities are rebuilding slowly with minimal "
            "resources -- the Bear Fire survivors notably received far less rebuild "
            "assistance than Camp Fire survivors in Paradise despite similar devastation."
        ),
        "key_features": [
            "Four communities in Feather River Canyon fire corridor: Concow, Berry Creek, Stirling City, Yankee Hill",
            "All devastated by Camp Fire (2018) and/or North Complex/Bear Fire (2020)",
            "Combined pre-fire population ~2,500; significantly reduced post-fire",
            "Jarbo Gap NE foehn wind regime -- most destructive fire weather in NorCal",
            "Single-road access for each community via narrow, winding mountain roads",
            "Berry Creek: 14 of 16 North Complex Fire fatalities were Berry Creek residents",
            "Concow: 95% of structures destroyed in first 6 hours of Camp Fire",
            "Yankee Hill: devastated by both Camp Fire (2018) and Bear Fire (2020)",
            "Stirling City: sawmill siren installed as evacuation warning system",
            "Slow rebuild: Berry Creek survivors lack rebuild resources compared to Paradise",
            "Park Fire (2024, 429,000+ acres) again threatened Stirling City and upper corridor",
        ],
        "sub_profiles": {
            "concow": {
                "center": [39.7302, -121.5266],
                "elevation_ft": 1759,
                "population_2020": 402,
                "population_pre_fire": 710,
                "terrain_notes": (
                    "Unincorporated community in a bowl-shaped valley surrounding "
                    "Concow Reservoir (PG&E), at ~1,759 ft elevation. Located 5 miles "
                    "NW of Paradise on the same narrow ridge system. Access via Concow "
                    "Road -- narrow, winding, no shoulders. During the 2018 Camp Fire, "
                    "Concow was reached by fire within ~1 hour of ignition (by 07:30) "
                    "and lost ~95% of structures. Four residents killed. The community "
                    "is a sentinel for Paradise: if Concow is burning, Paradise has "
                    "30-60 minutes before fire arrival during Jarbo wind events. "
                    "The 2020 Census counted only 402 people (305 households), a 43% "
                    "decline from 710 in 2010. Was also evacuated during the 2020 "
                    "North Complex/Bear Fire. Rebuilding has been extremely slow."
                ),
                "access_roads": [
                    "Concow Road (2-lane, narrow, winding, no shoulders -- only paved route)",
                    "Hoffman Road (narrow connecting road to Yankee Hill area)",
                ],
                "historical_fires": [
                    "Camp Fire 2018 (95% of structures destroyed in first 6 hours, 4 killed)",
                    "North Complex / Bear Fire 2020 (second evacuation in 2 years)",
                    "Park Fire 2024 (evacuation orders issued for Concow area)",
                ],
            },
            "berry_creek": {
                "center": [39.6652, -121.4250],
                "elevation_ft": 2000,
                "population_2020": 1637,
                "population_pre_fire": 1200,
                "terrain_notes": (
                    "Census-designated place 25 miles NE of Oroville at ~2,000 ft "
                    "elevation, in hilly terrain on the western slope of the Sierra "
                    "Nevada. On September 9, 2020, the Bear Fire (North Complex West "
                    "Zone) reached Berry Creek at 10 PM with virtually no warning -- "
                    "evacuation orders were issued at 3:15 PM the same day with no "
                    "prior warning. The fire destroyed nearly the entire town, leaving "
                    "only 3 houses standing. 14 of the 16 North Complex Fire fatalities "
                    "were Berry Creek residents. The community has been described as "
                    "'leveled by a wall of fire.' Three years post-fire, rebuilding "
                    "efforts remain slow, with survivors lacking the rebuild resources "
                    "that other fire communities (like Paradise) received. The 2020 "
                    "Census population figure of 1,637 was recorded before the Bear Fire."
                ),
                "access_roads": [
                    "Bald Rock Road / Oroville-Quincy Highway (2-lane, winding, 25 mi to Oroville)",
                    "Forbestown Road (narrow mountain road connecting to Forbestown/Clipper Mills)",
                ],
                "historical_fires": [
                    "North Complex / Bear Fire 2020 (town nearly 100% destroyed, 14 killed, 2,352 structures across complex)",
                ],
            },
            "stirling_city": {
                "center": [39.9077, -121.5280],
                "elevation_ft": 3570,
                "population_2020": 284,
                "population_pre_fire": 300,
                "terrain_notes": (
                    "Tiny unincorporated community (pop. 284, 2020 census) at 3,570 ft "
                    "elevation, 32 miles NE of Chico, nestled in timberland in the "
                    "Sierra Nevada foothills. The community is surrounded by dense "
                    "conifer forest and was historically a lumber mill town. Access is "
                    "via Skyway northbound from Paradise/Magalia -- the same road that "
                    "serves as Paradise's primary evacuation route, creating a cascading "
                    "vulnerability where Stirling City's evacuation depends on the "
                    "road through communities that may already be on fire. The "
                    "community installed a sawmill siren on the volunteer fire station "
                    "roof as a wildfire evacuation warning system after the 2018 Camp "
                    "Fire demonstrated the inadequacy of cell/internet-based "
                    "notification in remote mountain communities. Threatened by Camp "
                    "Fire (2018), evacuated during Park Fire (2024, 429,000+ acres). "
                    "At 3,570 ft, Stirling City is in the dense montane conifer zone "
                    "with extremely heavy fuel loads."
                ),
                "access_roads": [
                    "Skyway (SR 191) north from Paradise/Magalia (2-lane, narrow, winding mountain road)",
                    "Inskip Road (narrow connecting road to Inskip and surrounding forest)",
                ],
                "historical_fires": [
                    "Camp Fire 2018 (evacuation orders issued, fire threatened community)",
                    "Park Fire 2024 (evacuation warnings issued, 429,000+ acres)",
                ],
            },
            "yankee_hill": {
                "center": [39.73, -121.48],
                "elevation_ft": 1982,
                "population_2020": 260,
                "population_pre_fire": 800,
                "terrain_notes": (
                    "Unincorporated community (pop. 260, 2020 census; ~800 pre-fire) "
                    "at ~1,982 ft elevation, 6.5 miles ESE of Paradise. Devastated "
                    "by BOTH the 2018 Camp Fire AND the 2020 North Complex/Bear Fire, "
                    "making it one of only a handful of American communities to be "
                    "largely destroyed by two separate wildfires in a 2-year period. "
                    "The community lost its Grange Hall (main community center) in "
                    "2018 and it is not being rebuilt. Current development is primarily "
                    "re-development as the community slowly recovers. The Yankee Hill "
                    "Fire Safe Council annex to the 2024 Butte County Local Hazard "
                    "Mitigation Plan documents the ongoing vulnerability. Population "
                    "in 2023 estimated at 384 with a median age of 53.5, indicating "
                    "an aging population rebuilding in place. Access is via narrow "
                    "connecting roads to Concow and Paradise -- same road network that "
                    "proved inadequate during Camp Fire."
                ),
                "access_roads": [
                    "Yankee Hill Road / connecting roads to Concow Road (narrow, winding)",
                    "Routes through Paradise to Skyway (dependent on Paradise being passable)",
                ],
                "historical_fires": [
                    "Camp Fire 2018 (community largely destroyed along with Paradise/Concow)",
                    "North Complex / Bear Fire 2020 (second destruction in 2 years)",
                ],
            },
        },
        "elevation_range_ft": [1600, 3600],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Camp Fire",
                "year": 2018,
                "acres": 153336,
                "details": (
                    "Deadliest and most destructive wildfire in California history. "
                    "85 fatalities, 18,804 structures destroyed, 153,336 acres. "
                    "Ignited on PG&E's Caribou-Palermo 115kV line near Pulga. "
                    "Destroyed Paradise, Concow, and Yankee Hill within 6 hours. "
                    "Driven by NE Jarbo Gap foehn winds sustained 35-45 mph with "
                    "gusts to 50+. Ember spotting documented up to 6.3 km ahead of "
                    "fire front. 27,000 people evacuated simultaneously; trips "
                    "normally 25 min took 3-4 hours. 19 documented burnovers on roads."
                ),
            },
            {
                "name": "North Complex / Bear Fire",
                "year": 2020,
                "acres": 318935,
                "details": (
                    "North Complex Fire complex (318,935 acres total) including the "
                    "Bear Fire component that devastated Berry Creek, Feather Falls, "
                    "and areas near Concow and Yankee Hill. 16 fatalities (14 in "
                    "Berry Creek, 2 in Feather Falls). 2,352 structures destroyed. "
                    "Berry Creek was destroyed with virtually no warning -- evacuation "
                    "orders issued same day fire arrived, 'wall of fire' reached town "
                    "at 10 PM on Sep 9, 2020. Only 3 houses left standing in Berry "
                    "Creek. Survivors received far less rebuild assistance than Camp "
                    "Fire survivors."
                ),
            },
            {
                "name": "Park Fire",
                "year": 2024,
                "acres": 429000,
                "details": (
                    "California's 5th largest wildfire in recorded history. 429,000+ "
                    "acres in Butte and Tehama counties. Evacuation orders/warnings "
                    "issued for Concow, Stirling City, Magalia, and Paradise areas. "
                    "Arson-caused. At least 209 homes destroyed. Demonstrated that "
                    "the Feather River Canyon corridor remains under persistent, "
                    "recurring mega-fire threat."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Concow Road to Paradise / Skyway (Concow, Yankee Hill)",
                "direction": "S/SW",
                "lanes": 2,
                "bottleneck": (
                    "Narrow, winding, no shoulders. Must transit through Paradise "
                    "to reach Skyway and ultimately Chico. If Paradise is on fire "
                    "(as in 2018), this route is a death trap. During Camp Fire, "
                    "most Concow residents could not evacuate before fire arrived."
                ),
                "risk": (
                    "Extreme. Dependent on Paradise being passable. Single route "
                    "for Concow and Yankee Hill. 23 life-threatening entrapment "
                    "events documented during Camp Fire, 17 involving civilians "
                    "on evacuation roads."
                ),
            },
            {
                "route": "Bald Rock Road / Oroville-Quincy Hwy to Oroville (Berry Creek)",
                "direction": "SW",
                "lanes": 2,
                "bottleneck": (
                    "25-mile, 2-lane winding mountain road from Berry Creek to "
                    "Oroville. Only paved route out. Passes through heavily "
                    "forested terrain and descends steeply to the Sacramento Valley. "
                    "During Bear Fire, evacuation orders came with no prior warning "
                    "on the same day fire destroyed the town."
                ),
                "risk": (
                    "Extreme. Single route for ~1,200 residents. 25 miles of narrow "
                    "mountain road through fire-prone forest. Zero-warning evacuation "
                    "demonstrated in 2020."
                ),
            },
            {
                "route": "Skyway north from Paradise/Magalia (Stirling City)",
                "direction": "N",
                "lanes": 2,
                "bottleneck": (
                    "2-lane mountain road extending Skyway northward from Magalia. "
                    "Narrow, winding, passes through dense forest. A 185-ft section "
                    "was narrowed to only 11.5 ft wide (single lane) from 2022-23 "
                    "winter storm damage -- creating severe bottleneck for both "
                    "evacuation and fire apparatus access. FEMA repair funded but "
                    "not yet completed as of early 2025."
                ),
                "risk": (
                    "Extreme. Stirling City's evacuation route runs THROUGH "
                    "Paradise and Magalia, both of which are known to be in the "
                    "direct fire path during Jarbo wind events. If fire is "
                    "approaching from the NE, Stirling City residents must drive "
                    "south toward and through the fire to escape."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "NE Jarbo Gap foehn winds. Katabatic foehn events where dry Great "
                "Basin air descends the western Sierra slope, funneling through "
                "Jarbo Gap -- a topographic constriction where the Feather River "
                "Canyon narrows between Jarbo Gap Ridge and Table Mountain. Venturi "
                "effect accelerates winds to 50-70 mph. These events drive the "
                "most catastrophic fires in the corridor: Camp Fire (2018) spread "
                "at 1 m/s (~2.2 mph / 180 chains/hr) through wildland fuels. When "
                "winds align NE-to-SW through Jarbo Gap, the entire Feather River "
                "Canyon becomes a blowtorch aimed at Paradise and its satellite "
                "communities."
            ),
            "critical_corridors": [
                "Feather River Canyon (NE-SW -- primary fire corridor for Camp Fire, Park Fire)",
                "West Branch Feather River (N-S -- parallel canyon channeling wind and fire)",
                "Concow valley bowl (trapped topography creating extreme fire behavior)",
                "Berry Creek / Bald Rock drainage (N-S -- Bear Fire spread corridor)",
                "Butte Creek Canyon (E -- parallel to Paradise ridge, ember receptor)",
            ],
            "rate_of_spread_potential": (
                "Extreme. Camp Fire: 1 m/s (180 chains/hr) sustained through wildland "
                "fuels during Jarbo wind event. Within communities, fire spread could "
                "not be computed due to simultaneous spotting from hundreds of ignition "
                "points. Bear Fire: 8-mile-long flank swept through Berry Creek in "
                "hours. Park Fire: grew to 429,000+ acres, one of the fastest-growing "
                "fires in CA history. These are among the highest fire spread rates "
                "documented in North American wildfire history."
            ),
            "spotting_distance": (
                "Up to 6.3 km (3.9 miles) documented during Camp Fire per NIST study. "
                "Softball-sized embers lofted over the Paradise/Magalia ridge and into "
                "Butte Creek Canyon during Camp Fire. During Bear Fire, ember transport "
                "distances of 1-3 miles were observed ahead of the fire front."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Varied by sub-community. Concow: PG&E's Concow Reservoir provides "
                "limited water but no fire suppression capacity. Berry Creek: rural "
                "well systems, no municipal water. Stirling City: small community "
                "water system. Yankee Hill: rural wells. None of these communities "
                "have water infrastructure adequate for wildfire suppression."
            ),
            "power": (
                "PG&E overhead distribution through dense forest. Camp Fire was "
                "ignited by failure of PG&E's Caribou-Palermo 115kV transmission "
                "line -- the very infrastructure that powered these communities. "
                "That line has been permanently de-energized. Remaining distribution "
                "lines are subject to PSPS de-energization. Extended outages during "
                "fire weather are routine."
            ),
            "communications": (
                "Minimal to none. Cell coverage is spotty to nonexistent in canyon "
                "and mountain areas. 17 cell towers destroyed during Camp Fire. "
                "Stirling City installed a sawmill siren as a backup notification "
                "system because cell/internet-based alerts are unreliable. Berry "
                "Creek received evacuation orders on the same day fire destroyed "
                "the town -- notification came too late."
            ),
            "medical": (
                "No medical facilities in any of these communities. Nearest hospital "
                "is Enloe Medical Center in Chico (30-50 miles depending on community) "
                "or Oroville Hospital (25 miles from Berry Creek). During fire events, "
                "road access to hospitals may be cut off. Aging populations with "
                "medical needs in all four communities."
            ),
        },
        "demographics_risk_factors": {
            "population": 2500,
            "seasonal_variation": (
                "Minimal seasonal variation. These are primarily permanent-resident "
                "communities with little tourism infrastructure. Population has "
                "declined post-fire in all four communities."
            ),
            "elderly_percentage": "~25-30% age 65+ (estimated, skews older post-fire as younger residents relocate)",
            "mobile_homes": (
                "Significant mobile home presence in all four communities, "
                "especially Concow and Yankee Hill. Post-fire rebuilding has "
                "included mobile/manufactured homes as the most affordable option. "
                "These structures are extremely vulnerable to the ember attack "
                "fire regime documented during Camp Fire."
            ),
            "special_needs_facilities": (
                "None. No senior care, assisted living, medical clinics, or "
                "special needs facilities in any of the four communities. "
                "Yankee Hill lost its only community center (Grange Hall) in "
                "2018 and it is not being rebuilt. Residents with special needs "
                "are entirely dependent on private resources and neighborly "
                "assistance during emergencies."
            ),
        },
    },
}
