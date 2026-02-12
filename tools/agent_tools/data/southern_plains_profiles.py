"""Texas, Oklahoma & Kansas Fire-Vulnerable City Profiles
====================================================

Comprehensive terrain, evacuation, fire behavior, infrastructure, and demographic
data for 28 fire-vulnerable cities across the Southern Plains.
Winter grass fire regime (Nov-Mar), extreme wind events, dryline dynamics,
cold front passages, and hidden canyon/breaks terrain.

Usage:
    from tools.agent_tools.data.southern_plains_profiles import (
        PLAINS_TERRAIN_PROFILES,
        PLAINS_IGNITION_SOURCES,
        PLAINS_CLIMATOLOGY,
    )

Cities covered (28 entries across 3 states):
    TEXAS (17 cities):
        Abilene
        Amarillo
        Bastrop
        Borger Pampa
        Canadian
        Childress
        Cross Plains
        Eastland
        Fritch
        Granbury
        Lubbock
        Midland Odessa
        Perryton
        Possum Kingdom
        San Angelo
        Shamrock
        Wichita Falls
    OKLAHOMA (6 cities):
        Guthrie
        Newalla
        Norman
        Oklahoma City
        Stillwater
        Woodward
    KANSAS (5 cities):
        Ashland
        Dodge City
        Liberal
        Medicine Lodge
        Wichita

Sources:
    - NOAA Climate.gov: Feb 2024 megafire outbreak context
    - Texas Tribune: Smokehouse Creek, Eastland Complex coverage
    - Texas A&M Forest Service: Historical Fire Statistics
    - Oklahoma Forestry Services: Fire Situation Reports
    - NWS Amarillo, NWS Lubbock, NWS Dodge City
    - NASA Earth Observatory: East Amarillo Complex
    - WRCC / IEM / ASOS climatology archives
"""

# =============================================================================
# TERRAIN PROFILES -- 28 entries organized by state
# =============================================================================

