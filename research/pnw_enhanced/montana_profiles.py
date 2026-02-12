"""
Montana Fire-Vulnerable City Profiles — Research-Paper Quality
==============================================================
Enhanced profiles for 11 Montana cities with extreme wildfire vulnerability.
Covers terrain, historical fires, evacuation routes, infrastructure, demographics,
and fire spread characteristics at depth suitable for academic/research use.

Sources include USFS Community Wildfire Protection Plans, InciWeb incident data,
US Census Bureau, Montana DNRC, NPS fire history records, peer-reviewed smoke/health
studies (Seeley Lake PM2.5), and local/regional journalism.

Generated: 2026-02-09
"""

PNW_MONTANA_ENHANCED = {

    # =========================================================================
    # 1. MISSOULA, MT — "Hub of Five Valleys"
    # =========================================================================
    "missoula_mt": {
        "center": [46.8721, -113.9940],
        "terrain_notes": (
            "Missoula sits at the convergence of five mountain-ringed valleys in western Montana, "
            "at approximately 3,209 ft elevation on the floor of ancient Glacial Lake Missoula. "
            "The Clark Fork River bisects the city east-to-west, joined by the Bitterroot River "
            "from the south and Rattlesnake Creek from the north. Mount Sentinel (5,158 ft) rises "
            "immediately east of the University of Montana campus, while Mount Jumbo (4,768 ft) "
            "flanks the north side of Hellgate Canyon. The city is literally surrounded by National "
            "Forest on all sides: Lolo NF to the south and west (2.3 million acres), portions of "
            "Flathead NF to the north, and the Rattlesnake Wilderness/NRA directly north of town. "
            "Pattee Canyon and the South Hills extend forested WUI terrain to within blocks of "
            "downtown. The five valleys (Missoula, Bitterroot, Blackfoot, Clark Fork/Hellgate, "
            "Frenchtown) all funnel toward the city, creating complex wind channeling that can "
            "drive fire and trap smoke in inversions. The 2017 fire season demonstrated this when "
            "the Lolo Peak, Rice Ridge, and other fires filled the valley with hazardous smoke "
            "for weeks. Missoula County's populated areas have greater wildfire risk than 84% of "
            "Montana counties. With 78,000+ residents and the state's second-largest metro area, "
            "Missoula represents the highest-consequence WUI scenario in Montana."
        ),
        "key_features": [
            {"name": "Mount Sentinel", "bearing": "E", "type": "mountain",
             "notes": "5,158 ft, rises directly above UM campus; steep grass/timber slopes, 1985 Hellgate Canyon fire burned here; the iconic 'M' trail"},
            {"name": "Mount Jumbo", "bearing": "NE", "type": "mountain",
             "notes": "4,768 ft, north side of Hellgate Canyon; elk winter range; grass/shrub lower slopes transition to timber"},
            {"name": "Pattee Canyon", "bearing": "SE", "type": "canyon/WUI",
             "notes": "Heavily developed residential canyon extending into Lolo NF; dense ponderosa/Douglas fir; extreme WUI exposure"},
            {"name": "Rattlesnake Creek/Wilderness", "bearing": "N", "type": "drainage/wilderness",
             "notes": "Major drainage running north from city into 33,000-acre Rattlesnake Wilderness; residential development along lower creek"},
            {"name": "Clark Fork River", "bearing": "E-W through city", "type": "river",
             "notes": "Primary river bisecting city; potential firebreak but bridged extensively; riparian corridor"},
            {"name": "Bitterroot River confluence", "bearing": "SW", "type": "river",
             "notes": "Joins Clark Fork at west edge of city; Bitterroot Valley fires can channel smoke and fire NE toward Missoula"},
            {"name": "Lolo National Forest", "bearing": "S/W/N", "type": "national_forest",
             "notes": "2.3 million acres surrounding Missoula on three sides; mixed-severity fire regime; major fire source"},
            {"name": "Miller Creek drainage", "bearing": "SE", "type": "drainage/WUI",
             "notes": "Site of 2024 Miller Peak Fire (2,724 acres); residential development up narrow canyon into NF land"},
        ],
        "elevation_range_ft": [3100, 5200],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Miller Peak Fire", "year": 2024, "acres": 2724,
             "details": "Burned 8 miles SE of Missoula in Plant Creek drainage; 600+ personnel, 19 engines, 3 helicopters; evacuation warnings for Upper Miller Creek Road residents; difficult terrain limited access and visibility"},
            {"name": "Lolo Peak Fire", "year": 2017, "acres": 53902,
             "details": "Lightning-caused fire on Lolo Peak; 3,000+ evacuated, 1,150 residences threatened, 2 homes destroyed, 1 firefighter killed; 9,000 acres burned in single 24-hr wind event; filled Missoula Valley with hazardous smoke for weeks"},
            {"name": "Lolo Creek Complex", "year": 2013, "acres": 12000,
             "details": "West Fork Two fire combined with Schoolhouse Fire when high winds barreled down Lolo Creek Valley; fire jumped highway; residents had no time for evacuation warnings; 5 homes burned"},
            {"name": "Hellgate Canyon Fire", "year": 1985, "acres": 800,
             "details": "Burned slopes of Mount Sentinel adjacent to UM campus; demonstrated direct urban fire threat"},
        ],
        "evacuation_routes": [
            {"route": "I-90 West (toward Frenchtown)", "direction": "W", "lanes": 4,
             "bottleneck": "Reserve St / Orange St on-ramps; Missoula grid congestion",
             "risk": "Smoke from Bitterroot or Lolo fires can reduce visibility on I-90 through Hellgate Canyon"},
            {"route": "I-90 East (toward Clinton/Drummond)", "direction": "E", "lanes": 4,
             "bottleneck": "Hellgate Canyon narrows I-90 between Mount Sentinel and Mount Jumbo",
             "risk": "Canyon funnels both wind and smoke; fires on either peak would threaten this corridor"},
            {"route": "US-93 South (Bitterroot Valley)", "direction": "S", "lanes": 4,
             "bottleneck": "US-93/Reserve St intersection; heavy daily traffic",
             "risk": "Evacuating toward active Bitterroot fires is counterproductive; this route leads deeper into fire-prone valley"},
            {"route": "US-93 North (toward Flathead)", "direction": "N", "lanes": 2,
             "bottleneck": "Evaro Hill grade; single road through Flathead Reservation",
             "risk": "Only viable northern escape; 2-lane road would bottleneck with mass evacuation"},
            {"route": "MT-200 East (toward Lincoln/Great Falls)", "direction": "NE", "lanes": 2,
             "bottleneck": "Bonner interchange; narrow Blackfoot River canyon",
             "risk": "Remote 2-lane highway; long distance to next population center; fire can close Blackfoot corridor"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Complex valley winds driven by five converging valleys. Daytime up-valley winds from "
                "the west through Hellgate Canyon at 10-25 mph; nighttime drainage winds from side canyons. "
                "Chinook (foehn) winds in spring/fall can produce extreme fire behavior. Inversions trap smoke "
                "and create prolonged hazardous air quality events."
            ),
            "critical_corridors": [
                "Pattee Canyon — dense WUI timber directly into city neighborhoods",
                "Rattlesnake Creek — north drainage funnels fire toward university/downtown",
                "Miller Creek — SE drainage, site of 2024 fire, residential development up canyon",
                "Hellgate Canyon — east-west wind tunnel between Sentinel and Jumbo",
                "Lolo Creek corridor — SW approach, demonstrated 2013 blowup potential",
            ],
            "rate_of_spread_potential": (
                "Extreme in wind-driven canyon events. Lolo Peak Fire burned 9,000 acres in 24 hours "
                "during wind event. Lolo Creek Complex fire jumped highway in minutes. Steep slopes "
                "on Sentinel and Jumbo can produce rapid upslope runs. Grass/timber interface on "
                "mountain flanks allows fast transition from surface to crown fire."
            ),
            "spotting_distance": (
                "0.5-1.5 miles typical in canyon wind events; embers carried through Hellgate Canyon "
                "corridor. Potential for long-range spotting into urban neighborhoods from Pattee Canyon "
                "or Miller Creek drainage fires."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Mountain Water Company (now Missoula Water) serves city from multiple wells and the "
                "Rattlesnake Creek watershed. Fire flow capacity generally adequate for urban core but "
                "WUI homes on dead-end canyon roads (Miller Creek, Pattee Canyon, Rattlesnake) may "
                "exceed system capacity during simultaneous structure fires."
            ),
            "power": (
                "NorthWestern Energy serves the region; transmission lines cross forested corridors "
                "vulnerable to fire damage. Power outages during smoke events affect air filtration "
                "systems. Grid reliability threatened by simultaneous fire on multiple fronts."
            ),
            "communications": (
                "Cell towers on mountain peaks (Sentinel, Jumbo, Blue Mountain) are fire-exposed. "
                "Emergency alert systems require functional cell/internet infrastructure. University "
                "of Montana campus has independent emergency notification system."
            ),
            "medical": (
                "Providence St. Patrick Hospital (~250 beds) and Community Medical Center (~150 beds) "
                "provide Level II trauma capability. Both facilities are in the valley floor and "
                "accessible, but smoke events overwhelm respiratory care capacity. The 2017 smoke "
                "season demonstrated healthcare surge challenges."
            ),
        },
        "demographics_risk_factors": {
            "population": 78204,
            "seasonal_variation": (
                "University of Montana adds ~10,000 students Sept-May. Summer tourism and outdoor "
                "recreation bring additional thousands. Peak fire season overlaps with student arrival "
                "in August/September — unfamiliar population during highest risk period."
            ),
            "elderly_percentage": "~12% over 65 (lower than state average due to university population)",
            "mobile_homes": (
                "Several mobile home parks along US-93 corridor and in Wye/Frenchtown area; "
                "concentrated vulnerability in WUI-adjacent locations."
            ),
            "special_needs_facilities": (
                "Multiple assisted living facilities, university dormitories (2,500+ students), "
                "Missoula County jail (~300 capacity), homeless shelter populations. "
                "Significant transient/unhoused population in riverfront areas."
            ),
        },
    },

    # =========================================================================
    # 2. HELENA, MT — State Capital
    # =========================================================================
    "helena_mt": {
        "center": [46.5958, -112.0270],
        "terrain_notes": (
            "Helena, Montana's state capital, sits at ~4,058 ft elevation in a broad valley between "
            "the Big Belt Mountains to the east and the Continental Divide/Helena National Forest to "
            "the west and south. The city was founded during the 1864 gold rush in Last Chance Gulch, "
            "and the historic downtown sits in a narrow gulch at the base of Mount Helena (5,468 ft), "
            "which rises 1,300 ft directly above the city center. The South Hills immediately south "
            "of town are heavily forested with ponderosa pine and Douglas fir extending into the "
            "Helena-Lewis and Clark National Forest. Ten Mile Creek and Prickly Pear Creek drain "
            "through the western and eastern portions of the city respectively. The Sleeping Giant "
            "Wilderness Study Area lies 30 miles north along the Missouri River, with elevations "
            "from 3,600 to 6,800 ft. Helena has experienced repeated wildfire threats: the 2021 "
            "fire season brought the Rock Creek Fire (2,560 acres), Woods Creek Fire (12,000 acres), "
            "and Harris Mountain Fire (25,000 acres) all burning simultaneously near the city. "
            "A 2023 fire on Mount Helena itself burned 18 acres within the city park. The South Hills "
            "trail system area has active USFS prescribed burn programs specifically to reduce WUI risk."
        ),
        "key_features": [
            {"name": "Mount Helena", "bearing": "SW", "type": "mountain/city_park",
             "notes": "5,468 ft summit, 620-acre city park; 2023 fire burned 18 acres on slopes; ponderosa pine/grass; directly above downtown"},
            {"name": "South Hills", "bearing": "S", "type": "forested_WUI",
             "notes": "Dense ponderosa/Douglas fir extending from residential neighborhoods into Helena NF; active prescribed burn area; camping closures due to fire risk"},
            {"name": "Sleeping Giant WSA", "bearing": "N", "type": "wilderness_study_area",
             "notes": "30 mi north; 3,600-6,800 ft elevation; half forested; 20+ creeks; fire smoke funnels south toward Helena"},
            {"name": "Helena-Lewis and Clark NF", "bearing": "S/W", "type": "national_forest",
             "notes": "Surrounds Helena on south and west; mixed conifer forests; significant fire history including 1988 Elkhorn fire (37,000 acres)"},
            {"name": "Ten Mile Creek", "bearing": "W", "type": "drainage",
             "notes": "Major western drainage; municipal watershed; forested corridor providing fire pathway toward city"},
            {"name": "Elkhorn Mountains", "bearing": "SE", "type": "mountain_range",
             "notes": "1988 fire from faulty jeep exhaust grew from truck-sized to 37,000 acres; steep terrain, 2,500 firefighters deployed"},
        ],
        "elevation_range_ft": [3800, 5500],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Harris Mountain Fire", "year": 2021, "acres": 25000,
             "details": "Burned north of Helena; 13% contained at peak; simultaneous with Rock Creek and Woods Creek fires creating multi-front threat"},
            {"name": "Woods Creek Fire", "year": 2021, "acres": 12000,
             "details": "East of Helena; active at northwest and southeast corners; evacuation orders for Highway 284 area; highway closed"},
            {"name": "Rock Creek Fire", "year": 2021, "acres": 2560,
             "details": "North of Helena near Highway 287; Lewis & Clark County evacuated residents along Craig River Road; I-15 partially closed"},
            {"name": "Mount Helena Fire", "year": 2023, "acres": 18,
             "details": "Human-caused fire within Mount Helena City Park; demonstrated direct urban ignition risk; fire mitigation efforts praised"},
            {"name": "Elkhorn Mountains Fire", "year": 1988, "acres": 37000,
             "details": "Started from faulty jeep exhaust in Warm Springs Creek; grew from truck-sized to 2,500 acres overnight; 2,500 firefighters"},
            {"name": "North Helena Fire", "year": 1988, "acres": 34000,
             "details": "Late-season wildfire north of Sleeping Giant area; significant acreage in rugged terrain"},
        ],
        "evacuation_routes": [
            {"route": "I-15 North (toward Great Falls)", "direction": "N", "lanes": 4,
             "bottleneck": "Montana City interchange; merge with US-12 traffic",
             "risk": "2021 Rock Creek Fire forced partial I-15 closure; fires north of Helena can cut this route"},
            {"route": "I-15 South (toward Butte)", "direction": "S", "lanes": 4,
             "bottleneck": "Boulder Hill grade; construction zones",
             "risk": "South Hills fires could threaten southern approaches; generally most reliable evacuation route"},
            {"route": "US-12 West (toward Missoula)", "direction": "W", "lanes": 2,
             "bottleneck": "MacDonald Pass (6,325 ft); narrow, winding 2-lane over Continental Divide",
             "risk": "Helena NF fires along corridor; winter conditions make pass treacherous; long detour if closed"},
            {"route": "US-12 East (toward Townsend)", "direction": "E", "lanes": 2,
             "bottleneck": "Canyon Ferry Road narrows; limited passing zones",
             "risk": "Big Belt Mountain fires could close this corridor; serves as access to Canyon Ferry Dam area"},
            {"route": "Highway 284 (toward York/Trout Creek)", "direction": "NE", "lanes": 2,
             "bottleneck": "Narrow canyon road; limited capacity",
             "risk": "2021 Woods Creek Fire forced full closure; dead-end road beyond York for many residents"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Southwest winds dominate, channeled through gulches and valleys. Chinook winds from "
                "the west over the Continental Divide can produce rapid fire growth. Afternoon thermal "
                "winds drive upslope fire behavior on Mount Helena and South Hills. Valley inversions "
                "common in fall, trapping smoke."
            ),
            "critical_corridors": [
                "South Hills — direct forested WUI connection from Helena NF into residential areas",
                "Ten Mile Creek — western drainage corridor channeling fire toward city",
                "Last Chance Gulch — narrow historic downtown in fire-funneling terrain",
                "Prickly Pear Valley — eastern approach with grass fire potential",
                "Mount Helena City Park — 620 forested acres immediately above downtown",
            ],
            "rate_of_spread_potential": (
                "Moderate to high. South Hills terrain produces classic upslope fire runs in afternoon "
                "heating. Grass-to-timber transition on Mount Helena allows rapid fire development. "
                "The 1988 Elkhorn fire demonstrated overnight explosive growth (truck-sized to 2,500 acres) "
                "in similar fuel types."
            ),
            "spotting_distance": (
                "0.25-0.75 miles typical in ponderosa pine/Douglas fir fuel types; "
                "higher in Chinook wind events. South Hills fires could spot into residential "
                "neighborhoods within minutes."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "City of Helena water from Ten Mile Creek watershed and Missouri River wells. "
                "Ten Mile treatment plant vulnerable to fire in upper watershed. South Hills "
                "residential areas on higher-elevation pressure zones may lose pressure during "
                "high fire-flow demand."
            ),
            "power": (
                "NorthWestern Energy grid; transmission lines cross Helena NF and South Hills. "
                "State government buildings have backup generators but residential areas do not. "
                "Extended outages possible if fire damages transmission infrastructure."
            ),
            "communications": (
                "State capital has robust government communications infrastructure. Cell towers "
                "on Mount Helena and surrounding peaks are fire-exposed. Emergency Operations "
                "Center in Lewis and Clark County courthouse."
            ),
            "medical": (
                "St. Peter's Health (~120 beds) is the sole hospital; Level III trauma center. "
                "State capital location provides access to additional government emergency resources "
                "but single-hospital city is vulnerable to surge events during fire evacuations."
            ),
        },
        "demographics_risk_factors": {
            "population": 34729,
            "seasonal_variation": (
                "State government workforce (largest employer) is year-round. Carroll College adds "
                "~1,500 students. Tourism moderate in summer. Population relatively stable but "
                "surrounding Lewis and Clark County (pop 70,973) residents evacuate into Helena."
            ),
            "elderly_percentage": "~18% over 65 (median age 40.4, higher than state average)",
            "mobile_homes": (
                "Mobile home parks in Montana City area south of Helena and along US-12 east corridor; "
                "moderate concentration relative to city size."
            ),
            "special_needs_facilities": (
                "Montana State Capitol complex, state offices, Montana State Prison (Deer Lodge, 50 mi), "
                "multiple assisted living facilities, Carroll College dormitories, Helena Regional Airport."
            ),
        },
    },

    # =========================================================================
    # 3. KALISPELL / WHITEFISH, MT — Flathead Valley
    # =========================================================================
    "kalispell_whitefish_mt": {
        "center": [48.2148, -114.3130],
        "terrain_notes": (
            "Kalispell (pop ~31,000) and Whitefish (pop ~7,750) sit in the broad Flathead Valley "
            "of northwest Montana, the southern extension of the Rocky Mountain Trench that runs "
            "from the Yukon Territory into Montana. Kalispell lies at ~2,956 ft elevation on the "
            "valley floor, while Whitefish is at 3,028 ft at the northern tip of the valley, just "
            "25 miles west of Glacier National Park. The Flathead National Forest (2.4 million acres) "
            "dominates the landscape to the north, east, and west. Flathead Lake, the largest natural "
            "freshwater lake west of the Mississippi, lies to the south. The valley was formed by "
            "glaciers flowing down the Trench from British Columbia, leaving a flat floor surrounded "
            "by steep, forested mountains. Flathead County's WUI amounts to 37% of total land area — "
            "the largest landowner is the US Forest Service. The 2003 fire season devastated the region: "
            "the Robert Fire burned 57,570 acres in Glacier NP and Flathead NF, forcing evacuations of "
            "West Glacier and Apgar. The valley has experienced extreme growth with homes built within "
            "or adjacent to forest lands, often on steep terrain or hilltops. Decades of fire suppression "
            "have created dangerous fuel accumulations. The fire regime is classified as mixed to high "
            "severity, meaning large fires can be stand-replacing crown fires."
        ),
        "key_features": [
            {"name": "Flathead National Forest", "bearing": "N/E/W", "type": "national_forest",
             "notes": "2.4 million acres surrounding valley; mixed to high severity fire regime; decades of fuel buildup from suppression"},
            {"name": "Glacier National Park", "bearing": "NE", "type": "national_park",
             "notes": "25 mi from Whitefish; 2003 fires burned 13% of park (136,000 acres); fire source for NW winds"},
            {"name": "Flathead Lake", "bearing": "S", "type": "lake",
             "notes": "Largest natural freshwater lake W of Mississippi; southern boundary of valley; potential firebreak"},
            {"name": "Whitefish Range", "bearing": "NW", "type": "mountain_range",
             "notes": "Active USFS fuel mitigation project ($2M+); steep forested terrain directly above Whitefish; WUI exposure"},
            {"name": "Swan Range", "bearing": "E", "type": "mountain_range",
             "notes": "Eastern valley wall; steep, heavily forested; fires here produce smoke that settles into valley"},
            {"name": "Flathead River", "bearing": "through valley", "type": "river",
             "notes": "North and Middle Forks converge in valley; riparian corridors but not effective firebreaks for crown fire"},
            {"name": "Columbia Falls", "bearing": "NE of Kalispell", "type": "community",
             "notes": "Pop 4,688; gateway community to Glacier; directly in path of NE-origin fires"},
        ],
        "elevation_range_ft": [2900, 7500],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Robert Fire", "year": 2003, "acres": 57570,
             "details": "Human-caused; burned in Glacier NP and Flathead NF; jumped North Fork Flathead River; forced evacuations of Lake McDonald Valley, West Glacier, and Apgar; $68M+ cost for 2003 fire season in park; 5,000-acre tactical burnout saved communities"},
            {"name": "Wedge Canyon Fire", "year": 2003, "acres": 53314,
             "details": "Part of 2003 fire complex in Glacier NP; 26 wildfires scorched ~13% of park that season"},
            {"name": "Moose Fire", "year": 2001, "acres": 71000,
             "details": "Burned in Flathead NF north of Glacier; demonstrated scale of potential fire events in the region"},
            {"name": "Red Meadow Fire", "year": 2003, "acres": 17000,
             "details": "Additional 2003 fire season blaze in Flathead NF; contributed to regional smoke and resource strain"},
        ],
        "evacuation_routes": [
            {"route": "US-93 South (toward Polson/Missoula)", "direction": "S", "lanes": 4,
             "bottleneck": "Kalispell Bypass; Flathead Lake narrows road to 2 lanes at Elmo/Polson",
             "risk": "Long distance to next major city (Missoula, 120 mi); fires along corridor possible"},
            {"route": "US-93 North (toward Eureka/Canada)", "direction": "N", "lanes": 2,
             "bottleneck": "2-lane road; Whitefish congestion; narrow Tobacco Valley",
             "risk": "Heads deeper into forested North Fork area; limited Canadian border crossing capacity"},
            {"route": "US-2 East (toward Glacier/Browning)", "direction": "E", "lanes": 2,
             "bottleneck": "Marias Pass (5,213 ft); narrow canyon sections",
             "risk": "2003 fires closed areas along this corridor; passes through fire-prone Flathead NF"},
            {"route": "US-2 West (toward Libby/Idaho)", "direction": "W", "lanes": 2,
             "bottleneck": "2-lane through mountainous terrain; limited passing",
             "risk": "Remote corridor through Kootenai NF; fire can close road for extended periods"},
            {"route": "MT-35 (east shore Flathead Lake)", "direction": "SE", "lanes": 2,
             "bottleneck": "Narrow lakeside road; limited capacity",
             "risk": "Scenic route with steep terrain; not suitable for mass evacuation"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Prevailing westerly and southwesterly winds channel through the Rocky Mountain Trench. "
                "Strong downslope (Chinook/foehn) winds from the Continental Divide can produce extreme "
                "fire behavior. Valley thermals create afternoon up-valley winds. Pacific weather systems "
                "bring dry lightning in July-August."
            ),
            "critical_corridors": [
                "Whitefish Range — steep forested slopes directly above Whitefish residential areas",
                "North Fork Flathead — fire approach corridor from Glacier NP area",
                "Swan Valley — eastern approach with continuous forest fuel",
                "Stillwater corridor — river valley connecting wildlands to Kalispell suburbs",
                "Columbia Falls gateway — funnel point between park and valley communities",
            ],
            "rate_of_spread_potential": (
                "High to extreme. Mixed to high severity fire regime means crown fires are expected. "
                "The Robert Fire demonstrated rapid growth (7,000 acres in first few days) and ability "
                "to jump major rivers. Decades of suppression have created ladder fuels throughout "
                "the valley's forested WUI."
            ),
            "spotting_distance": (
                "1-2+ miles in wind-driven crown fire events. Robert Fire jumped the North Fork "
                "Flathead River. Conifer bark and ember transport in Trench winds can carry ignition "
                "sources well ahead of the fire front."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Kalispell municipal water from wells and Ashley Creek watershed. Whitefish draws from "
                "Whitefish Lake. Both systems adequate for normal operations but simultaneous structure "
                "fires in WUI areas could exceed capacity, especially for outlying developments on "
                "private wells."
            ),
            "power": (
                "Flathead Electric Cooperative and NorthWestern Energy. Transmission lines traverse "
                "Flathead NF; vulnerable to fire damage. Glacier Park area has limited redundant power "
                "infrastructure. Rolling outages possible during extreme fire events."
            ),
            "communications": (
                "Cell coverage good in valley floor but gaps in surrounding mountains and drainages. "
                "North Fork area has extremely limited communications. Emergency radio repeaters on "
                "mountain peaks are fire-exposed."
            ),
            "medical": (
                "Logan Health Medical Center in Kalispell (~577 beds systemwide across 5 hospitals) is the "
                "regional referral center with 400+ physicians. Logan Health-Whitefish is a 25-bed "
                "Critical Access Hospital serving 30,000+ people. North Valley Hospital in Whitefish "
                "provides additional capacity. Regional center adequate but 100+ mile distance to next "
                "major medical center (Missoula)."
            ),
        },
        "demographics_risk_factors": {
            "population": 38750,
            "seasonal_variation": (
                "Massive summer tourism surge from Glacier National Park (3+ million visitors/year). "
                "Whitefish Mountain Resort brings winter tourism. Summer population in broader Flathead "
                "Valley may double. Tourist population unfamiliar with fire evacuation routes."
            ),
            "elderly_percentage": "~18% over 65 (Whitefish skews older/wealthier; Kalispell more mixed)",
            "mobile_homes": (
                "Scattered mobile home parks throughout valley, especially along US-93 corridor "
                "between Kalispell and Whitefish and in Evergreen area east of Kalispell."
            ),
            "special_needs_facilities": (
                "Logan Health hospital complex, multiple assisted living/memory care facilities, "
                "Flathead Valley Community College, seasonal workforce housing (limited quality), "
                "Glacier Park lodges and campgrounds with transient populations."
            ),
        },
    },

    # =========================================================================
    # 4. HAMILTON, MT — Bitterroot Valley
    # =========================================================================
    "hamilton_mt": {
        "center": [46.2468, -114.1594],
        "terrain_notes": (
            "Hamilton (pop ~4,659) is the county seat of Ravalli County, situated at 3,570 ft "
            "elevation in the heart of the Bitterroot Valley of southwestern Montana. The valley "
            "extends ~95 miles from Lost Trail Pass (Idaho border) north to Missoula, with the "
            "Bitterroot Range (steep, heavily forested, 7,000-9,000 ft peaks) to the west and the "
            "Sapphire Mountains (more rounded, drier, less forested) to the east. The Bitterroot "
            "River flows north through the valley floor. Hamilton sits at a moderate-width point in "
            "the valley where deep canyons from the Bitterroot Range — including Blodgett Canyon, "
            "Mill Creek, and Sleeping Child — channel directly toward town. The 2000 Bitterroot "
            "fire season was among the most catastrophic in US history: 356,000 acres burned, 70 homes "
            "and 170 structures destroyed, 1,500+ evacuated, and the valley was declared a national "
            "disaster area. On July 31, 2000, a single dry lightning storm ignited 70+ fires in the "
            "Bitterroot Mountains. On 'Black Sunday' (Aug 6, 2000), multiple fires merged into massive "
            "complexes. Ravalli County is one of Montana's fastest-growing counties (pop 44,174), with "
            "84.4% of residents living in rural areas — many building homes in the trees. Over 162,000 "
            "acres of high-risk forest remain in the valley's WUI."
        ),
        "key_features": [
            {"name": "Bitterroot Range", "bearing": "W", "type": "mountain_range",
             "notes": "Longest single range in Rockies; steep faces, deep canyons, heavily forested; within Bitterroot NF (1.6M acres); 50% designated wilderness"},
            {"name": "Sapphire Mountains", "bearing": "E", "type": "mountain_range",
             "notes": "More rounded, drier, less forested than Bitterroots; grass/shrub fire regime; faster fire spread on open terrain"},
            {"name": "Bitterroot River", "bearing": "N-S through valley", "type": "river",
             "notes": "Primary drainage; north-flowing; riparian corridor but insufficient as crown fire barrier"},
            {"name": "Blodgett Canyon", "bearing": "W", "type": "canyon",
             "notes": "Deep glacial canyon cutting into Bitterroots; dramatic fire runs possible down-canyon toward valley homes"},
            {"name": "Sleeping Child drainage", "bearing": "SW", "type": "drainage",
             "notes": "2000 Sleeping Child fire burned 38,000 acres; drainage channels directly toward Hamilton area"},
            {"name": "Bitterroot National Forest", "bearing": "W/S", "type": "national_forest",
             "notes": "1.6 million acres; 3 ranger districts (Stevensville, Darby/Sula, West Fork); largest continuous pristine wilderness in lower 48"},
        ],
        "elevation_range_ft": [3400, 7500],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Bitterroot Fires of 2000 (complex)", "year": 2000, "acres": 356000,
             "details": "Most expensive fire season in US history at the time; 70+ fires ignited by single lightning storm July 31; Black Sunday (Aug 6) saw massive blowup; 70 homes, 170 structures, 94 vehicles destroyed; 1,500+ evacuated; valley declared national disaster area; millions in suppression costs and property losses"},
            {"name": "Sleeping Child Fire", "year": 2000, "acres": 38000,
             "details": "Landmark fire in the Sleeping Child drainage southwest of Hamilton; part of the 2000 complex; threatened valley floor communities"},
            {"name": "Valley Complex Fire", "year": 2000, "acres": 120000,
             "details": "Multiple fires merged in West Fork Bitterroot River on Aug 6; largest single complex in the 2000 season"},
            {"name": "Bass Creek Fire", "year": 2000, "acres": 4000,
             "details": "Burned closer to valley floor near Florence; demonstrated fire reaching populated valley bottom"},
        ],
        "evacuation_routes": [
            {"route": "US-93 North (toward Missoula)", "direction": "N", "lanes": 2,
             "bottleneck": "Single primary highway for entire valley; bottleneck at Florence and Lolo",
             "risk": "The ONLY major evacuation route for entire southern Bitterroot Valley; 47 miles to Missoula; 1,500+ people evacuated on this road in 2000"},
            {"route": "US-93 South (toward Darby/Lost Trail Pass)", "direction": "S", "lanes": 2,
             "bottleneck": "Road narrows through Darby; Lost Trail Pass (7,014 ft) to Idaho",
             "risk": "Leads deeper into fire-prone country; 2000 fires burned on both sides of this road; Idaho side equally remote"},
            {"route": "MT-38 West (Skalkaho Pass to Anaconda)", "direction": "E", "lanes": 2,
             "bottleneck": "Unpaved mountain road; Skalkaho Pass (7,260 ft); seasonal closure",
             "risk": "Not suitable for mass evacuation; closed in winter; narrow switchbacks"},
            {"route": "MT-269 (Eastside Highway)", "direction": "N", "lanes": 2,
             "bottleneck": "Narrow rural road through farmland and small towns",
             "risk": "Parallel to US-93 on east side of valley; provides alternative but same general direction"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Afternoon thermal up-valley (south-to-north) winds at 10-20 mph driving fire north "
                "through the Bitterroot corridor. Strong westerly canyon winds from Bitterroot Range "
                "drainages during fire events. The 2000 fires demonstrated fire creating its own weather "
                "with pyroconvection columns and erratic wind shifts."
            ),
            "critical_corridors": [
                "West Fork Bitterroot — primary fire approach from the south/southwest wilderness",
                "Blodgett/Mill Creek canyons — channeled fire runs directly toward Hamilton",
                "Sleeping Child drainage — proven catastrophic fire corridor in 2000",
                "Valley floor grass/sage — allows rapid lateral fire spread between canyons",
                "US-93 corridor — timber and homes along highway create continuous fuel",
            ],
            "rate_of_spread_potential": (
                "Extreme. The 2000 Bitterroot fires set the national standard for catastrophic WUI "
                "fire events. Black Sunday (Aug 6, 2000) saw multiple fires merge and run tens of "
                "thousands of acres in a single day. Canyon winds can drive crown fire at 2-5 mph "
                "sustained through heavy timber. Grass fire on valley floor can spread at 10+ mph."
            ),
            "spotting_distance": (
                "1-3 miles in Bitterroot Range canyon wind events; the 2000 fires threw embers "
                "across the valley floor. Spot fires ignited ahead of the main fire front were a "
                "primary mechanism of the rapid fire spread during the complex."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Hamilton municipal water from wells. Rural areas on private wells with limited fire flow. "
                "2000 fires demonstrated water system overwhelmed when dozens of structures burning "
                "simultaneously. Rural volunteer fire departments have limited water tender capacity."
            ),
            "power": (
                "Ravalli Electric Cooperative; single transmission line through valley vulnerable to "
                "fire damage. Extended outages during 2000 fires. Many rural residences on single-line "
                "power feeds."
            ),
            "communications": (
                "Limited cell coverage in canyon areas and Bitterroot Range. Rural areas rely on "
                "landlines and radio. 2000 fires overwhelmed communications systems; evacuation "
                "notifications were delayed for some areas."
            ),
            "medical": (
                "Bitterroot Health (Marcus Daly Memorial Hospital) — small community hospital (~25 beds) "
                "founded 1931. Only hospital for entire Bitterroot Valley south of Missoula. "
                "Nearest Level II trauma center is 47 miles north in Missoula."
            ),
        },
        "demographics_risk_factors": {
            "population": 4659,
            "seasonal_variation": (
                "Ravalli County pop 44,174; one of Montana's fastest-growing counties. Summer recreation "
                "and tourism increase valley population. Many seasonal/second homes in forested WUI areas."
            ),
            "elderly_percentage": "~28% over 65 (median age 50.2 — significantly higher than state average; oldest-skewing county in MT)",
            "mobile_homes": (
                "Significant mobile home presence throughout valley; rural lots with single-wide "
                "units common; 84.4% of county residents in rural areas, many in fire-vulnerable settings."
            ),
            "special_needs_facilities": (
                "Marcus Daly Memorial Hospital, several assisted living facilities, Ravalli County "
                "fairgrounds (evacuation staging), rural schools scattered through valley."
            ),
        },
    },

    # =========================================================================
    # 5. SEELEY LAKE, MT — Clearwater Valley
    # =========================================================================
    "seeley_lake_mt": {
        "center": [47.1794, -113.4847],
        "terrain_notes": (
            "Seeley Lake (pop ~1,682) is a small resort and retirement community nestled in a "
            "heavily forested valley at approximately 4,000 ft elevation in northeastern Missoula "
            "County. The community sits between the Swan Range to the east and the Mission Mountains "
            "to the west, in the Seeley-Swan Valley — an 80-mile-long glacially carved corridor. "
            "The Clearwater River flows southwest out of Seeley Lake through a chain of glacially "
            "formed lakes into the Blackfoot River. Highway 83 is the sole road through the valley, "
            "connecting small rural communities. The area supports grizzly bears, gray wolves, and "
            "diverse ecosystems from valley grasslands to subalpine forests. In 2017, the Rice Ridge "
            "Fire burned 160,000+ acres and produced what peer-reviewed research identified as the "
            "worst sustained wildfire smoke event ever measured in the United States: PM2.5 levels "
            "peaked near 1,000-1,200 ug/m3 (the EPA 'hazardous' threshold is 250.5 ug/m3), with a "
            "24-hour average reaching 623.5 ug/m3. From July 31 to September 18, 2017 — 49 straight "
            "days — the daily PM2.5 average was 220.9 ug/m3. The Missoula City-County Health Department "
            "issued an unprecedented recommendation for all residents to evacuate. University of Montana "
            "research found sustained lung function decline in residents one year after exposure. "
            "The community has a median age of 62.6 years — one of the oldest in Montana — making "
            "it exceptionally vulnerable to smoke-related health impacts."
        ),
        "key_features": [
            {"name": "Swan Range", "bearing": "E", "type": "mountain_range",
             "notes": "Eastern valley wall; steep, heavily forested; fire source for westerly wind events; peaks to 9,000+ ft"},
            {"name": "Mission Mountains", "bearing": "W", "type": "mountain_range",
             "notes": "Western valley wall; tribal wilderness; deep timber; smoke from fires pools in valley between ranges"},
            {"name": "Seeley Lake (body of water)", "bearing": "center", "type": "lake",
             "notes": "Glacially formed lake; community surrounds shoreline; limited firebreak value for crown fire"},
            {"name": "Clearwater River", "bearing": "SW", "type": "river",
             "notes": "Flows SW from Seeley Lake to Blackfoot River; drainage corridor that channels smoke"},
            {"name": "Highway 83 corridor", "bearing": "N-S", "type": "road/corridor",
             "notes": "Only through-road in 80-mile valley; no alternatives; fire closure isolates community completely"},
            {"name": "Lolo National Forest (Seeley Lake RD)", "bearing": "surrounding", "type": "national_forest",
             "notes": "Ranger station in community; forest extends in all directions; continuous heavy fuel loading"},
        ],
        "elevation_range_ft": [3900, 9100],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Rice Ridge Fire", "year": 2017, "acres": 160000,
             "details": "Burned for nearly 2 months (July 31-Sept 18); produced worst sustained smoke event in US measurement history; PM2.5 peaked ~1,000-1,200 ug/m3 (4x hazardous threshold); 24-hr average reached 623.5 ug/m3; 49 consecutive days of hazardous air; health department recommended full community evacuation; UM research found persistent lung function decline in residents"},
            {"name": "Jocko Lakes Fire", "year": 2007, "acres": 36000,
             "details": "Burned west of Seeley Lake in Mission Mountains; contributed to smoke in valley"},
            {"name": "Fires of 1910 (Big Blowup)", "year": 1910, "acres": 3000000,
             "details": "Regional catastrophe burned 3 million acres across MT/ID in 2 days; Seeley-Swan Valley heavily impacted; defined US fire suppression policy for a century"},
        ],
        "evacuation_routes": [
            {"route": "MT-83 South (toward Clearwater Junction/MT-200)", "direction": "S", "lanes": 2,
             "bottleneck": "Single 2-lane road; Clearwater Junction intersection; 30 miles to MT-200",
             "risk": "THE ONLY southbound escape; fire on either side of valley can close road; smoke reduces visibility to near zero as demonstrated in 2017"},
            {"route": "MT-83 North (toward Condon/Swan Lake)", "direction": "N", "lanes": 2,
             "bottleneck": "Single 2-lane road; narrow valley; 60+ miles to Bigfork/Flathead Valley",
             "risk": "Leads deeper into remote forested valley; fire closure of MT-83 at any point isolates Seeley Lake completely"},
            {"route": "MT-200 (via Clearwater Junction)", "direction": "E/W", "lanes": 2,
             "bottleneck": "Must first reach Clearwater Junction (30 mi south on MT-83); then 2-lane highway",
             "risk": "Only connection to Missoula (60+ mi total) or Great Falls; Blackfoot Valley fire can close this route"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Valley-channeled winds between Swan Range and Mission Mountains create a natural "
                "chimney effect. Afternoon up-valley thermals drive fire northward. Nighttime drainage "
                "winds reverse. Strong inversions trap smoke in the narrow valley, creating the extreme "
                "PM2.5 concentrations observed in 2017. Ridgetop winds can be dramatically different "
                "from valley-floor conditions."
            ),
            "critical_corridors": [
                "Seeley-Swan Valley — entire 80-mile corridor is continuous fuel with no breaks",
                "Clearwater drainage — smoke and fire channel SW toward Blackfoot Valley",
                "Rice Ridge/Morrell Creek — demonstrated 2017 fire approach from NE",
                "Mission Mountains west slope — fires generate extreme smoke pooling in valley",
            ],
            "rate_of_spread_potential": (
                "Moderate to high for fire spread; EXTREME for smoke impact. The Rice Ridge Fire "
                "demonstrated that even moderate fire spread in surrounding terrain can create "
                "unsurvivable air quality conditions in the valley. Crown fire in the Swan or "
                "Mission ranges would generate massive smoke production funneled into the valley."
            ),
            "spotting_distance": (
                "0.5-1.5 miles in mountain terrain; valley configuration means spotting across "
                "the community is possible from fires on either range. Bark beetle-killed timber "
                "increases ember generation."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Community water district from wells. No municipal fire hydrant system outside "
                "immediate town core. Volunteer fire department with limited water tender capacity. "
                "Extended fire operations strain limited water resources."
            ),
            "power": (
                "Missoula Electric Cooperative; single transmission line through forested valley. "
                "Power outages common during fire events. No backup generation for community facilities. "
                "Extended outages isolate elderly residents dependent on medical equipment."
            ),
            "communications": (
                "Limited cell coverage; gaps in surrounding mountains. Satellite phone or ham radio "
                "may be only communication during fire events. Emergency notifications depend on "
                "functional cell infrastructure. No local radio station."
            ),
            "medical": (
                "Seeley Swan Medical Center — small clinic only; family medicine and dental. "
                "Described as 'the only spot with primary and dental care in about a 50-mile radius.' "
                "Nearest hospital is in Missoula, 60+ miles away (1+ hour drive in good conditions). "
                "No ambulance with advanced life support. Air evacuation limited by smoke conditions."
            ),
        },
        "demographics_risk_factors": {
            "population": 1682,
            "seasonal_variation": (
                "Resort community with significant summer population increase from recreationists, "
                "second-home owners, and campers in surrounding NF. Winter population drops. "
                "Peak fire season coincides with peak recreational use."
            ),
            "elderly_percentage": "~40%+ over 65 (median age 62.6 — among the oldest communities in Montana; extremely vulnerable to smoke/health impacts)",
            "mobile_homes": (
                "Significant mobile home and older cabin stock around lake and along Highway 83; "
                "many structures are seasonal/recreational with deferred maintenance."
            ),
            "special_needs_facilities": (
                "Small community clinic, volunteer fire department, no nursing home or assisted living. "
                "Elderly residents with mobility/health limitations dispersed in rural settings. "
                "Transportation assistance program available but limited capacity."
            ),
        },
    },

    # =========================================================================
    # 6. STEVENSVILLE, MT — Northern Bitterroot Valley
    # =========================================================================
    "stevensville_mt": {
        "center": [46.5100, -114.0930],
        "terrain_notes": (
            "Stevensville (pop ~2,015) is a small historic town in the northern Bitterroot Valley, "
            "flanked by the Bitterroot Range to the west and Sapphire Mountains to the east, at "
            "approximately 3,370 ft elevation. It is the home of the Stevensville Ranger District "
            "of the Bitterroot National Forest. The town sits near the Bitterroot River with canyons "
            "from the Bitterroot Range — including Bass Creek, Kootenai Creek, and St. Mary's Peak "
            "drainage — cutting directly toward the community. The Bitterroot Range west of "
            "Stevensville is the longest single mountain range in the Rocky Mountains, heavily "
            "forested with mixed conifer stands. During the 2000 Bitterroot fire season, fires "
            "threatened the Stevensville area from multiple directions; the Bass Creek Fire was one "
            "of the closer threats to the valley floor. More than 162,000 acres of high-risk forest "
            "remain in the valley's WUI. Ravalli County's rapid growth has placed many new homes "
            "'in the trees' — building in forested WUI settings without adequate defensible space."
        ),
        "key_features": [
            {"name": "Bitterroot Range", "bearing": "W", "type": "mountain_range",
             "notes": "Longest single range in Rockies; St. Mary's Peak (9,351 ft) is highest point; steep canyons channel fire toward valley"},
            {"name": "Sapphire Mountains", "bearing": "E", "type": "mountain_range",
             "notes": "Drier eastern range; grass/shrub fuel types allow fast lateral fire spread"},
            {"name": "Bass Creek", "bearing": "W", "type": "drainage",
             "notes": "2000 Bass Creek Fire (4,000 acres) demonstrated fire reaching valley floor near Stevensville"},
            {"name": "Kootenai Creek", "bearing": "W", "type": "drainage",
             "notes": "Deep canyon from Bitterroot wilderness; channeled fire approach toward community"},
            {"name": "Bitterroot River", "bearing": "through valley", "type": "river",
             "notes": "North-flowing river; limited firebreak for wind-driven fire"},
            {"name": "Stevensville Ranger District", "bearing": "surrounding", "type": "ranger_district",
             "notes": "Headquarters of Bitterroot NF Stevensville RD; manages 1.6M acres including wilderness"},
        ],
        "elevation_range_ft": [3300, 9400],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Bitterroot Fires of 2000", "year": 2000, "acres": 356000,
             "details": "Valley-wide catastrophe; 70 homes, 170 structures, 94 vehicles destroyed across Ravalli County; 1,500+ evacuated; national disaster declaration"},
            {"name": "Bass Creek Fire", "year": 2000, "acres": 4000,
             "details": "Burned near valley floor close to Stevensville/Florence; demonstrated fire penetrating to populated valley bottom"},
            {"name": "Kootenai Creek Fire", "year": 2003, "acres": 2000,
             "details": "Burned in canyon west of Stevensville; required evacuation of canyon residents"},
        ],
        "evacuation_routes": [
            {"route": "US-93 North (toward Missoula)", "direction": "N", "lanes": 2,
             "bottleneck": "Lolo/Missoula traffic merge; 25 miles to Missoula",
             "risk": "Shared evacuation corridor with all Bitterroot Valley communities; congestion likely in mass evacuation"},
            {"route": "US-93 South (toward Hamilton/Darby)", "direction": "S", "lanes": 2,
             "bottleneck": "Leads deeper into fire-prone valley",
             "risk": "Contraflow to 2000 fire locations; evacuating south during Bitterroot Range fires is dangerous"},
            {"route": "MT-269 (Eastside Highway)", "direction": "N/S", "lanes": 2,
             "bottleneck": "Narrow rural road; limited capacity",
             "risk": "Parallel alternative to US-93 but same general limitations; crosses agricultural land"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Up-valley thermal winds (south to north) during afternoon; canyon winds from Bitterroot "
                "Range drainages. Stevensville sits at a wider section of valley where multiple canyons "
                "converge, creating complex wind interactions during fire events."
            ),
            "critical_corridors": [
                "Bass Creek canyon — proven 2000 fire corridor to valley floor",
                "Kootenai Creek — deep canyon channeling fire east toward town",
                "St. Mary's Peak drainage — high-elevation fire could run downslope",
                "Valley floor grass/sage — lateral fire spread between canyon mouths",
            ],
            "rate_of_spread_potential": (
                "High in canyon wind events; moderate on valley floor. The 2000 fires demonstrated "
                "that canyon-channeled fires can reach the valley floor rapidly. Grass fire on the "
                "drier Sapphire Mountain side can spread very quickly."
            ),
            "spotting_distance": (
                "0.5-2 miles from canyon-exit fires into valley floor; similar to Hamilton-area "
                "fire behavior during 2000 season."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Small municipal water system from wells. Limited fire hydrant coverage outside "
                "town core. Surrounding rural areas on private wells with no fire flow capacity."
            ),
            "power": (
                "Ravalli Electric Cooperative; single distribution lines through forested areas. "
                "Extended outages during fire events common."
            ),
            "communications": (
                "Basic cell coverage in town; gaps in canyon areas. Volunteer fire department "
                "communications. Limited emergency notification capacity for dispersed rural residents."
            ),
            "medical": (
                "No hospital. Nearest hospital is Marcus Daly Memorial in Hamilton (15 mi south) "
                "or Missoula hospitals (25 mi north). Response time for ambulance: 15-30 minutes."
            ),
        },
        "demographics_risk_factors": {
            "population": 2015,
            "seasonal_variation": (
                "Moderate summer increase from recreation. Surrounding Ravalli County rural population "
                "of 44,174 adds dispersed vulnerable residents in WUI areas."
            ),
            "elderly_percentage": "~25% over 65 (consistent with Ravalli County median age of 50.2)",
            "mobile_homes": (
                "Rural lots with mobile homes common in surrounding areas; limited defensible space."
            ),
            "special_needs_facilities": (
                "Small town with limited special needs infrastructure; senior services through "
                "Ravalli County; volunteer fire/EMS."
            ),
        },
    },

    # =========================================================================
    # 7. SUPERIOR, MT — I-90 Corridor / Clark Fork Valley
    # =========================================================================
    "superior_mt": {
        "center": [47.1916, -114.8910],
        "terrain_notes": (
            "Superior (pop ~830) is the county seat of Mineral County, a remote town at 2,844 ft "
            "elevation on the northeast side of the Bitterroot Range in western Montana, situated "
            "in the narrow Clark Fork River valley where I-90 threads through mountainous terrain. "
            "The town occupies a tight valley floor with steep, forested hillsides rising immediately "
            "on both sides. The Clark Fork River runs through the valley, and the Bitterroot Mountains "
            "to the west along the Montana/Idaho border receive enormous precipitation — nearby "
            "Lookout Pass averages 400 inches of snow annually, supporting dense timber that becomes "
            "extreme fire fuel in summer. Flat Creek Canyon runs north out of Superior, creating a "
            "critical fire corridor. The West Mullan fire demonstrated the terrain challenges: flames "
            "headed north and east into steep uninhabited hillsides while across the Clark Fork River, "
            "both timber and houses were much thicker. Fire behavior in the Superior area is described "
            "as 'dictated by weather and topography' with very steep slopes, rough terrain, and "
            "limited access for firefighters. Mineral County has a population of just 4,535 across "
            "3,459 square miles — one of Montana's most sparsely populated and remote counties."
        ),
        "key_features": [
            {"name": "Clark Fork River", "bearing": "through valley", "type": "river",
             "notes": "River runs through Superior; narrow valley constrains town; limited firebreak for slope-driven fire"},
            {"name": "Bitterroot Range (west)", "bearing": "W", "type": "mountain_range",
             "notes": "Montana/Idaho border; extreme snowfall (400 in/yr at Lookout Pass) supports dense timber = extreme fuel"},
            {"name": "Flat Creek Canyon", "bearing": "N", "type": "canyon",
             "notes": "Runs north from Superior; identified as critical fire corridor concern during West Mullan fire"},
            {"name": "I-90 corridor", "bearing": "E-W", "type": "highway/valley",
             "notes": "Major interstate follows narrow Clark Fork valley; fire and smoke regularly impact traffic; headlights required during smoke events"},
            {"name": "Lookout Pass", "bearing": "W", "type": "mountain_pass",
             "notes": "Montana/Idaho border; 4,700 ft; heavy timber; fire can close I-90 over the pass"},
        ],
        "elevation_range_ft": [2700, 6500],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "West Mullan Fire", "year": 2005, "acres": 700,
             "details": "Started as grass fire, grew to 700 acres in one night; burned toward Flat Creek Canyon; timber and houses threatened across Clark Fork River"},
            {"name": "Prospect Fire", "year": 2003, "acres": 5000,
             "details": "Burned in remote steep terrain near I-90; limited access, very steep slopes; extremely difficult suppression"},
            {"name": "Fires of 1910 (Big Blowup)", "year": 1910, "acres": 3000000,
             "details": "Regional catastrophe; Clark Fork corridor was heavily impacted; fire ran through the Bitterroots destroying towns across MT/ID border region"},
        ],
        "evacuation_routes": [
            {"route": "I-90 East (toward Missoula)", "direction": "E", "lanes": 4,
             "bottleneck": "Narrow Clark Fork canyon; 50 miles to Missoula",
             "risk": "Fire and smoke regularly close I-90; headlights-at-noon visibility documented; only high-capacity route"},
            {"route": "I-90 West (toward Lookout Pass/Idaho)", "direction": "W", "lanes": 4,
             "bottleneck": "Lookout Pass (4,700 ft); mountain grade; heavy timber both sides",
             "risk": "Fire in Bitterroots can close I-90 over the pass; Idaho side equally remote (Wallace, 30 mi)"},
            {"route": "Local forest roads", "direction": "various", "lanes": 1,
             "bottleneck": "Single-lane gravel; gated; unmaintained sections",
             "risk": "Not viable for evacuation; may serve as last-resort escape for remote residents"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Valley winds channeled through the Clark Fork River corridor east-west. Slope-driven "
                "winds on steep hillsides above town. The narrow valley creates wind acceleration effects "
                "during fire events. Thermal inversions trap smoke in the valley, reducing visibility "
                "on I-90 to near zero."
            ),
            "critical_corridors": [
                "Flat Creek Canyon — primary fire corridor running north from Superior",
                "Clark Fork River valley — east-west wind tunnel; fire can run along valley",
                "West Mullan drainage — demonstrated grass-to-timber fire transition near town",
                "Lookout Pass corridor — dense timber on steep grades; potential for massive fire runs",
            ],
            "rate_of_spread_potential": (
                "High on steep slopes with heavy timber fuel loading. The West Mullan fire grew "
                "from grass fire to 700 acres overnight. Steep terrain above Superior means fires "
                "can run rapidly downhill toward town driven by slope and wind."
            ),
            "spotting_distance": (
                "0.5-1 mile typical in steep terrain; embers can cross Clark Fork River. "
                "Valley wind acceleration can increase spotting distance during blow-up events."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Small municipal system. Limited water storage and fire flow capacity for a town "
                "of 830 people. Surrounding areas on wells. Volunteer fire department with "
                "limited equipment."
            ),
            "power": (
                "Single transmission line through Clark Fork corridor; highly vulnerable to fire "
                "damage. Extended outages likely during any significant fire event. No backup "
                "generation for public facilities."
            ),
            "communications": (
                "Limited cell coverage; mountainous terrain creates dead zones. I-90 corridor has "
                "better coverage but side valleys have none. Emergency communications rely on "
                "radio repeaters on fire-exposed peaks."
            ),
            "medical": (
                "Mineral Community Hospital — critical access hospital with minimal beds. "
                "Nearest major hospital is Missoula (50 miles east) or Wallace, ID (30 miles west). "
                "Ambulance response to outlying areas can exceed 30 minutes."
            ),
        },
        "demographics_risk_factors": {
            "population": 830,
            "seasonal_variation": (
                "I-90 corridor brings through-traffic but limited tourism compared to other MT towns. "
                "Mineral County pop 4,535 across 3,459 sq mi — extremely dispersed rural population."
            ),
            "elderly_percentage": "~30%+ over 65 (median age 59.2 — very elderly community; limited mobility)",
            "mobile_homes": (
                "Significant mobile home stock in and around Superior; aging housing stock common "
                "in remote western Montana communities."
            ),
            "special_needs_facilities": (
                "Critical access hospital, volunteer fire/EMS, county courthouse. Very limited "
                "social services for such a remote and elderly population."
            ),
        },
    },

    # =========================================================================
    # 8. WEST YELLOWSTONE, MT — Park Gateway
    # =========================================================================
    "west_yellowstone_mt": {
        "center": [44.6621, -111.1041],
        "terrain_notes": (
            "West Yellowstone (pop ~1,272) is a gateway town to Yellowstone National Park, sitting "
            "at 6,660 ft elevation on the Madison Plateau in Gallatin County. The town occupies just "
            "0.80 square miles immediately adjacent to the park's west entrance, surrounded by Gallatin "
            "National Forest and Yellowstone NP on all sides. The terrain is a high-elevation plateau "
            "dominated by lodgepole pine — the same fuel type that carried the catastrophic 1988 "
            "Yellowstone fires across 793,880 acres (36% of the park). The 1988 fires are a defining "
            "event in American wildfire history: they questioned a century of fire suppression policy, "
            "demonstrated that fires can create their own weather systems, and showed that embers could "
            "be thrown a mile or more ahead of crown fire fronts. West Yellowstone itself nearly burned "
            "in September 1988 when an unexpected wind shift brought the North Fork Fire within 100 "
            "yards of structures, forcing emergency evacuations. The town holds the record for the "
            "lowest temperature ever recorded in the contiguous US (-66F) and has a subarctic climate, "
            "but summers bring extreme fire risk in the dense lodgepole forests. The town's economy "
            "is entirely tourism-dependent, with estimates of 41% Hispanic population and significant "
            "seasonal workforce housing challenges."
        ),
        "key_features": [
            {"name": "Yellowstone National Park", "bearing": "E/S", "type": "national_park",
             "notes": "West entrance directly adjacent; 2.2 million acres; 1988 fires burned 793,880 acres; lodgepole pine dominant fuel"},
            {"name": "Gallatin National Forest", "bearing": "N/W", "type": "national_forest",
             "notes": "Surrounds town on non-park sides; continuous lodgepole pine forest; fire from any direction threatens town"},
            {"name": "Madison Plateau", "bearing": "surrounding", "type": "plateau",
             "notes": "High elevation (6,660 ft) flat terrain; lodgepole pine monoculture = extreme crown fire potential"},
            {"name": "Madison River", "bearing": "W/N", "type": "river",
             "notes": "Flows northwest from park; limited firebreak value in lodgepole terrain"},
            {"name": "Hebgen Lake", "bearing": "NW", "type": "lake",
             "notes": "8 miles NW; potential refuge area but access road through forest"},
        ],
        "elevation_range_ft": [6500, 8000],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "North Fork Fire (1988 Yellowstone)", "year": 1988, "acres": 500000,
             "details": "Largest of the 1988 fires; human-caused; came within 100 yards of West Yellowstone structures; emergency evacuations Sept 6; wind shift nearly caused catastrophic loss; firefighters attempted bulldozer fire breaks"},
            {"name": "Yellowstone Fires Complex (1988)", "year": 1988, "acres": 793880,
             "details": "Combined acreage of all 1988 fires; 36% of park burned; high winds moved fire through tree crowns throwing embers 1+ mile ahead; 25,000 firefighters deployed; $120M suppression cost; fundamentally changed US fire policy"},
            {"name": "West Fork Fire", "year": 2024, "acres": 853,
             "details": "Burned near West Yellowstone in heavy fuel loading; steep terrain; 33% containment; demonstrated ongoing threat"},
            {"name": "Horn Fire", "year": 2024, "acres": 2000,
             "details": "17 miles NW of West Yellowstone between Cliff Lake and Highway 87; forced highway closure and evacuation warnings"},
        ],
        "evacuation_routes": [
            {"route": "US-191/US-287 North (toward Big Sky/Bozeman)", "direction": "N", "lanes": 2,
             "bottleneck": "Gallatin Canyon — narrow, winding 2-lane road through 50 miles of forest; limited passing",
             "risk": "Primary evacuation route but passes through dense forest for entire length; fire can close road; 90 miles to Bozeman"},
            {"route": "US-20 West (toward Idaho Falls)", "direction": "W", "lanes": 2,
             "bottleneck": "Targhee Pass (7,072 ft); forested mountain pass; 2-lane",
             "risk": "Crosses Continental Divide through lodgepole forest; 110 miles to Idaho Falls; fire can close pass"},
            {"route": "US-191 South (into Yellowstone NP)", "direction": "S", "lanes": 2,
             "bottleneck": "Park entrance; single road; 100+ miles to any other town via park roads",
             "risk": "NOT a viable evacuation route — leads into the park with fires, wildlife, and extremely long distances to exit"},
            {"route": "US-287 South (toward Hebgen Lake)", "direction": "S/W", "lanes": 2,
             "bottleneck": "2-lane through forest; connects to US-20 eventually",
             "risk": "Alternative to reach Idaho but through same forested terrain; earthquake-damaged Hebgen Dam area"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "High-elevation plateau winds with strong afternoon thermal development. The 1988 fires "
                "demonstrated that high winds (40+ mph) in this terrain produce unstoppable crown fire in "
                "lodgepole pine. Fires can create their own pyroconvective weather systems generating "
                "erratic winds. The town's flat, forested setting means fire can approach from any direction."
            ),
            "critical_corridors": [
                "Yellowstone NP west boundary — fire from park threatens town directly",
                "Gallatin Canyon corridor — continuous forest north toward Big Sky",
                "Madison Plateau — flat lodgepole terrain allows fire to run unimpeded",
                "Hebgen Lake area — fires west/northwest approach through dense timber",
            ],
            "rate_of_spread_potential": (
                "Extreme. Lodgepole pine crown fire in wind events can travel 5-10+ miles per day. "
                "The 1988 fires covered 10 miles in a single afternoon on multiple occasions. "
                "Flat terrain with continuous fuel and no natural firebreaks around West Yellowstone "
                "means any approaching crown fire can reach town without stopping."
            ),
            "spotting_distance": (
                "1-2+ miles documented in 1988 fires. High winds threw burning embers across rivers, "
                "roads, and prepared firebreaks. The North Fork Fire spotted ahead by a mile or more "
                "on multiple occasions, outpacing suppression efforts completely."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Small municipal system for ~1,300 permanent residents. Summer tourism may "
                "increase water demand 5-10x. Fire hydrant system limited to town core. "
                "Surrounding forest has no water infrastructure."
            ),
            "power": (
                "Remote grid connection; single transmission line through forested corridor. "
                "Power outages during fire events isolate the community. Backup generation "
                "limited to individual businesses."
            ),
            "communications": (
                "Cell coverage in town but gaps in surrounding forest and park. Park Service "
                "radio network provides some redundancy. Emergency communications dependent on "
                "cell towers in fire-exposed locations."
            ),
            "medical": (
                "West Yellowstone Clinic — small clinic only; no hospital. Nearest hospital is "
                "in Bozeman (90 miles north through Gallatin Canyon) or Idaho Falls (110 miles west). "
                "Air evacuation limited by smoke conditions and 6,660 ft elevation (reduced helicopter "
                "performance). Medical surge capacity essentially zero."
            ),
        },
        "demographics_risk_factors": {
            "population": 1272,
            "seasonal_variation": (
                "Extreme seasonal swing. Yellowstone NP receives 4+ million visitors/year; West "
                "Yellowstone is the primary west entrance gateway. Summer population may be 5-10x "
                "permanent residents on peak days. Thousands of tourists unfamiliar with fire risk, "
                "evacuation routes, or local conditions. International visitors (significant Chinese "
                "tourism) may face language barriers during evacuation."
            ),
            "elderly_percentage": "~10% over 65 (median age 33.3 — young due to seasonal workforce; BUT seasonal elderly tourists are significant)",
            "mobile_homes": (
                "Seasonal workforce housing includes mobile homes and temporary structures. "
                "Tourism economy creates housing instability."
            ),
            "special_needs_facilities": (
                "Small clinic, hotels/motels with transient populations, campgrounds in surrounding "
                "forest, seasonal workforce housing of varying quality. No assisted living or "
                "nursing facilities."
            ),
        },
    },

    # =========================================================================
    # 9. RED LODGE, MT — Beartooth Mountains
    # =========================================================================
    "red_lodge_mt": {
        "center": [45.1857, -109.2468],
        "terrain_notes": (
            "Red Lodge (pop ~2,257) is the county seat of Carbon County, situated at 5,562 ft "
            "elevation along Rock Creek at the northern edge of the Absaroka-Beartooth Wilderness "
            "adjacent to the Beartooth Mountains in south-central Montana. The town lies in a narrow "
            "valley surrounded by steep, forested terrain rising to peaks over 12,000 ft in the "
            "Beartooths. US Route 212 runs through town and south becomes the Beartooth Highway, "
            "a 68-mile National Scenic Byway open only late May to October. The community was "
            "devastated by the 2021 Robertson Draw Fire — a human-caused fire that burned 27,556 "
            "acres south of town, destroyed 21 structures, threatened 450 homes, and cost $10.5 "
            "million. In June 2022, catastrophic flooding on Rock Creek caused historic damage: "
            "100+ homes flooded, 8 public bridges washed away, the water main was compromised "
            "(town water shut off), and portions of Highway 212 were destroyed. A $14 million "
            "renovation project is ongoing. The community has a median age of 57.9 years and "
            "median household income of $43,857 — an aging, tourism-dependent mountain town "
            "with infrastructure still recovering from back-to-back fire and flood disasters."
        ),
        "key_features": [
            {"name": "Beartooth Mountains", "bearing": "S/W", "type": "mountain_range",
             "notes": "Part of Absaroka-Beartooth Wilderness; peaks to 12,799 ft (Granite Peak, MT highest); steep terrain, mixed conifer forest"},
            {"name": "Rock Creek", "bearing": "through town", "type": "creek/drainage",
             "notes": "Runs through center of Red Lodge; 2022 flooding crested at record 7.98 ft; destroyed bridges, water main, roads"},
            {"name": "Beartooth Highway (US-212)", "bearing": "S", "type": "highway/scenic_byway",
             "notes": "68-mi National Scenic Byway; seasonal (late May-Oct); only southern egress; connects to Yellowstone via Cooke City"},
            {"name": "Absaroka-Beartooth Wilderness", "bearing": "S/SW", "type": "wilderness",
             "notes": "944,000 acres; fire suppression limited in wilderness; natural fire starts common; source of Robertson Draw Fire approach"},
            {"name": "Mount Maurice area", "bearing": "S", "type": "mountain",
             "notes": "Origin point of Robertson Draw Fire; sage/grass at base transitions to timber; rapid fire spread terrain"},
        ],
        "elevation_range_ft": [5400, 12800],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Robertson Draw Fire", "year": 2021, "acres": 27556,
             "details": "Human-caused (spilled gasoline ignited by dirt bike spark plug); started 7 mi south of Red Lodge June 13; exploded to 24,470 acres in 3 days; 21 structures damaged; 450 homes threatened; evacuation orders south of Highway 308; $10.5M damage; felony arson charges filed"},
            {"name": "Rock Creek area fires", "year": 2006, "acres": 5000,
             "details": "Multiple fires in Rock Creek drainage; demonstrated fire approach through the primary valley toward town"},
        ],
        "evacuation_routes": [
            {"route": "MT-78 North (toward Columbus/I-90)", "direction": "N", "lanes": 2,
             "bottleneck": "2-lane highway; 60 miles to I-90 at Columbus",
             "risk": "Primary evacuation route; passes through open prairie/ranch land; generally reliable but long distance"},
            {"route": "US-212 South (Beartooth Highway)", "direction": "S", "lanes": 2,
             "bottleneck": "Seasonal road (closed Oct-May); mountain pass at 10,947 ft; extreme switchbacks",
             "risk": "NOT viable for winter evacuation; leads to extremely remote Cooke City (pop 75); 2021 Robertson Draw Fire burned along this corridor"},
            {"route": "MT-308 West (toward Belfry/Bridger)", "direction": "W", "lanes": 2,
             "bottleneck": "Narrow 2-lane; small rural communities only",
             "risk": "2021 evacuation orders covered area south of 308; limited capacity; leads to equally small communities"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Valley winds channeled along Rock Creek drainage. Afternoon thermal upslope winds "
                "on Beartooth front range. Chinook winds from the west can produce extreme conditions. "
                "The Robertson Draw Fire demonstrated rapid fire spread driven by afternoon winds in "
                "sage-grass transitioning to timber."
            ),
            "critical_corridors": [
                "Rock Creek drainage — primary fire approach corridor from south/southwest",
                "Robertson Draw — proven fire corridor reaching toward Red Lodge from south",
                "West Bench — residential areas above town on slopes of Beartooth foothills",
                "Highway 212 corridor — fire approach and escape route are the same road",
            ],
            "rate_of_spread_potential": (
                "High. Robertson Draw Fire grew from ignition to 24,470 acres in 72 hours. "
                "Sage-grass fuels at lower elevations allow very rapid initial spread; transition "
                "to timber at mid-elevation creates extreme fire behavior. Steep terrain multiplies "
                "rate of spread on upslope runs."
            ),
            "spotting_distance": (
                "0.5-1.5 miles in sage-grass/timber transition zone. Embers from crown fire "
                "in Beartooth timber can spot into town's forested residential areas."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Municipal water from Rock Creek watershed — ALREADY COMPROMISED by 2022 flood. "
                "Water main was cut during flooding; town water shut off entirely. $14M renovation "
                "underway but system remains fragile. Fire during construction period would be "
                "catastrophic for water supply."
            ),
            "power": (
                "Beartooth Electric Cooperative; transmission lines through forested mountain terrain. "
                "Extended outages during fire or flood events. 2022 flood damaged infrastructure still "
                "being repaired."
            ),
            "communications": (
                "Cell coverage in town; gaps in surrounding mountains and Beartooth wilderness. "
                "Emergency communications impacted by remote location."
            ),
            "medical": (
                "Beartooth Billings Clinic — critical access hospital with minimal beds. "
                "Nearest major hospital is Billings (60 miles NE on MT-78 and I-90). "
                "Helicopter evacuation limited by mountain weather. Median age of 57.9 means "
                "significant healthcare demand."
            ),
        },
        "demographics_risk_factors": {
            "population": 2257,
            "seasonal_variation": (
                "Significant tourism variation: winter population ~1,200 increasing to 1,800+ in summer. "
                "Beartooth Highway and Red Lodge Mountain ski area drive seasonal economy. "
                "Peak fire season coincides with peak tourism."
            ),
            "elderly_percentage": "~35% over 65 (median age 57.9 — extremely elderly community; highest-risk demographic for fire evacuation)",
            "mobile_homes": (
                "Moderate mobile home presence; aging housing stock typical of small Montana mountain towns."
            ),
            "special_needs_facilities": (
                "Critical access hospital, small assisted living facilities, county courthouse, "
                "vacation rentals with transient populations. Infrastructure still recovering from "
                "2022 flood — compound disaster vulnerability."
            ),
        },
    },

    # =========================================================================
    # 10. LINCOLN, MT — Continental Divide Community
    # =========================================================================
    "lincoln_mt": {
        "center": [46.9547, -112.6811],
        "terrain_notes": (
            "Lincoln (pop ~868) is an unincorporated community in Lewis and Clark County at 4,536 ft "
            "elevation in the upper Blackfoot River valley, astride Montana Highway 200 near the "
            "Continental Divide. The community extends approximately 6 miles east and 3 miles west "
            "along the Blackfoot River valley, surrounded by the Helena-Lewis and Clark National Forest. "
            "Highway 200 — the longest state highway in Montana at 706.6 miles — is the ONLY road "
            "through Lincoln, running northeast 87 miles over the Continental Divide to Great Falls "
            "and west 77 miles to Missoula. The community is one of Montana's most remote and isolated "
            "towns, with the nearest hospital 60+ miles away in either direction. The Continental "
            "Divide bisects the region, with the Sun River Canyon on the east slope and the Blackfoot "
            "Valley on the west. Fire history is extensive: the 2017 Alice Creek Fire burned 29,252 "
            "acres north of Lincoln in the Helena NF (part of the record 1.25-million-acre 2017 MT "
            "fire season), the Park Creek Fire started 2 miles north of Lincoln that same year, and "
            "the 2024 Black Mountain Fire forced evacuation orders for residents north of Highway 200. "
            "The economy has traditionally centered on timber harvesting and ranching. The community "
            "has a humid continental/subarctic climate with 85.4 inches of annual snowfall."
        ),
        "key_features": [
            {"name": "Continental Divide", "bearing": "NE", "type": "geographic_divide",
             "notes": "Bisects the region; fires can cross the divide; Alice Creek Fire did so in 2017; major weather boundary"},
            {"name": "Blackfoot River valley", "bearing": "E-W", "type": "river_valley",
             "notes": "Community spreads along 9-mile stretch of valley; forested hillsides on both sides; smoke pools in inversions"},
            {"name": "Helena-Lewis and Clark NF", "bearing": "surrounding", "type": "national_forest",
             "notes": "Forest surrounds community in all directions; continuous fuel; fire can approach from any direction"},
            {"name": "Montana Highway 200", "bearing": "E-W", "type": "highway",
             "notes": "Only road through community; 706.6 mi total length; 77 mi to Missoula, 87 mi to Great Falls; closure isolates Lincoln completely"},
            {"name": "Stonewall Creek area", "bearing": "N", "type": "subdivision/drainage",
             "notes": "Subdivision north of town; 2024 Black Mountain Fire approached from NW; evacuation orders issued"},
            {"name": "Alice Creek drainage", "bearing": "N", "type": "drainage",
             "notes": "Site of 2017 29,252-acre fire; fire crossed Continental Divide; rerouted CDT hikers to Hwy 200"},
        ],
        "elevation_range_ft": [4400, 7500],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Alice Creek Fire", "year": 2017, "acres": 29252,
             "details": "Lightning-caused; north of Lincoln in Helena NF; crossed the Continental Divide; part of record 2017 MT fire season (1.25M acres statewide); rerouted Continental Divide Trail hikers"},
            {"name": "Park Creek Fire", "year": 2017, "acres": 5000,
             "details": "Lightning-caused; started just 2 miles north of Lincoln; Stonewall Mountain Lookout trail closures; concurrent with Alice Creek creating multi-front threat"},
            {"name": "Black Mountain Fire", "year": 2024, "acres": 185,
             "details": "Several miles NW of Lincoln; evacuation orders for residents north of Highway 200; firefighters stopped spread toward Stonewall Creek subdivision"},
            {"name": "Canyon Creek Fire", "year": 1988, "acres": 250000,
             "details": "Massive fire in the region; contributed to the understanding of blowup fire behavior; 30-year retrospective published in local media"},
        ],
        "evacuation_routes": [
            {"route": "MT-200 West (toward Missoula)", "direction": "W", "lanes": 2,
             "bottleneck": "77 miles of 2-lane highway through forested Blackfoot Valley; passes through minimal communities",
             "risk": "Only westbound escape; Blackfoot Valley fires can close road; 1.5+ hours to Missoula in best conditions; fire approach from either side of valley threatens road"},
            {"route": "MT-200 East (toward Great Falls)", "direction": "NE", "lanes": 2,
             "bottleneck": "87 miles over Continental Divide; Rogers Pass (5,609 ft); narrow mountain road",
             "risk": "Longest route to help; crosses Continental Divide in fire-prone terrain; winter conditions make pass extremely dangerous; Helena NF fires threaten this corridor"},
            {"route": "Local forest roads", "direction": "various", "lanes": 1,
             "bottleneck": "Gravel, gated, seasonal; dead-end into national forest",
             "risk": "Not viable for evacuation; potential entrapment hazard for unfamiliar drivers"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Complex terrain-driven winds along the Continental Divide. Blackfoot Valley channels "
                "winds east-west. The Continental Divide creates its own weather with terrain-forced "
                "thunderstorms producing dry lightning — the 2017 fires were lightning-caused. "
                "Afternoon thermals drive upslope fire on valley walls."
            ),
            "critical_corridors": [
                "Alice Creek drainage — proven 29,000+ acre fire corridor north of town",
                "Blackfoot Valley — east-west corridor where town sits; channeled fire and smoke",
                "Park Creek — fire started just 2 miles from town in 2017",
                "Stonewall Creek — residential area threatened by 2024 fire from NW",
            ],
            "rate_of_spread_potential": (
                "Moderate to high. Mixed conifer forest in mountainous terrain. The Alice Creek Fire "
                "reached 29,252 acres and crossed the Continental Divide, demonstrating significant "
                "fire runs. Valley orientation can channel fire directly through the community."
            ),
            "spotting_distance": (
                "0.5-1 mile typical in mixed conifer terrain; Continental Divide winds can increase "
                "spotting distance during extreme events."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Unincorporated community; limited centralized water infrastructure. Many residents "
                "on private wells. No municipal fire hydrant system. Volunteer fire department with "
                "extremely limited water supply for structural firefighting."
            ),
            "power": (
                "Lincoln Electric Cooperative; single transmission line through forested valley. "
                "Any fire in the vicinity likely causes extended power outages. No backup generation "
                "for community facilities. Nearest line crews are 60+ miles away."
            ),
            "communications": (
                "Very limited cell coverage; mountainous terrain creates extensive dead zones. "
                "Many residents rely on landlines. Emergency notifications depend on word-of-mouth "
                "and local volunteer networks. No local radio station."
            ),
            "medical": (
                "Lincoln Health Center — small rural clinic only. No hospital. Nearest hospital is "
                "St. Peter's Health in Helena (60+ miles east) or Missoula hospitals (77 miles west). "
                "Ambulance response time from nearest hospital: 1+ hour. Air evacuation severely "
                "limited by smoke, terrain, and weather. The 60+ mile distance to hospital makes "
                "Lincoln one of the most medically isolated communities in Montana."
            ),
        },
        "demographics_risk_factors": {
            "population": 868,
            "seasonal_variation": (
                "Modest summer recreation increase; Continental Divide Trail hikers pass through. "
                "Population declined from 1,005 to 868 between 2022-2023. Seasonal residents and "
                "cabin owners increase summer population somewhat."
            ),
            "elderly_percentage": "~35% over 65 (median age 56.8 — very elderly community; isolated from medical care)",
            "mobile_homes": (
                "Common housing type in Lincoln area; older manufactured homes with deferred "
                "maintenance. Limited defensible space around many structures."
            ),
            "special_needs_facilities": (
                "Small clinic only. No assisted living, no nursing facility, no pharmacy. "
                "Elderly residents with medical needs are extremely vulnerable during fire events "
                "due to isolation and distance from any hospital."
            ),
        },
    },

    # =========================================================================
    # 11. LOLO, MT — Bitterroot Gateway
    # =========================================================================
    "lolo_mt": {
        "center": [46.7576, -114.0821],
        "terrain_notes": (
            "Lolo (pop ~4,399) is a census-designated place in Missoula County at 3,198 ft elevation, "
            "positioned at the confluence of Lolo Creek and the Bitterroot River approximately 8 miles "
            "south of Missoula. The community serves as the gateway to the Bitterroot Mountains and "
            "the Lolo National Forest, and as the eastern approach to Lolo Pass (5,233 ft) — the key "
            "route into Idaho via US-12. Lolo occupies 9.63 square miles at a critical geographic "
            "pinch point where the Bitterroot Valley meets the Missoula Valley and where Lolo Creek "
            "emerges from a deep forested canyon to the west. The 2017 Lolo Peak Fire burned 53,902 "
            "acres on the western flank of Lolo Peak (9,096 ft), evacuating 3,000+ people and "
            "threatening 1,150 residences. One firefighter was killed. The fire burned 9,000 acres in "
            "a single 24-hour wind event, with strong canyon winds racing the fire eastward toward "
            "residential areas. The 2013 Lolo Creek Complex was equally terrifying: high winds down "
            "the Lolo Creek Valley turned the West Fork Two fire into a 'blow torch,' jumping the "
            "highway and merging with the Schoolhouse Fire — residents reported having no time for "
            "evacuation warnings. Five homes burned, demonstrating catastrophic WUI fire behavior. "
            "Lolo has grown 26.1% between 2011-2023, adding 1,362 people in fire-vulnerable terrain."
        ),
        "key_features": [
            {"name": "Lolo Peak", "bearing": "SW", "type": "mountain",
             "notes": "9,096 ft; highest point on Lolo NF; 2017 fire burned 53,902 acres on its flanks; iconic Missoula-area landmark"},
            {"name": "Lolo Creek", "bearing": "W", "type": "creek/canyon",
             "notes": "Deep forested canyon running west to Lolo Pass; proven fire corridor; 2013 fire blowup here; canyon winds funnel fire toward town"},
            {"name": "Bitterroot River confluence", "bearing": "E", "type": "river",
             "notes": "Lolo Creek joins Bitterroot River at Lolo; town sits at this junction; fire from either drainage threatens community"},
            {"name": "US-12 / Lolo Pass corridor", "bearing": "W", "type": "highway/pass",
             "notes": "Route to Idaho; 5,233 ft pass through Lolo NF; fire can close this highway for extended periods"},
            {"name": "US-93 corridor", "bearing": "N-S", "type": "highway",
             "notes": "Primary Bitterroot Valley highway; connects Lolo to Missoula (8 mi N) and Hamilton (39 mi S)"},
            {"name": "Lolo National Forest", "bearing": "W/S", "type": "national_forest",
             "notes": "2.3 million acres; fire danger regularly reaches 'very high' to 'extreme' in summer"},
        ],
        "elevation_range_ft": [3100, 9100],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Lolo Peak Fire", "year": 2017, "acres": 53902,
             "details": "Lightning-caused on Lolo Peak July 15; 3,000+ evacuated; 1,150 residences threatened; 2 homes destroyed; firefighter Brent Witham killed; 9,000 acres burned in single wind-driven 24-hour run; fire raced eastward toward residences driven by canyon winds"},
            {"name": "Lolo Creek Complex", "year": 2013, "acres": 12000,
             "details": "West Fork Two fire became 'blow torch' in Lolo Creek Valley winds; jumped highway; merged with Schoolhouse Fire; 5 homes burned; residents had no evacuation warning time; graphic demonstration of defensible space importance"},
            {"name": "Bitterroot Fires of 2000", "year": 2000, "acres": 356000,
             "details": "Valley-wide catastrophe; Lolo at the northern end of the Bitterroot corridor was impacted by smoke and fire threat from the south"},
        ],
        "evacuation_routes": [
            {"route": "US-93 North (toward Missoula)", "direction": "N", "lanes": 4,
             "bottleneck": "Lolo/Missoula traffic merge; US-93/US-12 interchange congestion",
             "risk": "Primary and most viable evacuation route; 8 miles to Missoula; BUT Lolo Peak fire smoke filled this corridor and fire approach can threaten road"},
            {"route": "US-93 South (toward Florence/Hamilton)", "direction": "S", "lanes": 2,
             "bottleneck": "2-lane through Bitterroot Valley; shared with all valley evacuees",
             "risk": "Leads deeper into fire-prone Bitterroot Valley; contraflow to 2000 fire locations"},
            {"route": "US-12 West (toward Lolo Pass/Idaho)", "direction": "W", "lanes": 2,
             "bottleneck": "2-lane through Lolo Creek Canyon; narrow; Lolo Pass at 5,233 ft",
             "risk": "2013 fire blowup occurred in this exact canyon; fire jumped the highway; EXTREMELY DANGEROUS during fire events; proven death trap potential"},
            {"route": "Local roads (toward Florence via Eastside)", "direction": "SE", "lanes": 2,
             "bottleneck": "Rural roads through agricultural areas",
             "risk": "Alternative to US-93 but limited capacity; connects to same eventual corridors"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Complex interaction of Bitterroot Valley up-valley winds (south to north), Lolo Creek "
                "canyon winds (west to east), and Missoula Valley drainage. Afternoon thermal development "
                "drives upslope fire on Lolo Peak and surrounding mountains. The 2017 fire demonstrated "
                "that strong canyon winds from the west can drive fire rapidly eastward across the mountain "
                "face toward residential areas. The 2013 Lolo Creek Complex showed that valley winds "
                "can create blow-torch conditions in the canyon, jumping roads and structures."
            ),
            "critical_corridors": [
                "Lolo Creek Canyon — proven 2013 blowup corridor; fire jumped highway",
                "Lolo Peak western slope — 2017 fire ran 9,000 acres in 24 hours toward town",
                "Bitterroot Valley approach — fire from Hamilton/Florence area runs north toward Lolo",
                "US-12 highway corridor — evacuation route and fire corridor are the same road",
            ],
            "rate_of_spread_potential": (
                "Extreme during wind events. The 2017 Lolo Peak Fire burned 5,000 acres in a single "
                "night and 9,000 in 24 hours. The 2013 Lolo Creek Complex went from manageable to "
                "catastrophic in minutes when canyon winds arrived. Rate of spread in Lolo Creek Canyon "
                "during the 2013 blowup was described as 'blowtorch' conditions."
            ),
            "spotting_distance": (
                "0.5-1.5 miles in canyon wind events. The 2013 fire spotted across the highway. "
                "Embers from Lolo Peak fire carried by canyon winds threatened residential areas "
                "well ahead of the fire front."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Lolo Water District serves the community from wells. Growing population (26.1% "
                "increase 2011-2023) strains water system. Outlying homes on private wells with "
                "no fire flow. Homes in Lolo Creek canyon have extremely limited water access."
            ),
            "power": (
                "Missoula Electric Cooperative; transmission lines through forested Lolo Creek "
                "corridor and along US-93. Fire damage to power lines is common during events. "
                "No backup generation for community."
            ),
            "communications": (
                "Cell coverage adequate in town but gaps in Lolo Creek canyon and surrounding "
                "mountains. The 2013 fire demonstrated that residents received no evacuation "
                "warning before fire jumped the highway — communications failure during rapid events."
            ),
            "medical": (
                "No hospital or clinic in Lolo. Dependent on Missoula hospitals (8 miles north) — "
                "Providence St. Patrick and Community Medical Center. Response time generally adequate "
                "but fire/smoke on US-93 corridor between Lolo and Missoula can delay ambulance access. "
                "Community's proximity to Missoula is both its greatest asset and vulnerability."
            ),
        },
        "demographics_risk_factors": {
            "population": 4399,
            "seasonal_variation": (
                "Growing bedroom community for Missoula; 26.1% population increase 2011-2023. "
                "US-12 corridor to Idaho brings through-traffic. Lolo Hot Springs recreation area "
                "adds summer visitors. Many new residents may not understand local fire risk."
            ),
            "elderly_percentage": "~15% over 65 (younger than state average due to Missoula commuter population)",
            "mobile_homes": (
                "Several mobile home parks along US-93 and in Lolo area; vulnerable to fire and "
                "limited defensible space."
            ),
            "special_needs_facilities": (
                "Lolo School, volunteer fire department, small commercial district. Dependent on "
                "Missoula for all hospital, social service, and emergency management resources. "
                "Rapid growth (1,362 new residents) may outpace emergency services capacity."
            ),
        },
    },
}


# =============================================================================
# Summary statistics
# =============================================================================
def print_summary():
    """Print summary of all profiles in the dataset."""
    print("=" * 80)
    print("MONTANA FIRE-VULNERABLE CITY PROFILES — SUMMARY")
    print("=" * 80)
    total_pop = 0
    for key, profile in PNW_MONTANA_ENHANCED.items():
        pop = profile["demographics_risk_factors"]["population"]
        total_pop += pop
        n_fires = len(profile["historical_fires"])
        n_routes = len(profile["evacuation_routes"])
        wui = profile["wui_exposure"]
        elev = profile["elevation_range_ft"]
        print(f"\n  {key}")
        print(f"    Population: {pop:,}  |  WUI: {wui}  |  Elev: {elev[0]:,}-{elev[1]:,} ft")
        print(f"    Historical fires: {n_fires}  |  Evacuation routes: {n_routes}")
        print(f"    Center: {profile['center']}")
    print(f"\n{'=' * 80}")
    print(f"  TOTAL COMMUNITIES: {len(PNW_MONTANA_ENHANCED)}")
    print(f"  TOTAL POPULATION AT RISK: {total_pop:,}")
    print(f"{'=' * 80}")


if __name__ == "__main__":
    print_summary()
