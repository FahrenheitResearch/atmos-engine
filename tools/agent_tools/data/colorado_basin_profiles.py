"""Colorado, Great Basin & Wyoming Fire-Vulnerable City Profiles
===============================================================

Comprehensive terrain, evacuation, fire behavior, infrastructure, and demographic
data for 38 fire-vulnerable cities across Colorado, Nevada, Utah, and Wyoming.
Profiles derived from NWCG after-action reports, NIFC historical records,
state wildfire risk portals, CWPP documents, and peer-reviewed literature.

Usage:
    from tools.agent_tools.data.colorado_basin_profiles import (
        CO_BASIN_TERRAIN_PROFILES,
        CO_BASIN_IGNITION_SOURCES,
        CO_BASIN_CLIMATOLOGY,
    )

Cities covered (38 entries across 4 states):
    COLORADO (18 cities):
        Beulah
        Boulder
        Breckenridge
        Colorado Springs
        Durango
        Estes Park
        Evergreen Conifer
        Fort Collins
        Glenwood Springs
        Granby
        Grand Lake
        Louisville
        Manitou Springs
        Pagosa Springs
        Redstone Marble
        Steamboat Springs
        Superior
        Woodland Park
    NEVADA (8 cities):
        Carson City
        Elko
        Gardnerville Minden
        Genoa
        Incline Village
        Reno
        South Lake Tahoe
        Virginia City
    UTAH (6 cities):
        Brian Head
        Cedar City
        Heber City
        Midway
        Park City
        Springdale
    WYOMING (6 cities):
        Cody
        Dubois
        Jackson
        Lander
        Pinedale
        Sheridan

Sources:
    - NWCG after-action reports, NIFC historical records
    - Colorado State Forest Service wildfire risk portal
    - Nevada Division of Forestry fire records
    - Utah Division of Forestry, Fire & State Lands
    - Wyoming State Forestry Division
    - WRCC / IEM / ASOS climatology archives
"""

# =============================================================================
# TERRAIN PROFILES -- 38 entries organized by state
# =============================================================================