PLAINS_TERRAIN_PROFILES = {

    # =========================================================================
    # TEXAS (17 cities)
    # =========================================================================

    # =========================================================================
    # 5. ABILENE, TX
    # =========================================================================
    "abilene_tx": {
        "center": (32.4487, -99.7331),
        "terrain_notes": (
            "Abilene sits at approximately 1,710 ft elevation on the Rolling Plains of West-Central "
            "Texas, at the transition between the flat agricultural land of the western plains and "
            "the more dissected terrain of the Cross Timbers ecological region to the east. The city "
            "is flanked by three reservoirs: Fort Phantom Hill Lake to the north, Lake Abilene (in "
            "Abilene State Park) to the southwest, and Lytle Lake to the southeast. The terrain is "
            "gently rolling with mesquite-dominated rangeland, scattered live oak mottes, and dense "
            "juniper (cedar) on limestone outcrops. The Elm Creek and Cedar Creek drainages pass "
            "through the city, providing riparian corridors of cottonwood, pecan, and salt cedar. "
            "The Callahan Divide, a low east-west ridge separating the Brazos and Colorado River "
            "watersheds, runs south of the city and creates terrain-influenced fire behavior as "
            "winds accelerate over the ridge. Abilene is located approximately 60 miles west of "
            "the Eastland Complex Fire area and lies in the same fire-weather corridor that "
            "produced the 2022 Eastland fires. The Cross Timbers post oak/blackjack oak woodland "
            "to the east creates heavy fuel loads that can support crown fire in extreme conditions. "
            "Taylor County regularly experiences winter grass fires driven by post-frontal winds, "
            "and the 2011 drought season produced multiple fires exceeding 10,000 acres in the "
            "surrounding area. Abilene's population of approximately 125,000 includes Dyess Air "
            "Force Base (5,000+ personnel) and three universities (ACU, Hardin-Simmons, McMurry). "
            "The city serves as the commercial hub for a 19-county region and hosts the regional "
            "medical center."
        ),
        "key_features": [
            {"name": "Callahan Divide", "bearing": "S", "type": "ridge",
             "notes": "Low E-W ridge separating Brazos/Colorado watersheds; wind acceleration zone; terrain-influenced fire behavior"},
            {"name": "Fort Phantom Hill", "bearing": "N", "type": "reservoir/historic",
             "notes": "Reservoir and historic fort ruins; mesquite rangeland surrounds; WUI development on shores"},
            {"name": "Abilene State Park", "bearing": "SW", "type": "state_park",
             "notes": "In Callahan Divide foothills; native grass, live oak, mesquite; prescribed burn management"},
            {"name": "Dyess AFB", "bearing": "W", "type": "military",
             "notes": "B-1B bomber base; 5,000+ personnel; fuel/munitions storage; open rangeland perimeter"},
            {"name": "Cross Timbers transition", "bearing": "E", "type": "ecological_boundary",
             "notes": "Post oak/blackjack oak woodland begins 20-30 mi east; heavier fuel loads; crown fire potential"},
        ],
        "elevation_range_ft": (1600, 2100),
        "wui_exposure": (
            "Significant WUI on south and southwest city margins in Callahan Divide foothills. "
            "Lake Fort Phantom Hill residential areas embedded in mesquite rangeland. Dyess AFB "
            "western perimeter abuts open grass/mesquite. Rural subdivisions along FM 89 and "
            "FM 707 corridors with limited fire protection."
        ),
        "historical_fires": [
            {"name": "Taylor County Complex", "year": 2011, "acres": 18000,
             "structures_destroyed": 12, "fatalities": 0, "cause": "multiple",
             "notes": "Multiple fires during exceptional drought; burned mesquite rangeland south and west of city; evacuations in Buffalo Gap area"},
            {"name": "Potosi Fire", "year": 2022, "acres": 3500,
             "structures_destroyed": 4, "fatalities": 0, "cause": "power line",
             "notes": "Burned south of Abilene near FM 89; part of March 2022 fire outbreak that also included Eastland Complex"},
            {"name": "Lake Fort Phantom Fire", "year": 2006, "acres": 6000,
             "structures_destroyed": 3, "fatalities": 0, "cause": "unknown",
             "notes": "Burned around reservoir north of city; threatened lakeside homes; mesquite and grass fuels"},
        ],
        "evacuation_routes": [
            {"route": "I-20", "direction": "east toward Fort Worth / west toward Midland", "lanes": 4,
             "bottleneck": "Loop 322 interchanges; Tye exit congestion",
             "risk": "Primary E-W corridor; flat terrain allows fire approach from either side; smoke visibility hazard"},
            {"route": "US-83/84", "direction": "north toward Anson / south toward Coleman", "lanes": 4,
             "bottleneck": "S 1st St/Winters Freeway through city; narrows to 2 lanes south",
             "risk": "Primary N-S route; passes through mesquite rangeland; long rural stretches"},
            {"route": "US-277", "direction": "south toward Bronte", "lanes": 2,
             "bottleneck": "2-lane through Callahan Divide; Buffalo Gap narrows",
             "risk": "Passes through fire-prone terrain south of city; limited escape options"},
        ],
        "fire_spread_characteristics": (
            "Rolling terrain creates variable fire behavior with wind acceleration on ridges and "
            "sheltering in draws. Mesquite/grass fuel matrix supports 3-8 mph spread rates with "
            "10-15 ft flame lengths. Juniper on limestone outcrops creates intense spot fires. "
            "Transition to Cross Timbers woodland east of city adds crown fire potential in heavy "
            "fuel loads. Post-frontal NW winds of 35-55 mph drive rapid spread across all fuel types. "
            "The Callahan Divide creates localized wind acceleration zones."
        ),
        "infrastructure_vulnerabilities": (
            "AEP Texas and Oncor transmission lines cross open terrain. Dyess AFB requires "
            "specialized fire protection for fuel storage, munitions, and B-1B fleet. Water supply "
            "from three reservoirs vulnerable to drought; 2011 demonstrated supply limitations. "
            "Regional medical center (Hendrick Health) serves 19-county area; surge capacity "
            "limited. Natural gas pipelines cross mesquite rangeland throughout county."
        ),
        "demographics_risk_factors": (
            "Population ~125,000 with 5,000+ military at Dyess AFB and 15,000+ university students "
            "across three campuses. Significant elderly population in rural Taylor County communities. "
            "Buffalo Gap and surrounding unincorporated areas rely on volunteer fire departments. "
            "Growing Hispanic/Latino population (~27%) with potential language barriers. Mobile home "
            "concentrations on south and west city margins."
        ),
    },

    # =========================================================================
    # 1. AMARILLO, TX — Palo Duro Canyon / Smokehouse Creek Fire 2024
    # =========================================================================
    "amarillo_tx": {
        "center": (35.222, -101.831),
        "terrain_notes": (
            "Amarillo sits at approximately 3,600 ft elevation on the Llano Estacado (Staked Plains), "
            "the vast, remarkably flat high plateau of the Texas Panhandle. The city straddles the "
            "boundary between the flat caprock surface to the south and the Canadian River Breaks to "
            "the north and east, where dramatic erosional terrain drops 800-1,000 ft into the Canadian "
            "River valley. Palo Duro Canyon, the second-largest canyon in the United States at 120 miles "
            "long and up to 800 ft deep, lies just 25 miles southeast. The terrain around Amarillo "
            "transitions from perfectly flat irrigated farmland and CRP grassland on the caprock to "
            "deeply dissected badlands, mesas, and juniper-studded breaks along the Canadian River "
            "corridor. Native vegetation is shortgrass prairie dominated by blue grama and buffalograss "
            "on the caprock, with sand sagebrush, shin oak, and one-seed juniper in the breaks. These "
            "fuels cure to 90-100% by December and remain dormant through March, creating continuous "
            "fine fuel beds across millions of acres. The 2006 East Amarillo Complex Fire demonstrated "
            "how fires ignited in the breaks can race across the flat caprock at 40+ mph rates of "
            "spread, driven by post-frontal northwest winds. The 2024 Smokehouse Creek Fire, which "
            "originated north of Stinnett in Hutchinson County, burned 1,074,047 acres and became "
            "the largest fire in Texas history, with the smoke plume visible from Amarillo for days. "
            "Amarillo's metro population of approximately 265,000 makes it the largest city in the "
            "Panhandle and the primary evacuation destination and staging area for rural fires across "
            "the region. The city's WUI exposure is concentrated along the northern and eastern edges "
            "where residential development meets the Canadian River Breaks terrain."
        ),
        "key_features": [
            {"name": "Palo Duro Canyon", "bearing": "SE", "type": "canyon",
             "notes": "Second-largest US canyon, 120 mi long, 800 ft deep; juniper/mesquite fuels; state park; fire runs channel through canyon"},
            {"name": "Canadian River Breaks", "bearing": "N/NE", "type": "dissected_terrain",
             "notes": "800-1000 ft drop from caprock to river; badlands, mesas, juniper; fire channeling through draws and arroyos"},
            {"name": "Llano Estacado caprock", "bearing": "S/W", "type": "plateau",
             "notes": "Flat high plains at 3,500-3,800 ft; continuous grass fuels; unobstructed wind fetch; 40+ mph fire spread potential"},
            {"name": "Lake Meredith NRA", "bearing": "NE", "type": "reservoir/recreation",
             "notes": "35 mi NE; Canadian River impoundment; Alibates Flint Quarries NM; breaks terrain with juniper fuels"},
            {"name": "Amarillo Creek drainage", "bearing": "through city", "type": "drainage",
             "notes": "Playa lake chain through city center; urban drainage corridor; potential fire pathway from breaks into developed areas"},
        ],
        "elevation_range_ft": (3400, 3800),
        "wui_exposure": (
            "Moderate-high along north and east city margins where residential subdivisions abut "
            "Canadian River Breaks. Scattered rural WUI throughout Potter and Randall counties. "
            "New development pushing into breaks terrain with limited defensible space."
        ),
        "historical_fires": [
            {"name": "Smokehouse Creek Fire", "year": 2024, "acres": 1074047,
             "structures_destroyed": 500, "fatalities": 2, "cause": "downed power line",
             "notes": "Largest fire in Texas history; originated N of Stinnett in Hutchinson Co; burned across Panhandle into OK; 500+ structures destroyed; caused by decayed power pole falling into grass; 11,000 lost power"},
            {"name": "East Amarillo Complex", "year": 2006, "acres": 907245,
             "structures_destroyed": 89, "fatalities": 12, "cause": "downed power lines",
             "notes": "Largest US fire of 2006; 12 deaths in 6.5 hours across 4 counties; 50+ mph winds; 8 towns evacuated; 5,000 cattle killed; all deaths within 45-mile radius"},
            {"name": "Malibu-Winery Fire", "year": 2017, "acres": 3000,
             "structures_destroyed": 0, "fatalities": 0, "cause": "unknown",
             "notes": "Burned in breaks terrain north of Amarillo; demonstrated fire spread through Canadian River corridor"},
        ],
        "evacuation_routes": [
            {"route": "I-40", "direction": "east/west", "lanes": 4,
             "bottleneck": "I-40/I-27 interchange downtown; Lakeside Dr exits east side",
             "risk": "Smoke from Panhandle fires can reduce visibility to zero on I-40; 2006 fire crossed I-40 and killed motorists trapped in smoke"},
            {"route": "I-27", "direction": "south toward Lubbock", "lanes": 4,
             "bottleneck": "Canyon interchange 15 mi south; merges with US-87",
             "risk": "Primary southbound escape; passes through Palo Duro Canyon rim area; single viable high-capacity southbound route"},
            {"route": "US-87/287", "direction": "north toward Dumas", "lanes": 4,
             "bottleneck": "Single highway north; passes through open grassland",
             "risk": "Fires in northern Potter County can cut this route; limited alternative roads"},
            {"route": "US-66/Route 66 Blvd", "direction": "east/west", "lanes": 2,
             "bottleneck": "Urban arterial; traffic signals through city",
             "risk": "Secondary east-west route; slower than I-40; passes through older neighborhoods with limited fire resistance"},
        ],
        "fire_spread_characteristics": (
            "Extreme fire spread potential on flat caprock terrain with continuous cured grass fuels. "
            "Post-frontal northwest winds of 40-70 mph drive fire runs at 5-15 mph rates of spread "
            "across open prairie. The 2006 East Amarillo Complex demonstrated 40+ mph wind-driven "
            "spread that outran vehicles. Fires in the Canadian River Breaks experience terrain-channeled "
            "winds through draws and arroyos, with spotting across mesas. Dryline passages in spring "
            "create extreme fire weather along the caprock escarpment. Continuous fuel beds extend "
            "hundreds of miles in every direction with no natural firebreaks."
        ),
        "infrastructure_vulnerabilities": (
            "Xcel Energy transmission lines cross open grassland and breaks terrain, vulnerable to "
            "wind damage that both causes fires and disrupts power during events. The 2024 Smokehouse "
            "Creek Fire left 11,000 without power. Amarillo's water supply from Lake Meredith is "
            "supplemented by Ogallala Aquifer wells; extended fire operations strain water resources. "
            "Natural gas infrastructure (pipelines, compressor stations) throughout the Panhandle "
            "creates explosion risk during grass fires. Cell towers on flat terrain have limited "
            "redundancy; wind/fire damage to a few towers can create coverage gaps across counties."
        ),
        "demographics_risk_factors": (
            "Metro population ~265,000 with significant rural agricultural population in surrounding "
            "counties. Large livestock operations (feedlots, ranches) require animal evacuation during "
            "fires. Aging rural population in surrounding communities with limited mobility. Significant "
            "meatpacking workforce (immigrant communities) may face language barriers in emergency "
            "communications. Rural volunteer fire departments are primary responders across the region "
            "with limited equipment and training for megafire events."
        ),
    },

    # =========================================================================
    # 10. BASTROP, TX — Lost Pines, 2011 Fire
    # =========================================================================
    "bastrop_tx": {
        "center": (30.1103, -97.3153),
        "terrain_notes": (
            "Bastrop sits at approximately 374 ft elevation along the Colorado River in Central "
            "Texas, within the unique Lost Pines forest, an isolated 70-square-mile stand of "
            "loblolly pine disjunct from the East Texas Piney Woods by over 100 miles. This "
            "ecological anomaly creates the most unusual and dangerous wildland fire fuel complex "
            "in the Southern Plains: a dense pine forest surrounded by post oak woodland and "
            "prairie, located in a region where fire weather is driven by the winter dryline/cold "
            "front regime rather than the summer lightning regime of East Texas. The terrain is "
            "rolling to hilly, with sandy Carrizo Formation soils supporting the pine forest, "
            "and clay soils supporting post oak savanna. The Colorado River provides a major "
            "drainage and potential firebreak, but the pine forest extends well beyond the river "
            "corridor on both sides. Bastrop State Park (6,000 acres) and Buescher State Park "
            "(1,016 acres) preserve portions of the Lost Pines, connected by a 13-mile scenic "
            "corridor (Park Road 1C). The 2011 Bastrop County Complex Fire was the most "
            "destructive wildfire in Texas history by structures: 32,000 acres burned, 1,696 homes "
            "destroyed, 2 people killed, and $350 million in insured damage. The fire was driven "
            "by northerly winds generated by Tropical Storm Lee to the east, which pulled dry air "
            "across drought-stressed pine forest. The fire burned 96% of Bastrop State Park. "
            "Recovery has been slow: the pine forest regeneration is competing with invasive grasses "
            "and oak resprouting. Bastrop's population of approximately 10,000 has grown "
            "significantly since 2011, with new development in fire-scarred areas raising concerns "
            "about repeat catastrophe. The city is 30 miles SE of Austin, and rapid suburban "
            "growth along SH-71 and SH-21 is pushing WUI deeper into the remaining Lost Pines."
        ),
        "key_features": [
            {"name": "Lost Pines forest", "bearing": "throughout", "type": "pine_forest",
             "notes": "Isolated 70 sq mi loblolly pine stand; disjunct from East TX by 100+ mi; heavy fuel loads; crown fire potential"},
            {"name": "Colorado River", "bearing": "through city", "type": "river",
             "notes": "Major river bisecting area; potential firebreak; riparian pecan/elm; bridges at Bastrop and downstream"},
            {"name": "Bastrop State Park", "bearing": "E", "type": "state_park",
             "notes": "6,000 acres; CCC-era cabins; 96% burned in 2011; pine regeneration ongoing; connected to Buescher SP"},
            {"name": "Circle D-KC Estates", "bearing": "NE", "type": "subdivision",
             "notes": "Origin area of 2011 fire (fallen pine tree on power line); heavily damaged; rebuilt with WUI concerns"},
            {"name": "Tahitian Village", "bearing": "SE", "type": "subdivision",
             "notes": "Dense pine forest subdivision; suffered catastrophic losses in 2011; narrow streets, limited escape routes"},
        ],
        "elevation_range_ft": (350, 550),
        "wui_exposure": (
            "Extreme WUI exposure. Lost Pines subdivisions (Circle D-KC Estates, Tahitian Village, "
            "Colovista) embedded in dense pine/oak forest. Post-2011 rebuilding in fire-scarred "
            "areas. Rapid Austin-area suburban growth pushing into Lost Pines along SH-71 and "
            "SH-21. Many homes with pine canopy directly overhead."
        ),
        "historical_fires": [
            {"name": "Bastrop County Complex Fire", "year": 2011, "acres": 32000,
             "structures_destroyed": 1696, "fatalities": 2, "cause": "downed power line (pine tree fell on line)",
             "notes": "Most destructive TX fire by structures; $350M insured damage; 96% of Bastrop State Park burned; driven by Tropical Storm Lee winds; 55-day duration; homes destroyed in 10 subdivisions"},
            {"name": "Bastrop County fires", "year": 2015, "acres": 4400,
             "structures_destroyed": 8, "fatalities": 0, "cause": "unknown",
             "notes": "Hidden Pines Fire burned in area adjacent to 2011 burn scar; demonstrated continued vulnerability even in recovering forest"},
            {"name": "Highway 71 area fires", "year": 2009, "acres": 1500,
             "structures_destroyed": 3, "fatalities": 0, "cause": "arson",
             "notes": "Multiple fires along SH-71 corridor in pine forest; precursor to 2011 catastrophe"},
        ],
        "evacuation_routes": [
            {"route": "SH-71", "direction": "west toward Austin / east toward La Grange", "lanes": 4,
             "bottleneck": "SH-71/SH-21 intersection; single-lane sections east of Bastrop",
             "risk": "Primary route to Austin; passes through Lost Pines forest; smoke reduced visibility to zero in 2011; fire crossed SH-71"},
            {"route": "SH-21", "direction": "NE toward Bryan/College Station", "lanes": 2,
             "bottleneck": "2-lane through pine forest; narrow shoulders; Park Road 1C intersection",
             "risk": "Passes through densest pine forest; 2011 fire burned along this corridor; limited escape if fire crosses road"},
            {"route": "TX-95", "direction": "south toward Smithville/Luling", "lanes": 2,
             "bottleneck": "Colorado River bridge; 2-lane through post oak",
             "risk": "Secondary route south; must cross Colorado River; post oak woodland fire risk on far side"},
            {"route": "SH-304", "direction": "SE toward Rosanky", "lanes": 2,
             "bottleneck": "Narrow 2-lane farm road; no services",
             "risk": "Rural route through fire-prone terrain; not designed for mass evacuation"},
        ],
        "fire_spread_characteristics": (
            "Loblolly pine crown fire is the most intense fire behavior in the Southern Plains. "
            "The 2011 fire demonstrated 40-60 ft flame lengths in continuous pine canopy with "
            "rates of spread exceeding 5 mph in wind-driven crown fire runs. Pine needle litter "
            "creates deep, dry fuel beds that support sustained burning. Post oak understory "
            "provides ladder fuels. Ember transport 1-2 miles ahead of main fire front through "
            "lofted pine bark embers. Fire-generated convection columns created their own weather "
            "patterns in 2011. Drought-stressed pine produces volatile resins that increase fire "
            "intensity dramatically."
        ),
        "infrastructure_vulnerabilities": (
            "Bluebonnet Electric Cooperative lines through pine forest highly vulnerable to "
            "tree fall (proven ignition source for 2011 fire). Bastrop water system dependent on "
            "Colorado River and wells; fire flow inadequate for subdivision defense. Narrow "
            "subdivision roads (Tahitian Village, Circle D) create evacuation bottlenecks. Cell "
            "towers in pine forest damaged by crown fire. Bastrop State Park infrastructure "
            "rebuilt post-2011 but remains exposed. SH-71 is sole high-capacity route west."
        ),
        "demographics_risk_factors": (
            "Population ~10,000 (growing, Austin exurban). Significant post-2011 rebuilding with "
            "improved building codes but continued forest proximity. Austin-area commuters may "
            "be away during daytime fires. Retirement communities in Lost Pines. Mobile homes "
            "in rural areas. Lower-income residents in older subdivisions with limited resources "
            "for fire hardening. PTSD from 2011 fire affects community emergency response. "
            "Rapid growth adding population in fire-prone areas."
        ),
    },

    # =========================================================================
    # 7. BORGER/PAMPA, TX — Panhandle
    # =========================================================================
    "borger_pampa_tx": {
        "center": (35.667, -101.397),
        "terrain_notes": (
            "Borger and Pampa are industrial towns in the northeastern Texas Panhandle, sitting at "
            "approximately 3,100-3,200 ft elevation on the high plains between the Canadian River "
            "Breaks to the south and the flat shortgrass prairie extending north toward the Oklahoma "
            "Panhandle. Borger lies in the Canadian River valley in Hutchinson County, while Pampa "
            "sits on the flat caprock surface in Gray County, 25 miles to the northeast. The terrain "
            "around Borger is characterized by the deeply eroded Canadian River Breaks: a network of "
            "canyons, mesas, buttes, and draws that drop 400-600 ft from the caprock surface to the "
            "river bottom. These breaks are vegetated with one-seed juniper, sand sagebrush, and "
            "mixed grass, creating complex fuels in rugged terrain. North of Pampa, the landscape "
            "flattens into the continuous shortgrass prairie that extends to the Kansas line. Both "
            "cities have significant petrochemical infrastructure: the Phillips 66 Borger Refinery "
            "Complex is one of the largest refineries in the mid-continent, and numerous natural gas "
            "processing plants, compressor stations, and pipeline networks cross the region. The "
            "2024 Smokehouse Creek Fire originated north of Stinnett (10 miles north of Borger) in "
            "Hutchinson County when a decayed power pole fell into grass, ultimately burning over "
            "1 million acres. The 2006 East Amarillo Complex Fire also impacted Gray County near "
            "Pampa, killing multiple people. Both cities have experienced direct fire threat multiple "
            "times, and the combination of continuous grass fuels, extreme winds, and dense "
            "petrochemical infrastructure creates a uniquely hazardous fire environment."
        ),
        "key_features": [
            {"name": "Canadian River Breaks", "bearing": "S/SE", "type": "dissected_terrain",
             "notes": "400-600 ft deep canyons and mesas; juniper/sagebrush fuels; fire channeling through draws; rugged suppression access"},
            {"name": "Phillips 66 Borger Refinery", "bearing": "within Borger", "type": "industrial",
             "notes": "Major refinery complex; fuel storage; process units; creates explosion/toxic release risk during fires"},
            {"name": "Smokehouse Creek Fire origin", "bearing": "N of Stinnett", "type": "fire_origin",
             "notes": "Feb 26 2024 fire started here from downed power line; grew to 1,074,047 acres; demonstrates extreme fire risk"},
            {"name": "Lake Meredith NRA", "bearing": "W", "type": "reservoir/recreation",
             "notes": "Canadian River impoundment; breaks terrain surrounds lake; recreational areas in fire-prone vegetation"},
            {"name": "Flat shortgrass prairie", "bearing": "N/NE", "type": "grassland",
             "notes": "Continuous cured grass from Pampa to Kansas line; unimpeded wind fetch; 5-15 mph fire spread rates"},
        ],
        "elevation_range_ft": (2800, 3400),
        "wui_exposure": (
            "High exposure for both cities. Borger surrounded by breaks terrain and refinery "
            "infrastructure. Pampa on open prairie with grass fuels to city margins. Stinnett, "
            "Skellytown, and White Deer smaller communities with minimal defensible space. "
            "Petrochemical facilities throughout region create compounding risk."
        ),
        "historical_fires": [
            {"name": "Smokehouse Creek Fire", "year": 2024, "acres": 1074047,
             "structures_destroyed": 500, "fatalities": 2, "cause": "downed power line",
             "notes": "Originated N of Stinnett in Hutchinson County; over 100 homes destroyed in Hutchinson County alone; decayed power pole"},
            {"name": "East Amarillo Complex", "year": 2006, "acres": 907245,
             "structures_destroyed": 89, "fatalities": 12, "cause": "downed power lines",
             "notes": "Borger Fire component burned through Gray/Hutchinson counties; multiple fatalities near Pampa; 50+ mph winds"},
            {"name": "Stinnett area fires", "year": 2017, "acres": 8000,
             "structures_destroyed": 3, "fatalities": 0, "cause": "power line",
             "notes": "Part of March 2017 Panhandle fire outbreak; burned in breaks terrain near Canadian River"},
        ],
        "evacuation_routes": [
            {"route": "TX-152", "direction": "east toward Pampa / west toward Borger", "lanes": 2,
             "bottleneck": "2-lane through open prairie; Skellytown intersection",
             "risk": "Connects twin cities through fire-prone grassland; single route between communities"},
            {"route": "TX-136", "direction": "south toward Amarillo", "lanes": 2,
             "bottleneck": "Descends into Canadian River breaks; narrow road through rugged terrain",
             "risk": "Passes through breaks terrain where Smokehouse Creek Fire burned; fire can trap travelers in canyon"},
            {"route": "US-60", "direction": "east toward Miami/Canadian", "lanes": 2,
             "bottleneck": "2-lane through open prairie; no services for long stretches",
             "risk": "Flat terrain allows fire approach from any direction; no shelter or escape points"},
        ],
        "fire_spread_characteristics": (
            "Dual fire behavior regime: fast wind-driven grass fires on flat caprock surface "
            "(5-15 mph ROS) and terrain-channeled fires in Canadian River Breaks with complex "
            "wind patterns, spotting across mesas, and juniper torching. Post-frontal NW winds "
            "of 50-70 mph are the primary driver. Petrochemical infrastructure creates secondary "
            "ignition sources and explosion risk during grass fires. Continuous fuel beds extend "
            "hundreds of miles with no natural firebreaks."
        ),
        "infrastructure_vulnerabilities": (
            "Phillips 66 refinery and multiple gas processing plants create cascading failure risk. "
            "Natural gas pipelines and compressor stations throughout region. Xcel Energy "
            "transmission vulnerable to wind damage (proven ignition source). Water supply limited "
            "to Lake Meredith (chronically low) and groundwater. Small rural hospitals in Borger "
            "and Pampa inadequate for mass casualty events. Volunteer fire departments in satellite "
            "communities have minimal equipment."
        ),
        "demographics_risk_factors": (
            "Combined population ~30,000 (Borger ~13,000, Pampa ~17,000); both declining. "
            "Aging, economically stressed communities with limited resources. Significant "
            "petrochemical workforce. Rural elderly scattered across isolated ranch properties. "
            "Limited evacuation capacity on 2-lane highways. Stinnett, Skellytown, White Deer "
            "have populations under 2,000 each with volunteer-only fire protection."
        ),
    },

    # =========================================================================
    # 19. CANADIAN, TX — Hemphill County, Smokehouse Creek Fire Impact
    # =========================================================================
    "canadian_tx": {
        "center": (35.9129, -100.3820),
        "terrain_notes": (
            "Canadian sits at approximately 2,339 ft elevation on the Canadian River in Hemphill "
            "County, in the northeastern Texas Panhandle. The city is named for the Canadian River, "
            "which cuts a dramatic valley 300-500 ft deep through the surrounding high plains, "
            "creating the most significant terrain feature in the region. The Canadian River breaks "
            "here are characterized by steep canyon walls, isolated mesas, deep draws, and "
            "juniper-studded slopes descending to the sandy, braided river channel. The town "
            "itself sits on a bench above the river valley, with the breaks terrain extending "
            "north and south. Vegetation on the uplands is mixed-grass prairie (little bluestem, "
            "sideoats grama, blue grama) with one-seed juniper, sand sagebrush, and skunkbush "
            "sumac on canyon slopes. The Gene Howe Wildlife Management Area (5,394 acres) lies "
            "along the Canadian River east of town, managed by TPWD for lesser prairie-chicken "
            "habitat. The 2024 Smokehouse Creek Fire devastated Hemphill County: 400,000 acres "
            "burned (approximately 70% of the county), 107 structures were destroyed including "
            "53 homes in Canadian, and approximately 7,000 mother cows were killed. The fire "
            "burned 98% of the Gene Howe WMA. Canadian's population of approximately 2,600 "
            "makes it a small ranching community that was profoundly impacted by the largest "
            "fire in Texas history. The city sits at the junction of US-60 and US-83, making "
            "it a critical crossroads for the northeastern Panhandle. The combination of deep "
            "canyon terrain, continuous grass fuels on the uplands, juniper-heavy slopes, and "
            "extreme post-frontal winds creates one of the most dangerous fire environments "
            "in the Southern Plains."
        ),
        "key_features": [
            {"name": "Canadian River valley", "bearing": "through area", "type": "river_canyon",
             "notes": "300-500 ft deep valley; steep canyon walls; juniper/sagebrush slopes; braided sandy channel; fire channeling through draws"},
            {"name": "Gene Howe WMA", "bearing": "E", "type": "wildlife_management",
             "notes": "5,394 acres; 98% burned in 2024 Smokehouse Creek Fire; lesser prairie-chicken habitat; Canadian River frontage"},
            {"name": "Hemphill County uplands", "bearing": "N/S", "type": "grassland",
             "notes": "Mixed-grass prairie; 70% of county burned in 2024; continuous fine fuels; cattle ranching operations"},
            {"name": "US-60/US-83 junction", "bearing": "in town", "type": "transportation",
             "notes": "Critical crossroads for NE Panhandle; only paved routes through county; evacuation bottleneck"},
        ],
        "elevation_range_ft": (2200, 2800),
        "wui_exposure": (
            "High WUI exposure. Canadian surrounded by breaks terrain and grassland. 53 homes "
            "destroyed in town during 2024 fire. Rural ranches throughout county are primary "
            "WUI exposure. Post-fire rebuilding underway but community resources limited. "
            "Gene Howe WMA recreational areas fire-exposed."
        ),
        "historical_fires": [
            {"name": "Smokehouse Creek Fire", "year": 2024, "acres": 1074047,
             "structures_destroyed": 500, "fatalities": 2, "cause": "downed power line",
             "notes": "In Hemphill County: 400,000 acres burned (70% of county), 107 structures destroyed, 53 homes in Canadian, 7,000 mother cows killed, 98% of Gene Howe WMA burned"},
            {"name": "Hemphill County fire", "year": 2017, "acres": 18000,
             "structures_destroyed": 5, "fatalities": 0, "cause": "power line",
             "notes": "Part of March 2017 Panhandle fire outbreak; burned breaks terrain and upland grass; threatened Canadian"},
            {"name": "Canadian River fires", "year": 2006, "acres": 8000,
             "structures_destroyed": 2, "fatalities": 0, "cause": "unknown",
             "notes": "Part of East Amarillo Complex era fires; burned in breaks terrain along Canadian River"},
        ],
        "evacuation_routes": [
            {"route": "US-60", "direction": "west toward Pampa / east toward Higgins", "lanes": 2,
             "bottleneck": "2-lane through open prairie; Canadian River bridge west of town",
             "risk": "Primary E-W route; fire crossed this highway during 2024 Smokehouse Creek; long distances between communities"},
            {"route": "US-83", "direction": "north toward Perryton / south toward Shamrock", "lanes": 2,
             "bottleneck": "2-lane through breaks terrain; steep grades descending to Canadian River",
             "risk": "Passes through canyon terrain where fire behavior is most extreme; sole N-S route through county"},
            {"route": "FM roads", "direction": "various", "lanes": 2,
             "bottleneck": "Narrow, some unpaved; dead-end ranch roads",
             "risk": "Rural escape routes through continuous grass/juniper fuels; no shelter points; can trap evacuees"},
        ],
        "fire_spread_characteristics": (
            "Dual fire regime: rapid wind-driven grass fires on upland prairie (5-12 mph ROS) "
            "and terrain-channeled fires in Canadian River breaks with juniper torching (30-40 ft "
            "flame lengths), erratic canyon winds, and spotting across mesas (0.5-1 mi). The 2024 "
            "Smokehouse Creek Fire demonstrated both regimes simultaneously, burning 70% of the "
            "county in days. Post-frontal NW winds of 50-70 mph drive fire across all fuel types. "
            "Canyon draws accelerate fire and create unpredictable direction changes."
        ),
        "infrastructure_vulnerabilities": (
            "Xcel Energy transmission through breaks terrain; proven fire ignition source. "
            "Municipal water from groundwater wells; extremely limited fire flow. Small volunteer "
            "fire department devastated by 2024 fire (equipment damaged, members exhausted). "
            "Hemphill County Memorial Hospital (~15 beds) only medical facility in county. "
            "Cell coverage gaps in canyon terrain. Post-2024 infrastructure still under repair."
        ),
        "demographics_risk_factors": (
            "Population ~2,600. Small ranching community profoundly impacted by 2024 fire. "
            "7,000 mother cows killed devastated ranching economy. PTSD and mental health "
            "impacts severe. Aging population with limited mobility. Volunteer fire department "
            "recruitment challenged. Community rebuilding with limited financial resources. "
            "Seasonal hunting/tourism population in breaks terrain unfamiliar with fire risk."
        ),
    },

    # =========================================================================
    # 8. CHILDRESS, TX
    # =========================================================================
    "childress_tx": {
        "center": (34.4265, -100.2040),
        "terrain_notes": (
            "Childress sits at approximately 1,877 ft elevation in the eastern Texas Panhandle's "
            "Rolling Plains, at the junction of US-83, US-62, and US-287, making it a critical "
            "crossroads for the region. The city lies on the Prairie Dog Town Fork of the Red River, "
            "which carves a shallow valley through the rolling mesquite grassland. The terrain "
            "transitions from flat to gently rolling, with red sandy loam soils supporting dense "
            "mesquite, lotebush, and native grass. To the north and west, the landscape rises toward "
            "the Caprock Escarpment, while to the east the Rolling Plains continue into the Cross "
            "Timbers transition zone. Childress County is characterized by extensive ranching "
            "operations with continuous grass fuels across the landscape. The mesquite in this area "
            "has significantly increased in density over the past century due to fire suppression and "
            "overgrazing, creating heavier fuel loads than the historical shortgrass prairie. The "
            "dryline frequently passes through this area, and post-frontal cold fronts produce "
            "some of the most extreme fire weather in the Southern Plains: 40-60 mph northwest "
            "winds with single-digit relative humidity across miles of cured grass. Childress "
            "experienced significant fires during the 2006 and 2011 fire seasons, with fires "
            "exceeding 20,000 acres in the surrounding rangeland. The city has a population of "
            "approximately 6,100 and serves as a small regional center for surrounding agricultural "
            "communities. Its location at the intersection of three US highways makes it both a "
            "critical evacuation waypoint and vulnerable to highway-corridor fires. The Prairie "
            "Dog Town Fork of the Red River provides minimal firebreak capability due to salt "
            "cedar infestation along its banks."
        ),
        "key_features": [
            {"name": "Prairie Dog Town Fork Red River", "bearing": "through area", "type": "river",
             "notes": "Shallow river valley through rolling plains; salt cedar riparian fuels; minimal firebreak value"},
            {"name": "Caprock Escarpment", "bearing": "NW", "type": "escarpment",
             "notes": "30-40 mi NW; terrain rise to Llano Estacado; fire acceleration on escarpment slopes"},
            {"name": "Baylor/Childress Lake", "bearing": "NE", "type": "reservoir",
             "notes": "Small municipal water supply; mesquite rangeland surrounds; limited firebreak"},
            {"name": "US-287/US-83 junction", "bearing": "in city", "type": "transportation",
             "notes": "Critical crossroads for Panhandle; evacuation waypoint; highway corridor fire risk"},
        ],
        "elevation_range_ft": (1700, 2100),
        "wui_exposure": (
            "Small-city WUI with mesquite rangeland on all margins. Residential development is "
            "sparse but directly adjacent to continuous grass/mesquite fuels. Rural ranchettes "
            "along FM roads with no municipal fire protection. Childress serves as regional "
            "evacuation center for surrounding communities."
        ),
        "historical_fires": [
            {"name": "Childress County Fire", "year": 2006, "acres": 20000,
             "structures_destroyed": 5, "fatalities": 0, "cause": "power line",
             "notes": "Part of 2006 Panhandle fire outbreak; burned mesquite rangeland N and W of city; post-frontal winds"},
            {"name": "Rolling Plains Complex", "year": 2011, "acres": 15000,
             "structures_destroyed": 8, "fatalities": 0, "cause": "multiple",
             "notes": "Multiple fires during exceptional drought; burned close to city limits; water supply strained"},
            {"name": "FM 268 Fire", "year": 2022, "acres": 4500,
             "structures_destroyed": 1, "fatalities": 0, "cause": "equipment",
             "notes": "Fast-moving grass fire east of Childress during March cold front; reached city outskirts"},
        ],
        "evacuation_routes": [
            {"route": "US-287", "direction": "SE toward Wichita Falls / NW toward Amarillo", "lanes": 2,
             "bottleneck": "2-lane highway through open rangeland; limited passing zones",
             "risk": "Primary route to larger cities; 120+ mi to Amarillo; fire can close road at multiple points"},
            {"route": "US-83", "direction": "north toward Shamrock / south toward Paducah", "lanes": 2,
             "bottleneck": "2-lane through mesquite country; no services for long stretches",
             "risk": "Passes through continuous fire-prone rangeland; limited escape options"},
            {"route": "US-62", "direction": "east toward Quanah", "lanes": 2,
             "bottleneck": "2-lane; narrow bridges over Red River tributaries",
             "risk": "Rolling terrain limits visibility; fires can approach quickly from draws"},
        ],
        "fire_spread_characteristics": (
            "Rolling terrain with dense mesquite/grass fuels supports 3-8 mph rates of spread in "
            "post-frontal winds. Mesquite produces 10-15 ft flame lengths that resist direct "
            "attack. Salt cedar along river corridors burns intensely with embers lofted by "
            "convection columns. Dryline passages create abrupt transitions to extreme fire "
            "weather. Continuous fuel beds extend in all directions with no natural firebreaks "
            "for 30+ miles."
        ),
        "infrastructure_vulnerabilities": (
            "Limited water supply from small reservoirs and groundwater; extended fire operations "
            "strain capacity. Power lines cross open rangeland. Small volunteer fire department "
            "with limited apparatus. Regional hospital (Childress Regional Medical Center) has "
            "minimal beds. Highway corridors vulnerable to smoke closure. No interstate access; "
            "all routes are 2-lane highways."
        ),
        "demographics_risk_factors": (
            "Population ~6,100 and declining. Aging ranching community with limited mobility. "
            "Serves as regional center for scattered rural population. Limited emergency services "
            "for county size. Economically stressed community with limited resources for fire "
            "mitigation. High percentage of elderly and low-income residents."
        ),
    },

    # =========================================================================
    # 22. CROSS PLAINS, TX — Cross Plains Fire 2005
    # =========================================================================
    "cross_plains_tx": {
        "center": (32.1273, -99.1644),
        "terrain_notes": (
            "Cross Plains sits at approximately 1,718 ft elevation in Callahan County, at the "
            "heart of the Cross Timbers ecological region of Central Texas. The city lies along "
            "Turkey Creek at the junction of SH-36 and SH-206, surrounded by dense post oak, "
            "blackjack oak, and live oak woodland with extensive eastern redcedar encroachment. "
            "The terrain is rolling to hilly, with sandstone ridges and limestone outcrops "
            "creating complex topography that influences fire behavior. The Cross Timbers here "
            "represents some of the densest native woodland in the Southern Plains: post oak and "
            "blackjack oak form a closed canopy on sandy uplands, with heavy leaf litter, dead "
            "branches, and eastern redcedar creating continuous fuel from surface to crown. Pecan "
            "Creek, Turkey Creek, and other small drainages cut shallow valleys that channel "
            "wind and fire. The city experienced a catastrophic wildfire on December 27, 2005, "
            "when a grass fire started by a lit cigarette 5 miles west along Highway 36 was "
            "pushed into town by 30+ mph cold front winds. The fire destroyed 116 homes (85 "
            "single-family homes, 25 mobile homes, 6 apartment units), damaged 36 additional "
            "homes, destroyed the First United Methodist Church, killed 2 people, and caused "
            "$11 million in property damage. The fire burned 7,665 acres of land. December 2005 "
            "had received only 17% of normal rainfall, and the drought conditions combined with "
            "cold front winds and dry air created critical fire weather. Cross Plains is a small "
            "community of approximately 1,000 people that was profoundly shaped by this fire. "
            "The city lies 30 miles south of Abilene and 60 miles west of the Eastland Complex "
            "area, in the same Cross Timbers fuel type that produced the 2022 Eastland fires. "
            "Eastern redcedar continues to encroach on formerly open rangeland throughout "
            "Callahan County, continuously increasing wildfire hazard."
        ),
        "key_features": [
            {"name": "Cross Timbers woodland", "bearing": "throughout", "type": "woodland",
             "notes": "Dense post oak/blackjack/live oak; heavy fuel loads; closed canopy on sandy uplands; crown fire potential"},
            {"name": "Eastern redcedar encroachment", "bearing": "throughout", "type": "vegetation_change",
             "notes": "Aggressive invasion converting open rangeland to continuous canopy fuel; primary hazard intensifier"},
            {"name": "Turkey Creek", "bearing": "through town", "type": "creek",
             "notes": "Small drainage; riparian corridor; fire channeling potential; 2005 fire approached along this drainage"},
            {"name": "SH-36 fire approach corridor", "bearing": "W", "type": "fire_corridor",
             "notes": "2005 fire started 5 mi W along SH-36; cold front winds pushed fire E into town; continuous fuel along highway"},
        ],
        "elevation_range_ft": (1550, 1900),
        "wui_exposure": (
            "Extreme WUI exposure. Cross Timbers woodland extends to property lines throughout "
            "community. 2005 fire demonstrated that fire can penetrate to the center of town. "
            "Mobile homes comprised 25 of 116 destroyed structures. Post-fire rebuilding improved "
            "some setbacks but many properties remain in dense vegetation."
        ),
        "historical_fires": [
            {"name": "Cross Plains Fire", "year": 2005, "acres": 7665,
             "structures_destroyed": 116, "fatalities": 2, "cause": "lit cigarette",
             "notes": "116 homes destroyed (85 houses, 25 mobile homes, 6 apartments); 36 homes damaged; First United Methodist Church destroyed; $11M damage; only 17% normal Dec rainfall; 30+ mph cold front winds"},
            {"name": "Callahan County fires", "year": 2011, "acres": 8000,
             "structures_destroyed": 6, "fatalities": 0, "cause": "multiple",
             "notes": "Drought-driven fires in Cross Timbers; burned in same fuel type as 2005 fire; demonstrated continuing vulnerability"},
            {"name": "Cross Timbers area fires", "year": 2022, "acres": 3000,
             "structures_destroyed": 2, "fatalities": 0, "cause": "unknown",
             "notes": "Part of broader 2022 fire outbreak that included Eastland Complex; Cross Timbers fuels in Callahan County"},
        ],
        "evacuation_routes": [
            {"route": "SH-36", "direction": "east toward Rising Star / west toward Abilene", "lanes": 2,
             "bottleneck": "2-lane through Cross Timbers; fire approached along this route in 2005",
             "risk": "Primary E-W route but 2005 fire demonstrated fire can race along this corridor; continuous woodland fuels both sides"},
            {"route": "SH-206", "direction": "north toward Cisco / south toward Coleman", "lanes": 2,
             "bottleneck": "2-lane through rolling woodland; narrow in town",
             "risk": "Passes through dense Cross Timbers; fire can close road at any point; limited escape options"},
            {"route": "FM 880/county roads", "direction": "various", "lanes": 2,
             "bottleneck": "Narrow FM roads through woodland; dead-end ranch roads",
             "risk": "Rural routes through continuous fuel; many dead-ends; not designed for evacuation"},
        ],
        "fire_spread_characteristics": (
            "Cross Timbers fuel complex produces intense fire behavior with 20-40 ft flame lengths "
            "in crown fire. Post oak/blackjack canopy with cedar understory creates continuous "
            "fuel from surface to crown. 2005 fire demonstrated that wind-driven fire in Cross "
            "Timbers can overwhelm a community in minutes: fire traveled 5 miles in approximately "
            "1 hour across woodland terrain. Cedar torching launches firebrands 0.5-1 mi ahead "
            "of main front. Cold front passages with 30-40 mph winds and single-digit RH "
            "create the most dangerous conditions. Winter dormancy (leaf fall) increases surface "
            "fuel loads but cedar remains green and volatile year-round."
        ),
        "infrastructure_vulnerabilities": (
            "AEP Texas lines through Cross Timbers. Municipal water system adequate for small "
            "town but overwhelmed during simultaneous structure fires. Volunteer fire department "
            "with minimal apparatus. No hospital; nearest in Abilene (30 mi) or Brownwood (25 mi). "
            "All routes are 2-lane state highways through continuous woodland. Cell coverage "
            "limited in rural areas. Many structures have wood siding and shingled roofs "
            "vulnerable to ember ignition."
        ),
        "demographics_risk_factors": (
            "Population ~1,000. Small, aging community still affected by 2005 fire trauma. High "
            "poverty rates limit fire-resistant construction and vegetation management. Mobile "
            "homes are significant housing stock (25 of 116 structures destroyed in 2005 were "
            "mobile homes). Limited volunteer fire department resources. Elderly population "
            "with limited mobility. Post-fire population decline has reduced community capacity."
        ),
    },

    # =========================================================================
    # 9. EASTLAND, TX — Eastland Complex 2022
    # =========================================================================
    "eastland_tx": {
        "center": (32.4015, -98.8175),
        "terrain_notes": (
            "Eastland sits at approximately 1,421 ft elevation in the heart of the Cross Timbers "
            "ecological region of Central Texas, where post oak and blackjack oak woodland creates "
            "the heaviest natural fuel loads in the Southern Plains. The terrain is rolling to hilly, "
            "with sandstone ridges and limestone outcrops supporting dense woodland, while valleys "
            "and draws contain mesquite, live oak, and eastern redcedar. Eastland County is bisected "
            "by the Leon River and numerous creeks (Colony, Sabanna, Jim Ned) that create riparian "
            "corridors of pecan, elm, and salt cedar. The Cross Timbers here consists of dense, "
            "sometimes impenetrable thickets of post oak and blackjack oak on sandy soils, with "
            "understory of little bluestem, Indiangrass, and eastern redcedar. This fuel type is "
            "dramatically different from the shortgrass prairie to the west: fires in Cross Timbers "
            "produce extreme heat (up to 1,200 BTU/ft/sec), tall flame lengths (30-50 ft in crown "
            "fire), and resist direct attack. The 2022 Eastland Complex Fire demonstrated this when "
            "a cold front on March 17 produced strong winds that ignited multiple fires across the "
            "county, ultimately burning 54,463 acres and destroying 158 structures. The town of "
            "Carbon (population ~272) was nearly completely destroyed, with 86 homes lost. Sergeant "
            "Barbara Fenley of the Eastland County Sheriff's Office was killed attempting to "
            "evacuate residents from Carbon. Eastern redcedar encroachment has dramatically "
            "increased fuel loads across formerly open rangeland, creating continuous canopy fuels "
            "that support crown fire runs. Eastland's population of approximately 3,900 makes it "
            "a small community with limited fire suppression resources facing extreme wildland "
            "fire exposure."
        ),
        "key_features": [
            {"name": "Cross Timbers woodland", "bearing": "throughout", "type": "woodland",
             "notes": "Dense post oak/blackjack oak on sandy soils; heaviest natural fuel loads in Southern Plains; crown fire potential"},
            {"name": "Leon River", "bearing": "through area", "type": "river",
             "notes": "Primary drainage; pecan/elm riparian; Lake Leon impoundment SE of city; limited firebreak"},
            {"name": "Carbon townsite", "bearing": "S", "type": "community",
             "notes": "Pop ~272; nearly destroyed in 2022 Eastland Complex; 86 homes lost; demonstrated catastrophic WUI exposure"},
            {"name": "Eastern redcedar encroachment", "bearing": "throughout", "type": "vegetation_change",
             "notes": "Aggressive cedar invasion of open rangeland creating continuous canopy fuels; primary fire hazard intensifier"},
            {"name": "Lake Leon", "bearing": "SE", "type": "reservoir",
             "notes": "Reservoir on Leon River; WUI homes on shores in woodland setting; fire-exposed recreational area"},
        ],
        "elevation_range_ft": (1300, 1700),
        "wui_exposure": (
            "Extreme WUI exposure across entire county. Cross Timbers woodland extends to city "
            "limits of Eastland, Cisco, Ranger, and other communities. Lake Leon residential areas "
            "embedded in dense woodland. Carbon destroyed in 2022 demonstrates extreme vulnerability. "
            "Eastern redcedar encroachment has dramatically increased fuel continuity."
        ),
        "historical_fires": [
            {"name": "Eastland Complex", "year": 2022, "acres": 54463,
             "structures_destroyed": 158, "fatalities": 1, "cause": "cold front/multiple ignitions",
             "notes": "8 separate fires ignited March 17 during cold front; 86 homes destroyed in Carbon; Sgt Barbara Fenley killed evacuating residents; most destructive TX fire of 2022"},
            {"name": "Eastland County fires", "year": 2011, "acres": 12000,
             "structures_destroyed": 20, "fatalities": 0, "cause": "multiple",
             "notes": "Multiple fires during exceptional drought; Cross Timbers fuels produced extreme fire behavior"},
            {"name": "Ranger area fire", "year": 2006, "acres": 5000,
             "structures_destroyed": 6, "fatalities": 0, "cause": "power line",
             "notes": "Burned through Cross Timbers woodland near Ranger; demonstrated crown fire potential in post oak/cedar"},
        ],
        "evacuation_routes": [
            {"route": "I-20", "direction": "east toward Fort Worth / west toward Abilene", "lanes": 4,
             "bottleneck": "Eastland/Cisco exits limited capacity; on-ramp congestion",
             "risk": "Primary escape route but smoke from Cross Timbers fires reduces visibility to zero; 2022 fire crossed I-20 corridor"},
            {"route": "US-183", "direction": "south toward Brownwood / north toward Breckenridge", "lanes": 2,
             "bottleneck": "2-lane through dense Cross Timbers; no bypass",
             "risk": "Passes through heaviest fuel loads; fires can close road quickly; limited shoulders for escape"},
            {"route": "TX-6", "direction": "south toward De Leon/Dublin", "lanes": 2,
             "bottleneck": "2-lane through rolling woodland; Carbon was on this route",
             "risk": "2022 fire destroyed Carbon along this route; demonstrates extreme vulnerability of rural highway evacuation"},
        ],
        "fire_spread_characteristics": (
            "Cross Timbers fuels produce the most intense fire behavior in the Southern Plains. "
            "Post oak/blackjack canopy fires generate extreme heat (1,200+ BTU/ft/sec) with "
            "30-50 ft flame lengths. Eastern redcedar creates ladder fuels that transition surface "
            "fires to crown fires. Rate of spread 2-5 mph in woodland but flame lengths and heat "
            "make direct attack impossible. Cold front winds of 35-55 mph drive fire through "
            "continuous canopy. Spotting 0.5-1 mile ahead of main fire front via cedar torch "
            "embers. The 2022 Eastland Complex demonstrated catastrophic fire runs that outpaced "
            "evacuation in Carbon."
        ),
        "infrastructure_vulnerabilities": (
            "Oncor transmission lines through dense woodland highly vulnerable to fire damage. "
            "Rural water systems dependent on small reservoirs and wells; hydrant coverage minimal "
            "outside city limits. Cell towers in woodland settings vulnerable to fire. Carbon had "
            "no municipal fire department; relied on volunteer units with long response times. "
            "I-20 can be closed by smoke, isolating communities south of the highway."
        ),
        "demographics_risk_factors": (
            "Eastland pop ~3,900; Carbon pop ~272 (pre-fire). Aging rural communities with limited "
            "mobility. High poverty rates limit fire-resistant construction. Mobile homes comprise "
            "significant housing stock in rural areas. Volunteer fire departments are sole "
            "protection for most county residents. Limited emergency communication in woodland "
            "areas where cell coverage is poor. 2022 fire killed law enforcement officer "
            "attempting evacuation, demonstrating danger to first responders."
        ),
    },

    # =========================================================================
    # 11. FRITCH, TX — Smokehouse Creek Fire Origin Area
    # =========================================================================
    "fritch_tx": {
        "center": (35.6370, -101.6024),
        "terrain_notes": (
            "Fritch is a small community of approximately 2,000 people at 3,200 ft elevation on the "
            "southern shore of Lake Meredith in Hutchinson County, deep in the Canadian River Breaks "
            "of the Texas Panhandle. The terrain is among the most rugged in the Panhandle: deeply "
            "dissected canyons, mesas, buttes, and draws carved by the Canadian River and its "
            "tributaries into the Ogallala Formation caprock. Relief from caprock rim to river "
            "bottom ranges from 400 to 800 ft, with near-vertical cliff faces, narrow box canyons, "
            "and isolated mesa tops. Vegetation is one-seed juniper and sand sagebrush on slopes, "
            "with mesquite and native grass on flats and mesas. The Canadian River itself is a "
            "broad, sandy-bottomed, intermittent river flanked by dense salt cedar and tamarisk. "
            "Lake Meredith, a Bureau of Reclamation impoundment of the Canadian River, provides "
            "water supply to 11 Panhandle cities but has experienced severe drought-related "
            "drawdowns. The Alibates Flint Quarries National Monument lies adjacent to the lake. "
            "Fritch is located within the area directly impacted by the 2024 Smokehouse Creek "
            "Fire, which originated approximately 10 miles north near Stinnett when a decayed "
            "Xcel Energy power pole fell into dry grass on February 26, 2024. The fire burned "
            "through the breaks terrain surrounding Fritch, destroying structures and threatening "
            "the town. Hutchinson County lost over 100 homes in the fire. The rugged terrain "
            "surrounding Fritch makes fire suppression extremely difficult: apparatus cannot "
            "access canyon bottoms, air support is complicated by turbulent canyon winds, and "
            "the juniper fuels produce intense, fast-spreading fires that spot across mesas. "
            "The community has limited evacuation routes, all requiring travel through the "
            "breaks terrain."
        ),
        "key_features": [
            {"name": "Lake Meredith NRA", "bearing": "N/E", "type": "reservoir/recreation",
             "notes": "Bureau of Reclamation reservoir on Canadian River; drought-prone; surrounded by breaks terrain; water supply for 11 cities"},
            {"name": "Canadian River Breaks", "bearing": "throughout", "type": "dissected_terrain",
             "notes": "400-800 ft deep canyons, mesas, buttes; juniper/sagebrush fuels; impassable terrain for fire apparatus"},
            {"name": "Alibates Flint Quarries NM", "bearing": "NE", "type": "national_monument",
             "notes": "NPS site; flint quarries used 12,000+ years; in breaks terrain subject to fire"},
            {"name": "Smokehouse Creek Fire origin", "bearing": "N (Stinnett area)", "type": "fire_origin",
             "notes": "10 mi N; downed Xcel Energy pole started 1,074,047-acre fire Feb 26, 2024; fire spread through breaks to Fritch area"},
        ],
        "elevation_range_ft": (2800, 3400),
        "wui_exposure": (
            "Extreme WUI exposure. Fritch is embedded in Canadian River Breaks with juniper fuels "
            "on all sides. Limited defensible space. Structures built on mesas and canyon rims. "
            "Sanford and other small communities similarly exposed. Lake Meredith recreational "
            "areas have seasonal visitor populations in fire-exposed settings."
        ),
        "historical_fires": [
            {"name": "Smokehouse Creek Fire", "year": 2024, "acres": 1074047,
             "structures_destroyed": 500, "fatalities": 2, "cause": "downed power line",
             "notes": "Over 100 homes destroyed in Hutchinson County alone; Fritch directly impacted; fire burned through surrounding breaks terrain; 83-year-old woman killed in Hutchinson County"},
            {"name": "Hutchinson County fires", "year": 2006, "acres": 30000,
             "structures_destroyed": 12, "fatalities": 0, "cause": "power line",
             "notes": "Part of East Amarillo Complex outbreak; burned breaks terrain around Lake Meredith; threatened Fritch and Sanford"},
            {"name": "Lake Meredith area fire", "year": 2017, "acres": 5000,
             "structures_destroyed": 2, "fatalities": 0, "cause": "unknown",
             "notes": "Burned in breaks terrain near lake; juniper fuels produced intense fire; NPS resources deployed"},
        ],
        "evacuation_routes": [
            {"route": "TX-136", "direction": "south toward Amarillo", "lanes": 2,
             "bottleneck": "Descends through breaks terrain; narrow road; single route south",
             "risk": "Passes through canyon terrain where fire spread is unpredictable; smoke fills canyons rapidly; sole high-capacity escape route"},
            {"route": "TX-687 (Sanford-Fritch Rd)", "direction": "west toward Sanford/Borger", "lanes": 2,
             "bottleneck": "2-lane through breaks; Canadian River crossing; Sanford is similarly threatened",
             "risk": "Route goes through same fire-exposed terrain; Sanford may also be evacuating"},
            {"route": "FM roads (east)", "direction": "east toward various", "lanes": 2,
             "bottleneck": "Narrow FM roads through breaks terrain; not designed for evacuation",
             "risk": "Remote, unpaved sections; dead-end ranch roads can trap evacuees; no services"},
        ],
        "fire_spread_characteristics": (
            "Extreme fire behavior in breaks terrain. Juniper torching produces 30-40 ft flame "
            "lengths and launches firebrands across canyon gaps (0.5-1 mile spotting). Canyon "
            "winds create erratic fire behavior with rapid direction changes. Fires can race up "
            "canyon slopes at twice the rate of flat-terrain fires. Mesa-top grass fires spread "
            "rapidly (5-10 mph) in post-frontal winds. Salt cedar along Canadian River burns with "
            "extreme intensity. Terrain prevents direct attack on most fire flanks."
        ),
        "infrastructure_vulnerabilities": (
            "Xcel Energy transmission crosses breaks terrain; proven fire ignition source (2024). "
            "Lake Meredith water supply critically drought-vulnerable. Small volunteer fire "
            "department with minimal apparatus. No hospital in Fritch; nearest is Borger (15 mi). "
            "Cell coverage gaps in canyon terrain. Propane storage for heating (no natural gas "
            "service) creates explosion risk. Roads through breaks terrain vulnerable to washout "
            "and fire closure simultaneously."
        ),
        "demographics_risk_factors": (
            "Population ~2,000 and declining. Aging, economically stressed community. Significant "
            "elderly population with limited mobility. Many residents dependent on propane heating "
            "with limited ability to evacuate quickly. Volunteer fire department struggles with "
            "recruitment. Post-2024 fire community experiencing economic and psychological stress. "
            "Seasonal lake visitors may be unfamiliar with fire risk and evacuation procedures."
        ),
    },

    # =========================================================================
    # 24. GRANBURY, TX — Hood County, WUI Growth Area
    # =========================================================================
    "granbury_tx": {
        "center": (32.4419, -97.7942),
        "terrain_notes": (
            "Granbury sits at approximately 722 ft elevation in Hood County on the Brazos River "
            "arm of Lake Granbury, 35 miles southwest of Fort Worth. The city is positioned in "
            "the Cross Timbers ecological region at the edge of the Dallas-Fort Worth metroplex's "
            "exurban growth zone, making it one of the fastest-growing WUI areas in Texas. The "
            "terrain is rolling to hilly, with post oak, blackjack oak, live oak, and eastern "
            "redcedar woodland on sandstone and limestone ridges, and mesquite/grass on clay "
            "soils in the valleys. Lake Granbury, an impoundment of the Brazos River, provides "
            "a 100-mile shoreline with extensive residential development in wooded settings. "
            "The Brazos River canyon upstream (toward Possum Kingdom) features steeper terrain "
            "with heavier fuel loads. Hood County has experienced rapid population growth, "
            "increasing from approximately 41,000 in 2000 to over 65,000 by 2025, with much "
            "of this growth in low-density, wooded settings that constitute high-risk WUI. "
            "The county experienced an 11,000+ acre wildfire that prompted evacuations and was "
            "only 20% contained at one point, demonstrating the fire hazard inherent in the "
            "Cross Timbers terrain. Eastern redcedar encroachment is dramatically increasing "
            "fuel loads throughout Hood County, converting formerly open grassland to continuous "
            "canopy fuel. The proximity to DFW means that Hood County's fire risk affects a "
            "population accustomed to urban services and largely unfamiliar with wildland fire "
            "behavior. The combination of rapid growth, Cross Timbers fuels, eastern redcedar "
            "encroachment, steep terrain, and a population unfamiliar with fire risk creates "
            "a growing WUI catastrophe potential comparable to the conditions that produced "
            "the 2011 Bastrop fire in a different fuel type."
        ),
        "key_features": [
            {"name": "Lake Granbury", "bearing": "through city", "type": "reservoir",
             "notes": "Brazos River impoundment; 100-mi shoreline; extensive WUI development in wooded settings"},
            {"name": "Cross Timbers woodland", "bearing": "throughout", "type": "woodland",
             "notes": "Post oak/blackjack/live oak/cedar; rolling terrain; heavy fuel loads; crown fire potential"},
            {"name": "Brazos River corridor", "bearing": "NW-SE", "type": "river",
             "notes": "Links upstream to PK Lake; canyon terrain upstream; riparian corridor fire potential"},
            {"name": "DFW exurban growth zone", "bearing": "NE", "type": "development",
             "notes": "35 mi SW of Fort Worth; rapid growth; commuter population unfamiliar with fire risk"},
            {"name": "Eastern redcedar invasion", "bearing": "throughout", "type": "vegetation_change",
             "notes": "Converting open rangeland to continuous canopy; dramatically increasing fire hazard annually"},
        ],
        "elevation_range_ft": (650, 1100),
        "wui_exposure": (
            "High and rapidly increasing WUI exposure. Rapid DFW exurban growth placing new "
            "homes in Cross Timbers woodland. Lakeside development in dense vegetation on "
            "steep slopes. Rural ranchettes on wooded acreages. Eastern redcedar encroachment "
            "increasing hazard at existing homes. Population unfamiliar with wildfire risk. "
            "Conditions analogous to pre-2011 Bastrop in some respects."
        ),
        "historical_fires": [
            {"name": "Hood County wildfire", "year": 2022, "acres": 11000,
             "structures_destroyed": 12, "fatalities": 0, "cause": "multiple",
             "notes": "11,000+ acres; only 20% contained at point; evacuations ordered; demonstrated scale of fire possible in Hood County Cross Timbers"},
            {"name": "Lake Granbury area fires", "year": 2011, "acres": 5000,
             "structures_destroyed": 8, "fatalities": 0, "cause": "unknown",
             "notes": "Part of 2011 Texas fire season; burned in Cross Timbers around lake; threatened lakeside homes"},
            {"name": "Brazos corridor fire", "year": 2018, "acres": 3000,
             "structures_destroyed": 4, "fatalities": 0, "cause": "welding",
             "notes": "Burned along Brazos River corridor NW of Granbury; steep terrain complicated suppression; threatened upstream lake homes"},
        ],
        "evacuation_routes": [
            {"route": "US-377", "direction": "NE toward Fort Worth / SW toward Stephenville", "lanes": 4,
             "bottleneck": "Granbury square area congestion; narrows to 2 lanes south of city",
             "risk": "Primary route to DFW; heavily traveled; passes through Cross Timbers; fire can close road segments"},
            {"route": "SH-144", "direction": "east toward Cleburne/I-35W", "lanes": 2,
             "bottleneck": "2-lane through rolling woodland; Lake Granbury crossing",
             "risk": "Alternative route to DFW; passes through dense Cross Timbers; limited capacity for mass evacuation"},
            {"route": "US-377/SH-51", "direction": "SW toward Stephenville", "lanes": 2,
             "bottleneck": "2-lane through fire-prone terrain; Erath County woodland",
             "risk": "Leads away from DFW but into more Cross Timbers fuel; not a safer direction"},
            {"route": "Lakeside subdivision roads", "direction": "various", "lanes": 2,
             "bottleneck": "Narrow roads serving lake developments; dead-ends at coves",
             "risk": "Many lakeside homes on narrow, dead-end roads through woodland; evacuation traps similar to Possum Kingdom"},
        ],
        "fire_spread_characteristics": (
            "Cross Timbers fuel complex with increasing eastern redcedar creates potential for "
            "intense crown fire. Rolling terrain with slopes accelerates fire. Cedar torching "
            "produces 20-35 ft flame lengths and spotting 0.5 mi+. Post oak/blackjack canopy "
            "supports sustained crown fire in extreme conditions. Lake and river corridors "
            "create wind channeling. Post-frontal NW winds of 35-50 mph drive fire across "
            "continuous woodland. Winter fire season overlaps with lower lake levels and "
            "maximum cured grass fuels."
        ),
        "infrastructure_vulnerabilities": (
            "Oncor transmission through Cross Timbers. Rural water districts serve much of "
            "county with limited fire flow. Lakeside homes on well water with no hydrants. "
            "Narrow subdivision roads prevent fire apparatus access. Hood County has grown "
            "faster than fire protection infrastructure. Single hospital (Lake Granbury Medical "
            "Center) limited capacity. DFW commuters create daytime population deficit for "
            "emergency response."
        ),
        "demographics_risk_factors": (
            "Population ~65,000 (county, growing rapidly). DFW exurban commuters unfamiliar "
            "with wildfire behavior and evacuation procedures. Retirees in lakeside communities "
            "with limited mobility. Rapid growth outpacing fire protection resources. Many new "
            "homes built without WUI fire codes. Volunteer fire departments serve most of county. "
            "Weekend/vacation homeowners may be absent during fire events."
        ),
    },

    # =========================================================================
    # 2. LUBBOCK, TX — Caprock Escarpment
    # =========================================================================
    "lubbock_tx": {
        "center": (33.577, -101.855),
        "terrain_notes": (
            "Lubbock sits at approximately 3,256 ft elevation on the southern Llano Estacado, the "
            "vast flat high plains of West Texas. The city is located roughly 30 miles west of the "
            "Caprock Escarpment, where the Llano Estacado drops 200-1,000 ft to the Rolling Plains "
            "below. This escarpment is a critical fire weather feature: fires ignited on the flat "
            "caprock can race eastward driven by post-frontal winds and accelerate dramatically as "
            "they reach the escarpment edge, where slope effects and turbulent winds increase intensity. "
            "The terrain around Lubbock is dominated by cotton agriculture and CRP grassland on deep "
            "sandy soils. Native vegetation includes sand shinnery oak, mesquite grassland, and "
            "shortgrass prairie. Playa lakes (ephemeral, clay-bottomed depressions) dot the landscape "
            "by the thousands, providing the only topographic variation on the otherwise featureless "
            "plain. Yellow House Canyon and Mackenzie Park provide limited riparian corridors through "
            "the city. The dryline frequently sets up along or west of Lubbock, creating an abrupt "
            "moisture boundary with dewpoint drops of 30-40F over just a few miles. When the dryline "
            "moves through, relative humidity crashes to single digits and winds gust 40-60 mph, "
            "creating critical fire weather. The 2022 fire season saw multiple large grass fires in "
            "Lubbock County, and the city's WUI has expanded significantly as subdivisions push into "
            "former cotton fields and mesquite rangeland. Lubbock is the largest city on the southern "
            "Llano Estacado with a metro population of approximately 320,000 and serves as the "
            "economic hub for a vast agricultural region. Texas Tech University adds 40,000+ students."
        ),
        "key_features": [
            {"name": "Caprock Escarpment", "bearing": "E", "type": "escarpment",
             "notes": "200-1000 ft drop from Llano Estacado to Rolling Plains; 30 mi east; fire acceleration zone; turbulent winds at edge"},
            {"name": "Yellow House Canyon", "bearing": "through city", "type": "canyon/drainage",
             "notes": "Shallow canyon bisecting city N-S; Mackenzie Park; cottonwood/mesquite riparian; headwaters of Brazos River fork"},
            {"name": "Playa lake system", "bearing": "throughout region", "type": "ephemeral_lakes",
             "notes": "Thousands of small clay-bottomed depressions; only topographic relief on caprock; seasonal wetlands; minor firebreaks when wet"},
            {"name": "Sand shinnery oak dunes", "bearing": "W/NW", "type": "dune_field",
             "notes": "Sandy terrain with dense shinnery oak; highly flammable when dormant; difficult suppression terrain"},
            {"name": "Buffalo Springs Lake", "bearing": "SE", "type": "reservoir",
             "notes": "Small reservoir in Yellow House Canyon; recreational area; WUI development around shores"},
        ],
        "elevation_range_ft": (3100, 3400),
        "wui_exposure": (
            "Expanding WUI on all city margins as development pushes into former agricultural land. "
            "South and southeast Lubbock growing fastest toward mesquite rangeland. Wolfforth, "
            "Shallowater, and Idalou satellite communities create scattered WUI pockets. Texas Tech "
            "campus and medical district on west side near open agricultural land."
        ),
        "historical_fires": [
            {"name": "Lubbock County grass fires", "year": 2022, "acres": 5000,
             "structures_destroyed": 3, "fatalities": 0, "cause": "multiple",
             "notes": "Multiple grass fires driven by March cold front winds; several structures threatened; demonstrated WUI exposure on city edges"},
            {"name": "FM 1585 Fire", "year": 2011, "acres": 8000,
             "structures_destroyed": 5, "fatalities": 0, "cause": "equipment",
             "notes": "Large grass fire south of Lubbock during exceptional 2011 drought; burned across cotton stubble and mesquite rangeland"},
            {"name": "Caprock Escarpment fires", "year": 2006, "acres": 15000,
             "structures_destroyed": 12, "fatalities": 0, "cause": "power lines",
             "notes": "Part of broader 2006 Panhandle fire outbreak; burned along escarpment east of Lubbock; terrain-enhanced spread"},
        ],
        "evacuation_routes": [
            {"route": "I-27/US-87", "direction": "north toward Amarillo", "lanes": 4,
             "bottleneck": "Marsha Sharp Freeway interchange; limited on-ramps north side",
             "risk": "Primary high-capacity route north; passes through open grassland susceptible to fire crossing"},
            {"route": "US-84", "direction": "southeast toward Post/Snyder", "lanes": 4,
             "bottleneck": "Descends Caprock Escarpment at Post; steep grades; single route SE",
             "risk": "Crosses Caprock Escarpment where fire behavior intensifies; limited shoulders; heavy truck traffic"},
            {"route": "US-62/82 (Marsha Sharp Fwy)", "direction": "east/west", "lanes": 4,
             "bottleneck": "Intersection with I-27 downtown; narrow through Idalou",
             "risk": "Flat open terrain both directions; fires can approach from any angle across cotton/grass fields"},
            {"route": "US-87 South", "direction": "south toward Lamesa/Big Spring", "lanes": 4,
             "bottleneck": "Tahoka bypass; 2-lane sections south of Tahoka",
             "risk": "Long distance to next population center; passes through continuous mesquite/grass rangeland"},
        ],
        "fire_spread_characteristics": (
            "Flat terrain allows unimpeded wind-driven fire spread in all directions. Continuous "
            "fine fuels (cured grass, cotton stubble, CRP land) support rapid rates of spread of "
            "5-15 mph in post-frontal winds. Dryline passages create abrupt transitions to extreme "
            "fire weather with single-digit RH. Mesquite and shinnery oak produce higher flame "
            "lengths and more resistant fuels than pure grass. Playa lakes provide minimal firebreaks "
            "only when holding water. Agricultural field patterns create minor fuel discontinuities "
            "but cotton stubble and weedy fallowed fields burn readily."
        ),
        "infrastructure_vulnerabilities": (
            "Lubbock Power & Light and South Plains Electric Cooperative transmission lines cross "
            "flat open terrain vulnerable to wind damage. Water supply depends on Ogallala Aquifer "
            "wells and Lake Alan Henry pipeline; aquifer levels declining steadily. Cotton gin fires "
            "during harvest season (Oct-Dec) can ignite surrounding fields. Natural gas gathering "
            "lines throughout oil/gas production areas. Texas Tech campus and UMC hospital complex "
            "require specialized evacuation planning."
        ),
        "demographics_risk_factors": (
            "Metro population ~320,000. Texas Tech University adds 40,000+ students unfamiliar with "
            "grass fire behavior. Significant agricultural workforce in surrounding counties with "
            "limited English proficiency. Large elderly population in rural communities (Idalou, "
            "Shallowater, Wolfforth). Mobile home parks on city periphery highly vulnerable to "
            "wind-driven fire approach. Regional medical center serves vast rural area."
        ),
    },

    # =========================================================================
    # 3. MIDLAND/ODESSA, TX — Permian Basin
    # =========================================================================
    "midland_odessa_tx": {
        "center": (31.997, -102.077),
        "terrain_notes": (
            "Midland and Odessa are twin cities in the heart of the Permian Basin, the most prolific "
            "oil-producing region in the United States, sitting at approximately 2,800-2,900 ft "
            "elevation on the southern margin of the Llano Estacado. The terrain is gently rolling "
            "to flat, with sand dunes and mesquite-dominated rangeland interspersed with thousands "
            "of active oil wells, tank batteries, pump jacks, and associated infrastructure. Monahans "
            "Sandhills, a 3,840-acre field of active sand dunes up to 70 ft tall, lies 30 miles west "
            "of Odessa and supports shin oak and havard oak that burn intensely when cured. The "
            "landscape is characterized by caliche soils, mesquite savanna, and creosote bush desert "
            "scrub transitioning to shortgrass prairie to the north. The Pecos River runs roughly "
            "50 miles to the west, marking the eastern edge of the Chihuahuan Desert. Fire risk in "
            "the Permian Basin is uniquely compounded by the dense oil and gas infrastructure: wellhead "
            "fires, pipeline ruptures, and tank battery explosions can ignite and accelerate wildland "
            "fires. During the exceptional 2011 drought, multiple large grass fires burned through "
            "oilfield areas, threatening production facilities and creating toxic smoke from burning "
            "petroleum equipment. The dryline frequently sets up in this area, and post-frontal winds "
            "regularly exceed 50 mph across the flat terrain. Midland-Odessa metro has approximately "
            "175,000 residents with significant transient oilfield worker population. The cities have "
            "experienced rapid growth since 2010 driven by the shale oil boom, with WUI development "
            "pushing into previously undeveloped mesquite rangeland in all directions."
        ),
        "key_features": [
            {"name": "Monahans Sandhills", "bearing": "W", "type": "dune_field",
             "notes": "3,840-acre active sand dunes to 70 ft; shin oak/havard oak fuels; state park; 30 mi W of Odessa"},
            {"name": "Permian Basin oilfield", "bearing": "throughout", "type": "industrial",
             "notes": "Thousands of active wells, tank batteries, pipelines; ignition sources and explosion risk during fires"},
            {"name": "Pecos River valley", "bearing": "W", "type": "river/valley",
             "notes": "50 mi west; marks Chihuahuan Desert transition; salt cedar/tamarisk riparian fuels; minor firebreak"},
            {"name": "University of Texas Permian Basin", "bearing": "NE Odessa", "type": "campus",
             "notes": "4,000+ students; campus surrounded by development and open rangeland"},
            {"name": "Midland Draw", "bearing": "through Midland", "type": "drainage",
             "notes": "Intermittent drainage through city; mesquite/salt cedar riparian; connects to larger playa system"},
        ],
        "elevation_range_ft": (2700, 3100),
        "wui_exposure": (
            "Rapidly expanding WUI on all margins driven by Permian Basin oil boom growth. New "
            "subdivisions in west Midland and south Odessa abut mesquite rangeland. Oilfield worker "
            "man-camps (temporary housing) in rural areas with no fire protection. Garden City and "
            "Stanton corridor experiencing growth."
        ),
        "historical_fires": [
            {"name": "Complex 7 Fire", "year": 2011, "acres": 12000,
             "structures_destroyed": 8, "fatalities": 0, "cause": "oilfield equipment",
             "notes": "Burned through active oilfield south of Midland during exceptional drought; tank batteries threatened; toxic smoke"},
            {"name": "Rankin Highway Fire", "year": 2018, "acres": 4500,
             "structures_destroyed": 2, "fatalities": 0, "cause": "vehicle",
             "notes": "Fast-moving grass fire south of Midland; threatened subdivisions; post-frontal winds drove rapid spread"},
            {"name": "Andrews County Complex", "year": 2022, "acres": 8000,
             "structures_destroyed": 0, "fatalities": 0, "cause": "power line",
             "notes": "Burned NW of Odessa through mesquite rangeland and oilfield areas; pipeline concerns forced precautionary shutdowns"},
        ],
        "evacuation_routes": [
            {"route": "I-20", "direction": "east toward Abilene / west toward Pecos", "lanes": 4,
             "bottleneck": "I-20/Loop 250 interchanges in both cities; heavy truck traffic",
             "risk": "Primary E-W corridor through Permian Basin; oilfield truck traffic creates congestion; flat terrain allows fire approach from any direction"},
            {"route": "TX-349", "direction": "south toward Rankin/I-10", "lanes": 2,
             "bottleneck": "2-lane highway through mesquite rangeland; no services for 50+ miles",
             "risk": "Limited capacity; remote; fires in mesquite rangeland can close road quickly"},
            {"route": "TX-158", "direction": "east toward Garden City/Sterling City", "lanes": 2,
             "bottleneck": "2-lane through open rangeland; long distances between towns",
             "risk": "Secondary route east; passes through continuous grass/mesquite fuels"},
            {"route": "US-385", "direction": "north toward Andrews/Seminole", "lanes": 2,
             "bottleneck": "Heavy oilfield traffic; 2-lane with limited passing zones",
             "risk": "Oilfield infrastructure along route creates additional hazards during fires"},
        ],
        "fire_spread_characteristics": (
            "Flat to gently rolling terrain allows rapid wind-driven fire spread. Mesquite rangeland "
            "produces higher flame lengths (8-15 ft) than pure grass, with volatile oils increasing "
            "fire intensity. Sand shinnery oak on sandy soils burns intensely and regenerates from "
            "roots. Oilfield infrastructure creates spot fire sources (wellhead fires, pipeline leaks) "
            "and complicates suppression. Post-frontal northwest winds of 40-60 mph drive grass fires "
            "at 5-10 mph rates of spread. The dryline frequently ignites in this area with afternoon "
            "RH dropping to 5-10%."
        ),
        "infrastructure_vulnerabilities": (
            "Dense oil/gas infrastructure creates cascading failure risk: wellhead fires, pipeline "
            "ruptures, tank battery explosions, and produced water pond contamination. Power lines "
            "serving oilfield (Oncor, TXU) cross open terrain. Water supply from T-Bar Ranch well "
            "field and Colorado River Municipal Water District pipeline; limited fire flow in "
            "outlying areas. Oilfield roads (caliche, unpaved) may be impassable for fire apparatus. "
            "Chemical storage at refineries and processing plants creates HAZMAT risk during fires."
        ),
        "demographics_risk_factors": (
            "Metro population ~175,000 with significant transient oilfield workforce. Man-camps and "
            "temporary housing in rural areas with no fire protection. Large Hispanic/Latino workforce "
            "(55%+) with potential language barriers. Boom-bust economy creates periods of rapid "
            "growth with insufficient infrastructure. Limited hospital capacity (Midland Memorial, "
            "Medical Center Hospital) for mass casualty events. High rates of uninsured workers."
        ),
    },

    # =========================================================================
    # 20. PERRYTON, TX — Lipscomb County, Panhandle Fire Corridor
    # =========================================================================
    "perryton_tx": {
        "center": (36.4000, -100.8028),
        "terrain_notes": (
            "Perryton sits at approximately 2,943 ft elevation on the flat high plains of the "
            "northern Texas Panhandle in Ochiltree County, just 12 miles south of the Oklahoma "
            "border. The terrain is among the flattest in the Panhandle, dominated by shortgrass "
            "prairie, CRP grassland, and irrigated wheat/corn agriculture on deep sandy loam soils "
            "overlying the Ogallala Aquifer. The landscape is remarkably featureless: no significant "
            "topographic relief for 30+ miles in any direction, creating unimpeded wind fetch that "
            "produces extreme fire weather conditions. Wolf Creek runs through the county from west "
            "to east, providing minor drainage relief with cottonwood/salt cedar riparian vegetation. "
            "The Perryton area lies in the heart of the Texas Panhandle fire corridor that has "
            "produced multiple catastrophic fires. The 2017 Perryton Fire burned 318,000 acres, "
            "making it the third-largest fire in Texas history at the time, spreading east across "
            "southern Lipscomb and northern Hemphill counties. The fire killed 7 people, injured 5, "
            "destroyed 87 structures, burned 1,500 miles of fencing, and killed 9,000-10,000 cattle. "
            "The fire started when an electric line blew down west of the Canadian River valley. "
            "Perryton also experienced a devastating EF-3 tornado in June 2023 that destroyed "
            "portions of the city, compounding the community's disaster vulnerability. Natural "
            "gas production and processing facilities are scattered throughout the area, creating "
            "additional fire hazards. The city population of approximately 8,700 makes it the "
            "largest community in Ochiltree County, serving as the commercial hub for the "
            "surrounding agricultural and energy production region."
        ),
        "key_features": [
            {"name": "Flat shortgrass prairie", "bearing": "throughout", "type": "grassland",
             "notes": "Featureless terrain; no topographic relief for 30+ mi; unimpeded wind fetch; extreme fire spread potential"},
            {"name": "Wolf Creek", "bearing": "E-W through county", "type": "creek",
             "notes": "Minor drainage; salt cedar riparian; minimal firebreak; connects to Beaver River in OK"},
            {"name": "Natural gas infrastructure", "bearing": "throughout", "type": "industrial",
             "notes": "Gas wells, processing plants, compressor stations, pipelines; ignition and explosion risk during fires"},
            {"name": "OK state line", "bearing": "N", "type": "border",
             "notes": "12 mi north; fires cross state line rapidly; Beaver County OK is source area for many fires"},
            {"name": "Canadian River breaks", "bearing": "SE", "type": "dissected_terrain",
             "notes": "30+ mi SE; breaks terrain where 2017 Perryton Fire accelerated; canyon fire behavior"},
        ],
        "elevation_range_ft": (2800, 3100),
        "wui_exposure": (
            "Moderate WUI with city surrounded by grassland and agricultural land. Perryton proper "
            "has some defensible space from irrigated fields but rural areas are fully exposed. "
            "Natural gas infrastructure scattered throughout county compounds fire risk. Post-2023 "
            "tornado rebuilding has improved some structures but community resources stretched thin."
        ),
        "historical_fires": [
            {"name": "Perryton Fire", "year": 2017, "acres": 318000,
             "structures_destroyed": 87, "fatalities": 7, "cause": "downed power line",
             "notes": "3rd largest TX fire at time; spread E across Lipscomb/Hemphill counties; 7 deaths, 5 injuries; 9,000-10,000 cattle killed; 1,500 mi fencing destroyed"},
            {"name": "Ochiltree County fire", "year": 2024, "acres": 15000,
             "structures_destroyed": 4, "fatalities": 0, "cause": "power line",
             "notes": "Part of Smokehouse Creek Fire outbreak; burned shortgrass prairie north of Perryton"},
            {"name": "Lipscomb County fire", "year": 2006, "acres": 10000,
             "structures_destroyed": 3, "fatalities": 0, "cause": "unknown",
             "notes": "Part of East Amarillo Complex era fires; burned grassland east of Perryton"},
        ],
        "evacuation_routes": [
            {"route": "US-83", "direction": "south toward Canadian / north toward OK", "lanes": 2,
             "bottleneck": "2-lane through flat prairie; Canadian River breaks south; OK border north",
             "risk": "Primary N-S route; fire can close at any point across flat terrain; leads through fire-prone landscape both directions"},
            {"route": "US-54", "direction": "NE toward Liberal KS / SW toward various", "lanes": 2,
             "bottleneck": "2-lane through open prairie; long distances between services",
             "risk": "Route into Kansas; crosses same fire corridor as Starbuck Fire; flat, continuous fuel"},
            {"route": "TX-15", "direction": "east toward Lipscomb/Higgins", "lanes": 2,
             "bottleneck": "2-lane through prairie; Lipscomb County roads narrow",
             "risk": "2017 Perryton Fire burned along this corridor; leads deeper into fire-prone region"},
        ],
        "fire_spread_characteristics": (
            "Extreme flat-terrain grass fire conditions. Shortgrass/CRP fuels cure to 95-100% by "
            "December. Post-frontal NW winds of 50-70 mph drive fire at 8-15 mph ROS across "
            "featureless terrain. No natural firebreaks for 30+ miles. Fires transition into "
            "breaks terrain to SE where canyon dynamics accelerate spread and create erratic "
            "behavior. The 2017 Perryton Fire killed 7 people, demonstrating that fire can "
            "outrun vehicles in this landscape. Dryline passages create additional extreme "
            "fire weather episodes."
        ),
        "infrastructure_vulnerabilities": (
            "Power lines across flat prairie are proven ignition source (2017 fire). Natural gas "
            "infrastructure creates explosion and toxic release risk. Water supply from Ogallala "
            "Aquifer wells; declining levels. Small regional hospital limited for mass casualty. "
            "Post-2023 tornado community still rebuilding. All routes are 2-lane highways with "
            "limited evacuation capacity. Cell coverage adequate in town but gaps in rural areas."
        ),
        "demographics_risk_factors": (
            "Population ~8,700. Community devastated by 2017 fire (7 deaths) and 2023 tornado. "
            "Compound disaster fatigue and PTSD. Significant Hispanic/Latino meatpacking workforce "
            "with language barriers. Aging ranching population in surrounding area. Limited mental "
            "health and social services. Volunteer fire departments serve rural areas with minimal "
            "equipment."
        ),
    },

    # =========================================================================
    # 23. POSSUM KINGDOM LAKE, TX — PK Complex 2011, Palo Pinto County
    # =========================================================================
    "possum_kingdom_tx": {
        "center": (32.8700, -98.4340),
        "terrain_notes": (
            "Possum Kingdom Lake sits at approximately 1,000 ft elevation in Palo Pinto County, "
            "in the rugged terrain where the Brazos River cuts through the Palo Pinto Mountains "
            "and the western edge of the Cross Timbers. The lake is a 17,000-acre reservoir "
            "created by Morris Sheppard Dam, with 310 miles of highly irregular shoreline featuring "
            "limestone cliffs, steep wooded slopes, and narrow coves. The terrain around the lake "
            "is the most rugged between Fort Worth and Abilene: the Palo Pinto Mountains (peaks "
            "to 1,500 ft) are dissected by the Brazos River and numerous tributaries into steep "
            "canyons, mesas, and rocky ridges covered with dense post oak, blackjack oak, live "
            "oak, eastern redcedar, and Ashe juniper. This terrain creates some of the most "
            "challenging fire suppression conditions in Texas: steep slopes accelerate fire, "
            "canyon winds are erratic, and the dense woodland fuels support intense crown fire. "
            "The 2011 PK Complex Fire burned 126,734 acres and destroyed 168 homes over 34 days, "
            "starting April 9 from a lightning strike. Ninety percent of Possum Kingdom State "
            "Park's 1,500 acres burned. A subsequent fire outbreak in August 2011 destroyed 39 "
            "more homes around the lake. By year's end, Palo Pinto County had lost 215 homes "
            "to wildfire. The lake is a major recreational destination with extensive residential "
            "development along the shoreline, much of it in dense woodland on steep slopes with "
            "single-lane access roads. The Hells Gate area, a narrow limestone passage between "
            "cliffs, is both an iconic swimming destination and a fire-weather wind tunnel. The "
            "combination of steep terrain, heavy fuel loads, recreational/residential development "
            "on dead-end roads, and extreme fire weather makes Possum Kingdom one of the highest "
            "WUI fire risk areas in the Southern Plains."
        ),
        "key_features": [
            {"name": "Possum Kingdom Lake", "bearing": "central", "type": "reservoir",
             "notes": "17,000-acre reservoir; 310 mi shoreline; steep wooded slopes; extensive WUI development on shores"},
            {"name": "Palo Pinto Mountains", "bearing": "throughout", "type": "mountains",
             "notes": "Peaks to 1,500 ft; rugged terrain; dense oak/juniper woodland; steep slopes accelerate fire"},
            {"name": "Hells Gate", "bearing": "NE portion of lake", "type": "geologic_feature",
             "notes": "Narrow limestone passage; 200+ ft cliffs; wind tunnel effect; iconic swimming area; fire funneling potential"},
            {"name": "Possum Kingdom State Park", "bearing": "S shore", "type": "state_park",
             "notes": "1,500 acres; 90% burned in 2011; CCC-era structures; recovering woodland; limited defensible space"},
            {"name": "Brazos River canyon", "bearing": "through area", "type": "river_canyon",
             "notes": "Deep canyon where Brazos is impounded; steep walls with juniper/oak; fire channeling corridor"},
        ],
        "elevation_range_ft": (850, 1500),
        "wui_exposure": (
            "Extreme WUI. Lakeside homes built on steep wooded slopes with single-lane access "
            "roads. Many properties accessible only by narrow roads through dense woodland. "
            "Possum Kingdom State Park and recreational areas in fire-exposed terrain. 215 homes "
            "lost in Palo Pinto County in 2011 demonstrates scale of WUI vulnerability. Post-fire "
            "rebuilding has improved some properties but fundamental terrain/access challenges persist."
        ),
        "historical_fires": [
            {"name": "PK Complex Fire", "year": 2011, "acres": 126734,
             "structures_destroyed": 168, "fatalities": 0, "cause": "lightning",
             "notes": "34-day fire; 168 homes destroyed; 90% of PK State Park burned; 600+ homes threatened at peak; extreme terrain-driven fire behavior"},
            {"name": "PK Lake August fires", "year": 2011, "acres": 15000,
             "structures_destroyed": 39, "fatalities": 0, "cause": "multiple",
             "notes": "Second 2011 fire outbreak around lake; 39 additional homes destroyed; Palo Pinto County total 215 homes lost in 2011"},
            {"name": "Palo Pinto County fire", "year": 2022, "acres": 500,
             "structures_destroyed": 4, "fatalities": 0, "cause": "welding",
             "notes": "Smaller fire near lake demonstrating continued vulnerability; steep terrain complicated suppression"},
        ],
        "evacuation_routes": [
            {"route": "US-180", "direction": "east toward Mineral Wells / west toward Breckenridge", "lanes": 2,
             "bottleneck": "Narrow through Palo Pinto Mountains; steep grades; 2-lane",
             "risk": "Primary E-W route but passes through heaviest fuel loads; fire can close road at multiple narrow points"},
            {"route": "SH-16", "direction": "south from Possum Kingdom to Strawn/I-20", "lanes": 2,
             "bottleneck": "2-lane through rugged terrain; Morris Sheppard Dam area narrow",
             "risk": "Steep, winding road through fire-prone terrain; sole southern escape from lake"},
            {"route": "Park Road 33", "direction": "to state park/south shore", "lanes": 2,
             "bottleneck": "Narrow park road; dead-end beyond state park; single entry/exit",
             "risk": "Dead-end road serving state park and south shore residences; fire can trap evacuees; 2011 fire burned along this road"},
            {"route": "Lakeside subdivision roads", "direction": "various", "lanes": 1,
             "bottleneck": "Single-lane, dead-end roads serving individual coves; no turnaround space",
             "risk": "Many lakeside homes accessible only by single-lane roads through dense woodland; no alternative escape; fire trap potential"},
        ],
        "fire_spread_characteristics": (
            "Steep terrain with heavy Cross Timbers/juniper fuel loads produces extreme fire "
            "behavior. Slope effects accelerate fire uphill at 2-4x flat-rate speeds. Canyon "
            "winds create erratic direction changes. Dense oak/juniper canopy supports crown "
            "fire with 30-50 ft flame lengths. Juniper torching and spotting 0.5-1 mi across "
            "canyons. The 2011 PK Complex demonstrated sustained extreme fire behavior over "
            "34 days in this terrain. Hells Gate and similar narrow passages create wind tunnel "
            "effects that accelerate fire. Lake surface creates wind channeling effects on "
            "surrounding slopes."
        ),
        "infrastructure_vulnerabilities": (
            "Oncor transmission through rugged terrain vulnerable to fire and wind damage. "
            "Rural water districts serve lakeside communities with limited fire flow; many "
            "homes on well water with no hydrants. Single-lane access roads prevent fire "
            "apparatus from reaching many properties. Morris Sheppard Dam is critical "
            "infrastructure (flood control, water supply, power generation). Cell coverage gaps "
            "in canyons. Propane storage for heating at many lakeside homes."
        ),
        "demographics_risk_factors": (
            "Permanent population modest but weekend/summer recreational population is much "
            "larger. Many homes are vacation/second homes with owners absent during fire events. "
            "Retirees in lakeside communities with limited mobility. Tourism economy dependent "
            "on lake access. 2011 fire destroyed significant portion of property tax base. "
            "Volunteer fire departments serve the area with limited apparatus for rugged terrain."
        ),
    },

    # =========================================================================
    # 4. SAN ANGELO, TX — Concho Valley
    # =========================================================================
    "san_angelo_tx": {
        "center": (31.4638, -100.4370),
        "terrain_notes": (
            "San Angelo sits at approximately 1,880 ft elevation in the Concho Valley of West-Central "
            "Texas, at the confluence of the North Concho River, South Concho River, and Spring Creek, "
            "which join to form the Concho River flowing east to the Colorado River. The city is "
            "positioned at the ecological transition zone between the Edwards Plateau to the south, "
            "the Rolling Plains to the north, and the Permian Basin mesquite country to the west. "
            "This creates a diverse fuel matrix: live oak/juniper savanna on limestone hills to the "
            "south and east, mesquite grassland on sandy soils to the north and west, and dense "
            "riparian corridors of pecan, cottonwood, and salt cedar along the river systems. O.C. "
            "Fisher Reservoir (dry since 2011 drought) and Twin Buttes Reservoir provide some "
            "terrain relief northwest and southwest of the city. The Concho Valley is one of the "
            "windiest regions in Texas, with sustained winds regularly exceeding 30 mph and gusts "
            "to 60+ mph during frontal passages. The terrain transitions from flat to gently rolling "
            "provide little obstruction to wind, and the mix of cured grass, mesquite, and juniper "
            "fuels creates a complex fire environment with high flame lengths and intense heat. "
            "Tom Green County has experienced multiple significant wildfire events, including a "
            "28,000-acre fire in 2011 that threatened the southwestern city limits. San Angelo's "
            "population of approximately 100,000 includes Goodfellow Air Force Base (3,200 personnel) "
            "and Angelo State University (10,000+ students). The city serves as the regional hub for "
            "a vast ranching area stretching across the Concho, Edwards Plateau, and Permian Basin."
        ),
        "key_features": [
            {"name": "Concho River confluence", "bearing": "through city", "type": "river",
             "notes": "North Concho, South Concho, and Spring Creek converge; dense pecan/cottonwood riparian; potential firebreak and corridor"},
            {"name": "Twin Buttes Reservoir", "bearing": "SW", "type": "reservoir",
             "notes": "Large reservoir SW of city; mesquite/juniper slopes around lake; WUI development on shores"},
            {"name": "O.C. Fisher Reservoir", "bearing": "NW", "type": "reservoir",
             "notes": "Largely dry since 2011 drought; exposed lake bed with colonizing vegetation; state park"},
            {"name": "Edwards Plateau escarpment", "bearing": "S/SE", "type": "escarpment",
             "notes": "Rolling limestone hills with live oak/juniper; terrain-enhanced fire spread; rugged suppression access"},
            {"name": "Goodfellow AFB", "bearing": "SE", "type": "military",
             "notes": "3,200+ personnel; jet fuel storage; ammunition; requires specialized evacuation planning"},
        ],
        "elevation_range_ft": (1750, 2200),
        "wui_exposure": (
            "Significant WUI exposure on south and west city margins where residential development "
            "meets mesquite/juniper rangeland. Lake Nasworthy and Twin Buttes lakeside homes embedded "
            "in dense brush. Rural ranchettes along FM roads with no municipal fire protection. "
            "Goodfellow AFB perimeter abuts open rangeland."
        ),
        "historical_fires": [
            {"name": "Tom Green County Fire", "year": 2011, "acres": 28000,
             "structures_destroyed": 15, "fatalities": 0, "cause": "equipment",
             "notes": "Burned to SW city limits during exceptional drought; threatened subdivisions near Twin Buttes; 100+ firefighters deployed"},
            {"name": "Wildcat Fire", "year": 2006, "acres": 12000,
             "structures_destroyed": 4, "fatalities": 0, "cause": "unknown",
             "notes": "Burned through mesquite rangeland north of San Angelo; post-frontal winds drove rapid spread"},
            {"name": "Concho Valley fires", "year": 2022, "acres": 6000,
             "structures_destroyed": 2, "fatalities": 0, "cause": "power line",
             "notes": "Multiple grass fires during March cold front passage; demonstrated continued vulnerability"},
        ],
        "evacuation_routes": [
            {"route": "US-87", "direction": "north toward Sterling City / south toward Mason", "lanes": 4,
             "bottleneck": "Loop 306 interchanges; narrows to 2 lanes outside city",
             "risk": "Primary N-S route; passes through open mesquite rangeland; long distances between services"},
            {"route": "US-67", "direction": "east toward Ballinger/Abilene", "lanes": 2,
             "bottleneck": "2-lane highway; crosses open rangeland for 60+ miles",
             "risk": "Rolling terrain limits visibility; fires can approach undetected from draws and valleys"},
            {"route": "US-277", "direction": "NW toward Bronte/Sweetwater", "lanes": 2,
             "bottleneck": "2-lane through ranch country; minimal services",
             "risk": "Remote route through fire-prone mesquite country; limited escape options if road is cut"},
        ],
        "fire_spread_characteristics": (
            "Complex fuel matrix creates variable fire behavior. Mesquite grassland supports rapid "
            "spread (3-8 mph) with high flame lengths (10-20 ft) in mesquite brush. Juniper/live oak "
            "on Edwards Plateau terrain burns with extreme intensity and resists suppression. Riparian "
            "salt cedar along rivers creates intense corridor fires. Post-frontal winds of 40-60 mph "
            "drive fire across all fuel types. The Concho Valley's position at the convergence of "
            "three ecological regions creates diverse and unpredictable fire behavior."
        ),
        "infrastructure_vulnerabilities": (
            "AEP Texas transmission crosses open rangeland; wind damage to lines is primary ignition "
            "source. Water supply from O.H. Ivie Reservoir (75 mi NE) via pipeline; drought "
            "vulnerability demonstrated in 2011 when O.C. Fisher went dry. Goodfellow AFB fuel and "
            "munitions storage requires evacuation buffer zones. Natural gas pipelines cross "
            "rangeland throughout region. Remote ranches dependent on volunteer fire departments "
            "with 30-60 minute response times."
        ),
        "demographics_risk_factors": (
            "Population ~100,000 with Goodfellow AFB (3,200) and Angelo State University (10,000+). "
            "Large retired military population with mobility limitations. Significant ranching "
            "community in surrounding counties requires livestock evacuation. Hispanic/Latino "
            "population (~43%) may face language barriers. Rural elderly population scattered across "
            "remote ranch properties with limited communication infrastructure."
        ),
    },

    # =========================================================================
    # 21. SHAMROCK/WHEELER, TX — I-40 Corridor, Panhandle Fires
    # =========================================================================
    "shamrock_tx": {
        "center": (35.2140, -100.2487),
        "terrain_notes": (
            "Shamrock sits at approximately 2,310 ft elevation in Wheeler County, at the junction "
            "of I-40 and US-83 in the eastern Texas Panhandle. The city lies on the historic Route "
            "66 corridor and serves as a critical transportation node where north-south and east-west "
            "routes intersect. The terrain is rolling mixed-grass prairie, transitioning from the "
            "flat high plains to the west to the more dissected Red River Rolling Plains to the "
            "east. The North Fork of the Red River flows through Wheeler County from west to east, "
            "cutting a moderate valley with sand sage, salt cedar, and cottonwood riparian vegetation. "
            "Sweetwater Creek, a major tributary, joins from the north. The vegetation is mixed-grass "
            "prairie with increasing mesquite density to the south and east, and some eastern "
            "redcedar encroachment on sandstone outcrops. Wheeler County has been repeatedly impacted "
            "by Panhandle wildfires: a 2016 fire outbreak burned at least 15,000 acres and shut "
            "down I-40 heading into Shamrock for hours. A 2018 Carbon Fire burned 7,000+ acres "
            "and crossed I-40 in Wheeler County. The 2024 Windy Deuce Fire burned approximately "
            "142,000 acres in the Shamrock/Wheeler area. The I-40 corridor through Wheeler County "
            "is particularly vulnerable to fire: the highway passes through continuous grass/mesquite "
            "fuels, and smoke from even moderate-sized fires can reduce visibility to zero, creating "
            "deadly driving conditions. Wheeler's population of approximately 1,600 and Shamrock's "
            "population of approximately 1,700 make these small communities with limited fire "
            "suppression resources. The combination of major interstate traffic, continuous fuels, "
            "extreme winds, and small community response capacity creates a significant risk for "
            "both residents and travelers."
        ),
        "key_features": [
            {"name": "I-40 corridor", "bearing": "E-W through area", "type": "interstate",
             "notes": "Major transcontinental route; carries heavy truck traffic; passes through continuous grass fuels; smoke visibility hazard"},
            {"name": "North Fork Red River", "bearing": "through county", "type": "river",
             "notes": "Moderate valley; sand sage/salt cedar riparian; minimal firebreak; Sweetwater Creek tributary joins from N"},
            {"name": "Route 66 heritage", "bearing": "through Shamrock", "type": "historic",
             "notes": "U-Drop Inn and other Route 66 landmarks; tourism draw; historic structures fire-vulnerable"},
            {"name": "Rolling mixed-grass prairie", "bearing": "throughout", "type": "grassland",
             "notes": "Mixed-grass with increasing mesquite; continuous fine fuels; 5-10 mph fire spread rates"},
        ],
        "elevation_range_ft": (2100, 2500),
        "wui_exposure": (
            "Moderate WUI with both communities surrounded by grass/mesquite rangeland. I-40 "
            "corridor creates linear WUI exposure for truck stops, motels, and highway businesses. "
            "Rural ranches throughout county. Wheeler's location on Sweetwater Creek has riparian "
            "corridor fire risk."
        ),
        "historical_fires": [
            {"name": "Windy Deuce Fire", "year": 2024, "acres": 142000,
             "structures_destroyed": 30, "fatalities": 0, "cause": "under investigation",
             "notes": "Part of 2024 Panhandle fire outbreak concurrent with Smokehouse Creek; 142,000 acres in Wheeler County area"},
            {"name": "Wheeler County fire outbreak", "year": 2016, "acres": 15000,
             "structures_destroyed": 8, "fatalities": 0, "cause": "multiple",
             "notes": "I-40 shut down heading into Shamrock for hours; 15,000+ acres burned; demonstrated I-40 vulnerability"},
            {"name": "Carbon Fire", "year": 2018, "acres": 7000,
             "structures_destroyed": 3, "fatalities": 0, "cause": "unknown",
             "notes": "Crossed I-40 in Wheeler County; 5% containment initially; TxDOT diverted traffic; demonstrated cross-interstate fire spread"},
        ],
        "evacuation_routes": [
            {"route": "I-40", "direction": "east toward Oklahoma / west toward Amarillo", "lanes": 4,
             "bottleneck": "US-83 interchange at Shamrock; rest areas between exits",
             "risk": "Primary evacuation route but frequently closed by fire smoke; fire has crossed I-40 multiple times; truck traffic compounds congestion"},
            {"route": "US-83", "direction": "north toward Canadian / south toward Childress", "lanes": 2,
             "bottleneck": "2-lane through rolling prairie; Wheeler town narrows",
             "risk": "N-S route through fire corridor; 2024 Windy Deuce Fire burned along this route; limited capacity"},
            {"route": "SH-152", "direction": "west toward Pampa", "lanes": 2,
             "bottleneck": "2-lane through open prairie; no services for 30+ miles",
             "risk": "Passes through continuous grass fuels; fire can close road at any point"},
        ],
        "fire_spread_characteristics": (
            "Rolling terrain with mixed-grass/mesquite fuels supports 5-10 mph rates of spread in "
            "post-frontal winds. Mesquite adds fuel loading and flame length (8-15 ft) compared to "
            "pure grass. Salt cedar along Red River tributaries burns intensely. I-40 is not an "
            "effective firebreak: fires have crossed the interstate multiple times. Post-frontal "
            "NW winds of 40-60 mph shift fire direction rapidly. The 2024 Windy Deuce Fire "
            "demonstrated extreme spread rates across 142,000 acres."
        ),
        "infrastructure_vulnerabilities": (
            "I-40 closure isolates communities and disrupts interstate commerce. Power lines "
            "across open terrain are ignition source. Small volunteer fire departments in Wheeler "
            "and Shamrock with limited apparatus. No hospital; nearest significant medical in "
            "Childress or Pampa (30+ mi). Water from municipal wells with limited fire flow. "
            "Motels, truck stops, and highway businesses along I-40 are fire-exposed. Cell "
            "coverage adequate on I-40 but limited off-highway."
        ),
        "demographics_risk_factors": (
            "Shamrock pop ~1,700; Wheeler pop ~1,600; both declining. Aging communities with "
            "limited resources. Transient I-40 traveler population may be trapped by fire/smoke "
            "on highway. Tourism (Route 66) brings visitors unfamiliar with fire risk. Rural "
            "ranching population scattered across county with limited evacuation options. "
            "Volunteer fire department recruitment challenged by declining population."
        ),
    },

    # =========================================================================
    # 6. WICHITA FALLS, TX
    # =========================================================================
    "wichita_falls_tx": {
        "center": (33.9137, -98.4934),
        "terrain_notes": (
            "Wichita Falls sits at approximately 946 ft elevation in the Red Rolling Plains of "
            "North-Central Texas, on the south bank of the Wichita River just 12 miles south of the "
            "Red River and the Oklahoma border. The terrain is gently rolling to hilly, with mesquite "
            "grassland on sandy and clay loam soils, scattered live oak mottes, and dense riparian "
            "corridors along the Wichita River and its tributaries (Holliday Creek, Beaver Creek). "
            "Lake Wichita and Lake Arrowhead provide reservoir-based terrain relief near the city. "
            "The Cross Timbers ecological region extends from east of the city, bringing denser "
            "woodland fuels (post oak, blackjack oak, eastern redcedar) that increase fire intensity "
            "compared to the pure grass/mesquite fuels to the west. Wichita Falls is positioned in "
            "a critical fire-weather corridor: cold fronts moving southeast across the Red River "
            "produce 40-60 mph post-frontal winds that push fires rapidly across flat to rolling "
            "terrain. The city experienced devastating fires in the 2005-2006 drought, and the "
            "surrounding area regularly sees winter grass fires exceeding 5,000 acres. Sheppard Air "
            "Force Base, one of the largest training installations in the Air Force, sits on the "
            "north side of the city with 4,000+ personnel. The metro population of approximately "
            "152,000 is declining but the WUI is expanding as rural subdivisions develop along "
            "lake shores and creek corridors. Eastern redcedar encroachment is dramatically "
            "increasing fuel loads on formerly open rangeland throughout Wichita and surrounding "
            "counties."
        ),
        "key_features": [
            {"name": "Wichita River", "bearing": "through city", "type": "river",
             "notes": "Primary drainage; riparian corridor of cottonwood/salt cedar; potential firebreak but also corridor fire risk"},
            {"name": "Red River", "bearing": "N", "type": "river/state_border",
             "notes": "12 mi north; TX-OK border; broad floodplain with salt cedar; fires can cross state line rapidly"},
            {"name": "Sheppard AFB", "bearing": "N", "type": "military",
             "notes": "Major Air Force training base; 4,000+ personnel; fuel storage; runway buffer zones"},
            {"name": "Lake Arrowhead", "bearing": "SE", "type": "reservoir",
             "notes": "Primary water supply; WUI development on shores; mesquite/juniper slopes; Clay County fire exposure"},
            {"name": "Cross Timbers transition", "bearing": "E", "type": "ecological_boundary",
             "notes": "Post oak/blackjack/redcedar woodland 15+ mi east; heavy fuel loads; cedar encroachment increasing fire risk"},
        ],
        "elevation_range_ft": (900, 1200),
        "wui_exposure": (
            "Moderate WUI on east and southeast city margins where development meets Cross Timbers "
            "woodland. Lake Arrowhead and Lake Kickapoo residential areas embedded in mesquite/juniper. "
            "Sheppard AFB northern perimeter borders open grassland. Iowa Park and Burkburnett "
            "satellite communities in fire-prone corridors."
        ),
        "historical_fires": [
            {"name": "Wichita County Complex", "year": 2006, "acres": 14000,
             "structures_destroyed": 8, "fatalities": 0, "cause": "power line",
             "notes": "Part of 2006 Panhandle/Rolling Plains fire outbreak; burned mesquite grassland west and south of city"},
            {"name": "Clay County Fire", "year": 2011, "acres": 22000,
             "structures_destroyed": 18, "fatalities": 0, "cause": "equipment",
             "notes": "Large fire east of Wichita Falls in Cross Timbers transition; demonstrated heavy fuel loads; multiple structures lost"},
            {"name": "Iowa Park area fires", "year": 2022, "acres": 3000,
             "structures_destroyed": 2, "fatalities": 0, "cause": "unknown",
             "notes": "Grass fires west of city during March cold front; threatened Iowa Park community"},
        ],
        "evacuation_routes": [
            {"route": "I-44", "direction": "NE toward Lawton, OK", "lanes": 4,
             "bottleneck": "Red River bridge crossing; Burkburnett narrows",
             "risk": "Crosses Red River floodplain with salt cedar fuels; fires can close bridge approaches; only Interstate route"},
            {"route": "US-287", "direction": "SE toward Fort Worth / NW toward Vernon", "lanes": 4,
             "bottleneck": "Kell Blvd interchange; Iowa Park congestion",
             "risk": "Primary route to DFW; 150 mi through fire-prone rangeland; smoke visibility hazard common"},
            {"route": "US-281", "direction": "south toward Jacksboro/Mineral Wells", "lanes": 2,
             "bottleneck": "2-lane through Cross Timbers; narrow bridges",
             "risk": "Passes through heavy woodland fuels in Jack and Young Counties; limited passing zones"},
        ],
        "fire_spread_characteristics": (
            "Rolling terrain with mixed fuel types creates variable fire behavior. Grass/mesquite "
            "fuels to the west support 5-10 mph rates of spread in post-frontal winds. Cross Timbers "
            "woodland to the east produces higher intensity fires with crown fire potential in "
            "redcedar stands. Eastern redcedar encroachment is converting open rangeland to heavy "
            "fuel loads, dramatically increasing fire potential. Red River corridor fires can cross "
            "the state line rapidly. Cold front passages produce the most dangerous conditions with "
            "40-60 mph gusts shifting NW."
        ),
        "infrastructure_vulnerabilities": (
            "Oncor transmission lines cross open terrain; wind damage is primary ignition source. "
            "Sheppard AFB requires specialized fire protection for flight line operations, fuel "
            "storage, and training exercises. Water supply from Lake Arrowhead and Lake Kickapoo "
            "via pipeline; drought vulnerability significant. Regional hospital (United Regional) "
            "serves large rural area. Railroad corridors through city carry hazardous materials."
        ),
        "demographics_risk_factors": (
            "Metro population ~152,000 (declining). Sheppard AFB international training mission "
            "includes allied nation personnel. Aging population with 16%+ over 65. Iowa Park and "
            "Burkburnett satellite communities rely on volunteer fire departments. Significant "
            "mobile home population on city periphery. Rural elderly on isolated ranch properties."
        ),
    },

    # =========================================================================
    # OKLAHOMA (6 cities)
    # =========================================================================

    # =========================================================================
    # 14. GUTHRIE, OK
    # =========================================================================
    "guthrie_ok": {
        "center": (35.8789, -97.4253),
        "terrain_notes": (
            "Guthrie sits at approximately 1,010 ft elevation in central Oklahoma, on the Cimarron "
            "River at the transition between the mixed-grass prairie to the west and the Cross "
            "Timbers woodland to the east. The city was Oklahoma's first state capital and preserves "
            "one of the largest contiguous districts of Victorian-era commercial architecture in the "
            "United States, with 2,169 buildings listed in the National Historic District. The "
            "terrain is gently rolling, with the Cimarron River cutting a broad valley through "
            "red-bed sandstone and shale. Vegetation transitions sharply from open grassland west "
            "of the city to increasingly dense post oak, blackjack oak, and eastern redcedar woodland "
            "to the east and southeast. Cottonwood Creek and other tributaries create riparian "
            "corridors through the area. Logan County has experienced significant eastern redcedar "
            "encroachment over the past several decades, converting formerly open prairie to dense "
            "cedar woodland with continuous canopy fuel. This creates increasing wildfire risk as "
            "the fuel type shifts from grass (surface fire) to cedar (crown fire). The Red Fork of "
            "the Cimarron River provides some terrain relief but salt cedar infestation reduces "
            "its firebreak value. Guthrie is located 30 miles north of Oklahoma City on I-35, "
            "and the corridor between the two cities is experiencing rapid suburban development "
            "in fire-prone Cross Timbers transition zone. Langston University, Oklahoma's only "
            "historically Black university, is located 10 miles east of Guthrie in dense Cross "
            "Timbers woodland. The city population of approximately 11,500 includes significant "
            "retirement and agricultural community."
        ),
        "key_features": [
            {"name": "Cimarron River", "bearing": "through area", "type": "river",
             "notes": "Major drainage; broad sandy floodplain; salt cedar infestation; limited firebreak value"},
            {"name": "National Historic District", "bearing": "downtown", "type": "historic",
             "notes": "2,169 Victorian-era buildings; irreplaceable cultural resource; older construction fire-vulnerable"},
            {"name": "Cross Timbers transition", "bearing": "E/SE", "type": "ecological_boundary",
             "notes": "Dense post oak/blackjack/redcedar east of city; fuel loads increasing with cedar encroachment"},
            {"name": "Langston University", "bearing": "E", "type": "university",
             "notes": "10 mi E in Cross Timbers; HBCU; ~2,200 students; fire-exposed campus in woodland setting"},
        ],
        "elevation_range_ft": (950, 1150),
        "wui_exposure": (
            "Moderate-high WUI on east and southeast margins where development meets Cross Timbers. "
            "Langston/Coyle communities in woodland. Historic downtown with older construction. "
            "I-35 corridor south toward Edmond experiencing rapid growth in transition zone. "
            "Eastern redcedar encroachment increasing fuel loads annually."
        ),
        "historical_fires": [
            {"name": "Logan County fires", "year": 2023, "acres": 4000,
             "structures_destroyed": 8, "fatalities": 0, "cause": "power line",
             "notes": "Burned in Cross Timbers east of Guthrie; redcedar crown fire; evacuations at Langston"},
            {"name": "Cimarron corridor fire", "year": 2011, "acres": 6000,
             "structures_destroyed": 5, "fatalities": 0, "cause": "unknown",
             "notes": "Burned along Cimarron River salt cedar corridor; spread into adjacent grassland and Cross Timbers"},
            {"name": "Mulhall area fire", "year": 2016, "acres": 3500,
             "structures_destroyed": 2, "fatalities": 0, "cause": "prescribed burn escape",
             "notes": "Escaped prescribed burn NW of Guthrie; demonstrated rapid grass fire spread; threatened rural homes"},
        ],
        "evacuation_routes": [
            {"route": "I-35", "direction": "south toward OKC / north toward Ponca City", "lanes": 4,
             "bottleneck": "Guthrie exits; merge with US-77; Seward Road interchange",
             "risk": "Primary escape route; high capacity but crosses fire-prone corridor; grass fires can approach from west"},
            {"route": "US-77", "direction": "south toward Edmond / north toward Perry", "lanes": 2,
             "bottleneck": "2-lane through Cross Timbers transition; Langston area narrows",
             "risk": "Passes through cedar-encroached areas east of I-35; fire can close road"},
            {"route": "SH-33", "direction": "east toward Cushing / west toward Kingfisher", "lanes": 2,
             "bottleneck": "2-lane; Cimarron River bridge; narrow through Cross Timbers east",
             "risk": "East route goes deeper into Cross Timbers; west route crosses open prairie"},
        ],
        "fire_spread_characteristics": (
            "Transition zone creates dual fire behavior: grass fires on western prairie (5-10 mph "
            "ROS) and Cross Timbers woodland fires to the east (2-5 mph ROS but extreme intensity). "
            "Eastern redcedar encroachment is rapidly converting grass fire regime to crown fire "
            "regime. Cedar torching launches firebrands 0.5-1 mi ahead of main front. Salt cedar "
            "along Cimarron burns with extreme intensity, creating corridor fire potential through "
            "the metro area. Post-frontal NW winds of 35-50 mph are the primary driver."
        ),
        "infrastructure_vulnerabilities": (
            "OG&E transmission through Cross Timbers transition zone. Historic downtown Victorian "
            "buildings are irreplaceable and highly combustible (wood frame, shared walls). "
            "Municipal water system adequate for city but rural areas on well/cistern. Langston "
            "University campus requires specialized evacuation planning. Cell coverage limited "
            "in Cross Timbers east of city."
        ),
        "demographics_risk_factors": (
            "Population ~11,500. Significant tourism-dependent economy (Victorian architecture, "
            "Lazy E Arena). Langston University adds ~2,200 students. Aging population with "
            "15%+ over 65. Rural communities east of city (Langston, Coyle) with limited "
            "resources. Historic district businesses have limited fire insurance options. "
            "I-35 corridor growth bringing new residents unfamiliar with wildfire risk."
        ),
    },

    # =========================================================================
    # 25. NEWALLA/HARRAH, OK — E Oklahoma City WUI, 2024 Fires
    # =========================================================================
    "newalla_ok": {
        "center": (35.3880, -97.1720),
        "terrain_notes": (
            "Newalla and Harrah are adjacent communities on the southeastern fringe of the Oklahoma "
            "City metropolitan area, sitting at approximately 1,100-1,200 ft elevation in the Cross "
            "Timbers ecological region of Oklahoma County and Pottawatomie County. The terrain is "
            "rolling to hilly, with deeply weathered sandstone creating ridges and valleys covered "
            "by dense post oak, blackjack oak, and aggressive eastern redcedar. The area represents "
            "the classic Oklahoma WUI problem: rural and semi-rural residential development spreading "
            "into Cross Timbers woodland, with homes built on wooded acreages accessed by narrow, "
            "dead-end roads. Harrah Road (SE 59th) serves as the primary north-south corridor, "
            "connecting these communities to the Oklahoma City metro, but it passes through the same "
            "woodland that presents the fire hazard. The North Canadian River runs north of the area, "
            "while smaller tributaries (Elm Creek, Little River) cut shallow valleys through the "
            "Cross Timbers. Eastern redcedar encroachment is the critical fire hazard trend: cedar "
            "has invaded post oak woodland and open grassland throughout the area, creating "
            "continuous canopy fuel where previously only grass fires occurred. Oklahoma State "
            "University research indicates that fire intensity increases dramatically in cedar-"
            "encroached Cross Timbers, with greater flame heights, increased fire intensity, and "
            "more erratic fire behavior. The Newalla area experienced multiple fire events in "
            "2024, with homes destroyed and evacuations ordered. The combination of expanding "
            "residential development, increasing cedar fuel loads, limited road access, and "
            "volunteer fire department coverage creates a high-risk WUI scenario that is "
            "replicating across the entire eastern OKC metro fringe. Population in the Newalla/"
            "Harrah area is approximately 15,000 and growing as OKC metro expansion pushes east."
        ),
        "key_features": [
            {"name": "Cross Timbers woodland", "bearing": "throughout", "type": "woodland",
             "notes": "Dense post oak/blackjack/redcedar; heavy fuel loads; crown fire potential; extends E into Pottawatomie County"},
            {"name": "Eastern redcedar invasion", "bearing": "throughout", "type": "vegetation_change",
             "notes": "OSU research shows fire intensity increases dramatically; converting grass to canopy fuel; primary hazard driver"},
            {"name": "Harrah Road corridor", "bearing": "N-S", "type": "road/WUI_corridor",
             "notes": "Primary access road; passes through woodland; connects to OKC metro; evacuation bottleneck"},
            {"name": "Elm Creek drainage", "bearing": "through area", "type": "creek",
             "notes": "Tributary of North Canadian; shallow valley with riparian woodland; fire channeling potential"},
            {"name": "OKC metro fringe", "bearing": "W/NW", "type": "development_boundary",
             "notes": "Rapidly expanding eastern metro edge; new homes in woodland; population unfamiliar with fire risk"},
        ],
        "elevation_range_ft": (1050, 1250),
        "wui_exposure": (
            "High and rapidly increasing WUI. Residential development in Cross Timbers woodland "
            "with homes on 2-10 acre wooded lots accessed by narrow roads. Many dead-end "
            "subdivision roads. Volunteer fire department coverage. Eastern redcedar increasing "
            "fuel loads continuously. 2024 fires destroyed homes, demonstrating current "
            "vulnerability."
        ),
        "historical_fires": [
            {"name": "Newalla/Luther fires", "year": 2024, "acres": 3000,
             "structures_destroyed": 12, "fatalities": 0, "cause": "power line",
             "notes": "Multiple fires in eastern OKC metro; homes destroyed in Newalla/Harrah area; Cross Timbers/redcedar fuels; evacuations ordered"},
            {"name": "Harrah area fires", "year": 2023, "acres": 2000,
             "structures_destroyed": 6, "fatalities": 0, "cause": "unknown",
             "notes": "Grass/cedar fire; rapid spread in redcedar stands; threatened subdivisions; demonstrated WUI growth impact"},
            {"name": "Eastern OKC metro fires", "year": 2011, "acres": 5000,
             "structures_destroyed": 15, "fatalities": 0, "cause": "multiple",
             "notes": "Part of 2011 drought fires; Cross Timbers fuels; multiple structures destroyed in eastern Oklahoma County"},
        ],
        "evacuation_routes": [
            {"route": "SE 59th/Harrah Road", "direction": "north to OKC / south to various", "lanes": 2,
             "bottleneck": "2-lane through woodland; dead-end subdivisions feed onto single road; Harrah intersection congested",
             "risk": "Primary route to OKC but passes through same woodland that burns; can be overwhelmed by subdivision evacuation"},
            {"route": "SH-270/Indian Meridian Rd", "direction": "NE toward Shawnee", "lanes": 2,
             "bottleneck": "2-lane; Pottawatomie County line; limited interchanges",
             "risk": "Alternative E escape but goes deeper into Cross Timbers; fire can close at multiple points"},
            {"route": "SE 44th / Peebly Road", "direction": "west to Choctaw/OKC", "lanes": 2,
             "bottleneck": "Narrow E-W routes through woodland; residential congestion",
             "risk": "Local routes to western safety but narrow, winding, and through fire-prone areas"},
        ],
        "fire_spread_characteristics": (
            "Eastern redcedar encroachment is transforming fire behavior from grass fire regime "
            "to woodland crown fire regime. Cedar torching produces 20-35 ft flame lengths with "
            "spotting 0.5+ mi ahead of main front. Post oak/blackjack canopy supports crown fire "
            "in extreme wind events. Winter dormancy increases grass and leaf litter fuel loads "
            "while cedar remains green and volatile. Post-frontal NW winds of 35-50 mph drive "
            "fire through continuous woodland. Narrow road corridors create fire tunnels. "
            "Rate of spread 2-5 mph in woodland, 5-10 mph in grass/cedar transition."
        ),
        "infrastructure_vulnerabilities": (
            "OG&E lines through Cross Timbers; ignition source and vulnerable to fire damage. "
            "Rural Water District #3 serves area with limited fire flow; many homes on wells. "
            "Narrow, dead-end subdivision roads prevent fire apparatus access and create "
            "evacuation traps. Newalla Volunteer Fire Department has limited apparatus for "
            "woodland fires. Cell coverage adequate but emergency notification systems may "
            "not reach all residents. No hospital in area; nearest in OKC (20+ mi)."
        ),
        "demographics_risk_factors": (
            "Population ~15,000 (Newalla/Harrah area, growing). OKC metro transplants unfamiliar "
            "with wildfire risk. Many homes built without WUI fire codes on wooded lots. Volunteer "
            "fire department serves area with limited resources. Mix of incomes: higher-income "
            "ranchettes and lower-income mobile homes both fire-exposed. Growing school-age "
            "population (Harrah schools) creates daytime evacuation challenges. Rural water "
            "districts unable to support fire flow for structure defense."
        ),
    },

    # =========================================================================
    # 26. NORMAN/MOORE, OK — Cross Timbers South OKC
    # =========================================================================
    "norman_ok": {
        "center": (35.2226, -97.4395),
        "terrain_notes": (
            "Norman sits at approximately 1,171 ft elevation in Cleveland County, 20 miles south "
            "of downtown Oklahoma City, along the Canadian River which forms the city's northern "
            "boundary. The terrain transitions from flat to gently rolling, with the city positioned "
            "at the ecological transition between the mixed-grass prairie to the west and the Cross "
            "Timbers woodland extending east and southeast. The Canadian River floodplain is broad "
            "and sandy, heavily infested with salt cedar and eastern redcedar, creating an intense "
            "fire corridor along the northern edge of the city. Lake Thunderbird State Park "
            "(6,070 acres including 5,550 of parkland) lies 8 miles east of the city, surrounded "
            "by dense Cross Timbers woodland that extends southeast toward the South Canadian River. "
            "Norman is best known as the home of the University of Oklahoma (30,000+ students) and "
            "the National Weather Center (NOAA/NWS Storm Prediction Center, NSSL). Moore, directly "
            "north, is a city of 62,000 that sits between Norman and OKC proper. The Canadian River "
            "separates Moore from OKC to the north. Eastern redcedar encroachment is progressively "
            "converting open grassland and post oak savanna to dense cedar woodland throughout the "
            "area, particularly in the Lake Thunderbird watershed and the Canadian River corridor. "
            "The Norman/Moore area experiences the same winter fire regime as the broader Southern "
            "Plains, with post-frontal cold front winds and low humidity across cured grass and "
            "dormant woodland. Cleveland County has recorded multiple grass fires exceeding 1,000 "
            "acres in recent fire seasons. The combination of large university population, rapid "
            "suburban growth, Cross Timbers transition, and Canadian River fire corridor creates "
            "a significant and growing wildfire risk for a metro-area population of approximately "
            "180,000 (Norman/Moore combined) that is primarily focused on tornado preparedness "
            "and largely unaware of wildfire hazard."
        ),
        "key_features": [
            {"name": "Canadian River corridor", "bearing": "N", "type": "river/fire_corridor",
             "notes": "Broad sandy floodplain; dense salt cedar/redcedar; fire corridor along Norman/Moore northern boundary"},
            {"name": "Lake Thunderbird", "bearing": "E", "type": "reservoir/state_park",
             "notes": "6,070-acre park; Cross Timbers woodland; residential development W and S shores; fire-exposed recreation area"},
            {"name": "University of Oklahoma", "bearing": "central Norman", "type": "university",
             "notes": "30,000+ students; large campus; game day crowds 80,000+; specialized evacuation needs"},
            {"name": "National Weather Center", "bearing": "OU campus", "type": "federal_facility",
             "notes": "SPC, NSSL, NWS offices; critical national weather forecasting infrastructure; ironic fire exposure"},
            {"name": "Cross Timbers transition", "bearing": "E/SE", "type": "ecological_boundary",
             "notes": "Post oak/blackjack/redcedar woodland increasing E of I-35; cedar encroachment expanding hazard zone"},
        ],
        "elevation_range_ft": (1050, 1300),
        "wui_exposure": (
            "Moderate WUI concentrated in three areas: Canadian River corridor along northern "
            "boundary (salt cedar fire threat), Lake Thunderbird area to east (Cross Timbers "
            "woodland), and expanding development south and east of city in transition zone. "
            "Moore faces Canadian River fire corridor on both north and south sides. Eastern "
            "redcedar encroachment expanding hazard zone."
        ),
        "historical_fires": [
            {"name": "Canadian River grass fires", "year": 2023, "acres": 2500,
             "structures_destroyed": 3, "fatalities": 0, "cause": "unknown",
             "notes": "Salt cedar/grass fire along Canadian River; smoke drifted over Norman/Moore; demonstrated river corridor fire hazard"},
            {"name": "Cleveland County fires", "year": 2011, "acres": 4000,
             "structures_destroyed": 5, "fatalities": 0, "cause": "multiple",
             "notes": "Multiple grass fires during exceptional drought; burned E of Norman in Cross Timbers transition; evacuations ordered"},
            {"name": "Lake Thunderbird area fire", "year": 2016, "acres": 1500,
             "structures_destroyed": 2, "fatalities": 0, "cause": "campfire",
             "notes": "Burned in Cross Timbers near state park; threatened lakeside development; cedar fuels produced intense fire"},
        ],
        "evacuation_routes": [
            {"route": "I-35", "direction": "north to OKC / south to Pauls Valley", "lanes": 6,
             "bottleneck": "I-35/SH-9 interchange; Indian Hills Rd; chronically congested through Moore",
             "risk": "Primary N-S escape; very high capacity but chronically congested; Canadian River bridges could be smoke-affected"},
            {"route": "SH-9", "direction": "east toward Tecumseh / west toward Tuttle", "lanes": 4,
             "bottleneck": "SH-9/I-35 interchange; narrows to 2 lanes east of city",
             "risk": "Primary E-W route; east leads into Cross Timbers; west crosses open prairie"},
            {"route": "US-77", "direction": "south toward Purcell/Davis", "lanes": 4,
             "bottleneck": "South Canadian River bridge; Purcell interchange",
             "risk": "Alternative to I-35 south; crosses Canadian River corridor; largely open terrain"},
            {"route": "SH-77H/Lindsay", "direction": "SE through Noble", "lanes": 2,
             "bottleneck": "2-lane through Cross Timbers transition; Noble congestion",
             "risk": "Passes through fire-prone woodland transition; limited capacity"},
        ],
        "fire_spread_characteristics": (
            "Dual fire regime. Canadian River corridor supports intense salt cedar/grass fires "
            "with 10-20 ft flame lengths; fire can race along river corridor for miles. Cross "
            "Timbers to east supports woodland fire with cedar crown fire potential (20-35 ft "
            "flame lengths). Prairie to west supports rapid grass fire spread (5-10 mph). "
            "Post-frontal NW winds of 35-50 mph drive fire across all fuel types. Winter fire "
            "season (Nov-Mar) with cured grass at 90-100%. Cedar remains volatile year-round. "
            "Canadian River corridor fires can produce thick smoke over Norman/Moore."
        ),
        "infrastructure_vulnerabilities": (
            "OG&E transmission through Cross Timbers and river corridor. University of Oklahoma "
            "campus (30,000+ students) requires specialized evacuation. National Weather Center "
            "houses SPC and NSSL critical operations. Norman Regional Hospital limited for mass "
            "casualty. Moore and Norman both focused on tornado shelter infrastructure rather than "
            "fire evacuation. Canadian River bridges on I-35 and US-77 are critical chokepoints."
        ),
        "demographics_risk_factors": (
            "Norman pop ~130,000; Moore pop ~62,000. OU adds 30,000+ students; game days 80,000+. "
            "Population focused on tornado preparedness; largely unaware of wildfire risk. Rapid "
            "growth east and south of Norman into Cross Timbers transition. Student population "
            "unfamiliar with fire behavior. International student/researcher population at "
            "OU/NWC may face language barriers. Retirement communities near Lake Thunderbird."
        ),
    },

    # =========================================================================
    # 12. OKLAHOMA CITY, OK — Newalla/Cross Timbers
    # =========================================================================
    "oklahoma_city_ok": {
        "center": (35.4676, -97.5164),
        "terrain_notes": (
            "Oklahoma City sits at approximately 1,200 ft elevation in Central Oklahoma, straddling "
            "the ecological boundary between the mixed-grass prairie to the west and the Cross Timbers "
            "woodland to the east. The city covers 621 square miles, making it one of the largest "
            "cities by area in the United States, with extensive low-density development that creates "
            "a vast wildland-urban interface on the eastern margins. The Cross Timbers in eastern "
            "Oklahoma County and Pottawatomie County consists of dense post oak and blackjack oak "
            "woodland with aggressive eastern redcedar encroachment, creating heavy fuel loads. "
            "The terrain becomes rolling to hilly east of I-35, with the Newalla and Harrah areas "
            "experiencing significant residential development in and around Cross Timbers woodland. "
            "The North Canadian River (Oklahoma River through downtown) and the Canadian River to "
            "the south provide major drainages, but riparian corridors are heavily infested with "
            "salt cedar and eastern redcedar, acting more as fire corridors than firebreaks. Lake "
            "Draper, Lake Thunderbird, and Lake Stanley Draper lie in the eastern metro, surrounded "
            "by woodland. The Newalla and east OKC WUI has experienced multiple fire events, with "
            "2024 bringing fires that destroyed homes in the area. Eastern redcedar encroachment "
            "is the primary fire hazard intensifier: cedar converts open grassland to continuous "
            "canopy fuel, creating crown fire potential where previously only grass fires occurred. "
            "OKC metro population of approximately 1.4 million makes it the largest metro in the "
            "Southern Plains, with evacuation challenges concentrated in the eastern WUI where "
            "narrow, dead-end subdivision roads serve low-density development in woodland settings."
        ),
        "key_features": [
            {"name": "Cross Timbers woodland", "bearing": "E", "type": "woodland",
             "notes": "Dense post oak/blackjack/redcedar east of I-35; heavy fuel loads; crown fire potential; extends into Pottawatomie County"},
            {"name": "Newalla/Harrah WUI", "bearing": "E/SE", "type": "WUI_zone",
             "notes": "Rapid residential growth in woodland; narrow roads; limited fire protection; 2024 fire damage"},
            {"name": "Lake Thunderbird", "bearing": "SE", "type": "reservoir",
             "notes": "State park; surrounded by Cross Timbers; WUI development on west and south shores"},
            {"name": "North Canadian River", "bearing": "through city", "type": "river",
             "notes": "Major drainage; salt cedar/redcedar riparian corridor; fire corridor potential through metro area"},
            {"name": "Canadian River", "bearing": "S", "type": "river",
             "notes": "Southern metro boundary; sandy floodplain with salt cedar; Norman/Moore border area"},
        ],
        "elevation_range_ft": (1050, 1450),
        "wui_exposure": (
            "Extensive WUI on eastern metro margins from Edmond south through Harrah, Newalla, "
            "and Choctaw. Low-density ranchette development in Cross Timbers woodland. Lake "
            "Thunderbird and Lake Draper residential areas embedded in dense vegetation. Western "
            "metro has grass fire exposure but less intense. Eastern redcedar encroachment "
            "continuously expanding the high-hazard WUI zone."
        ),
        "historical_fires": [
            {"name": "Luther/Newalla fires", "year": 2024, "acres": 3000,
             "structures_destroyed": 12, "fatalities": 0, "cause": "power line",
             "notes": "Multiple fires in eastern OKC metro; homes destroyed in Newalla/Harrah area; Cross Timbers fuels"},
            {"name": "NE Oklahoma City fire", "year": 2023, "acres": 1500,
             "structures_destroyed": 5, "fatalities": 0, "cause": "unknown",
             "notes": "Burned in Cross Timbers east of Harrah; rapid spread in redcedar; evacuations ordered"},
            {"name": "Choctaw/Harrah Complex", "year": 2011, "acres": 8000,
             "structures_destroyed": 30, "fatalities": 0, "cause": "multiple",
             "notes": "Multiple fires during 2011 drought; Cross Timbers fuels produced extreme fire behavior; eastern OKC metro threatened"},
        ],
        "evacuation_routes": [
            {"route": "I-40", "direction": "east toward Shawnee / west through OKC", "lanes": 6,
             "bottleneck": "I-40/I-35 interchange; Tinker AFB area congestion",
             "risk": "Primary E-W escape from eastern metro; high capacity but smoke from Cross Timbers fires can close segments"},
            {"route": "I-35", "direction": "north toward Edmond / south toward Norman", "lanes": 6,
             "bottleneck": "I-35/I-40 junction; I-35/I-240 merge; chronically congested",
             "risk": "Primary N-S escape but crosses fire-prone areas; grass fires can approach from west; heavy daily traffic"},
            {"route": "SE 59th/Newalla Road", "direction": "east from OKC to Newalla", "lanes": 2,
             "bottleneck": "Narrow 2-lane through Cross Timbers; dead-end subdivisions feed onto single road",
             "risk": "Primary evacuation route for Newalla area but passes through same woodland that burns; easily overwhelmed"},
            {"route": "US-270/SH-3", "direction": "SE toward Shawnee", "lanes": 4,
             "bottleneck": "Narrows to 2 lanes past Harrah; limited interchanges",
             "risk": "Passes through Cross Timbers corridor; fire can close road at multiple points"},
        ],
        "fire_spread_characteristics": (
            "Dual fire regime: grass fires on western prairie (5-10 mph ROS, 3-6 ft flame lengths) "
            "and woodland fires in eastern Cross Timbers (2-5 mph ROS, 20-40 ft flame lengths in "
            "crown fire). Eastern redcedar encroachment is the critical trend: converting grass "
            "fire regime to crown fire regime across formerly open rangeland. Cedar torching produces "
            "extreme spotting (0.5-1 mi). Post-frontal NW winds of 35-55 mph drive both fire types. "
            "Winter fire season (Nov-Mar) with dormant grass curing to 90-100% and deciduous "
            "woodland leaf litter adding to fuel bed."
        ),
        "infrastructure_vulnerabilities": (
            "OG&E transmission through Cross Timbers vulnerable to fire damage and as ignition "
            "source. Eastern metro water systems served by Rural Water Districts with limited fire "
            "flow. Cell towers in woodland vulnerable to cedar crown fire. Tinker AFB (SE OKC) "
            "requires specialized fire protection. Narrow, dead-end subdivision roads in Newalla "
            "area create evacuation traps. Storm shelters (tornado) may not be appropriate for "
            "fire evacuation."
        ),
        "demographics_risk_factors": (
            "Metro population ~1.4 million but WUI-exposed eastern population in tens of thousands. "
            "Rapid growth in Harrah, Newalla, Choctaw communities. Mixed income levels with "
            "significant mobile home population. Rural water districts provide unreliable fire flow. "
            "Volunteer fire departments serve eastern metro fringe. Many residents relocated from "
            "urban core unfamiliar with wildfire risk. Large military population at Tinker AFB."
        ),
    },

    # =========================================================================
    # 15. STILLWATER, OK
    # =========================================================================
    "stillwater_ok": {
        "center": (36.1156, -97.0584),
        "terrain_notes": (
            "Stillwater sits at approximately 886 ft elevation in north-central Oklahoma, in the "
            "Cross Timbers ecological region along Stillwater Creek. The city is home to Oklahoma "
            "State University (25,000+ students) and has a population of approximately 50,000 that "
            "swells during academic sessions and football Saturdays. The terrain is rolling to "
            "hilly, with Stillwater Creek and its tributaries cutting shallow valleys through "
            "sandstone bedrock. The Cross Timbers here consists of post oak and blackjack oak "
            "woodland on sandy upland soils, with tallgrass prairie in the valleys and on clay "
            "soils. Eastern redcedar has aggressively encroached across formerly open rangeland "
            "and prairie, converting grass fuels to continuous canopy fuels at an estimated rate "
            "of 700+ acres per day statewide. Oklahoma State University manages extensive "
            "research rangeland and the Cross Timbers Experimental Range south of the city, "
            "providing some of the best-documented fuel condition data in the region. Lake Carl "
            "Blackwell (3,370 acres), 10 miles west, is surrounded by Cross Timbers woodland "
            "with recreational and residential development on its shores. Boomer Lake, within the "
            "city, provides limited terrain relief. The Stillwater area experiences the same "
            "winter fire regime as the broader Southern Plains: post-frontal cold front winds of "
            "35-55 mph with low RH across cured grass and dormant deciduous woodland. Payne "
            "County has recorded multiple fires exceeding 2,000 acres in recent decades, and "
            "the combination of university population, cedar encroachment, and expanding WUI "
            "development makes Stillwater increasingly vulnerable to wildland fire."
        ),
        "key_features": [
            {"name": "Oklahoma State University", "bearing": "central", "type": "university",
             "notes": "25,000+ students; large campus; agricultural research land borders rangeland; Boone Pickens Stadium (60,000 capacity)"},
            {"name": "Cross Timbers Experimental Range", "bearing": "S", "type": "research_rangeland",
             "notes": "OSU research facility; well-documented fuel conditions; post oak/blackjack/cedar study area"},
            {"name": "Lake Carl Blackwell", "bearing": "W", "type": "reservoir",
             "notes": "3,370-acre OSU-managed lake; Cross Timbers woodland surrounds; recreational/residential WUI"},
            {"name": "Stillwater Creek", "bearing": "through city", "type": "creek",
             "notes": "Primary drainage; shallow valley; riparian corridor; Boomer Lake impoundment in city"},
            {"name": "Eastern redcedar invasion", "bearing": "throughout", "type": "vegetation_change",
             "notes": "Aggressive encroachment converting prairie to woodland; dramatically increasing fire hazard"},
        ],
        "elevation_range_ft": (800, 1050),
        "wui_exposure": (
            "Moderate-high WUI on west, south, and east city margins. Lake Carl Blackwell residential "
            "areas in Cross Timbers. OSU agricultural research land provides buffer on some margins "
            "but also extends fuel continuity. Rural development along SH-51 and SH-177 corridors. "
            "Cedar encroachment increasing hazard annually."
        ),
        "historical_fires": [
            {"name": "Payne County fires", "year": 2016, "acres": 3500,
             "structures_destroyed": 4, "fatalities": 0, "cause": "power line",
             "notes": "Multiple fires in Cross Timbers west of Stillwater; redcedar crown fire; OSU research land burned"},
            {"name": "Lake Carl Blackwell fire", "year": 2011, "acres": 2000,
             "structures_destroyed": 2, "fatalities": 0, "cause": "campfire escape",
             "notes": "Burned Cross Timbers around reservoir; threatened recreational facilities and lakeside homes"},
            {"name": "Perkins Road fire", "year": 2023, "acres": 1500,
             "structures_destroyed": 1, "fatalities": 0, "cause": "unknown",
             "notes": "Grass/cedar fire south of Stillwater; rapid spread in post-frontal winds; evacuations ordered"},
        ],
        "evacuation_routes": [
            {"route": "SH-51", "direction": "west toward Ponca City area / east toward Tulsa turnpike", "lanes": 4,
             "bottleneck": "SH-51/US-177 interchange; Cimarron Turnpike access east",
             "risk": "Primary E-W route; passes through Cross Timbers in both directions; fire can close segments"},
            {"route": "US-177", "direction": "south toward OKC / north toward Ponca City", "lanes": 4,
             "bottleneck": "OSU campus area congestion; narrows outside city",
             "risk": "Primary N-S route; crosses fire-prone rangeland; football game day traffic can compound evacuation"},
            {"route": "SH-33", "direction": "west toward Guthrie", "lanes": 2,
             "bottleneck": "2-lane through rolling prairie/Cross Timbers; Cimarron River crossing",
             "risk": "Secondary route; passes through cedar-encroached terrain; limited capacity"},
        ],
        "fire_spread_characteristics": (
            "Cross Timbers fuel complex with post oak/blackjack canopy and aggressive redcedar "
            "understory creates potential for crown fire runs in extreme wind events. Cedar torching "
            "produces 20-35 ft flame lengths and launches firebrands 0.5 mi+. Tallgrass prairie "
            "valleys provide rapid spread corridors (5-10 mph) connecting woodland patches. "
            "Post-frontal NW winds of 35-55 mph drive fire across all fuel types. Winter dormancy "
            "increases grass fire spread rates while leaf litter in woodland increases fire "
            "intensity."
        ),
        "infrastructure_vulnerabilities": (
            "OG&E and PSO transmission through Cross Timbers. OSU campus power, heating, and "
            "research facility infrastructure. Municipal water from Kaw Lake pipeline (50+ mi); "
            "drought vulnerability. Boone Pickens Stadium (60,000 capacity) during events creates "
            "mass evacuation challenge. Cell towers in woodland settings vulnerable to cedar fire."
        ),
        "demographics_risk_factors": (
            "Population ~50,000; OSU adds 25,000+ students. Students unfamiliar with wildfire risk "
            "and evacuation procedures. Game day crowds (60,000+) create massive temporary "
            "population in fire season. International student population may face language barriers. "
            "Rural areas south and west rely on volunteer fire departments. Growing WUI population "
            "on city margins."
        ),
    },

    # =========================================================================
    # 13. WOODWARD, OK
    # =========================================================================
    "woodward_ok": {
        "center": (36.4336, -99.3903),
        "terrain_notes": (
            "Woodward sits at approximately 1,900 ft elevation in the mixed-grass prairie of "
            "northwestern Oklahoma, at the confluence of the North Canadian River and numerous "
            "smaller tributaries. The terrain is gently rolling to hilly, with distinctive sand "
            "dunes and sand sage grassland to the south (Packsaddle Wildlife Management Area) "
            "and flat mixed-grass prairie to the north and west. The North Canadian River has "
            "carved a broad, shallow valley through the area, with sandy floodplains supporting "
            "cottonwood, salt cedar, and sand plum thickets. The Boiling Springs State Park, "
            "located 6 miles east of Woodward, features natural springs and dense riparian "
            "woodland. Woodward County's vegetation is primarily mixed-grass prairie (little "
            "bluestem, sideoats grama, sand dropseed) with sand sagebrush on sandy soils and "
            "increasing eastern redcedar encroachment on formerly open rangeland. The area is "
            "in the heart of Oklahoma's winter fire belt: cold fronts sweeping southeast across "
            "the flat terrain produce 40-60 mph winds with single-digit RH across miles of "
            "cured dormant grass. Woodward has a tragic tornado history (1947 tornado killed "
            "116) but also faces significant wildfire risk. The city is located 60 miles south "
            "of the Kansas border and lies in the same fire corridor that produced the 2017 "
            "Starbuck Fire (which originated in Beaver County, 100 miles to the west). Multiple "
            "grass fires exceeding 10,000 acres have burned in Woodward County during recent "
            "fire seasons. The city population of approximately 12,000 serves as the regional "
            "hub for a vast ranching area in northwestern Oklahoma."
        ),
        "key_features": [
            {"name": "North Canadian River", "bearing": "through area", "type": "river",
             "notes": "Major drainage; sandy floodplain; salt cedar/cottonwood riparian; minimal firebreak value"},
            {"name": "Packsaddle WMA", "bearing": "S", "type": "wildlife_management",
             "notes": "Sand sage grassland and sand dunes; unique habitat; fire-maintained ecosystem; prescribed burn area"},
            {"name": "Boiling Springs State Park", "bearing": "E", "type": "state_park",
             "notes": "6 mi E; natural springs; dense riparian woodland; recreational area in fire-exposed setting"},
            {"name": "Sand sage prairie", "bearing": "S/SW", "type": "grassland",
             "notes": "Distinctive sand sage/grass community on sandy soils; highly flammable when cured; difficult suppression"},
        ],
        "elevation_range_ft": (1750, 2100),
        "wui_exposure": (
            "Moderate WUI with city surrounded by mixed-grass prairie and sand sage. Eastern "
            "and southern development abuts rangeland directly. Fort Supply (15 mi NW) and other "
            "small communities similarly exposed. Ranching operations throughout county create "
            "scattered rural WUI."
        ),
        "historical_fires": [
            {"name": "Woodward County Complex", "year": 2017, "acres": 18000,
             "structures_destroyed": 6, "fatalities": 0, "cause": "power line",
             "notes": "Part of March 2017 fire outbreak that included Starbuck Fire; burned NW Oklahoma grassland"},
            {"name": "Northwest Oklahoma fires", "year": 2016, "acres": 12000,
             "structures_destroyed": 3, "fatalities": 0, "cause": "multiple",
             "notes": "Multiple fires during Anderson Creek Fire outbreak; burned mixed-grass prairie; threatened small communities"},
            {"name": "Woodward County fire", "year": 2011, "acres": 8000,
             "structures_destroyed": 2, "fatalities": 0, "cause": "unknown",
             "notes": "Drought-driven grass fire; burned to city outskirts; demonstrated WUI vulnerability"},
        ],
        "evacuation_routes": [
            {"route": "US-270", "direction": "east toward Enid / west toward various", "lanes": 4,
             "bottleneck": "US-270/US-183 junction; narrows to 2 lanes west of city",
             "risk": "Primary E-W route; flat terrain allows fire approach; long distance to Enid (80 mi)"},
            {"route": "US-183", "direction": "north toward KS / south toward various", "lanes": 2,
             "bottleneck": "2-lane through open prairie; Fort Supply area",
             "risk": "Passes through continuous grass fuels; fires can close road; limited escape options"},
            {"route": "US-412", "direction": "east toward Cherokee", "lanes": 2,
             "bottleneck": "2-lane through rolling prairie; no services for long stretches",
             "risk": "Secondary route east; remote; fire exposure throughout"},
        ],
        "fire_spread_characteristics": (
            "Flat to rolling terrain with continuous mixed-grass fuels supports rapid wind-driven "
            "fire spread at 5-12 mph in post-frontal conditions. Sand sage adds volatility and "
            "resistance to suppression. Salt cedar along North Canadian River burns with extreme "
            "intensity. Cold front passages produce the most dangerous conditions: wind shifts "
            "NW at 40-60 mph with 5-10% RH. Continuous fuel beds extend to Kansas line with "
            "no significant breaks."
        ),
        "infrastructure_vulnerabilities": (
            "PSO/AEP transmission lines across open prairie. Water supply from Fort Supply Lake "
            "and groundwater; limited fire flow outside city. Volunteer fire departments serve "
            "surrounding communities. Small regional hospital (Woodward Regional) limited capacity. "
            "Natural gas infrastructure throughout county from oil/gas production. Cell coverage "
            "gaps in rural areas."
        ),
        "demographics_risk_factors": (
            "Population ~12,000. Regional hub for NW Oklahoma ranching community. Aging rural "
            "population with limited mobility. Significant livestock operations requiring animal "
            "evacuation. High poverty rates in surrounding communities. Volunteer fire departments "
            "are sole protection for rural residents. Limited multilingual emergency communications."
        ),
    },

    # =========================================================================
    # KANSAS (5 cities)
    # =========================================================================

    # =========================================================================
    # 18. ASHLAND, KS — Anderson Creek Fire 2016, Starbuck Fire 2017
    # =========================================================================
    "ashland_ks": {
        "center": (37.1886, -99.7654),
        "terrain_notes": (
            "Ashland sits at approximately 1,998 ft elevation in Clark County, Kansas, on the "
            "mixed-grass prairie of the southern High Plains. The city is the county seat of "
            "Clark County, which holds the grim distinction of having experienced the two largest "
            "wildfires in Kansas history in consecutive years: the 2016 Anderson Creek Fire "
            "(400,000 acres) and the 2017 Starbuck Fire (623,000 acres, of which 400,000 acres "
            "were in Clark County alone, burning approximately 75% of the county). The terrain "
            "around Ashland is gently rolling to flat, with the Cimarron River running through "
            "the southern part of the county and Bluff Creek, Bear Creek, and numerous smaller "
            "drainages creating shallow valleys in the prairie surface. Clark State Fishing Lake "
            "and Clark County State Park provide minor terrain relief south of town. The vegetation "
            "is mixed-grass prairie dominated by little bluestem, sideoats grama, big bluestem, "
            "and switchgrass, with sand sage on sandy soils along drainages. These taller grass "
            "species produce heavier fuel loads than the shortgrass prairie to the west, creating "
            "more intense fire behavior with 6-12 ft flame lengths. The Starbuck Fire burned at "
            "temperatures up to 1,600 degrees Fahrenheit, killing thousands of cattle, destroying "
            "4,100 miles of fence, and causing $44 million in property damage. The fire was driven "
            "by winds exceeding 60 mph from a March cold front, with the fire starting from "
            "ice-storm-damaged power lines in Beaver County, Oklahoma, and racing north into "
            "Kansas. Ashland's population of approximately 800 makes it a tiny community that "
            "has been repeatedly devastated by megafires, yet it remains the primary service "
            "center for Clark County's ranching operations."
        ),
        "key_features": [
            {"name": "Starbuck Fire burn scar", "bearing": "throughout county", "type": "burn_history",
             "notes": "75% of Clark County burned in 2017; 400,000 acres; recovery ongoing; fencing still being rebuilt"},
            {"name": "Anderson Creek Fire burn scar", "bearing": "E/SE", "type": "burn_history",
             "notes": "2016 fire burned 272,000 acres in Barber County, 141,000 in Comanche County to east"},
            {"name": "Cimarron River", "bearing": "S", "type": "river",
             "notes": "Intermittent river through southern county; sandy bed; salt cedar; minimal firebreak"},
            {"name": "Clark State Fishing Lake", "bearing": "S", "type": "reservoir",
             "notes": "Small reservoir; state park; mixed-grass surrounds; recreational area"},
            {"name": "Mixed-grass prairie", "bearing": "throughout", "type": "grassland",
             "notes": "Little bluestem/sideoats grama/big bluestem; heavier fuel loads than shortgrass; 6-12 ft flame lengths"},
        ],
        "elevation_range_ft": (1900, 2200),
        "wui_exposure": (
            "Small-city WUI with mixed-grass prairie on all margins. Ashland population ~800 with "
            "limited defensible space. Rural ranches scattered across county are primary WUI "
            "exposure. Post-Starbuck rebuilding has improved some structures but fencing and "
            "infrastructure still recovering."
        ),
        "historical_fires": [
            {"name": "Starbuck Fire", "year": 2017, "acres": 623000,
             "structures_destroyed": 50, "fatalities": 0, "cause": "downed power line (ice storm damage)",
             "notes": "Largest Kansas fire ever; 400,000 acres in Clark County alone (75% of county); 60+ mph winds; 1,600F temps; 4,100 mi fence destroyed; $44M damage; thousands of cattle killed"},
            {"name": "Anderson Creek Fire", "year": 2016, "acres": 400000,
             "structures_destroyed": 16, "fatalities": 0, "cause": "vehicle (Woods County OK)",
             "notes": "2nd largest KS fire; burned from OK into Barber/Comanche counties adjacent to Clark; 272,000 acres in Barber County; 600 cattle killed; $1.5M suppression cost"},
            {"name": "Clark County fires", "year": 2011, "acres": 15000,
             "structures_destroyed": 3, "fatalities": 0, "cause": "unknown",
             "notes": "Drought-driven grass fire; burned mixed-grass prairie; demonstrated continued vulnerability between megafires"},
        ],
        "evacuation_routes": [
            {"route": "US-160", "direction": "east toward Medicine Lodge / west toward Meade", "lanes": 2,
             "bottleneck": "2-lane through open prairie; 50+ mi between towns",
             "risk": "Primary E-W route; flat terrain, continuous fuel; fire outran vehicles during Starbuck Fire; 60 mph winds"},
            {"route": "US-283", "direction": "north toward Dodge City / south toward OK border", "lanes": 2,
             "bottleneck": "2-lane through prairie; Cimarron River crossing south",
             "risk": "Primary N-S route; Starbuck Fire crossed this highway; long distance to larger cities"},
            {"route": "KS-34/county roads", "direction": "various", "lanes": 2,
             "bottleneck": "Narrow county roads; many unpaved; not designed for evacuation",
             "risk": "Rural escape routes through continuous grass fuels; no shelter points; can be impassable in wet conditions"},
        ],
        "fire_spread_characteristics": (
            "Among the most extreme grassfire environments in the world. Mixed-grass prairie "
            "produces heavier fuel loads and taller flame lengths (6-12 ft) than shortgrass. "
            "The 2017 Starbuck Fire reached 1,600F and was driven by 60+ mph winds, outrunning "
            "vehicles and killing cattle that could not flee. Rate of spread exceeded 10 mph in "
            "open prairie. Fire fronts tens of miles wide during peak spread. No natural firebreaks "
            "exist across Clark County. Post-frontal NW wind shifts create the most dangerous "
            "conditions, converting flank fires to head fires across tens of thousands of acres "
            "simultaneously."
        ),
        "infrastructure_vulnerabilities": (
            "Power lines are proven fire ignition source (both 2016 and 2017 fires started from "
            "downed lines). Sunflower Electric transmission crosses open prairie. Municipal water "
            "from groundwater; severely limited fire flow. Volunteer fire department with minimal "
            "apparatus serves entire county. No hospital in Ashland; nearest significant medical "
            "facility 50+ mi. Cell coverage gaps throughout county. Post-Starbuck infrastructure "
            "still being rebuilt years later."
        ),
        "demographics_risk_factors": (
            "Population ~800 (county ~2,000). Extremely small, aging ranching community. "
            "Many residents are elderly with limited mobility. Post-fire economic stress from "
            "consecutive megafires. Cattle losses devastated local economy. Volunteer fire "
            "department struggles with recruitment in declining population. Mental health impacts "
            "from repeated fire trauma significant. County seat services (courthouse, school, "
            "medical clinic) serve scattered rural population with limited evacuation capacity."
        ),
    },

    # =========================================================================
    # 17. DODGE CITY, KS
    # =========================================================================
    "dodge_city_ks": {
        "center": (37.7528, -100.0171),
        "terrain_notes": (
            "Dodge City sits at approximately 2,493 ft elevation on the shortgrass prairie of "
            "southwestern Kansas, along the Arkansas River. The city is one of the windiest "
            "locations in the continental United States, with average annual wind speeds exceeding "
            "14 mph and frequent gusts above 50 mph during cold front passages. The terrain is "
            "flat to gently rolling, dominated by shortgrass prairie (blue grama, buffalograss) "
            "and irrigated agriculture (corn, wheat, sorghum) on the High Plains above the "
            "Arkansas River. The river has cut a broad, shallow valley through the flat terrain, "
            "with sandy banks supporting cottonwood, salt cedar, and sand plum. Sand dunes and "
            "sand sage prairie occur south of the river in the Cimarron National Grassland area "
            "(50 miles south). Dodge City is the center of the Kansas beef industry, surrounded "
            "by massive feedlots (Cargill, National Beef) processing over 5 million head annually. "
            "The flat terrain and extreme winds create some of the most dangerous grass fire "
            "conditions in North America: post-frontal winds routinely exceed 50 mph with single-"
            "digit RH, driving fires across continuous cured shortgrass at rates exceeding 10 mph. "
            "Ford County has experienced multiple large grass fires in recent decades, and the "
            "proximity to the Starbuck Fire corridor (2017, 623,000 acres, Clark/Comanche/Meade "
            "counties) demonstrates the scale of fire possible in this landscape. CRP grassland "
            "interspersed with crop stubble creates continuous fine fuels across the county. "
            "Dodge City's population of approximately 28,000 includes a significant immigrant "
            "meatpacking workforce, with limited multilingual emergency communication capacity."
        ),
        "key_features": [
            {"name": "Arkansas River", "bearing": "through city", "type": "river",
             "notes": "Major drainage; often dry or low flow; sandy bed; salt cedar/cottonwood riparian; minimal firebreak when dry"},
            {"name": "Shortgrass prairie", "bearing": "throughout", "type": "grassland",
             "notes": "Blue grama/buffalograss; cures by December; continuous fine fuels; extreme wind-driven fire potential"},
            {"name": "Feedlot complexes", "bearing": "S/W", "type": "agricultural/industrial",
             "notes": "Cargill, National Beef; 5M+ head annually; animal evacuation challenge; ammonia/methane hazards"},
            {"name": "CRP grassland", "bearing": "throughout county", "type": "conservation_grassland",
             "notes": "USDA Conservation Reserve Program; planted grass on former cropland; creates continuous fine fuel"},
            {"name": "Cimarron National Grassland", "bearing": "S", "type": "national_grassland",
             "notes": "50 mi S; 108,175 acres; sand sage/shortgrass; managed by USFS; large fire potential"},
        ],
        "elevation_range_ft": (2400, 2600),
        "wui_exposure": (
            "Moderate WUI with city surrounded by grassland and agricultural land on all sides. "
            "Feedlot complexes and associated worker housing in fire-exposed locations. Rural "
            "communities (Bucklin, Cimarron, Jetmore) similarly exposed. CRP grassland creates "
            "continuous fuel to city margins."
        ),
        "historical_fires": [
            {"name": "Ford County Complex", "year": 2017, "acres": 25000,
             "structures_destroyed": 5, "fatalities": 0, "cause": "power line",
             "notes": "Part of March 2017 Southern Plains fire outbreak that included Starbuck Fire; burned shortgrass/CRP south of Dodge City"},
            {"name": "Starbuck Fire", "year": 2017, "acres": 623000,
             "structures_destroyed": 50, "fatalities": 0, "cause": "downed power line (OK)",
             "notes": "Burned 50-80 mi E of Dodge City in Clark/Comanche/Meade counties; demonstrated regional fire scale; 75% of Clark County burned"},
            {"name": "Ford County grass fire", "year": 2022, "acres": 8000,
             "structures_destroyed": 2, "fatalities": 0, "cause": "equipment",
             "notes": "Winter grass fire NW of city; 50+ mph winds drove rapid spread; threatened rural homes and feedlot operations"},
        ],
        "evacuation_routes": [
            {"route": "US-56/US-283", "direction": "NE toward Great Bend / south toward Liberal", "lanes": 2,
             "bottleneck": "2-lane highways; Mullinville and Bucklin towns slow traffic",
             "risk": "Primary routes out of city; flat terrain allows fire approach from any direction; long distances between services"},
            {"route": "US-50", "direction": "east toward Kinsley/Hutchinson / west toward Garden City", "lanes": 2,
             "bottleneck": "2-lane through flat prairie; Arkansas River bridges",
             "risk": "Flat terrain; fire can close road at any point; smoke visibility hazard in winter fire weather"},
            {"route": "US-400", "direction": "east toward Greensburg", "lanes": 2,
             "bottleneck": "2-lane through open prairie; no services for 30+ miles",
             "risk": "Passes through continuous shortgrass/CRP fuels; extreme fire exposure"},
        ],
        "fire_spread_characteristics": (
            "Among the most extreme grass fire conditions in North America. Flat terrain with "
            "unimpeded wind fetch allows fire to spread at 8-15+ mph in post-frontal conditions. "
            "Shortgrass/CRP fuels cure to 95-100% by December. Post-frontal NW winds routinely "
            "exceed 50 mph with 5-10% RH. Continuous fuel beds extend 100+ miles in every "
            "direction. No natural firebreaks. Dryline passages create abrupt transitions to "
            "extreme fire weather. Rate of spread can exceed rate of evacuation on 2-lane roads."
        ),
        "infrastructure_vulnerabilities": (
            "Sunflower Electric and Mid-Kansas Electric transmission across flat prairie. Water "
            "supply from groundwater (Ogallala Aquifer/Arkansas River alluvium); declining levels. "
            "Feedlot ammonia and methane systems create HAZMAT risk during fires. Small regional "
            "hospital (Western Plains Medical Complex) limited capacity. Railroad corridors carry "
            "hazardous materials. All routes out of city are 2-lane highways."
        ),
        "demographics_risk_factors": (
            "Population ~28,000 with large immigrant meatpacking workforce (Hispanic/Latino 62%, "
            "Somali, Burmese, Vietnamese communities). Limited multilingual emergency communication. "
            "High poverty rates. Significant mobile home population. Rural elderly scattered on "
            "isolated farms and ranches. Feedlot workers may have limited transportation options. "
            "Dodge City Community College adds ~2,000 students."
        ),
    },

    # =========================================================================
    # 28. LIBERAL, KS — SW Kansas, Shortgrass Prairie Fires
    # =========================================================================
    "liberal_ks": {
        "center": (37.0439, -100.9210),
        "terrain_notes": (
            "Liberal sits at approximately 2,839 ft elevation on the flat shortgrass prairie of "
            "southwestern Kansas in Seward County, in the heart of the High Plains. The terrain "
            "is among the flattest in North America, with the Cimarron River providing the only "
            "significant topographic feature as it runs 15 miles south of the city. The landscape "
            "is dominated by irrigated agriculture (corn, wheat, sorghum, cattle) overlying the "
            "Ogallala Aquifer, with CRP grassland, shortgrass prairie (blue grama, buffalograss), "
            "and sand sage on sandy soils in the southern part of the county. The Cimarron National "
            "Grassland (108,175 acres), managed by the U.S. Forest Service, lies 30 miles south "
            "in Morton and Stevens counties, representing the largest tract of public land in "
            "Kansas and a significant fire management landscape. Liberal is located 40 miles "
            "east of the Oklahoma Panhandle and 50 miles north of the Texas Panhandle, placing "
            "it in the same fire corridor that has produced megafires in both states. The 2017 "
            "Starbuck Fire burned 60 miles east of Liberal; the 2024 Smokehouse Creek Fire burned "
            "70 miles south. Seward County experiences regular winter grass fires, with warm, dry "
            "conditions fueling multiple fires in southwestern Kansas in February 2024. The flat "
            "terrain and extreme winds (Liberal averages 15+ mph annual wind speed, among the "
            "highest in the US) create extreme grass fire conditions: post-frontal winds routinely "
            "exceed 50 mph with single-digit RH across miles of continuous cured grass. Liberal's "
            "population of approximately 19,000 is the largest city in the Kansas High Plains "
            "southwest of Dodge City, with a significant immigrant meatpacking workforce. National "
            "Beef Packing operates a major processing facility in Liberal."
        ),
        "key_features": [
            {"name": "Flat shortgrass prairie", "bearing": "throughout", "type": "grassland",
             "notes": "Featureless terrain; no topographic relief; unimpeded wind fetch; 15+ mph average wind; extreme fire spread"},
            {"name": "Cimarron River", "bearing": "S", "type": "river",
             "notes": "15 mi S; intermittent flow; sandy bed; salt cedar; minimal firebreak when dry; connects to Cimarron Nat'l Grassland"},
            {"name": "Cimarron National Grassland", "bearing": "SW", "type": "national_grassland",
             "notes": "108,175 acres; 30 mi S; USFS managed; sand sage/shortgrass; largest KS public land; significant fire management"},
            {"name": "National Beef Packing", "bearing": "S", "type": "industrial",
             "notes": "Major meatpacking facility; ammonia systems; large workforce; specialized evacuation needs"},
            {"name": "Irrigated agriculture", "bearing": "throughout", "type": "agriculture",
             "notes": "Center pivot irrigation from Ogallala Aquifer; green fields provide some firebreak during growing season; stubble burns in winter"},
        ],
        "elevation_range_ft": (2750, 2900),
        "wui_exposure": (
            "Moderate WUI with city surrounded by agricultural land and grassland. National Beef "
            "facility and associated worker housing in fire-exposed locations. Mobile home parks "
            "on city periphery. Rural communities (Kismet, Plains, Hugoton) similarly exposed. "
            "CRP grassland creates continuous fuel to city margins in some areas."
        ),
        "historical_fires": [
            {"name": "Seward County fires", "year": 2024, "acres": 8000,
             "structures_destroyed": 2, "fatalities": 0, "cause": "unknown",
             "notes": "Multiple fires in Feb 2024 during warm dry conditions; 50% containment; demonstrated continued vulnerability; 10 mi E of Liberal"},
            {"name": "SW Kansas fire complex", "year": 2017, "acres": 15000,
             "structures_destroyed": 3, "fatalities": 0, "cause": "power line",
             "notes": "Part of March 2017 fire outbreak concurrent with Starbuck Fire; burned shortgrass/CRP in Seward and Stevens counties"},
            {"name": "Kansas wildfire outbreak", "year": 2021, "acres": 20000,
             "structures_destroyed": 5, "fatalities": 0, "cause": "multiple",
             "notes": "163,000 acres burned statewide in single day; 100 mph gusts in some areas; Seward County among affected; southwestern KS hit hard"},
        ],
        "evacuation_routes": [
            {"route": "US-83", "direction": "north toward Garden City / south toward OK Panhandle", "lanes": 2,
             "bottleneck": "2-lane through flat prairie; 50+ mi to Garden City; OK border south",
             "risk": "Primary N-S route; flat terrain; continuous fuel; fire can close at any point; long distances between services"},
            {"route": "US-54", "direction": "NE toward Dodge City / SW toward Guymon OK", "lanes": 2,
             "bottleneck": "2-lane through open prairie; Kismet junction; long stretches without services",
             "risk": "Primary NE route; passes through continuous shortgrass/CRP; 50+ mi to Dodge City; fire corridor"},
            {"route": "US-270", "direction": "east toward various", "lanes": 2,
             "bottleneck": "2-lane through flat prairie; limited alternatives",
             "risk": "Secondary route east; same flat, fire-prone terrain; no significant firebreaks"},
            {"route": "US-56", "direction": "west toward Hugoton/Elkhart", "lanes": 2,
             "bottleneck": "2-lane through open prairie; remote; minimal services",
             "risk": "Leads into more remote terrain; Cimarron National Grassland area fire-prone; not toward safety"},
        ],
        "fire_spread_characteristics": (
            "Among the most extreme flat-terrain grass fire conditions in North America. Average "
            "wind speed 15+ mph year-round; post-frontal gusts 50-70 mph. Shortgrass/CRP fuels "
            "cure to 95-100% by December. Rate of spread 8-15+ mph in extreme conditions. "
            "Continuous fuel beds extend 100+ miles in every direction. No natural firebreaks. "
            "Irrigated center pivots provide seasonal breaks (growing season only); winter stubble "
            "burns readily. Dryline passages create extreme fire weather with RH dropping to "
            "3-8%. The 2021 outbreak with 100 mph gusts demonstrated the extreme end of fire "
            "weather in this landscape."
        ),
        "infrastructure_vulnerabilities": (
            "Sunflower Electric and Pioneer Electric transmission across flat prairie. National Beef "
            "ammonia refrigeration systems create HAZMAT risk during fires. Water supply from "
            "Ogallala Aquifer; declining levels threaten long-term supply. Small hospital (Southwest "
            "Medical Center) limited for mass casualty. All routes are 2-lane highways. Railroad "
            "carries hazardous materials. Meatpacking workforce housing concentrated in "
            "fire-exposed areas."
        ),
        "demographics_risk_factors": (
            "Population ~19,000. Majority-minority city (Hispanic/Latino 65%+; Somali, Guatemalan, "
            "Vietnamese communities). Significant meatpacking workforce with limited English "
            "proficiency. Emergency communications must be multilingual to be effective. High "
            "poverty rates; limited ability to evacuate or shelter independently. Large mobile home "
            "population highly vulnerable to fire. Seward County Community College adds ~1,500 "
            "students. Rural elderly scattered on isolated farms."
        ),
    },

    # =========================================================================
    # 27. MEDICINE LODGE, KS — Barber County, Starbuck Fire Impact
    # =========================================================================
    "medicine_lodge_ks": {
        "center": (37.2811, -98.5805),
        "terrain_notes": (
            "Medicine Lodge sits at approximately 1,496 ft elevation in the Medicine River valley "
            "in Barber County, Kansas, at the transition between the tallgrass Flint Hills to the "
            "east and the mixed-grass prairie of the Great Plains to the west. The terrain is "
            "gently rolling to hilly, with the Medicine River and Elm Creek providing drainage "
            "corridors lined with cottonwood, hackberry, and salt cedar. The Gypsum Hills (Red "
            "Hills) extend to the south and west, featuring distinctive red-orange gypsum and "
            "red-bed sandstone outcrops with cedar-covered slopes. These hills create more "
            "complex terrain and fuel patterns than the flat prairie to the north. Barber County "
            "was devastated by the 2016 Anderson Creek Fire, which burned 272,000 acres in the "
            "county (the bulk of the 400,000-acre fire). The following year, the 2017 Starbuck "
            "Fire also impacted the region, burning through adjacent Clark and Comanche counties "
            "with 623,000 total acres. The back-to-back megafires were catastrophic for the "
            "county's ranching economy, killing hundreds of cattle, destroying thousands of "
            "miles of fence, and devastating grassland that took years to recover. During the "
            "2017 Starbuck Fire, the mayor of Medicine Lodge called for voluntary evacuations "
            "as massive wildfires bore down on the town, with the blaze consuming two houses on "
            "the northern edge of the city and threatening the remaining 800-1,000 homes and "
            "businesses. Medicine Lodge's population of approximately 1,900 makes it a tiny "
            "community that has experienced repeated fire devastation. The mixed-grass prairie "
            "in Barber County produces heavier fuel loads than the shortgrass prairie to the "
            "west, with little bluestem and big bluestem creating 3-4 ft tall cured fuel beds "
            "that support intense fire behavior."
        ),
        "key_features": [
            {"name": "Medicine River valley", "bearing": "through town", "type": "river_valley",
             "notes": "Primary drainage; cottonwood/salt cedar riparian; moderate firebreak when river has flow"},
            {"name": "Gypsum Hills (Red Hills)", "bearing": "S/SW", "type": "hills",
             "notes": "Distinctive red gypsum/sandstone terrain; cedar-covered slopes; complex fire behavior; scenic area"},
            {"name": "Anderson Creek Fire scar", "bearing": "throughout county", "type": "burn_history",
             "notes": "272,000 acres of Barber County burned in 2016; recovery ongoing; fencing rebuilt but ecosystem altered"},
            {"name": "Mixed-grass prairie", "bearing": "throughout", "type": "grassland",
             "notes": "Little bluestem/big bluestem/sideoats grama; 3-4 ft cured fuel; heavier than shortgrass; intense fire behavior"},
            {"name": "Flint Hills transition", "bearing": "E", "type": "ecological_boundary",
             "notes": "Tallgrass prairie begins 20-30 mi east; even heavier fuel loads; prescribed burn culture"},
        ],
        "elevation_range_ft": (1400, 1700),
        "wui_exposure": (
            "Small-city WUI with mixed-grass prairie on all margins. Starbuck Fire approached "
            "city in 2017, destroying 2 houses on northern edge and threatening 800-1,000 "
            "structures. Rural ranches throughout county are primary WUI exposure. Gypsum Hills "
            "to south have scattered rural development in complex terrain."
        ),
        "historical_fires": [
            {"name": "Anderson Creek Fire", "year": 2016, "acres": 400000,
             "structures_destroyed": 16, "fatalities": 0, "cause": "vehicle (Woods County OK)",
             "notes": "272,000 acres in Barber County alone; largest KS fire at time; started in OK; 600 cattle killed; 45 mph winds; fire spread a mile every 4 minutes"},
            {"name": "Starbuck Fire", "year": 2017, "acres": 623000,
             "structures_destroyed": 50, "fatalities": 0, "cause": "downed power line (ice storm damage)",
             "notes": "Burned through adjacent Clark/Comanche counties; Medicine Lodge evacuated; 2 houses destroyed on city's N edge; 60+ mph winds; larger fire passed 10-20 mi west"},
            {"name": "Barber County grass fire", "year": 2022, "acres": 5000,
             "structures_destroyed": 1, "fatalities": 0, "cause": "unknown",
             "notes": "Winter grass fire demonstrating continued vulnerability between megafires; burned mixed-grass prairie"},
        ],
        "evacuation_routes": [
            {"route": "US-160", "direction": "west toward Ashland / east toward Wellington", "lanes": 2,
             "bottleneck": "2-lane through open prairie; 50+ mi between towns in each direction",
             "risk": "Primary E-W route; flat terrain; continuous fuel; Starbuck Fire could have closed this road; fire outran vehicles at 60 mph"},
            {"route": "US-281", "direction": "north toward Pratt / south toward OK border", "lanes": 2,
             "bottleneck": "2-lane through mixed-grass prairie; Gypsum Hills south",
             "risk": "Primary N-S route; 40+ mi to Pratt; passes through fire-prone terrain in both directions"},
            {"route": "KS-2", "direction": "east toward Anthony", "lanes": 2,
             "bottleneck": "Narrow 2-lane; rolling terrain through prairie",
             "risk": "Secondary route; passes through mixed-grass/Flint Hills transition; limited services"},
        ],
        "fire_spread_characteristics": (
            "Mixed-grass prairie produces heavier fuel loads and taller flame lengths (6-12 ft) "
            "than shortgrass to the west. Anderson Creek Fire spread a mile every 4 minutes in "
            "45 mph winds. Starbuck Fire was driven by 60+ mph winds. Back-to-back megafires "
            "demonstrate that this landscape produces extreme fire behavior regularly. Gypsum "
            "Hills cedar adds crown fire component on slopes. Post-frontal NW wind shifts "
            "convert flank fires to head fires across tens of thousands of acres simultaneously. "
            "No natural firebreaks across the county."
        ),
        "infrastructure_vulnerabilities": (
            "Power lines are proven fire pathway (Starbuck Fire started from ice-storm-damaged "
            "lines). Sunflower Electric transmission across open prairie. Municipal water from "
            "groundwater; limited fire flow. Volunteer fire department with minimal apparatus "
            "devastated by back-to-back megafires. No hospital; nearest in Pratt (40 mi) or "
            "Wichita (80 mi). All routes are 2-lane highways. Cell coverage gaps. Post-fire "
            "fencing infrastructure rebuilt with $18M NRCS investment."
        ),
        "demographics_risk_factors": (
            "Population ~1,900. Tiny ranching community devastated by consecutive megafires. "
            "Aging population with limited mobility. Post-fire economic stress ongoing: cattle "
            "losses, fence replacement costs, grassland recovery time. Volunteer fire department "
            "recruitment challenged. Mental health impacts from repeated fire trauma. School "
            "consolidation reflects declining population. Community resilience tested but "
            "strained by repeated disasters."
        ),
    },

    # =========================================================================
    # 16. WICHITA, KS
    # =========================================================================
    "wichita_ks": {
        "center": (37.6872, -97.3301),
        "terrain_notes": (
            "Wichita sits at approximately 1,299 ft elevation at the confluence of the Arkansas "
            "River and Little Arkansas River in south-central Kansas, on the flat to gently rolling "
            "mixed-grass and tallgrass prairie transition zone. The city is the largest in Kansas "
            "with a metro population of approximately 650,000 and serves as the aviation capital "
            "of the world, with major facilities for Boeing, Spirit AeroSystems, Textron Aviation "
            "(Cessna/Beechcraft), and Bombardier/Learjet. The terrain around Wichita is among the "
            "flattest in North America, with the Flint Hills tallgrass prairie rising to the east "
            "and the Great Plains mixed-grass prairie extending west. The Arkansas River provides "
            "a major drainage through the city, but the broad, sandy floodplain with cottonwood "
            "and salt cedar creates more of a fire corridor than a firebreak. Chisholm Creek, "
            "Cowskin Creek, and other tributaries provide minor terrain relief. The Flint Hills, "
            "beginning 30-40 miles east, are the largest remaining intact tallgrass prairie in "
            "North America and are managed with prescribed fire annually (millions of acres burned "
            "each spring), creating a unique fire culture but also extreme fire risk when burns "
            "escape or when wildfires ignite during unplanned conditions. West of Wichita, the "
            "terrain transitions to wheat agriculture and CRP grassland that cures in late fall "
            "and supports rapid fire spread through winter. Sedgwick County experiences regular "
            "grass fires during the November-March fire season, with post-frontal cold front "
            "winds of 40-60 mph across flat terrain creating extreme spread rates. The 2016 "
            "Anderson Creek Fire burned 400,000 acres 80 miles south of Wichita, demonstrating "
            "the scale of prairie fire possible in this region."
        ),
        "key_features": [
            {"name": "Arkansas River", "bearing": "through city", "type": "river",
             "notes": "Major drainage; sandy floodplain; salt cedar/cottonwood riparian; fire corridor potential; bridges throughout metro"},
            {"name": "Flint Hills tallgrass prairie", "bearing": "E", "type": "grassland",
             "notes": "30-40 mi E; largest intact tallgrass prairie; managed with prescribed fire; extreme fire weather potential"},
            {"name": "Aviation industry complex", "bearing": "S/SE", "type": "industrial",
             "notes": "Boeing, Spirit AeroSystems, Textron; McConnell AFB; fuel storage; specialized evacuation requirements"},
            {"name": "Great Plains prairie", "bearing": "W", "type": "grassland",
             "notes": "Flat wheat/CRP/mixed-grass to west; continuous fine fuels; unimpeded wind fetch"},
            {"name": "McConnell AFB", "bearing": "SE", "type": "military",
             "notes": "KC-46 tanker base; fuel storage; munitions; 3,500+ personnel; requires buffer zones"},
        ],
        "elevation_range_ft": (1250, 1400),
        "wui_exposure": (
            "Moderate WUI on west and south city margins where development meets grassland. "
            "Haysville, Derby, Goddard satellite communities expanding into agricultural land. "
            "Aviation industrial complex on south side borders open grassland. McConnell AFB "
            "perimeter abuts prairie. East side faces Flint Hills fire corridor."
        ),
        "historical_fires": [
            {"name": "Sedgwick County grass fires", "year": 2018, "acres": 4000,
             "structures_destroyed": 3, "fatalities": 0, "cause": "multiple",
             "notes": "Multiple fires during March cold front; burned west and south of city; demonstrated urban fringe vulnerability"},
            {"name": "Flint Hills escaped burns", "year": 2016, "acres": 8000,
             "structures_destroyed": 2, "fatalities": 0, "cause": "prescribed burn escape",
             "notes": "Escaped prescribed burns in Flint Hills east of Wichita; demonstrated extreme fire behavior in tallgrass"},
            {"name": "Anderson Creek Fire", "year": 2016, "acres": 400000,
             "structures_destroyed": 16, "fatalities": 0, "cause": "vehicle",
             "notes": "80 mi S of Wichita; 400,000 acres in KS/OK; largest KS fire at time; 600 cattle killed; demonstrated regional fire scale"},
        ],
        "evacuation_routes": [
            {"route": "I-35", "direction": "north toward Topeka / south toward OKC", "lanes": 6,
             "bottleneck": "Kellogg (US-54) interchange; I-35/I-135 junction; daily congestion",
             "risk": "Primary N-S escape; high capacity; crosses prairie on both ends; smoke can reduce visibility"},
            {"route": "US-54/Kellogg", "direction": "east toward Augusta / west toward Kingman", "lanes": 6,
             "bottleneck": "Downtown interchanges; narrows to 4 lanes outside metro",
             "risk": "Primary E-W route; east leads toward Flint Hills (potential fire source); west through open prairie"},
            {"route": "I-135/US-81", "direction": "north toward Salina", "lanes": 4,
             "bottleneck": "I-135/I-235 interchange; North Junction",
             "risk": "Route north through flat agricultural land; fires can approach from west across wheat stubble/CRP"},
            {"route": "US-400/US-166", "direction": "SE toward Independence/Chanute", "lanes": 4,
             "bottleneck": "Narrows to 2 lanes past Derby; Flint Hills terrain",
             "risk": "Enters Flint Hills tallgrass prairie; extreme fire potential in prescribed burn season (Mar-Apr)"},
        ],
        "fire_spread_characteristics": (
            "Flat terrain allows unimpeded wind-driven fire spread in all directions. Tallgrass "
            "prairie (Flint Hills) to east produces the most intense grass fires in North America "
            "when ignited under extreme conditions: 10-20 ft flame lengths, 8-15 mph ROS, ember "
            "transport 0.5+ mi. Mixed-grass and wheat stubble/CRP to west supports 5-12 mph "
            "spread rates. Post-frontal NW winds of 40-60 mph drive fire across all fuel types. "
            "Prescribed burn season (Mar-Apr) creates additional ignition sources. Winter dormancy "
            "(Nov-Mar) produces cured fuels at 90-100%."
        ),
        "infrastructure_vulnerabilities": (
            "Evergy and Westar Energy transmission across open prairie. Aviation industry facilities "
            "(Boeing, Spirit, Textron) contain specialized materials and fuels. McConnell AFB "
            "requires military fire protection protocols. Water supply from Cheney Reservoir "
            "(20 mi W) via pipeline; drought vulnerability. Major rail yards carry hazardous "
            "materials. Aviation fuel storage throughout south side of metro."
        ),
        "demographics_risk_factors": (
            "Metro population ~650,000. Major aviation workforce (50,000+ jobs). McConnell AFB "
            "military population. Significant Southeast Asian refugee community (Vietnamese, "
            "Laotian) with potential language barriers. Wichita State University adds 16,000+ "
            "students. Derby, Haysville, Goddard growing rapidly in WUI zone. Large elderly "
            "population in established neighborhoods."
        ),
    },

}




