"""
Idaho Fire-Vulnerable City Profiles — Research-Paper Quality
=============================================================
Enhanced profiles for 10 fire-vulnerable Idaho communities.
Includes terrain analysis, historical fire data, evacuation infrastructure,
fire spread characteristics, and demographic risk factors.

Sources:
- USFS InciWeb incident reports (2007-2024)
- Ada Fire Adapted Communities (ADAFAC)
- Boise State University Hazard & Climate Resilience Institute
- Idaho Department of Lands fire statistics
- NOAA/NWS fire weather data
- US Census Bureau (2020 Census)
- First Street Foundation wildfire risk assessments
- Idaho Capital Sun, KTVB, Mountain Express reporting
- USFS Southwest Idaho Wildfire Crisis Landscape Project
- Sawtooth Wildland Fire Collaborative
"""

PNW_IDAHO_ENHANCED = {

    # =========================================================================
    # 1. BOISE, ID — Enhanced (foothills WUI, Boise Front)
    # =========================================================================
    "boise_id": {
        "center": [43.6150, -116.2023],
        "terrain_notes": (
            "Boise (pop ~240,000) sits at the interface of the Snake River Plain and the Boise "
            "Front — a dramatic escarpment of foothill ridges rising 2,500-3,000 ft above the city "
            "floor within 2-3 miles. The Boise Front extends ~30 miles along the city's northern "
            "edge, from Lucky Peak Dam on the east to Eagle on the west, creating one of the most "
            "extensive wildland-urban interface zones in the American West. Subdivision development "
            "has pushed deep into foothill drainages including Hulls Gulch, Crane Creek, Dry Creek, "
            "Bogus Basin Road corridor, and the Table Rock/Warm Springs Mesa area. The terrain is "
            "characterized by steep, south-facing grass and sagebrush slopes that cure rapidly by "
            "late June, interspersed with draws that channel both wind and fire upslope. The "
            "1992 Foothills Fire (257,000 acres), 1996 8th Street Fire (15,300 acres), 2016 Table "
            "Rock Fire (2,600 acres), and 2024 Valley Fire (9,904 acres) all demonstrate the "
            "recurring ignition risk. Ada County's Community Wildfire Protection Plan identifies "
            "seven Firewise Communities and has invested over $1M in fuel treatments, but the pace "
            "of WUI development continues to outstrip mitigation. Humans cause >80% of Treasure "
            "Valley wildfires. The BLM manages most foothills land, complicating jurisdictional "
            "response with Boise Fire Department, Ada County, and federal agencies all overlapping."
        ),
        "key_features": [
            {"name": "Table Rock", "bearing": "ENE", "type": "landmark",
             "notes": "Iconic sandstone butte above city; 2016 fire origin. Steep grass slopes funnel fire toward Warm Springs residential area."},
            {"name": "Boise Front Ridgeline", "bearing": "N", "type": "terrain",
             "notes": "30-mile escarpment rising 2,500-3,000 ft above city. South-facing slopes cure early, creating fire-receptive fuels by late June."},
            {"name": "Bogus Basin Road Corridor", "bearing": "NNE", "type": "corridor",
             "notes": "Primary access to Bogus Basin ski area. Narrow two-lane road through dense WUI development in timber/brush transition zone."},
            {"name": "Hulls Gulch / Camelsback", "bearing": "N", "type": "drainage",
             "notes": "Deep drainage opening directly into North End residential neighborhood. Grass/sage fuels channel upslope winds into city."},
            {"name": "Lucky Peak Reservoir", "bearing": "E", "type": "water",
             "notes": "Dam and reservoir at east end of Boise Front. Highway 21 corridor to Idaho City passes through extreme fire terrain."},
            {"name": "Eagle Foothills", "bearing": "NW", "type": "terrain",
             "notes": "Rapidly developing WUI on western Boise Front. New subdivisions with limited egress into cheatgrass-dominated rangeland."},
        ],
        "elevation_range_ft": [2700, 7590],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Foothills Fire", "year": 1992, "acres": 257000,
             "details": "Massive range/forest fire across Boise Front. Burned for two weeks. Demonstrated catastrophic potential of foothills terrain."},
            {"name": "8th Street Fire", "year": 1996, "acres": 15300,
             "details": "Started by police officer firing tracer rounds at training range. Burned for 96 hours across Boise Foothills. Transformative event for local fire agencies."},
            {"name": "Table Rock Fire", "year": 2016, "acres": 2600,
             "details": "Human-caused (fireworks) on June 29. Destroyed 1 home that family had occupied 60+ years. Burned native grassland directly above east Boise neighborhoods."},
            {"name": "Valley Fire", "year": 2024, "acres": 9904,
             "details": "Caused by Idaho Power line contacting ground on Oct 4. Burned in east Boise foothills along Hwy 21 corridor. 79% contained, no structures lost but threatened homes in SE Boise."},
        ],
        "evacuation_routes": [
            {"route": "I-84 West", "direction": "W toward Nampa/Caldwell", "lanes": 6,
             "bottleneck": "Meridian interchange congestion; shared with normal commuter traffic",
             "risk": "Smoke from foothill fires can reduce visibility on I-84 connector routes"},
            {"route": "I-84 East", "direction": "E toward Mountain Home", "lanes": 4,
             "bottleneck": "Single corridor through canyon east of city; Lucky Peak Dam area",
             "risk": "Highway 21 junction directly in fire-prone terrain"},
            {"route": "Highway 55 North", "direction": "N toward Horseshoe Bend/McCall", "lanes": 2,
             "bottleneck": "Narrow canyon along Payette River; single road north",
             "risk": "Passes through extreme fire terrain in Boise NF; historically closed by fires"},
            {"route": "Highway 21 East", "direction": "NE toward Idaho City/Stanley", "lanes": 2,
             "bottleneck": "Winding mountain highway through Boise NF; frequently closed by wildfire",
             "risk": "2024 Valley Fire burned along this corridor; Pioneer Fire closed it in 2016"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Diurnal upslope/downslope cycle dominates. Afternoon SW winds push fire uphill into "
                "foothills at 15-25 mph. Nocturnal drainage winds reverse flow but are typically lighter. "
                "East wind events (rare but dangerous) drive fire downslope directly into populated areas. "
                "Thermal belt effects keep mid-slope fuels warm and dry overnight."
            ),
            "critical_corridors": [
                "Hulls Gulch — direct drainage into North End neighborhoods",
                "Table Rock / Warm Springs — steep grass slopes above dense residential",
                "Bogus Basin Road — timber/brush corridor with WUI development on both sides",
                "Dry Creek — Eagle foothills drainage into rapidly developing subdivisions",
                "Highway 21 corridor — Lucky Peak to Idaho City, extreme terrain fire runs"
            ],
            "rate_of_spread_potential": (
                "Grass/sage fuels on south-facing slopes support 3-5 mph head fire spread in "
                "moderate winds. Extreme conditions (as in 1992 Foothills Fire) can produce "
                "rates exceeding 6-8 mph with 100+ ft flame lengths in continuous grass. Cheatgrass "
                "invasion has increased fine fuel continuity across the entire Boise Front."
            ),
            "spotting_distance": (
                "0.25-0.5 miles typical in grass/sage; longer in timber transition zones above "
                "5,000 ft. Ember transport into residential areas is the primary home ignition mechanism — "
                "wind-blown embers are the main cause of structure ignition per Ada County CWPP."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Municipal system adequate for urban core but foothill subdivisions on smaller mains "
                "and some on private wells. Hydrant coverage thins rapidly above 3,200 ft elevation. "
                "Pressure issues in uphill subdivisions during high-demand firefighting operations."
            ),
            "power": (
                "Idaho Power overhead lines throughout foothills — 2024 Valley Fire caused by power "
                "line contact with ground. Wind events down lines regularly. Transformer fires can "
                "become ignition sources. Grid vulnerable to multi-point failure during large fires."
            ),
            "communications": (
                "Good cellular coverage in city and lower foothills. Gaps in deeper canyons (Hulls "
                "Gulch, Dry Creek upper reaches). CodeRED emergency notification system deployed by "
                "Ada County. Amateur radio backup networks established post-Table Rock Fire."
            ),
            "medical": (
                "St. Luke's Boise Medical Center (Level II Trauma), Saint Alphonsus Regional Medical "
                "Center, and VA Medical Center provide robust capacity. Medical infrastructure not a "
                "limiting factor for Boise proper, but access roads to foothill areas can be cut."
            ),
        },
        "demographics_risk_factors": {
            "population": 240000,
            "seasonal_variation": (
                "Year-round metro population ~770K (Treasure Valley). Summer recreation increases "
                "foothill trail usage dramatically — Boise River Greenbelt and Ridge to Rivers trail "
                "system see 1M+ annual visits, concentrating people in fire-prone terrain."
            ),
            "elderly_percentage": "~14% (65+), higher in some foothill neighborhoods",
            "mobile_homes": (
                "Limited in city proper but mobile home parks exist in Boise Bench and Garden City "
                "areas. More prevalent in unincorporated Ada County foothill fringe areas."
            ),
            "special_needs_facilities": (
                "Multiple assisted living facilities, hospitals, and schools in potential smoke "
                "impact zone. Boise State University campus (24,000 students) in Boise River "
                "corridor downwind of foothills."
            ),
        },
    },

    # =========================================================================
    # 2. McCALL, ID — Enhanced (Payette NF, mountain resort)
    # =========================================================================
    "mccall_id": {
        "center": [44.9108, -116.0987],
        "terrain_notes": (
            "McCall (pop ~3,700) sits on the southern shore of Payette Lake at 5,021 ft elevation, "
            "surrounded on three sides by the Payette National Forest. The town occupies a narrow "
            "bench between the lake and forested mountains that rise to 8,000-9,000 ft within a few "
            "miles. Dense lodgepole pine, Douglas-fir, and subalpine fir forests extend from the "
            "town boundary to the Selway-Bitterroot and Frank Church-River of No Return wilderness "
            "areas. The 2007 Cascade Complex fires burned over 300,000 acres in the Boise and "
            "Payette NFs with extreme fire behavior including 300-ft flame lengths, crown runs, "
            "and confirmed spotting distances of 5-7 miles (unconfirmed to 15 miles). McCall hosts "
            "a USFS Smokejumper Base on its municipal airport, making it a critical node in "
            "national fire response. The Southwest Idaho Wildfire Crisis Landscape Project "
            "identifies McCall as one of 14 community cores with elevated transboundary fire "
            "exposure risk. Population triples in summer with tourists and vacation homeowners. "
            "Highway 55 is the sole paved route south — a two-lane road through the Payette "
            "River canyon that is routinely threatened by fire and rock slides."
        ),
        "key_features": [
            {"name": "Payette Lake", "bearing": "N", "type": "water",
             "notes": "Glacier-carved, 4,987-acre lake (8.3 sq mi), max depth 304 ft. Northern shore is unroaded NF land. Provides natural firebreak on town's north side."},
            {"name": "McCall Smokejumper Base", "bearing": "S", "type": "infrastructure",
             "notes": "USFS smokejumper facility on McCall Airport. Critical national asset; one of few remaining active smokejumper bases."},
            {"name": "Brundage Mountain", "bearing": "NW", "type": "terrain",
             "notes": "Ski area 8 miles NW of town. Mixed conifer forest on steep terrain; fire in this drainage would threaten Warren Wagon Road corridor."},
            {"name": "Lick Creek Range", "bearing": "E", "type": "terrain",
             "notes": "8,000-9,000 ft range east of town. Dense forest with significant beetle-kill standing dead timber. Fire here would threaten east McCall."},
            {"name": "Warren Wagon Road", "bearing": "N", "type": "corridor",
             "notes": "Unpaved historic road north into remote backcountry. Only access to Warren and several trailheads. Single-track, no turnarounds."},
            {"name": "North Fork Payette River", "bearing": "S", "type": "drainage",
             "notes": "River corridor south toward Cascade. Highway 55 follows this canyon — fire or slides close the only paved route out."},
        ],
        "elevation_range_ft": [5021, 9100],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Cascade Complex", "year": 2007, "acres": 300000,
             "details": "Multiple fires merged in central Idaho. Extreme behavior on Aug 13 — 300-ft flame lengths, crown runs, confirmed 5-7 mile spotting. Burned in Payette and Boise NFs surrounding McCall region."},
            {"name": "Burgdorf Junction Fire", "year": 2003, "acres": 24000,
             "details": "Burned north of McCall in Payette NF. Threatened Warren Road corridor and remote communities."},
            {"name": "Rock Fire", "year": 2025, "acres": 2844,
             "details": "Lightning-caused fire near Tamarack Resort (20 mi S of McCall). Forced resort closure, Level 2 evacuations for west Lake Cascade residents. ~700 personnel deployed."},
        ],
        "evacuation_routes": [
            {"route": "Highway 55 South", "direction": "S toward Cascade/Boise", "lanes": 2,
             "bottleneck": "Payette River canyon — narrow, winding, single route south. 70+ miles to Boise through fire-prone terrain.",
             "risk": "Routinely threatened by wildfire. Rock slides and winter closures. No alternate paved route."},
            {"route": "Highway 55 North to New Meadows", "direction": "N toward US-95", "lanes": 2,
             "bottleneck": "30 miles to New Meadows junction. US-95 provides north-south alternative but adds 100+ miles.",
             "risk": "Forest-lined highway with fire exposure. Limited passing opportunities."},
            {"route": "Warren Wagon Road", "direction": "NE into backcountry", "lanes": 1,
             "bottleneck": "Unpaved, single-lane, no services. Dead-ends in remote Warren mining district.",
             "risk": "Not a viable evacuation route — leads deeper into fire-prone wilderness."},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Afternoon SW thermal winds 10-20 mph channeled by Payette River valley. Nighttime "
                "drainage winds from surrounding peaks. Thunderstorm outflows from July-August convection "
                "can produce erratic 40-60 mph gusts with dry lightning, as seen in the 2007 Cascade "
                "Complex when inversion breakup unleashed extreme fire behavior."
            ),
            "critical_corridors": [
                "Payette River canyon south — fire here cuts sole highway to Boise",
                "Lick Creek drainage east — dense forest funnels fire toward east McCall",
                "Lake Fork drainage — connects wildland fire to residential development",
                "Brundage Mountain NW slopes — steep terrain above Warren Wagon Road",
            ],
            "rate_of_spread_potential": (
                "Mixed conifer forests support 1-3 mph surface fire spread under moderate conditions. "
                "Crown fire in continuous canopy can achieve 3-5 mph. The 2007 Cascade Complex "
                "demonstrated that post-inversion breakup conditions produce very rapid crown runs "
                "with extreme spotting. Beetle-kill standing dead increases torching potential."
            ),
            "spotting_distance": (
                "5-7 miles confirmed during 2007 Cascade Complex, with unconfirmed reports of 15 miles. "
                "Terrain-amplified convective columns in mountain valleys can loft embers to extreme "
                "distances. McCall's forested neighborhoods are highly receptive to long-range spotting."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Municipal system draws from Payette Lake — abundant supply. However, distribution "
                "mains are limited in newer developments outside city limits. Rural properties on "
                "individual wells with no fire hydrant access."
            ),
            "power": (
                "Idaho Power transmission through forested corridors. Lines vulnerable to tree fall "
                "and fire damage. Extended outages during major fire events common in surrounding area. "
                "Hospital and smokejumper base have backup generation."
            ),
            "communications": (
                "Cellular coverage good in town, poor in surrounding wilderness. Radio repeaters on "
                "mountain peaks can be damaged by fire. Satellite communication backup for USFS "
                "operations. Emergency alert system via Valley County Sheriff."
            ),
            "medical": (
                "St. Luke's McCall — 15-bed community hospital expanded to 65,000 sq ft in 2023. "
                "Limited capacity for mass casualty. Nearest Level II trauma is Boise (100+ miles, "
                "2+ hours by ground). Helicopter medevac available weather permitting."
            ),
        },
        "demographics_risk_factors": {
            "population": 3700,
            "seasonal_variation": (
                "Year-round pop ~3,700 triples to 10,000-12,000 in summer with tourists, vacation "
                "homeowners, and seasonal workers. Winter ski season adds another population surge. "
                "Many visitors unfamiliar with fire evacuation procedures."
            ),
            "elderly_percentage": "~18% (65+), significant retiree community",
            "mobile_homes": (
                "Limited within city limits. Some mobile/manufactured homes in unincorporated "
                "Valley County areas south of town along Highway 55."
            ),
            "special_needs_facilities": (
                "St. Luke's McCall hospital, one assisted living facility. McCall-Donnelly School "
                "District serves ~900 students. Summer camps and outdoor education programs bring "
                "children into fire-prone backcountry."
            ),
        },
    },

    # =========================================================================
    # 3. KETCHUM / SUN VALLEY, ID — New
    # =========================================================================
    "ketchum_sun_valley_id": {
        "center": [43.6807, -114.3637],
        "terrain_notes": (
            "Ketchum (pop ~3,550) and Sun Valley (pop ~1,780) occupy a narrow section of the "
            "Wood River Valley at 5,850-5,920 ft elevation, hemmed in by the Boulder Mountains to "
            "the north and the Smoky Mountains to the west. The Sawtooth National Forest surrounds "
            "the communities on all sides. The valley floor is only 0.5-1 mile wide in places, with "
            "steep sagebrush and conifer-covered slopes rising 3,000-4,000 ft above town. Baldy "
            "Mountain (Sun Valley ski area) rises directly to the east. Multiple side canyons — "
            "Warm Springs, Cold Springs, Trail Creek, Greenhorn Gulch, Deer Creek — open onto the "
            "valley floor and can channel fire directly into town. The 2013 Beaver Creek Fire "
            "(114,900 acres) entered the valley through Greenhorn Gulch and Deer Creek Canyon, "
            "forcing evacuation of 2,300 homes. In 2024, the Wapiti Fire (126,817 acres) and 38 "
            "other fire starts on the Sawtooth NF smothered the valley in smoke. This is a wealthy "
            "resort community with seasonal population swings of 3-5x, a regional airport, and "
            "a hospital — but only one highway (Hwy 75) threading the narrow valley for egress."
        ),
        "key_features": [
            {"name": "Bald Mountain (Baldy)", "bearing": "E", "type": "terrain",
             "notes": "Sun Valley ski area, summit 9,150 ft. Steep east-facing slopes above town. Mixed conifer and sage."},
            {"name": "Greenhorn Gulch", "bearing": "W", "type": "drainage",
             "notes": "Canyon midway between Hailey and Ketchum. Entry point for 2013 Beaver Creek Fire into the valley. Direct threat corridor."},
            {"name": "Trail Creek Canyon", "bearing": "E", "type": "corridor",
             "notes": "Drainage east of Ketchum leading to Trail Creek summit. Funnels east winds and fire toward town."},
            {"name": "Warm Springs Canyon", "bearing": "W", "type": "drainage",
             "notes": "Major drainage west of Ketchum feeding Warm Springs residential area and ski base. Fire channel from Smoky Mtns."},
            {"name": "Big Wood River", "bearing": "N-S", "type": "water",
             "notes": "Flows south through valley floor. Minimal firebreak value due to narrow riparian zone."},
            {"name": "Sawtooth NRA", "bearing": "N", "type": "wilderness",
             "notes": "National Recreation Area begins just north of town. Unmanaged fuels in wilderness provide unlimited fire source."},
        ],
        "elevation_range_ft": [5750, 9150],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Beaver Creek Fire", "year": 2013, "acres": 114900,
             "details": "Lightning-caused Aug 7. Exploded Aug 16 driven by erratic south/west winds. Entered Wood River Valley through Greenhorn Gulch. 2,300 homes evacuated between Hailey and Ketchum. St. Luke's Wood River evacuated patients. One of Idaho's worst-ever wildfires."},
            {"name": "Castle Rock Fire", "year": 2007, "acres": 48000,
             "details": "Burned on the east side of the Wood River Valley. Threatened Ketchum and Sun Valley. Significant smoke impacts on resort communities."},
            {"name": "Wapiti Fire (smoke impact)", "year": 2024, "acres": 126817,
             "details": "Lightning-caused near Grandjean. While not directly threatening Ketchum, smoke smothered the valley for weeks. 38 total fire starts on Sawtooth NF in 2024 season."},
        ],
        "evacuation_routes": [
            {"route": "Highway 75 South", "direction": "S toward Hailey/Shoshone", "lanes": 2,
             "bottleneck": "Only paved route south. Passes through Hailey — if fire crosses Hwy 75 between towns (as nearly happened in 2013), both communities trapped.",
             "risk": "2013 Beaver Creek Fire crossed terrain adjacent to Hwy 75. Smoke can reduce visibility to zero."},
            {"route": "Highway 75 North", "direction": "N toward Stanley/Sawtooth", "lanes": 2,
             "bottleneck": "Galena Summit (8,701 ft) — steep, narrow, winter-closure road. 60 miles to Stanley with no services.",
             "risk": "Not viable for mass evacuation. Road crosses high-elevation terrain impassable in bad weather."},
            {"route": "Trail Creek Road", "direction": "E toward Mackay", "lanes": 2,
             "bottleneck": "Unpaved/gravel sections over Trail Creek Summit (7,760 ft). Steep, narrow, seasonal.",
             "risk": "Emergency-only alternate. Cannot handle significant traffic volume."},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Valley channeling dominates — afternoon up-valley (southerly) winds 10-20 mph, "
                "nighttime down-valley (northerly) drainage. Strong SW winds during frontal passages "
                "push fire out of Smoky Mountains directly into the valley (as in 2013 Beaver Creek). "
                "The narrow valley acts as a chimney, accelerating wind flow through the constriction "
                "between Baldy and the Smoky Range."
            ),
            "critical_corridors": [
                "Greenhorn Gulch — 2013 Beaver Creek entry point; direct path Smoky Mtns to Hwy 75",
                "Deer Creek Canyon — secondary 2013 entry point, south of Greenhorn",
                "Warm Springs drainage — channels fire from west directly into Ketchum",
                "Trail Creek Canyon — east-side threat corridor funneling wind and fire into town",
                "Big Wood River corridor — continuous valley-floor fuel path connecting communities",
            ],
            "rate_of_spread_potential": (
                "Sagebrush/grass slopes support 2-4 mph spread; conifer forests 1-3 mph surface, "
                "3-5 mph in crown fire. The 2013 Beaver Creek Fire demonstrated explosive runs on "
                "Aug 16 when winds shifted — multiple drainages simultaneously channeled fire into "
                "the valley floor at rates exceeding any defensible response window."
            ),
            "spotting_distance": (
                "1-3 miles in typical conditions. Canyon terrain amplifies convective lift, increasing "
                "spotting potential. Ember showers from Greenhorn Gulch fire run in 2013 landed in "
                "subdivisions on both sides of Highway 75."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Municipal systems in Ketchum and Sun Valley adequate for normal operations. Fire "
                "flow capacity stressed during large-scale structure protection. Many rural-residential "
                "properties in canyons on private wells with no hydrant access."
            ),
            "power": (
                "Idaho Power transmission through forested mountain corridors. Long lead times for "
                "repair in remote terrain. Overhead lines in canyon drainages are vulnerable. "
                "Extended outages during fire events impact water pumping."
            ),
            "communications": (
                "Good cellular and fiber coverage in town centers. Canyon areas and mountain slopes "
                "have significant coverage gaps. Blaine County Sheriff CodeRED alerts. Radio repeaters "
                "on mountain peaks vulnerable to fire damage."
            ),
            "medical": (
                "St. Luke's Wood River Medical Center in Ketchum — 25-bed facility with 24-hour ER. "
                "Was evacuated during 2013 Beaver Creek Fire. Nearest major trauma center is Boise "
                "(150 miles, 2.5 hours). Limited mass casualty capacity."
            ),
        },
        "demographics_risk_factors": {
            "population": 5330,
            "seasonal_variation": (
                "Combined year-round pop ~5,330 (Ketchum + Sun Valley). Swells to 15,000-25,000 "
                "during ski season (Dec-Apr) and summer season (Jun-Sep). Wealthy second-home "
                "community — many properties unoccupied and undefended during fire events. Summer "
                "visitors unfamiliar with evacuation routes."
            ),
            "elderly_percentage": "~20% (65+), significant retiree/second-home demographic",
            "mobile_homes": (
                "Very few in Ketchum/Sun Valley proper due to high property values. Workforce "
                "housing in Hailey and Bellevue includes some manufactured homes."
            ),
            "special_needs_facilities": (
                "St. Luke's Wood River hospital (required evacuation in 2013). Multiple luxury "
                "lodges and hotels housing transient visitors. Sun Valley Resort can host 2,000+ "
                "guests who may need coordinated evacuation. Community School of Sun Valley."
            ),
        },
    },

    # =========================================================================
    # 4. HAILEY, ID — New
    # =========================================================================
    "hailey_id": {
        "center": [43.5196, -114.3153],
        "terrain_notes": (
            "Hailey (pop ~9,200) is the largest community and economic hub of the Wood River "
            "Valley, situated at 5,322 ft elevation on the Big Wood River. The valley floor is "
            "roughly 1 mile wide at Hailey, bounded by Croy Canyon and Della Mountain (7,500 ft) "
            "to the west and the Pioneer Mountains foothills to the east. Friedman Memorial Airport "
            "(SUN) sits on the valley floor just south of town, providing the only commercial air "
            "service to the Sun Valley resort area. The 2013 Beaver Creek Fire burned directly to "
            "Hailey's western edge, with the fire entering the valley through Greenhorn Gulch and "
            "Deer Creek Canyon between Hailey and Ketchum. Complete evacuations of subdivisions on "
            "both sides of Highway 75 were ordered Aug 15-24, 2013. Hailey serves as the workforce "
            "housing center for Ketchum/Sun Valley, with a younger, more diverse population but "
            "also more manufactured housing. The town is the bottleneck for southbound evacuation "
            "from the entire upper Wood River Valley."
        ),
        "key_features": [
            {"name": "Friedman Memorial Airport (SUN)", "bearing": "S", "type": "infrastructure",
             "notes": "Regional airport at 5,318 ft. Commercial flights to SLC, Seattle, seasonal to LAX/DEN/SFO. On valley floor — vulnerable to smoke closure."},
            {"name": "Croy Canyon", "bearing": "W", "type": "drainage",
             "notes": "Major drainage west of town. Residential development extends into canyon mouth. Fire approach vector from Smoky Mountains."},
            {"name": "Deer Creek Canyon", "bearing": "NW", "type": "drainage",
             "notes": "Canyon between Hailey and Ketchum. 2013 Beaver Creek Fire entered valley through this drainage. Direct threat to subdivisions."},
            {"name": "Della Mountain", "bearing": "W", "type": "terrain",
             "notes": "7,500 ft peak immediately west of town. Steep sagebrush slopes above residential areas."},
            {"name": "Big Wood River", "bearing": "N-S", "type": "water",
             "notes": "River bisects valley through town center. Narrow riparian corridor, limited firebreak value."},
            {"name": "Quigley Canyon", "bearing": "E", "type": "drainage",
             "notes": "East-side drainage with dispersed residential development. Cross-country ski area and recreation."},
        ],
        "elevation_range_ft": [5280, 7500],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Beaver Creek Fire", "year": 2013, "acres": 114900,
             "details": "Fire entered Wood River Valley through drainages west of Hailey. 2,300 homes evacuated between Hailey and Ketchum. Subdivisions on both sides of Hwy 75 evacuated Aug 15-24. St. Luke's Wood River evacuated."},
            {"name": "Castle Rock Fire", "year": 2007, "acres": 48000,
             "details": "Burned east side of Wood River Valley. Smoke severely impacted Hailey. Demonstrated vulnerability from multiple approach directions."},
        ],
        "evacuation_routes": [
            {"route": "Highway 75 South", "direction": "S toward Bellevue/Shoshone", "lanes": 2,
             "bottleneck": "Two-lane highway; funnels all upper Wood River Valley traffic (Ketchum, Sun Valley, Hailey) through single corridor.",
             "risk": "Total upper valley population of 15,000-25,000+ in summer must evacuate south through Hailey on one road."},
            {"route": "Highway 75 North", "direction": "N toward Ketchum", "lanes": 2,
             "bottleneck": "Leads deeper into valley. Only useful if fire is south of town.",
             "risk": "Fire between Hailey and Ketchum (as in 2013) can trap both communities."},
            {"route": "Croy Canyon Road", "direction": "W", "lanes": 2,
             "bottleneck": "Unpaved, dead-ends in forest. Not a viable evacuation route.",
             "risk": "Leads toward fire source terrain."},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Same valley-channeled winds as Ketchum — southerly up-valley in afternoon, "
                "northerly drainage at night. Hailey's slightly wider valley floor provides "
                "marginally more defensible space than Ketchum. However, SW frontal winds push "
                "fire from Smoky Mountains directly toward town across open sagebrush."
            ),
            "critical_corridors": [
                "Deer Creek Canyon — 2013 fire entry point between Hailey and Ketchum",
                "Croy Canyon — west-side drainage opening directly into residential areas",
                "Highway 75 corridor — continuous fuel path connecting communities",
                "Della Mountain west slopes — sagebrush/grass fire can run downslope into town",
            ],
            "rate_of_spread_potential": (
                "Sagebrush-dominated hillsides west and east of town support 2-4 mph fire spread. "
                "The 2013 Beaver Creek Fire's Aug 16 explosive run demonstrated that multiple canyons "
                "can simultaneously channel fire into the valley, overwhelming suppression resources."
            ),
            "spotting_distance": (
                "1-2 miles typical in sage/brush. Gusty conditions during 2013 fire carried embers "
                "across Highway 75 and into subdivisions on both sides of the road."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Municipal water system serves town core. Outlying areas and canyon developments on "
                "wells. Fire flow capacity adequate for normal operations but stressed during "
                "simultaneous multi-structure protection."
            ),
            "power": (
                "Idaho Power distribution through valley. Overhead lines along Highway 75 corridor "
                "and into canyons. Smoke can cause flashovers on transmission lines. Extended outages "
                "during fire events."
            ),
            "communications": (
                "Good cellular coverage in town. Blaine County CodeRED emergency notification. Some "
                "canyon areas have reception gaps. Local radio station KECH provides fire updates."
            ),
            "medical": (
                "St. Luke's clinic in Hailey. Main hospital is St. Luke's Wood River in Ketchum "
                "(12 miles north) — which was itself evacuated in 2013. Nearest major trauma "
                "center is Boise (150 miles). Community health center serves Latino workforce population."
            ),
        },
        "demographics_risk_factors": {
            "population": 9200,
            "seasonal_variation": (
                "Year-round pop ~9,200, largest town in Wood River Valley. Summer and ski season "
                "add 3,000-5,000 seasonal residents/visitors. Hailey is workforce housing center — "
                "lower income than Ketchum/Sun Valley."
            ),
            "elderly_percentage": "~12% (65+), younger than Ketchum due to workforce demographics",
            "mobile_homes": (
                "More manufactured/mobile homes than Ketchum, particularly in south Hailey and "
                "Bellevue area. Higher vulnerability structures in workforce housing areas."
            ),
            "special_needs_facilities": (
                "Wood River High School (~800 students). Blaine County School District offices. "
                "Community health center. Hailey is ~30% Hispanic/Latino — language barriers in "
                "emergency communications are a documented concern."
            ),
        },
    },

    # =========================================================================
    # 5. CASCADE, ID — New
    # =========================================================================
    "cascade_id": {
        "center": [44.5163, -116.0418],
        "terrain_notes": (
            "Cascade (pop ~1,000) is the county seat of Valley County, situated at 4,780 ft "
            "elevation on the southeast shore of Lake Cascade (formerly Cascade Reservoir) in "
            "Long Valley. The town sits at the junction of the North Fork of the Payette River "
            "and Lake Cascade, between the West Mountain range to the west and the Boise National "
            "Forest to the east. Highway 55 (Payette River Scenic Byway) is the primary "
            "transportation artery, connecting Cascade to Boise (75 miles south) and McCall "
            "(30 miles north). The USFS Southwest Idaho Wildfire Crisis Landscape Project "
            "identifies Cascade as one of 14 community cores with elevated transboundary wildfire "
            "exposure. The surrounding 1.7-million-acre landscape encompasses 424,000 acres of "
            "the Boise NF and 505,000 acres of the Payette NF. Prescribed fire projects have "
            "treated areas 4-10 miles from town (Willow South 228 acres, Moore Moths 148 acres, "
            "Lost Horse 173 acres), but the scale of treatment is dwarfed by the scale of risk. "
            "Tamarack Resort (12 miles west on West Mountain) brings seasonal population surges "
            "and was forced to close by the 2025 Rock Fire."
        ),
        "key_features": [
            {"name": "Lake Cascade", "bearing": "NW", "type": "water",
             "notes": "Large reservoir (28,000 acres when full) formed by Cascade Dam. Provides significant natural firebreak to north and west of town."},
            {"name": "Cascade Dam", "bearing": "N", "type": "infrastructure",
             "notes": "Bureau of Reclamation dam on North Fork Payette River. Critical infrastructure — damage would impact downstream communities."},
            {"name": "West Mountain", "bearing": "W", "type": "terrain",
             "notes": "7,500+ ft mountain range west of lake. Forested slopes with Tamarack Resort. 2025 Rock Fire burned on these slopes."},
            {"name": "Thunder Mountain", "bearing": "E", "type": "terrain",
             "notes": "Boise NF backcountry east of Cascade. Remote, unmanaged fuels. Source area for fires threatening from east."},
            {"name": "North Fork Payette River", "bearing": "S", "type": "water",
             "notes": "World-class kayaking river. Highway 55 follows this corridor south to Banks — narrow canyon, fire-prone."},
            {"name": "Warm Lake Road", "bearing": "E", "type": "corridor",
             "notes": "Access to Warm Lake area east of Cascade. 2007 Cascade Complex fires burned in this drainage."},
        ],
        "elevation_range_ft": [4780, 7600],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Cascade Complex", "year": 2007, "acres": 300000,
             "details": "Multiple fires in Boise/Payette NFs. Extreme behavior near Warm Lake east of Cascade. 300-ft flame lengths, 5-7 mile spotting confirmed. Threatened Cascade from multiple directions."},
            {"name": "Rock Fire (nearby)", "year": 2025, "acres": 2844,
             "details": "Lightning-caused fire near Tamarack Resort on West Mountain. Forced resort closure and Level 2 evacuations for west Lake Cascade residents. 700 personnel deployed."},
            {"name": "Four Corners Fire", "year": 2024, "acres": 7500,
             "details": "Burned on border of Payette and Boise NFs near Cascade area. Part of the extreme 2024 Idaho fire season."},
        ],
        "evacuation_routes": [
            {"route": "Highway 55 South", "direction": "S toward Banks/Boise", "lanes": 2,
             "bottleneck": "Payette River canyon — narrow, winding, 75 miles to Boise. Single paved route south.",
             "risk": "Canyon terrain channels fire across highway. Rock slides and avalanche zones. Winter closures."},
            {"route": "Highway 55 North", "direction": "N toward McCall/New Meadows", "lanes": 2,
             "bottleneck": "30 miles to McCall. Road passes through forested terrain with fire exposure.",
             "risk": "Fire on West Mountain or east-side Boise NF can threaten this route."},
            {"route": "Warm Lake Road East", "direction": "E toward Landmark/Idaho backcountry", "lanes": 1,
             "bottleneck": "Unpaved, remote, dead-end. Leads into fire source terrain.",
             "risk": "Not a viable evacuation route — leads to Warm Lake area (2007 Cascade Complex origin)."},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Long Valley acts as a wind corridor with afternoon southerly thermal winds and "
                "nighttime northerly drainage. Thunderstorm outflows from Boise NF to the east "
                "can produce sudden wind shifts. West Mountain creates its own mesoscale wind "
                "patterns, with upslope heating driving afternoon fires uphill toward Tamarack."
            ),
            "critical_corridors": [
                "Warm Lake drainage east — source area for 2007 Cascade Complex",
                "West Mountain slopes — fire here threatens west Lake Cascade and Tamarack Resort",
                "North Fork Payette canyon south — fire cuts sole highway to Boise",
                "Poison Creek drainage — approaches town from southeast through Boise NF",
            ],
            "rate_of_spread_potential": (
                "Mixed sagebrush/conifer fuels support 2-4 mph spread in grass/sage, 1-3 mph in "
                "timber. Lake Cascade provides significant natural firebreak on west/north but town "
                "is exposed from east and south. The 2007 Cascade Complex showed that fires in "
                "this terrain can make multi-thousand-acre runs in a single day."
            ),
            "spotting_distance": (
                "1-3 miles in typical conditions; 2007 Cascade Complex confirmed 5-7 miles. Long "
                "Valley terrain amplifies convective columns, increasing long-range spotting risk."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Small municipal system serves town core. Abundant raw water from Lake Cascade "
                "but treatment and distribution capacity limited. Rural-residential areas on wells."
            ),
            "power": (
                "Idaho Power distribution through forested corridors. Limited redundancy. Extended "
                "outages likely during major fire events. No backup generation for most facilities."
            ),
            "communications": (
                "Cellular coverage adequate in town, poor in surrounding forest. Valley County "
                "emergency alerts via CodeRED. Radio communications limited by terrain."
            ),
            "medical": (
                "Cascade Medical Center — small critical access facility, basic ER. Nearest hospital "
                "is St. Luke's McCall (30 miles north). Major trauma requires transport to Boise "
                "(75 miles south). Air ambulance weather-dependent."
            ),
        },
        "demographics_risk_factors": {
            "population": 1005,
            "seasonal_variation": (
                "Year-round pop ~1,000. Summer tourism and Tamarack Resort operations can double "
                "or triple population. Winter ski season at Tamarack adds another surge. Many "
                "vacation/second homes around Lake Cascade are seasonally occupied."
            ),
            "elderly_percentage": "~22% (65+), higher than state average for rural community",
            "mobile_homes": (
                "Significant manufactured/mobile home presence in and around town. Lower property "
                "values attract fixed-income residents. Higher vulnerability structures."
            ),
            "special_needs_facilities": (
                "Cascade Medical Center. Cascade Elementary and Jr-Sr High School. Limited "
                "assisted living. Small, close-knit community with mutual-aid social networks "
                "but limited institutional capacity for mass care."
            ),
        },
    },

    # =========================================================================
    # 6. GARDEN VALLEY, ID — New
    # =========================================================================
    "garden_valley_id": {
        "center": [44.0883, -115.9630],
        "terrain_notes": (
            "Garden Valley (pop ~380) is an unincorporated community in Boise County, situated "
            "at approximately 3,200 ft elevation along the Middle Fork of the Boise River in a "
            "narrow valley surrounded by the Boise National Forest. The community is accessed "
            "primarily via State Highway 17 (Banks-Lowman Road) from Banks on Highway 55 — a "
            "narrow, winding two-lane road through steep, forested canyon terrain. Garden Valley "
            "represents one of the most extreme WUI situations in Idaho: dispersed rural "
            "residential development deep in national forest with limited road access. The 2024 "
            "Middle Fork Complex Fire burned 61,495 acres just 9 miles east of town, triggering "
            "Level 2 evacuations along Middlefork Road. During the 2024 fire season, Garden "
            "Valley had the worst air quality in Idaho. The community relies on a volunteer fire "
            "department and has no hospital, no commercial services of scale, and limited "
            "communications infrastructure. Fires approaching from the east (Middle Fork drainage), "
            "south (along Hwy 21 from Lowman), or north (Deadwood drainage) can cut access routes "
            "and trap residents."
        ),
        "key_features": [
            {"name": "Middle Fork Boise River", "bearing": "E", "type": "drainage",
             "notes": "Major river corridor east of town. 2024 Middle Fork Complex burned along this drainage. Roads follow river — fire cuts access."},
            {"name": "Banks (Highway 55 junction)", "bearing": "W", "type": "infrastructure",
             "notes": "Junction town 15 miles west on Hwy 17. Only connection to Hwy 55 and route to Boise. Narrow canyon between Garden Valley and Banks."},
            {"name": "Deadwood Ridge", "bearing": "N", "type": "terrain",
             "notes": "Forested ridge north of community. Fire here would push south into residential areas with drainage winds."},
            {"name": "Crouch", "bearing": "SW", "type": "community",
             "notes": "Small community 5 miles west on Middlefork Road. Shares Garden Valley's vulnerability and access constraints."},
            {"name": "Terrace Lakes Resort", "bearing": "NE", "type": "development",
             "notes": "Golf resort and residential development in forest setting. Concentrated structures in high-fire-risk terrain."},
            {"name": "Lowman Road (Hwy 17/21)", "bearing": "E", "type": "corridor",
             "notes": "Road east toward Lowman. Follows river through fire-prone canyon. Access to Middle Fork backcountry."},
        ],
        "elevation_range_ft": [3100, 7200],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Middle Fork Complex", "year": 2024, "acres": 61495,
             "details": "Three fires merged 9 miles east of Garden Valley. Level 2 evacuations on Middlefork Road. Garden Valley had worst air quality in Idaho. 95% contained by Oct 31."},
            {"name": "Rabbit Creek Fire", "year": 2022, "acres": 8500,
             "details": "Burned in Boise NF near Garden Valley area. Part of ongoing pattern of fires threatening community."},
            {"name": "Payette Complex", "year": 2018, "acres": 38000,
             "details": "Multiple fires in Boise NF affecting Garden Valley zone. Smoke and evacuation readiness."},
        ],
        "evacuation_routes": [
            {"route": "Highway 17 West to Banks", "direction": "W to Hwy 55", "lanes": 2,
             "bottleneck": "15-mile narrow, winding canyon road. Single paved route out. No alternate routes.",
             "risk": "Fire in canyon between Garden Valley and Banks traps the entire community. Road subject to slides and closures."},
            {"route": "Middlefork Road East", "direction": "E toward Lowman/Hwy 21", "lanes": 2,
             "bottleneck": "Rough road through fire-prone canyon along Middle Fork. Subject to fire closure (2024).",
             "risk": "2024 Middle Fork Complex closed this route. Leads through, not away from, fire terrain."},
            {"route": "Deadwood Road North", "direction": "N toward Deadwood Reservoir", "lanes": 1,
             "bottleneck": "Unpaved, remote, seasonal. Dead-ends at reservoir in wilderness.",
             "risk": "Not a viable evacuation route. Leads deeper into unroaded forest."},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Canyon/valley winds dominate. Afternoon up-canyon (easterly) thermal winds draw "
                "fire from surrounding forest toward the community. Nighttime drainage winds reverse "
                "but can push fire down from higher elevations. Thunderstorm outflows from afternoon "
                "convection produce erratic gusts in complex terrain."
            ),
            "critical_corridors": [
                "Middle Fork Boise River drainage — fire runs along river corridor, cuts road access",
                "Highway 17 canyon to Banks — fire here isolates entire community",
                "Deadwood drainage — north-side approach with downslope wind-driven fire",
                "South Fork tributaries — fire approaches from Lowman/Pioneer Fire area",
            ],
            "rate_of_spread_potential": (
                "Dense mixed conifer forest with significant understory fuels. Surface fire 1-2 mph, "
                "crown fire 2-4 mph in continuous canopy. Canyon terrain amplifies fire behavior with "
                "chimney effect in narrow drainages. 2024 Middle Fork Complex demonstrated multi-fire "
                "merger and rapid growth in this terrain."
            ),
            "spotting_distance": (
                "1-3 miles typical in forested terrain. Canyon updrafts can loft embers significant "
                "distances. Receptive fuels (dry forest duff, needle cast on roofs) everywhere."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "No municipal water system. All properties on individual wells or small community "
                "systems. No fire hydrants. Firefighting water must be drafted from rivers/ponds "
                "or trucked in. Severe constraint on structure protection."
            ),
            "power": (
                "Idaho Power distribution through forested terrain on overhead lines. Extended "
                "outages during fire events. No backup generation for community. Power loss means "
                "well pumps fail — no water for firefighting or domestic use."
            ),
            "communications": (
                "Limited cellular coverage — significant dead zones in canyon terrain. Landline "
                "service spotty. Boise County CodeRED emergency alerts. Community relies heavily "
                "on word-of-mouth and volunteer fire department notification."
            ),
            "medical": (
                "No hospital or clinic. Garden Valley has a volunteer fire/EMS department. Nearest "
                "hospital is in Boise (50+ miles, 1.5 hours via narrow Hwy 17/55). Air ambulance "
                "is weather-dependent and requires clear landing zone."
            ),
        },
        "demographics_risk_factors": {
            "population": 380,
            "seasonal_variation": (
                "Year-round pop ~380. Summer recreation season doubles or triples occupancy with "
                "vacation homes, camping, and resort visitors. Many structures are seasonal cabins "
                "with deferred maintenance and poor defensible space."
            ),
            "elderly_percentage": "~25% (65+), significant retiree population in rural setting",
            "mobile_homes": (
                "Moderate presence of manufactured homes and older cabins. Many structures built "
                "before modern fire codes, with wood shake roofs and combustible siding."
            ),
            "special_needs_facilities": (
                "Garden Valley School (K-8, ~100 students). No assisted living or medical "
                "facilities. Isolated elderly residents particularly vulnerable. Community "
                "self-reliance is both strength and limitation."
            ),
        },
    },

    # =========================================================================
    # 7. STANLEY, ID — New
    # =========================================================================
    "stanley_id": {
        "center": [44.2075, -114.9381],
        "terrain_notes": (
            "Stanley (pop ~120) sits at 6,250 ft elevation at the confluence of Valley Creek "
            "and the Salmon River in the Sawtooth Valley — a broad, high-elevation basin ringed "
            "by the Sawtooth Range (10,000+ ft) to the west, the White Cloud Peaks to the east, "
            "and the Salmon River Mountains to the north. Stanley is often cited as the coldest "
            "town in the lower 48 states (record -54F, avg annual temp 21.2F). Despite its "
            "extreme remoteness — 130 miles from Boise, 60 miles from the nearest town of any "
            "size — Stanley is a hub for recreation in the Sawtooth National Recreation Area "
            "and Frank Church-River of No Return Wilderness. The 2024 fire season was catastrophic: "
            "the Wapiti Fire (126,817 acres) burned from Grandjean toward Stanley, closing 50 miles "
            "of Highway 21 and forcing evacuation preparation. Crews built indirect fireline from "
            "the Stanley Ranger Station to Redfish Lake. The Bench Lake Fire (2,600 acres) closed "
            "Redfish Lake Lodge. Highway 75 (south to Sun Valley) and Highway 21 (west to Boise) "
            "are the only routes, and both traverse remote fire-prone terrain."
        ),
        "key_features": [
            {"name": "Sawtooth Range", "bearing": "W", "type": "terrain",
             "notes": "Jagged granite peaks to 10,751 ft (Thompson Peak). Wilderness boundary within 5 miles. Unmanaged fuels."},
            {"name": "Redfish Lake", "bearing": "SW", "type": "water",
             "notes": "Iconic alpine lake 5 miles south. Lodge and campgrounds host thousands of visitors. 2024 Bench Lake Fire forced closure."},
            {"name": "Salmon River", "bearing": "N-E", "type": "water",
             "notes": "Headwaters of the River of No Return. Flows north through Stanley then east. River corridor is primary fire approach vector from east."},
            {"name": "Galena Summit", "bearing": "S", "type": "terrain",
             "notes": "8,701 ft pass on Hwy 75 south of Stanley. High-elevation crossing to Wood River Valley. Winter closures, avalanche zones."},
            {"name": "Highway 21 / Grandjean", "bearing": "W", "type": "corridor",
             "notes": "Route to Boise via Banner Summit (7,056 ft). 2024 Wapiti Fire closed 50 miles of this highway. Passes through Boise NF fire terrain."},
            {"name": "White Cloud Peaks", "bearing": "E", "type": "terrain",
             "notes": "11,000+ ft peaks east of Stanley. Castle Peak (11,815 ft). Wilderness area with unmanaged fuels in lower elevations."},
        ],
        "elevation_range_ft": [6100, 10751],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Wapiti Fire", "year": 2024, "acres": 126817,
             "details": "Lightning-caused July 24 near Grandjean. Burned across Boise NF, Sawtooth NF, Sawtooth Wilderness, and Salmon-Challis NF. Closed Hwy 21 for 50 miles. Crews built fireline from Stanley Ranger Station to Redfish Lake. 80% contained with 186 personnel."},
            {"name": "Bench Lake Fire", "year": 2024, "acres": 2600,
             "details": "Ignited 1 mile west of Redfish Lake on July 11. Doubled in size daily for first week. Closed Redfish Lake Lodge and campgrounds — major economic/recreation impact."},
            {"name": "Valley Road Fire", "year": 2005, "acres": 12000,
             "details": "Burned in Sawtooth Valley near Stanley. Threatened homes and infrastructure in the community."},
        ],
        "evacuation_routes": [
            {"route": "Highway 75 South", "direction": "S toward Sun Valley (60 mi)", "lanes": 2,
             "bottleneck": "Galena Summit (8,701 ft) — steep, narrow, winter-closure road. 60 miles to Ketchum with no services.",
             "risk": "High-elevation pass impassable in winter. Fire or avalanche can close. No alternate route."},
            {"route": "Highway 21 West", "direction": "W toward Boise (130 mi)", "lanes": 2,
             "bottleneck": "Banner Summit (7,056 ft), then drops through Lowman/Idaho City. 50 miles closed by 2024 Wapiti Fire.",
             "risk": "Passes through extreme fire terrain in Boise NF. Routinely closed by wildfire, slides, winter weather."},
            {"route": "Highway 75 North to Challis", "direction": "N/E toward Challis (60 mi)", "lanes": 2,
             "bottleneck": "Follows Salmon River through remote canyon. No services for 60 miles.",
             "risk": "Fire in Salmon River corridor can close this route. Extremely remote — no cell service for much of distance."},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Sawtooth Valley is a high-elevation basin with complex wind patterns. Afternoon "
                "thermal winds draw up-valley (southerly) through the valley floor. Strong nocturnal "
                "drainage from surrounding peaks (10,000+ ft) creates cold-pool inversions that "
                "suppress overnight fire but trap smoke. Frontal passages and thunderstorm outflows "
                "produce the most dangerous conditions — sudden wind shifts with 40-60 mph gusts "
                "that break inversions and unleash explosive fire behavior."
            ),
            "critical_corridors": [
                "Salmon River corridor east — primary fire approach vector; 2024 fires burned along this axis",
                "Highway 21 / Grandjean drainage west — 2024 Wapiti Fire approach",
                "Redfish Lake / Alturas Lake drainages south — fire approaches from Sawtooth Wilderness",
                "Valley Creek drainage — connects fire from NE directly to Stanley",
            ],
            "rate_of_spread_potential": (
                "Mixed lodgepole pine and Douglas-fir forests with sagebrush/grass openings on "
                "valley floor. Surface fire 1-2 mph in timber, 2-4 mph in sage openings. Crown "
                "fire potential high in dense lodgepole stands with ladder fuels. Beetle-kill "
                "standing dead timber increases torching risk. High elevation moderates fire season "
                "length but concentrated July-September window produces intense events."
            ),
            "spotting_distance": (
                "1-3 miles in forested terrain. Mountain terrain amplifies convective columns — "
                "the 2024 Wapiti Fire produced massive pyrocumulus visible from Boise. Long-range "
                "spotting across the valley floor is a primary concern for Stanley."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Small community water system. Limited fire flow capacity. No hydrants in "
                "surrounding areas. Sawtooth NRA ranger station has some water infrastructure "
                "but not designed for community firefighting. River drafting possible but requires "
                "equipment positioning."
            ),
            "power": (
                "Idaho Power single-transmission feed through remote, forested terrain. No "
                "redundancy. Extended outages common during fire events (Hwy 21 corridor poles "
                "burn). Limited backup generation — Stanley is essentially off-grid during outages. "
                "Winter power loss in -40F conditions is life-threatening."
            ),
            "communications": (
                "Very limited cellular coverage. One cell tower serves Stanley area. Satellite "
                "internet for some residents. USFS radio network provides best communications. "
                "Emergency notification relies on Custer County Sheriff and word-of-mouth in this "
                "tiny community. Landline service intermittent."
            ),
            "medical": (
                "No hospital, no clinic. Sawtooth Wilderness medical services are volunteer-based. "
                "Nearest hospital is Challis (60 miles) with basic ER, or Boise (130 miles) for "
                "trauma. Air ambulance extremely weather-dependent at 6,250 ft in mountain valley. "
                "Medical evacuation during active fire may be impossible."
            ),
        },
        "demographics_risk_factors": {
            "population": 120,
            "seasonal_variation": (
                "Year-round pop ~120. Summer tourism swells effective population to 2,000-5,000 "
                "with campgrounds, lodges, outfitters, and Redfish Lake visitors. Winter population "
                "drops below 100. Visitors are overwhelmingly unfamiliar with evacuation procedures "
                "and terrain hazards. Many recreating in backcountry miles from any road."
            ),
            "elderly_percentage": "~15% (65+), hardy year-round residents",
            "mobile_homes": (
                "Some older mobile/manufactured homes and seasonal cabins. Many structures are "
                "historic wood-frame construction. Limited fire-code compliance in unincorporated area."
            ),
            "special_needs_facilities": (
                "Stanley Community School (K-8, ~20 students). No assisted living. No medical "
                "facilities. Seasonal outfitter camps and lodges house visitors who may have "
                "mobility limitations. Backcountry recreators (hikers, rafters) can be cut off "
                "from evacuation routes by fire."
            ),
        },
    },

    # =========================================================================
    # 8. SALMON, ID — New
    # =========================================================================
    "salmon_id": {
        "center": [45.1758, -113.8953],
        "terrain_notes": (
            "Salmon (pop ~3,300) is the county seat of Lemhi County, situated at ~3,950 ft "
            "elevation at the confluence of the Salmon River and the Lemhi River. The town is "
            "the economic and services hub for a vast, sparsely populated region — the nearest "
            "city of any size is Idaho Falls (160 miles east) or Missoula, MT (150 miles north). "
            "The Salmon River corridor runs east-west through town, flanked by steep, sagebrush "
            "and conifer-covered mountains rising 4,000+ ft above the valley floor. The 2022 "
            "Moose Fire (130,111 acres) — Idaho's largest fire that year — burned from a campfire "
            "left unattended in Lemhi County, with wind gusts to 55 mph driving extreme fire "
            "behavior and forcing evacuations of multiple zones around Salmon. Two helicopter "
            "pilots died fighting the Moose Fire. In 2024, the Elkhorn Fire made a 20,000-acre "
            "run of extreme behavior up the Salmon River, and the Red Rock Fire (78,795 acres) "
            "burned 15 miles west of town with 60+ mph winds that trapped 45 firefighters when "
            "the blaze destroyed a bridge. Highway 93 is the sole major route, running north-south "
            "through the valley."
        ),
        "key_features": [
            {"name": "Salmon River", "bearing": "E-W", "type": "water",
             "notes": "The 'River of No Return' flows through town. Corridor channels fire and wind. Steep canyon walls above town."},
            {"name": "Lemhi Range", "bearing": "E", "type": "terrain",
             "notes": "Mountain range east of Lemhi Valley. 10,000+ ft peaks. Sagebrush/grass lower slopes, conifer higher. Fire approach vector from east."},
            {"name": "Bitterroot Range", "bearing": "W", "type": "terrain",
             "notes": "Continental Divide west of Salmon. Frank Church Wilderness beyond. Unmanaged fuels in vast wilderness."},
            {"name": "North Fork (Salmon River)", "bearing": "N", "type": "community",
             "notes": "Small community 20 miles north at river junction. 2022 Moose Fire forced evacuations in this area."},
            {"name": "Panther Creek", "bearing": "W", "type": "drainage",
             "notes": "Major drainage west of Salmon. 2024 Red Rock Fire started near Panther Creek. Canyon terrain funnels fire toward town."},
            {"name": "Salmon-Challis NF", "bearing": "all directions", "type": "forest",
             "notes": "4.3 million acre national forest/wilderness complex surrounds town. Largest NF in lower 48. Vast unmanaged fuel loads."},
        ],
        "elevation_range_ft": [3900, 10985],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Moose Fire", "year": 2022, "acres": 130111,
             "details": "Human-caused (unattended campfire). Idaho's largest fire of 2022. 55 mph wind gusts drove extreme behavior. Multiple evacuation zones activated around Salmon. Two helicopter pilots killed July 20. Burned 200+ square miles."},
            {"name": "Red Rock Fire", "year": 2024, "acres": 78795,
             "details": "Lightning-caused Sept 2 near Panther Creek, 15 miles west. 60+ mph wind gusts. Destroyed bridge, trapping 45 firefighters Oct 5. 19% contained by October."},
            {"name": "Elkhorn Fire", "year": 2024, "acres": 26048,
             "details": "Burned in Salmon River corridor. Made 20,000-acre run of extreme fire behavior. One structure lost at Yellow Pine Ranch, seven buildings at Allison Ranch."},
            {"name": "Thunder Fire", "year": 2024, "acres": 2474,
             "details": "Lightning-caused July 24, 12 miles SW of Salmon. Burned in timber, sagebrush, grass. 100% contained."},
        ],
        "evacuation_routes": [
            {"route": "US-93 North", "direction": "N toward Missoula, MT (150 mi)", "lanes": 2,
             "bottleneck": "Two-lane highway through North Fork canyon. 150 miles to Missoula. Passes through 2022 Moose Fire area.",
             "risk": "Fire in Salmon River or North Fork canyon closes sole northern route. Remote canyon with no alternate roads."},
            {"route": "US-93 South", "direction": "S toward Challis (60 mi)", "lanes": 2,
             "bottleneck": "Follows Salmon River through canyon. 60 miles to Challis, then 160 miles to Idaho Falls.",
             "risk": "Fire in Salmon River corridor cuts route. 2024 Elkhorn Fire burned along this corridor."},
            {"route": "Highway 28 East", "direction": "E toward Tendoy/Leadore", "lanes": 2,
             "bottleneck": "Follows Lemhi River valley east. Remote, no services for 60 miles.",
             "risk": "Connects to US-93 at Lost Trail Pass or Highway 28 south. Adds hours to any evacuation."},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Salmon River canyon creates powerful wind channeling. Up-canyon (westerly) thermal "
                "winds in afternoon, down-canyon (easterly) drainage at night. Frontal passages "
                "produce extreme wind events — the 2022 Moose Fire saw 55 mph gusts, and the 2024 "
                "Red Rock Fire experienced 60+ mph winds that destroyed infrastructure. The canyon "
                "terrain amplifies wind speeds through constriction effects."
            ),
            "critical_corridors": [
                "Salmon River corridor — fire channeled by canyon directly toward/through town",
                "Panther Creek drainage — 2024 Red Rock Fire approach from west",
                "North Fork Salmon River — 2022 Moose Fire approach from north",
                "Lemhi Valley — sagebrush-dominated, rapid fire spread east of town",
            ],
            "rate_of_spread_potential": (
                "Sagebrush/grass fuels on valley floor and lower slopes support 3-6 mph spread. "
                "Canyon terrain accelerates fire behavior dramatically — the 2024 Elkhorn Fire's "
                "20,000-acre run demonstrates the potential for extreme rates in the Salmon River "
                "corridor. Conifer forests at higher elevations support crown fire at 2-4 mph."
            ),
            "spotting_distance": (
                "1-3 miles typical. Canyon convective dynamics can produce longer spotting. The "
                "2022 Moose Fire's 55 mph winds and 2024 Red Rock Fire's 60+ mph winds demonstrate "
                "the potential for extreme ember transport in this terrain."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Municipal system serves town core. Rural areas on wells. Water supply from Salmon "
                "River adequate but treatment/distribution capacity limited for large-scale "
                "firefighting. Upstream fire debris in river can impact water quality."
            ),
            "power": (
                "Idaho Power long-distance transmission through remote terrain. Single feed, no "
                "redundancy. Power poles in fire-prone corridors. Extended outages during major "
                "fire events — infrastructure destroyed (2024 Red Rock Fire destroyed bridge)."
            ),
            "communications": (
                "Cellular coverage in town, very poor in surrounding canyons and wilderness. "
                "Lemhi County emergency alerts. Radio repeaters on peaks vulnerable to fire. "
                "Satellite phones used by USFS but not available to public. Large communication "
                "dead zones on highways."
            ),
            "medical": (
                "Steele Memorial Medical Center — 25-bed critical access hospital with ER. Local "
                "VA clinic. This is the ONLY hospital for a region larger than some states. "
                "Nearest additional hospital is Challis (60 mi) or Idaho Falls (160 mi). "
                "Air ambulance weather-dependent in canyon terrain."
            ),
        },
        "demographics_risk_factors": {
            "population": 3300,
            "seasonal_variation": (
                "Year-round pop ~3,300. Summer increases 50-100% with rafters, outfitters, hunters, "
                "and tourists accessing Frank Church Wilderness and Salmon River. Fall hunting "
                "season brings additional visitors to remote backcountry. Many visitors are miles "
                "from roads in wilderness when fires start."
            ),
            "elderly_percentage": "~22% (65+), aging rural community",
            "mobile_homes": (
                "Significant manufactured/mobile home presence. Lower property values in Lemhi "
                "County. Many structures lack fire-resistant construction. Some older mobile homes "
                "in flood/fire interface zones along rivers."
            ),
            "special_needs_facilities": (
                "Steele Memorial Medical Center. Salmon River School District. County senior "
                "center. Limited assisted living. Isolated elderly and disabled residents in "
                "remote river locations particularly vulnerable."
            ),
        },
    },

    # =========================================================================
    # 9. LOWMAN, ID — New
    # =========================================================================
    "lowman_id": {
        "center": [44.0833, -115.6167],
        "terrain_notes": (
            "Lowman (pop ~44) is an unincorporated community in Boise County at 3,960 ft "
            "elevation, nestled along the South Fork of the Payette River in the heart of "
            "the Boise National Forest. Highway 21 (Ponderosa Pine Scenic Byway) is the sole "
            "paved road, connecting Lowman to Boise (75 miles southwest) and Stanley (65 miles "
            "northeast). Lowman has been devastated by wildfire repeatedly: the 1989 Lowman Fire "
            "burned 45,000 acres (72 sq miles) and destroyed 26 structures in the community; "
            "the 2016 Pioneer Fire (189,032 acres) crossed Highway 21 at Lowman with 40 mph "
            "gusts, triggering Level 2 evacuations; and the 2024 Bulltrout Fire burned 35 miles "
            "northeast. A historical marker in Lowman states: 'During the last 100 years, the "
            "natural fire cycle has been altered by humans putting out fires, and as a result, "
            "unnaturally abundant fuels built up in the Lowman area.' The community sits in a "
            "narrow river canyon with forested slopes rising steeply on all sides — there is "
            "essentially no defensible space at the landscape level."
        ),
        "key_features": [
            {"name": "South Fork Payette River", "bearing": "E-W", "type": "water",
             "notes": "River flows through Lowman. Narrow canyon with Highway 21 on the bank. Fire terrain on both sides of river."},
            {"name": "Highway 21 (Ponderosa Pine Scenic Byway)", "bearing": "SW-NE", "type": "corridor",
             "notes": "Only paved road. Connects Boise to Stanley through Boise NF. Routinely closed by fire — 50+ miles closed in 2024."},
            {"name": "Pioneer Fire burn scar (2016)", "bearing": "S", "type": "terrain",
             "notes": "189,000-acre burn scar south/east of Lowman. Reburned areas have dense brush regrowth. Dead standing timber remains."},
            {"name": "Kirkham Hot Springs", "bearing": "W", "type": "recreation",
             "notes": "Popular hot springs 4 miles west. Concentrates recreators in fire-prone canyon terrain."},
            {"name": "Grandjean (Hwy 21)", "bearing": "NE", "type": "trailhead",
             "notes": "Backcountry access point 25 miles NE. Origin area of 2024 Wapiti Fire. Highway 21 closure cut Stanley access."},
            {"name": "Lowman Ranger District", "bearing": "local", "type": "infrastructure",
             "notes": "USFS ranger station. Provides some fire suppression resources. One of few institutional structures in community."},
        ],
        "elevation_range_ft": [3960, 8200],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Lowman Fire", "year": 1989, "acres": 45000,
             "details": "Burned 72 sq miles from July 26 to Aug 30. Destroyed 26 structures in community. No injuries or fatalities. Altered by unnaturally abundant fuel buildup from fire suppression."},
            {"name": "Pioneer Fire", "year": 2016, "acres": 189032,
             "details": "Massive fire in Boise NF. Crossed Highway 21 at Lowman with 20 mph sustained winds, 28-40 mph gusts. Level 2 evacuations. 900 acres aerial mulching, 300 miles road drainage reconstruction in BAER response."},
            {"name": "Bulltrout Fire", "year": 2024, "acres": 5000,
             "details": "Lightning-caused July 24, 35 miles NE of Lowman. Part of the extreme 2024 central Idaho fire season."},
            {"name": "Wapiti Fire (Hwy 21 closure)", "year": 2024, "acres": 126817,
             "details": "While centered near Grandjean, the Wapiti Fire closed Highway 21 from Lowman to Stanley — cutting Lowman's only route northeast."},
        ],
        "evacuation_routes": [
            {"route": "Highway 21 Southwest", "direction": "SW toward Idaho City/Boise (75 mi)", "lanes": 2,
             "bottleneck": "Narrow, winding mountain highway through Boise NF. 75 miles to Boise. Passes through 2016 Pioneer Fire burn scar.",
             "risk": "Fire or slides close this road frequently. Only paved route to civilization. No services for 35+ miles to Idaho City."},
            {"route": "Highway 21 Northeast", "direction": "NE toward Stanley (65 mi)", "lanes": 2,
             "bottleneck": "Crosses Banner Summit (7,056 ft). 2024 Wapiti Fire closed 50 miles of this route.",
             "risk": "Routinely closed by fire, avalanche, winter weather. Leads toward more remote terrain, not toward services."},
            {"route": "South Fork Payette Road", "direction": "E toward Garden Valley (30 mi)", "lanes": 1,
             "bottleneck": "Rough, unpaved road along river. Subject to fire closure and flooding.",
             "risk": "Not a reliable evacuation route. Connects to Garden Valley which has its own access constraints."},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Canyon wind regime dominates. Strong afternoon up-canyon thermal winds from the "
                "southwest, nighttime drainage from northeast. The 2016 Pioneer Fire demonstrated "
                "the danger: sustained 20 mph south winds with 28-40 mph gusts pushed fire across "
                "Highway 21 and directly through the community. Canyon constriction at Lowman "
                "accelerates wind flow."
            ),
            "critical_corridors": [
                "South Fork Payette River canyon — fire channeled along Highway 21 corridor directly through community",
                "Highway 21 NE toward Grandjean — 2024 Wapiti Fire approach",
                "Side drainages from south (Pioneer Fire area) — downslope fire approach",
                "Deadwood River drainage from north — fire approach from NE direction",
            ],
            "rate_of_spread_potential": (
                "Dense conifer forest in narrow canyon. Surface fire 1-2 mph. Crown fire in "
                "continuous canopy 2-4 mph. Canyon chimney effect can produce extreme rates during "
                "wind events — the 2016 Pioneer Fire's crossing of Hwy 21 at 40 mph gusts "
                "demonstrates potential for overwhelming any defensive measures. Post-fire brush "
                "regrowth in 1989 and 2016 burn scars adds flashy fuels."
            ),
            "spotting_distance": (
                "1-2 miles in typical conditions. Canyon updrafts amplify spotting. The narrow "
                "canyon at Lowman means any significant spotting crosses the entire community. "
                "Receptive fuels on roofs, in yards, and forest duff everywhere."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "No municipal water system. Individual wells. No fire hydrants. South Fork Payette "
                "River provides drafting source but requires equipment. 26 structures lost in 1989 "
                "partly due to inability to mount effective water-based defense."
            ),
            "power": (
                "Idaho Power single feed through forested canyon. Power poles in fire corridor. "
                "Extended outages during any nearby fire. No backup generation. Power loss = no "
                "well pumps = no water."
            ),
            "communications": (
                "Minimal cellular coverage. Deep canyon blocks signals. USFS ranger station has "
                "radio. Satellite communication limited. Landline service unreliable. Community "
                "notification is essentially door-to-door in a community of 44 people."
            ),
            "medical": (
                "No medical facilities whatsoever. Nearest clinic is Idaho City (35 miles). "
                "Nearest hospital is Boise (75 miles, 1.5-2 hours on winding mountain road). "
                "Medical emergency during active fire = potentially fatal delay."
            ),
        },
        "demographics_risk_factors": {
            "population": 44,
            "seasonal_variation": (
                "Year-round pop ~44 (2020 Census). Summer recreation at hot springs, river "
                "activities, and campgrounds increases effective population 5-10x. Kirkham Hot "
                "Springs alone can have 200+ visitors on summer weekends. Many campers dispersed "
                "in forest along Highway 21 corridor."
            ),
            "elderly_percentage": "~30% (est.), small population skews older",
            "mobile_homes": (
                "Mix of manufactured homes, older cabins, and a few newer structures. Most "
                "buildings pre-date fire codes. Wood-frame construction universal. Limited "
                "defensible space due to canyon terrain and forest encroachment."
            ),
            "special_needs_facilities": (
                "None. No school (students bus to Idaho City or Garden Valley). No assisted "
                "living. Community is essentially self-reliant. Volunteer fire department provides "
                "first response. Mutual aid response times measured in hours, not minutes."
            ),
        },
    },

    # =========================================================================
    # 10. FEATHERVILLE / PINE, ID — New
    # =========================================================================
    "featherville_pine_id": {
        "center": [43.5050, -115.3050],
        "terrain_notes": (
            "Featherville (pop ~150) and Pine (pop ~60) are small, remote communities along the "
            "South Fork of the Boise River in Elmore County, 105 miles northeast of Boise. "
            "Featherville sits at approximately 4,964 ft elevation. The two towns, separated by "
            "10 miles, occupy a narrow river valley surrounded by the Boise National Forest with "
            "steep, forested mountain slopes on all sides. The area has ~450 homes, with about "
            "half occupied year-round and half serving as summer/weekend retreats. This community "
            "has been evacuated repeatedly: the 2012 Trinity Ridge Fire (138,965 acres, "
            "human-caused from ATV fire) burned just 2 miles from Featherville; the 2013 Elk "
            "Complex Fire (130,000+ acres, lightning-caused) destroyed 38 residences and over "
            "a dozen homes directly in Pine and Featherville. It was the second consecutive year "
            "of mandatory evacuation. Anderson Ranch Reservoir to the south provides recreation "
            "access but the road network is limited to a single paved route (Pine-Featherville "
            "Road connecting to Highway 20 near Fairfield or Forest Road to Idaho City)."
        ),
        "key_features": [
            {"name": "South Fork Boise River", "bearing": "E-W", "type": "water",
             "notes": "River flows through both communities. USGS gauge station at Featherville. Canyon terrain with fire-prone slopes above."},
            {"name": "Anderson Ranch Reservoir", "bearing": "S", "type": "water",
             "notes": "Large reservoir south of Pine. Recreation destination. Access road is one of few routes in/out."},
            {"name": "Trinity Mountain", "bearing": "NW", "type": "terrain",
             "notes": "Area where 2012 Trinity Ridge Fire originated (ATV fire). 7,000+ ft. Dense conifer forest."},
            {"name": "Elk Mountain Complex", "bearing": "N-NE", "type": "terrain",
             "notes": "Area of 2013 Elk Complex Fire. Lightning-caused. Forest terrain with steep approaches to community."},
            {"name": "Featherville Main Street", "bearing": "local", "type": "community",
             "notes": "Historic mining town — single main street, saloon, motel, cafe. Clustered structures in narrow canyon."},
            {"name": "Boise National Forest", "bearing": "all directions", "type": "forest",
             "notes": "Surrounds communities completely. Dense mixed conifer with fire-adapted ecosystems and heavy fuel loads."},
        ],
        "elevation_range_ft": [4800, 7500],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Trinity Ridge Fire", "year": 2012, "acres": 138965,
             "details": "Human-caused (ATV caught fire) Aug 3. Burned 2 miles NW of Featherville. Forced evacuation of hundreds. Blackened 228 square miles. 10% contained at peak."},
            {"name": "Elk Complex Fire", "year": 2013, "acres": 130000,
             "details": "Lightning-caused Aug 8. Multiple fires merged. Destroyed 38 residences, a dozen+ homes in Pine and Featherville. Second consecutive year of evacuation. Second-largest active fire in US at peak. 90,249 acres of grass, brush, conifer burned."},
            {"name": "Little Queens Fire", "year": 2018, "acres": 5500,
             "details": "Burned in Boise NF near Featherville area. Continued pattern of annual fire threats."},
        ],
        "evacuation_routes": [
            {"route": "Pine-Featherville Road South", "direction": "S toward Anderson Ranch/Highway 20", "lanes": 2,
             "bottleneck": "Narrow, winding road through forest/canyon. 40+ miles to Highway 20 near Fairfield.",
             "risk": "Fire can cut this road in multiple locations. Primary evacuation route for all 450 homes."},
            {"route": "Forest Road to Idaho City", "direction": "NW toward Idaho City/Boise", "lanes": 1,
             "bottleneck": "Rough forest road, unpaved sections, steep grades. Not suitable for passenger vehicles.",
             "risk": "Passes through Trinity Ridge Fire burn area. Emergency use only."},
            {"route": "South Fork Road East", "direction": "E toward Ketchum (remote)", "lanes": 1,
             "bottleneck": "Extremely rough, seasonal, unpaved. Dead-ends or connects to primitive roads.",
             "risk": "Not a viable evacuation route for general population."},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Canyon/valley thermal winds similar to other South Fork communities. Afternoon "
                "up-canyon (westerly) winds draw fire from forest toward communities. Evening "
                "drainage winds reverse. Thunderstorm outflows produce the most dangerous conditions "
                "— the 2013 Elk Complex fires were lightning-caused and driven by erratic storm "
                "winds. Canyon constriction at Featherville accelerates wind flow past structures."
            ),
            "critical_corridors": [
                "South Fork Boise River canyon — fire channeled directly through both communities",
                "Trinity Mountain drainage NW — 2012 fire approach direction",
                "Elk Creek drainage NE — 2013 fire approach, multiple drainage fire merger",
                "Pine-Featherville Road corridor — fire along road cuts sole evacuation route",
            ],
            "rate_of_spread_potential": (
                "Dense mixed conifer forest with significant fuel accumulation. Surface fire "
                "1-2 mph, crown fire 2-4 mph in continuous canopy. The 2013 Elk Complex "
                "demonstrated that multiple lightning-ignited fires can merge and produce "
                "simultaneous assaults on the community from multiple directions, overwhelming "
                "suppression capacity."
            ),
            "spotting_distance": (
                "1-3 miles in forested canyon terrain. Canyon updrafts amplify lofting. "
                "Ember showers from ridge-top fires land directly in community due to narrow "
                "canyon geometry. Combustible roof materials on older structures highly receptive."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "No municipal water system. Individual wells and river drafting. No fire hydrants. "
                "USGS gauge station on South Fork but no firefighting water infrastructure. The "
                "destruction of 38 residences in 2013 demonstrated that water supply is the "
                "critical limiting factor in structure defense."
            ),
            "power": (
                "Idaho Power single-feed distribution through forested terrain. Power poles in "
                "fire corridor. Lines damaged in both 2012 and 2013 fires. Extended outages. "
                "No backup generation. Power loss cascades to water supply failure."
            ),
            "communications": (
                "Extremely limited cellular coverage in canyon terrain. No cell towers in immediate "
                "area. Landline service only for some properties. Emergency notification is "
                "door-to-door and word-of-mouth. Some residents chose to stay during 2013 "
                "evacuations partly due to lack of timely notification."
            ),
            "medical": (
                "No medical facilities. Nearest is Mountain Home (60+ miles) or Boise (105 miles). "
                "Volunteer fire/EMS provides first response. Air ambulance requires clear landing "
                "zone and may be grounded by fire activity/smoke. During 2013 Elk Complex, medical "
                "resources were fully committed to fire operations."
            ),
        },
        "demographics_risk_factors": {
            "population": 210,
            "seasonal_variation": (
                "Combined year-round pop ~210 (Featherville ~150, Pine ~60). Summer recreation "
                "doubles population with vacation homeowners, campers, and Anderson Ranch Reservoir "
                "visitors. About half of 450 homes are summer/weekend retreats — owners may not "
                "receive evacuation notifications or may not know evacuation routes."
            ),
            "elderly_percentage": "~25% (est.), significant retiree/fixed-income residents",
            "mobile_homes": (
                "Substantial presence of manufactured homes and older cabins. Historic mining "
                "town structures. Wood-frame construction universal. Many pre-date fire codes. "
                "Limited defensible space in forested canyon setting."
            ),
            "special_needs_facilities": (
                "None. No school (students bus to remote districts). No assisted living. No "
                "medical facilities. Community self-reliance is the only option. Some residents "
                "in 2013 refused to evacuate, complicating rescue operations."
            ),
        },
    },
}