CO_BASIN_TERRAIN_PROFILES = {

    # =========================================================================
    # COLORADO (18 cities)
    # =========================================================================

    # =========================================================================
    # 18. BEULAH, CO (NEW)
    # =========================================================================
    "beulah_co": {
        "center": [38.0761, -104.9817],
        "terrain_notes": (
            "Beulah (6,300 ft) is a small unincorporated community of approximately 600 "
            "residents in southwestern Pueblo County, nestled in a narrow valley where "
            "Middle Creek, North Creek, and Pine Creek converge at the edge of the San "
            "Isabel National Forest and the Wet Mountains. The community has essentially "
            "a single access road — CO-78 (Beulah Highway) — running 20 miles southwest "
            "from Pueblo through increasingly narrow canyon terrain. The surrounding Wet "
            "Mountains rise to 12,000+ ft with dense ponderosa pine, Douglas-fir, and "
            "spruce-fir forests. Beulah has been repeatedly threatened by wildfire: the "
            "Beulah Hill Fire (2016) forced evacuations and destroyed structures, and the "
            "Oak Ridge Fire (June 2024) burned 1,310 acres nearby, evacuating 20 homes "
            "with 40 more under pre-evacuation. The community conducted a formal "
            "evacuation drill with the Pueblo County Sheriff's Office, demonstrating "
            "awareness of its extreme vulnerability. The single-road access means any "
            "fire blocking CO-78 traps the entire community."
        ),
        "key_features": [
            {"name": "CO-78 (Beulah Highway)", "bearing": "NE", "type": "sole_access_road",
             "notes": "Single road to Pueblo (20 miles); narrows through canyon terrain; fire on either side blocks all evacuation; no alternative paved routes"},
            {"name": "Middle Creek Canyon", "bearing": "C", "type": "canyon",
             "notes": "Primary valley through community; CO-78 follows creek; narrow terrain constrains development and evacuation"},
            {"name": "San Isabel National Forest", "bearing": "W/S", "type": "national_forest",
             "notes": "Dense ponderosa pine, Douglas-fir, spruce-fir; Wet Mountains terrain; fire-prone fuel conditions; oak brush at lower elevations"},
            {"name": "Wet Mountains", "bearing": "W/SW", "type": "mountain_range",
             "notes": "Rise to 12,000+ ft (Greenhorn Mountain 12,347 ft); dense forested slopes above community; steep terrain accelerates fire runs downhill toward town"},
            {"name": "Oak Ridge Fire area", "bearing": "NW", "type": "burn_scar",
             "notes": "1,310-acre 2024 fire; lightning-caused; burned near Pueblo-Custer County border; demonstrated ongoing fire risk just miles from town"},
            {"name": "Lake Isabel / St. Charles Peak area", "bearing": "SW", "type": "recreation",
             "notes": "Recreation area in San Isabel NF; draws visitors through Beulah; adds to evacuation population during fire events"},
        ],
        "elevation_range_ft": [6100, 6800],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Oak Ridge Fire", "year": 2024, "acres": 1310,
             "details": "June 22-July 2024; lightning-caused; 3 miles NW of Beulah near Pueblo-Custer County border; 20 homes evacuated, 40 under pre-evacuation; Middle Creek Canyon Road under mandatory evacuation; Vine Mesa, Cascade Ave, Pine Ave in pre-evacuation; 69% containment reached"},
            {"name": "Beulah Hill Fire", "year": 2016, "acres": 2037,
             "details": "Nov 28 2016; wind-driven fire forced evacuations; structures lost; Pueblo County emergency response; demonstrated fall/winter fire risk; Chinook wind event"},
            {"name": "North Creek Fire", "year": 2023, "acres": 50,
             "details": "Small fire near Beulah; 100% contained; demonstrated recurring ignition risk; evacuation protocols activated"},
            {"name": "Junkins Fire", "year": 2016, "acres": 1970,
             "details": "October 2016; burned in Wet Mountains south of Beulah; demonstrated regional fire risk; single structure destroyed"},
        ],
        "evacuation_routes": [
            {"route": "CO-78 Northeast (to Pueblo)", "direction": "NE", "lanes": 2,
             "bottleneck": "20 miles to Pueblo; narrows through canyon; single lane each direction; curves and grades; fire on either side of road blocks all evacuation",
             "risk": "ONLY paved evacuation route; fire blocking any section of CO-78 traps entire community of 600+; successful evacuation drill conducted but real event with fire on road would be catastrophic"},
            {"route": "Middle Creek Canyon Road", "direction": "W", "lanes": 2,
             "bottleneck": "Unpaved road into national forest; dead-end",
             "risk": "NOT an evacuation route; leads deeper into forested mountains; dead-end; mandatory evacuation zone during Oak Ridge Fire"},
            {"route": "Forest Service roads", "direction": "Various", "lanes": 1,
             "bottleneck": "Unpaved, narrow, seasonal; 4WD required; not connected to any alternative paved routes in reasonable distance",
             "risk": "Emergency-only for individual vehicles; not viable for community evacuation; may lead into active fire zones"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Chinook downslope winds from west through Wet Mountains; canyon winds channeled through Middle Creek and Pine Creek drainages; afternoon upslope thermals; Beulah Hill Fire demonstrated wind-driven fire in fall Chinook event",
            "critical_corridors": [
                "Middle Creek Canyon — single-road community; fire in canyon traps entire population",
                "CO-78 corridor — fire along highway blocks only evacuation route",
                "Wet Mountains western slopes — steep terrain with dense timber above community",
                "North Creek / Pine Creek drainages — fire approach corridors from west and south",
            ],
            "rate_of_spread_potential": "High to extreme on steep mountain slopes; Beulah Hill Fire demonstrated rapid wind-driven spread in fall; Oak Ridge Fire tripled in size in 48 hours despite suppression efforts; ponderosa pine and oak brush provide continuous fuel; steep terrain creates chimney effect in drainages",
            "spotting_distance": "0.5-1 mile; canyon updrafts from steep Wet Mountain slopes; ponderosa bark firebrands; oak brush produces intense heat; embers can cross creek drainages and ignite opposite slope",
        },
        "infrastructure_vulnerabilities": {
            "water_system": "No municipal water; private wells and springs; no fire hydrants; fire suppression entirely by tanker shuttle from Pueblo (20 miles); limited water storage for firefighting; streams may be insufficient during drought",
            "power": "Black Hills Energy; overhead lines along CO-78; single feed; power loss common during fire events; downed lines potential ignition source; no redundant supply",
            "communications": "Very limited cell coverage in canyon; CO-78 corridor has some coverage but gaps in surrounding mountains; Pueblo County emergency alerts primary notification; some residents may not receive alerts; landline service limited",
            "medical": "No medical facilities; nearest hospital is Parkview Medical Center (Pueblo, 20+ miles NE); ambulance response 30-45 min under normal conditions; fire on CO-78 could prevent ambulance access entirely; no helicopter landing zone in narrow canyon; nearest air ambulance base in Pueblo",
        },
        "demographics_risk_factors": {
            "population": 600,
            "seasonal_variation": "Summer recreation draws visitors to Lake Isabel and national forest through town; some vacation/seasonal homes; ranching community with dispersed rural population",
            "elderly_percentage": "22%+ (rural retirement community character)",
            "mobile_homes": "Significant manufactured homes in community; highly vulnerable; limited defensible space on many properties; older construction",
            "special_needs_facilities": "No medical facilities; no hospital; volunteer fire protection district; high elderly percentage in remote single-access community; many residents live alone on dispersed properties; successful evacuation drill (2024) shows community awareness but real event complexity would be far greater",
        },
    },

    # =========================================================================
    # 2. BOULDER, CO
    # =========================================================================
    "boulder_co": {
        "center": [40.0150, -105.2705],
        "terrain_notes": (
            "Boulder sits at the base of the Flatirons and the Front Range, with the "
            "city climbing from approximately 5,300 ft on the eastern plains to over "
            "8,000 ft at the mountain parks boundary. The western half of the city is "
            "the textbook definition of wildland-urban interface — homes built directly "
            "into ponderosa pine and Douglas-fir forests on steep mountain slopes. "
            "Flagstaff Mountain (6,983 ft) rises directly above downtown, and Boulder "
            "Canyon, Fourmile Canyon, Sunshine Canyon, and Left Hand Canyon penetrate "
            "deep into the mountains with scattered residential development. The city "
            "experienced the Fourmile Canyon Fire (2010, 6,181 acres, 168 homes) which "
            "at the time was the most destructive fire in Colorado history. Boulder is "
            "also ground zero for Chinook downslope wind events, with NCAR Mesa Lab "
            "recording gusts up to 109 mph. The Marshall Fire (2021) demonstrated that "
            "even the grassland-suburban interface east of Boulder is catastrophically "
            "vulnerable when winds exceed 100 mph."
        ),
        "key_features": [
            {"name": "Flatirons / Flagstaff Mountain", "bearing": "W", "type": "mountain",
             "notes": "Iconic sandstone formations; Flagstaff at 6,983 ft directly above downtown; forest thinning projects ongoing"},
            {"name": "Boulder Canyon", "bearing": "W", "type": "canyon",
             "notes": "CO-119 corridor into mountains; residential development in narrow canyon; single road access"},
            {"name": "Fourmile Canyon", "bearing": "NW", "type": "canyon_wui",
             "notes": "Site of 2010 fire; scattered mountain homes in ponderosa pine; limited egress"},
            {"name": "Sunshine Canyon", "bearing": "NW", "type": "canyon_wui",
             "notes": "Dense WUI with single-road access canyons; Gold Hill community at dead end"},
            {"name": "NCAR / Table Mesa", "bearing": "SW", "type": "research_facility",
             "notes": "National Center for Atmospheric Research at WUI boundary; Mesa Lab records extreme wind data"},
            {"name": "Marshall / Superior grasslands", "bearing": "SE", "type": "grassland",
             "notes": "Open grassland that carried Marshall Fire into suburban development at extreme speed"},
        ],
        "elevation_range_ft": [5300, 8459],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Fourmile Canyon Fire", "year": 2010, "acres": 6181,
             "details": "Started Sep 6; 168 homes destroyed; 7% humidity, 40+ mph gusts; burned 5,700 acres on day 1 alone; was most destructive CO fire at the time"},
            {"name": "Marshall Fire", "year": 2021, "acres": 6200,
             "details": "Dec 30 grassland fire with 115 mph wind gusts; 1,084 structures in Superior/Louisville; unprecedented winter suburban wildfire"},
            {"name": "Flagstaff/Realization Fire", "year": 2025, "acres": 2,
             "details": "Small Nov 2025 fire near Realization Point on Flagstaff Mountain; quickly contained but demonstrated ongoing ignition risk directly above downtown"},
            {"name": "Cold Springs Fire", "year": 2016, "acres": 528,
             "details": "Nederland area fire west of Boulder; 8 homes destroyed; demonstrated continued canyon WUI vulnerability"},
        ],
        "evacuation_routes": [
            {"route": "US-36 (to Denver)", "direction": "SE", "lanes": 4,
             "bottleneck": "Single expressway connecting Boulder to Denver metro; closed during Marshall Fire",
             "risk": "Primary evacuation route for 105K residents; closure during fire events forces all traffic to secondary roads"},
            {"route": "CO-119 (Boulder Canyon)", "direction": "W", "lanes": 2,
             "bottleneck": "Narrow mountain canyon; single lane each direction; no shoulders",
             "risk": "Only western route; canyon could trap evacuees if fire enters from either end"},
            {"route": "CO-93 / CO-72 (to Golden)", "direction": "S", "lanes": 2,
             "bottleneck": "Marshall Fire originated near CO-93/Marshall Road intersection",
             "risk": "Southern route passes through highest grassland fire risk zone"},
            {"route": "US-36 North (to Lyons/Estes)", "direction": "N", "lanes": 4,
             "bottleneck": "Narrows through foothills north of town",
             "risk": "Viable evacuation route but leads toward other fire-prone mountain communities"},
            {"route": "Diagonal Highway / CO-119 East", "direction": "E", "lanes": 4,
             "bottleneck": "Best capacity route but requires crossing open grassland",
             "risk": "Grassland fire exposure during wind events; Marshall Fire demonstrated this vulnerability"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Chinook downslope westerlies; NCAR Mesa Lab recorded 109 mph gust (Dec 2025); sustained 60-80 mph common in major events",
            "critical_corridors": [
                "Fourmile/Sunshine Canyon fire runs downslope into city",
                "Flagstaff Mountain — directly above downtown, upwind in Chinook events",
                "CO-93 grassland corridor — Marshall Fire path",
                "Left Hand Canyon to northern Boulder neighborhoods",
            ],
            "rate_of_spread_potential": "Catastrophic in Chinook wind events; Marshall Fire moved through 6,200 acres of grass in hours; Fourmile burned 5,700 acres in single day; canyon fires can reach city in under 1 hour",
            "spotting_distance": "1-2+ miles in Chinook events; Marshall Fire documented ember ignitions well ahead of main front in grass; mountain fires produce lofted embers in canyon updrafts",
        },
        "infrastructure_vulnerabilities": {
            "water_system": "City of Boulder water from Barker Reservoir (Boulder Canyon) and Carter Lake; mountain watershed vulnerable to fire contamination; Fourmile burn scar impacted Boulder Creek water quality for years",
            "power": "Xcel Energy and Boulder municipal utility; mountain transmission lines through WUI; power shutoffs now planned during extreme wind events",
            "communications": "Flagstaff Mountain and Sugarloaf towers; smoke and wind can degrade coverage in canyons; canyon communities may lose cell service",
            "medical": "Boulder Community Health (Foothills Hospital); Good Samaritan Medical Center in Lafayette; limited hospital capacity for 105K city + university population",
        },
        "demographics_risk_factors": {
            "population": 105098,
            "seasonal_variation": "CU Boulder adds 35,000 students during academic year; Pearl Street tourism peaks in summer; total daily population can exceed 160K",
            "elderly_percentage": "11.2%",
            "mobile_homes": "Limited within city; some mobile home parks in unincorporated Boulder County",
            "special_needs_facilities": "CU campus (35K students, many unfamiliar with fire evacuation); Frasier Meadows retirement community in south Boulder WUI zone; multiple assisted living facilities",
        },
    },

    # =========================================================================
    # 11. BRECKENRIDGE, CO (NEW)
    # =========================================================================
    "breckenridge_co": {
        "center": [39.4817, -106.0384],
        "terrain_notes": (
            "Breckenridge (9,600 ft) is a ski resort town in Summit County, 50 air miles "
            "west of Denver on the western slope of the Continental Divide. The town is "
            "almost entirely surrounded by the White River National Forest, with dense "
            "spruce-fir and lodgepole pine forests heavily impacted by mountain pine "
            "beetle extending from the valley floor to timberline at ~11,500 ft. The "
            "Peak 2 Fire (July 2017) demonstrated the community's vulnerability when an "
            "83-acre fire produced 100-ft flames racing toward the Peak 7 subdivision, "
            "forcing evacuation of 463+ homes. Summit County's biggest challenge is "
            "infrastructure — limited roadways restrict the ability to evacuate large "
            "volumes of people quickly. The county launched a Comprehensive Emergency "
            "Evacuation Assessment in 2024 to address this critical gap. During ski "
            "season and summer events, the town population can swell from ~5,000 to "
            "35,000+, with most visitors unfamiliar with fire evacuation procedures. "
            "I-70 through the Eisenhower Tunnel (11,158 ft) is the sole high-capacity "
            "route east."
        ),
        "key_features": [
            {"name": "Breckenridge Ski Resort / Peaks 6-10", "bearing": "W", "type": "ski_area",
             "notes": "12,998 ft summit; resort extends into dense timber; Peak 2 Fire burned between resort and Peak 7 neighborhood"},
            {"name": "White River National Forest", "bearing": "ALL", "type": "national_forest",
             "notes": "Surrounds town entirely; extensive beetle-kill lodgepole pine; spruce-fir crown fire potential; continuous fuel from wilderness to town boundary"},
            {"name": "Blue River / Dillon Reservoir", "bearing": "N", "type": "reservoir",
             "notes": "Denver Water supply reservoir 9 miles north; fire contamination of watershed would affect Denver metro water; 254,000 acre-ft capacity"},
            {"name": "Eisenhower-Johnson Memorial Tunnels", "bearing": "NE", "type": "infrastructure",
             "notes": "11,158 ft elevation; sole I-70 route through Continental Divide; closure isolates entire Summit County from Front Range; hazmat restrictions limit tunnel capacity"},
            {"name": "Boreas Pass", "bearing": "S", "type": "mountain_pass",
             "notes": "11,481 ft historic railroad pass; unpaved road to South Park; emergency-only alternative to I-70; not viable for mass evacuation"},
            {"name": "Peak 7 / Warriors Mark neighborhoods", "bearing": "NW", "type": "subdivision",
             "notes": "463+ homes evacuated during Peak 2 Fire; dense timber surrounds development; limited access roads"},
        ],
        "elevation_range_ft": [9530, 10200],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Peak 2 Fire", "year": 2017, "acres": 83,
             "details": "July 5; 100-ft flames; 463+ homes evacuated (Peak 7 neighborhood); Gold Hill and Silver Shekel under pre-evacuation; smokejumpers deployed; small acreage but extremely close to dense residential; caused widespread panic"},
            {"name": "Buffalo Fire", "year": 2018, "acres": 70,
             "details": "Campfire-caused fire near Breckenridge neighborhood; quickly contained; demonstrated ongoing human-caused ignition risk in heavily visited forest"},
        ],
        "evacuation_routes": [
            {"route": "CO-9 North to I-70 (Frisco)", "direction": "N", "lanes": 2,
             "bottleneck": "Two-lane road to Frisco (4 miles); merges with I-70 traffic at congested interchange",
             "risk": "Primary evacuation route; single road from Breckenridge to I-70; bottleneck at Frisco roundabouts; handles all Summit County south-valley traffic"},
            {"route": "I-70 East (Eisenhower Tunnel)", "direction": "E toward Denver", "lanes": 4,
             "bottleneck": "11,158 ft tunnel; already congests on normal ski weekends; hazmat restrictions; bore closures",
             "risk": "Sole route to Front Range; regular weekend traffic gridlock; fire evacuation of Summit County would overwhelm tunnel capacity"},
            {"route": "I-70 West (Vail Pass)", "direction": "W toward Vail/Grand Junction", "lanes": 4,
             "bottleneck": "10,662 ft Vail Pass; steep grades; truck traffic",
             "risk": "Western alternative but leads deeper into mountain communities, not to population centers"},
            {"route": "CO-9 South (Hoosier Pass)", "direction": "S toward Fairplay", "lanes": 2,
             "bottleneck": "11,539 ft pass; two-lane mountain road; winter closures; slow travel",
             "risk": "Emergency-only alternative; leads to South Park (rural); no significant services for 40+ miles"},
            {"route": "Boreas Pass Road", "direction": "SE", "lanes": 1,
             "bottleneck": "Unpaved; 11,481 ft; impassable in winter; ATV/4WD only in sections",
             "risk": "Not viable for mass evacuation; emergency-only for individual vehicles"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Valley winds channeled by Blue River drainage; afternoon upslope thermals; occasional strong westerlies over Continental Divide; less extreme than Front Range Chinook but significant in beetle-kill timber",
            "critical_corridors": [
                "Peak 2 / Tenmile Range — proven fire path toward Peak 7 residential",
                "Blue River corridor — continuous timber from Hoosier Pass to Dillon",
                "French Gulch / Lincoln Park — historic mining areas with regenerating beetle-kill forest",
                "Ski area glades — resort terrain intermixed with dense forest",
            ],
            "rate_of_spread_potential": "Extreme in beetle-kill timber; Peak 2 Fire demonstrated rapid uphill crown fire runs with 100-ft flame lengths; spruce-fir at higher elevations produces intense fire; steep terrain accelerates spread",
            "spotting_distance": "0.5-1 mile in beetle-kill stands; dead standing snags produce prolific embers; convection columns in mountain terrain create long-range lofting; embers can cross valley and ignite opposite slope",
        },
        "infrastructure_vulnerabilities": {
            "water_system": "Town of Breckenridge water from Goose Pasture Tarn and Blue River; forested watershed extremely vulnerable to fire contamination; Dillon Reservoir (Denver Water) at risk from large-scale fire; limited alternative water sources at 9,600+ ft",
            "power": "Xcel Energy; overhead lines through dense forest; mountain transmission vulnerable; extended outages likely during fire events; backup generation limited",
            "communications": "Cell coverage adequate in town but gaps on ski mountain and surrounding forest; terrain blocks signals in valleys; mountain communities north (Frisco, Silverthorne) share limited infrastructure",
            "medical": "St. Anthony Summit Medical Center (35 beds, Frisco); sole hospital for Summit County; limited trauma capability; helicopter medevac to Denver (weather-dependent at 9,500+ ft); golden hour challenging",
        },
        "demographics_risk_factors": {
            "population": 5078,
            "seasonal_variation": "Peak population 35,000+ during ski season and summer events; 1.6M annual skier visits; most visitors unfamiliar with fire risk and evacuation routes; large STR inventory means many overnight guests with zero local knowledge",
            "elderly_percentage": "9.2%",
            "mobile_homes": "Workforce housing crisis; some manufactured homes in Blue River area south of town; seasonal workers in shared housing",
            "special_needs_facilities": "St. Anthony Summit Medical Center (Frisco, 35 beds); Summit County Senior Center; many vacation rentals with guests including elderly and mobility-impaired visitors; language diversity among workforce",
        },
    },

    # =========================================================================
    # 1. COLORADO SPRINGS, CO
    # =========================================================================
    "colorado_springs_co": {
        "center": [38.8339, -104.8214],
        "terrain_notes": (
            "Colorado Springs sits at the base of Pikes Peak (14,115 ft) along the "
            "Front Range, with city elevations ranging from 5,706 ft in the northeast "
            "plains to 9,212 ft at The Horns on Cheyenne Mountain. The western edge of "
            "the city abuts Pike National Forest and the Rampart Range, creating one of "
            "the most extensive wildland-urban interfaces in the American West. Dense "
            "ponderosa pine and Douglas-fir forests in the foothills give way to Gambel "
            "oak and mountain shrub at mid-elevations, with grassland-scrub on the "
            "eastern plains. The Waldo Canyon fire (2012) and Black Forest fire (2013) "
            "demonstrated the city's extreme vulnerability on both its western (mountain) "
            "and northeastern (forest) flanks. Chinook downslope winds regularly produce "
            "gusts of 60-100 mph along the Front Range, rapidly desiccating fuels and "
            "driving fire runs. The city's North Slope Pikes Peak watersheds provide "
            "approximately 15% of drinking water; the Waldo Canyon burn scar continues "
            "to threaten water quality with post-fire debris flows."
        ),
        "key_features": [
            {"name": "Pikes Peak", "bearing": "W", "type": "mountain",
             "notes": "14,115 ft, dominant topographic feature; orographic effects drive downslope winds"},
            {"name": "Waldo Canyon Burn Scar", "bearing": "NW", "type": "burn_scar",
             "notes": "18,247-acre 2012 burn scar; ongoing debris flow and flooding risk to Manitou/west COS"},
            {"name": "Black Forest", "bearing": "NE", "type": "forest_wui",
             "notes": "Dense ponderosa pine WUI community; 14,280-acre 2013 fire destroyed 486+ homes"},
            {"name": "Garden of the Gods", "bearing": "W", "type": "park",
             "notes": "Sandstone formations at WUI boundary; fuel break between city and foothills"},
            {"name": "Cheyenne Mountain", "bearing": "SW", "type": "mountain",
             "notes": "9,212 ft summit; NORAD complex; steep terrain with heavy timber"},
            {"name": "North Slope Pikes Peak Watershed", "bearing": "NW", "type": "watershed",
             "notes": "Critical drinking water infrastructure; reservoirs at risk from wildfire"},
            {"name": "Air Force Academy", "bearing": "N", "type": "military",
             "notes": "18,500 acres of mixed forest and grassland; buffer zone but also fire risk"},
        ],
        "elevation_range_ft": [5706, 9212],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Waldo Canyon Fire", "year": 2012, "acres": 18247,
             "details": "Started June 23 in Rampart Range; 347 homes destroyed, 2 fatalities; 32,000+ evacuated; $353M damage; wind-driven firestorm overran Mountain Shadows subdivision in hours"},
            {"name": "Black Forest Fire", "year": 2013, "acres": 14280,
             "details": "Started June 11 NE of city; 486-511 homes destroyed, 2 fatalities; was most destructive CO fire until Marshall; $85M+ property damage; 100F temps on ignition day"},
            {"name": "Waldo Canyon area fires", "year": 2022, "acres": 5,
             "details": "Recurring small ignitions in Waldo Canyon area demonstrate ongoing risk in recovering burn scar zone"},
        ],
        "evacuation_routes": [
            {"route": "I-25", "direction": "N/S", "lanes": 6,
             "bottleneck": "Interchanges at Cimarron/Bijou; merges with US-24 traffic",
             "risk": "Primary regional evacuation corridor; congestion from 480K+ metro population"},
            {"route": "US-24 West (Ute Pass)", "direction": "W", "lanes": 4,
             "bottleneck": "Narrows to 2 lanes through Ute Pass canyon above Manitou Springs",
             "risk": "Single western evacuation route; canyon terrain limits capacity; closure during Waldo Canyon forced all traffic east"},
            {"route": "CO-83 (Academy Blvd extension)", "direction": "N", "lanes": 2,
             "bottleneck": "Two-lane road through Black Forest area",
             "risk": "Passes through highest-risk WUI zone; road closures during Black Forest Fire isolated neighborhoods"},
            {"route": "CO-115 South", "direction": "S", "lanes": 4,
             "bottleneck": "Single corridor south along Fort Carson boundary",
             "risk": "Limited alternatives if fire approaches from Cheyenne Mountain area"},
            {"route": "US-24 East / CO-94", "direction": "E", "lanes": 4,
             "bottleneck": "Plains routes; minimal bottlenecks",
             "risk": "Best evacuation options but require traversing city to reach from western WUI"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Chinook/downslope westerlies 40-100 mph; also afternoon upslope thunderstorm outflows",
            "critical_corridors": [
                "Queens Canyon to Mountain Shadows (Waldo Canyon fire path)",
                "Black Forest northeast corridor along CO-83",
                "Cheyenne Canyon south to Broadmoor",
                "Ute Pass / Fountain Creek corridor from Manitou Springs",
            ],
            "rate_of_spread_potential": "Extreme in downslope wind events; Waldo Canyon firestorm moved 3+ miles in 1 hour through Mountain Shadows; Black Forest fire consumed 8,000 acres in first 24 hours",
            "spotting_distance": "0.5-1.5 miles in Chinook events; ember transport into suburban neighborhoods documented in both Waldo Canyon and Black Forest fires",
        },
        "infrastructure_vulnerabilities": {
            "water_system": "North Slope Pikes Peak reservoirs provide 15% of supply; Waldo Canyon burn scar threatens water quality; dual-source system (Homestake + Blue River) provides redundancy but mountain infrastructure at risk",
            "power": "Xcel Energy distribution; mountain transmission lines through fire-prone corridors; 2012 Waldo Canyon caused widespread outages in western COS",
            "communications": "Cell towers on Cheyenne Mountain and Pikes Peak slopes; smoke interference during major events; Mountain Shadows lost communications during 2012 firestorm",
            "medical": "UCHealth Memorial (level 1 trauma), Penrose-St. Francis; adequate hospital capacity but western-side evacuees must cross city to reach facilities",
        },
        "demographics_risk_factors": {
            "population": 478961,
            "seasonal_variation": "Tourism adds 50K+ visitors in summer; Pikes Peak Highway, Garden of the Gods attract peak crowds during fire season",
            "elderly_percentage": "13.8%",
            "mobile_homes": "Moderate concentration in eastern plains areas and Fountain/Security-Widefield",
            "special_needs_facilities": "Multiple senior living complexes in western WUI zone including Cedar Heights area; VA hospital; 5 major hospital campuses",
        },
    },

    # =========================================================================
    # 8. DURANGO, CO
    # =========================================================================
    "durango_co": {
        "center": [37.2753, -107.8801],
        "terrain_notes": (
            "Durango sits at 6,512 ft in the Animas River valley in southwestern "
            "Colorado, surrounded by the San Juan National Forest and the San Juan "
            "Mountains. The terrain rises steeply from the river valley to peaks "
            "exceeding 13,000 ft. Dense mixed-conifer forests (ponderosa pine, Douglas-fir, "
            "white fir, spruce-fir at higher elevations) cover the surrounding mountains. "
            "Durango has experienced two of Colorado's most significant wildfires: the "
            "Missionary Ridge Fire (2002, 73,000 acres, 46 structures) which burned "
            "northeast of town, and the 416 Fire (2018, 54,130 acres) started by the "
            "Durango & Silverton Narrow Gauge Railroad. US-550 north (to Silverton) "
            "passes through Hermosa Creek and the Animas Valley — both fires forced "
            "closures of this sole northern route. The region's economy depends heavily "
            "on tourism (D&SNGRR, Mesa Verde NP, skiing), making fire season economically "
            "devastating even when structures are spared."
        ),
        "key_features": [
            {"name": "Missionary Ridge", "bearing": "NE", "type": "ridge",
             "notes": "Site of 2002 fire (73,000 acres); steep terrain NE of city; post-fire debris flows into Animas River tributaries"},
            {"name": "US-550 / Hermosa Creek corridor", "bearing": "N", "type": "highway_corridor",
             "notes": "Sole northern route to Silverton/Purgatory; closed during both 2002 and 2018 fires; 1,300+ homes evacuated in 2018"},
            {"name": "D&SNGRR Railroad", "bearing": "N", "type": "railroad",
             "notes": "Coal-fired narrow gauge railroad; ignited 416 Fire (2018); historic but fire-causing asset; spark arrestor improvements made post-2018"},
            {"name": "Animas River valley", "bearing": "N/S", "type": "river_valley",
             "notes": "Primary corridor through town; post-fire flooding risk; Gold King Mine spill (2015) already impacted river"},
            {"name": "Purgatory Resort", "bearing": "N", "type": "ski_area",
             "notes": "25 miles north on US-550; 416 Fire burned adjacent to resort; evacuated; single road access"},
            {"name": "Mesa Verde National Park", "bearing": "W", "type": "national_park",
             "notes": "36 miles west; major tourism driver; fire-adapted pinyon-juniper woodland; Bircher Fire (2000) and others have burned in park"},
        ],
        "elevation_range_ft": [6512, 8000],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Missionary Ridge Fire", "year": 2002, "acres": 73000,
             "details": "June 9-July 15; 46 homes/cabins destroyed; 1 firefighter fatality; $37M suppression; 2,000+ firefighters; burned NE of Durango in steep terrain; post-fire debris flows damaged additional homes"},
            {"name": "416 Fire", "year": 2018, "acres": 54130,
             "details": "June 1-July 31; ignited by D&SNGRR coal train; 6th largest CO fire at time; 0 structures destroyed but 1,300+ homes evacuated; US-550 closed repeatedly; devastating economic impact on tourism; two 500-year-old champion trees killed"},
            {"name": "East Animas Fire", "year": 2023, "acres": 50,
             "details": "Small but concerning fire in East Animas area demonstrating ongoing ignition risk in residential WUI"},
        ],
        "evacuation_routes": [
            {"route": "US-550 North", "direction": "N to Silverton", "lanes": 2,
             "bottleneck": "Two-lane mountain highway; Hermosa Creek narrows; Coal Bank/Molas passes above 10,000 ft",
             "risk": "Closed during both 2002 and 2018 fires; sole northern route; fire or avalanche makes it impassable; dead-end route if fire blocks both directions"},
            {"route": "US-550 South / US-160 East", "direction": "S/E", "lanes": 2,
             "bottleneck": "US-160 is primary escape route east to Pagosa Springs (60 mi) or south to New Mexico",
             "risk": "Best evacuation option; two-lane through mountain terrain; 60+ miles to next significant town"},
            {"route": "US-160 West", "direction": "W to Cortez", "lanes": 2,
             "bottleneck": "Mancos Hill; two-lane through La Plata Mountains",
             "risk": "Alternative western route; 36 miles to Cortez; passes through fire-prone pinyon-juniper"},
            {"route": "CO-145 / Lizard Head Pass", "direction": "NW to Telluride", "lanes": 2,
             "bottleneck": "Remote mountain pass at 10,222 ft; narrow; seasonal concerns",
             "risk": "Emergency alternate when US-550N closed; very limited capacity; adds hours to northbound travel"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Diurnal upslope/downslope mountain winds; southwest monsoon thunderstorm outflows; foehn-type warm dry winds from west; valley channeling along Animas River",
            "critical_corridors": [
                "Hermosa Creek / US-550 corridor — both major fires burned along this axis",
                "Missionary Ridge — steep NE slopes above Lemon Reservoir and Vallecito",
                "Junction Creek — drainage running west from town into national forest",
                "Animas River valley — fire and post-fire debris flow corridor",
            ],
            "rate_of_spread_potential": "High to extreme on steep terrain; Missionary Ridge fire made major runs on multiple days; 416 Fire burned in steep, inaccessible terrain making suppression extremely difficult; mixed-conifer crown fire potential",
            "spotting_distance": "0.5-1 mile typical; steep terrain and strong thermals loft embers; D&SNGRR spark ignitions documented miles from tracks along corridor",
        },
        "infrastructure_vulnerabilities": {
            "water_system": "City of Durango water from Florida River and Animas River; Lemon Reservoir threatened during Missionary Ridge Fire; post-fire debris flows contaminate water sources; limited treatment capacity for turbid water",
            "power": "La Plata Electric Association (co-op); overhead lines through mountain terrain; extended outages during fires; single transmission feed from north (via US-550 corridor)",
            "communications": "Cell coverage limited in surrounding mountains; terrain blocks signals in valleys; radio repeaters on mountain peaks vulnerable; Missionary Ridge Fire disrupted communications infrastructure",
            "medical": "Mercy Regional Medical Center (82 beds); sole hospital for 55,000+ service area covering La Plata, San Juan, and parts of Archuleta counties; helicopter medevac to Grand Junction or Albuquerque for trauma",
        },
        "demographics_risk_factors": {
            "population": 19071,
            "seasonal_variation": "Tourism doubles population in summer; D&SNGRR, Mesa Verde NP, Purgatory Resort draw 2M+ visitors/year; Fort Lewis College adds 3,500 students; many seasonal workers in tourism industry",
            "elderly_percentage": "14.7%",
            "mobile_homes": "Moderate presence in Animas Valley and surrounding unincorporated La Plata County; manufactured homes in fire-prone areas",
            "special_needs_facilities": "Mercy Regional Medical Center (82 beds); Fort Lewis College (3,500 students); Pine River Senior Center; rural elderly population in WUI areas often resist evacuation",
        },
    },

    # =========================================================================
    # 5. ESTES PARK, CO
    # =========================================================================
    "estes_park_co": {
        "center": [40.3772, -105.5217],
        "terrain_notes": (
            "Estes Park is a mountain town at 7,522 ft elevation in a broad valley "
            "at the eastern entrance to Rocky Mountain National Park. The town is "
            "surrounded on three sides by mountains reaching 12,000-14,000 ft, with "
            "dense lodgepole pine, ponderosa pine, and Douglas-fir forests. In October "
            "2020, the town faced simultaneous threats from the Cameron Peak Fire "
            "(approaching from the northwest) and the East Troublesome Fire (approaching "
            "from the west through RMNP after crossing the Continental Divide). The "
            "entire Estes Valley was evacuated on October 22, 2020 — approximately "
            "10,000 residents and visitors fled through only two viable routes. A "
            "snowstorm on October 25 likely saved the town from catastrophic destruction. "
            "The Big Thompson Canyon (US-34) provides the primary eastern access but is "
            "historically vulnerable to flash flooding (144 killed in 1976 flood) and "
            "fire simultaneously."
        ),
        "key_features": [
            {"name": "Rocky Mountain National Park", "bearing": "W/N/S", "type": "national_park",
             "notes": "Surrounds town on three sides; East Troublesome burned 30,000 acres of RMNP; dense timber fuel loads"},
            {"name": "Big Thompson Canyon / US-34", "bearing": "E", "type": "canyon_road",
             "notes": "Primary eastern access; narrow canyon; 1976 flood killed 144; simultaneous flood-fire risk"},
            {"name": "Lake Estes / Olympus Dam", "bearing": "E", "type": "reservoir",
             "notes": "Town water supply; Colorado-Big Thompson Project infrastructure; dam breach risk if fire damages watershed"},
            {"name": "Fall River / US-34 West (Trail Ridge Road)", "bearing": "W", "type": "mountain_pass",
             "notes": "Western route into RMNP; seasonal closure; 12,183 ft pass; only western escape route"},
            {"name": "Cameron Peak burn scar", "bearing": "NW", "type": "burn_scar",
             "notes": "208,663-acre burn scar NW of town; post-fire debris flow and flooding risk"},
            {"name": "Moraine Park / Bear Lake corridor", "bearing": "SW", "type": "park_valley",
             "notes": "East Troublesome fire reached Moraine Park area; popular visitor area; heavy fuel loads"},
        ],
        "elevation_range_ft": [7500, 8600],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "East Troublesome Fire", "year": 2020, "acres": 193812,
             "details": "Started Oct 14 near Kremmling; burned 100K+ acres Oct 21 alone (6,000 acres/hour); crossed Continental Divide into RMNP; forced total Estes Park evacuation Oct 22; 555 structures destroyed overall; snowstorm saved town Oct 25"},
            {"name": "Cameron Peak Fire", "year": 2020, "acres": 208663,
             "details": "Largest CO fire; burned Aug-Dec 2020 NW of Estes Park; forced evacuation of 20,000+ mountain residents; 469 structures destroyed; threatened Estes Park from northwest simultaneously with East Troublesome"},
            {"name": "Fern Lake Fire", "year": 2012, "acres": 3500,
             "details": "Burned in RMNP Oct 2012-Jan 2013; demonstrated fire risk within the park adjacent to town"},
        ],
        "evacuation_routes": [
            {"route": "US-34 East (Big Thompson Canyon)", "direction": "E to Loveland", "lanes": 2,
             "bottleneck": "Narrow mountain canyon; single lane each direction; no passing; 25 miles to plains",
             "risk": "Historically deadly (1976 flood); canyon fire could trap evacuees; only viable year-round eastern route"},
            {"route": "US-36 South (to Lyons/Boulder)", "direction": "SE", "lanes": 2,
             "bottleneck": "Mountain road through narrow valleys; 20+ miles to plains",
             "risk": "Secondary route; passes through fire-prone foothill forests; can be cut off by fire"},
            {"route": "Trail Ridge Road / US-34 West", "direction": "W", "lanes": 2,
             "bottleneck": "12,183 ft pass; closed Oct-May typically; not available during fall fire season",
             "risk": "Seasonal road; was closed during Oct 2020 fires; leads into fire zone (Grand Lake side was burning)"},
            {"route": "CO-7 South (Peak to Peak)", "direction": "S", "lanes": 2,
             "bottleneck": "Narrow mountain road; connects to Allenspark, Raymond, Nederland",
             "risk": "Remote mountain route; limited capacity; also in fire-prone terrain"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Westerly Chinook winds up to 60+ mph; upslope afternoon thunderstorm winds; channeled through valley corridors; East Troublesome driven by 120 mph gusts at Continental Divide",
            "critical_corridors": [
                "Fall River valley — East Troublesome fire path from west",
                "Big Thompson corridor — fire and flood dual hazard",
                "Moraine Park / Glacier Creek — dense timber corridor into town",
                "Fish Creek / Lily Lake area — southern approach through continuous forest",
            ],
            "rate_of_spread_potential": "Extreme; East Troublesome burned at 6,000 acres/hour during wind event; crown fire runs in lodgepole pine; fire crossed 2-mile rocky Continental Divide",
            "spotting_distance": "2+ miles; East Troublesome produced pyrocumulonimbus columns generating long-range spot fires; embers lofted over Continental Divide",
        },
        "infrastructure_vulnerabilities": {
            "water_system": "Town water from Lake Estes (Olympus Dam); Colorado-Big Thompson Project; Cameron Peak burn scar threatens watershed with sediment/debris; water treatment plant capacity limited for emergency demand",
            "power": "Estes Park Power & Communications (municipal utility); overhead lines through forested corridors; power lost during Oct 2020 evacuations; single transmission feed from plains",
            "communications": "Limited cell coverage in surrounding mountains; municipal broadband helps but towers vulnerable; radio repeaters on mountain peaks at fire risk; lost communications hampered 2020 evacuation",
            "medical": "Estes Park Health (critical access hospital, 25 beds); limited capacity; patients must be transferred to Loveland/Fort Collins for serious injuries; hospital evacuated in 2020",
        },
        "demographics_risk_factors": {
            "population": 6304,
            "seasonal_variation": "4.4 million RMNP visitors annually; summer population can exceed 25,000-30,000; many visitors unfamiliar with evacuation routes; short-term rental occupants particularly vulnerable",
            "elderly_percentage": "28.5% (retirement community character)",
            "mobile_homes": "Several mobile home parks in Estes Valley; high vulnerability",
            "special_needs_facilities": "Estes Park Health (25 beds, evacuated 2020); multiple senior living facilities; many elderly residents with limited mobility chose not to evacuate in 2020",
        },
    },

    # =========================================================================
    # 7. EVERGREEN / CONIFER, CO
    # =========================================================================
    "evergreen_conifer_co": {
        "center": [39.6333, -105.3172],
        "terrain_notes": (
            "Evergreen and Conifer are unincorporated mountain communities in western "
            "Jefferson County, at 7,000-8,500 ft elevation in the Front Range foothills "
            "19 miles west of Denver. The area ranks #1 in Colorado and top-10 nationally "
            "for catastrophic wildfire risk with potential for significant loss of life. "
            "Evergreen ranks higher than 99% of US communities for wildfire risk. The "
            "terrain is characterized by steep, narrow canyons (Bear Creek, Turkey Creek, "
            "Cub Creek) with dense ponderosa pine, Douglas-fir, and lodgepole pine "
            "forests heavily impacted by mountain pine beetle. Jefferson County has the "
            "most homes in high/extreme wildfire risk areas of any Colorado county. "
            "Development follows canyon roads with limited egress points, and many "
            "properties are accessed by single-lane gravel roads. The I-70 corridor "
            "runs along the northern boundary but is separated from most development "
            "by steep terrain."
        ),
        "key_features": [
            {"name": "Bear Creek Canyon", "bearing": "C", "type": "canyon_wui",
             "notes": "Primary canyon through Evergreen; CO-74 follows creek; dense residential development on steep slopes; single-road access for many neighborhoods"},
            {"name": "Conifer Mountain", "bearing": "SW", "type": "mountain_wui",
             "notes": "7,800-8,500 ft; scattered residential in heavy timber; US-285 corridor at base"},
            {"name": "Evergreen Lake / Downtown", "bearing": "C", "type": "town_center",
             "notes": "Commercial center in narrow valley; traffic bottleneck at CO-74/CO-73 junction"},
            {"name": "I-70 corridor", "bearing": "N", "type": "highway",
             "notes": "Major interstate 5-8 miles north; separated by steep terrain; not directly accessible from most neighborhoods"},
            {"name": "Mount Evans / Chicago Creek", "bearing": "W", "type": "wilderness",
             "notes": "14,265 ft peak; alpine and subalpine forests provide continuous fuel to mountain communities"},
            {"name": "Elk Meadow / Bergen Park", "bearing": "NE", "type": "open_space",
             "notes": "Jefferson County open space; grassland-forest transition; potential fire corridor toward Denver suburbs"},
        ],
        "elevation_range_ft": [6800, 8600],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Lower North Fork Fire", "year": 2012, "acres": 1410,
             "details": "March prescribed burn reignition; 3 fatalities; 27 homes destroyed near Conifer; demonstrated early-season fire risk in beetle-kill timber"},
            {"name": "Elephant Butte Fire", "year": 2002, "acres": 3000,
             "details": "Burned near Evergreen; homes threatened; demonstrated WUI vulnerability of mountain communities"},
            {"name": "Hi Meadow Fire", "year": 2000, "acres": 10800,
             "details": "58 structures destroyed near Bailey/Conifer area; early indicator of growing WUI risk in Jefferson/Park County foothills"},
        ],
        "evacuation_routes": [
            {"route": "CO-74 (Bear Creek Canyon)", "direction": "E to Morrison / W to Kittredge", "lanes": 2,
             "bottleneck": "Narrow canyon road; single lane each direction; winding; school zone in Evergreen",
             "risk": "Primary Evergreen evacuation route; canyon fire could trap thousands; bottleneck at CO-74/CO-73 junction handles all traffic"},
            {"route": "CO-73 (Evergreen Parkway)", "direction": "N to I-70 / S to Conifer", "lanes": 2,
             "bottleneck": "Mountain road connecting to I-70 at El Rancho; steep grades; curves",
             "risk": "Sole connection to I-70 for most Evergreen residents; fire on either side blocks route"},
            {"route": "US-285", "direction": "SW to Fairplay / NE to Denver", "lanes": 4,
             "bottleneck": "Four-lane divided highway but access requires traversing Conifer area roads",
             "risk": "Good capacity once reached; Conifer residents' primary route; Turkey Creek Canyon section is constrained"},
            {"route": "Squaw Pass Road / CO-103", "direction": "W to Idaho Springs", "lanes": 2,
             "bottleneck": "Remote mountain road; steep; unpaved sections; seasonal",
             "risk": "Emergency alternative to I-70; very limited capacity; impassable in winter"},
            {"route": "Brook Forest Road / Upper Bear Creek", "direction": "W", "lanes": 2,
             "bottleneck": "Narrow residential roads; dead-end or loop configurations",
             "risk": "Many neighborhoods have single access point; evacuation creates convergence on main roads"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Channeled Chinook winds through canyons; up-canyon afternoon thermals; complex terrain creates erratic fire behavior; 40-70 mph gusts common in canyon corridors",
            "critical_corridors": [
                "Bear Creek Canyon — dense timber corridor connecting mountain communities to Morrison/Denver suburbs",
                "Turkey Creek Canyon (US-285) — fire corridor toward Conifer/Bailey",
                "Mount Evans / Chicago Creek — continuous alpine-to-foothill fuel",
                "Cub Creek / Brook Forest — dead-end canyons with trapped populations",
            ],
            "rate_of_spread_potential": "Extreme; steep terrain and beetle-kill timber enable rapid crown fire runs; canyon winds accelerate fire; Lower North Fork Fire demonstrated 3 fatalities from rapid fire movement in beetle-kill",
            "spotting_distance": "0.5-1.5 miles; canyon updrafts loft embers; beetle-kill dead standing timber produces intense ember showers; structures in heavy timber ignite from ember accumulation on roofs/decks",
        },
        "infrastructure_vulnerabilities": {
            "water_system": "Evergreen Metropolitan District; wells and surface water; limited fire hydrant coverage in rural areas; many homes on private wells with no hydrant access; fire suppression relies heavily on tanker shuttles",
            "power": "Xcel Energy; overhead lines on wooden poles through heavy timber; frequent fire-season outages; downed lines are ignition source",
            "communications": "Cell coverage inconsistent in canyons; terrain blocks signals; Jefferson County reverse-911 is primary alert system; radio dead spots in narrow valleys",
            "medical": "No hospital in Evergreen or Conifer; nearest is St. Anthony (Lakewood, 30+ min) or Lutheran (Wheat Ridge); critical access gap for 26,000+ residents; EMS response times 15-45 min in remote areas",
        },
        "demographics_risk_factors": {
            "population": 24284,
            "seasonal_variation": "Mountain recreation draws Denver metro visitors year-round; Evergreen Lake skating/fishing; summer hiking peaks; some seasonal/vacation homes",
            "elderly_percentage": "18.2%",
            "mobile_homes": "Some manufactured homes in rural areas; particularly vulnerable to wildfire",
            "special_needs_facilities": "No hospital; limited medical facilities; senior population in remote locations; many homes not ADA accessible; narrow driveways impede emergency vehicle access",
        },
    },

    # =========================================================================
    # 6. FORT COLLINS, CO
    # =========================================================================
    "fort_collins_co": {
        "center": [40.5853, -105.0844],
        "terrain_notes": (
            "Fort Collins sits at approximately 5,003 ft elevation at the mouth of the "
            "Cache la Poudre River canyon, where the Front Range meets the northern "
            "Colorado plains. The Poudre Canyon (CO-14) extends 60+ miles west into "
            "the Roosevelt National Forest and Arapaho National Forest, creating a "
            "continuous fuel corridor from remote wilderness to the city's western edge. "
            "The Cameron Peak Fire (2020) — the largest wildfire in Colorado history at "
            "208,663 acres — burned for nearly 4 months in the Poudre watershed, "
            "threatening the city's primary water supply. Fort Collins relies on a "
            "dual water system: the Poudre River and Horsetooth Reservoir (Colorado-Big "
            "Thompson Project). Post-fire debris flows from the Cameron Peak burn scar "
            "continue to degrade Poudre River water quality. The city's western foothill "
            "communities (Horsetooth, Rist Canyon, Glacier View Meadows, Bellvue) "
            "represent significant WUI exposure with limited-access mountain roads."
        ),
        "key_features": [
            {"name": "Poudre Canyon / CO-14", "bearing": "W", "type": "canyon_corridor",
             "notes": "60+ mile canyon with scattered residential development; Cameron Peak Fire corridor; single road access to mountain communities"},
            {"name": "Horsetooth Reservoir", "bearing": "W", "type": "reservoir",
             "notes": "Water supply for 220,000+ people; C-BT Project infrastructure; surrounded by WUI development on hogback ridges"},
            {"name": "Cameron Peak burn scar", "bearing": "W/NW", "type": "burn_scar",
             "notes": "208,663-acre scar; post-fire debris flows threaten Poudre water quality; ongoing sediment loading"},
            {"name": "Lory State Park / Horsetooth Mountain", "bearing": "W", "type": "park",
             "notes": "Foothill open space at WUI boundary; heavy recreational use; fire ignition risk from users"},
            {"name": "Red Feather Lakes", "bearing": "NW", "type": "mountain_community",
             "notes": "Remote mountain community evacuated during Cameron Peak Fire; single road access; beetle-kill timber"},
            {"name": "CSU Mountain Campus", "bearing": "W", "type": "educational",
             "notes": "Colorado State University facility in Pingree Park; evacuated during Cameron Peak Fire"},
        ],
        "elevation_range_ft": [4982, 5500],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Cameron Peak Fire", "year": 2020, "acres": 208663,
             "details": "Largest CO fire in history; started Aug 13 near Chambers Lake; contained Dec 2; 469 structures destroyed (42 primary residences); 20,000+ evacuated; $134M suppression cost; threatened Fort Collins water supply"},
            {"name": "High Park Fire", "year": 2012, "acres": 87284,
             "details": "Started June 9 in Poudre Canyon; 259 homes destroyed; 1 fatality; at time was 3rd largest CO fire; burned in beetle-kill timber; severe post-fire flooding"},
            {"name": "Hewlett Gulch Fire", "year": 2012, "acres": 7685,
             "details": "April fire in Poudre Canyon; rapid early-season fire in dry conditions; preceded High Park by 2 months"},
        ],
        "evacuation_routes": [
            {"route": "I-25", "direction": "N/S", "lanes": 6,
             "bottleneck": "Primary regional corridor; congestion at Harmony/Prospect interchanges",
             "risk": "Serves 170K+ city and surrounding communities; viable for plains-side evacuation"},
            {"route": "US-287", "direction": "N to Laramie / S to Loveland", "lanes": 4,
             "bottleneck": "College Avenue through city; signal-controlled intersections",
             "risk": "Secondary N/S route; passes through city center with potential congestion"},
            {"route": "CO-14 (Poudre Canyon)", "direction": "W", "lanes": 2,
             "bottleneck": "Narrow mountain canyon; single lane each direction; 60+ miles with no alternatives",
             "risk": "Only access for canyon communities; fire or rockfall closes entire corridor; 6,000+ canyon residents with single egress"},
            {"route": "CO-392 / Harmony Road", "direction": "E", "lanes": 4,
             "bottleneck": "Eastern plains route; minimal constraints",
             "risk": "Best mass evacuation corridor; grassland fire risk similar to Marshall Fire scenario"},
            {"route": "Rist Canyon Road / Stove Prairie Road", "direction": "W", "lanes": 2,
             "bottleneck": "Narrow mountain roads; hairpin turns; no shoulders",
             "risk": "Secondary mountain access; easily cut off by fire; used as alternative when CO-14 closed"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Chinook downslope winds from west 40-80+ mph; also afternoon upslope thunderstorm winds; Poudre Canyon channeling amplifies wind speed",
            "critical_corridors": [
                "Poudre Canyon — continuous timber fuel from wilderness to city",
                "Horsetooth hogback — WUI corridor along reservoir's eastern shore",
                "Rist Canyon — mountain community with single road",
                "Grassland interface on eastern/northern city edges (Marshall Fire-type risk)",
            ],
            "rate_of_spread_potential": "High to extreme; Cameron Peak Fire exploded from 24K to 96K acres in single wind event; High Park Fire burned 60K acres in first week; beetle-kill timber enables rapid crown fire runs",
            "spotting_distance": "1-2 miles in canyon wind events; Cameron Peak documented long-range spotting across ridges; ember production extreme in beetle-kill stands",
        },
        "infrastructure_vulnerabilities": {
            "water_system": "Dual source: Poudre River (Michigan Ditch provides 11% of supply, runs through Cameron Peak burn scar) and Horsetooth Reservoir (C-BT Project, 220K+ users); post-fire sediment and ash contaminate Poudre for years; can shift to Horsetooth during contamination events",
            "power": "Platte River Power Authority; overhead transmission through Poudre Canyon vulnerable to fire; mountain communities lose power frequently during fire events",
            "communications": "Good coverage in city; mountain communities (Red Feather, Livermore, Crystal Lakes) have limited cell service; radio repeaters on peaks vulnerable to fire",
            "medical": "UCHealth Poudre Valley Hospital (level 2 trauma, 340 beds); Banner Fort Collins Medical Center; adequate urban capacity but mountain communities 30-60+ min from hospitals",
        },
        "demographics_risk_factors": {
            "population": 169810,
            "seasonal_variation": "CSU adds 33,000 students; Poudre Canyon recreation peaks in summer; Horsetooth Reservoir draws heavy summer crowds; mountain STRs increase seasonal population",
            "elderly_percentage": "11.5%",
            "mobile_homes": "Several mobile home parks in city and Laporte area; Poudre Canyon has manufactured homes",
            "special_needs_facilities": "CSU campus (33K students); Poudre Valley Hospital; Columbine Health System senior facilities; mountain communities include elderly residents with limited mobility who resisted evacuation in 2020",
        },
    },

    # =========================================================================
    # 9. GLENWOOD SPRINGS, CO
    # =========================================================================
    "glenwood_springs_co": {
        "center": [39.5505, -107.3248],
        "terrain_notes": (
            "Glenwood Springs (5,761 ft) occupies a narrow valley at the confluence of "
            "the Colorado River and Roaring Fork River, pinched between steep canyon walls "
            "on all sides. To the east, Glenwood Canyon is a dramatic 1,800-ft-deep gorge "
            "carrying I-70 — the most critical east-west highway in Colorado. The Grizzly "
            "Creek Fire (2020, 32,631 acres) burned directly through this canyon, forcing "
            "a 13-day I-70 closure that severed the state's primary transportation artery. "
            "The fire threatened the Shoshone Hydroelectric Generating Station (15 MW, "
            "built 1909), which holds foundational water rights on the upper Colorado River. "
            "The town is also accessible via CO-82 south to Aspen through the Roaring Fork "
            "Valley. The surrounding White River National Forest contains extensive "
            "beetle-kill timber and dense mixed-conifer forests on steep slopes."
        ),
        "key_features": [
            {"name": "Glenwood Canyon / I-70", "bearing": "E", "type": "canyon_highway",
             "notes": "1,800-ft deep canyon; I-70 most expensive interstate section ever built (40 bridges, 3 tunnels); 13-day closure during 2020 fire; subsequent mudslides from burn scar closed I-70 repeatedly in 2021"},
            {"name": "Shoshone Hydroelectric Station", "bearing": "E", "type": "power_plant",
             "notes": "15 MW plant built 1909; holds senior water rights on upper Colorado River; threatened by Grizzly Creek Fire; loss would affect entire Colorado River Compact water allocation"},
            {"name": "Colorado River confluence", "bearing": "C", "type": "river",
             "notes": "Colorado and Roaring Fork rivers meet at town; post-fire debris flows affect water quality; rafting/recreation economy dependent on water quality"},
            {"name": "Iron Mountain", "bearing": "S", "type": "mountain",
             "notes": "Steep south-facing slope directly above downtown; dense vegetation; fire on Iron Mountain would directly threaten town center"},
            {"name": "Storm King Mountain", "bearing": "W", "type": "memorial",
             "notes": "Site of 1994 South Canyon Fire where 14 firefighters died; steep terrain with Gambel oak; memorial site; demonstrates extreme fire behavior potential near town"},
            {"name": "No Name area / Hanging Lake", "bearing": "E", "type": "recreation",
             "notes": "Popular recreation area in Glenwood Canyon; Grizzly Creek Fire burned through area; fragile ecosystem impacted"},
        ],
        "elevation_range_ft": [5761, 7500],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Grizzly Creek Fire", "year": 2020, "acres": 32631,
             "details": "Aug 10-Dec 18 2020; human-caused; burned through Glenwood Canyon; 13-day I-70 closure; threatened Shoshone generating station; largest fire in White River NF history; evacuations in No Name and other canyon areas"},
            {"name": "South Canyon Fire (Storm King Mountain)", "year": 1994, "acres": 2115,
             "details": "July 6; 14 firefighters killed (9 Prineville Hotshots, 4 smokejumpers, 1 helitack); Gambel oak blowup on steep terrain; one of deadliest US wildfire disasters; occurred 7 miles west of Glenwood Springs"},
            {"name": "Coal Seam Fire", "year": 2002, "acres": 12209,
             "details": "June 2002; burned from underground coal seam ignition south of town; 43 homes destroyed; fire entered neighborhoods; demonstrated urban fire risk from geologic sources"},
        ],
        "evacuation_routes": [
            {"route": "I-70 East (Glenwood Canyon)", "direction": "E toward Vail/Denver", "lanes": 4,
             "bottleneck": "Canyon highway; 13-day closure in 2020; mudslides from burn scar closed it repeatedly in 2021",
             "risk": "Most critical CO transportation corridor; no viable alternative for east-west travel when closed; closure costs CO economy millions per day"},
            {"route": "I-70 West", "direction": "W toward Grand Junction", "lanes": 4,
             "bottleneck": "Canyon de Beque; fewer constraints than Glenwood Canyon",
             "risk": "Viable western evacuation; 85 miles to Grand Junction; less fire-constrained"},
            {"route": "CO-82 South (Roaring Fork Valley)", "direction": "S to Aspen/Carbondale", "lanes": 2,
             "bottleneck": "Two-lane road through Roaring Fork Valley; Carbondale congestion; dead-end at Aspen",
             "risk": "Leads deeper into mountains, not to safety; CO-82 itself passes through fire-prone terrain"},
            {"route": "CO-13 North", "direction": "N to Rifle/Meeker", "lanes": 2,
             "bottleneck": "Two-lane mountain road; remote",
             "risk": "Low-capacity alternative; long detour for eastbound travel when I-70 closed"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Canyon winds — channeled by Glenwood Canyon and Roaring Fork Valley; diurnal up-canyon/down-canyon flow; foehn-type drying events; afternoon thermal wind reversals create erratic behavior",
            "critical_corridors": [
                "Glenwood Canyon — fire runs along steep canyon walls; I-70 infrastructure at risk",
                "Iron Mountain — steep slope directly above downtown; south-facing, rapid drying",
                "Storm King Mountain — Gambel oak blowup terrain; proven lethal fire behavior",
                "Roaring Fork Valley — fire corridor toward Carbondale/Aspen",
            ],
            "rate_of_spread_potential": "Extreme on steep canyon slopes; South Canyon Fire overran firefighters in minutes; Gambel oak produces intense heat and rapid spread; Grizzly Creek jumped Colorado River and I-70",
            "spotting_distance": "0.5-1 mile; canyon updrafts loft embers; fire crossed I-70 and Colorado River during Grizzly Creek Fire; steep terrain creates extreme convection columns",
        },
        "infrastructure_vulnerabilities": {
            "water_system": "City water from Grizzly Creek and No Name Creek — both in Grizzly Creek Fire burn scar; post-fire debris flows contaminate water; Roaring Fork River backup supply; water treatment challenged by turbidity",
            "power": "Holy Cross Energy (co-op); Shoshone Hydroelectric (15 MW, senior water rights); overhead lines through canyon terrain; extended outages during fire events; Shoshone plant loss would have Colorado River Compact implications",
            "communications": "Canyon terrain creates coverage gaps; I-70 fiber optic lines through Glenwood Canyon; fire/mudslides can sever telecommunications; limited cell service in canyon",
            "medical": "Valley View Hospital (78 beds); sole hospital for Garfield County (60,000+ service area); helicopter medevac to Grand Junction or Denver for trauma; hospital access impaired if I-70 and CO-82 both affected",
        },
        "demographics_risk_factors": {
            "population": 9963,
            "seasonal_variation": "Tourism hub; Glenwood Hot Springs, Hanging Lake, ski proximity; I-70 traffic (30,000+ vehicles/day through canyon); summer population can double; rafting/recreation economy",
            "elderly_percentage": "12.8%",
            "mobile_homes": "Some manufactured homes in Roaring Fork Valley; affordable housing shortage pushes workers into fire-prone areas",
            "special_needs_facilities": "Valley View Hospital (78 beds); senior care facilities; many tourism workers in seasonal housing; large Hispanic/Latino workforce (30%+) with potential language barriers in emergency communications",
        },
    },

    # =========================================================================
    # 15. GRANBY, CO (NEW)
    # =========================================================================
    "granby_co": {
        "center": [40.0861, -105.9394],
        "terrain_notes": (
            "Granby (7,935 ft) is a small town of approximately 2,100 residents in Grand "
            "County, situated along US-40 at the junction with US-34, 15 miles south of "
            "Grand Lake. The town sits in a broad valley where the Fraser River meets the "
            "Colorado River, surrounded by the Arapaho National Forest. During the East "
            "Troublesome Fire (October 2020), Granby was under mandatory evacuation as "
            "fire burned the ridgeline directly above town, with eerie orange skies "
            "visible from US-40. Firefighters cleared the 15-mile Grand Lake-to-Granby "
            "corridor in 90 minutes. Granby serves as the service hub for Grand County "
            "and the gateway to Winter Park, Ski Granby Ranch, and the C-BT Project "
            "reservoirs (Lake Granby, Shadow Mountain, Grand Lake). The town's economy "
            "depends on recreation and ranching, both vulnerable to wildfire impacts."
        ),
        "key_features": [
            {"name": "Lake Granby / Shadow Mountain Reservoir", "bearing": "N/NE", "type": "reservoir",
             "notes": "C-BT Project reservoirs; 539,758 acre-ft combined; fire contamination of watershed threatens Denver Water supply; shoreline development at risk"},
            {"name": "US-40 / US-34 junction", "bearing": "C", "type": "highway",
             "notes": "Critical intersection; US-34 north to Grand Lake, US-40 east to Winter Park/Denver, US-40 west to Kremmling; convergence during evacuation"},
            {"name": "East Troublesome burn scar", "bearing": "N/NE", "type": "burn_scar",
             "notes": "193,812-acre scar; post-fire debris flows into Colorado River and tributaries; ongoing erosion and water quality concerns"},
            {"name": "Arapaho National Forest", "bearing": "E/N/W", "type": "national_forest",
             "notes": "Surrounds town; beetle-kill lodgepole pine; continuous fuel from Kremmling to Continental Divide"},
            {"name": "Ski Granby Ranch", "bearing": "NE", "type": "ski_area",
             "notes": "Small ski area at town boundary; forested terrain; residential development on ski slopes"},
            {"name": "Fraser River / Colorado River headwaters", "bearing": "E/W", "type": "river",
             "notes": "River confluence near town; headwaters region; C-BT diversion infrastructure; post-fire water quality critical"},
        ],
        "elevation_range_ft": [7900, 8200],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "East Troublesome Fire", "year": 2020, "acres": 193812,
             "details": "Fire burned ridgeline above Granby; mandatory evacuation of town and surrounding areas; part of 35,000-person evacuation zone; fire visible from downtown; 555 total structures destroyed in Grand County; $543M insured losses; Granby proper largely spared but surrounding areas devastated"},
            {"name": "Williams Fork Fire", "year": 2020, "acres": 14833,
             "details": "Burned Aug-Dec 2020 south of Granby near Williams Fork Reservoir; demonstrated multiple simultaneous fire threat; beetle-kill timber; required significant suppression resources"},
        ],
        "evacuation_routes": [
            {"route": "US-40 East (Berthoud Pass to Denver)", "direction": "E", "lanes": 2,
             "bottleneck": "Berthoud Pass at 11,307 ft; two-lane mountain highway; 1.5-2 hours to Denver metro; winter conditions challenging",
             "risk": "Primary route to Front Range; mountain pass can close in weather events; passes through fire-prone forest; single road for 60+ miles"},
            {"route": "US-40 West (to Kremmling)", "direction": "W", "lanes": 2,
             "bottleneck": "Open ranch land initially; two-lane; 25 miles to Kremmling",
             "risk": "East Troublesome Fire originated near this corridor; passes through burn scar and active fire zones; connects to CO-9 or I-70 via Kremmling"},
            {"route": "US-34 North (to Grand Lake)", "direction": "N", "lanes": 2,
             "bottleneck": "15 miles to Grand Lake; two-lane through forested area",
             "risk": "During East Troublesome, this corridor was the evacuation path FROM Grand Lake THROUGH Granby; both directions on US-34 were active during 2020 fire"},
            {"route": "CO-125 North (to Walden)", "direction": "NW", "lanes": 2,
             "bottleneck": "Remote mountain road; 80+ miles to Walden; sparse services",
             "risk": "Emergency alternative; extremely remote; leads away from population centers; was in fire zone during 2020"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Valley winds along Colorado and Fraser river drainages; strong westerlies during fire weather events; East Troublesome driven by 60-120 mph gusts; diurnal up-valley/down-valley flow patterns",
            "critical_corridors": [
                "East Troublesome Creek drainage — proven 6,000 acre/hour fire path",
                "US-34 corridor to Grand Lake — fire spread along highway",
                "Fraser River valley — continuous fuel corridor toward Winter Park",
                "Lake Granby shoreline — structures in forested lakefront development",
            ],
            "rate_of_spread_potential": "Extreme; East Troublesome demonstrated 6,000 acres/hour; beetle-kill lodgepole pine produces explosive crown fire; pyrocumulonimbus fire weather self-sustaining; valley terrain channels fire runs",
            "spotting_distance": "2+ miles; East Troublesome produced extreme spotting; embers documented crossing valleys and ridges; pyrocumulonimbus convection lofted firebrands to unprecedented distances",
        },
        "infrastructure_vulnerabilities": {
            "water_system": "Town of Granby water from wells and surface sources; C-BT Project infrastructure (Granby Pump Canal, Farr Pumping Plant) locally critical; post-fire sediment loading affects water treatment; limited capacity for extended firefighting",
            "power": "Mountain Parks Electric (co-op); overhead lines through beetle-kill forest; extended outages during fire events; power loss hampers water pumping for firefighting",
            "communications": "Limited cell coverage outside town center; mountain terrain blocks signals; Grand County emergency communications were overwhelmed during 2020 evacuation of 35,000; some residents received no official warning",
            "medical": "Middle Park Medical Center (Granby, critical access hospital, 17 beds); sole hospital for Grand County (15,000+ population); limited trauma capability; helicopter medevac to Denver (1.5+ hours); weather-dependent; nearest level 1 trauma in Denver",
        },
        "demographics_risk_factors": {
            "population": 2100,
            "seasonal_variation": "Winter Park ski area and Lake Granby recreation swell population to 10,000+ seasonally; STRs and vacation homes dominate surrounding areas; ranching community with dispersed rural population; seasonal workers",
            "elderly_percentage": "15.2%",
            "mobile_homes": "Significant manufactured home presence in Granby and surrounding Grand County; affordable housing shortage; trailer parks near town center; highly vulnerable to wildfire",
            "special_needs_facilities": "Middle Park Medical Center (17 beds); Grand County Senior Center; dispersed rural elderly; many vacation homeowners absent during fire season; limited social services infrastructure",
        },
    },

    # =========================================================================
    # 14. GRAND LAKE, CO (NEW)
    # =========================================================================
    "grand_lake_co": {
        "center": [40.2522, -105.8231],
        "terrain_notes": (
            "Grand Lake (8,369 ft) is a tiny resort town of approximately 500 year-round "
            "residents at the western entrance to Rocky Mountain National Park, on the "
            "shore of Colorado's largest natural lake. The town sits in a narrow valley "
            "between the Continental Divide to the east and the Arapaho National Forest "
            "to the west and north. On October 21, 2020, the East Troublesome Fire — "
            "burning at 6,000 acres per hour with 120 mph wind gusts — exploded toward "
            "Grand Lake, giving residents minutes to evacuate. The fire destroyed 366 "
            "homes and 189 other structures in Grand County, with devastating losses in "
            "the Grand Lake area. Two elderly residents (Lyle and Marylin Hileman, ages "
            "86 and 84) who chose not to evacuate were killed. The fire crossed the "
            "Continental Divide into RMNP — a nearly unprecedented event. If a snowstorm "
            "had not arrived October 25, fire chiefs believe most of Grand Lake would "
            "have been lost."
        ),
        "key_features": [
            {"name": "Grand Lake (water body)", "bearing": "C", "type": "lake",
             "notes": "Largest natural lake in CO; tourism economy; Shadow Mountain and Granby reservoirs connected via channel; C-BT Project infrastructure"},
            {"name": "Rocky Mountain National Park (west entrance)", "bearing": "E", "type": "national_park",
             "notes": "Town at west entrance; Trail Ridge Road (US-34) seasonal; East Troublesome burned 30,000 acres of park; dense lodgepole pine and spruce-fir"},
            {"name": "Continental Divide", "bearing": "E", "type": "geographic",
             "notes": "2 miles east via Trail Ridge; East Troublesome Fire crossed divide in unprecedented event; 12,000+ ft; normally considered fire break but proved permeable"},
            {"name": "Shadow Mountain / Lake Granby", "bearing": "S", "type": "reservoir",
             "notes": "C-BT Project reservoirs; infrastructure threatened by fire; recreation economy dependent"},
            {"name": "US-34 / Trail Ridge Road", "bearing": "E", "type": "mountain_pass",
             "notes": "12,183 ft; closed Oct-May; western approach to Estes Park; was closed during Oct 2020 fires; seasonal isolation"},
            {"name": "Arapaho National Forest", "bearing": "W/N", "type": "national_forest",
             "notes": "Dense beetle-kill lodgepole pine; East Troublesome originated in Arapaho NF; continuous fuel from Kremmling 45 miles west"},
        ],
        "elevation_range_ft": [8369, 8600],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "East Troublesome Fire", "year": 2020, "acres": 193812,
             "details": "Started Oct 14 near Kremmling; exploded Oct 21 to 187,964 acres in 24 hours (6,000 acres/hr); 120 mph gusts; 555 structures destroyed; 2 fatalities near Grand Lake; crossed Continental Divide; $543M insured losses; 35,000 evacuated; firefighters cleared Grand Lake to Granby (15 miles) in 90 minutes; snowstorm Oct 25 saved remaining structures"},
        ],
        "evacuation_routes": [
            {"route": "US-34 South (to Granby)", "direction": "S", "lanes": 2,
             "bottleneck": "15 miles to Granby; two-lane road; single corridor for all Grand Lake evacuees; was evacuated with fire approaching from west",
             "risk": "ONLY viable evacuation route; fire on either side of US-34 traps entire town; 90 minutes to clear all residents in 2020; any delay would have been catastrophic"},
            {"route": "Trail Ridge Road / US-34 East", "direction": "E to Estes Park", "lanes": 2,
             "bottleneck": "12,183 ft pass; CLOSED Oct-May; unavailable during fall fire season; single lane in sections",
             "risk": "Closed during October 2020 fire; even when open, leads over 12,000 ft with no services; not a viable emergency route during fire season"},
            {"route": "CO-125 North (to Walden)", "direction": "N", "lanes": 2,
             "bottleneck": "Remote two-lane road north through Arapaho NF; 60+ miles to Walden; sparse population",
             "risk": "Leads into fire-prone forest; East Troublesome was burning along this corridor; CO-125 was closed during fire; not viable"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Strong westerly winds channeled through mountain valleys; East Troublesome driven by 120 mph gusts at Continental Divide; diurnal valley winds; foehn-type warming events; fire-generated weather (pyrocumulonimbus) documented during 2020 event",
            "critical_corridors": [
                "East Troublesome Creek drainage — fire origin to Grand Lake path",
                "US-34 corridor from Granby — fire approached along highway",
                "RMNP west side — continuous timber from town to Continental Divide",
                "Shadow Mountain / Lake Granby shoreline — structures on forested lakefront",
            ],
            "rate_of_spread_potential": "Unprecedented; 6,000 acres per hour (75 football fields per minute) during Oct 21 2020 blowup; fire-generated thunderstorm (pyrocumulonimbus); crossed 2-mile rocky Continental Divide; crown fire runs in beetle-kill lodgepole impossible to suppress",
            "spotting_distance": "2+ miles; pyrocumulonimbus lofted embers over Continental Divide; spot fires documented miles ahead of main front; extreme convection created self-sustaining fire weather",
        },
        "infrastructure_vulnerabilities": {
            "water_system": "Grand Lake water from wells and lake; very limited municipal infrastructure for 500 residents; fire hydrant coverage minimal outside town core; surrounding properties on wells; no capacity for extended firefighting operations",
            "power": "Mountain Parks Electric (co-op); overhead lines through dense forest; power lost during 2020 fire; single transmission feed; extended outages; backup generation critical for few remaining services",
            "communications": "Very limited cell coverage; terrain blocks signals; mountain radio repeaters serve area but vulnerable to fire; Grand County emergency communications strained during 2020 evacuation of 35,000; residents reported receiving no official warning before fire arrived",
            "medical": "No medical facility in Grand Lake; nearest is Middle Park Medical Center (Granby, 15 miles south, critical access hospital); patients must travel 70+ miles to major hospital in Summit County or Front Range; helicopter medevac weather-dependent at 8,400+ ft",
        },
        "demographics_risk_factors": {
            "population": 410,
            "seasonal_variation": "Summer population swells to 3,000-5,000 with vacation homes, STRs, and RMNP visitors; many vacation homeowners not present during fire season to maintain defensible space; RMNP west entrance draws heavy traffic; seasonal workers in tourism",
            "elderly_percentage": "35%+ (significant retirement community; highest risk)",
            "mobile_homes": "Some manufactured homes in surrounding areas; vulnerable seasonal structures; many older cabins with wood construction",
            "special_needs_facilities": "No medical facility; no hospital; high elderly percentage; Lyle and Marylin Hileman (ages 86, 84) died in 2020 fire after choosing not to evacuate; many elderly residents with limited mobility; vacation property owners may not have local support network",
        },
    },

    # =========================================================================
    # 4. LOUISVILLE, CO
    # =========================================================================
    "louisville_co": {
        "center": [39.9778, -105.1319],
        "terrain_notes": (
            "Louisville is a residential city immediately east of Superior on the "
            "Boulder-Jefferson county line, at approximately 5,350-5,500 ft elevation. "
            "The community occupies gently rolling terrain transitioning from foothills "
            "grassland to suburban development. During the Marshall Fire, the southern "
            "and western neighborhoods bore catastrophic losses as fire spread from "
            "Superior through dry grass corridors and via structure-to-structure "
            "ignition. The Original Town and Harper Lake areas sustained heavy damage. "
            "Louisville's older housing stock with mature landscaping proved both a "
            "buffer (green irrigated lawns) and a liability (large trees and wooden "
            "fences) depending on maintenance and proximity to ignition sources."
        ),
        "key_features": [
            {"name": "Original Town / Old Town Louisville", "bearing": "C", "type": "historic_district",
             "notes": "Historic downtown; some structures destroyed in Marshall Fire; older wood construction"},
            {"name": "Harper Lake area", "bearing": "SW", "type": "subdivision",
             "notes": "Heavy Marshall Fire losses; homes adjacent to open grassland"},
            {"name": "Coal Creek corridor", "bearing": "W", "type": "drainage",
             "notes": "Dry grass and open space; fire spread corridor from Superior into Louisville"},
            {"name": "Avista Adventist Hospital", "bearing": "N", "type": "medical",
             "notes": "Evacuated during Marshall Fire; critical medical facility at risk"},
            {"name": "US-36 / McCaslin Blvd", "bearing": "W", "type": "highway",
             "notes": "Major transportation corridors; both impacted during Marshall Fire"},
        ],
        "elevation_range_ft": [5300, 5550],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Marshall Fire", "year": 2021, "acres": 6200,
             "details": "Destroyed approximately 550+ structures in Louisville and surrounding unincorporated area; Avista Hospital evacuated; $2B+ total damages across all affected communities; wind-driven grass fire in winter"},
        ],
        "evacuation_routes": [
            {"route": "US-36", "direction": "SE toward Denver", "lanes": 4,
             "bottleneck": "Closed during Marshall Fire; primary regional artery",
             "risk": "Closure forces 21K residents onto local streets"},
            {"route": "CO-42 (96th St)", "direction": "N toward Boulder/Lafayette", "lanes": 2,
             "bottleneck": "Two-lane road; residential intersections",
             "risk": "Viable northern evacuation but limited capacity"},
            {"route": "US-287 (Federal Blvd)", "direction": "N/S", "lanes": 4,
             "bottleneck": "Eastern alternative; requires crossing through town",
             "risk": "Best capacity route; directed 'go north, go east' during Marshall Fire"},
            {"route": "South Boulder Road", "direction": "E", "lanes": 4,
             "bottleneck": "Local arterial; traffic signal congestion",
             "risk": "Secondary route; functional during Marshall Fire for eastbound evacuation"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Chinook downslope winds from west; sustained 80-100+ mph during Marshall Fire; wind-channeled through Coal Creek corridor",
            "critical_corridors": [
                "Coal Creek open space — grass fire corridor from Superior",
                "Southern Louisville grassland interface",
                "Structure-to-structure spread in older neighborhoods with wood fences and mature vegetation",
            ],
            "rate_of_spread_potential": "Extreme during Chinook events; fire reached Louisville from Superior in under 1 hour; grass fire speed in open terrain combined with ember-driven structure ignitions",
            "spotting_distance": "1-2 miles; ember transport from burning structures in Superior ignited homes in Louisville; windborne debris (roof materials, fence sections) documented as ignition vectors",
        },
        "infrastructure_vulnerabilities": {
            "water_system": "Louisville water utility; adequate pressure under normal conditions; system strained by simultaneous structure fires during Marshall Fire; some hydrants inaccessible due to road closures",
            "power": "Xcel Energy; 34,000+ customers lost power across Superior/Louisville; some outages lasted days; downed power lines complicated evacuation",
            "communications": "Emergency alert system reached most residents but some received no official warning; Reverse-911 delays documented; social media became primary information source",
            "medical": "Avista Adventist Hospital evacuated during Marshall Fire — only hospital in community required full evacuation; patients transferred to Denver metro facilities",
        },
        "demographics_risk_factors": {
            "population": 21376,
            "seasonal_variation": "Suburban community; stable year-round population; retail corridors draw regional visitors",
            "elderly_percentage": "12.1%",
            "mobile_homes": "Minimal; primarily single-family residential",
            "special_needs_facilities": "Avista Hospital (evacuated during Marshall Fire); Balfour Senior Living; multiple daycare centers; school-age children required emergency dismissal during Marshall Fire",
        },
    },

    # =========================================================================
    # 13. MANITOU SPRINGS, CO (NEW)
    # =========================================================================
    "manitou_springs_co": {
        "center": [38.8597, -104.9172],
        "terrain_notes": (
            "Manitou Springs (6,412 ft) is a small city of ~5,000 nestled in a narrow "
            "canyon at the base of Pikes Peak, immediately west of Colorado Springs. "
            "The town occupies the mouth of Ute Pass where Fountain Creek exits the "
            "mountains. Steep canyon walls rise 1,000-2,000 ft on both sides, with dense "
            "Gambel oak, mountain mahogany, and ponderosa pine on south-facing slopes. "
            "The Waldo Canyon Fire (2012) originated just 3 miles northwest and forced "
            "full evacuation of the entire town. While the fire did not directly burn "
            "into Manitou Springs, the 18,000-acre burn scar on the hillsides above "
            "town created severe post-fire debris flow risk. In summer 2013, flash floods "
            "from the burn scar inundated downtown with mud and debris, prompting CDOT "
            "to rebuild drainage infrastructure including a 24-ft-wide, 10-ft-high box "
            "culvert in Ute Pass. The town's narrow canyon geography and historic "
            "Victorian architecture make it one of the most physically constrained "
            "communities in Colorado for both fire and flood hazards."
        ),
        "key_features": [
            {"name": "Waldo Canyon burn scar", "bearing": "NW", "type": "burn_scar",
             "notes": "18,247-acre scar directly above town; ongoing debris flow risk; channeled into Williams Canyon Creek and Fountain Creek through downtown"},
            {"name": "Ute Pass / US-24", "bearing": "W", "type": "canyon_road",
             "notes": "Narrow canyon road; sole western access; steep grades and curves for 5 miles; CDOT rebuilt drainage after post-fire flooding"},
            {"name": "Pikes Peak (Barr Trail)", "bearing": "W", "type": "mountain",
             "notes": "Iconic trailhead in Manitou; draws 250K+ hikers annually; mountain rises 8,000 ft above town; dense timber on lower slopes"},
            {"name": "Williams Canyon", "bearing": "NW", "type": "canyon",
             "notes": "Cave of the Winds tourist attraction; narrow side canyon draining burn scar directly into town center"},
            {"name": "Fountain Creek", "bearing": "C", "type": "creek",
             "notes": "Runs through downtown; flood channel during post-fire debris flows; 2013 flooding deposited feet of mud in businesses"},
            {"name": "Garden of the Gods (adjacent)", "bearing": "NE", "type": "park",
             "notes": "Sandstone formations immediately east; partial fire break between Manitou and COS; heavy tourist traffic"},
        ],
        "elevation_range_ft": [6320, 6700],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Waldo Canyon Fire (evacuation zone)", "year": 2012, "acres": 18247,
             "details": "Entire town of Manitou Springs evacuated June 24 2012; fire burned 3 miles NW; 32,000 total evacuated across COS/Manitou/Woodland Park; US-24 closed by CO State Patrol; town not directly burned but post-fire debris flows devastated downtown 2013"},
            {"name": "Engel Fire", "year": 2009, "acres": 80,
             "details": "Burned on slopes above Manitou Springs; demonstrated fire risk on steep terrain directly above town; quickly contained"},
        ],
        "evacuation_routes": [
            {"route": "US-24 East (to Colorado Springs)", "direction": "E", "lanes": 4,
             "bottleneck": "Widens to 4 lanes entering COS but narrows through Old Colorado City; single route east",
             "risk": "Primary and essentially only evacuation route; US-24 was closed during Waldo Canyon Fire; 5,000 residents plus tourists must evacuate through single corridor"},
            {"route": "US-24 West (Ute Pass)", "direction": "W", "lanes": 2,
             "bottleneck": "Narrow canyon; steep grades; tight curves; 2 lanes; construction zones",
             "risk": "Leads uphill through Ute Pass toward fire-prone terrain; was closed during Waldo Canyon Fire; not viable when fire is to west/northwest"},
            {"route": "Manitou Avenue / El Monte Place", "direction": "E", "lanes": 2,
             "bottleneck": "Narrow historic streets; on-street parking; tourist congestion",
             "risk": "Local streets not designed for mass evacuation; Victorian-era road layout; tourist vehicles parked along narrow streets impede flow"},
            {"route": "Ruxton Avenue (to Cog Railway)", "direction": "W", "lanes": 2,
             "bottleneck": "Dead-end road to Pikes Peak Cog Railway base; narrows to single lane",
             "risk": "Dead-end; not an evacuation route; Cog Railway visitors must reverse through town to evacuate"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Canyon winds — Ute Pass channels downslope Chinook winds directly through town; afternoon upslope winds from Colorado Springs basin; terrain funneling amplifies wind speed; Waldo Canyon Fire driven by strong west winds",
            "critical_corridors": [
                "Waldo Canyon / Williams Canyon — proven fire and debris flow path to downtown",
                "Ute Pass corridor — wind tunnel effect from west",
                "South-facing slopes above town — Gambel oak and mountain mahogany (flash fuels)",
                "Fountain Creek canyon — channeling for both fire spread and debris flows",
            ],
            "rate_of_spread_potential": "Extreme on steep south-facing slopes; Gambel oak produces intense, fast-moving fire; canyon terrain creates chimney effect; Waldo Canyon Fire demonstrated 3-mile fire run toward city in hours; post-fire debris flows can arrive in minutes after heavy rain",
            "spotting_distance": "0.5-1 mile; steep terrain and strong thermals loft embers; Gambel oak produces intense radiant heat and firebrands; embers could cross narrow canyon and ignite opposite slope simultaneously",
        },
        "infrastructure_vulnerabilities": {
            "water_system": "Manitou Springs water from mineral springs and wells; limited capacity; famous mineral springs are historic/tourism asset but not fire suppression source; fire hydrant coverage limited in historic district with narrow streets",
            "power": "Xcel Energy; overhead lines through canyon terrain; lines run along US-24 through Ute Pass; power outages during wind events and fires; no redundant feeds",
            "communications": "Canyon terrain limits cell coverage; downtown is narrow valley floor; emergency sirens installed post-Waldo Canyon (3 early-warning sirens); Reverse-911 primary alert method",
            "medical": "No hospital in Manitou Springs; nearest is UCHealth Memorial in Colorado Springs (5 miles east); ambulance must navigate narrow streets and US-24; response time 10-20 min under normal conditions but significantly longer during evacuation",
        },
        "demographics_risk_factors": {
            "population": 4858,
            "seasonal_variation": "Pikes Peak Cog Railway, Cave of the Winds, mineral springs draw 1M+ tourists annually; summer weekends can triple daytime population; many visitors parked in narrow streets impede evacuation",
            "elderly_percentage": "16.8%",
            "mobile_homes": "Minimal within city limits; some older housing stock with wood shake roofs in historic district",
            "special_needs_facilities": "No hospital; limited medical facilities; historic senior housing; many homes on steep hillsides with limited ADA access; Cog Railway visitors include elderly and mobility-impaired tourists; pet-friendly tourism means animal evacuation complicates logistics",
        },
    },

    # =========================================================================
    # 16. PAGOSA SPRINGS, CO (NEW)
    # =========================================================================
    "pagosa_springs_co": {
        "center": [37.2695, -107.0098],
        "terrain_notes": (
            "Pagosa Springs (7,126 ft) is a remote mountain town of approximately 1,800 "
            "residents in Archuleta County, situated at the junction of US-160 and US-84 "
            "in the upper San Juan River valley. The town is surrounded by the San Juan "
            "National Forest, with dense ponderosa pine at lower elevations transitioning "
            "to mixed-conifer and spruce-fir forests on surrounding mountains reaching "
            "12,000+ ft. The San Juan National Forest has a fire-adapted ecosystem that "
            "historically experienced frequent low-intensity fires, but decades of fire "
            "suppression have created heavy fuel accumulations. The town is known for "
            "the world's deepest geothermal hot spring. Its remote location — 60 miles "
            "east of Durango, 60 miles south of Wolf Creek Pass, and 150+ miles from any "
            "major city — makes emergency response and evacuation extremely challenging. "
            "Recent fires include a 75-acre illegal burn that became a wildfire in 2024, "
            "evacuating 144 structures."
        ),
        "key_features": [
            {"name": "San Juan National Forest", "bearing": "ALL", "type": "national_forest",
             "notes": "Surrounds town; ponderosa pine, mixed-conifer, spruce-fir; fire-adapted ecosystem with suppressed fire regime; heavy fuel loads; prescribed burns active"},
            {"name": "Pagosa Hot Springs / San Juan River", "bearing": "C", "type": "hot_springs",
             "notes": "World's deepest geothermal spring; tourism anchor; river runs through town center; geothermal infrastructure"},
            {"name": "Wolf Creek Pass / US-160 East", "bearing": "E", "type": "mountain_pass",
             "notes": "10,857 ft pass; US-160 east to Alamosa; notorious for winter weather; sole eastern route; heavy truck traffic"},
            {"name": "Chimney Rock National Monument", "bearing": "W", "type": "monument",
             "notes": "17 miles west; archaeological site in fire-prone pinyon-juniper and ponderosa woodland; fires have burned near monument"},
            {"name": "Turkey Springs area", "bearing": "NW", "type": "wildland",
             "notes": "USFS prescribed burn area (650 acres); ponderosa pine restoration; Brockover-Devil Creek project reducing hazardous fuels"},
            {"name": "Navajo Lake / Piedra River", "bearing": "W/SW", "type": "recreation",
             "notes": "Reservoir and river recreation; surrounding forest at fire risk; Southern Ute Reservation border"},
        ],
        "elevation_range_ft": [7079, 7500],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Unnamed illegal burn wildfire", "year": 2024, "acres": 75,
             "details": "Aug 10; illegal burn became 75-acre wildfire; mandatory evacuation of 144 structures for 70 hours; demonstrated rapid escalation from human ignition"},
            {"name": "West Fork Complex", "year": 2013, "acres": 109049,
             "details": "June-July 2013; multiple fires in San Juan and Rio Grande NFs; largest complex fire in CO at time; US-160 Wolf Creek Pass closed; severe economic impact on Pagosa Springs tourism; 0 structures destroyed but massive smoke and closure impacts"},
            {"name": "Missionary Ridge Fire (regional impact)", "year": 2002, "acres": 73000,
             "details": "Burned 60 miles west near Durango; demonstrated regional San Juan NF fire risk; smoke impacts in Pagosa Springs"},
        ],
        "evacuation_routes": [
            {"route": "US-160 West (to Durango)", "direction": "W", "lanes": 2,
             "bottleneck": "60 miles to Durango; two-lane mountain highway; passes through forested terrain; Chimney Rock area fire-prone",
             "risk": "Primary route to nearest significant city; fire along US-160 corridor would isolate town from west; long distance to services"},
            {"route": "US-160 East (Wolf Creek Pass)", "direction": "E", "lanes": 2,
             "bottleneck": "10,857 ft pass; notorious winter weather; steep grades; heavy truck traffic; 90 miles to Alamosa",
             "risk": "Only eastern route; pass closure (weather or fire) eliminates eastern evacuation; West Fork Complex closed this route in 2013"},
            {"route": "US-84 South (to Chama, NM)", "direction": "S", "lanes": 2,
             "bottleneck": "Two-lane road south to New Mexico border; rural; 47 miles to Chama (pop 1,000)",
             "risk": "Southern alternative; leads to very small NM communities; limited services; viable escape route but offers minimal resources"},
            {"route": "CR-600 / Piedra Road", "direction": "NW", "lanes": 2,
             "bottleneck": "County road; narrow; forest service road quality",
             "risk": "Emergency-only; leads into national forest; not a viable mass evacuation route"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Diurnal mountain valley winds; southwest monsoon thunderstorm outflows (July-August); occasional dry lightning with no rain; foehn-type warm dry winds from northwest; less extreme than Front Range Chinook but consistent fire-season risk",
            "critical_corridors": [
                "San Juan River valley — US-160 corridor with ponderosa pine",
                "Wolf Creek Pass approaches — heavy timber, steep terrain",
                "Turkey Springs / Mill Creek — USFS fuel reduction area NW of town indicates recognized risk",
                "Piedra River drainage — continuous forest corridor to west",
            ],
            "rate_of_spread_potential": "High on slopes in ponderosa pine; extreme in mixed-conifer and spruce-fir at higher elevations; West Fork Complex demonstrated 109,000-acre fire in San Juan NF; steep terrain with heavy fuel loads; monsoonal thunderstorm ignitions can produce multiple simultaneous starts",
            "spotting_distance": "0.5-1 mile typical; steep terrain creates strong updrafts; ponderosa bark firebrands; mixed-conifer crown fire produces intense convection; monsoonal wind gusts can accelerate ember transport",
        },
        "infrastructure_vulnerabilities": {
            "water_system": "Pagosa Area Water and Sanitation District; San Juan River surface water; geothermal infrastructure for heating; water/sewer infrastructure under construction (US-160 corridor); limited fire suppression capacity in surrounding WUI areas",
            "power": "La Plata Electric Association (co-op); overhead lines through forest; single transmission feed; extended outages possible; nearest alternative power sources distant; geothermal could provide limited local backup",
            "communications": "Limited cell coverage outside town; mountain terrain creates extensive dead zones; remote location means delayed mutual aid response; Archuleta County emergency notification system covers town but gaps in surrounding areas",
            "medical": "Pagosa Springs Medical Center (critical access hospital, 11 beds); very limited capacity; nearest major hospital in Durango (60 miles); helicopter medevac from Durango or Grand Junction; golden hour nearly impossible given remoteness",
        },
        "demographics_risk_factors": {
            "population": 1810,
            "seasonal_variation": "Wolf Creek Ski Area (25 miles east) and hot springs draw winter visitors; summer recreation increases population; many vacation/seasonal homes; ranching community with dispersed rural population",
            "elderly_percentage": "24.3%",
            "mobile_homes": "Significant manufactured home presence in Archuleta County; affordable housing shortage; rural properties with limited fire mitigation",
            "special_needs_facilities": "Pagosa Springs Medical Center (11 beds); senior services center; high elderly percentage in remote setting; many rural residents miles from nearest neighbor; limited public transportation; Southern Ute tribal members in surrounding area",
        },
    },

    # =========================================================================
    # 17. REDSTONE / MARBLE, CO (NEW)
    # =========================================================================
    "redstone_marble_co": {
        "center": [39.2003, -107.2381],
        "terrain_notes": (
            "Redstone (7,180 ft) and Marble (7,950 ft) are tiny unincorporated communities "
            "in the Crystal River valley of Pitkin and Gunnison counties, accessed exclusively "
            "by CO-133 — a narrow two-lane highway that follows the Crystal River south from "
            "Carbondale. Redstone (population ~100-200) is a historic coal mining village with "
            "a single street of charming Victorian homes and the historic Redstone Castle. "
            "Marble (population ~130) lies 6 miles further south at a virtual dead end, "
            "famous for the quarry that provided marble for the Lincoln Memorial and Tomb of "
            "the Unknown Soldier. The Crystal River valley narrows dramatically between these "
            "communities, with steep canyon walls of 1,500-2,500 ft rising on both sides. "
            "CO-133 is the sole access road for both communities, and it continues over "
            "McClure Pass (8,755 ft) — a narrow, winding mountain road that can close due "
            "to avalanches, rockfall, or fire. A 2024 propane tanker rollover near Marble "
            "forced evacuation and CO-133 closure, demonstrating the fragility of single-road "
            "access. The surrounding White River National Forest contains dense aspen, "
            "mixed-conifer, and spruce-fir forests on steep terrain."
        ),
        "key_features": [
            {"name": "CO-133 (sole access road)", "bearing": "N/S", "type": "highway",
             "notes": "Two-lane road; sole access for both communities; follows Crystal River through narrow canyon; closure traps all residents; McClure Pass section especially constrained"},
            {"name": "Redstone Castle / Historic District", "bearing": "C (Redstone)", "type": "historic",
             "notes": "1902 Tudor-style mansion (John Cleveland Osgood); National Historic Landmark; wooden structure in forested canyon; irreplaceable cultural asset"},
            {"name": "Crystal River canyon", "bearing": "N/S", "type": "canyon",
             "notes": "Narrow V-shaped canyon; steep walls; fire on slopes would funnel directly through valley; limited defensible space; riparian corridor provides limited fuel break"},
            {"name": "Marble quarry / Yule Creek", "bearing": "S", "type": "quarry",
             "notes": "Historic marble quarry; Yule Creek Road is dead-end beyond Marble; famous blocks for Lincoln Memorial; community at literal end of road"},
            {"name": "McClure Pass", "bearing": "S", "type": "mountain_pass",
             "notes": "8,755 ft; narrow, winding CO-133 section; avalanche and rockfall closures; connects to Paonia/Delta; not reliable escape route"},
            {"name": "Chair Mountain / Elk Mountains", "bearing": "SE", "type": "mountain",
             "notes": "12,000+ ft peaks; alpine terrain above timberline; steep forested slopes drain into Crystal River valley; avalanche and fire risk"},
        ],
        "elevation_range_ft": [7100, 8000],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Coal Basin fires (historic)", "year": 1990, "acres": 500,
             "details": "Historic fires in coal mining areas above Redstone; spontaneous combustion of coal seams; demonstrated geologic fire risk similar to Glenwood Springs Coal Seam Fire"},
            {"name": "Grizzly Creek Fire (regional)", "year": 2020, "acres": 32631,
             "details": "Burned 25 miles north in Glenwood Canyon; demonstrated regional fire risk; smoke impacts throughout Crystal River valley; CO-133 to I-70 access threatened"},
            {"name": "Propane tanker incident", "year": 2024, "acres": 0,
             "details": "Propane tanker rollover near Marble forced evacuations and CO-133 closure; demonstrated single-road access vulnerability; hazmat risk in narrow canyon; County Road 3 and CO-133 both closed"},
        ],
        "evacuation_routes": [
            {"route": "CO-133 North (to Carbondale)", "direction": "N", "lanes": 2,
             "bottleneck": "19 miles from Redstone to Carbondale; narrow canyon road; single lane each direction; rockfall zones; curves",
             "risk": "ONLY viable evacuation route for Redstone; fire in canyon between Redstone and Carbondale traps entire community; Marble residents must pass through Redstone to reach this route"},
            {"route": "CO-133 South (McClure Pass to Paonia)", "direction": "S", "lanes": 2,
             "bottleneck": "8,755 ft pass; narrow and winding; avalanche closures in winter; 50+ miles to Delta/Paonia",
             "risk": "Emergency alternative if northern route blocked; unreliable due to pass conditions; long distance to safety; Marble residents closer to this route but McClure Pass is marginal"},
            {"route": "Marble / Crystal Mill Road (dead end)", "direction": "S beyond Marble", "lanes": 1,
             "bottleneck": "Dead-end road; deteriorates to ATV trail; leads to Crystal Mill (tourist site) and nothing else",
             "risk": "Absolute dead end; zero evacuation value; tourists driving to Crystal Mill may be trapped during fire event"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Canyon winds — up-valley during day, down-valley at night; strong channeling through narrow Crystal River canyon; wind acceleration at canyon narrows; occasional strong westerlies from Elk Mountains",
            "critical_corridors": [
                "Crystal River canyon — narrow valley concentrates fire and smoke; chimney effect on steep side slopes",
                "Coal Basin drainage above Redstone — historic coal fire area; dense timber",
                "Yule Creek / Marble approach — dead-end valley; fire traps entire community",
                "McClure Pass corridor — heavy timber, steep terrain, limited escape",
            ],
            "rate_of_spread_potential": "High to extreme on steep canyon walls; chimney effect in narrow valley accelerates upslope runs; mixed-conifer and aspen-conifer forests; dense undergrowth in riparian areas; steep terrain above communities makes suppression extremely difficult",
            "spotting_distance": "0.5-1 mile; narrow canyon creates strong updrafts; embers lofted from one canyon wall can cross valley and ignite opposite slope; timber on steep slopes produces rolling firebrands",
        },
        "infrastructure_vulnerabilities": {
            "water_system": "No municipal water system; private wells and springs; Crystal River for emergency supply; no fire hydrants outside of limited Redstone infrastructure; fire suppression entirely dependent on tanker shuttle operations",
            "power": "Holy Cross Energy (co-op); single overhead line along CO-133; extremely vulnerable to fire/wind/avalanche; outage isolates both communities; no redundant feeds; propane for heating (tanker rollover risk demonstrated 2024)",
            "communications": "Very limited cell coverage; canyon terrain blocks signals; landline/fiber follows CO-133 corridor; single point of failure; residents may have no way to receive emergency alerts; satellite phone recommended",
            "medical": "No medical facilities; nearest hospital is Valley View (Glenwood Springs, 30+ miles north) or Aspen Valley Hospital (30+ miles east); ambulance response 45-60+ min; helicopter landing zones extremely limited in narrow canyon; medevac complicated by terrain and smoke",
        },
        "demographics_risk_factors": {
            "population": 330,
            "seasonal_variation": "Summer tourism triples population; Crystal Mill, Redstone Castle, and hiking draw day visitors; STRs and vacation homes; most visitors completely unfamiliar with area and unaware of single-road access vulnerability",
            "elderly_percentage": "20%+ (small retired community; exact data limited for unincorporated areas)",
            "mobile_homes": "Some manufactured homes; older cabin construction; historic wooden structures; limited fire-resistant construction",
            "special_needs_facilities": "No medical facilities; no emergency services based locally; volunteer fire department; many residents are seasonal; elderly and mobility-impaired residents extremely vulnerable given 30+ mile distance to hospital; no public transportation",
        },
    },

    # =========================================================================
    # 10. STEAMBOAT SPRINGS, CO
    # =========================================================================
    "steamboat_springs_co": {
        "center": [40.4850, -106.8317],
        "terrain_notes": (
            "Steamboat Springs (6,700 ft) sits in the Yampa River valley in Routt County, "
            "surrounded by the Routt National Forest and the Park Range of the Rocky "
            "Mountains. More than 99% of Routt County residents live in the wildland-urban "
            "interface. The ski resort town has experienced rapid growth, pushing new "
            "development into forested areas on Emerald Mountain (south), the ski mountain "
            "slopes (east), and rural ranchland corridors along the Yampa and Elk River "
            "valleys. The surrounding forests contain extensive beetle-kill lodgepole pine "
            "and spruce-fir, creating extreme fuel loads. While Steamboat has been "
            "relatively spared from major wildfires historically, the combination of "
            "growing WUI, beetle-kill timber, and increasing drought makes it increasingly "
            "vulnerable. The 2025 Lee Fire on the Western Slope prompted a statewide "
            "disaster emergency declaration that included Routt County."
        ),
        "key_features": [
            {"name": "Mt. Werner / Steamboat Ski Area", "bearing": "E", "type": "ski_area",
             "notes": "10,568 ft summit; ski area base at 6,900 ft; resort development in forested terrain; summer operations increase fire-season visitation"},
            {"name": "Emerald Mountain", "bearing": "S", "type": "mountain_wui",
             "notes": "Directly south of downtown; wildfire mitigation project underway; city open space with dense timber; fire here would threaten downtown core"},
            {"name": "Routt National Forest", "bearing": "E/N/S", "type": "national_forest",
             "notes": "Surrounds town on three sides; extensive beetle-kill lodgepole pine; spruce-fir at higher elevations; continuous fuel from wilderness to town"},
            {"name": "Yampa River corridor", "bearing": "W/E", "type": "river_valley",
             "notes": "Valley floor development corridor; US-40 follows river; ranch properties with grass and brush fuels"},
            {"name": "Elk River valley", "bearing": "N", "type": "valley_wui",
             "notes": "Rural residential development in forested valley north of town; single road access; growing community"},
            {"name": "Rabbit Ears Pass (US-40)", "bearing": "SE", "type": "mountain_pass",
             "notes": "9,426 ft pass on primary route to Denver; beetle-kill timber corridor; closure isolates Steamboat from Front Range"},
        ],
        "elevation_range_ft": [6695, 7200],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Various small fires", "year": 2020, "acres": 100,
             "details": "Multiple small fires in Routt NF during 2020 fire season; all contained but demonstrated increasing fire risk in beetle-kill timber"},
            {"name": "Silver Creek Fire", "year": 2018, "acres": 512,
             "details": "Lightning-caused fire in Routt NF north of Steamboat; burned in beetle-kill timber; demonstrated fuel conditions surrounding town"},
            {"name": "Lee Fire (Western Slope)", "year": 2025, "acres": 2500,
             "details": "Prompted statewide disaster emergency declaration by Governor Polis that included Routt County; demonstrated regional fire risk escalation"},
        ],
        "evacuation_routes": [
            {"route": "US-40 East (Rabbit Ears Pass)", "direction": "E toward Kremmling/Denver", "lanes": 2,
             "bottleneck": "9,426 ft mountain pass; two-lane; winter closures; 2+ hours to I-70",
             "risk": "Primary route to Front Range; beetle-kill fire corridor; closure isolates town from east; no alternative"},
            {"route": "US-40 West", "direction": "W toward Craig/Hayden", "lanes": 2,
             "bottleneck": "Yampa Valley; agricultural area; less constrained terrain",
             "risk": "Best evacuation route; lower fire risk on western prairie approach; 30 miles to Craig"},
            {"route": "CO-131 South", "direction": "S to Wolcott/I-70", "lanes": 2,
             "bottleneck": "60 miles to I-70; two-lane mountain road through Gore Creek area",
             "risk": "Long secondary route to I-70; passes through fire-prone terrain; limited services"},
            {"route": "Elk River Road / CR-129", "direction": "N", "lanes": 2,
             "bottleneck": "Two-lane road north into Elk River valley; dead-end at Slavonia",
             "risk": "Dead-end route; not an evacuation option; traps Elk River residents; single road access for growing community"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Prevailing westerlies; valley channeling along Yampa River; afternoon upslope thermals; occasional foehn-type dry wind events from west; less extreme than Front Range Chinook events but still significant",
            "critical_corridors": [
                "Emerald Mountain — directly south of downtown, dense timber",
                "Rabbit Ears Pass / US-40 — beetle-kill corridor from east",
                "Elk River valley — single-road access community in forested valley",
                "Ski mountain slopes — resort development in high-risk timber",
            ],
            "rate_of_spread_potential": "High; beetle-kill lodgepole pine produces explosive crown fire; steep mountain terrain accelerates fire; less extreme wind events than Front Range but fuel conditions are worse in some areas due to beetle-kill",
            "spotting_distance": "0.5-1 mile; beetle-kill snags produce prolific ember showers; spruce-fir crown fire generates intense convection and long-range spotting",
        },
        "infrastructure_vulnerabilities": {
            "water_system": "City of Steamboat Springs water from Fish Creek and Yampa River; Fish Creek watershed heavily forested and vulnerable to wildfire contamination; limited alternative water sources; post-fire flooding would devastate Fish Creek filtration plant",
            "power": "Yampa Valley Electric Association (co-op); overhead lines through forested terrain; regional power from Hayden and Craig coal plants (transitioning to renewables); extended outages possible during fire events",
            "communications": "Cell coverage adequate in town but gaps in surrounding valleys; Elk River valley and mountain areas have limited service; radio repeaters on peaks vulnerable",
            "medical": "UCHealth Yampa Valley Medical Center (39 beds); sole hospital for Routt County; limited capacity; helicopter medevac to Denver (2+ hours); nearest trauma center is in Denver",
        },
        "demographics_risk_factors": {
            "population": 13224,
            "seasonal_variation": "Ski season doubles population; summer recreation and events draw large crowds; peak-season population can exceed 30,000; large seasonal workforce in hospitality",
            "elderly_percentage": "10.5%",
            "mobile_homes": "Affordable housing crisis means workforce in manufactured homes and older structures in fire-prone locations; trailer parks in Yampa Valley",
            "special_needs_facilities": "Yampa Valley Medical Center (39 beds); senior living facilities; seasonal tourist population unfamiliar with fire risk; large immigrant workforce with potential language barriers",
        },
    },

    # =========================================================================
    # 3. SUPERIOR, CO
    # =========================================================================
    "superior_co": {
        "center": [39.9528, -105.1686],
        "terrain_notes": (
            "Superior is a suburban community on the Boulder-Broomfield county line, "
            "situated on the elevated mesa between Boulder and Denver at approximately "
            "5,500-5,700 ft elevation. The town is surrounded by open grassland and "
            "agricultural fields on its south and east sides, with the foothills visible "
            "to the west. The Marshall Fire (December 30, 2021) completely redefined "
            "wildfire risk assessment for suburban communities nationwide. Driven by "
            "Chinook winds gusting to 115 mph, a grass fire originating near Marshall "
            "Road destroyed 991 structures in Superior alone, including the Sagamore "
            "subdivision which was nearly completely leveled. The fire demonstrated that "
            "structure-to-structure ignition in suburban density is as dangerous as "
            "wildland fire when winds are extreme. The town had no wildfire evacuation "
            "plan prior to the Marshall Fire; residents had minutes to evacuate."
        ),
        "key_features": [
            {"name": "Marshall Mesa / Marshall Road", "bearing": "W", "type": "grassland_origin",
             "notes": "Fire origin area; open grassland at CO-93/Marshall Road; direct wind exposure from foothills"},
            {"name": "Sagamore neighborhood", "bearing": "C", "type": "subdivision",
             "notes": "Nearly completely destroyed Dec 30 2021; dense suburban development; structure-to-structure fire spread"},
            {"name": "Rock Creek neighborhood", "bearing": "N", "type": "subdivision",
             "notes": "Significant losses in Marshall Fire; vinyl fencing and wood decks enabled structure-to-structure spread"},
            {"name": "US-36 corridor", "bearing": "N", "type": "highway",
             "notes": "Major evacuation route; was closed during Marshall Fire due to fire crossing highway"},
            {"name": "Coal Creek open space", "bearing": "S", "type": "grassland",
             "notes": "Dry grass corridor connecting to Louisville; fire spread path during Marshall Fire"},
        ],
        "elevation_range_ft": [5450, 5750],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Marshall Fire", "year": 2021, "acres": 6200,
             "details": "Dec 30 winter grassland fire; 115 mph wind gusts; 1,084 total structures destroyed across Superior/Louisville/unincorporated Boulder County; ~991 structures in Superior; most destructive fire in CO history; $2B+ in damages; unprecedented suburban wildfire"},
        ],
        "evacuation_routes": [
            {"route": "US-36", "direction": "E to Denver / NW to Boulder", "lanes": 4,
             "bottleneck": "Closed in both directions during Marshall Fire due to fire activity",
             "risk": "Primary evacuation route was unusable; residents directed 'go east, go north' on local streets"},
            {"route": "McCaslin Blvd / CO-128", "direction": "N/S", "lanes": 4,
             "bottleneck": "Local arterials not designed for mass evacuation",
             "risk": "Intersection congestion; traffic signals non-functional during power outages"},
            {"route": "CO-170 (Eldorado Springs Dr)", "direction": "W", "lanes": 2,
             "bottleneck": "Two-lane road toward foothills; closed during Marshall Fire",
             "risk": "Leads toward fire origin; unusable during westerly wind-driven fires"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Chinook downslope winds from west/southwest; Marshall Fire sustained hurricane-force winds for 11 hours; 115 mph peak gust",
            "critical_corridors": [
                "Marshall Mesa grassland — direct fire path from foothills to town",
                "Coal Creek corridor — fire spread path to Louisville",
                "US-36 corridor — fire jumped the highway",
                "Structure-to-structure spread through subdivisions via fences, decks, landscaping",
            ],
            "rate_of_spread_potential": "Extreme; Marshall Fire went from origin to destroying hundreds of structures within 2-3 hours; grass fire ROS of 50-100+ chains/hour in 100+ mph winds",
            "spotting_distance": "2+ miles documented in Marshall Fire; embers crossed US-36 and ignited structures well ahead of main fire front; structure embers (roof shingles, fence debris) carried by wind",
        },
        "infrastructure_vulnerabilities": {
            "water_system": "Municipal water from Denver Water system; fire hydrant pressure adequate under normal conditions but Marshall Fire overwhelmed suppression capacity; 34,000+ customers lost power",
            "power": "Xcel Energy; 34,000 customers lost power during Marshall Fire across Superior/Louisville; downed power lines suspected as contributing ignition source",
            "communications": "Cell towers functional but overloaded during evacuation; emergency alerts delayed for some residents; many learned of fire from neighbors not official channels",
            "medical": "No hospital in Superior; nearest is Avista Adventist (Louisville) and Good Samaritan (Lafayette); all patients evacuated from Avista during Marshall Fire",
        },
        "demographics_risk_factors": {
            "population": 13094,
            "seasonal_variation": "Suburban commuter community; daytime population lower as residents work in Denver/Boulder; Costco and retail draws regional shoppers",
            "elderly_percentage": "8.5%",
            "mobile_homes": "None significant; primarily single-family homes and townhomes",
            "special_needs_facilities": "Several assisted living facilities; daycare centers required emergency evacuation during Marshall Fire; some residents with mobility limitations could not self-evacuate quickly",
        },
    },

    # =========================================================================
    # 12. WOODLAND PARK, CO (NEW)
    # =========================================================================
    "woodland_park_co": {
        "center": [38.9939, -105.0569],
        "terrain_notes": (
            "Woodland Park (8,465 ft) is a mountain community of 8,000+ in Teller County, "
            "situated along US-24 (Ute Pass) between Colorado Springs and the mountain "
            "communities of Cripple Creek/Victor. The city sits in the transition zone "
            "between Front Range ponderosa pine forests and the higher montane forests "
            "of the Pikes Peak massif. The Hayman Fire (2002) — at 137,760 acres the "
            "largest Colorado fire at the time — burned within 6-7 miles of Woodland Park, "
            "placing 7,500 residents on standby for evacuation. The fire destroyed 133 "
            "residences and 466 outbuildings across Park, Teller, Jefferson, and Douglas "
            "counties. More recently, the Highland Lakes Fire (2024) forced evacuations "
            "of subdivisions in southwest Teller County. Woodland Park incorporated "
            "wildfire protection into its comprehensive plan following the Hayman Fire "
            "and adopted a fire code in 2009, but continued WUI development in "
            "surrounding Teller County increases exposure."
        ),
        "key_features": [
            {"name": "Hayman Fire burn scar", "bearing": "NE/E", "type": "burn_scar",
             "notes": "137,760-acre scar; still recovering 20+ years later; some areas have not regenerated forest; ongoing debris flow risk"},
            {"name": "US-24 / Ute Pass corridor", "bearing": "E/W", "type": "highway",
             "notes": "Primary route connecting COS to mountain communities; narrow canyon from Manitou Springs to Woodland Park; sole east-west artery"},
            {"name": "Pikes Peak massif", "bearing": "S/SE", "type": "mountain",
             "notes": "14,115 ft; dense timber on north slopes above town; Pike National Forest surrounds community"},
            {"name": "Rampart Range", "bearing": "E", "type": "ridge",
             "notes": "Forested ridge between Woodland Park and Colorado Springs; Rampart Range Road provides emergency access but is unpaved"},
            {"name": "Cripple Creek / Victor mining district", "bearing": "SW", "type": "mountain_community",
             "notes": "Historic mining towns 18 miles SW; single road access via CO-67; fire would isolate communities"},
            {"name": "Mueller State Park", "bearing": "SW", "type": "state_park",
             "notes": "5,121-acre park in heavy timber; recreation area; potential ignition and fuel source"},
        ],
        "elevation_range_ft": [8200, 8800],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Hayman Fire", "year": 2002, "acres": 137760,
             "details": "June 8-July 18; arson by USFS fire prevention tech Terry Barton; 133 residences and 466 outbuildings destroyed; 6 indirect fatalities; $42M+ housing losses; Woodland Park 7,500 residents on evacuation standby; came within 6-7 miles of town; fire burned across 4 counties"},
            {"name": "Highland Lakes Fire", "year": 2024, "acres": 150,
             "details": "Oct 2024; forced evacuations of subdivisions in southwest Teller County; crews made progress on 'aggressive' fire; demonstrated ongoing WUI risk"},
            {"name": "Waldo Canyon Fire (proximity)", "year": 2012, "acres": 18247,
             "details": "Burned 15 miles east in Rampart Range; 32,000 evacuated including Woodland Park residents; US-24 closed; demonstrated Ute Pass vulnerability"},
        ],
        "evacuation_routes": [
            {"route": "US-24 East (Ute Pass to COS)", "direction": "E", "lanes": 4,
             "bottleneck": "Narrows to 2 lanes through steep Ute Pass canyon; hairpin turns; 5-mile canyon section above Manitou Springs",
             "risk": "Primary evacuation route; canyon fire could close route; 20-mile constrained corridor to Colorado Springs; single route for 8,000+ residents plus Cripple Creek traffic"},
            {"route": "US-24 West", "direction": "W toward Buena Vista", "lanes": 2,
             "bottleneck": "Two-lane mountain road through Wilkerson Pass (9,507 ft); 50+ miles to Buena Vista",
             "risk": "Long secondary route; remote; limited services; leads into fire-prone mountain terrain"},
            {"route": "CO-67 South (to Cripple Creek/Victor)", "direction": "S", "lanes": 2,
             "bottleneck": "Mountain road through Pike NF; dead-end at Cripple Creek (must then take CO-67 south to Florence)",
             "risk": "Not a viable mass evacuation route; leads to isolated mountain communities; itself at fire risk"},
            {"route": "Rampart Range Road", "direction": "E/NE", "lanes": 1,
             "bottleneck": "Unpaved forest road; seasonal closures; 4WD recommended; very slow",
             "risk": "Emergency-only alternative to US-24; used during Hayman Fire when US-24 closed; not viable for mass evacuation"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Chinook downslope winds through Ute Pass; west-to-east canyon channeling; afternoon upslope thermals from Colorado Springs basin; Hayman Fire demonstrated extreme fire weather with multiple major fire runs",
            "critical_corridors": [
                "Ute Pass corridor — US-24 canyon from Manitou Springs to Divide",
                "Hayman burn scar — NE approach; regenerating but still fire-prone",
                "Pikes Peak north slope — dense timber above town",
                "CO-67 corridor — forested route to Cripple Creek",
            ],
            "rate_of_spread_potential": "Extreme; Hayman Fire burned 60,000 acres in first 4 days; drought conditions and beetle-kill amplify crown fire potential; steep terrain above Ute Pass creates rapid uphill runs",
            "spotting_distance": "1-2 miles; Hayman Fire documented extreme spotting distances across ridges; ponderosa pine bark produces prolific firebrands; canyon winds loft embers over ridgelines",
        },
        "infrastructure_vulnerabilities": {
            "water_system": "Woodland Park water from wells and surface sources; limited capacity for fire suppression demand; some WUI areas on private wells with no hydrant coverage; post-Hayman watershed still producing sediment 20+ years later",
            "power": "Mountain View Electric Association (co-op); overhead lines through heavy timber; frequent outages during fire events; single transmission feed through forested terrain",
            "communications": "Cell coverage adequate in town; gaps in surrounding forest and canyons; Pikes Peak summit repeaters serve area; CO-67 corridor to Cripple Creek has dead spots",
            "medical": "Pikes Peak Regional Hospital (15 beds, critical access); very limited capacity; patients transferred to Colorado Springs hospitals (20+ miles through canyon); ambulance response from COS complicated by Ute Pass congestion",
        },
        "demographics_risk_factors": {
            "population": 8156,
            "seasonal_variation": "Summer tourism and recreation increase population; Cripple Creek casinos (18 miles SW) generate substantial traffic through town; Mueller State Park visitors; some seasonal/vacation homes",
            "elderly_percentage": "22.1% (high retirement community proportion)",
            "mobile_homes": "Significant mobile/manufactured home presence in Teller County WUI; highly vulnerable structures; dispersed rural development",
            "special_needs_facilities": "Pikes Peak Regional Hospital (15 beds); senior care facilities; high elderly percentage; many rural residents without neighbors or nearby assistance; some areas lack street addressing for emergency response",
        },
    },

    # =========================================================================
    # NEVADA (8 cities)
    # =========================================================================

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
    # UTAH (6 cities)
    # =========================================================================

    # =========================================================================
    # 5. BRIAN HEAD, UT -- New (Brian Head Fire 2017, extreme mountain WUI)
    # =========================================================================
    "brian_head_ut": {
        "center": [37.6931, -112.8497],
        "terrain_notes": (
            "Brian Head (pop ~200 permanent, 2,000+ seasonal) is a tiny ski resort town perched "
            "at 9,800 ft elevation on the western rim of the Markagunt Plateau in Iron County, "
            "making it one of the highest-elevation communities in Utah. The town is surrounded "
            "on all sides by the Dixie National Forest, with dense spruce-fir and aspen forests "
            "extending from the town boundary to the 11,307 ft summit of Brian Head Peak. The "
            "2017 Brian Head Fire ignited just south of town on June 17 and burned 71,673 acres "
            "over 38 days, destroying 13 homes and 10 outbuildings within the town. The fire "
            "forced complete evacuation of Brian Head's ~200 permanent residents plus hundreds "
            "of vacation homeowners. The town sits along SR-143, a narrow, winding 2-lane road "
            "that is the sole access route -- connecting to Parowan (14 miles north, elevation "
            "6,000 ft) and Cedar Breaks National Monument to the south. During the 2017 fire, "
            "SR-143 was closed in both directions, trapping some residents until emergency "
            "convoys could be organized. The town's housing stock is predominantly vacation "
            "cabins and condominiums with wood-shake roofs and decking, many surrounded by "
            "dense forest with zero defensible space. Post-fire recovery has been slow, and "
            "much of the surrounding forest remains in early-succession fire-scarred condition."
        ),
        "key_features": [
            {"name": "Brian Head Peak", "bearing": "E", "type": "summit",
             "notes": "11,307 ft; highest point on Markagunt Plateau; ski area on north face; dense spruce-fir forest on all aspects below treeline"},
            {"name": "Dixie National Forest", "bearing": "all directions", "type": "national_forest",
             "notes": "Completely surrounds town; 2017 fire burned through NF land on south, east, and north sides; post-fire dead standing timber remains hazardous"},
            {"name": "Cedar Breaks National Monument", "bearing": "S", "type": "national_monument",
             "notes": "3 miles south; 10,350 ft amphitheater; SR-148 access closed during 2017 fire; surrounding forest heavily burned"},
            {"name": "Brian Head Resort (ski area)", "bearing": "E", "type": "ski_resort",
             "notes": "Two peaks (9,600 and 10,920 ft); ski infrastructure in dense forest; base area is the town itself; economic lifeline for community"},
            {"name": "SR-143 corridor", "bearing": "N-S", "type": "highway",
             "notes": "SOLE access road; 2-lane, steep, winding; closed in both directions during 2017 fire; descends 3,800 ft in 14 miles to Parowan"},
            {"name": "Parowan Canyon", "bearing": "N", "type": "canyon",
             "notes": "SR-143 descends through narrow forested canyon to reach I-15 at Parowan; fire in canyon would trap Brian Head completely"},
        ],
        "elevation_range_ft": [9600, 11307],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Brian Head Fire", "year": 2017, "acres": 71673,
             "details": (
                 "Human-caused fire ignited June 17, 2017, just south of town. Burned for 38 days "
                 "across Iron and Garfield counties. Destroyed 13 primary residences and 10 "
                 "outbuildings/cabins within Brian Head town limits. Complete evacuation of all "
                 "residents and visitors. SR-143 closed in both directions -- some residents "
                 "temporarily trapped. Over 1,500 firefighters deployed at peak. Estimated $40M+ "
                 "suppression cost. Fire burned through dense spruce-fir forest with extreme crown "
                 "fire behavior. One of the largest wildfires in Utah history. Post-fire flooding "
                 "and debris flows caused additional damage to roads and infrastructure."
             )},
        ],
        "evacuation_routes": [
            {"route": "SR-143 North (Parowan Canyon to I-15 at Parowan)", "direction": "N", "lanes": 2,
             "bottleneck": "Steep, winding descent through forested canyon; hairpin turns; single lane effective width in places",
             "risk": "CRITICAL -- sole realistic escape route; fire in Parowan Canyon traps entire town; road was closed during 2017 fire"},
            {"route": "SR-143 South (toward Panguitch via SR-148)", "direction": "S", "lanes": 2,
             "bottleneck": "Narrow plateau road through dense forest; passes Cedar Breaks NM; 30+ miles to Panguitch",
             "risk": "Also closed during 2017 fire; evacuating south means driving through or adjacent to fire zone; not a viable alternative when fire is south of town"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Exposed plateau location receives strong prevailing southwest winds at 15-30 mph, "
                "with gusts exceeding 50 mph during frontal passages. Elevation creates rapid fuel "
                "drying despite cooler temperatures. Diurnal upslope winds from surrounding valleys "
                "drive afternoon fire activity. The 2017 fire exhibited extreme crown fire behavior "
                "in spruce-fir with fire whirls observed, driven by convective column interaction "
                "with terrain winds."
            ),
            "critical_corridors": [
                "Parowan Canyon / SR-143 North -- sole escape route through dense forest",
                "South slopes below town -- origin area of 2017 fire; dense regenerating forest",
                "Brian Head Peak eastern face -- ski area timber extends to town boundary",
                "SR-148 to Cedar Breaks -- forested corridor closed during 2017 fire",
            ],
            "rate_of_spread_potential": (
                "High to extreme in spruce-fir (1-3 mph crown fire). The 2017 fire exhibited "
                "multiple 2,000+ acre growth days with active crown runs. Subalpine fuels at "
                "9,600-11,000 ft are typically moist but extended drought dries them to extreme "
                "flammability. Post-fire standing dead timber mixed with dense regeneration "
                "creates volatile fuel complex."
            ),
            "spotting_distance": (
                "0.5-2.0 miles in spruce-fir crown fire; firebrands lofted by convection columns "
                "at this elevation can travel significant distances downwind. 2017 fire produced "
                "spot fires across SR-143 and multiple drainages."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Brian Head municipal water from local springs and wells on the plateau. System is "
                "minimal, designed for small permanent population. Fire flow capacity is extremely "
                "limited -- hydrant coverage sparse. During 2017 fire, water system could not support "
                "simultaneous structure protection and wildland firefighting operations."
            ),
            "power": (
                "Single transmission line to Brian Head through forested corridor from Parowan. "
                "Fire along SR-143 severs power to entire town. No backup generation for community "
                "infrastructure. 2017 fire caused extended power outage."
            ),
            "communications": (
                "Limited cell coverage; one tower serving town. 2017 fire disrupted communications. "
                "No landline redundancy for most vacation homes. Emergency notification challenging "
                "when most property owners are non-residents. Iron County CodeRED system deployed "
                "but many vacation-home owners not registered."
            ),
            "medical": (
                "No medical facilities in Brian Head. Nearest hospital is Cedar City Hospital (30 mi "
                "down SR-143 and I-15). Emergency medical response time from Cedar City exceeds 30 "
                "minutes under normal conditions; during fire conditions with road closures, EMS "
                "access may be impossible. No helicopter landing zone in town."
            ),
        },
        "demographics_risk_factors": {
            "population": 200,
            "seasonal_variation": (
                "Permanent population only ~200 but ski season (Dec-April) and summer recreation "
                "bring 1,500-2,500 visitors. Town has ~1,500 housing units, overwhelmingly vacation "
                "homes with intermittent occupancy. During 2017 fire, many homes were unoccupied, "
                "complicating evacuation accountability and structure triage. Property owners "
                "scattered across Utah and neighboring states, making emergency communication "
                "extremely difficult."
            ),
            "elderly_percentage": "~25% of permanent residents over 65 (small retirement community at elevation)",
            "mobile_homes": "None -- town is entirely stick-built cabins, condominiums, and resort lodging",
            "special_needs_facilities": (
                "No hospitals, schools, or institutional facilities. Brian Head Resort lodge and "
                "condominium complexes house visitors. No emergency shelter capacity within town. "
                "Nearest shelter is Cedar City (30 mi)."
            ),
        },
    },

    # =========================================================================
    # 1. CEDAR CITY, UT -- Enhanced (Brian Head Fire 2017, Dixie NF)
    # =========================================================================
    "cedar_city_ut": {
        "center": [37.6775, -113.0619],
        "terrain_notes": (
            "Cedar City (pop ~35,000) sits at 5,846 ft elevation on the western edge of the "
            "Markagunt Plateau in Iron County, southwestern Utah. The city occupies a broad valley "
            "floor at the base of the Hurricane Cliffs to the west and the steeply rising Markagunt "
            "Plateau to the east, which climbs from 5,800 ft at the city boundary to over 10,000 ft "
            "at Brian Head Peak within 25 miles. Cedar Canyon (SR-14) cuts a dramatic east-west "
            "corridor from the city up through the Dixie National Forest to Cedar Breaks National "
            "Monument at 10,350 ft. This canyon is the primary fire corridor threatening the city -- "
            "the 2017 Brian Head Fire burned 71,673 acres along the Markagunt Plateau and generated "
            "smoke visible from 100+ miles away, forcing evacuations in Brian Head, Duck Creek Village, "
            "and triggering pre-evacuation warnings for eastern Cedar City neighborhoods. The Dixie "
            "National Forest (1.8 million acres) surrounds the plateau above the city with dense "
            "spruce-fir forests at elevation transitioning to pinyon-juniper woodlands on lower slopes. "
            "Coal Creek flows through the city from Cedar Canyon, providing a direct fire pathway from "
            "the National Forest into residential areas. The city is growing rapidly as a regional hub "
            "for Southern Utah University (~13,000 students) and as a bedroom community for workers "
            "commuting to St. George and recreation areas. WUI development has pushed eastward along "
            "SR-14 and into foothill subdivisions along the base of the plateau, placing new "
            "construction in direct contact with wildland fuels."
        ),
        "key_features": [
            {"name": "Markagunt Plateau", "bearing": "E", "type": "plateau",
             "notes": "Rises from 5,800 ft to 11,307 ft (Brian Head Peak); dense spruce-fir at elevation, pinyon-juniper on lower flanks; source of 2017 Brian Head Fire"},
            {"name": "Cedar Canyon / SR-14", "bearing": "E", "type": "canyon/corridor",
             "notes": "Primary east corridor from city to Cedar Breaks NM; steep-walled canyon channels wind and fire; Coal Creek drainage funnels directly into city"},
            {"name": "Dixie National Forest", "bearing": "E/SE", "type": "national_forest",
             "notes": "1.8 million acres; surrounds Markagunt and Paunsaugunt plateaus; mixed conifer at elevation, extensive pinyon-juniper woodland on lower slopes"},
            {"name": "Coal Creek", "bearing": "E through city", "type": "drainage",
             "notes": "Flows from Cedar Canyon through city center; riparian corridor provides direct fire pathway from NF to residential areas; flash flood risk compounds fire damage"},
            {"name": "Cedar Breaks National Monument", "bearing": "E", "type": "national_monument",
             "notes": "10,350 ft elevation, 23 miles east; amphitheater of eroded red rock; surrounding forests were directly impacted by 2017 Brian Head Fire"},
            {"name": "Hurricane Cliffs", "bearing": "W", "type": "escarpment",
             "notes": "Western escarpment dropping toward the Great Basin; limits western expansion; dry desert winds from the west accelerate fire weather"},
            {"name": "Southern Utah University", "bearing": "central", "type": "institution",
             "notes": "~13,000 students; campus in city center; large transient population unfamiliar with local fire risk; dormitories would require mass evacuation"},
        ],
        "elevation_range_ft": [5600, 10600],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Brian Head Fire", "year": 2017, "acres": 71673,
             "details": (
                 "Human-caused fire ignited June 17, 2017 on Markagunt Plateau. Burned for 38 days across "
                 "Iron and Garfield counties. Destroyed 13 homes and 10 outbuildings in Brian Head. Forced "
                 "evacuation of Brian Head (~200 residents + hundreds of vacation homeowners), Duck Creek "
                 "Village, Panguitch Lake, and surrounding areas. Pre-evacuation warnings issued for parts "
                 "of Cedar City. Over 1,500 personnel deployed. SR-143 and SR-148 closed for weeks. "
                 "Estimated $40M+ in suppression costs. One of the largest fires in Utah history."
             )},
            {"name": "Cedar Canyon Fire", "year": 2019, "acres": 566,
             "details": "Burned east of Cedar City in Dixie NF along SR-14 corridor; prompted red flag warnings; demonstrated recurring ignition risk in Cedar Canyon"},
            {"name": "Shurtz Creek Fire", "year": 2018, "acres": 480,
             "details": "Burned 5 miles south of Cedar City near Shurtz Creek; evacuation of several homes; fire threatened Cedar City water infrastructure"},
        ],
        "evacuation_routes": [
            {"route": "I-15 North (toward Beaver/Provo)", "direction": "N", "lanes": 4,
             "bottleneck": "Main St / 200 N on-ramp congestion; merges with local traffic",
             "risk": "Primary escape route for most residents; functional unless fire crosses I-15 corridor from east-side plateau fires"},
            {"route": "I-15 South (toward St. George/Las Vegas)", "direction": "S", "lanes": 4,
             "bottleneck": "Southern interchange with SR-56; merges with tourist traffic to Zion/Bryce",
             "risk": "Generally safe corridor but smoke from Brian Head-type fires can reduce visibility on I-15"},
            {"route": "SR-14 East (Cedar Canyon to Cedar Breaks)", "direction": "E", "lanes": 2,
             "bottleneck": "Narrow, winding canyon road; no shoulders; limited turnaround points",
             "risk": "EXTREMELY HIGH -- this is the primary fire corridor; closed during Brian Head Fire; evacuees from Brian Head/Duck Creek must descend through active fire zone"},
            {"route": "SR-56 West (toward Modena/Nevada)", "direction": "W", "lanes": 2,
             "bottleneck": "Remote 2-lane highway through desert; 80+ miles to next services",
             "risk": "Low fire risk but impractical for mass evacuation; leads to sparsely populated desert"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Prevailing southwest winds accelerate up Cedar Canyon corridor at 15-30 mph during summer "
                "afternoons. Foehn-type downslope winds off the Markagunt Plateau can produce sudden gusty "
                "conditions in the city, particularly in spring and fall. Thermal convection columns from "
                "plateau fires generate erratic winds that have been observed shifting fire direction "
                "multiple times during the Brian Head Fire."
            ),
            "critical_corridors": [
                "Cedar Canyon / SR-14 -- primary fire funnel from Dixie NF directly into city",
                "Coal Creek drainage -- connects canyon fire to residential areas in city center",
                "East bench subdivisions -- new WUI development at pinyon-juniper interface",
                "SR-143 corridor -- Brian Head to Parowan; fire pathway along western plateau escarpment",
                "Shurtz Creek -- southern approach from NF land to city water infrastructure",
            ],
            "rate_of_spread_potential": (
                "Moderate to high in pinyon-juniper woodland (1-3 mph head fire); extreme in cured grass "
                "understory during drought (4-6 mph). The 2017 Brian Head Fire exhibited extreme fire "
                "behavior with multiple 2,000+ acre growth days driven by wind alignment with terrain. "
                "Slope-driven runs up Cedar Canyon can produce rapid upslope spread exceeding 3 mph."
            ),
            "spotting_distance": (
                "0.5-2.0 miles in conifer stands at elevation; pinyon-juniper produces abundant firebrands "
                "that can spot 0.25-1.0 miles downslope. Long-range spotting from plateau fires into the "
                "city proper (15+ miles) is unlikely but ember showers are possible during extreme events "
                "with strong downslope winds."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Cedar City municipal water comes from Coal Creek watershed and several springs in Cedar "
                "Canyon / Dixie NF. The 2017 Brian Head Fire directly threatened watershed infrastructure. "
                "Post-fire debris flows and ash contamination remain risks for 5-10 years after major burns. "
                "Fire-damaged watersheds produce flash floods that overwhelm city drainage infrastructure."
            ),
            "power": (
                "Rocky Mountain Power serves the region via transmission lines crossing the Markagunt "
                "Plateau and through Cedar Canyon. Fire damage to these lines caused extended outages "
                "during Brian Head Fire. Substation on east side of city is in WUI zone."
            ),
            "communications": (
                "Cell towers on plateau ridges are fire-exposed. Cedar Canyon corridor has limited cell "
                "coverage in lower sections. Emergency alert systems depend on functional cell/internet. "
                "Southern Utah University has independent notification system for campus."
            ),
            "medical": (
                "Cedar City Hospital (~50 beds) is the only acute care facility for 60+ miles. Nearest "
                "Level I trauma is in St. George (55 mi) or Las Vegas (175 mi). Medical surge capacity "
                "is severely limited for mass casualty events from a fast-moving WUI fire."
            ),
        },
        "demographics_risk_factors": {
            "population": 35000,
            "seasonal_variation": (
                "SUU students (~13,000) present Sept-May with reduced summer population. Utah Shakespeare "
                "Festival (July-Oct) draws 100,000+ visitors during peak fire season. Brian Head ski "
                "resort area has large vacation-home population with intermittent occupancy -- many homes "
                "were empty during 2017 fire, complicating structure triage."
            ),
            "elderly_percentage": "~14% over 65; higher in retirement communities on south side of city",
            "mobile_homes": (
                "Several mobile home parks along Main St corridor and south Cedar City; concentrated "
                "vulnerability in areas with limited defensible space. Estimated 8-10% of housing stock."
            ),
            "special_needs_facilities": (
                "Southern Utah University dormitories (1,500+ students), Cedar City Hospital, multiple "
                "assisted living facilities, elementary/secondary schools. Iron County jail (~150 capacity)."
            ),
        },
    },

    # =========================================================================
    # 6. HEBER CITY, UT -- New (Wasatch Back, rapid WUI growth)
    # =========================================================================
    "heber_city_ut": {
        "center": [40.5069, -111.4131],
        "terrain_notes": (
            "Heber City (pop ~16,000) sits at 5,604 ft elevation in the Heber Valley on the "
            "eastern slope of the Wasatch Range, 45 miles southeast of Salt Lake City. The city "
            "occupies a broad mountain valley floor surrounded by the Uinta-Wasatch-Cache National "
            "Forest on three sides: the Wasatch Range to the west (rising to 11,000+ ft), the "
            "Uinta Mountains to the east, and forested foothills to the south. The Provo River "
            "flows north through the valley into Jordanelle and Deer Creek reservoirs. Heber City "
            "is the county seat of Wasatch County, one of Utah's fastest-growing counties (60%+ "
            "growth 2010-2020), with new subdivisions pushing directly into WUI terrain on the "
            "valley margins. The 2024 Yellow Lake Fire (16,053 acres) burned in the Heber-Kamas "
            "Ranger District just 10-15 miles east of town, forcing evacuations in Duchesne Ridge, "
            "Mill Hollow, and Wolf Creek areas. Parleys Canyon to the northwest -- the I-80 "
            "corridor connecting the Wasatch Back to Salt Lake City -- experienced a 562-acre fire "
            "in 2021 that closed the interstate. US-40 through Heber is the primary east-west "
            "corridor for the Wasatch Back, and its intersection with US-189 in Heber City is "
            "the transportation hub for the region. Dense Gambel oak on surrounding foothills "
            "creates extreme fire risk on south-facing slopes from June through October."
        ),
        "key_features": [
            {"name": "Wasatch Range (western wall)", "bearing": "W", "type": "mountain_range",
             "notes": "Rises from 5,600 ft valley floor to 11,000+ ft; dense conifer at elevation, Gambel oak on lower slopes; Provo River corridor cuts through"},
            {"name": "Jordanelle Reservoir", "bearing": "N", "type": "reservoir",
             "notes": "Major reservoir on Provo River; US-40 crosses dam; residential development on shores in WUI terrain; limited firebreak function"},
            {"name": "Deer Creek Reservoir", "bearing": "W", "type": "reservoir",
             "notes": "Provo River impoundment in narrow canyon; US-189 follows canyon to Provo; fire in canyon closes western escape route"},
            {"name": "Heber-Kamas Ranger District", "bearing": "E/NE", "type": "national_forest",
             "notes": "Dense mixed conifer and aspen; 2024 Yellow Lake Fire burned 16,053 acres here; beetle-kill fuel loading increasing"},
            {"name": "Timber Lakes Subdivision", "bearing": "NE", "type": "WUI_development",
             "notes": "Large residential development extending into NF terrain at 7,000-8,000 ft; narrow roads, dense forest, extreme WUI exposure"},
            {"name": "Wasatch State Park", "bearing": "NW", "type": "state_park",
             "notes": "Golf course and recreation area in Gambel oak foothills between Heber and Midway; fire in park would threaten both communities"},
        ],
        "elevation_range_ft": [5400, 8500],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Yellow Lake Fire", "year": 2024, "acres": 16053,
             "details": (
                 "Lightning-caused in Uinta-Wasatch-Cache NF, Heber-Kamas Ranger District. Forced "
                 "evacuations in Duchesne Ridge, Mill Hollow, Wolf Creek, Soapstone Pass. 10% "
                 "contained at peak. Heavy smoke impacted Heber Valley for weeks. Demonstrated "
                 "fire risk in national forest terrain directly adjacent to growing community."
             )},
            {"name": "Parleys Canyon Fire (regional impact)", "year": 2021, "acres": 562,
             "details": "Burned in I-80 corridor 20 miles NW of Heber; closed I-80 (primary route to SLC) for 12+ hours; Heber/Park City residents cut off from Salt Lake Valley"},
            {"name": "Wallsburg Fire", "year": 2012, "acres": 300,
             "details": "Burned in foothills south of Heber Valley in Wallsburg area; grassland/oak fire threatened rural residences; rapid spread in cured grass"},
        ],
        "evacuation_routes": [
            {"route": "US-40 West (through Jordanelle to I-80/Park City)", "direction": "NW", "lanes": 4,
             "bottleneck": "Jordanelle dam crossing; merges with Park City evacuation traffic at Kimball Junction",
             "risk": "Converges with Park City evacuees; I-80 through Parleys Canyon is single corridor vulnerable to fire"},
            {"route": "US-40 East (toward Duchesne/Vernal)", "direction": "E", "lanes": 2,
             "bottleneck": "Daniels Canyon -- narrow, forested canyon climbing to 8,000 ft; limited passing",
             "risk": "Leads into remote Uinta Basin; 2024 Yellow Lake Fire burned near this corridor; long distance to services"},
            {"route": "US-189 South (Provo Canyon to Provo/Orem)", "direction": "SW", "lanes": 2,
             "bottleneck": "Narrow canyon along Provo River; Deer Creek Reservoir area; single road",
             "risk": "Canyon fire would close this route; dense Gambel oak on canyon walls; limited turnaround points"},
            {"route": "SR-113 North (toward Kamas/Mirror Lake Highway)", "direction": "N", "lanes": 2,
             "bottleneck": "Two-lane road through agricultural area; merges with SR-150",
             "risk": "Leads toward fire-prone Uinta terrain; not suitable for large-scale evacuation"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Afternoon westerly upslope winds from the Wasatch Range at 10-20 mph; nocturnal "
                "easterly drainage winds from the Uintas. Strong canyon winds through Provo Canyon "
                "and Daniels Canyon during frontal passages. Gambel oak on south-facing foothills "
                "cures to extreme flammability by July. Valley inversions common, trapping smoke "
                "and creating multi-day air quality events."
            ),
            "critical_corridors": [
                "Western foothills -- Gambel oak interface between Heber and Wasatch Range",
                "Timber Lakes / NE foothills -- WUI development extending into NF terrain",
                "Provo Canyon / US-189 -- narrow canyon with oak/conifer, western escape route",
                "Daniels Canyon / US-40 East -- forested canyon, eastern escape route",
                "Jordanelle reservoir margins -- WUI development along reservoir shores",
            ],
            "rate_of_spread_potential": (
                "Extreme in Gambel oak on south-facing slopes (4-8 mph head fire in wind-driven "
                "events). Moderate in conifer at elevation (1-2 mph crown fire). Grass/sage valley "
                "floor supports 3-5 mph spread. The combination of oak foothills and rapid WUI "
                "development creates conditions similar to the devastating Traverse Fire scenario "
                "in nearby Lehi (2022, 523 acres, 0 structures but demonstrated extreme oak fire)."
            ),
            "spotting_distance": (
                "0.25-0.75 miles in Gambel oak; 0.5-1.5 miles in mixed conifer. Oak embers are "
                "prolific and ignite cedar-shake roofs and dry landscaping in WUI neighborhoods. "
                "Many new Heber subdivisions have inadequate defensible space."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Heber City municipal water from springs and wells in the Provo River watershed. "
                "System expanding rapidly with population growth but fire flow capacity in newer "
                "WUI subdivisions may lag behind development. Upper Timber Lakes area homes on "
                "private wells with minimal fire flow."
            ),
            "power": (
                "Rocky Mountain Power; transmission from Provo Canyon corridor. Fire in Provo Canyon "
                "could sever power and evacuation route simultaneously. Rapid load growth from new "
                "development strains grid capacity."
            ),
            "communications": (
                "Good cellular in valley floor; gaps in canyon corridors and mountain subdivisions. "
                "Wasatch County emergency notification system deployed. Many new residents unfamiliar "
                "with local fire risk. Second-home owners may not be registered for alerts."
            ),
            "medical": (
                "Heber Valley Hospital (~20 beds) provides basic emergency care. Nearest major "
                "hospitals in Provo (30 mi through Provo Canyon) or Salt Lake City (45 mi through "
                "Parleys Canyon). Both routes are fire-vulnerable canyon corridors."
            ),
        },
        "demographics_risk_factors": {
            "population": 16000,
            "seasonal_variation": (
                "Rapid year-round growth (~4% annually). Summer recreation and second-home occupancy "
                "increases population by 30-40%. Nearby Soldier Hollow (2002 Olympics venue) and "
                "Wasatch State Park draw additional visitors. Many new residents are transplants from "
                "Salt Lake Valley with limited wildfire experience."
            ),
            "elderly_percentage": "~11% over 65 (younger-skewing due to family growth)",
            "mobile_homes": (
                "Some manufactured housing on east side of Heber and in unincorporated Wasatch County. "
                "Estimated 5-8% of housing stock."
            ),
            "special_needs_facilities": (
                "Heber Valley Hospital, multiple schools, senior facilities. No major institutional "
                "population. Growing number of daycare/preschool facilities serving commuter families."
            ),
        },
    },

    # =========================================================================
    # 7. MIDWAY, UT -- New (Wasatch Back, surrounded by NF)
    # =========================================================================
    "midway_ut": {
        "center": [40.5122, -111.4733],
        "terrain_notes": (
            "Midway (pop ~5,300) is a small agricultural-turned-resort community at 5,560 ft "
            "elevation in the western Heber Valley, nestled against the base of the Wasatch Range "
            "in Wasatch County. The town sits in a scenic bowl with the steep western wall of the "
            "Wasatch Range rising immediately to the west and north, reaching 11,000+ ft within "
            "4 miles. The Uinta-Wasatch-Cache National Forest boundary is less than 1 mile from "
            "the town center in several directions. Dense Gambel oak blankets the foothills between "
            "town and the NF boundary, creating a continuous fuel bed from the valley floor to the "
            "conifer zone above 7,000 ft. Snake Creek canyon cuts westward from Midway into the "
            "Wasatch Range, carrying both a road and the Snake Creek drainage that channels wind "
            "and potential fire directly toward town. Wasatch State Park (22,000 acres) occupies "
            "the hills between Midway and Heber City with oak/sage vegetation. The Homestead "
            "Resort and Crater hot springs are major tourist draws. Swiss-heritage town character "
            "has attracted luxury development, but many properties are older with wood construction "
            "and no defensible space. The town has experienced rapid growth as part of the Wasatch "
            "Back boom, with new subdivisions extending upslope into oak-covered terrain."
        ),
        "key_features": [
            {"name": "Wasatch Range (western wall)", "bearing": "W/NW", "type": "mountain_range",
             "notes": "Rises from 5,560 ft to 11,000+ ft within 4 miles; dense forest above 7,000 ft; Gambel oak on lower slopes directly above town"},
            {"name": "Snake Creek Canyon", "bearing": "W", "type": "canyon/drainage",
             "notes": "Drainage from Wasatch Range through Midway; road access up canyon; channels wind and potential fire directly toward residential areas"},
            {"name": "Wasatch State Park", "bearing": "E/NE", "type": "state_park",
             "notes": "22,000 acres of oak/sage/grass between Midway and Heber; fire in park threatens both communities; golf courses provide limited firebreak"},
            {"name": "Homestead Resort / Crater", "bearing": "central", "type": "resort",
             "notes": "Historic hot spring resort; tourist draw bringing visitors unfamiliar with fire risk; wooden structures in oak-interface setting"},
            {"name": "Pine Creek drainage", "bearing": "NW", "type": "drainage",
             "notes": "Forested drainage from NF through residential development north of Midway; dense mixed conifer and oak"},
            {"name": "Dutch Hollow development", "bearing": "W", "type": "WUI_development",
             "notes": "Upscale subdivision extending into oak-covered foothills; narrow roads with limited egress; minimal defensible space on many lots"},
        ],
        "elevation_range_ft": [5400, 8000],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Yellow Lake Fire (regional impact)", "year": 2024, "acres": 16053,
             "details": "Burned 10-15 miles east of Midway in Heber-Kamas district; heavy smoke impacted Midway for weeks; demonstrated regional fire exposure"},
            {"name": "Midway foothills grass fire", "year": 2020, "acres": 50,
             "details": "Small but fast-moving grass fire on south-facing slopes above Midway; initial attack successful but demonstrated how quickly fire approaches town from oak foothills"},
        ],
        "evacuation_routes": [
            {"route": "SR-113 East (to Heber City / US-40)", "direction": "E", "lanes": 2,
             "bottleneck": "Single corridor through Wasatch State Park; merges with Heber traffic on US-40",
             "risk": "Fire in Wasatch State Park would close this route; only realistic escape eastward"},
            {"route": "SR-113 North / Snake Creek Road (toward Park City)", "direction": "NW", "lanes": 2,
             "bottleneck": "Narrow mountain road climbing over ridge between drainages; limited capacity",
             "risk": "Passes through dense oak and conifer; fire on Wasatch slopes would threaten this corridor"},
            {"route": "River Road South (toward Charleston/US-189)", "direction": "S", "lanes": 2,
             "bottleneck": "Local road through agricultural area; limited capacity; eventually reaches Deer Creek / Provo Canyon",
             "risk": "Indirect route; fire in Provo Canyon blocks onward travel to Provo/SLC"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Afternoon westerly winds descending Wasatch slopes at 10-20 mph; nocturnal drainage "
                "from Snake Creek and Pine Creek canyons. The bowl-like setting concentrates wind and "
                "traps smoke during inversions. Gambel oak on south- and west-facing slopes cures to "
                "extreme flammability by mid-July."
            ),
            "critical_corridors": [
                "Snake Creek Canyon -- direct fire pathway from NF to town center",
                "Western oak foothills -- continuous fuel from NF boundary to residential areas",
                "Pine Creek drainage -- forested corridor through north Midway development",
                "Wasatch State Park -- oak/sage connecting Midway to Heber; fire spreads both directions",
            ],
            "rate_of_spread_potential": (
                "Extreme in Gambel oak (4-8 mph head fire in wind events). Grass/sage in State Park "
                "supports 3-5 mph spread. The proximity of NF conifer to town through continuous oak "
                "understory means a crown fire on the Wasatch slopes could reach residential areas "
                "within 1-2 hours of ignition under critical fire weather."
            ),
            "spotting_distance": (
                "0.25-0.75 miles in oak; 0.5-1.5 miles from conifer crown fire above. Wood-shake "
                "roofs and cedar fencing on older Midway homes provide receptive fuel beds for "
                "firebrands. Limited fire-resistant landscaping in established neighborhoods."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Midway municipal water from local springs and wells. Small system designed for "
                "5,000 residents; fire flow capacity limited in WUI neighborhoods. Hydrant coverage "
                "thins in upslope developments. Growth has stressed water supply."
            ),
            "power": (
                "Rocky Mountain Power; transmission enters from Heber City direction. Overhead lines "
                "through oak foothills are fire-exposed. Extended outage likely during WUI fire event."
            ),
            "communications": (
                "Good cellular in town core; some gaps in canyon and foothill areas. Wasatch County "
                "emergency notification deployed. Many second-home and vacation-rental occupants "
                "not registered for local alerts."
            ),
            "medical": (
                "No hospital in Midway. Closest is Heber Valley Hospital (5 mi east). Major trauma "
                "care requires transport to Provo (30 mi) or Salt Lake City (45 mi) through "
                "fire-vulnerable canyon corridors."
            ),
        },
        "demographics_risk_factors": {
            "population": 5300,
            "seasonal_variation": (
                "Growing year-round but summer recreation and second-home occupancy increase population "
                "by 25-35%. Swiss Days festival (Labor Day weekend) draws 50,000+ visitors -- during "
                "peak fire season. Growing vacation-rental market brings unfamiliar visitors."
            ),
            "elderly_percentage": "~15% over 65 (retirement/lifestyle community character)",
            "mobile_homes": "Minimal; town is predominantly single-family residential and resort condominiums",
            "special_needs_facilities": (
                "Elementary school, assisted living facilities. No hospital. Homestead Resort and "
                "other lodging house tourists. No institutional population."
            ),
        },
    },

    # =========================================================================
    # 2. PARK CITY, UT -- Enhanced (Wasatch Range WUI, resort town)
    # =========================================================================
    "park_city_ut": {
        "center": [40.6461, -111.4980],
        "terrain_notes": (
            "Park City (pop ~8,500 permanent) occupies a narrow mountain valley at 6,900-7,200 ft "
            "elevation on the eastern slope of the Wasatch Range in Summit County. The city is built "
            "along a historic mining-era Main Street in a steep-sided gulch, with residential "
            "development climbing forested mountainsides to elevations exceeding 8,500 ft. The "
            "Uinta-Wasatch-Cache National Forest surrounds the city on three sides, with dense "
            "stands of Gambel oak, aspen, Douglas fir, and mixed conifer extending to the backyards "
            "of thousands of homes. Two world-class ski resorts (Deer Valley and Park City Mountain) "
            "have driven explosive WUI development with luxury homes built deep into forested terrain "
            "on narrow, winding mountain roads. The Wasatch Back region (Park City, Heber, Midway, "
            "Kamas) is Utah's fastest-growing WUI area, with Summit County adding ~2,000 residents "
            "annually. Parleys Canyon (I-80 corridor) connects Park City to Salt Lake City through "
            "a narrow, fire-prone canyon with dense Gambel oak -- the 2021 Parleys Canyon fire closed "
            "I-80 and forced evacuations. The 2024 Yellow Lake Fire burned 16,053 acres in the "
            "Uinta-Wasatch-Cache NF just 15 miles east of town in the Heber-Kamas Ranger District, "
            "triggering evacuations. Park City Fire District has identified over 4,000 structures "
            "in the WUI zone with inadequate defensible space."
        ),
        "key_features": [
            {"name": "Deer Valley Resort", "bearing": "SE", "type": "ski_resort/WUI",
             "notes": "Luxury resort development extending to 9,400 ft; homes built in dense aspen/conifer forest on steep slopes; narrow single-access roads"},
            {"name": "Park City Mountain Resort", "bearing": "W", "type": "ski_resort/WUI",
             "notes": "Largest ski resort in US; Canyons Village side has extensive WUI development in forested terrain; Jupiter Peak area is extreme fire terrain"},
            {"name": "Historic Main Street", "bearing": "central", "type": "historic_district",
             "notes": "19th-century mining town core in narrow gulch; densely packed wood-frame buildings; extremely limited access; fire would spread rapidly through connected structures"},
            {"name": "Parleys Canyon / I-80", "bearing": "W", "type": "canyon/corridor",
             "notes": "Primary access to Salt Lake City; dense Gambel oak (highly flammable); 2021 fire closed I-80; single realistic evacuation corridor westward"},
            {"name": "Uinta-Wasatch-Cache NF", "bearing": "E/S/N", "type": "national_forest",
             "notes": "Surrounds city on three sides; mixed oak/aspen/conifer; 2024 Yellow Lake Fire burned 16,053 acres in Heber-Kamas district 15 mi east"},
            {"name": "Snyderville Basin", "bearing": "NW", "type": "developed_basin",
             "notes": "Rapidly growing unincorporated area west of Park City; WUI development in oak/sage foothills; Kimball Junction commercial hub"},
            {"name": "Thaynes Canyon", "bearing": "W", "type": "drainage/WUI",
             "notes": "Residential canyon extending from Old Town into NF; dense oak understory; limited egress; identified by PCFD as extreme WUI risk"},
        ],
        "elevation_range_ft": [6200, 9600],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Yellow Lake Fire", "year": 2024, "acres": 16053,
             "details": (
                 "Lightning-caused fire in Uinta-Wasatch-Cache NF in Heber-Kamas Ranger District, "
                 "approximately 15 miles east of Park City. Forced evacuations in Duchesne Ridge, "
                 "Mill Hollow, Wolf Creek, and Soapstone Pass areas of Wasatch County. 10% contained "
                 "at peak; heavy smoke impacted Park City and Heber Valley for weeks."
             )},
            {"name": "Parleys Canyon Fire", "year": 2021, "acres": 562,
             "details": (
                 "Ignited August 14 near Lambs Canyon along I-80 corridor. Forced closure of I-80 -- "
                 "the sole freeway connection between Park City and Salt Lake City -- for 12+ hours. "
                 "Evacuations in Summit Park and Lambs Canyon. Burned in dense Gambel oak with "
                 "extreme rate of spread. Demonstrated catastrophic vulnerability of the I-80 corridor."
             )},
            {"name": "Round Valley Fire", "year": 2018, "acres": 40,
             "details": "Small but significant fire in open space directly adjacent to residential neighborhoods in Quinn's Junction area; rapid initial spread in cured grass; demonstrated how quickly fire approaches homes in Park City"},
            {"name": "Rockport Fire", "year": 2002, "acres": 3000,
             "details": "Burned in Wanship/Rockport area 15 miles east of Park City; forced evacuations along Weber River corridor; demonstrated fire risk in eastern Summit County"},
        ],
        "evacuation_routes": [
            {"route": "I-80 West (Parleys Canyon to Salt Lake City)", "direction": "W", "lanes": 4,
             "bottleneck": "Narrow canyon; dense Gambel oak on both sides; 2021 fire closed this route entirely",
             "risk": "CRITICAL -- sole freeway connection to Salt Lake Valley; fire in Parleys Canyon eliminates primary evacuation route for 30,000+ residents/visitors"},
            {"route": "SR-224 North (toward I-80 at Kimball Junction)", "direction": "NW", "lanes": 4,
             "bottleneck": "Kimball Junction roundabout; merges Park City, Snyderville Basin, and I-80 traffic",
             "risk": "Convergence point for entire western evacuation; gridlock probable during mass evacuation"},
            {"route": "SR-248 East (toward Kamas/Heber)", "direction": "E", "lanes": 2,
             "bottleneck": "Two-lane road through Brown's Canyon; limited capacity",
             "risk": "Leads toward fire-prone terrain; 2024 Yellow Lake Fire burned in this direction; evacuating east may be counterproductive"},
            {"route": "SR-224 South (Deer Valley to US-40)", "direction": "SE", "lanes": 2,
             "bottleneck": "Winding mountain road through dense forest; single lane each direction",
             "risk": "Deer Valley residents have limited egress; roads were not designed for mass evacuation; hundreds of homes on dead-end mountain roads"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Diurnal canyon winds dominate: afternoon up-canyon (westerly) from Salt Lake Valley "
                "through Parleys Canyon at 10-20 mph; nighttime drainage winds (easterly) from Uinta "
                "Range. Southwest winds during frontal passages can produce extreme fire weather. Gambel "
                "oak on south-facing slopes cures to extreme flammability by late July. Inversions trap "
                "smoke in the Park City valley for days during regional fire events."
            ),
            "critical_corridors": [
                "Parleys Canyon / I-80 -- dense Gambel oak corridor directly connecting SLC to Park City",
                "Thaynes Canyon -- WUI drainage from Main Street into NF timber",
                "Deer Valley -- luxury homes in dense forest with narrow single-access roads",
                "Empire Canyon -- steep terrain with mixed oak/conifer above residential development",
                "Round Valley -- open grass/sage interface between Snyderville Basin and NF",
                "Kimball Junction to Jeremy Ranch -- I-80 corridor WUI with oak-covered slopes",
            ],
            "rate_of_spread_potential": (
                "Extreme in Gambel oak -- the most fire-prone shrub species in the Intermountain West. "
                "Cured oak produces 4-8 mph head fire rates of spread with 50-100 ft flame lengths in "
                "wind-driven events. The 2021 Parleys Canyon fire demonstrated rapid spread through oak "
                "that overwhelmed initial attack. Conifer stands above 8,000 ft support crown fire runs "
                "of 1-3 mph with heavy spotting. Steep terrain multiplies effective wind speed."
            ),
            "spotting_distance": (
                "0.25-0.75 miles in Gambel oak (prolific ember producer); 0.5-1.5 miles in mixed "
                "conifer. Ember transport into residential areas is the primary ignition mechanism -- "
                "wood shake roofs and cedar decking on many older homes provide receptive fuel beds. "
                "Park City Fire District has campaigned for roof material upgrades but compliance is "
                "incomplete, particularly on historic Main Street structures."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Park City municipal water from Weber River watershed and mountain springs. System "
                "designed for resort-town peak demand (winter ski season) but fire flow requirements "
                "during summer WUI events may exceed capacity in upper-elevation neighborhoods. "
                "Hydrant spacing thins above 7,500 ft where WUI exposure is greatest. Many Deer Valley "
                "homes are on private water systems with limited fire flow."
            ),
            "power": (
                "Rocky Mountain Power serves the area via transmission lines through Parleys Canyon "
                "and over the Wasatch Range. Canyon fire would threaten both power delivery and the "
                "evacuation route simultaneously. Mountain substations serve resort areas but are "
                "exposed to wildfire. Widespread use of electric heating means winter power loss is "
                "life-threatening, though summer fire season is the primary concern."
            ),
            "communications": (
                "Good cellular coverage in city core and resort bases; significant gaps in backcountry "
                "and some high-elevation residential areas. Summit County emergency notification system "
                "(Everbridge) deployed. Park City Fire District conducts annual WUI awareness campaigns. "
                "Many vacation homes have no landline -- owners may not receive emergency alerts."
            ),
            "medical": (
                "Park City Hospital / Intermountain Health (~30 beds) provides basic emergency care. "
                "Nearest Level I trauma is University of Utah Hospital in Salt Lake City -- 32 miles "
                "west through Parleys Canyon (the same canyon vulnerable to fire closure). Medical "
                "evacuation by helicopter is feasible but smoke may limit operations. Summer population "
                "of 25,000-40,000 far exceeds local medical capacity."
            ),
        },
        "demographics_risk_factors": {
            "population": 8500,
            "seasonal_variation": (
                "Permanent population ~8,500 but effective population swings dramatically: winter ski "
                "season brings 20,000-30,000 visitors/week; Sundance Film Festival (January) adds "
                "50,000+ for 10 days. Summer population 15,000-25,000 with tourists, second homeowners, "
                "and outdoor recreation visitors. Peak fire season (July-September) coincides with heavy "
                "recreation and vacation-home occupancy. An estimated 40-60% of Park City housing stock "
                "is second homes or vacation rentals with intermittent occupancy."
            ),
            "elderly_percentage": "~16% over 65 (higher than state average; affluent retirees in Deer Valley area)",
            "mobile_homes": (
                "Minimal within Park City proper due to high property values. Some manufactured housing "
                "in Snyderville Basin and along US-40 corridor outside city limits."
            ),
            "special_needs_facilities": (
                "Park City Hospital, multiple assisted living/senior facilities, several schools and "
                "daycare centers. Winter Park / Silver Star condominium complexes house thousands of "
                "visitors. No jail or large institutional population. Large tourist population unfamiliar "
                "with evacuation routes and local hazards."
            ),
        },
    },

    # =========================================================================
    # 8. SPRINGDALE, UT -- New (Zion NP gateway, narrow canyon, single road)
    # =========================================================================
    "springdale_ut": {
        "center": [37.1890, -112.9988],
        "terrain_notes": (
            "Springdale (pop ~530 permanent) is the gateway community to Zion National Park, "
            "located at 3,900 ft elevation in a narrow canyon of the Virgin River in Washington "
            "County, southwestern Utah. The town stretches approximately 2 miles along SR-9, which "
            "is the sole road through town and the only vehicle access to Zion's main canyon. "
            "Towering Navajo sandstone cliffs (1,000-2,000 ft vertical walls) flank the town on "
            "both sides, with pinyon-juniper and desert scrub vegetation on accessible slopes and "
            "benches. The Virgin River flows south through the canyon floor, with the entire town "
            "built in the narrow floodplain and on low benches between the river and canyon walls. "
            "SR-9 is the ONLY road -- there is no alternative route. To the north, SR-9 enters "
            "Zion NP through the park entrance; to the south, it passes through Rockville to reach "
            "I-15 at Hurricane (20 miles). In June 2024, the Rockville Fire (72 acres) burned near "
            "Rockville and forced closure of SR-9 between Rockville and Springdale, temporarily "
            "isolating the town. Zion National Park receives 4.5+ million visitors annually, with "
            "most accessing the main canyon through Springdale. During peak season (May-October), "
            "daily visitor counts can exceed 15,000 -- all funneled through this single-road "
            "canyon town. The combination of extreme terrain confinement, a single access road, "
            "massive transient visitor population, and surrounding wildland fuels makes Springdale "
            "one of the most evacuation-constrained communities in the American West."
        ),
        "key_features": [
            {"name": "Zion Canyon walls", "bearing": "E/W", "type": "canyon_walls",
             "notes": "1,000-2,000 ft vertical Navajo sandstone cliffs on both sides of town; no lateral escape; create wind tunnel effect and trap smoke"},
            {"name": "Virgin River", "bearing": "N-S through town", "type": "river",
             "notes": "Flows through narrow canyon floor; flash flood risk compounds fire emergency; riparian vegetation provides limited fuel break"},
            {"name": "SR-9 (sole road)", "bearing": "N-S", "type": "highway",
             "notes": "ONLY road through Springdale; 2 lanes; connects to Zion NP north and I-15 south; 2024 Rockville Fire closed this route; zero alternatives"},
            {"name": "Zion National Park entrance", "bearing": "N", "type": "park_entrance",
             "notes": "Main canyon entrance immediately north of Springdale; 4.5M+ annual visitors; park shuttle system originates in Springdale"},
            {"name": "Rockville", "bearing": "S", "type": "community",
             "notes": "Small community 2 miles south along SR-9; 2024 fire burned here; SR-9 closure at Rockville isolates Springdale entirely"},
            {"name": "Watchman Campground (Zion NP)", "bearing": "N", "type": "campground",
             "notes": "NPS campground at park entrance adjacent to Springdale; 190 sites; campers would join town evacuation through single road"},
        ],
        "elevation_range_ft": [3800, 5900],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Rockville Fire", "year": 2024, "acres": 72,
             "details": (
                 "Burned in steep, rocky terrain near Rockville, 2 miles south of Springdale. SR-9 "
                 "closed between Rockville and Springdale, temporarily isolating the town and all "
                 "visitors within it. 100% contained after several days. Small fire but demonstrated "
                 "the catastrophic isolation risk when SR-9 is closed -- no alternative route exists."
             )},
            {"name": "Kolob Canyon Fire", "year": 2025, "acres": 350,
             "details": "Lightning-caused fire in Kolob Canyons section of Zion NP (northern district); prompted closures in park; smoke impacted Springdale area"},
            {"name": "Forsyth Canyon Fire (regional)", "year": 2025, "acres": 5000,
             "details": "Burned west of Zion NP; smoke blanketed Springdale and Zion Canyon for days; demonstrated how regional fires impact air quality in the narrow canyon"},
        ],
        "evacuation_routes": [
            {"route": "SR-9 South (through Rockville to I-15 at Hurricane)", "direction": "S", "lanes": 2,
             "bottleneck": "Narrow canyon road; passes through Rockville (2024 fire site); 20 miles to I-15",
             "risk": "CRITICAL -- sole escape route; fire at Rockville cuts off Springdale entirely; during peak season, 5,000-15,000 visitors plus residents must evacuate on this 2-lane road"},
            {"route": "SR-9 North (into Zion NP -- dead end for vehicles)", "direction": "N", "lanes": 2,
             "bottleneck": "Enters park but Zion Canyon is a dead end for vehicles; Zion-Mt. Carmel tunnel restricts large vehicles",
             "risk": "NOT a viable evacuation route -- leads deeper into canyon with no exit; Zion-Mt. Carmel Highway over to east side is 25+ miles of winding mountain road and may also be fire-threatened"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Strong canyon wind effect: afternoon up-canyon (northerly) winds at 10-25 mph as "
                "desert heat draws air into Zion Canyon; nocturnal drainage (southerly) as cold air "
                "flows downcanyon. Canyon walls create venturi acceleration of winds. Extreme solar "
                "heating of south-facing sandstone walls desiccates vegetation on benches. Hot, dry "
                "Santa Ana-type conditions from the Mojave can produce extreme fire weather in "
                "spring and fall transitional seasons."
            ),
            "critical_corridors": [
                "SR-9 corridor -- any fire along the highway isolates the town",
                "Virgin River floodplain -- only developable land; entire town is in this corridor",
                "Rockville gap -- fire between Rockville and Springdale severs sole exit",
                "Bench vegetation above town -- pinyon-juniper on accessible slopes can carry fire to structures",
                "Watchman area -- fire near park entrance traps both campers and town residents",
            ],
            "rate_of_spread_potential": (
                "Moderate in pinyon-juniper (1-2 mph) but terrain amplifies spread on steep slopes. "
                "Desert grass and scrub on lower slopes supports 2-4 mph spread in wind-driven events. "
                "Narrow canyon concentrates fire products (heat, embers, smoke) -- even a small fire "
                "can produce town-threatening conditions due to confined terrain."
            ),
            "spotting_distance": (
                "0.25-0.5 miles in pinyon-juniper; limited by canyon width (town is only 0.2-0.5 miles "
                "wide). Firebrands from canyon walls can fall directly onto structures below. Updrafts "
                "along heated cliff faces can loft embers unpredictably."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Springdale municipal water from springs and Virgin River watershed. Small system "
                "designed for ~500 permanent residents; vastly overwhelmed during peak tourist "
                "season. Fire flow capacity is minimal. No redundancy in water supply."
            ),
            "power": (
                "Single transmission line following SR-9 through Virgin River canyon. Any fire along "
                "the canyon severs power to Springdale and all facilities within Zion NP's main canyon. "
                "No backup generation for town infrastructure."
            ),
            "communications": (
                "Cell coverage limited in canyon due to terrain shadowing. NPS has radio network for "
                "park operations. Emergency notification for town relies on cell/internet that may fail "
                "during power outage. Many visitors are international tourists who may not receive or "
                "understand English-language emergency alerts."
            ),
            "medical": (
                "No medical facilities in Springdale. Nearest emergency care is Dixie Regional Medical "
                "Center in St. George (40 mi via I-15) or Hurricane urgent care (20 mi). Medical "
                "evacuation by helicopter is extremely limited due to canyon terrain and narrow "
                "landing zones. During SR-9 closure, ground ambulance access is impossible."
            ),
        },
        "demographics_risk_factors": {
            "population": 530,
            "seasonal_variation": (
                "Permanent population ~530 but Zion NP receives 4.5+ million visitors annually, "
                "with most accessing through Springdale. Peak daily visitor counts exceed 15,000 in "
                "summer -- a 30:1 visitor-to-resident ratio. Hotels, lodges, and vacation rentals "
                "in Springdale house 2,000-3,000 guests nightly during peak season. Watchman "
                "Campground adds 700+ campers. The combination of a massive transient population, "
                "zero local knowledge, and a single-road canyon creates the worst evacuation scenario "
                "of any NP gateway community in the US."
            ),
            "elderly_percentage": "~18% of permanent residents over 65 (small community skews older)",
            "mobile_homes": "None -- zoning prohibits; all construction is stick-built or resort-style lodging",
            "special_needs_facilities": (
                "No hospital, no school (students attend in Hurricane). Multiple hotels and lodges "
                "housing thousands of visitors nightly. Zion NP Visitor Center and shuttle staging "
                "area. No emergency shelter capacity within town."
            ),
        },
    },

    # =========================================================================
    # WYOMING (6 cities)
    # =========================================================================

    # =========================================================================
    # 4. CODY, WY -- Enhanced (Shoshone NF, Yellowstone gateway)
    # =========================================================================
    "cody_wy": {
        "center": [44.5263, -109.0565],
        "terrain_notes": (
            "Cody (pop ~10,000) sits at 5,016 ft elevation in the Bighorn Basin of northwestern "
            "Wyoming, at the confluence of the North Fork and South Fork of the Shoshone River. "
            "The town is positioned at the eastern gateway to Yellowstone National Park, with "
            "US-14/16/20 (the Buffalo Bill Cody Scenic Byway) running 52 miles west through the "
            "Shoshone National Forest to Yellowstone's East Entrance. The Absaroka Range rises "
            "dramatically to the west and south, with peaks exceeding 12,000 ft, while the Bighorn "
            "Basin extends as arid sagebrush-grassland to the east. The Shoshone National Forest "
            "(2.4 million acres, America's first NF, established 1891) covers the mountainous "
            "terrain west and south of Cody with dense Douglas fir, lodgepole pine, and spruce-fir "
            "forests. The 1937 Blackwater Fire, 35 miles west of Cody in the Shoshone NF, killed "
            "15 firefighters -- the fourth deadliest wildfire for firefighters in US history -- and "
            "led directly to creation of the smokejumper program. More recently, the Clearwater Fire "
            "(2024) burned along the North Fork Shoshone corridor, closing the highway to "
            "Yellowstone and evacuating campgrounds and residences along the scenic byway. The "
            "North Fork and South Fork valleys extending west from Cody contain hundreds of "
            "homes, guest ranches, and lodges interspersed in National Forest land, creating "
            "a linear WUI corridor with single-road access."
        ),
        "key_features": [
            {"name": "Absaroka Range", "bearing": "W/SW", "type": "mountain_range",
             "notes": "Volcanic peaks to 12,000+ ft; dense conifer forests on lower slopes; headwaters of Shoshone River forks; extremely rugged terrain limits firefighting access"},
            {"name": "North Fork Shoshone River / Scenic Byway", "bearing": "W", "type": "corridor",
             "notes": "US-14/16/20 to Yellowstone East Entrance; 52-mile linear WUI corridor with lodges, guest ranches, campgrounds; single road; Clearwater Fire 2024 closed this route"},
            {"name": "South Fork Shoshone River", "bearing": "SW", "type": "corridor",
             "notes": "Valley with residential development, ranches extending 30+ miles into Shoshone NF; single road (South Fork Road) for access; dead-end corridor"},
            {"name": "Shoshone National Forest", "bearing": "W/S", "type": "national_forest",
             "notes": "2.4 million acres; America's first NF (1891); dense conifer with significant deadfall from fire suppression; Blackwater Fire (1937) killed 15 here"},
            {"name": "Buffalo Bill Reservoir", "bearing": "W", "type": "reservoir",
             "notes": "Shoshone River impoundment 6 miles west of Cody; dam and spillway infrastructure; reservoir provides limited firebreak in narrow canyon"},
            {"name": "Rattlesnake Mountain", "bearing": "NW", "type": "mountain",
             "notes": "8,500 ft; sage/grass lower slopes, timber above; directly above North Fork road; Rattlesnake Fire (2024) burned here"},
            {"name": "Cedar Mountain", "bearing": "S", "type": "mountain",
             "notes": "7,899 ft; juniper/Douglas fir; rises directly south of Cody; fire here would threaten south-side residential development"},
        ],
        "elevation_range_ft": [4900, 12500],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Blackwater Fire", "year": 1937, "acres": 1700,
             "details": (
                 "Lightning-caused fire Aug 18, 1937, on Clayton Mountain 35 miles west of Cody in "
                 "Shoshone NF. Winds shifted abruptly from SW to W at 30 mph, causing crown runs and "
                 "spotting over fire lines. 15 firefighters killed (9 on fireline, 6 from burns later), "
                 "38 burned. Fourth deadliest wildfire for firefighters in US history. Directly led to "
                 "development of the smokejumper program (1939) and modern fire shelter research."
             )},
            {"name": "Clearwater Fire", "year": 2024, "acres": 4500,
             "details": (
                 "Started July 19 on Shoshone NF along North Fork corridor. Evacuated Elk Fork "
                 "Campground, Wapiti Campground, Wapiti Ranger Station. Temporarily closed US-14/16/20 "
                 "to Yellowstone East Entrance, severing primary tourist access. Burned in steep, "
                 "timbered terrain with limited road access for suppression."
             )},
            {"name": "Rattlesnake Fire", "year": 2024, "acres": 1200,
             "details": "Burned on Rattlesnake Mountain NW of Cody; forced evacuations along North Fork road; two homes lost in Park County fires during same period"},
            {"name": "Reef Creek Fire", "year": 2011, "acres": 5000,
             "details": "Burned in Shoshone NF south of Yellowstone East Entrance corridor; closed sections of scenic byway; demonstrated fire risk along tourist corridor"},
        ],
        "evacuation_routes": [
            {"route": "US-14/16/20 East (toward Bighorn Basin/Thermopolis)", "direction": "E", "lanes": 2,
             "bottleneck": "Single corridor through Bighorn Basin; 80+ miles to Thermopolis",
             "risk": "Low fire risk (arid basin) but limited capacity and very long distance to significant population centers"},
            {"route": "US-14/16/20 West (toward Yellowstone East Entrance)", "direction": "W", "lanes": 2,
             "bottleneck": "Narrow canyon along North Fork; single road; campgrounds and lodges create congestion",
             "risk": "EXTREME -- this corridor is the primary fire zone; Clearwater Fire closed it; evacuating toward active fire is counterproductive"},
            {"route": "WY-120 South (toward Meeteetse/Thermopolis)", "direction": "S", "lanes": 2,
             "bottleneck": "Two-lane highway through arid terrain; 30 miles to Meeteetse, 85 to Thermopolis",
             "risk": "Moderate -- passes through sage/grassland fire terrain but generally lower risk"},
            {"route": "WY-120 North (toward Powell/Montana)", "direction": "N", "lanes": 2,
             "bottleneck": "Two-lane highway; 25 miles to Powell; crosses Shoshone River valley",
             "risk": "Generally safest evacuation direction; leads to agricultural Bighorn Basin away from forest fires"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Prevailing westerly winds channeled through North Fork and South Fork canyons at "
                "15-25 mph. Strong downslope (chinook) winds off the Absaroka Range during winter and "
                "transitional seasons can produce 40-60 mph gusts in Cody. Summer thermal winds drive "
                "upslope/upcanyon flow in afternoon, reversing at night. The 1937 Blackwater Fire "
                "demonstrated how sudden wind shifts in complex terrain produce fatal fire behavior. "
                "Winds funneling through canyon mouths accelerate as terrain narrows."
            ),
            "critical_corridors": [
                "North Fork Shoshone corridor -- linear WUI along Yellowstone highway",
                "South Fork Shoshone -- dead-end residential/ranch corridor into NF",
                "Cedar Mountain -- Douglas fir/juniper directly above south Cody residential areas",
                "Rattlesnake Mountain -- sage-to-timber transition above North Fork road",
                "Carter Mountain -- southern approach through Shoshone NF to Cody outskirts",
            ],
            "rate_of_spread_potential": (
                "Extreme in wind-driven conifer crown fire (1-3 mph with spotting). Moderate in "
                "sagebrush-grassland surrounding Cody (2-4 mph in cured grass). The Blackwater Fire "
                "exhibited explosive behavior when winds shifted, overwhelming crews in minutes. "
                "Steep canyon walls amplify effective wind speed and create alignment conditions "
                "for rapid upslope runs."
            ),
            "spotting_distance": (
                "0.5-2.0 miles in Douglas fir/lodgepole; Blackwater Fire produced spotting over "
                "fire lines that trapped crews. Canyon terrain can loft firebrands with updrafts "
                "created by canyon-channeled winds. Spotting into sagebrush below timberline can "
                "establish new fire well ahead of main front."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Cody municipal water from Shoshone River and mountain springs. System adequate for "
                "town proper but North Fork and South Fork corridor homes are on private wells with "
                "minimal fire flow. Guest ranches and lodges along scenic byway have independent "
                "water systems not designed for wildfire suppression."
            ),
            "power": (
                "Rocky Mountain Power; transmission lines follow North Fork and South Fork corridors "
                "through forested terrain. Fire along either corridor severs power to Yellowstone "
                "East Entrance facilities and all upstream residences/lodges. Cody has limited "
                "backup generation capacity."
            ),
            "communications": (
                "Good cellular in Cody proper; degraded coverage in canyon corridors west of town. "
                "North Fork canyon has intermittent cell service at best. Park County emergency "
                "management uses CodeRED. Tourist population unlikely to be enrolled in alerts. "
                "Radio repeaters on mountain peaks are fire-exposed."
            ),
            "medical": (
                "West Park Hospital (~50 beds) serves Cody and surrounding Park County. Nearest "
                "larger facility is Billings, MT (108 mi). Air ambulance available but smoke limits "
                "helicopter operations. During peak tourist season (Yellowstone visitors), medical "
                "demand already approaches capacity."
            ),
        },
        "demographics_risk_factors": {
            "population": 10000,
            "seasonal_variation": (
                "Permanent population ~10,000 but summer tourism to Yellowstone (4+ million annual "
                "park visitors, many entering via Cody) triples effective population June-September. "
                "North Fork corridor lodges and guest ranches house hundreds nightly in peak season "
                "in the heart of the fire-prone zone. Yellowstone East Entrance closure redirects "
                "traffic, creating gridlock. Many tourists are international with no wildfire awareness."
            ),
            "elderly_percentage": "~20% over 65 (retirement destination; higher than Wyoming average)",
            "mobile_homes": (
                "Significant manufactured housing on south and east sides of Cody; estimated 10-15% "
                "of housing stock. Some mobile home parks in unincorporated Park County near WUI zones."
            ),
            "special_needs_facilities": (
                "West Park Hospital, multiple senior living facilities, schools. Park County jail. "
                "Large tourist lodging population (1,000+ rooms in Cody plus corridor lodges). "
                "Buffalo Bill Center of the West museum draws large crowds. Rodeo grounds (nightly "
                "summer events with 1,000+ attendees)."
            ),
        },
    },

    # =========================================================================
    # 9. DUBOIS, WY -- New (remote Wind River valley, Shoshone NF)
    # =========================================================================
    "dubois_wy": {
        "center": [43.5333, -109.6303],
        "terrain_notes": (
            "Dubois (pop ~1,000) sits at 6,917 ft elevation in the upper Wind River valley of "
            "Fremont County, one of the most remote communities in the lower 48 states. The town "
            "occupies a narrow valley between the Absaroka Range to the north (rising to 13,000+ ft) "
            "and the Wind River Range to the south (13,804 ft Gannett Peak, Wyoming's highest). "
            "The Shoshone National Forest (2.4 million acres) and Bridger-Teton National Forest "
            "(3.4 million acres) surround the town on all sides, with the Fitzpatrick and "
            "Washakie Wilderness areas to the south and north respectively. Dense lodgepole pine, "
            "Douglas fir, and Engelmann spruce forests -- much of it with significant beetle-kill "
            "standing dead timber -- extend from the valley margins to timberline. US-26/287 is "
            "the sole paved highway, running east-west through the valley: east toward Riverton "
            "(80 miles) through Wind River Canyon and west over Togwotee Pass (9,658 ft) to "
            "Jackson (85 miles). The 2024 Pack Trail Fire (66,000 acres when merged with Fish "
            "Creek Fire) burned in Bridger-Teton NF west of Dubois with 60 mph wind gusts, "
            "forcing evacuations from ranches and cabins west of town and closing US-26/287 over "
            "Togwotee Pass. The town serves as the eastern gateway to Yellowstone/Teton tourism "
            "via Togwotee Pass. With the nearest hospital 80 miles away and a single highway in "
            "each direction, Dubois represents extreme remoteness vulnerability."
        ),
        "key_features": [
            {"name": "Absaroka Range", "bearing": "N", "type": "mountain_range",
             "notes": "Volcanic peaks to 13,000+ ft; Washakie Wilderness; dense conifer with beetle-kill; fire here would threaten Dubois from the north"},
            {"name": "Wind River Range", "bearing": "S", "type": "mountain_range",
             "notes": "13,804 ft Gannett Peak (highest in WY); Fitzpatrick Wilderness; extensive beetle-kill lodgepole; headwaters of Wind River"},
            {"name": "Togwotee Pass / US-26/287", "bearing": "W", "type": "mountain_pass",
             "notes": "9,658 ft pass to Jackson; closed by 2024 Pack Trail Fire; single westward route; frequently closed by weather Oct-May"},
            {"name": "Wind River", "bearing": "E through valley", "type": "river",
             "notes": "Flows east through Dubois valley toward Riverton/Boysen Reservoir; river corridor provides limited firebreak"},
            {"name": "Shoshone National Forest", "bearing": "N/NW", "type": "national_forest",
             "notes": "2.4 million acres; surrounds valley to north; significant deadfall from decades of fire suppression; America's first NF"},
            {"name": "Bridger-Teton National Forest", "bearing": "W/SW", "type": "national_forest",
             "notes": "3.4 million acres; source of 2024 Pack Trail Fire; beetle-kill fuel loading creating extreme fire risk"},
            {"name": "Ramshorn Peak", "bearing": "NW", "type": "mountain",
             "notes": "11,881 ft; prominent landmark above town; dense forest on flanks; fire on Ramshorn would threaten Dubois directly"},
        ],
        "elevation_range_ft": [6800, 13804],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Pack Trail Fire", "year": 2024, "acres": 66000,
             "details": (
                 "Lightning-ignited Sept 15, 2024 in Bridger-Teton NF, Jackson Ranger District. "
                 "Merged with Fish Creek Fire into 66,000-acre complex. Extreme fire behavior with "
                 "60 mph wind gusts in heavy timber. Forced evacuations from subdivisions and ranches "
                 "west of Dubois in Fremont County. US-26/287 (Togwotee Pass) closed, severing "
                 "western access to Jackson. Red Cross evacuation center opened at Warm Valley "
                 "Assisted Living in Dubois. 1,000+ firefighters deployed."
             )},
            {"name": "Fish Creek Fire", "year": 2024, "acres": 25052,
             "details": "Lightning-caused Aug 16, 2024; burned in remote North Fork Fish Creek drainage 7 miles SW of Togwotee Pass; eventually merged with Pack Trail Fire"},
            {"name": "Dunoir Fire", "year": 2018, "acres": 1500,
             "details": "Burned in Dunoir Special Management Area north of Dubois in Shoshone NF; smoke filled Wind River valley; demonstrated fire risk in surrounding NF"},
        ],
        "evacuation_routes": [
            {"route": "US-26/287 East (toward Riverton)", "direction": "E", "lanes": 2,
             "bottleneck": "80 miles to Riverton; passes through Wind River Indian Reservation; narrow canyon sections",
             "risk": "Only eastward escape; extremely long distance to services; road conditions can be poor; fire along route would leave town completely isolated"},
            {"route": "US-26/287 West (Togwotee Pass toward Jackson)", "direction": "W", "lanes": 2,
             "bottleneck": "9,658 ft mountain pass; frequently closed by weather and fire; 85 miles to Jackson",
             "risk": "EXTREME -- 2024 Pack Trail Fire closed this route; pass is unreliable in winter; evacuating into active fire zone toward Jackson is counterproductive"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Strong westerly winds through Wind River valley, accelerating through terrain "
                "constrictions at 15-30 mph. Chinook (foehn) winds produce winter and spring extremes "
                "with gusts exceeding 60 mph. The 2024 Pack Trail Fire demonstrated how wind events "
                "drive explosive fire growth in beetle-kill timber. Valley orientation (E-W) aligns "
                "with prevailing winds, channeling fire directly toward or away from town."
            ),
            "critical_corridors": [
                "Wind River valley floor -- sage/grass continuous fuel from NF boundary to town",
                "Togwotee Pass corridor -- beetle-kill timber; 2024 fire origin area",
                "Horse Creek / Warm Springs -- drainages from Absaroka Range toward town from north",
                "Jakeys Fork -- drainage from Wind River Range approaching town from south",
            ],
            "rate_of_spread_potential": (
                "Extreme in beetle-kill lodgepole (2-4 mph crown fire with massive firebrands). "
                "Pack Trail Fire grew from discovery to 66,000 acres in approximately 3 weeks with "
                "multiple explosive growth days. Wind-driven grass/sage on valley floor supports "
                "4-6 mph spread, potentially faster in chinook events."
            ),
            "spotting_distance": (
                "1-3+ miles in beetle-kill lodgepole -- standing dead timber produces prolific "
                "firebrands. Confirmed 5-7 mile spotting in similar fuel types during 2007 Cascade "
                "Complex in nearby Idaho. Valley sage is highly receptive to long-range spotting."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Dubois municipal water from local wells and Wind River watershed. System designed "
                "for ~1,000 residents; minimal fire flow capacity. Outlying ranches and subdivisions "
                "on private wells with no firefighting water supply."
            ),
            "power": (
                "Single transmission line serving Dubois through Wind River valley. Fire along "
                "either highway corridor can sever power. No backup generation for community "
                "infrastructure. Extended outages (days to weeks) possible during major fire events."
            ),
            "communications": (
                "Very limited cell coverage; terrain shadows block signal in many areas. Fremont "
                "County emergency management uses sirens and door-to-door notification for some "
                "areas. Satellite phone may be only reliable communication during major events. "
                "Radio communications have significant dead zones in surrounding mountains."
            ),
            "medical": (
                "No hospital in Dubois. Nearest emergency room is Riverton Memorial Hospital "
                "(80 mi east) or St. John's Health in Jackson (85 mi west over Togwotee Pass). "
                "Dubois has a small volunteer EMS squad. Medical evacuation by helicopter is "
                "critical but smoke severely limits flight operations. Response time for ground "
                "ambulance from either direction exceeds 90 minutes under ideal conditions."
            ),
        },
        "demographics_risk_factors": {
            "population": 1000,
            "seasonal_variation": (
                "Summer tourism via Togwotee Pass to Yellowstone/Teton increases population "
                "significantly. Hunting season (Sept-Nov) brings hundreds of visitors into "
                "surrounding NF. Several guest ranches and lodges west of town in the fire-prone "
                "corridor house visitors in peak fire season. Snowmobile tourism in winter."
            ),
            "elderly_percentage": "~28% over 65 (high -- small retirement community; aging in place)",
            "mobile_homes": (
                "Significant proportion of housing stock; estimated 15-20% manufactured homes. "
                "Concentrated vulnerability given limited water supply and fire flow."
            ),
            "special_needs_facilities": (
                "Warm Valley Assisted Living (served as Red Cross evacuation center during 2024 fire). "
                "Small school. No hospital. Limited social services. Extremely remote from "
                "any major service center."
            ),
        },
    },

    # =========================================================================
    # 3. JACKSON, WY -- Enhanced (Teton Range, Bridger-Teton NF, extreme WUI)
    # =========================================================================
    "jackson_wy": {
        "center": [43.4799, -110.7624],
        "terrain_notes": (
            "Jackson (pop ~11,000 permanent) sits at 6,237 ft elevation in Jackson Hole -- a "
            "narrow, 60-mile-long valley flanked by the Teton Range (13,775 ft Grand Teton) to the "
            "west and the Gros Ventre Range (11,682 ft Doubletop Peak) to the east. The town "
            "occupies the southern end of this valley where the Snake River exits through a narrow "
            "canyon. Bridger-Teton National Forest (3.4 million acres -- the largest NF in the lower "
            "48 outside Alaska) surrounds the valley on three sides, with Grand Teton National Park "
            "to the north and the National Elk Refuge immediately east of town. The valley floor is "
            "dominated by sagebrush-grassland, but dense lodgepole pine and Douglas fir forests "
            "climb the surrounding mountains, with significant beetle-kill standing dead timber "
            "throughout. The 2018 Roosevelt Fire (61,511 acres) burned 32 miles south and destroyed "
            "55 homes in Hoback Ranches, demonstrating the catastrophic WUI risk in the region. "
            "Jackson Hole is the gateway to both Grand Teton and Yellowstone National Parks, drawing "
            "4+ million visitors annually. The combination of extreme terrain, limited road access "
            "(only 4 highways, all 2-lane), massive seasonal population surge, and surrounding "
            "wilderness makes Jackson one of the highest-consequence WUI scenarios in the Rocky "
            "Mountain West. Teton County's median home price exceeds $2 million, creating enormous "
            "asset exposure. The Teton Interagency Fire program coordinates USFS, NPS, BLM, and "
            "local resources across this complex jurisdictional landscape."
        ),
        "key_features": [
            {"name": "Teton Range", "bearing": "W", "type": "mountain_range",
             "notes": "Grand Teton at 13,775 ft; dramatic fault-block range rising 7,000 ft above valley floor; alpine/subalpine forests on lower flanks; Grand Teton NP"},
            {"name": "Gros Ventre Range", "bearing": "E", "type": "mountain_range",
             "notes": "11,682 ft Doubletop Peak; dense lodgepole/Douglas fir with extensive beetle-kill; Gros Ventre Wilderness; fire in these forests threatens Jackson directly"},
            {"name": "Snake River Canyon", "bearing": "S", "type": "canyon/corridor",
             "notes": "Narrow canyon south of Jackson where Snake River exits valley; US-26/89 passes through; fire or rockslide closes sole southern escape route"},
            {"name": "National Elk Refuge", "bearing": "E/NE", "type": "wildlife_refuge",
             "notes": "24,700 acres of sagebrush-grassland immediately east of Jackson; winter home to 7,500 elk; grass fires here would threaten east Jackson directly"},
            {"name": "Bridger-Teton National Forest", "bearing": "S/E", "type": "national_forest",
             "notes": "3.4 million acres, largest NF in lower 48 outside Alaska; significant beetle-kill fuel loading; source of 2018 Roosevelt Fire and 2024 Pack Trail/Fish Creek fires"},
            {"name": "Teton Pass", "bearing": "SW", "type": "mountain_pass",
             "notes": "8,431 ft pass on WY-22 to Idaho; 10% grades; only western escape route; frequently closed by avalanche, construction, and fire; historically unreliable"},
            {"name": "Hoback Junction", "bearing": "S", "type": "junction/community",
             "notes": "Critical junction of US-26/89/189/191 south of Jackson; Hoback Canyon narrows to single corridor; 2018 Roosevelt Fire closed 50-mile stretch of highway here"},
        ],
        "elevation_range_ft": [6000, 13775],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Roosevelt Fire", "year": 2018, "acres": 61511,
             "details": (
                 "Human-caused fire reported Sept 15, 2018, near head of Hoback River in Wyoming Range, "
                 "32 miles south of Jackson. Ideal fire conditions allowed rapid growth. 55 of 150 homes "
                 "in Hoback Ranches subdivision destroyed. 230 homes evacuated. 50-mile stretch of "
                 "US-189/191 closed, cutting off a primary Jackson evacuation route. 982 firefighters, "
                 "28 crews, 56 engines, 10 helicopters deployed. Demonstrated how quickly fire can "
                 "overwhelm WUI subdivisions in the Jackson Hole region."
             )},
            {"name": "Pack Trail Fire", "year": 2024, "acres": 66000,
             "details": (
                 "Lightning-caused fire Sept 15, 2024, in Bridger-Teton NF. Merged with Fish Creek Fire "
                 "into 66,000-acre complex. Extreme fire behavior with 60 mph wind gusts in heavy timber. "
                 "Closed US-26/287 (Togwotee Pass), cutting off eastern access to Jackson. Evacuations "
                 "in Fremont County west of Dubois. 1,000+ firefighters deployed across this fire and "
                 "the simultaneous Elk Fire near Sheridan."
             )},
            {"name": "Fish Creek Fire", "year": 2024, "acres": 25052,
             "details": "Lightning-caused, discovered Aug 16, 2024, 7 miles SW of Togwotee Pass in remote North Fork Fish Creek drainage. Burned in dense timber. Eventually merged with Pack Trail Fire."},
            {"name": "Cliff Creek Fire", "year": 2016, "acres": 5000,
             "details": "Burned in Gros Ventre Range east of Jackson; smoke filled Jackson Hole valley for weeks; demonstrated smoke trapping in valley inversions"},
        ],
        "evacuation_routes": [
            {"route": "US-26/89 South (Snake River Canyon toward Alpine)", "direction": "S", "lanes": 2,
             "bottleneck": "Narrow canyon with no shoulders; single road; river on one side, cliffs on other",
             "risk": "EXTREME -- only southern exit; fire or rockslide in canyon traps entire town; Roosevelt Fire closed 50-mile stretch of highway in this direction"},
            {"route": "US-26/89/191 North (toward Yellowstone/Moran Junction)", "direction": "N", "lanes": 2,
             "bottleneck": "Two-lane highway through Grand Teton NP; Moran Junction splits to Togwotee Pass (E) or Yellowstone (N)",
             "risk": "2024 Pack Trail Fire closed Togwotee Pass; Yellowstone fires could close northern route; tourists unfamiliar with routes add congestion"},
            {"route": "WY-22 West (Teton Pass to Victor, ID)", "direction": "W", "lanes": 2,
             "bottleneck": "8,431 ft mountain pass; 10% grades; frequent closures for construction, avalanche, weather",
             "risk": "High -- steep, winding road not designed for mass evacuation; Idaho side has limited capacity; historically unreliable year-round"},
            {"route": "US-191 South (toward Hoback Junction/Pinedale)", "direction": "S", "lanes": 2,
             "bottleneck": "Hoback Canyon narrows; converges with US-26/89 at Hoback Junction",
             "risk": "Roosevelt Fire demonstrated this corridor's vulnerability; burned directly along highway; limited alternate routes in canyon terrain"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Complex terrain-driven winds. Prevailing westerly/southwesterly flow at ridgetop level "
                "but valley floor experiences strong diurnal up-valley (southerly) and down-valley "
                "(northerly) winds. Foehn winds over Teton Pass can produce 40-60 mph gusts in western "
                "Jackson. Snake River Canyon funnels southerly winds. Inversions are common and trap "
                "smoke for days to weeks during regional fire events. The 2018 Roosevelt Fire exhibited "
                "erratic fire behavior driven by terrain-channeled winds."
            ),
            "critical_corridors": [
                "Snake River Canyon -- sole southern exit; fire closes evacuation route",
                "Gros Ventre River drainage -- eastern approach from beetle-kill forest toward town",
                "National Elk Refuge -- sagebrush grassland directly east of town; fast grass fire spread",
                "Hoback Canyon -- southern approach demonstrated by 2018 Roosevelt Fire",
                "Cache Creek / Snow King -- forested slopes directly above Jackson town center",
                "West bank subdivisions -- homes along Snake River with forest/sage interface",
            ],
            "rate_of_spread_potential": (
                "Extreme in sagebrush-grassland (3-6 mph head fire). Beetle-kill lodgepole forests "
                "produce catastrophic crown fire behavior with rates of 1-3 mph and massive firebrands. "
                "The Roosevelt Fire grew from initial report to 25,000+ acres in 3 days. Steep terrain "
                "in surrounding ranges amplifies effective wind speed. Alignment of wind, slope, and "
                "aspect can produce explosive runs down any of the major drainages toward Jackson."
            ),
            "spotting_distance": (
                "1-3+ miles in beetle-kill lodgepole (abundant standing dead fuel produces prolific "
                "firebrands). The 2007 Cascade Complex in nearby Idaho confirmed 5-7 mile spotting in "
                "similar fuel types. Jackson's sagebrush surroundings are receptive to long-range "
                "firebrands, creating potential for fire establishment well ahead of the main front."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Jackson municipal water from Snake River alluvial aquifer and mountain springs. Water "
                "system adequate for normal demand but not designed for simultaneous wildfire suppression "
                "across multiple WUI neighborhoods. Upper-elevation homes on private wells with no "
                "fire flow capacity. Teton Village water system independent and limited."
            ),
            "power": (
                "Lower Valley Energy serves the region; primary transmission enters through Snake River "
                "Canyon corridor. Fire in the canyon could sever power to the entire valley simultaneously "
                "with closing the evacuation route. Backup generation limited to individual buildings. "
                "Regional grid has minimal redundancy due to remoteness."
            ),
            "communications": (
                "Cell coverage adequate in town and major corridors but significant gaps in surrounding "
                "mountains and wilderness. Teton County emergency management uses Everbridge notification. "
                "Satellite phones used by backcountry operations. Tourist population may not be registered "
                "for local alerts. Radio communications (VHF) have terrain shadow issues."
            ),
            "medical": (
                "St. John's Health (Jackson) -- ~60 beds, Level IV trauma. Nearest higher-level trauma "
                "is Eastern Idaho Regional Medical Center (90 mi W over Teton Pass) or Idaho Falls "
                "(100 mi). Air ambulance (fixed-wing and helicopter) is critical but smoke limits "
                "operations. During peak tourist season, medical demand already strains capacity -- a "
                "mass casualty WUI fire event would quickly overwhelm available resources."
            ),
        },
        "demographics_risk_factors": {
            "population": 11000,
            "seasonal_variation": (
                "Permanent population ~11,000 in town, ~24,000 in Teton County. However, Jackson Hole "
                "hosts 4+ million visitors annually to Grand Teton and Yellowstone. Summer daily "
                "population can reach 35,000-50,000+ in the valley. Peak fire season (July-September) "
                "coincides with peak tourism. Many visitors are from out of state/country with zero "
                "familiarity with wildfire risk, evacuation routes, or local conditions. Large workforce "
                "commutes from Teton Valley, Idaho (over Teton Pass) and Star Valley (through Snake "
                "River Canyon) -- fire closing either route strands thousands."
            ),
            "elderly_percentage": "~12% over 65 (affluent retirees; higher in Teton Village/Wilson area)",
            "mobile_homes": (
                "Very limited in Jackson proper due to extreme property values ($2M+ median home). "
                "Workforce housing in trailers/manufactured homes concentrated in unincorporated areas "
                "south of town along US-89 and in Hoback Junction area -- directly in fire corridors."
            ),
            "special_needs_facilities": (
                "St. John's Health hospital, senior living facilities, multiple schools and daycare "
                "centers. Large hotel/motel population (2,000+ rooms). Teton County jail (~40 capacity). "
                "Significant homeless/workforce population in vehicles during summer. National park "
                "campgrounds (1,000+ campers nightly) within smoke/fire impact zone."
            ),
        },
    },

    # =========================================================================
    # 11. LANDER, WY -- New (Wind River Range base, Shoshone NF)
    # =========================================================================
    "lander_wy": {
        "center": [42.8330, -108.7307],
        "terrain_notes": (
            "Lander (pop ~7,700) sits at 5,357 ft elevation at the southeastern base of the Wind "
            "River Range in Fremont County, at the transition between the mountains and the open "
            "Wind River Basin. The Shoshone National Forest extends to within 10 miles of town on "
            "the western and northern sides, with the Wind River Range rising to 13,804 ft (Gannett "
            "Peak) beyond. The Popo Agie River flows through the city from Sinks Canyon -- a "
            "narrow, forested limestone canyon that has been identified as the primary fire corridor "
            "threatening Lander. Sinks Canyon State Park, 6 miles southwest of town, sits in dense "
            "Douglas fir and lodgepole pine forest that transitions to sagebrush on the city's "
            "outskirts. The Wind River Indian Reservation borders Lander to the north and east. "
            "WUI development has expanded southwestward toward Sinks Canyon along the Popo Agie "
            "corridor, placing homes in direct contact with NF fuels. The 2002 Kate's Basin "
            "Complex fire burned 180,000 acres to the north near Wind River Canyon, and the "
            "region has significant beetle-kill fuel loading that increases fire risk. Lander "
            "serves as a major outdoor recreation hub (climbing, backpacking, mountain biking) "
            "and gateway to the southern Wind River Range wilderness. NOLS (National Outdoor "
            "Leadership School) is headquartered here, regularly sending hundreds of students "
            "into backcountry during fire season."
        ),
        "key_features": [
            {"name": "Wind River Range", "bearing": "W/NW", "type": "mountain_range",
             "notes": "13,804 ft Gannett Peak; Popo Agie Wilderness; extensive beetle-kill lodgepole; dramatic terrain rising 8,000+ ft above Lander"},
            {"name": "Sinks Canyon", "bearing": "SW", "type": "canyon/state_park",
             "notes": "Narrow limestone canyon with dense Douglas fir and lodgepole; state park 6 miles from town; primary fire corridor threatening Lander; WUI development along canyon road"},
            {"name": "Popo Agie River", "bearing": "SW through city", "type": "river/drainage",
             "notes": "Flows from Sinks Canyon through Lander; riparian corridor; drainage channels wind from canyon into city"},
            {"name": "Shoshone National Forest", "bearing": "W/NW", "type": "national_forest",
             "notes": "2.4 million acres; extends to within 10 miles of town; beetle-kill fuel loading; America's first NF"},
            {"name": "Red Canyon", "bearing": "S", "type": "canyon",
             "notes": "Dramatic red-rock canyon south of town; WUI development along canyon road; sage/juniper transition to conifer"},
            {"name": "NOLS Headquarters", "bearing": "central", "type": "institution",
             "notes": "National Outdoor Leadership School; sends hundreds of students into Wind River backcountry annually during fire season; institutional population in remote terrain"},
        ],
        "elevation_range_ft": [5200, 13804],
        "wui_exposure": "moderate",
        "historical_fires": [
            {"name": "Kate's Basin Complex", "year": 2002, "acres": 180000,
             "details": "Massive fire complex near Wind River Canyon between Thermopolis and Riverton, north of Lander; burned in sage/grass and conifer; smoke impacted Lander for weeks"},
            {"name": "Sand Creek Fire", "year": 2021, "acres": 150,
             "details": "Burned in remote Wind River Range area; required 140 personnel; demonstrated fire risk in mountain terrain accessible from Lander trailheads"},
            {"name": "Sinks Canyon area fires", "year": "various", "acres": "small",
             "details": "Multiple small fires in Sinks Canyon corridor over decades; each demonstrating the primary threat vector from NF through canyon toward city"},
        ],
        "evacuation_routes": [
            {"route": "US-287 North (toward Riverton/Thermopolis)", "direction": "N", "lanes": 2,
             "bottleneck": "25 miles to Riverton; passes through Wind River Reservation",
             "risk": "Generally safe -- leads away from mountain fire sources toward open basin; most viable evacuation direction"},
            {"route": "US-287 South (toward Rawlins via South Pass)", "direction": "S", "lanes": 2,
             "bottleneck": "Climbs to South Pass (7,550 ft); 130 miles to Rawlins; very remote",
             "risk": "Extremely remote highway through open terrain; low fire risk but impractical for most evacuees"},
            {"route": "WY-131 / Sinks Canyon Road (toward mountains)", "direction": "SW", "lanes": 2,
             "bottleneck": "Dead-end road into NF beyond Sinks Canyon State Park",
             "risk": "NOT an evacuation route -- leads into the fire threat; narrow canyon road would be death trap during fire"},
            {"route": "WY-789 East (toward Riverton)", "direction": "E", "lanes": 2,
             "bottleneck": "Alternative to US-287 N; passes through reservation; 24 miles to Riverton",
             "risk": "Low fire risk; viable alternative eastward escape"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Prevailing westerly and southwesterly winds at 10-20 mph, accelerating through "
                "Sinks Canyon and Red Canyon corridors. Chinook winds produce extreme gusts in "
                "winter/spring but can occur in late summer during frontal passages. Diurnal upslope "
                "(afternoon) and drainage (nighttime) wind patterns in canyon corridors. Open "
                "sagebrush basin east of town creates long, unobstructed wind fetch."
            ),
            "critical_corridors": [
                "Sinks Canyon -- primary fire corridor from NF through dense forest toward city",
                "Popo Agie River drainage -- carries fire and wind from canyon into residential areas",
                "Red Canyon -- southern approach from sage/juniper interface",
                "Mortimore Lane / Baldwin Creek -- WUI development extending toward NF boundary",
            ],
            "rate_of_spread_potential": (
                "Moderate to high in sagebrush-grassland (3-5 mph in wind events). High in Douglas "
                "fir and lodgepole in Sinks Canyon (1-3 mph crown fire). Beetle-kill standing dead "
                "timber increases potential for extreme crown fire behavior. Terrain channeling in "
                "canyon corridors amplifies effective wind speed."
            ),
            "spotting_distance": (
                "0.5-2.0 miles in conifer; 0.25-0.5 miles in sagebrush. Sinks Canyon corridor "
                "can funnel firebrands toward city neighborhoods along Popo Agie River. Mountain "
                "terrain creates complex spotting patterns with lofting and down-valley transport."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Lander municipal water from wells and Middle Fork Popo Agie River watershed. "
                "System adequate for city population but WUI homes on southwest side extending "
                "toward Sinks Canyon may exceed system capacity during fire events. Canyon-area "
                "homes on private wells with no fire flow."
            ),
            "power": (
                "Rocky Mountain Power; transmission enters from Riverton direction. Lines through "
                "Sinks Canyon corridor are fire-exposed. Power outage during canyon fire would "
                "affect water pumping capacity for fire suppression."
            ),
            "communications": (
                "Adequate cell coverage in city; gaps in canyons and surrounding mountains. "
                "Fremont County emergency notification system deployed. NOLS has independent "
                "satellite communication for backcountry operations. Wind River Reservation "
                "has separate emergency management coordination."
            ),
            "medical": (
                "SageWest Health Care (Lander campus, ~75 beds) provides emergency and basic "
                "hospital services. Nearest larger facility is in Riverton (25 mi) or Casper "
                "(145 mi). Air ambulance available. Medical capacity adequate for routine "
                "emergencies but would strain with mass casualty WUI event."
            ),
        },
        "demographics_risk_factors": {
            "population": 7700,
            "seasonal_variation": (
                "Summer outdoor recreation increases population by 20-30%. NOLS headquarters sends "
                "hundreds of students into Wind River backcountry June-September -- dispersed "
                "population in extremely remote, fire-prone terrain. Climbing and backpacking "
                "tourism brings additional visitors. Wind River Reservation border adds cultural "
                "and jurisdictional complexity to emergency response."
            ),
            "elderly_percentage": "~20% over 65 (retirement and aging-in-place community)",
            "mobile_homes": (
                "Estimated 10-12% of housing stock; concentrated on east side of town and along "
                "US-287 corridor. Mobile homes on reservation border area."
            ),
            "special_needs_facilities": (
                "SageWest Health Care hospital, NOLS campus, multiple schools, senior center, "
                "assisted living facilities. Fremont County jail. Small homeless population. "
                "Wind River Reservation communities (Ethete, Fort Washakie) nearby with shared "
                "emergency resources."
            ),
        },
    },

    # =========================================================================
    # 10. PINEDALE, WY -- New (Bridger-Teton NF, Wind River Range)
    # =========================================================================
    "pinedale_wy": {
        "center": [42.8666, -109.8608],
        "terrain_notes": (
            "Pinedale (pop ~2,000) sits at 7,175 ft elevation on the western slope of the Wind "
            "River Range in Sublette County, one of the least populated counties in the lower 48 "
            "(~10,000 people in an area the size of Connecticut). The town is positioned on a "
            "sagebrush-covered bench above the Green River, with the Wind River Range rising "
            "dramatically to the east (peaks exceeding 13,000 ft) and the Wyoming Range to the "
            "west. The Bridger-Teton National Forest surrounds the town on three sides, with the "
            "Bridger Wilderness (428,087 acres) directly east. Dense lodgepole pine forests with "
            "significant beetle-kill extend from the NF boundary -- just 5-6 miles from town -- "
            "to timberline. The 2025 Dollar Lake Fire exploded from 20 acres to 1,388 acres "
            "overnight 40 miles north of Pinedale, forcing immediate evacuations of homes and "
            "campgrounds and closing Green River Lakes Road. The fire burned through dense "
            "overgrowth including pine beetle-damaged timber. US-191 is the primary north-south "
            "highway, connecting to Jackson (77 mi N) and Rock Springs (100 mi S). WY-352 "
            "provides access to Green River Lakes area to the north. Pinedale is the jumping-off "
            "point for hundreds of backcountry recreationists entering the Bridger Wilderness "
            "in summer, adding a dispersed population in extremely remote, fire-prone terrain."
        ),
        "key_features": [
            {"name": "Wind River Range", "bearing": "E", "type": "mountain_range",
             "notes": "Peaks exceeding 13,000 ft; Bridger Wilderness (428,087 acres); dense lodgepole with beetle-kill; headwaters of Green River"},
            {"name": "Wyoming Range", "bearing": "W", "type": "mountain_range",
             "notes": "9,000-11,000 ft peaks west of Green River valley; Bridger-Teton NF; conifer forests with fire history"},
            {"name": "Green River", "bearing": "N-S", "type": "river",
             "notes": "Major river flowing south through Pinedale area; limited firebreak in sagebrush terrain; Green River Lakes area is popular recreation"},
            {"name": "Bridger-Teton National Forest", "bearing": "E/N/W", "type": "national_forest",
             "notes": "Surrounds Pinedale on three sides; 3.4 million acres; beetle-kill fuel loading; source of Dollar Lake Fire (2025)"},
            {"name": "Fremont Lake", "bearing": "NE", "type": "lake",
             "notes": "Large natural lake 4 miles NE of town; recreational area with homes and campgrounds in forested WUI setting"},
            {"name": "Green River Lakes Road / WY-352", "bearing": "N", "type": "corridor",
             "notes": "Access to Green River Lakes and trailheads; closed by 2025 Dollar Lake Fire; homes and campgrounds along route"},
        ],
        "elevation_range_ft": [7000, 13500],
        "wui_exposure": "moderate",
        "historical_fires": [
            {"name": "Dollar Lake Fire", "year": 2025, "acres": 1388,
             "details": (
                 "Exploded from 20 acres to 1,388 acres overnight Aug 21-22, 2025, approximately "
                 "40 miles north of Pinedale. Burned through dense overgrowth with pine beetle-damaged "
                 "timber. Forced immediate evacuation of homes and campgrounds. Green River Lakes Road "
                 "closed. Emergency declaration issued by Sublette County. Aerial assets deployed "
                 "immediately. Demonstrated explosive growth potential in beetle-kill fuels."
             )},
            {"name": "Roosevelt Fire (regional impact)", "year": 2018, "acres": 61511,
             "details": "Burned in Wyoming Range along US-189/191 between Pinedale and Jackson; closed primary northward highway; smoke impacted Pinedale for weeks"},
            {"name": "Fontenelle Fire", "year": 2012, "acres": 52000,
             "details": "Burned in BLM/NF land west of Pinedale in the Wyoming Range; sage/grass and conifer; demonstrated large-fire potential in the Upper Green River region"},
        ],
        "evacuation_routes": [
            {"route": "US-191 North (toward Jackson via Hoback Junction)", "direction": "N", "lanes": 2,
             "bottleneck": "77 miles to Jackson through remote terrain; Hoback Canyon narrows; single road",
             "risk": "High -- 2018 Roosevelt Fire closed this corridor; passes through extensive NF; long distance with no services for 50+ miles"},
            {"route": "US-191 South (toward Rock Springs via Farson)", "direction": "S", "lanes": 2,
             "bottleneck": "100 miles to Rock Springs through open desert/sage; very remote",
             "risk": "Low fire risk (open sage steppe) but extremely remote; safest evacuation direction; no services for 70+ miles"},
            {"route": "WY-352 North (Green River Lakes)", "direction": "N", "lanes": 2,
             "bottleneck": "Dead-end road into NF; no through-access",
             "risk": "NOT an evacuation route -- leads deeper into fire-prone NF; closed by 2025 Dollar Lake Fire"},
            {"route": "WY-351/Sublette CR 23 East (toward South Pass)", "direction": "E", "lanes": 2,
             "bottleneck": "Unpaved/poorly maintained county roads; extremely remote mountain terrain",
             "risk": "Not suitable for mass evacuation; leads to remote Wind River Range backcountry"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Strong prevailing westerly and southwesterly winds at 15-25 mph; exposed location "
                "at 7,175 ft on open sagebrush bench. Chinook winds produce extreme gusts (50-70 mph) "
                "in winter and transitional seasons. Dollar Lake Fire experienced wind-driven explosive "
                "growth. Valley orientation channels wind along Green River corridor."
            ),
            "critical_corridors": [
                "Green River Lakes Road -- WUI corridor with homes/campgrounds extending into NF",
                "Fremont Lake area -- residential WUI development in forested lake margins",
                "Eastern foothills -- beetle-kill lodgepole approaching from Wind River Range",
                "Half Moon Lake / Burnt Lake -- forested recreation areas east of town",
            ],
            "rate_of_spread_potential": (
                "Extreme in beetle-kill lodgepole (2-4 mph crown fire). Dollar Lake Fire grew from "
                "20 to 1,388 acres in approximately 12 hours -- a rate exceeding 100 acres/hour. "
                "Sagebrush on bench around town supports 3-5 mph spread in wind events. The combination "
                "of beetle-kill timber and strong winds creates conditions for explosive growth."
            ),
            "spotting_distance": (
                "1-3+ miles in beetle-kill lodgepole; standing dead timber is among the most prolific "
                "firebrand producers in Western fuel types. Long-range spotting into sagebrush around "
                "town is possible during extreme wind events."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Pinedale municipal water from wells and local springs. Small system for ~2,000 "
                "residents; fire flow capacity limited. Outlying areas on private wells. No "
                "redundancy in supply. System would be overwhelmed by simultaneous structure fires."
            ),
            "power": (
                "Lower Valley Energy; transmission line enters from the south. Remote location "
                "means repair crews may take days to reach damaged infrastructure during fire events. "
                "Extended outages (days) are routine during winter storms and would be expected "
                "during summer fire events."
            ),
            "communications": (
                "Limited cell coverage in town; very poor in surrounding mountains and wilderness. "
                "Sublette County has minimal emergency notification infrastructure. Backcountry "
                "recreationists in Bridger Wilderness may be unreachable during fire events. "
                "Satellite communication is often the only option."
            ),
            "medical": (
                "Pinedale Medical Clinic provides basic care only. Nearest hospital is St. John's "
                "Health in Jackson (77 mi N) or Rock Springs hospital (100 mi S). Air ambulance "
                "from Jackson or Idaho Falls. Medical evacuation by ground takes 75-100+ minutes. "
                "Smoke limits helicopter operations during fire events."
            ),
        },
        "demographics_risk_factors": {
            "population": 2000,
            "seasonal_variation": (
                "Summer recreation increases population significantly. Pinedale is the primary staging "
                "point for Bridger Wilderness backpackers and horseback trips -- hundreds of people "
                "dispersed in extremely remote terrain during peak fire season. Hunting season "
                "(Sept-Nov) brings additional visitors. Energy industry workers (natural gas "
                "development in Jonah/Pinedale Anticline fields) add to population."
            ),
            "elderly_percentage": "~22% over 65 (aging ranching/retirement community)",
            "mobile_homes": (
                "Significant proportion; estimated 12-15% of housing stock. Energy worker housing "
                "includes manufactured homes. Concentrated along US-191 corridor."
            ),
            "special_needs_facilities": (
                "Small school, medical clinic. No hospital or major institutional facility. "
                "Sublette County Senior Center. Museum of the Mountain Man (tourist draw). "
                "Very limited social service infrastructure for a community this remote."
            ),
        },
    },

    # =========================================================================
    # 12. SHERIDAN, WY -- New (Bighorn NF, grassland-forest interface)
    # =========================================================================
    "sheridan_wy": {
        "center": [44.7972, -106.9562],
        "terrain_notes": (
            "Sheridan (pop ~18,000) sits at 3,745 ft elevation on the eastern slope of the Bighorn "
            "Mountains in Sheridan County, northeastern Wyoming. The city occupies the transition "
            "zone between the Great Plains grassland to the east and the Bighorn National Forest "
            "(1.1 million acres) rising steeply to the west, reaching 13,175 ft at Cloud Peak. "
            "This grassland-forest interface is one of the most fire-active ecotones in Wyoming. "
            "The 2024 Elk Fire, which started September 27 approximately 15 miles northwest of "
            "Dayton (30 miles west of Sheridan), burned 96,197 acres in the Bighorn NF and "
            "surrounding rangeland -- one of the largest fires in Wyoming history. The fire forced "
            "multiple waves of evacuations across Sheridan County, closed US-14 between Burgess "
            "Junction and Dayton, and required 654 personnel before snowfall brought 97% "
            "containment. Tongue River, Goose Creek, and Big Goose Creek drain eastward from the "
            "Bighorns through Sheridan, providing both fire corridors and water supply. The western "
            "foothills of the Bighorns, where ranches and rural subdivisions have expanded, "
            "represent the highest WUI risk zone. Ponderosa pine savanna on the lower mountain "
            "slopes transitions to dense Douglas fir, lodgepole pine, and spruce-fir at higher "
            "elevations. The grass/sage/pine ecotone on the mountain front is adapted to frequent "
            "fire and supports rapid fire spread from grassland into forest under wind-driven "
            "conditions."
        ),
        "key_features": [
            {"name": "Bighorn Mountains", "bearing": "W", "type": "mountain_range",
             "notes": "13,175 ft Cloud Peak; Bighorn NF (1.1 million acres); dense conifer at elevation; ponderosa pine savanna on eastern front; 2024 Elk Fire burned 96,197 acres"},
            {"name": "Tongue River", "bearing": "W through city", "type": "river",
             "notes": "Drains from Bighorns through Sheridan; riparian corridor; municipal water source; fire corridor from mountains to city"},
            {"name": "Goose Creek / Big Goose Creek", "bearing": "SW", "type": "drainage",
             "notes": "Major drainages from Bighorns passing south of Sheridan; ranch/residential development along corridors; fire pathways"},
            {"name": "Bighorn National Forest", "bearing": "W", "type": "national_forest",
             "notes": "1.1 million acres; source of 2024 Elk Fire; dense conifer with mixed-severity fire regime; ponderosa savanna on eastern front"},
            {"name": "US-14 / Bighorn Scenic Byway", "bearing": "W", "type": "highway",
             "notes": "Crosses Bighorns via Burgess Junction; closed during 2024 Elk Fire; access to western Wyoming; scenic route"},
            {"name": "Red Grade Road", "bearing": "W", "type": "mountain_road",
             "notes": "Mountain road west of Sheridan; evacuations ordered during 2024 Elk Fire; rural residential development in fire-prone foothills"},
            {"name": "Pass Creek area", "bearing": "NW", "type": "foothill_WUI",
             "notes": "Rural residential area in Bighorn foothills; evacuated during 2024 Elk Fire; ponderosa pine/grass interface"},
        ],
        "elevation_range_ft": [3600, 13175],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Elk Fire", "year": 2024, "acres": 96197,
             "details": (
                 "Detected September 27, 2024, approximately 15 miles NW of Dayton in Bighorn NF. "
                 "Grew to 96,197 acres -- one of Wyoming's largest recorded fires. Multiple waves "
                 "of evacuations across Sheridan County including Pass Creek, Red Grade Road, and "
                 "areas near Bighorn Mountains. US-14 closed between Burgess Junction and Dayton. "
                 "654 personnel deployed. 48% containment at peak operations. Declared out "
                 "January 3, 2025, after snowfall provided natural containment. Burned in dense "
                 "conifer transitioning to ponderosa pine savanna and grassland."
             )},
            {"name": "Welch Fire", "year": 2019, "acres": 2500,
             "details": "Burned in Bighorn foothills west of Sheridan; forced evacuations along Tongue River corridor; demonstrated foothills WUI risk"},
            {"name": "Bone Gulch Fire", "year": 2021, "acres": 400,
             "details": "Rapid grass/sage fire southwest of Sheridan; wind-driven; burned to within 3 miles of city; demonstrated how quickly grassland fire approaches from the west"},
        ],
        "evacuation_routes": [
            {"route": "I-90 North (toward Billings, MT)", "direction": "N", "lanes": 4,
             "bottleneck": "Montana border 22 miles north; good road capacity",
             "risk": "Safest and highest-capacity evacuation route; leads away from mountain fire sources; I-90 is generally reliable"},
            {"route": "I-90 South (toward Buffalo)", "direction": "S", "lanes": 4,
             "bottleneck": "35 miles to Buffalo; good road capacity",
             "risk": "Low risk -- leads south along plains east of Bighorns; viable secondary evacuation direction"},
            {"route": "US-14 West (over Bighorn Mountains)", "direction": "W", "lanes": 2,
             "bottleneck": "Mountain pass highway; narrow, winding; Burgess Junction area",
             "risk": "EXTREME -- 2024 Elk Fire closed this route; leads directly into fire zone; not viable during western fires"},
            {"route": "US-87 South (toward Buffalo via foothills)", "direction": "S", "lanes": 2,
             "bottleneck": "Follows Bighorn foothills; passes through fire-prone grassland/pine interface",
             "risk": "Moderate -- passes through ecotone where 2024 Elk Fire burned; grass fires can close this corridor"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Strong westerly and southwesterly winds prevail, with chinook (foehn) events producing "
                "50-70+ mph gusts as air descends the eastern Bighorn slope. These downslope wind events "
                "drive fire rapidly from the mountains toward Sheridan across grass and ponderosa savanna. "
                "The 2024 Elk Fire exhibited extreme behavior when strong winds aligned with the "
                "east-facing mountain front. Thunderstorm outflows during fire season can produce "
                "sudden erratic wind shifts."
            ),
            "critical_corridors": [
                "Bighorn foothills ponderosa pine -- continuous fuel from NF to rangeland",
                "Tongue River corridor -- fire pathway from mountains through Sheridan",
                "Goose Creek / Big Goose Creek -- drainages carrying fire from Bighorns toward valley",
                "Red Grade Road area -- evacuated during 2024 Elk Fire; residential WUI",
                "Pass Creek -- foothill community directly in path of westerly fire runs",
                "Grassland-sage interface east of foothills -- fast-running fire toward city",
            ],
            "rate_of_spread_potential": (
                "Extreme in wind-driven grass/sage (4-8 mph head fire, potentially faster in chinook "
                "events). High in ponderosa pine savanna (2-4 mph surface fire transitioning to "
                "torching runs). The 2024 Elk Fire's growth to 96,197 acres demonstrated catastrophic "
                "potential when fire escapes from dense forest into grassland-forest ecotone under "
                "wind. Grass fires can bridge from forest to Sheridan outskirts in hours under "
                "extreme conditions."
            ),
            "spotting_distance": (
                "0.5-2.0 miles in ponderosa/Douglas fir; 0.25-0.5 miles in grass/sage. Chinook "
                "winds can transport firebrands much farther. The grassland-forest ecotone creates "
                "conditions where forest-generated embers land in receptive grass fuels, rapidly "
                "establishing new fire fronts ahead of the main fire."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Sheridan municipal water from Tongue River watershed and Big Goose Creek. Water "
                "treatment plant in the foothills west of city is fire-exposed. System generally "
                "adequate for city but foothills WUI areas have limited fire flow. Post-fire "
                "watershed contamination (ash, sediment) is a major concern for water quality."
            ),
            "power": (
                "Rocky Mountain Power; transmission lines cross Bighorn foothills and are fire-exposed. "
                "2024 Elk Fire caused power disruptions to rural areas west of Sheridan. City grid "
                "is more resilient but large fires threatening transmission infrastructure could "
                "affect the broader region."
            ),
            "communications": (
                "Good cellular coverage in Sheridan; degrades in foothills and mountains. Sheridan "
                "County emergency management uses CodeRED and social media for notifications. "
                "2024 Elk Fire demonstrated effective multi-agency communication through Sheridan "
                "County Emergency Operations Center. AM/FM radio stations provide emergency broadcasts."
            ),
            "medical": (
                "Sheridan Memorial Hospital (~88 beds, Level III trauma). Adequate for normal "
                "operations and moderate emergencies. Nearest larger facility is in Billings, MT "
                "(130 mi). Air ambulance available from both Sheridan and Billings. Medical capacity "
                "would be challenged by mass casualty event but Sheridan has better infrastructure "
                "than most Wyoming communities of its size."
            ),
        },
        "demographics_risk_factors": {
            "population": 18000,
            "seasonal_variation": (
                "Moderate seasonal variation. Summer tourism to Bighorns and nearby ranches/dude "
                "ranches increases population. Hunting season (Sept-Nov) brings visitors. Sheridan "
                "WYO Rodeo (July) is a major event. Polo season (summer) draws affluent visitors. "
                "Less extreme seasonal swing than Jackson or Park City but still significant "
                "during peak fire season."
            ),
            "elderly_percentage": "~22% over 65 (significant retirement community; VA hospital draws veterans)",
            "mobile_homes": (
                "Estimated 8-10% of housing stock; mobile home parks on east and south sides of city. "
                "Some manufactured housing in unincorporated Sheridan County foothills area."
            ),
            "special_needs_facilities": (
                "Sheridan Memorial Hospital, VA Medical Center (draws regional veteran population), "
                "multiple assisted living and nursing facilities, several schools, Sheridan College "
                "(~4,000 students). County jail. Higher institutional population density than most "
                "Wyoming towns, creating greater evacuation complexity."
            ),
        },
    },

}