# ---------------------------------------------------------------------------
# 2. IGNITION SOURCES — Southern Plains specific
# ---------------------------------------------------------------------------

PLAINS_IGNITION_SOURCES = {
    # -- Transportation Corridor Ignitions --
    "trucking_corridors": {
        "description": (
            "The Southern Plains has the densest transcontinental trucking "
            "corridors in the US. Chain drags on concrete, tire blowouts, "
            "brake fires, catalytic converter heat, and cigarettes from truck "
            "cabs are all documented ignition sources. Smoke across highways "
            "is also a major secondary hazard (East Amarillo Complex 2006: "
            "4 died in I-40 smoke pileup)."
        ),
        "corridors": {
            "I-40": {
                "route": "E-W across TX Panhandle and central OK",
                "cities_affected": [
                    "amarillo_tx", "childress_tx", "oklahoma_city_ok",
                ],
                "fire_history": (
                    "2006: 4 deaths in smoke pileup. 2016: fire jumped I-40 "
                    "near Shamrock, TxDOT used blades for firebreaks. 2024: "
                    "Smokehouse Creek forced closures."
                ),
                "risk_level": "extreme",
            },
            "I-35": {
                "route": "N-S through central OK/KS",
                "cities_affected": [
                    "oklahoma_city_ok", "guthrie_ok", "wichita_ks",
                ],
                "fire_history": (
                    "2025: Both directions closed at 122nd in OKC, NB closed "
                    "at Covell Rd in Edmond due to fire."
                ),
                "risk_level": "high",
            },
            "I-27": {
                "route": "N-S Lubbock to Amarillo",
                "cities_affected": ["lubbock_tx", "amarillo_tx"],
                "fire_history": "Smoke closures during Panhandle fire events.",
                "risk_level": "high",
            },
            "I-20": {
                "route": "E-W across W/Central TX",
                "cities_affected": [
                    "midland_odessa_tx", "abilene_tx", "eastland_tx",
                ],
                "fire_history": (
                    "Large grass fire erupted along I-20 west of Abilene. "
                    "Mesquite Heat Fire (2022) required I-20 area evacuations."
                ),
                "risk_level": "high",
            },
            "US-287": {
                "route": "NW-SE diagonal across TX Panhandle",
                "cities_affected": [
                    "amarillo_tx", "childress_tx", "wichita_falls_tx",
                ],
                "fire_history": (
                    "Closed between Claude and SH-70 during 2016 fires. "
                    "4-vehicle accident near Childress sparked median fire. "
                    "Childress FD works multiple grass fires along 287 annually."
                ),
                "risk_level": "extreme",
            },
        },
    },

    # -- Utility Infrastructure --
    "power_lines": {
        "description": (
            "Power line failures are the #1 cause of megafires in the Southern "
            "Plains. Aging wooden poles (some nearly 100 years old) snap in "
            "50-70 mph winds, dropping energized lines onto cured grass. "
            "Ice storms loosen hardware that fails weeks later in wind events."
        ),
        "utilities": {
            "xcel_energy": {
                "territory": "TX Panhandle, eastern NM",
                "cities_served": [
                    "amarillo_tx", "borger_pampa_tx", "fritch_tx",
                ],
                "fire_history": (
                    "Smokehouse Creek Fire (2024): decayed utility pole broke "
                    "at ground level 1 mi NW of Stinnett, lines fell on dry "
                    "grass. TX sued Xcel for $1B+ — some poles were nearly "
                    "100 years old, 2.5x their typical lifespan. Xcel "
                    "acknowledged facilities involved in ignition."
                ),
                "risk_level": "extreme",
            },
            "aep_swepco": {
                "territory": "Central/West TX",
                "cities_served": [
                    "abilene_tx", "san_angelo_tx", "wichita_falls_tx",
                    "eastland_tx",
                ],
                "fire_history": (
                    "AEP Texas serves much of the western TX region. "
                    "Power line failures during wind events are a recurring "
                    "ignition source across the territory."
                ),
                "risk_level": "high",
            },
            "oge_energy": {
                "territory": "Central/Western OK",
                "cities_served": [
                    "oklahoma_city_ok", "guthrie_ok", "stillwater_ok",
                ],
                "fire_history": (
                    "OG&E lines affected by ice storms and sustained high "
                    "winds. Eastern OK and Cross Timbers areas see line "
                    "failures in winter storms."
                ),
                "risk_level": "moderate-high",
            },
            "kansas_utilities": {
                "territory": "Western/Central KS",
                "cities_served": [
                    "dodge_city_ks", "ashland_ks", "wichita_ks",
                ],
                "fire_history": (
                    "Starbuck Fire (2017): ignited in OK by power lines "
                    "loosened in prior ice storm that arced/sparked in 60+ "
                    "mph winds. Downed power line in Hodgeman County caused "
                    "18,000 ac fire that destroyed homes."
                ),
                "risk_level": "high",
            },
        },
    },

    # -- Oil & Gas Infrastructure --
    "oil_gas_equipment": {
        "description": (
            "The Permian Basin (Midland-Odessa) and Texas Panhandle have "
            "thousands of active wells, pump jacks, tank batteries, flare "
            "stacks, and pipelines. Equipment failures — hydraulic line "
            "bursts contacting hot surfaces, static electricity in dry air "
            "igniting vapors, and unattended flare stacks — are unique "
            "ignition sources found nowhere else at this density."
        ),
        "high_risk_areas": [
            "midland_odessa_tx",
            "borger_pampa_tx",
            "san_angelo_tx",
        ],
        "ignition_mechanisms": [
            "Hydraulic line burst + hot surface contact",
            "Static electricity on dry equipment igniting vapors",
            "Flare stack sparks carried by wind",
            "Pipeline leak/rupture + friction ignition",
            "Vehicle/equipment exhaust in dry grass around well pads",
        ],
        "risk_level": "high",
    },

    # -- Prescribed Burns --
    "prescribed_burns": {
        "description": (
            "The Southern Plains has the heaviest prescribed burn activity "
            "in the US. The Flint Hills of KS/OK burn ~2.2 million acres "
            "annually (primarily March-April). Oklahoma has dozens of "
            "Prescribed Burn Associations. Escaped prescribed burns are a "
            "documented wildfire ignition source, though prescribed fire is "
            "also the primary tool for REDUCING wildfire risk by removing "
            "fuel and controlling eastern redcedar invasion."
        ),
        "hot_zones": {
            "flint_hills_ks_ok": {
                "area_burned_annually_ac": 2_200_000,
                "peak_season": "March-April",
                "cities_affected": ["wichita_ks", "stillwater_ok"],
                "notes": (
                    "KDHE Flint Hills Smoke Management Plan regulates burns. "
                    "Smoke transport to Wichita causes PM2.5 exceedances. "
                    "Escaped burns rare but catastrophic when they occur."
                ),
            },
            "cross_timbers_ok": {
                "peak_season": "February-April",
                "cities_affected": [
                    "oklahoma_city_ok", "guthrie_ok", "stillwater_ok",
                ],
                "notes": (
                    "Cross Timber PBA (Chandler), North Central Range "
                    "Improvement Assn (Guthrie). Burns to control eastern "
                    "redcedar invasion. Liability is #1 landowner concern."
                ),
            },
        },
        "risk_level": "moderate (escape risk) / beneficial (fuel reduction)",
    },

    # -- Railroad --
    "railroad": {
        "description": (
            "BNSF's transcontinental mainline (Transcon) runs through the "
            "Texas Panhandle, SW Kansas, and central Oklahoma. Train sparks "
            "from brakes, bearing failures, and rail grinding ignite trackside "
            "grass. Downed lines from fire can also impact rail operations — "
            "the Smokehouse Creek Fire damaged BNSF's Canadian River bridge."
        ),
        "corridors": {
            "bnsf_transcon": {
                "route": "Chicago-LA via Amarillo, Dodge City, Wichita",
                "cities_affected": [
                    "amarillo_tx", "borger_pampa_tx", "dodge_city_ks",
                    "wichita_ks",
                ],
                "fire_history": (
                    "2024: Smokehouse Creek Fire severely damaged BNSF bridge "
                    "over Canadian River (Panhandle Subdivision). 2023: BNSF "
                    "sued for train-spark wildfire in NE (40,000 ac). "
                    "Failure to clear dry brush from right-of-way cited."
                ),
                "risk_level": "moderate-high",
            },
            "bnsf_panhandle_sub": {
                "route": "Amarillo to Wellington, KS",
                "cities_affected": [
                    "amarillo_tx", "borger_pampa_tx", "childress_tx",
                ],
                "fire_history": (
                    "Both mainlines impacted by Smokehouse Creek Fire. "
                    "One mainline restored in ~36 hours."
                ),
                "risk_level": "high",
            },
        },
    },

    # -- Agricultural Equipment --
    "agricultural_equipment": {
        "description": (
            "Farm equipment is a major ignition source across the Southern "
            "Plains: combine sparks during harvest (especially cotton, wheat, "
            "milo), tractor exhaust systems in dry stubble, welding on ranch "
            "equipment, and hay baling equipment friction. Cotton harvest in "
            "West TX (Sep-Nov) and wheat harvest in KS/OK (Jun-Jul) are "
            "peak risk periods."
        ),
        "high_risk_activities": [
            "Cotton harvest (W TX, Sep-Nov) — module builders, pickers",
            "Wheat harvest (KS/OK, Jun-Jul) — combine fires",
            "Hay baling (year-round in TX) — baler friction",
            "Welding/cutting on ranch equipment (year-round)",
            "Tractor exhaust in stubble fields",
        ],
        "cities_most_affected": [
            "lubbock_tx", "midland_odessa_tx", "childress_tx",
            "dodge_city_ks", "ashland_ks", "woodward_ok",
        ],
        "risk_level": "high (especially during harvest periods)",
    },

    # -- Other Human Sources --
    "other_human": {
        "description": "Additional human ignition sources specific to the region.",
        "sources": [
            {
                "type": "vehicle_accidents",
                "notes": (
                    "Anderson Creek Fire (2016, 400,000 ac) ignited by a "
                    "vehicle spark. 4-vehicle accident on US-287 near "
                    "Childress sparked median fire."
                ),
            },
            {
                "type": "arson",
                "notes": (
                    "Some of the Eastland Complex fires (2022) are suspected "
                    "to have been human-caused. 7 fires ignited within hours."
                ),
            },
            {
                "type": "debris_burning",
                "notes": (
                    "Escaped trash burns and debris burns are common in "
                    "rural areas. Often during burn bans when legal burning "
                    "is prohibited."
                ),
            },
            {
                "type": "lightning",
                "notes": (
                    "Dry thunderstorms (lightning without significant precip) "
                    "common in spring/summer along the dryline. Wildcat Fire "
                    "near San Angelo was lightning-caused."
                ),
            },
        ],
    },
}


