"""
Colorado Fire-Vulnerable City Profiles — Research-Paper Quality
================================================================
18 cities: 10 enhanced existing + 8 new vulnerable towns.
Data compiled from NIFC, USFS, NWS, Colorado Sun, Denver Post,
Wikipedia, InciWeb, Colorado Encyclopedia, and official AARs.

Key Colorado fire context:
- Marshall Fire (Dec 30 2021): 1,084 structures, most destructive CO fire
- East Troublesome (Oct 2020): 193,812 acres, 2nd largest CO fire, crossed Continental Divide
- Cameron Peak (2020): 208,663 acres, largest CO fire in history
- Hayman (2002): 137,760 acres, arson, largest at the time
- Waldo Canyon (2012): 347 homes destroyed in Colorado Springs
- Black Forest (2013): 486-511 homes destroyed, 14,280 acres
- Front Range Chinook/downslope winds: 100+ mph gusts, extreme fire weather
"""

CO_ENHANCED = {

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
}