# =============================================================================
# 2. IGNITION SOURCES
# =============================================================================

CO_BASIN_IGNITION_SOURCES = {

    "colorado_springs_co": {
        "primary_sources": [
            {"source": "Human (arson, equipment, campfire)", "risk": "very_high",
             "notes": "35,000 WUI homes, heavy recreational use of foothills. "
                      "Waldo Canyon Fire cause undetermined but human-related"},
            {"source": "Power lines", "risk": "high",
             "notes": "Mountain terrain strains overhead lines in wind events. "
                      "Black Forest Fire ignition source suspected electrical"},
            {"source": "Lightning", "risk": "high",
             "notes": "Summer convective storms common, esp June-August"},
            {"source": "Vehicle / highway", "risk": "moderate",
             "notes": "I-25, US-24 through foothills terrain"},
        ],
        "highway_corridors": [
            {"name": "I-25", "bearing": "N-S", "risk": "moderate"},
            {"name": "US-24 / Ute Pass", "bearing": "W", "risk": "high",
             "notes": "Mountain highway through dense WUI"},
            {"name": "Hwy 115", "bearing": "S", "risk": "moderate"},
        ],
        "railroad_corridors": [
            {"name": "BNSF mainline", "bearing": "N-S through city",
             "risk": "moderate"},
        ],
    },

    "boulder_co": {
        "primary_sources": [
            {"source": "Power lines / electrical", "risk": "very_high",
             "notes": "Marshall Fire under investigation -- Xcel Energy power "
                      "lines/equipment primary suspect. Extreme wind event"},
            {"source": "Human (recreation, equipment)", "risk": "high",
             "notes": "Heavy recreational use of open space and mountain parks"},
            {"source": "Lightning", "risk": "high",
             "notes": "Summer storms, Fourmile Canyon Fire was human-caused"},
            {"source": "Downslope wind events", "risk": "very_high",
             "notes": "Not ignition per se, but chinook winds create conditions "
                      "where any ignition becomes catastrophic. 115 mph gusts"},
        ],
        "highway_corridors": [
            {"name": "Hwy 93", "bearing": "N-S", "risk": "high",
             "notes": "Runs along wind corridor where Marshall Fire originated"},
            {"name": "US-36", "bearing": "SE-NW", "risk": "moderate"},
            {"name": "Hwy 119 / Boulder Canyon", "bearing": "W", "risk": "moderate"},
        ],
        "railroad_corridors": [],
    },

    "superior_co": {
        "primary_sources": [
            {"source": "Power lines / electrical", "risk": "very_high",
             "notes": "Marshall Fire -- Xcel Energy equipment under investigation"},
            {"source": "Grass fire from adjacent open space", "risk": "very_high",
             "notes": "No buffer between grassland open space and subdivisions"},
            {"source": "Ember transport", "risk": "very_high",
             "notes": "90% of structure ignitions were ember cast, wood fences "
                      "connected structures creating fire chains"},
        ],
        "highway_corridors": [
            {"name": "US-36", "bearing": "E-W", "risk": "high",
             "notes": "Fire jumped 6-lane highway during Marshall Fire"},
            {"name": "Hwy 128", "bearing": "N-S", "risk": "moderate"},
        ],
        "railroad_corridors": [],
    },

    "louisville_co": {
        "primary_sources": [
            {"source": "Ember transport from upwind fire", "risk": "very_high",
             "notes": "Marshall Fire embers traveled miles in 100+ mph winds"},
            {"source": "Structure-to-structure spread", "risk": "very_high",
             "notes": "Wood fences, landscaping, vinyl siding created fire chains "
                      "in dense suburban setting"},
            {"source": "Power lines", "risk": "high",
             "notes": "Infrastructure vulnerability in extreme wind"},
        ],
        "highway_corridors": [
            {"name": "US-36", "bearing": "E-W", "risk": "moderate"},
        ],
        "railroad_corridors": [],
    },

    "estes_park_co": {
        "primary_sources": [
            {"source": "Lightning", "risk": "very_high",
             "notes": "High-elevation forests, summer convective storms. "
                      "East Troublesome Fire was lightning-caused"},
            {"source": "Human (campfire, recreation)", "risk": "high",
             "notes": "RMNP receives 4+ million visitors/year"},
            {"source": "Power lines", "risk": "moderate",
             "notes": "Mountain terrain, wind exposure"},
        ],
        "highway_corridors": [
            {"name": "US-34 (Big Thompson Canyon)", "bearing": "SE", "risk": "high",
             "notes": "Primary evacuation route through narrow canyon"},
            {"name": "US-36", "bearing": "SE", "risk": "moderate"},
            {"name": "US-34 W (Trail Ridge Rd)", "bearing": "W", "risk": "low",
             "notes": "Seasonal, closes in winter"},
        ],
        "railroad_corridors": [],
    },

    "fort_collins_co": {
        "primary_sources": [
            {"source": "Lightning", "risk": "very_high",
             "notes": "Cameron Peak and High Park fires were lightning-caused"},
            {"source": "Human (equipment, campfire)", "risk": "high",
             "notes": "Heavy recreational use of Poudre Canyon"},
            {"source": "Power lines", "risk": "high",
             "notes": "Mountain terrain strains transmission lines"},
        ],
        "highway_corridors": [
            {"name": "I-25", "bearing": "N-S", "risk": "moderate"},
            {"name": "Hwy 14 (Poudre Canyon)", "bearing": "W", "risk": "high",
             "notes": "Deep mountain canyon, WUI communities along entire length"},
            {"name": "US-287", "bearing": "NW", "risk": "moderate"},
        ],
        "railroad_corridors": [
            {"name": "BNSF", "bearing": "N-S", "risk": "low"},
        ],
    },

    "evergreen_conifer_co": {
        "primary_sources": [
            {"source": "Human (equipment, debris burning)", "risk": "very_high",
             "notes": "Lower North Fork Fire was prescribed burn escape. "
                      "Dense population in heavy fuel creates constant ignition risk"},
            {"source": "Power lines", "risk": "very_high",
             "notes": "Mountain terrain, wind exposure, aging infrastructure "
                      "through dense forest"},
            {"source": "Lightning", "risk": "high",
             "notes": "Summer storms, high-elevation forest"},
            {"source": "Vehicle / highway", "risk": "moderate",
             "notes": "I-70, US-285 through dense forest"},
        ],
        "highway_corridors": [
            {"name": "I-70", "bearing": "E-W", "risk": "high"},
            {"name": "US-285", "bearing": "SW", "risk": "high",
             "notes": "Dense forest both sides of highway"},
            {"name": "Hwy 74 (Bear Creek Canyon)", "bearing": "SE", "risk": "high",
             "notes": "Narrow canyon, primary evacuation route"},
        ],
        "railroad_corridors": [],
    },

    "durango_co": {
        "primary_sources": [
            {"source": "Durango & Silverton Railroad", "risk": "very_high",
             "notes": "Coal-fired steam locomotive, persistent ember source. "
                      "416 Fire (2018) sparked by train. Multiple train fires annually"},
            {"source": "Lightning", "risk": "high",
             "notes": "San Juan Mountains, frequent summer storms"},
            {"source": "Human (recreation, camping)", "risk": "high",
             "notes": "San Juan NF heavy recreation use"},
        ],
        "highway_corridors": [
            {"name": "US-550 (Million Dollar Highway)", "bearing": "N", "risk": "moderate"},
            {"name": "US-160", "bearing": "E-W", "risk": "moderate"},
        ],
        "railroad_corridors": [
            {"name": "Durango & Silverton Narrow Gauge", "bearing": "N through "
             "Animas Canyon", "risk": "very_high",
             "notes": "Coal-fired steam, sparks in steep canyon, 416 Fire ignition"},
        ],
    },

    "glenwood_springs_co": {
        "primary_sources": [
            {"source": "Vehicle / I-70 corridor", "risk": "very_high",
             "notes": "Grizzly Creek Fire started in I-70 median. Heavy traffic "
                      "through extreme canyon terrain, vehicle debris/sparks"},
            {"source": "Lightning", "risk": "high",
             "notes": "Mountain terrain, summer storms"},
            {"source": "Human (recreation)", "risk": "moderate",
             "notes": "Hanging Lake, recreation areas in canyon"},
        ],
        "highway_corridors": [
            {"name": "I-70 (Glenwood Canyon)", "bearing": "E", "risk": "very_high",
             "notes": "Grizzly Creek Fire origin. Canyon so steep fire is "
                      "uncontrollable once established"},
            {"name": "Hwy 82 (Roaring Fork Valley)", "bearing": "SE", "risk": "moderate"},
        ],
        "railroad_corridors": [
            {"name": "Union Pacific (Dotsero Cutoff)", "bearing": "E",
             "risk": "moderate",
             "notes": "Runs through Glenwood Canyon alongside I-70"},
        ],
    },

    "steamboat_springs_co": {
        "primary_sources": [
            {"source": "Lightning", "risk": "very_high",
             "notes": "High-elevation forest, frequent summer storms"},
            {"source": "Human (recreation, campfire)", "risk": "high",
             "notes": "Heavy recreation in Routt NF, increasing visitors"},
            {"source": "Power lines", "risk": "moderate",
             "notes": "Mountain terrain infrastructure"},
        ],
        "highway_corridors": [
            {"name": "US-40", "bearing": "E-W", "risk": "moderate"},
            {"name": "Hwy 131", "bearing": "S", "risk": "moderate"},
        ],
        "railroad_corridors": [],
    },

    "reno_nv": {
        "primary_sources": [
            {"source": "Power lines / utility failure", "risk": "very_high",
             "notes": "Pinehaven Fire (2020) and Caughlin Fire (2011) both "
                      "caused by power line arcing in extreme winds. NV Energy "
                      "infrastructure in WUI zones"},
            {"source": "Vehicle / I-80 corridor", "risk": "high",
             "notes": "I-80 through Truckee Canyon and urban fringe"},
            {"source": "Human (arson, debris burning)", "risk": "high",
             "notes": "Urban-wildland interface, rapid development"},
            {"source": "Lightning", "risk": "moderate",
             "notes": "Occasional summer dry thunderstorms"},
        ],
        "highway_corridors": [
            {"name": "I-80", "bearing": "E-W", "risk": "high"},
            {"name": "I-580 / US-395", "bearing": "S", "risk": "high",
             "notes": "Through Washoe Valley, Davis Fire area"},
            {"name": "Mt Rose Highway / Hwy 431", "bearing": "SW", "risk": "moderate"},
        ],
        "railroad_corridors": [
            {"name": "Union Pacific (Truckee Canyon)", "bearing": "E-W",
             "risk": "moderate"},
        ],
    },

    "south_lake_tahoe_ca_nv": {
        "primary_sources": [
            {"source": "Human (campfire, recreation)", "risk": "very_high",
             "notes": "Extremely heavy recreation use. Angora Fire was escaped "
                      "campfire. Tourist population doubles summer population"},
            {"source": "Power lines", "risk": "high",
             "notes": "Mountain terrain, wind events, dense forest"},
            {"source": "Lightning", "risk": "high",
             "notes": "Sierra Nevada summer storms, dry lightning"},
            {"source": "Structure fire escape to wildland", "risk": "moderate",
             "notes": "Dense development adjacent to forest"},
        ],
        "highway_corridors": [
            {"name": "US-50 (Echo Summit)", "bearing": "SW", "risk": "high",
             "notes": "Primary evacuation route, steep canyon terrain"},
            {"name": "Hwy 89 (Emerald Bay)", "bearing": "NW", "risk": "moderate"},
            {"name": "Hwy 89 (Luther Pass)", "bearing": "S", "risk": "moderate"},
        ],
        "railroad_corridors": [],
    },

    "carson_city_nv": {
        "primary_sources": [
            {"source": "Power lines / utility", "risk": "high",
             "notes": "Downslope wind events stress overhead lines in WUI"},
            {"source": "Human (debris burning, equipment)", "risk": "high",
             "notes": "Growing WUI development on western foothills"},
            {"source": "Vehicle / Hwy 395", "risk": "high",
             "notes": "Washoe Drive Fire jumped Hwy 395"},
            {"source": "Lightning", "risk": "moderate",
             "notes": "Occasional dry thunderstorms from Great Basin"},
        ],
        "highway_corridors": [
            {"name": "US-395", "bearing": "N-S", "risk": "high",
             "notes": "Major corridor, fire has jumped this highway"},
            {"name": "US-50 E", "bearing": "E", "risk": "moderate"},
            {"name": "Hwy 28 (Lake Tahoe)", "bearing": "W", "risk": "moderate"},
        ],
        "railroad_corridors": [],
    },

    "cedar_city_ut": {
        "primary_sources": [
            {"source": "Human (debris burning, equipment)", "risk": "very_high",
             "notes": "Brian Head Fire started by weed torch in dry conditions"},
            {"source": "Lightning", "risk": "high",
             "notes": "Summer monsoon storms on Markagunt Plateau"},
            {"source": "Vehicle / I-15 corridor", "risk": "moderate",
             "notes": "I-15 through sagebrush terrain"},
        ],
        "highway_corridors": [
            {"name": "I-15", "bearing": "N-S", "risk": "moderate"},
            {"name": "Hwy 14 (Cedar Canyon)", "bearing": "E", "risk": "high",
             "notes": "Through steep canyon into Dixie NF"},
            {"name": "Hwy 143 (Brian Head)", "bearing": "NE", "risk": "high"},
        ],
        "railroad_corridors": [
            {"name": "Union Pacific (Cedar City)", "bearing": "N-S",
             "risk": "low"},
        ],
    },

    "park_city_ut": {
        "primary_sources": [
            {"source": "Human (recreation, equipment)", "risk": "high",
             "notes": "Ski resort town, heavy summer recreation. 1898 fire "
                      "was mine-related"},
            {"source": "Power lines", "risk": "high",
             "notes": "Mountain terrain, aging infrastructure in dense forest"},
            {"source": "Lightning", "risk": "high",
             "notes": "Summer storms, Wasatch Range high terrain"},
        ],
        "highway_corridors": [
            {"name": "I-80", "bearing": "N", "risk": "moderate",
             "notes": "Through Parley's Canyon, evacuation route"},
            {"name": "Hwy 224", "bearing": "N-S", "risk": "moderate"},
            {"name": "Hwy 248", "bearing": "E", "risk": "moderate"},
        ],
        "railroad_corridors": [],
    },

    "jackson_wy": {
        "primary_sources": [
            {"source": "Lightning", "risk": "very_high",
             "notes": "Primary ignition source for Teton County fires. "
                      "Summer dry thunderstorms in mountains. Berry Fire was "
                      "lightning-caused"},
            {"source": "Human (campfire, recreation)", "risk": "high",
             "notes": "Heavy NP recreation -- Grand Teton + Yellowstone visitors"},
            {"source": "Vehicle / Hwy 89", "risk": "moderate",
             "notes": "Through sagebrush/grass terrain in valley"},
        ],
        "highway_corridors": [
            {"name": "Hwy 89/191", "bearing": "N-S", "risk": "moderate",
             "notes": "Through valley, primary N-S evacuation route"},
            {"name": "Hwy 22 (Teton Pass)", "bearing": "W", "risk": "moderate",
             "notes": "Steep mountain pass, limited evacuation capacity"},
            {"name": "Hwy 26/89 (Hoback Junction)", "bearing": "S", "risk": "moderate"},
        ],
        "railroad_corridors": [],
    },

    "cody_wy": {
        "primary_sources": [
            {"source": "Lightning", "risk": "very_high",
             "notes": "Absaroka Range, 1937 Blackwater Fire was lightning-caused"},
            {"source": "Human (campfire, recreation)", "risk": "high",
             "notes": "Yellowstone gateway, heavy recreation in Shoshone NF"},
            {"source": "Rangeland fire (sagebrush)", "risk": "high",
             "notes": "Bighorn Basin sagebrush-grassland, wind-driven spread"},
            {"source": "Vehicle / highway", "risk": "moderate",
             "notes": "Hwy 14/16/20 through Shoshone Canyon"},
        ],
        "highway_corridors": [
            {"name": "Hwy 14/16/20 (Yellowstone Hwy)", "bearing": "W",
             "risk": "high",
             "notes": "Through Shoshone Canyon into mountains"},
            {"name": "Hwy 120", "bearing": "S", "risk": "moderate"},
            {"name": "US-14A", "bearing": "E", "risk": "moderate"},
        ],
        "railroad_corridors": [],
    },
}