# ---------------------------------------------------------------------------
# 3. CLIMATOLOGY — Winter fire season focus (Nov-Mar)
# ---------------------------------------------------------------------------

PLAINS_CLIMATOLOGY = {
    "region_overview": {
        "primary_fire_season": "November through April (peak: January-March)",
        "secondary_fire_season": "June-July (harvest fires, lightning)",
        "why_winter": (
            "Grasses (buffalo grass, blue grama, big bluestem, little bluestem) "
            "go dormant by November and cure to 5-10% fuel moisture by December. "
            "Winter cold fronts bring 40-70 mph wind gusts with RH dropping to "
            "8-15%. The combination of fully cured continuous grassland fuel, "
            "extreme wind, and very low RH creates the most explosive fire "
            "conditions in North America. This is the opposite of western US "
            "fire season (summer/fall)."
        ),
        "worst_months_by_acres": ["March", "February", "April", "January"],
        "key_weather_drivers": [
            "Cold front passage — wind shift from SW to NW, gust to 50-80 mph",
            "Dryline — boundary between Gulf moisture and High Plains dry air",
            "Lee-side troughing — low pressure east of Rockies accelerates surface wind",
            "Chinook/downslope warming — warm dry air descends east of Rockies",
            "Jet stream amplification — 100+ kt jets aloft mix to surface",
        ],
    },

    # Per-city climatology with quantitative data
    "city_climatology": {
        "amarillo_tx": {
            "annual_avg_wind_mph": 13.6,
            "peak_gust_recorded_mph": 84,
            "winter_avg_rh_pct": 40,
            "critical_rh_threshold_pct": 15,
            "days_below_15pct_rh_winter": 25,
            "annual_precip_in": 19.7,
            "winter_precip_in": 2.5,
            "avg_first_hard_freeze": "Oct 25",
            "avg_last_hard_freeze": "Apr 15",
            "dormant_grass_period": "Nov 1 - Apr 15",
            "fire_weather_notes": (
                "Palo Duro Canyon creates its own microclimate — inversions "
                "trap cold air in canyon while rim is warm and windy. NWS "
                "Amarillo created a dedicated Palo Duro Canyon forecast zone "
                "due to unique conditions. Dust storms reduce visibility to "
                "near zero during extreme wind events, complicating fire ops."
            ),
        },
        "lubbock_tx": {
            "annual_avg_wind_mph": 12.4,
            "peak_gust_recorded_mph": 90,
            "winter_avg_rh_pct": 38,
            "critical_rh_threshold_pct": 15,
            "days_below_15pct_rh_winter": 28,
            "annual_precip_in": 18.7,
            "winter_precip_in": 2.2,
            "avg_first_hard_freeze": "Nov 1",
            "avg_last_hard_freeze": "Apr 5",
            "dormant_grass_period": "Nov 1 - Apr 10",
            "fire_weather_notes": (
                "Caprock Escarpment accelerates wind — 80-90 mph gusts "
                "observed along the escarpment edge during fire events. "
                "NWS Lubbock Red Flag Warnings specifically reference "
                "Caprock enhancement. Dust is a major secondary hazard."
            ),
        },
        "midland_odessa_tx": {
            "annual_avg_wind_mph": 11.2,
            "peak_gust_recorded_mph": 75,
            "winter_avg_rh_pct": 35,
            "critical_rh_threshold_pct": 15,
            "days_below_15pct_rh_winter": 30,
            "annual_precip_in": 14.6,
            "winter_precip_in": 1.8,
            "avg_first_hard_freeze": "Nov 10",
            "avg_last_hard_freeze": "Mar 25",
            "dormant_grass_period": "Nov 15 - Mar 30",
            "fire_weather_notes": (
                "Driest metro on this list. Extended drought is the norm, "
                "not the exception. Oil field flares and equipment add unique "
                "ignition risk absent from other High Plains locations. "
                "Monahans sand dunes to the west generate extreme dust "
                "during wind events."
            ),
        },
        "san_angelo_tx": {
            "annual_avg_wind_mph": 10.8,
            "peak_gust_recorded_mph": 70,
            "winter_avg_rh_pct": 42,
            "critical_rh_threshold_pct": 20,
            "days_below_15pct_rh_winter": 15,
            "annual_precip_in": 21.3,
            "winter_precip_in": 3.0,
            "avg_first_hard_freeze": "Nov 15",
            "avg_last_hard_freeze": "Mar 15",
            "dormant_grass_period": "Dec 1 - Mar 15",
            "fire_weather_notes": (
                "Concho Valley is a convergence zone — terrain features "
                "can enhance local wind during cold front passages. Rough "
                "terrain to the NW (Coke County) makes fire suppression "
                "difficult. Mixed juniper-mesquite adds crown fire potential."
            ),
        },
        "abilene_tx": {
            "annual_avg_wind_mph": 11.5,
            "peak_gust_recorded_mph": 75,
            "winter_avg_rh_pct": 45,
            "critical_rh_threshold_pct": 20,
            "days_below_15pct_rh_winter": 12,
            "annual_precip_in": 24.0,
            "winter_precip_in": 3.5,
            "avg_first_hard_freeze": "Nov 15",
            "avg_last_hard_freeze": "Mar 15",
            "dormant_grass_period": "Dec 1 - Mar 15",
            "fire_weather_notes": (
                "Juniper-mesquite brush SW of Abilene creates crown fire "
                "risk not present in pure grassland. Mesquite Heat Fire "
                "(2022) showed active crown fire in this vegetation type. "
                "I-20 corridor adds trucking ignition risk."
            ),
        },
        "wichita_falls_tx": {
            "annual_avg_wind_mph": 11.0,
            "peak_gust_recorded_mph": 72,
            "winter_avg_rh_pct": 48,
            "critical_rh_threshold_pct": 20,
            "days_below_15pct_rh_winter": 10,
            "annual_precip_in": 28.5,
            "winter_precip_in": 3.8,
            "avg_first_hard_freeze": "Nov 15",
            "avg_last_hard_freeze": "Mar 15",
            "dormant_grass_period": "Dec 1 - Mar 15",
            "fire_weather_notes": (
                "Red River breaks terrain creates channeling and turbulence. "
                "Eastern redcedar encroachment along river corridors is "
                "increasing fire intensity. Higher moisture from Red River "
                "proximity partially mitigates some risk compared to the "
                "Panhandle, but drought years remove this buffer."
            ),
        },
        "borger_pampa_tx": {
            "annual_avg_wind_mph": 13.0,
            "peak_gust_recorded_mph": 80,
            "winter_avg_rh_pct": 38,
            "critical_rh_threshold_pct": 15,
            "days_below_15pct_rh_winter": 25,
            "annual_precip_in": 20.1,
            "winter_precip_in": 2.3,
            "avg_first_hard_freeze": "Oct 28",
            "avg_last_hard_freeze": "Apr 10",
            "dormant_grass_period": "Nov 1 - Apr 10",
            "fire_weather_notes": (
                "Ground zero for the two largest TX fires in history. "
                "Canadian River breaks create wind channeling that turns "
                "grass fires into freight-train events. Xcel Energy aging "
                "infrastructure (poles up to ~100 yrs old) is a proven "
                "catastrophic ignition source. Feb 2024 Smokehouse Creek "
                "started here."
            ),
        },
        "childress_tx": {
            "annual_avg_wind_mph": 12.0,
            "peak_gust_recorded_mph": 70,
            "winter_avg_rh_pct": 40,
            "critical_rh_threshold_pct": 15,
            "days_below_15pct_rh_winter": 20,
            "annual_precip_in": 22.0,
            "winter_precip_in": 2.8,
            "avg_first_hard_freeze": "Nov 5",
            "avg_last_hard_freeze": "Apr 1",
            "dormant_grass_period": "Nov 5 - Apr 1",
            "fire_weather_notes": (
                "I-40/US-287 junction makes this a convergence point for "
                "both fire and traffic. Flat terrain allows unimpeded fire "
                "runs. Wind shifts during cold front passage can reverse "
                "fire direction — happened during 2016 event when SW-to-NW "
                "shift blew fire back toward Shamrock and I-40."
            ),
        },
        "eastland_tx": {
            "annual_avg_wind_mph": 10.0,
            "peak_gust_recorded_mph": 65,
            "winter_avg_rh_pct": 50,
            "critical_rh_threshold_pct": 20,
            "days_below_15pct_rh_winter": 8,
            "annual_precip_in": 27.5,
            "winter_precip_in": 4.0,
            "avg_first_hard_freeze": "Nov 20",
            "avg_last_hard_freeze": "Mar 10",
            "dormant_grass_period": "Dec 1 - Mar 15",
            "fire_weather_notes": (
                "Cross Timbers vegetation adds crown fire risk from juniper "
                "and oak. March cold fronts are the trigger — the Eastland "
                "Complex ignited on March 17, 2022 as a cold front produced "
                "strong winds, dry air, and warm temperatures. 7 fires "
                "ignited within hours. Post oak-juniper fuel complex burns "
                "far more intensely than grassland alone."
            ),
        },
        "bastrop_tx": {
            "annual_avg_wind_mph": 8.5,
            "peak_gust_recorded_mph": 55,
            "winter_avg_rh_pct": 58,
            "critical_rh_threshold_pct": 25,
            "days_below_15pct_rh_winter": 5,
            "annual_precip_in": 34.0,
            "winter_precip_in": 6.0,
            "avg_first_hard_freeze": "Dec 1",
            "avg_last_hard_freeze": "Feb 28",
            "dormant_grass_period": "Dec 15 - Feb 28",
            "fire_weather_notes": (
                "Wetter than the Panhandle but the Lost Pines are a special "
                "case. Loblolly pine on deep sand — the sandy soil drains "
                "fast, creating a fuel moisture deficit even in normally wet "
                "years. The 2011 fire occurred after the worst single-year "
                "drought in TX history (2011). Pine needle litter and dead "
                "grass understory cure rapidly. Fire severity in 2011 was "
                "unprecedented in 360+ years of reconstructed fire history. "
                "Fire season here is Sep-Mar (later start than Panhandle)."
            ),
        },
        "fritch_tx": {
            "annual_avg_wind_mph": 13.0,
            "peak_gust_recorded_mph": 78,
            "winter_avg_rh_pct": 38,
            "critical_rh_threshold_pct": 15,
            "days_below_15pct_rh_winter": 25,
            "annual_precip_in": 19.5,
            "winter_precip_in": 2.3,
            "avg_first_hard_freeze": "Oct 28",
            "avg_last_hard_freeze": "Apr 10",
            "dormant_grass_period": "Nov 1 - Apr 10",
            "fire_weather_notes": (
                "Nearly identical to Borger/Pampa climatology but with "
                "additional exposure from Canadian River breaks terrain. "
                "Lake Meredith NRA provides no fire break — lake levels "
                "have been extremely low for decades. Town is physically "
                "adjacent to the breaks with no buffer zone."
            ),
        },
        "oklahoma_city_ok": {
            "annual_avg_wind_mph": 12.2,
            "peak_gust_recorded_mph": 82,
            "winter_avg_rh_pct": 52,
            "critical_rh_threshold_pct": 20,
            "days_below_15pct_rh_winter": 8,
            "annual_precip_in": 36.5,
            "winter_precip_in": 5.5,
            "avg_first_hard_freeze": "Nov 10",
            "avg_last_hard_freeze": "Mar 25",
            "dormant_grass_period": "Dec 1 - Mar 20",
            "fire_weather_notes": (
                "Higher precipitation than the Panhandle but fire risk is "
                "growing due to (1) eastern redcedar invasion creating "
                "volatile fuel loads, (2) rapid suburban expansion into "
                "cross-timbers WUI, and (3) periodic drought that erases "
                "the moisture advantage. March 2025 event showed this: "
                "113+ homes destroyed, 4 fire-related deaths across 12 "
                "counties. I-35 and I-40 closures in the metro."
            ),
        },
        "woodward_ok": {
            "annual_avg_wind_mph": 13.0,
            "peak_gust_recorded_mph": 80,
            "winter_avg_rh_pct": 42,
            "critical_rh_threshold_pct": 15,
            "days_below_15pct_rh_winter": 18,
            "annual_precip_in": 25.0,
            "winter_precip_in": 3.2,
            "avg_first_hard_freeze": "Nov 1",
            "avg_last_hard_freeze": "Apr 5",
            "dormant_grass_period": "Nov 1 - Apr 5",
            "fire_weather_notes": (
                "NW Oklahoma is one of the windiest, driest parts of the "
                "state. Open terrain with no firebreaks. The 2017 NW Oklahoma "
                "fire complex burned 830,000+ ac across the region. "
                "Sun-baked, wind-whipped landscape dries out quickly in "
                "late winter — all it takes is a day or two of extreme fire "
                "weather with strong winds and very low RH."
            ),
        },
        "guthrie_ok": {
            "annual_avg_wind_mph": 11.5,
            "peak_gust_recorded_mph": 75,
            "winter_avg_rh_pct": 50,
            "critical_rh_threshold_pct": 20,
            "days_below_15pct_rh_winter": 8,
            "annual_precip_in": 35.0,
            "winter_precip_in": 5.0,
            "avg_first_hard_freeze": "Nov 10",
            "avg_last_hard_freeze": "Mar 25",
            "dormant_grass_period": "Dec 1 - Mar 20",
            "fire_weather_notes": (
                "Transition zone between wetter eastern OK and drier west. "
                "Fire risk spikes during drought years when the moisture "
                "gradient collapses. Cross-timbers vegetation with eastern "
                "redcedar adds volatile fuels. March 2025 evacuations of "
                "SE Guthrie demonstrate that even moderate-risk cities can "
                "face extreme fire events."
            ),
        },
        "stillwater_ok": {
            "annual_avg_wind_mph": 11.0,
            "peak_gust_recorded_mph": 72,
            "winter_avg_rh_pct": 52,
            "critical_rh_threshold_pct": 20,
            "days_below_15pct_rh_winter": 8,
            "annual_precip_in": 36.0,
            "winter_precip_in": 5.5,
            "avg_first_hard_freeze": "Nov 5",
            "avg_last_hard_freeze": "Mar 28",
            "dormant_grass_period": "Nov 15 - Mar 25",
            "fire_weather_notes": (
                "Tallgrass prairie produces very high fuel loads when cured "
                "— big bluestem stands at 6-8 ft tall, creating a standing "
                "dead fuel complex that burns with extreme intensity. OSU "
                "research ranges use prescribed fire extensively. Eastern "
                "redcedar invasion is the fastest-growing fire risk factor."
            ),
        },
        "wichita_ks": {
            "annual_avg_wind_mph": 12.5,
            "peak_gust_recorded_mph": 80,
            "winter_avg_rh_pct": 55,
            "critical_rh_threshold_pct": 20,
            "days_below_15pct_rh_winter": 6,
            "annual_precip_in": 32.5,
            "winter_precip_in": 3.8,
            "avg_first_hard_freeze": "Nov 5",
            "avg_last_hard_freeze": "Apr 5",
            "dormant_grass_period": "Nov 10 - Apr 10",
            "fire_weather_notes": (
                "Primary fire hazard is smoke from Flint Hills prescribed "
                "burns (2.2M ac annually, peak March-April). PM2.5 "
                "exceedances during burn season. Direct wildfire threat is "
                "lower than western KS but Flint Hills tallgrass produces "
                "intense fires when they do occur."
            ),
        },
        "dodge_city_ks": {
            "annual_avg_wind_mph": 14.0,
            "peak_gust_recorded_mph": 100,
            "winter_avg_rh_pct": 45,
            "critical_rh_threshold_pct": 15,
            "days_below_15pct_rh_winter": 18,
            "annual_precip_in": 22.0,
            "winter_precip_in": 2.5,
            "avg_first_hard_freeze": "Oct 25",
            "avg_last_hard_freeze": "Apr 15",
            "dormant_grass_period": "Nov 1 - Apr 15",
            "fire_weather_notes": (
                "Windiest city on this list (~14 mph annual average). "
                "Dec 2021 windstorm produced 75-100 mph gusts — fires spread "
                "at 50+ mph, burning 67,500 ac in the Dodge City CWA alone. "
                "Total across W Kansas: 163,756 ac in a SINGLE DAY. "
                "RH drops as low as 13%. Extremely critical fire weather "
                "conditions occur multiple times per winter."
            ),
        },
        "ashland_ks": {
            "annual_avg_wind_mph": 13.5,
            "peak_gust_recorded_mph": 85,
            "winter_avg_rh_pct": 42,
            "critical_rh_threshold_pct": 15,
            "days_below_15pct_rh_winter": 20,
            "annual_precip_in": 23.0,
            "winter_precip_in": 2.5,
            "avg_first_hard_freeze": "Oct 28",
            "avg_last_hard_freeze": "Apr 10",
            "dormant_grass_period": "Nov 1 - Apr 10",
            "fire_weather_notes": (
                "Climate is similar to Dodge City but with even less "
                "infrastructure for suppression — tiny rural community "
                "dependent on volunteer fire departments. 80-85% of the "
                "entire county burned in Starbuck (2017). Wind gusts "
                "exceeded 60 mph with temperatures reaching 1,600F at the "
                "fire front. CRP grassland and cattle range provide "
                "continuous, unbroken fuel in every direction."
            ),
        },
    },

    # Regional fire-weather pattern signatures
    "fire_weather_patterns": {
        "cold_front_passage": {
            "description": (
                "The #1 fire weather trigger in the Southern Plains. A cold "
                "front approaching from the NW brings a wind shift from "
                "southwesterly to northwesterly. Pre-frontal winds are warm, "
                "dry, and strong (SW at 25-40 mph). As the front passes, "
                "winds shift to NW and may gust to 50-80 mph. RH drops to "
                "8-15% behind the front. Fires that were running NE on SW "
                "winds suddenly have their entire flank become the head as "
                "NW winds push the fire SE. This is how 5-10 mile wide fire "
                "heads develop."
            ),
            "peak_months": ["January", "February", "March"],
            "signature_events": [
                "Smokehouse Creek (2024): cold front + downed power line",
                "East Amarillo Complex (2006): 5 mph fire spread, 45 mi in 9 hrs",
                "Starbuck (2017): 60+ mph winds behind front",
            ],
        },
        "dryline_events": {
            "description": (
                "The dryline is a sharp moisture boundary between Gulf air "
                "(dewpoints 50-60F) and High Plains air (dewpoints -10 to "
                "20F). It typically sets up along a N-S line from the TX "
                "Panhandle through OK. Winds converge along the dryline and "
                "RH gradients are extreme — stepping from 60% to 10% in a "
                "few miles. Fires can explode when the dryline moves through."
            ),
            "peak_months": ["March", "April", "May"],
            "typical_position": "TX Panhandle through central OK (varies daily)",
        },
        "lee_trough_downslope": {
            "description": (
                "When strong westerly flow aloft interacts with the Rockies, "
                "a lee-side trough forms over the High Plains. Air descends "
                "east of the mountains, warming and drying adiabatically. "
                "This produces chinook-like conditions — warm (60-80F in "
                "winter), extremely dry (RH 5-15%), and windy (30-50 mph "
                "sustained). These events can persist for 1-3 days and are "
                "often the precursor to cold front passage."
            ),
            "peak_months": ["November", "December", "January", "February", "March"],
            "most_affected": [
                "amarillo_tx", "lubbock_tx", "borger_pampa_tx",
                "dodge_city_ks", "ashland_ks", "woodward_ok",
            ],
        },
        "extreme_wind_events": {
            "description": (
                "Non-thunderstorm wind events exceeding 60 mph occur multiple "
                "times per winter in the Southern Plains. These are driven by "
                "strong pressure gradients associated with deep cyclones "
                "tracking through the central US. Unlike thunderstorm "
                "downbursts, these sustained winds can last 6-12+ hours, "
                "giving fires enormous run distances."
            ),
            "peak_months": ["December", "January", "February", "March"],
            "notable_events": [
                "Dec 15, 2021: 75-100 mph gusts across W KS, 163,756 ac burned",
                "Mar 2006 East Amarillo Complex: 45 mi fire run in 9 hours",
                "Feb 2024 Smokehouse Creek: 500,000 ac in first 24 hours",
            ],
        },
    },

    # Critical thresholds for fire-weather forecasting
    "critical_thresholds": {
        "red_flag_warning_criteria": {
            "sustained_wind_mph": 20,
            "rh_pct": 15,
            "temp_f": 50,
            "notes": (
                "NWS issues Red Flag Warnings when sustained winds >= 20 mph "
                "AND RH <= 15% (High Plains) or <= 20% (Central OK/KS). "
                "These are MINIMUM thresholds — actual fire events often far "
                "exceed them."
            ),
        },
        "extremely_critical": {
            "sustained_wind_mph": 30,
            "gust_mph": 50,
            "rh_pct": 10,
            "notes": (
                "SPC Extremely Critical fire weather outlook issued when "
                "sustained winds >= 30 mph with gusts >= 50 mph AND "
                "RH <= 10%. These are the conditions that produce megafires."
            ),
        },
        "grass_fire_spread_rates": {
            "moderate_mph": 3,
            "high_mph": 8,
            "extreme_mph": 15,
            "catastrophic_mph": 50,
            "notes": (
                "Grass fires in the Southern Plains can spread at 50+ mph "
                "under extreme wind/RH conditions (Dec 2021 KS event). "
                "Even 'moderate' 3 mph spread in continuous grass is 3 miles "
                "per hour that suppression forces cannot outpace."
            ),
        },
    },
}


# ---------------------------------------------------------------------------
# Convenience: all city keys for iteration
# ---------------------------------------------------------------------------

ALL_PLAINS_CITIES = list(PLAINS_TERRAIN_PROFILES.keys())
"""Sorted list of all city keys in the Southern Plains profiles."""

# Quick-access coordinate lookup
PLAINS_CITY_COORDS = {
    key: profile.get("center", profile.get("coords"))
    for key, profile in PLAINS_TERRAIN_PROFILES.items()
}
"""Dict mapping city key -> (lat, lon) tuple."""