# =============================================================================
# 3. CLIMATOLOGY -- FIRE SEASON NORMALS
# =============================================================================
#
# Format per city:
#   asos_id: Nearest ASOS station identifier
#   asos_name: Station name
#   elevation_ft: Station elevation
#   fire_season_months: Dict of month -> climate normals for fire season
#     Each month contains:
#       avg_high_f, avg_low_f     -- Temperature normals
#       typical_rh_pct            -- Average afternoon RH (fire weather metric)
#       extreme_low_rh_pct        -- 5th-percentile (critical fire weather) RH
#       avg_dewpoint_f            -- Average dewpoint
#       avg_wind_mph              -- Average wind speed
#       max_wind_gust_mph         -- Typical peak gust (95th percentile)
#       extreme_gust_mph          -- Maximum recorded / expected extreme
#       notes                     -- Month-specific fire weather context
#
# Data sources: NWS Climate Normals (1991-2020), RAWS, NIFC fire weather obs
# Extreme values from historical event data and NWCG after-action reports
#

CO_BASIN_CLIMATOLOGY = {

    "colorado_springs_co": {
        "asos_id": "KCOS",
        "asos_name": "City of Colorado Springs Municipal Airport",
        "elevation_ft": 6187,
        "fire_season_months": {
            "april": {
                "avg_high_f": 57, "avg_low_f": 31,
                "typical_rh_pct": 38, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 20, "avg_wind_mph": 11,
                "max_wind_gust_mph": 55, "extreme_gust_mph": 90,
                "notes": "Spring wind season peak. Chinook winds can produce "
                         "extreme fire weather with single-digit RH.",
            },
            "may": {
                "avg_high_f": 66, "avg_low_f": 40,
                "typical_rh_pct": 40, "extreme_low_rh_pct": 10,
                "avg_dewpoint_f": 28, "avg_wind_mph": 10,
                "max_wind_gust_mph": 50, "extreme_gust_mph": 75,
                "notes": "Greening reduces grass fire risk but forest fuels cure.",
            },
            "june": {
                "avg_high_f": 78, "avg_low_f": 49,
                "typical_rh_pct": 35, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 33, "avg_wind_mph": 9,
                "max_wind_gust_mph": 50, "extreme_gust_mph": 70,
                "notes": "Waldo Canyon Fire started June 23. Pre-monsoon dry "
                         "period with increasing heat. Peak fire danger.",
            },
            "july": {
                "avg_high_f": 85, "avg_low_f": 56,
                "typical_rh_pct": 38, "extreme_low_rh_pct": 10,
                "avg_dewpoint_f": 42, "avg_wind_mph": 8,
                "max_wind_gust_mph": 50, "extreme_gust_mph": 65,
                "notes": "Monsoon moisture begins mid-month reducing fire risk. "
                         "Dry thunderstorms possible early July.",
            },
            "august": {
                "avg_high_f": 82, "avg_low_f": 54,
                "typical_rh_pct": 42, "extreme_low_rh_pct": 12,
                "avg_dewpoint_f": 44, "avg_wind_mph": 8,
                "max_wind_gust_mph": 45, "extreme_gust_mph": 60,
                "notes": "Monsoon peak. Reduced fire danger but dry lightning "
                         "still possible.",
            },
            "september": {
                "avg_high_f": 75, "avg_low_f": 46,
                "typical_rh_pct": 38, "extreme_low_rh_pct": 10,
                "avg_dewpoint_f": 36, "avg_wind_mph": 8,
                "max_wind_gust_mph": 45, "extreme_gust_mph": 65,
                "notes": "Post-monsoon drying. Fuels cured, second fire peak.",
            },
            "december": {
                "avg_high_f": 43, "avg_low_f": 18,
                "typical_rh_pct": 45, "extreme_low_rh_pct": 10,
                "avg_dewpoint_f": 10, "avg_wind_mph": 9,
                "max_wind_gust_mph": 55, "extreme_gust_mph": 100,
                "notes": "Marshall Fire conditions: winter downslope wind events "
                         "with extreme gustiness. Dec-Jan chinook fires possible.",
            },
        },
    },

    "boulder_co": {
        "asos_id": "KBDU",
        "asos_name": "Boulder Municipal Airport",
        "elevation_ft": 5288,
        "fire_season_months": {
            "april": {
                "avg_high_f": 60, "avg_low_f": 34,
                "typical_rh_pct": 35, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 22, "avg_wind_mph": 10,
                "max_wind_gust_mph": 60, "extreme_gust_mph": 100,
                "notes": "Spring wind season. Downslope chinook events. "
                         "Grass fires on cured fuels.",
            },
            "june": {
                "avg_high_f": 82, "avg_low_f": 50,
                "typical_rh_pct": 33, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 34, "avg_wind_mph": 8,
                "max_wind_gust_mph": 45, "extreme_gust_mph": 65,
                "notes": "Pre-monsoon fire peak. Hot, dry, afternoon upslope "
                         "storms can produce dry lightning.",
            },
            "july": {
                "avg_high_f": 88, "avg_low_f": 56,
                "typical_rh_pct": 36, "extreme_low_rh_pct": 10,
                "avg_dewpoint_f": 43, "avg_wind_mph": 7,
                "max_wind_gust_mph": 45, "extreme_gust_mph": 60,
                "notes": "Hottest month. Monsoon arrivals reduce risk mid-month.",
            },
            "december": {
                "avg_high_f": 45, "avg_low_f": 20,
                "typical_rh_pct": 42, "extreme_low_rh_pct": 5,
                "avg_dewpoint_f": 10, "avg_wind_mph": 10,
                "max_wind_gust_mph": 70, "extreme_gust_mph": 115,
                "notes": "MARSHALL FIRE CONDITIONS: Dec 30, 2021 -- 115 mph gusts "
                         "sustained for 11 hours from SW. RH dropped to ~5%. "
                         "No precipitation for 3+ months. Winter chinook fires "
                         "are the primary catastrophic risk for this area.",
            },
        },
    },

    "superior_co": {
        "asos_id": "KBDU",
        "asos_name": "Boulder Municipal Airport (nearest)",
        "elevation_ft": 5288,
        "fire_season_months": {
            "december": {
                "avg_high_f": 45, "avg_low_f": 20,
                "typical_rh_pct": 42, "extreme_low_rh_pct": 5,
                "avg_dewpoint_f": 10, "avg_wind_mph": 10,
                "max_wind_gust_mph": 70, "extreme_gust_mph": 115,
                "notes": "See Boulder entry. Superior is more exposed to SW "
                         "downslope winds than Boulder proper. Marshall Fire "
                         "demonstrated that winter chinook grassfire in "
                         "suburban setting can be catastrophic.",
            },
            "april": {
                "avg_high_f": 60, "avg_low_f": 34,
                "typical_rh_pct": 35, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 22, "avg_wind_mph": 10,
                "max_wind_gust_mph": 60, "extreme_gust_mph": 100,
                "notes": "Secondary spring fire risk. Cured grasses in open space.",
            },
        },
    },

    "louisville_co": {
        "asos_id": "KBDU",
        "asos_name": "Boulder Municipal Airport (nearest)",
        "elevation_ft": 5288,
        "fire_season_months": {
            "december": {
                "avg_high_f": 45, "avg_low_f": 20,
                "typical_rh_pct": 42, "extreme_low_rh_pct": 5,
                "avg_dewpoint_f": 10, "avg_wind_mph": 10,
                "max_wind_gust_mph": 70, "extreme_gust_mph": 115,
                "notes": "See Boulder entry. Louisville slightly more sheltered "
                         "than Superior due to greater distance from foothills, "
                         "but Marshall Fire proved wind-driven ember transport "
                         "remains devastating.",
            },
        },
    },

    "estes_park_co": {
        "asos_id": "KLMO",
        "asos_name": "Longmont / Vance Brand Airport (nearest low-elev ASOS)",
        "elevation_ft": 5055,
        "fire_season_months": {
            "june": {
                "avg_high_f": 72, "avg_low_f": 42,
                "typical_rh_pct": 30, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 30, "avg_wind_mph": 7,
                "max_wind_gust_mph": 40, "extreme_gust_mph": 60,
                "notes": "At Estes Park elevation (7,522 ft), temps are ~10F "
                         "cooler. Pre-monsoon dry period with cured grass/timber.",
            },
            "july": {
                "avg_high_f": 72, "avg_low_f": 45,
                "typical_rh_pct": 35, "extreme_low_rh_pct": 10,
                "avg_dewpoint_f": 38, "avg_wind_mph": 6,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 55,
                "notes": "Monsoon moisture arrives. At mountain elevation, "
                         "afternoon thunderstorms common. Dry lightning risk.",
            },
            "october": {
                "avg_high_f": 55, "avg_low_f": 32,
                "typical_rh_pct": 30, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 20, "avg_wind_mph": 8,
                "max_wind_gust_mph": 50, "extreme_gust_mph": 80,
                "notes": "EAST TROUBLESOME FIRE CONDITIONS: Oct 2020, fire ran "
                         "100,000+ acres in one day with extreme wind. Post-monsoon "
                         "drying with strong wind events. This is the most "
                         "dangerous month for the Estes Park area.",
            },
        },
    },

    "fort_collins_co": {
        "asos_id": "KFNL",
        "asos_name": "Fort Collins-Loveland Municipal Airport",
        "elevation_ft": 5016,
        "fire_season_months": {
            "june": {
                "avg_high_f": 82, "avg_low_f": 50,
                "typical_rh_pct": 33, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 34, "avg_wind_mph": 9,
                "max_wind_gust_mph": 50, "extreme_gust_mph": 70,
                "notes": "Pre-monsoon fire peak. Hot days, low humidity, "
                         "afternoon upslope development.",
            },
            "august": {
                "avg_high_f": 84, "avg_low_f": 54,
                "typical_rh_pct": 38, "extreme_low_rh_pct": 10,
                "avg_dewpoint_f": 42, "avg_wind_mph": 7,
                "max_wind_gust_mph": 45, "extreme_gust_mph": 60,
                "notes": "Cameron Peak Fire started Aug 13, 2020. Even during "
                         "monsoon, mountain fires can establish and persist.",
            },
            "october": {
                "avg_high_f": 62, "avg_low_f": 34,
                "typical_rh_pct": 32, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 22, "avg_wind_mph": 9,
                "max_wind_gust_mph": 55, "extreme_gust_mph": 85,
                "notes": "Cameron Peak Fire blowup Oct 14, 2020 -- grew 20,000 "
                         "acres in one day toward Fort Collins. Post-monsoon "
                         "wind events with dry fuels are catastrophic.",
            },
        },
    },

    "evergreen_conifer_co": {
        "asos_id": "KBJC",
        "asos_name": "Rocky Mountain Metropolitan Airport (nearest)",
        "elevation_ft": 5673,
        "fire_season_months": {
            "june": {
                "avg_high_f": 78, "avg_low_f": 48,
                "typical_rh_pct": 32, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 32, "avg_wind_mph": 8,
                "max_wind_gust_mph": 45, "extreme_gust_mph": 65,
                "notes": "At Evergreen elevation (7,220 ft), ~8F cooler. Dense "
                         "forest fuels, pre-monsoon drying. Peak fire danger.",
            },
            "july": {
                "avg_high_f": 85, "avg_low_f": 54,
                "typical_rh_pct": 35, "extreme_low_rh_pct": 10,
                "avg_dewpoint_f": 40, "avg_wind_mph": 7,
                "max_wind_gust_mph": 40, "extreme_gust_mph": 60,
                "notes": "Monsoon arrives but dry lightning possible. Hi Meadow "
                         "Fire started during summer.",
            },
            "march": {
                "avg_high_f": 52, "avg_low_f": 26,
                "typical_rh_pct": 35, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 14, "avg_wind_mph": 10,
                "max_wind_gust_mph": 55, "extreme_gust_mph": 80,
                "notes": "Lower North Fork Fire: March 2012. Spring wind events "
                         "with cured fuels. Prescribed burns especially risky.",
            },
        },
    },

    "durango_co": {
        "asos_id": "KDRO",
        "asos_name": "Durango-La Plata County Airport",
        "elevation_ft": 6685,
        "fire_season_months": {
            "june": {
                "avg_high_f": 82, "avg_low_f": 43,
                "typical_rh_pct": 22, "extreme_low_rh_pct": 6,
                "avg_dewpoint_f": 25, "avg_wind_mph": 8,
                "max_wind_gust_mph": 40, "extreme_gust_mph": 55,
                "notes": "PEAK FIRE DANGER. 416 Fire started June 1, 2018. "
                         "Pre-monsoon extreme dryness, single-digit RH common. "
                         "Hottest and driest month before monsoon arrival.",
            },
            "july": {
                "avg_high_f": 85, "avg_low_f": 49,
                "typical_rh_pct": 32, "extreme_low_rh_pct": 10,
                "avg_dewpoint_f": 38, "avg_wind_mph": 7,
                "max_wind_gust_mph": 40, "extreme_gust_mph": 55,
                "notes": "Monsoon arrives but timing varies. Dry thunderstorms "
                         "possible early July, frequent lightning ignitions.",
            },
            "august": {
                "avg_high_f": 82, "avg_low_f": 47,
                "typical_rh_pct": 38, "extreme_low_rh_pct": 12,
                "avg_dewpoint_f": 42, "avg_wind_mph": 6,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 50,
                "notes": "Monsoon peak, reduced fire danger. But prolonged dry "
                         "monsoon breaks can re-elevate risk.",
            },
        },
    },

    "glenwood_springs_co": {
        "asos_id": "KGWS",
        "asos_name": "Glenwood Springs Municipal Airport",
        "elevation_ft": 5916,
        "fire_season_months": {
            "june": {
                "avg_high_f": 82, "avg_low_f": 45,
                "typical_rh_pct": 25, "extreme_low_rh_pct": 6,
                "avg_dewpoint_f": 24, "avg_wind_mph": 7,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 50,
                "notes": "Pre-monsoon dry period. Canyon terrain amplifies heat "
                         "and dryness. South Canyon Fire was July 1994.",
            },
            "july": {
                "avg_high_f": 88, "avg_low_f": 52,
                "typical_rh_pct": 28, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 32, "avg_wind_mph": 6,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 50,
                "notes": "South Canyon Fire (July 6, 1994): 14 fatalities. "
                         "Canyon terrain traps heat, canyon winds erratic.",
            },
            "august": {
                "avg_high_f": 86, "avg_low_f": 50,
                "typical_rh_pct": 30, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 34, "avg_wind_mph": 6,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 50,
                "notes": "Grizzly Creek Fire started Aug 10, 2020. Canyon "
                         "terrain so steep initial attack failed completely.",
            },
        },
    },

    "steamboat_springs_co": {
        "asos_id": "KSBS",
        "asos_name": "Steamboat Springs / Bob Adams Field",
        "elevation_ft": 6882,
        "fire_season_months": {
            "june": {
                "avg_high_f": 74, "avg_low_f": 37,
                "typical_rh_pct": 30, "extreme_low_rh_pct": 10,
                "avg_dewpoint_f": 28, "avg_wind_mph": 7,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 55,
                "notes": "Warming and drying. Beetle-killed timber begins to "
                         "reach critical moisture levels.",
            },
            "july": {
                "avg_high_f": 82, "avg_low_f": 43,
                "typical_rh_pct": 28, "extreme_low_rh_pct": 10,
                "avg_dewpoint_f": 35, "avg_wind_mph": 6,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 50,
                "notes": "Highest fire risk. Dry thunderstorms in mountains. "
                         "Fish Creek watershed most vulnerable to lightning fires.",
            },
            "august": {
                "avg_high_f": 80, "avg_low_f": 41,
                "typical_rh_pct": 30, "extreme_low_rh_pct": 10,
                "avg_dewpoint_f": 36, "avg_wind_mph": 6,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 55,
                "notes": "Monsoon provides some relief but dry breaks extend "
                         "fire season. Crosho Fire burned in August 2025.",
            },
        },
    },

    "reno_nv": {
        "asos_id": "KRNO",
        "asos_name": "Reno-Tahoe International Airport",
        "elevation_ft": 4404,
        "fire_season_months": {
            "june": {
                "avg_high_f": 84, "avg_low_f": 48,
                "typical_rh_pct": 22, "extreme_low_rh_pct": 6,
                "avg_dewpoint_f": 20, "avg_wind_mph": 10,
                "max_wind_gust_mph": 45, "extreme_gust_mph": 70,
                "notes": "Very dry, hot. Sagebrush and cheatgrass cured. "
                         "Afternoon thermal winds through Truckee Corridor.",
            },
            "july": {
                "avg_high_f": 92, "avg_low_f": 55,
                "typical_rh_pct": 18, "extreme_low_rh_pct": 5,
                "avg_dewpoint_f": 18, "avg_wind_mph": 9,
                "max_wind_gust_mph": 40, "extreme_gust_mph": 60,
                "notes": "Peak heat. Single-digit RH common afternoons. "
                         "Dry thunderstorm potential from Sierra convection.",
            },
            "august": {
                "avg_high_f": 90, "avg_low_f": 53,
                "typical_rh_pct": 18, "extreme_low_rh_pct": 5,
                "avg_dewpoint_f": 18, "avg_wind_mph": 9,
                "max_wind_gust_mph": 40, "extreme_gust_mph": 60,
                "notes": "Continued extreme fire weather. Caldor Fire approached "
                         "Lake Tahoe Aug-Sep 2021.",
            },
            "november": {
                "avg_high_f": 52, "avg_low_f": 29,
                "typical_rh_pct": 45, "extreme_low_rh_pct": 12,
                "avg_dewpoint_f": 18, "avg_wind_mph": 8,
                "max_wind_gust_mph": 55, "extreme_gust_mph": 90,
                "notes": "Pinehaven Fire: Nov 17, 2020. Strong downslope wind "
                         "events (Washoe Zephyr) in late fall create extreme "
                         "fire weather despite cooler temperatures.",
            },
        },
    },

    "south_lake_tahoe_ca_nv": {
        "asos_id": "KTVL",
        "asos_name": "South Lake Tahoe Airport",
        "elevation_ft": 6264,
        "fire_season_months": {
            "june": {
                "avg_high_f": 72, "avg_low_f": 37,
                "typical_rh_pct": 25, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 22, "avg_wind_mph": 8,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 55,
                "notes": "Dry season begins. Snowpack gone, fuels drying. "
                         "Jeffrey pine and fir understory curing.",
            },
            "july": {
                "avg_high_f": 80, "avg_low_f": 42,
                "typical_rh_pct": 20, "extreme_low_rh_pct": 6,
                "avg_dewpoint_f": 18, "avg_wind_mph": 7,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 50,
                "notes": "Driest month. Near-zero precipitation. Fire danger "
                         "high in surrounding forest.",
            },
            "august": {
                "avg_high_f": 79, "avg_low_f": 41,
                "typical_rh_pct": 20, "extreme_low_rh_pct": 6,
                "avg_dewpoint_f": 20, "avg_wind_mph": 7,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 55,
                "notes": "CALDOR/ANGORA FIRE MONTH. Caldor Fire erupted Aug 2021. "
                         "Angora Fire June 2007. Drought amplifies risk enormously.",
            },
            "september": {
                "avg_high_f": 73, "avg_low_f": 36,
                "typical_rh_pct": 22, "extreme_low_rh_pct": 7,
                "avg_dewpoint_f": 18, "avg_wind_mph": 7,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 50,
                "notes": "Extended fire season. Caldor Fire threatened SLT "
                         "Aug 30-Sep 7, 2021. Fuels at seasonal driest.",
            },
        },
    },

    "carson_city_nv": {
        "asos_id": "KCXP",
        "asos_name": "Carson City Airport",
        "elevation_ft": 4697,
        "fire_season_months": {
            "june": {
                "avg_high_f": 82, "avg_low_f": 43,
                "typical_rh_pct": 22, "extreme_low_rh_pct": 6,
                "avg_dewpoint_f": 20, "avg_wind_mph": 9,
                "max_wind_gust_mph": 40, "extreme_gust_mph": 60,
                "notes": "Dry, hot. Sagebrush and pinyon-juniper fuels cured.",
            },
            "july": {
                "avg_high_f": 90, "avg_low_f": 50,
                "typical_rh_pct": 18, "extreme_low_rh_pct": 5,
                "avg_dewpoint_f": 16, "avg_wind_mph": 8,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 55,
                "notes": "Peak fire danger. Extreme afternoon heat and dryness.",
            },
            "august": {
                "avg_high_f": 88, "avg_low_f": 48,
                "typical_rh_pct": 18, "extreme_low_rh_pct": 5,
                "avg_dewpoint_f": 18, "avg_wind_mph": 8,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 55,
                "notes": "Continued extreme dryness. Near-zero precipitation.",
            },
            "september": {
                "avg_high_f": 80, "avg_low_f": 42,
                "typical_rh_pct": 22, "extreme_low_rh_pct": 6,
                "avg_dewpoint_f": 16, "avg_wind_mph": 8,
                "max_wind_gust_mph": 40, "extreme_gust_mph": 60,
                "notes": "Davis Fire burned September 2024 in Washoe Valley. "
                         "Wind events increase in fall.",
            },
        },
    },

    "cedar_city_ut": {
        "asos_id": "KCDC",
        "asos_name": "Cedar City Regional Airport",
        "elevation_ft": 5622,
        "fire_season_months": {
            "june": {
                "avg_high_f": 85, "avg_low_f": 48,
                "typical_rh_pct": 18, "extreme_low_rh_pct": 5,
                "avg_dewpoint_f": 18, "avg_wind_mph": 8,
                "max_wind_gust_mph": 40, "extreme_gust_mph": 60,
                "notes": "BRIAN HEAD FIRE MONTH. June 2017 ignition. Pre-monsoon "
                         "extreme dryness, driest air in America (RH 10-20%). "
                         "Fire danger extreme on Markagunt Plateau above.",
            },
            "july": {
                "avg_high_f": 90, "avg_low_f": 55,
                "typical_rh_pct": 25, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 32, "avg_wind_mph": 7,
                "max_wind_gust_mph": 40, "extreme_gust_mph": 55,
                "notes": "Monsoon arrives, increasing humidity and thunderstorm "
                         "activity. Dry lightning risk at higher elevations.",
            },
            "august": {
                "avg_high_f": 87, "avg_low_f": 53,
                "typical_rh_pct": 28, "extreme_low_rh_pct": 10,
                "avg_dewpoint_f": 36, "avg_wind_mph": 6,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 50,
                "notes": "Monsoon moisture reduces fire danger on most days. "
                         "Dry breaks between monsoon surges remain dangerous.",
            },
        },
    },

    "park_city_ut": {
        "asos_id": "KSLC",
        "asos_name": "Salt Lake City International (nearest major ASOS)",
        "elevation_ft": 4226,
        "fire_season_months": {
            "june": {
                "avg_high_f": 83, "avg_low_f": 55,
                "typical_rh_pct": 25, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 28, "avg_wind_mph": 8,
                "max_wind_gust_mph": 40, "extreme_gust_mph": 60,
                "notes": "At Park City elevation (7,000 ft), temps ~10F cooler "
                         "but humidity similar. Dense forest fuels drying.",
            },
            "july": {
                "avg_high_f": 92, "avg_low_f": 63,
                "typical_rh_pct": 20, "extreme_low_rh_pct": 6,
                "avg_dewpoint_f": 28, "avg_wind_mph": 7,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 55,
                "notes": "Driest month. Old Town pine forest extremely vulnerable "
                         "to fire establishment in these conditions.",
            },
            "august": {
                "avg_high_f": 90, "avg_low_f": 61,
                "typical_rh_pct": 22, "extreme_low_rh_pct": 7,
                "avg_dewpoint_f": 30, "avg_wind_mph": 7,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 50,
                "notes": "Continued dry heat. Wasatch Range lightning storms "
                         "increase ignition risk in surrounding forest.",
            },
            "september": {
                "avg_high_f": 80, "avg_low_f": 51,
                "typical_rh_pct": 25, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 25, "avg_wind_mph": 7,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 55,
                "notes": "Extended fire season. Fuels at seasonal driest. "
                         "Wind events increase in fall.",
            },
        },
    },

    "jackson_wy": {
        "asos_id": "KJAC",
        "asos_name": "Jackson Hole Airport",
        "elevation_ft": 6451,
        "fire_season_months": {
            "june": {
                "avg_high_f": 72, "avg_low_f": 35,
                "typical_rh_pct": 30, "extreme_low_rh_pct": 10,
                "avg_dewpoint_f": 25, "avg_wind_mph": 8,
                "max_wind_gust_mph": 40, "extreme_gust_mph": 60,
                "notes": "Snowmelt complete, fuels drying. Sagebrush and grass "
                         "in valley, timber on mountain flanks.",
            },
            "july": {
                "avg_high_f": 80, "avg_low_f": 40,
                "typical_rh_pct": 25, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 25, "avg_wind_mph": 7,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 55,
                "notes": "PEAK FIRE DANGER. Berry Fire (2016) July. Dry "
                         "thunderstorms in Teton and Gros Ventre ranges. "
                         "Sagebrush embers carry 20+ miles in wind events.",
            },
            "august": {
                "avg_high_f": 78, "avg_low_f": 38,
                "typical_rh_pct": 25, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 26, "avg_wind_mph": 7,
                "max_wind_gust_mph": 35, "extreme_gust_mph": 55,
                "notes": "Roosevelt Fire (2018) August-September. Extended dry "
                         "periods possible despite mountain thunderstorms.",
            },
            "september": {
                "avg_high_f": 67, "avg_low_f": 30,
                "typical_rh_pct": 28, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 20, "avg_wind_mph": 7,
                "max_wind_gust_mph": 40, "extreme_gust_mph": 60,
                "notes": "Fall drying. Wind events increase. Fire season extends "
                         "through September in most years.",
            },
        },
    },

    "cody_wy": {
        "asos_id": "KCOD",
        "asos_name": "Yellowstone Regional Airport",
        "elevation_ft": 5098,
        "fire_season_months": {
            "june": {
                "avg_high_f": 76, "avg_low_f": 44,
                "typical_rh_pct": 30, "extreme_low_rh_pct": 10,
                "avg_dewpoint_f": 28, "avg_wind_mph": 9,
                "max_wind_gust_mph": 45, "extreme_gust_mph": 65,
                "notes": "Basin rangeland drying. Wind through Shoshone Canyon "
                         "can be channeled and gusty.",
            },
            "july": {
                "avg_high_f": 85, "avg_low_f": 50,
                "typical_rh_pct": 22, "extreme_low_rh_pct": 6,
                "avg_dewpoint_f": 26, "avg_wind_mph": 8,
                "max_wind_gust_mph": 40, "extreme_gust_mph": 60,
                "notes": "Peak fire danger. Sagebrush-grassland on basin floor, "
                         "timber fires in Absaroka Range. Hot and dry.",
            },
            "august": {
                "avg_high_f": 84, "avg_low_f": 48,
                "typical_rh_pct": 22, "extreme_low_rh_pct": 6,
                "avg_dewpoint_f": 26, "avg_wind_mph": 8,
                "max_wind_gust_mph": 40, "extreme_gust_mph": 60,
                "notes": "Blackwater Fire: August 1937. Continued extreme fire "
                         "weather. Mountain thunderstorms provide lightning ignitions.",
            },
            "september": {
                "avg_high_f": 73, "avg_low_f": 39,
                "typical_rh_pct": 28, "extreme_low_rh_pct": 8,
                "avg_dewpoint_f": 22, "avg_wind_mph": 8,
                "max_wind_gust_mph": 40, "extreme_gust_mph": 60,
                "notes": "Fall drying. Wind events increase. Rangeland and "
                         "mountain transition fires possible.",
            },
        },
    },
}


# =============================================================================
# Convenience lookups
# =============================================================================

def list_profiled_cities() -> list:
    """List all cities with fire vulnerability profiles.

    Returns:
        List of dicts with key, center, elevation, and WUI class.
    """
    return [
        {
            "key": key,
            "center": profile["center"],
            "elevation_ft": profile["elevation_ft"],
            "wui_class": profile.get("wui_class", "unknown"),
            "historical_fires": len(profile.get("historical_fires", [])),
        }
        for key, profile in CO_BASIN_TERRAIN_PROFILES.items()
    ]


def get_city_profile(city_key: str) -> dict:
    """Get full profile (terrain + ignition + climate) for a city.

    Args:
        city_key: City identifier (e.g., 'boulder_co', 'reno_nv')

    Returns:
        Dict with terrain, ignition, and climate data, or empty dict if not found.
    """
    result = {}
    if city_key in CO_BASIN_TERRAIN_PROFILES:
        result["terrain"] = CO_BASIN_TERRAIN_PROFILES[city_key]
    if city_key in CO_BASIN_IGNITION_SOURCES:
        result["ignition"] = CO_BASIN_IGNITION_SOURCES[city_key]
    if city_key in CO_BASIN_CLIMATOLOGY:
        result["climatology"] = CO_BASIN_CLIMATOLOGY[city_key]
    return result


def get_historical_fires(city_key: str) -> list:
    """Get historical fire list for a city.

    Args:
        city_key: City identifier

    Returns:
        List of historical fire dicts, or empty list.
    """
    profile = CO_BASIN_TERRAIN_PROFILES.get(city_key, {})
    return profile.get("historical_fires", [])


# Total: 17 cities profiled
# - 10 Colorado (Colorado Springs, Boulder, Superior, Louisville, Estes Park,
#                Fort Collins, Evergreen/Conifer, Durango, Glenwood Springs,
#                Steamboat Springs)
# - 3 Nevada (Reno, South Lake Tahoe, Carson City)
# - 2 Utah (Cedar City, Park City)
# - 2 Wyoming (Jackson, Cody)
