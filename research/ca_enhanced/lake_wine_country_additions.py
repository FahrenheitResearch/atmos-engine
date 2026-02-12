"""
Lake County, Wine Country & Mendocino Fire-Vulnerable City Profiles
====================================================================

Deep-research profiles for 10 fire-vulnerable communities in Lake County,
Napa/Sonoma Wine Country, and Mendocino County. These communities have
experienced some of the most devastating wildfires in California history,
including the Valley Fire (2015), Clayton Fire (2016), October 2017 Wine
Country Fires (Tubbs, Nuns, Atlas), Mendocino Complex (2018), Redwood
Complex (2017), and Glass Fire (2020).

Written with operationally relevant detail derived from CAL FIRE incident
reports, county after-action reviews, NIST case studies, NWS post-event
summaries, and investigative journalism.

Sources:
    - CAL FIRE incident reports: Valley, Clayton, Tubbs, Nuns, Glass,
      Mendocino Complex, Redwood Complex, Sulphur, Pawnee, Cache fires
    - Fire Weather Research Lab: Valley Fire rapid spread analysis
    - NIST technical notes on WUI fire behavior
    - Napa County Grand Jury: Angwin evacuation assessment (2021)
    - Sonoma County AAR (June 2018): October 2017 Complex Fires
    - KLD Associates SAFE Study (Feb 2025): Sonoma Valley evacuation modeling
    - Mendocino County Fire Vulnerability Assessment (MCog)
    - Lake County Community Wildfire Protection Plan
    - Press Democrat, Mendocino Voice, Napa Valley Register investigative reporting
    - U.S. Census Bureau 2020 decennial census
    - First Street Foundation wildfire risk assessments
"""

LAKE_WINE_COUNTRY_ADDITIONS = {

    # =========================================================================
    # LAKE COUNTY -- Valley Fire / Clayton Fire / Mendocino Complex zone
    # =========================================================================

    "middletown_ca": {
        "center": [38.7524, -122.6150],
        "terrain_notes": (
            "Small unincorporated community (pop. 1,114 per 2020 census) in a "
            "narrow valley at the junction of Highway 29 and Highway 175, flanked "
            "by the Mayacamas Mountains to the west and Cobb Mountain to the north. "
            "Elevation ~1,099 ft in a broad alluvial valley drained by Putah Creek "
            "and St. Helena Creek. The Valley Fire (Sep 12, 2015) was the defining "
            "catastrophe: ignited by faulty hot tub wiring near Cobb at 1:00 PM, "
            "the fire consumed 40,000 acres in the first 12 hours, driven by "
            "terrain-channeled winds through the Mayacamas slopes. Fire reached "
            "Middletown by early evening, incinerating much of the commercial "
            "district and residential areas along Highway 29. The fire ultimately "
            "burned 76,067 acres, destroyed 1,955 structures (including 1,322 "
            "homes and 27 multi-unit buildings), and killed 4 people. At the time, "
            "it was the 3rd most destructive wildfire in California history. "
            "Middletown's position at the base of steep, chaparral-covered slopes "
            "creates extreme pre-heating conditions during downslope fire runs. "
            "The community sits in a topographic funnel where fire descending from "
            "Cobb Mountain or the Mayacamas crest accelerates through narrowing "
            "terrain directly into the populated valley floor. Post-fire recovery "
            "has been slow; a 2019 CalMatters investigation documented severe "
            "impacts on local schools, with enrollment drops of 30%+ and sustained "
            "trauma effects on the student population."
        ),
        "key_features": [
            "Junction of Hwy 29 and Hwy 175 -- primary intersection and commercial core",
            "Putah Creek drainage -- runs W through valley, fuels moisture corridor but also fire path",
            "Mayacamas Mountains west flank -- steep chaparral slopes rising 1,500+ ft above valley",
            "Cobb Mountain (4,724 ft) to the north -- pine/fir forests on slopes above town",
            "St. Helena Creek -- drains south toward Napa County, secondary fire corridor",
            "Hidden Valley Lake (5 mi SE) -- gated community of 3,000+ also devastated by Valley Fire",
            "Boggs Mountain Demonstration State Forest -- 3,500 acres of managed timberland NE of town",
        ],
        "elevation_range_ft": [950, 1200],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Valley Fire",
                "year": 2015,
                "acres": 76067,
                "details": (
                    "Ignited Sep 12 near Cobb (faulty hot tub wiring). Consumed 40,000 acres "
                    "in 12 hours -- one of the fastest-spreading fires in CA history. Destroyed "
                    "1,955 structures including 1,322 homes. 4 fatalities. Displaced 20,000+ "
                    "people. 3rd most destructive CA fire at the time. Extreme drought conditions "
                    "(D3-D4) and terrain-channeled winds drove explosive spread. Long-distance "
                    "ember spotting documented. Middletown commercial district largely destroyed."
                ),
            },
            {
                "name": "Jerusalem Fire",
                "year": 2015,
                "acres": 25118,
                "details": (
                    "Burned Aug 9-24 in the Knoxville area SE of Middletown. 6 structures "
                    "destroyed. Demonstrated the persistent fire threat from the eastern "
                    "Mayacamas terrain. Occurred just one month before the Valley Fire."
                ),
            },
            {
                "name": "Rocky Fire",
                "year": 2015,
                "acres": 69438,
                "details": (
                    "Jul-Aug 2015, burned NW of Clearlake. 43 residences destroyed. Part of "
                    "the devastating 2015 fire season that preceded the Valley Fire. Lake County "
                    "had already been in emergency mode for weeks when Valley Fire struck."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 29 south",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Two-lane highway through winding terrain toward Calistoga/St. Helena. "
                    "Passes through narrow canyon sections with heavy vegetation on both sides. "
                    "During Valley Fire, this route was threatened by fire and traffic gridlocked."
                ),
                "risk": (
                    "Fire approaching from west (Mayacamas) or east can cut this route. "
                    "Narrow, winding sections with no shoulders create bottleneck."
                ),
            },
            {
                "route": "Highway 29 north",
                "direction": "N",
                "lanes": 2,
                "bottleneck": (
                    "Two-lane highway north toward Lower Lake and Lakeport. Passes through "
                    "relatively open terrain but merges with Hwy 53 traffic near Lower Lake."
                ),
                "risk": "Fire from the east (Cobb area) can cut access at multiple points.",
            },
            {
                "route": "Highway 175 west",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "Narrow, winding mountain road climbing over the Mayacamas to Hopland "
                    "and US-101. Extremely steep grades, tight switchbacks, no shoulders. "
                    "38-mile route through dense forest and chaparral."
                ),
                "risk": (
                    "Highly vulnerable to fire closure. Passes through some of the most "
                    "fire-prone terrain in the county. Not viable for mass evacuation."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Diablo winds (NE offshore flow) accelerate over the Mayacamas crest and "
                "funnel through canyons into the Middletown valley. Local thermal winds "
                "also drive upslope/downslope patterns on Cobb Mountain flanks. Valley Fire "
                "spread was amplified by terrain channeling and extreme drought."
            ),
            "critical_corridors": [
                "Cobb Mountain descent -- fire runs downhill from Cobb through pine/chaparral to valley floor",
                "Putah Creek drainage -- channels wind and fire W-E through the valley",
                "Mayacamas western slopes -- steep terrain with dense chaparral creates rapid upslope runs",
                "St. Helena Creek canyon -- fire corridor connecting to Napa County",
            ],
            "rate_of_spread_potential": (
                "Extreme. Valley Fire documented 40,000 acres in 12 hours. Slope-driven "
                "runs on the Mayacamas flanks exceed 200 chains/hour in heavy chaparral. "
                "Valley floor grasslands allow rapid lateral spread at 50-100 chains/hour."
            ),
            "spotting_distance": (
                "Long-distance spotting (0.5-1.5 mi) documented during Valley Fire. "
                "Convective column collapse and terrain-channeled winds lofted embers "
                "well ahead of the fire front, igniting spot fires in Middletown before "
                "the main front arrived from Cobb."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Small community water system with limited storage capacity. During "
                "Valley Fire, hydrant pressure failed as multiple structures burned "
                "simultaneously. System rebuilt post-fire but storage remains limited "
                "relative to simultaneous-ignition demand."
            ),
            "power": (
                "PG&E distribution lines through heavy vegetation. Subject to PSPS "
                "de-energization during red flag events. Valley Fire destroyed power "
                "infrastructure throughout the community. PG&E microgrids under "
                "development for Lake County to maintain power during PSPS events."
            ),
            "communications": (
                "Limited cell coverage in surrounding terrain. Cell towers on Cobb "
                "Mountain and Mayacamas ridgeline vulnerable to fire damage. During "
                "Valley Fire, communications were severely degraded. Lake County "
                "has invested in improved emergency notification but coverage gaps persist."
            ),
            "medical": (
                "No hospital in Middletown. Nearest hospital: Sutter Lakeside Hospital "
                "in Lakeport (~30 min north) or Adventist Health St. Helena (~30 min south). "
                "During fire, both routes may be compromised."
            ),
        },
        "demographics_risk_factors": {
            "population": 1114,
            "seasonal_variation": (
                "Modest summer tourism to Clear Lake area. Hidden Valley Lake (5 mi SE) "
                "adds ~3,000 residents to the evacuation demand."
            ),
            "elderly_percentage": "est. 20-22% (Lake County median age 43.5, higher than state avg)",
            "mobile_homes": (
                "Significant mobile home presence in surrounding areas. Valley Fire "
                "disproportionately destroyed manufactured housing. Mobile homes "
                "represent ~15-20% of housing stock in greater Middletown area."
            ),
            "special_needs_facilities": (
                "Limited. No nursing homes in immediate area. Middletown Elementary "
                "and Middletown High School serve as evacuation gathering points."
            ),
        },
    },

    "cobb_ca": {
        "center": [38.8226, -122.7234],
        "terrain_notes": (
            "Mountain community (pop. 1,295 per 2020 census, down from 1,778 in "
            "2010 -- a 27% decline attributable to Valley Fire displacement) perched "
            "on the flanks of Cobb Mountain at ~2,600 ft elevation along Highway 175. "
            "Cobb Mountain (4,724 ft) is the highest peak in the Mayacamas Mountains. "
            "The community is surrounded by dense pine and mixed-conifer forest with "
            "heavy fuel loads -- ponderosa pine, Douglas fir, and live oak create a "
            "continuous canopy over most residential areas. The Valley Fire (2015) "
            "originated HERE: faulty hot tub wiring at a residence near the "
            "intersection of High Valley Road and Bottlerock Road ignited at ~1:00 PM "
            "on Sep 12. Fire investigators identified this location as ground zero. "
            "Within 5 hours, Cobb was largely destroyed, along with the historic "
            "Hoberg's Resort (originally built in the 1880s as a mountain retreat; "
            "later used by Maharishi Mahesh Yogi as a TM center in the 1970s; "
            "reopened as resort in 2014, destroyed 2015). Harbin Hot Springs "
            "community was also obliterated. The fire moved downhill through heavy "
            "timber and chaparral toward Middletown and Hidden Valley Lake with "
            "explosive velocity. Anderson Springs, a small community south of Cobb, "
            "lost all but 19 homes; residents could not rebuild because building "
            "codes prohibited new septic systems, and the $7M sewer cost was "
            "prohibitive. Population decline reflects permanent displacement -- "
            "many residents never returned."
        ),
        "key_features": [
            "Cobb Mountain summit (4,724 ft) -- highest point in Mayacamas range, looms directly above",
            "Highway 175 -- sole paved route, narrow and winding through dense forest",
            "Bottlerock Road -- secondary road to Napa County, site of Valley Fire ignition area",
            "The Geysers geothermal field -- largest complex of geothermal power plants in world, NE of Cobb",
            "Hoberg's Resort site -- historic resort destroyed in Valley Fire, not rebuilt",
            "Anderson Springs (2 mi S) -- community almost completely destroyed, rebuilding blocked by septic codes",
            "Harbin Hot Springs -- retreat community destroyed in Valley Fire, partially rebuilt by 2020",
            "Boggs Mountain Demonstration State Forest -- managed timberland adjacent to community",
            "Pine-dominated forest canopy -- continuous overhead fuel creating extreme crown fire potential",
        ],
        "elevation_range_ft": [2200, 3200],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Valley Fire",
                "year": 2015,
                "acres": 76067,
                "details": (
                    "GROUND ZERO. Fire ignited near intersection of High Valley Rd and "
                    "Bottlerock Rd at 1:00 PM Sep 12. Caused by faulty hot tub wiring. "
                    "Destroyed most of Cobb within hours. 1,955 total structures destroyed "
                    "across the fire's footprint. 4 fatalities. Historic Hoberg's Resort "
                    "destroyed. Harbin Hot Springs destroyed. Anderson Springs nearly "
                    "obliterated (all but 19 homes). 76,067 acres, contained Oct 15."
                ),
            },
            {
                "name": "Mendocino Complex (Ranch Fire component)",
                "year": 2018,
                "acres": 459123,
                "details": (
                    "While the Ranch Fire burned primarily N and E of Cobb Mountain, "
                    "the massive complex (459,123 combined acres, largest CA fire at the "
                    "time) demonstrated the continued vulnerability of the Cobb Mountain "
                    "area. Evacuation warnings issued for Cobb-area communities."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 175 south toward Middletown",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Narrow, winding mountain road descending 1,500 ft in elevation "
                    "through dense pine forest. Multiple blind curves. No shoulders. "
                    "Single-lane bridges. Heavily used by Geysers plant workers."
                ),
                "risk": (
                    "Extremely vulnerable. During Valley Fire, this route was overtaken "
                    "by fire. Dense forest canopy closes over the road creating ember "
                    "tunnels. Trees falling across roadway can trap evacuees."
                ),
            },
            {
                "route": "Highway 175 west toward Hopland/US-101",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "Continues west from Cobb, winding through mountains for ~25 miles "
                    "to reach Hopland on US-101. Extremely remote, no services."
                ),
                "risk": (
                    "Fire from the west (as in a Mendocino Complex scenario) would "
                    "block this route. Remote terrain means delayed emergency response."
                ),
            },
            {
                "route": "Bottlerock Road south to Napa County",
                "direction": "SE",
                "lanes": 2,
                "bottleneck": (
                    "Narrow, steep mountain road dropping through heavy forest and "
                    "chaparral to the Napa Valley. Poor pavement condition. Extremely "
                    "winding with steep grades. Limited use for mass evacuation."
                ),
                "risk": (
                    "Valley Fire ignited adjacent to this road. Dense vegetation on "
                    "both sides. Essentially a tunnel through fuel."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Terrain-driven winds dominate. Diablo winds accelerate over the "
                "Mayacamas crest and downslope. Local slope winds drive upslope fire "
                "runs on all flanks of Cobb Mountain during afternoon heating. The "
                "Geysers geothermal area creates localized heat effects."
            ),
            "critical_corridors": [
                "Cobb Mountain west slope -- downhill runs toward Highway 175 and Middletown",
                "Anderson Springs drainage -- funnels fire S from Cobb toward Hidden Valley Lake",
                "Bottlerock Road corridor -- fire path through dense forest to Napa County",
                "Putah Creek headwaters -- channels fire movement along creek drainage",
            ],
            "rate_of_spread_potential": (
                "Extreme crown fire potential in continuous pine/fir canopy. Valley Fire "
                "demonstrated >3,000 acres/hour spread rate through this terrain. Steep "
                "slopes (30-60%) with heavy ladder fuels enable rapid transition from "
                "surface to crown fire. Drought-stressed pine is highly flammable."
            ),
            "spotting_distance": (
                "1-2 mile spotting documented during Valley Fire. Pine bark embers "
                "lofted by convective column spotted well downhill into Middletown "
                "valley. Terrain channeling amplifies spotting distance."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Community water system with very limited storage. Most residences "
                "on wells with electric pumps -- no pumping during power outage. "
                "No fire hydrant system outside immediate Cobb core."
            ),
            "power": (
                "PG&E lines through dense forest highly vulnerable to tree strikes "
                "and fire damage. Frequent PSPS shutoffs. Ironic proximity to The "
                "Geysers -- largest geothermal complex in the world is adjacent, "
                "yet community loses power regularly. PG&E microgrid projects planned."
            ),
            "communications": (
                "Very limited cell coverage. Mountain terrain blocks signals. "
                "During Valley Fire, most communications failed. Amateur radio "
                "was primary communication method for days after the fire."
            ),
            "medical": (
                "No medical facilities. Nearest hospital in Lakeport (~35 min) or "
                "St. Helena (~45 min via Bottlerock). During fire, response times "
                "effectively infinite. Helicopter access limited by terrain and smoke."
            ),
        },
        "demographics_risk_factors": {
            "population": 1295,
            "seasonal_variation": (
                "Summer population increases with vacation homes and Geysers workers. "
                "Harbin Hot Springs visitors add transient population unfamiliar with "
                "evacuation routes."
            ),
            "elderly_percentage": "est. 25-28% (retirement/rural community, high median age)",
            "mobile_homes": (
                "Significant manufactured housing presence -- many Valley Fire losses "
                "were mobile/manufactured homes. Estimated 20-25% of housing stock."
            ),
            "special_needs_facilities": (
                "None. Extremely limited social services. Community relies on volunteer "
                "fire department and mutual aid from CAL FIRE."
            ),
        },
    },

    "clearlake_ca": {
        "center": [38.9582, -122.6264],
        "terrain_notes": (
            "Lake County's largest city (pop. 16,685 per 2020 census) on the southern "
            "shore of Clear Lake, the largest natural freshwater lake entirely within "
            "California. Elevation ~1,417 ft. The city occupies gently rolling terrain "
            "between Clear Lake to the north and volcanic hills to the south and east. "
            "Clearlake has been described as a community under perpetual fire siege: "
            "nearly 70% of Lake County's land mass has burned in catastrophic wildfires "
            "since 2015 alone. The city itself has been directly threatened by the "
            "Sulphur Fire (2017, 2,207 acres, 162 structures destroyed mostly in "
            "Clearlake Oaks), Clayton Fire (2016, which impacted adjacent Lower Lake "
            "and burned toward Clearlake), Cache Fire (2021, 80 acres, dozens of homes "
            "destroyed in mobile home parks within city limits), and the Pawnee Fire "
            "(2018, 15,185 acres near Clearlake Oaks). The city has significant socio-"
            "economic vulnerability: it is one of the poorest incorporated cities in "
            "California, with high rates of poverty, disability, and elderly residents. "
            "Large mobile home parks along Cache Creek and along the lake shore are "
            "disproportionately vulnerable. The terrain south and east of the city "
            "rises steeply into volcanic hills covered in chaparral and blue oak "
            "woodland -- the WUI interface runs along much of the city's southern "
            "and eastern perimeter."
        ),
        "key_features": [
            "Clear Lake -- largest natural freshwater lake in CA, defines northern city boundary",
            "Cache Creek -- drains Clear Lake SE through Lower Lake, corridor for fire and wind",
            "Highway 53 -- primary route connecting Clearlake to Hwy 20 and Hwy 29",
            "Highway 20 -- E-W route along northern shore of Clear Lake",
            "Volcanic hills south/east -- chaparral-covered terrain rising above city",
            "Sulphur Bank Mercury Mine (EPA Superfund site) -- environmental contamination overlay",
            "Anderson Marsh State Historic Park -- 1,065 acres of grassland/oak/tule marsh at Cache Creek head",
            "Multiple mobile home parks along Cache Creek and lake shore -- concentrated vulnerability",
        ],
        "elevation_range_ft": [1320, 1600],
        "wui_exposure": "high",
        "historical_fires": [
            {
                "name": "Sulphur Fire",
                "year": 2017,
                "acres": 2207,
                "details": (
                    "Ignited 11:59 PM Oct 8 along Sulphur Bank Road off Hwy 20 in "
                    "Clearlake Oaks, near Clearlake city limits. 162 structures destroyed, "
                    "mostly homes. Part of the devastating October 2017 fire siege that "
                    "simultaneously hit Napa/Sonoma (Tubbs, Nuns, Atlas fires)."
                ),
            },
            {
                "name": "Clayton Fire",
                "year": 2016,
                "acres": 3929,
                "details": (
                    "Arson fire (Damin Pashilk convicted). Ignited 6 PM Aug 13 near "
                    "Lower Lake. Burned north toward Clearlake, crossing Morgan Valley "
                    "Road and Cache Creek. 300 structures destroyed (189 homes, 8 "
                    "commercial, 102 outbuildings). Evacuations in both Lower Lake and "
                    "Clearlake."
                ),
            },
            {
                "name": "Cache Fire",
                "year": 2021,
                "acres": 80,
                "details": (
                    "Small but devastating fire within/adjacent to Clearlake city limits. "
                    "Destroyed dozens of homes concentrated in Cache Creek Mobile Home Park "
                    "and Cache Creek Mobile Home Estates. 1,600 residents evacuated with "
                    "minutes of warning. Demonstrated the vulnerability of mobile home "
                    "communities to fast-moving grass/brush fires."
                ),
            },
            {
                "name": "Pawnee Fire",
                "year": 2018,
                "acres": 15185,
                "details": (
                    "Burned near Clearlake Oaks, Jun 23-Jul 8. 22 structures destroyed, "
                    "6 damaged. Spring Hills community threatened."
                ),
            },
            {
                "name": "Valley Fire",
                "year": 2015,
                "acres": 76067,
                "details": (
                    "While centered on Middletown/Cobb, smoke and evacuation impacts "
                    "reached Clearlake. Demonstrated county-wide vulnerability."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 53 south to Highway 29",
                "direction": "S",
                "lanes": 4,
                "bottleneck": (
                    "4-lane divided expressway is the primary route south from Clearlake "
                    "to Lower Lake and Highway 29. Relatively good capacity but merges to "
                    "2 lanes at Highway 29 junction."
                ),
                "risk": (
                    "Clayton Fire (2016) crossed Cache Creek and threatened this corridor. "
                    "Fire from southern hills could block access at Lower Lake junction."
                ),
            },
            {
                "route": "Highway 20 east toward Williams/I-5",
                "direction": "E",
                "lanes": 2,
                "bottleneck": (
                    "Two-lane highway winding along the northern shore of Clear Lake, "
                    "then through remote Cache Creek canyon toward the Sacramento Valley. "
                    "Narrow, winding, and remote for ~50 miles."
                ),
                "risk": (
                    "Pawnee Fire (2018) threatened this route near Clearlake Oaks. "
                    "Remote canyon sections highly vulnerable to fire closure."
                ),
            },
            {
                "route": "Highway 20 west toward Lakeport/US-101",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "Two-lane highway along the western shore of Clear Lake to Lakeport, "
                    "then over the Mayacamas to Ukiah. Moderate capacity."
                ),
                "risk": "Mendocino Complex (2018) threatened this route. Long detour to reach US-101.",
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Lake-breeze circulation creates afternoon onshore winds from Clear Lake "
                "that can push fire uphill into southern/eastern hills. Diablo wind events "
                "drive NE offshore flow over the surrounding hills and into the lake basin. "
                "The flat lake surface provides minimal friction, allowing high wind speeds."
            ),
            "critical_corridors": [
                "Cache Creek drainage -- channels fire SE from Clear Lake basin toward Lower Lake",
                "Southern volcanic hills -- chaparral-covered terrain above mobile home parks",
                "Sulphur Bank area -- Hwy 20 corridor between Clearlake and Clearlake Oaks",
                "Eastern hills toward Spring Valley -- fire can descend into developed areas",
            ],
            "rate_of_spread_potential": (
                "Moderate to high. Grass and chaparral fuels on southern hills allow rapid "
                "spread (50-150 chains/hour in grass, 30-80 in chaparral). Cache Fire (2021) "
                "demonstrated that even small fires can destroy dozens of structures within "
                "an hour in densely-spaced mobile home parks."
            ),
            "spotting_distance": (
                "0.25-0.5 mile spotting in chaparral fires. Urban conflagration risk in "
                "mobile home parks where structure-to-structure ignition can occur at "
                "distances of 15-30 ft from radiant heat alone."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "City water system draws from Clear Lake. Adequate source water but "
                "distribution system is aging with limited pressure in hillside areas. "
                "Mobile home parks often on small private water systems with minimal "
                "fire suppression capacity."
            ),
            "power": (
                "PG&E PSPS events are frequent in Lake County -- Clearlake has experienced "
                "multiple multi-day shutoffs. City maintains a community resource center "
                "during PSPS events. Many residents lack backup power. PG&E developing "
                "4 temporary microgrids in Lake County; 5 substations prepared for mobile "
                "generators."
            ),
            "communications": (
                "Cell coverage adequate in city core but degrades rapidly in surrounding "
                "hills. Emergency notification via Lake County OES; system tested regularly. "
                "Sulphur Bank Mercury Mine Superfund site complicates some emergency planning."
            ),
            "medical": (
                "Adventist Health Clear Lake (Clearlake) provides local hospital services. "
                "However, hospital capacity is limited and was strained during past fire "
                "evacuations. Nearest Level II trauma center is in Santa Rosa (~90 min)."
            ),
        },
        "demographics_risk_factors": {
            "population": 16685,
            "seasonal_variation": (
                "Summer tourism to Clear Lake increases population. Bass fishing and "
                "recreation draw visitors unfamiliar with fire evacuation procedures."
            ),
            "elderly_percentage": "est. 22-25% (high proportion of retirees, fixed-income residents)",
            "mobile_homes": (
                "CRITICAL vulnerability. Large mobile home parks -- Cache Creek MHP, "
                "Cache Creek Mobile Home Estates, and others -- contain hundreds of "
                "units with minimal fire resistance. Cache Fire (2021) destroyed dozens "
                "of homes in these parks. Mobile/manufactured homes estimated at 25-30% "
                "of housing stock."
            ),
            "special_needs_facilities": (
                "Multiple assisted living facilities and board-and-care homes. High "
                "disability rate (~25% of population). Significant homeless population. "
                "One of the poorest incorporated cities in California (median household "
                "income ~$27,000)."
            ),
        },
    },

    "lower_lake_ca": {
        "center": [38.9100, -122.6100],
        "terrain_notes": (
            "Small unincorporated community (pop. 1,276 per 2020 census) at the "
            "junction of Highway 29 and Highway 53, situated at the head of Cache "
            "Creek where it exits the Clear Lake basin. Elevation ~1,371 ft. The "
            "community lies in a WUI transition zone between the agricultural/lake "
            "shore areas to the north and the chaparral-covered volcanic hills to "
            "the south and west. Anderson Marsh State Historic Park (1,065 acres of "
            "native grassland, oak woodland, and tule marsh) sits between Lower Lake "
            "and Clearlake. The Clayton Fire (Aug 13, 2016) was an arson fire that "
            "devastated Lower Lake: ignited at 6 PM near town, it burned aggressively "
            "north, crossing Morgan Valley Road and Cache Creek, destroying 300 "
            "structures including 189 homes and 8 commercial buildings before "
            "containment on Aug 26. Arsonist Damin Pashilk, a construction worker "
            "from Clearlake, was arrested and convicted on 17 counts of arson. The "
            "fire exposed the vulnerability of the Lower Lake commercial core, which "
            "sits directly adjacent to wildland fuels. The community had barely "
            "recovered from the Valley Fire's impacts (2015) when the Clayton Fire "
            "struck -- the compounding psychological and economic trauma has been "
            "well documented."
        ),
        "key_features": [
            "Junction of Highway 29 and Highway 53 -- critical intersection for Lake County traffic",
            "Cache Creek at Clear Lake outlet -- drainage corridor and fire path",
            "Anderson Marsh State Historic Park (1,065 acres) -- grassland/oak/tule between Lower Lake and Clearlake",
            "Morgan Valley Road -- rural road south toward Napa County, fire corridor",
            "Volcanic hills south and west -- chaparral terrain rising above the community",
            "Lower Lake historic commercial district -- small-town core rebuilt after Clayton Fire",
        ],
        "elevation_range_ft": [1320, 1500],
        "wui_exposure": "high",
        "historical_fires": [
            {
                "name": "Clayton Fire",
                "year": 2016,
                "acres": 3929,
                "details": (
                    "Arson (Damin Pashilk convicted on 17 arson counts). Ignited 6 PM "
                    "Aug 13 near Lower Lake. Burned aggressively north. 300 structures "
                    "destroyed: 189 homes, 8 commercial buildings, 102 outbuildings. "
                    "Town's commercial district significantly damaged. Contained Aug 26."
                ),
            },
            {
                "name": "Valley Fire",
                "year": 2015,
                "acres": 76067,
                "details": (
                    "Burned SW of Lower Lake. While the town was not in the direct path, "
                    "evacuation impacts, smoke, and economic disruption were severe. "
                    "Community was still recovering from Valley Fire when Clayton Fire struck."
                ),
            },
            {
                "name": "Cache Fire",
                "year": 2021,
                "acres": 80,
                "details": (
                    "Burned near Lower Lake/Clearlake boundary. Destroyed homes in mobile "
                    "home parks along Cache Creek. Evacuations included Lower Lake residents."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 29 south toward Middletown/Calistoga",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Two-lane highway winding south through hilly terrain. Passes through "
                    "areas that have burned repeatedly. Limited shoulders."
                ),
                "risk": "Clayton Fire crossed paths near this route. Fire from south/west can block access.",
            },
            {
                "route": "Highway 29 north toward Lakeport",
                "direction": "N",
                "lanes": 2,
                "bottleneck": "Two-lane road along western shore of Clear Lake. Relatively open terrain.",
                "risk": "Generally safer route but long drive to reach US-101 via Lakeport/Ukiah.",
            },
            {
                "route": "Highway 53 north toward Clearlake/Hwy 20",
                "direction": "N/NE",
                "lanes": 4,
                "bottleneck": (
                    "4-lane expressway to Clearlake. Best capacity route but leads to "
                    "another fire-vulnerable community, not out of the fire zone."
                ),
                "risk": "Fire can block both ends of this route during large events.",
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Diablo winds funnel through the Cache Creek drainage and surrounding "
                "hills. Afternoon thermal winds drive upslope fire runs on southern "
                "hills. Clayton Fire demonstrated rapid spread from south to north "
                "through the community."
            ),
            "critical_corridors": [
                "Cache Creek corridor -- channels fire and wind between Lower Lake and Clearlake",
                "Morgan Valley Road south -- fire corridor through chaparral toward Napa County",
                "Hills south of town -- steep chaparral terrain above community",
            ],
            "rate_of_spread_potential": (
                "High. Grass and chaparral fuels allow 50-100 chains/hour. Clayton Fire "
                "burned through town in a single evening. Proximity of structures to "
                "wildland fuels means fire can reach buildings within minutes of ignition."
            ),
            "spotting_distance": (
                "0.25-0.75 mile. Chaparral fires generate significant ember showers. "
                "Wind-driven embers cross Cache Creek easily."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Small community water system. Limited fire suppression capacity. "
                "No redundant supply during high-demand fire events."
            ),
            "power": (
                "PG&E lines through fire-prone terrain. Frequent PSPS shutoffs. "
                "Arson (Clayton Fire) highlighted vulnerability independent of utility "
                "ignition -- fires can start from any source."
            ),
            "communications": (
                "Limited cell service. Lake County emergency notification system covers "
                "the area but opt-in registration limits reach."
            ),
            "medical": (
                "No medical facilities in Lower Lake. Nearest hospital: Adventist Health "
                "Clear Lake in Clearlake (~10 min) or Sutter Lakeside in Lakeport (~25 min)."
            ),
        },
        "demographics_risk_factors": {
            "population": 1276,
            "seasonal_variation": "Modest increase from summer lake tourism.",
            "elderly_percentage": "est. 20-24% (consistent with Lake County demographics)",
            "mobile_homes": (
                "Significant mobile home presence. Cache Creek area mobile home parks "
                "bridge Lower Lake and Clearlake -- high fire vulnerability."
            ),
            "special_needs_facilities": (
                "Minimal. Lower Lake Elementary School serves as community gathering point. "
                "Anderson Marsh area has scattered rural elderly residents."
            ),
        },
    },

    # =========================================================================
    # NAPA/SONOMA WINE COUNTRY -- Glass Fire / Tubbs Fire / Nuns Fire zone
    # =========================================================================

    "angwin_ca": {
        "center": [38.5757, -122.4499],
        "terrain_notes": (
            "Isolated mountaintop community (pop. ~3,200 permanent residents per "
            "2020 census, plus ~900 Pacific Union College students not captured in "
            "census, total ~4,100) on the western slopes of Howell Mountain at "
            "~1,752 ft elevation. Angwin is home to Pacific Union College (PUC), a "
            "Seventh-day Adventist liberal arts institution founded 1882 (relocated "
            "to Angwin 1909). The community's defining vulnerability is its extreme "
            "isolation: a single narrow, winding road (Deer Park Road / Howell "
            "Mountain Road) traverses Howell Mountain from Napa Valley up to Angwin. "
            "A 2021 Napa County Grand Jury report identified Angwin's evacuation "
            "vulnerability as a critical concern -- the community has essentially one "
            "way in and one way out. A secondary 'back gate road' known to local "
            "firefighters has been listed by CAL FIRE as an emergency evacuation "
            "route, and community efforts have pushed to reopen and maintain it. "
            "The Glass Fire (Sep 2020) forced mandatory evacuation of all Angwin "
            "residents; the fire burned to the community's edge, destroying homes "
            "along Deer Park Road and producing 'the most active fire behavior' "
            "observed by firefighters during the event. The LNU Lightning Complex "
            "(Aug 2020) had already forced evacuation just weeks earlier. The "
            "surrounding forest is dense mixed-conifer and oak woodland with "
            "significant fuel loads. PUC's 1,800-acre forest preserve surrounds "
            "much of the campus. CAL FIRE awarded a $5M grant to Napa Firewise "
            "in 2022 for forest restoration and fuel reduction around Angwin."
        ),
        "key_features": [
            "Pacific Union College (PUC) -- 1,800-acre campus and forest, Adventist institution since 1909",
            "Howell Mountain -- volcanic plateau, one of Napa's premier wine appellations",
            "Deer Park Road -- THE single primary evacuation route down to St. Helena/Napa Valley",
            "Back gate road (CAL FIRE emergency route) -- secondary escape route being maintained/improved",
            "PUC Forest Preserve (1,800 acres) -- dense mixed-conifer/oak surrounding campus",
            "Howell Mountain Mutual Water Company -- nonprofit water utility, limited capacity",
            "Angwin Airport (private) -- small strip on PUC campus, not viable for mass evacuation",
            "Las Posadas State Forest -- adjacent managed forestland",
        ],
        "elevation_range_ft": [1600, 2000],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Glass Fire",
                "year": 2020,
                "acres": 67484,
                "details": (
                    "Ignited Sep 27 in the Mayacamas Mountains. Burned through Napa Valley "
                    "and Sonoma County. 1,555 structures destroyed (308 homes, 343 commercial "
                    "in Napa; 334 homes in Sonoma). Mandatory evacuation of all Angwin residents. "
                    "Fire burned to the community edge, destroying homes along Deer Park Road. "
                    "Angwin experienced the 'most active fire behavior' during this event. "
                    "PUC campus ultimately survived intact. No fatalities."
                ),
            },
            {
                "name": "LNU Lightning Complex",
                "year": 2020,
                "acres": 363220,
                "details": (
                    "Aug 2020, sparked by lightning storms. 363,220 acres across Napa, "
                    "Sonoma, Lake, Solano, Yolo counties. Mandatory evacuation of Angwin "
                    "beginning Aug 19 -- just 5 weeks before the Glass Fire forced a second "
                    "evacuation. Hennessey Fire component burned closest to Angwin."
                ),
            },
            {
                "name": "Deer Park Fire",
                "year": 2008,
                "acres": 1200,
                "details": (
                    "Burned near the community, threatening PUC campus. Relatively small "
                    "but demonstrated the vulnerability of the single-access-road community."
                ),
            },
            {
                "name": "Tubbs Fire",
                "year": 2017,
                "acres": 36810,
                "details": (
                    "Originated near Calistoga, NW of Angwin. While fire primarily tracked "
                    "toward Santa Rosa, the event prompted evacuations in Angwin and "
                    "demonstrated the NE Diablo wind threat to Howell Mountain."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Deer Park Road / Howell Mountain Road down to St. Helena",
                "direction": "W/SW",
                "lanes": 2,
                "bottleneck": (
                    "THE SINGLE PRIMARY ROUTE. Narrow, winding mountain road descending "
                    "~1,400 ft from Angwin to the Napa Valley floor at St. Helena. "
                    "Multiple tight switchbacks, steep grades, no shoulders. During Glass "
                    "Fire, this road was directly threatened by active fire."
                ),
                "risk": (
                    "EXTREME. Any fire between Angwin and the valley floor cuts off the "
                    "primary evacuation route. 3,000-4,000 people funneled onto a single "
                    "narrow mountain road. Napa County Grand Jury (2021) identified this "
                    "as a critical life-safety concern."
                ),
            },
            {
                "route": "Back gate road (CAL FIRE emergency route) to Pope Valley",
                "direction": "E",
                "lanes": 1,
                "bottleneck": (
                    "Unpaved/poorly maintained road through forest to Pope Valley and "
                    "eventually to Berryessa. CAL FIRE lists as emergency evacuation "
                    "route. Community advocacy has improved maintenance."
                ),
                "risk": (
                    "Limited capacity -- essentially single lane. Rough surface. Passes "
                    "through dense forest. Better than no alternative but not suitable "
                    "for mass evacuation."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Diablo winds accelerate over the Howell Mountain plateau. NE winds "
                "push fire upslope from Pope Valley (east) toward Angwin. Glass Fire "
                "approached from the south/southwest through the Mayacamas. LNU Complex "
                "approached from the east. The mountaintop position means fire can "
                "approach from multiple directions."
            ),
            "critical_corridors": [
                "Deer Park Road drainage -- fire can run uphill from Napa Valley directly into community",
                "Pope Valley (east) -- NE winds push fire upslope to Howell Mountain",
                "Conn Valley (south) -- drainage connecting to main Napa Valley, Glass Fire approach vector",
                "PUC Forest (surrounding) -- 1,800 acres of continuous fuel surrounding campus",
            ],
            "rate_of_spread_potential": (
                "High to extreme. Dense forest and steep slopes create 50-200 chain/hour "
                "upslope runs. Glass Fire demonstrated rapid spread through this terrain. "
                "Crown fire potential in continuous conifer canopy."
            ),
            "spotting_distance": (
                "0.5-1.5 miles. Glass Fire demonstrated significant spotting across "
                "the Napa Valley -- embers carried from the Mayacamas to start new fires. "
                "Howell Mountain's exposed position catches lofted embers."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Howell Mountain Mutual Water Company (HMMWC) -- nonprofit mutual water "
                "company serving the community. Limited storage capacity on a mountaintop "
                "location. Water pressure may be inadequate during simultaneous multi-"
                "structure fire. System relies on pumping from lower elevations."
            ),
            "power": (
                "PG&E lines through dense forest. Frequent PSPS shutoffs -- Angwin is "
                "in a high-wind zone and has experienced multi-day de-energizations. "
                "PUC has backup generators for campus but surrounding residences do not."
            ),
            "communications": (
                "Limited cell coverage due to mountaintop location and surrounding "
                "forest. Napa County OES alert system covers the area. PUC campus "
                "has internal communication but gaps exist in surrounding community."
            ),
            "medical": (
                "Adventist Health St. Helena Hospital is located on Deer Park Road "
                "between Angwin and St. Helena -- directly in the fire path. During "
                "Glass Fire, hospital was evacuated. Loss of the hospital during a "
                "fire event eliminates the closest medical facility."
            ),
        },
        "demographics_risk_factors": {
            "population": 3200,
            "seasonal_variation": (
                "PUC academic calendar adds ~900 students Aug-May, many from out of "
                "state/country with no experience of wildfire evacuation. Summer "
                "population drops but tourists increase in wine country."
            ),
            "elderly_percentage": "est. 18-22% (mixed college and retirement community)",
            "mobile_homes": "Minimal. Primarily single-family homes and college housing.",
            "special_needs_facilities": (
                "Pacific Union College -- 900+ students requiring organized evacuation. "
                "Adventist Health St. Helena Hospital (on evacuation route) -- patient "
                "evacuation required during Glass Fire. Retirement-age residents in "
                "surrounding rural area."
            ),
        },
    },

    "calistoga_ca": {
        "center": [38.5788, -122.5797],
        "terrain_notes": (
            "Small city (pop. 5,228 per 2020 census) at the northern terminus of "
            "the Napa Valley, nestled in a narrow valley bounded by the Mayacamas "
            "Mountains to the west and the Palisades/Vaca Mountains to the east. "
            "Elevation ~348 ft on the valley floor, rising steeply on all three "
            "northern and eastern sides. Calistoga sits at the very head of the "
            "Napa Valley -- the valley narrows dramatically here, creating a "
            "topographic funnel for wind-driven fire. The Tubbs Fire (Oct 8, 2017) "
            "ignited near Tubbs Lane on the northern outskirts of Calistoga, then "
            "was driven 12 miles in 3 hours by extreme Diablo winds (60-65+ mph "
            "gusts) through the Mark West Springs corridor to devastate Santa Rosa. "
            "Calistoga itself was fully evacuated -- ~2,000 residents ordered to "
            "leave on Oct 11. The Glass Fire (Sep 27, 2020) again forced mandatory "
            "evacuation of the entire city on Sep 28 as fire approached from the "
            "east through the Mayacamas. Fire burned to within a mile of the city "
            "limits. The Pickett Fire (Aug 2025) was a more recent near-miss. "
            "Calistoga's predicament is that it sits at the convergence point of "
            "multiple fire corridors -- fires from the north (Tubbs), east "
            "(Glass), and south (any Napa Valley fire) all funnel toward this "
            "bottleneck. The city is also a dead end: Highway 29 terminates here "
            "(continuing north only as the narrow, winding Highway 29/128 over "
            "Mt. St. Helena), and the Silverado Trail dead-ends just south of town."
        ),
        "key_features": [
            "Northern terminus of Napa Valley -- valley narrows to <1 mile, topographic funnel",
            "Highway 29 -- primary road south through Napa Valley; becomes mountain road north",
            "Silverado Trail -- secondary N-S route along eastern valley wall, terminates near Calistoga",
            "Highway 128 -- branches NW toward Geyserville/US-101 over Mt. St. Helena",
            "Palisades -- dramatic volcanic cliffs east of town, chaparral-covered",
            "Mt. St. Helena (4,342 ft) -- dominant peak NW of town, Robert Louis Stevenson State Park",
            "Tubbs Lane -- rural area N of town where Tubbs Fire originated (2017)",
            "Hot springs / geothermal -- town founded on geothermal resources, tourist draw",
            "Extensive wine country development -- wineries, tasting rooms, resorts throughout WUI",
        ],
        "elevation_range_ft": [300, 500],
        "wui_exposure": "high",
        "historical_fires": [
            {
                "name": "Tubbs Fire",
                "year": 2017,
                "acres": 36810,
                "details": (
                    "Ignited Oct 8 near Tubbs Lane, north of Calistoga, from a private "
                    "electrical system. Driven by extreme Diablo winds (60-65+ mph), fire "
                    "raced SW through the Mark West Springs corridor, destroying 5,643 "
                    "structures and killing 22 people -- mostly in Santa Rosa's Coffey "
                    "Park and Fountaingrove neighborhoods. Calistoga fully evacuated Oct 11. "
                    "At the time, most destructive CA wildfire in history."
                ),
            },
            {
                "name": "Glass Fire",
                "year": 2020,
                "acres": 67484,
                "details": (
                    "Ignited Sep 27 in the Mayacamas Mountains. Mandatory evacuation of "
                    "entire city of Calistoga issued 6 PM Sep 28. Fire burned to within "
                    "~1 mile of city limits. 1,555 structures destroyed across the fire "
                    "footprint (Napa and Sonoma counties). Calistoga evacuated for the "
                    "second time in three years. No fatalities."
                ),
            },
            {
                "name": "Pickett Fire",
                "year": 2025,
                "acres": 80,
                "details": (
                    "Aug 21, 2025. Small fire near Calistoga. Quickly contained but "
                    "triggered evacuation warnings. Demonstrated the ongoing fire threat "
                    "to the community."
                ),
            },
            {
                "name": "Hanly Fire",
                "year": 1964,
                "acres": 52700,
                "details": (
                    "Historic fire that took nearly the identical path as the 2017 Tubbs "
                    "Fire -- from Calistoga area through Mark West Springs to Santa Rosa. "
                    "Demonstrates the recurrence of this specific fire corridor."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 29 south through Napa Valley",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Two-lane highway (widening to 4 lanes south of St. Helena) running "
                    "the length of Napa Valley. Primary evacuation route for Calistoga. "
                    "During Tubbs Fire, gridlocked as entire northern Napa evacuated."
                ),
                "risk": (
                    "Fire approaching from the east (Mayacamas) or west can cut Hwy 29 "
                    "at multiple points. Glass Fire threatened highway north of St. Helena. "
                    "Wine country traffic during harvest season (Sep-Oct, peak fire season) "
                    "adds enormous congestion."
                ),
            },
            {
                "route": "Silverado Trail south",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Two-lane road along eastern valley wall. Passes through dense WUI "
                    "with wineries and rural homes on both sides. Ends/begins just south "
                    "of Calistoga."
                ),
                "risk": (
                    "Highly vulnerable to fire from the Mayacamas Mountains to the east. "
                    "Glass Fire burned across/near the Silverado Trail. Not independent "
                    "from Hwy 29 -- both routes converge south of town."
                ),
            },
            {
                "route": "Highway 128 northwest toward Geyserville/US-101",
                "direction": "NW",
                "lanes": 2,
                "bottleneck": (
                    "Narrow, winding mountain road over the shoulder of Mt. St. Helena. "
                    "Steep grades, switchbacks, no shoulders. Eventually reaches Alexander "
                    "Valley and US-101 near Geyserville (~20 miles)."
                ),
                "risk": (
                    "Passes through heavy chaparral and forest. Extremely vulnerable to "
                    "fire closure. Not viable for mass evacuation but provides an escape "
                    "route when Napa Valley routes are blocked."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Diablo winds are the primary fire weather threat. NE offshore winds "
                "accelerate over the Vaca Mountains and Palisades, funneling through "
                "the narrowing Napa Valley and into Calistoga. The 2017 Tubbs Fire "
                "demonstrated extreme Diablo wind-driven fire propagation -- winds of "
                "60-65+ mph sustained for hours. The valley's N-S orientation aligns "
                "with the NE-to-SW Diablo flow, creating a natural venturi effect at "
                "Calistoga where the valley narrows."
            ),
            "critical_corridors": [
                "Mark West Springs corridor -- Tubbs Fire path, NE-to-SW from Calistoga to Santa Rosa",
                "Mayacamas west slopes -- Glass Fire approach vector from east into valley",
                "Mt. St. Helena / Robert Louis Stevenson SP -- fire on this peak spreads S toward town",
                "Palisades -- steep volcanic terrain east of town, fire descends rapidly to valley floor",
                "Bennett Lane / Tubbs Lane -- rural area N of town, Tubbs Fire origin zone",
            ],
            "rate_of_spread_potential": (
                "Extreme during Diablo wind events. Tubbs Fire covered 12 miles in 3 "
                "hours (4 mph average, with peak runs much faster). Chaparral on "
                "surrounding slopes burns at 100-200+ chains/hour with wind assistance. "
                "Valley floor vineyards provide some fuel break but embers spot over them."
            ),
            "spotting_distance": (
                "1-3+ miles. Tubbs Fire embers crossed a 6-lane freeway (Hwy 101) and "
                "ignited Coffey Park in Santa Rosa, 12 miles from origin. Glass Fire "
                "demonstrated cross-valley spotting from the Mayacamas into the Napa "
                "Valley -- embers carried across the entire valley width."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "City water system with Kimball Reservoir and groundwater wells. "
                "Adequate for normal operations but fire suppression demand during "
                "WUI fire may exceed capacity, especially for hillside properties."
            ),
            "power": (
                "PG&E PSPS events affect Calistoga regularly. Being at the end of "
                "the valley, power lines traverse fire-prone terrain. PG&E has "
                "undergrounded some lines post-Tubbs Fire. City invested in backup "
                "power for critical facilities."
            ),
            "communications": (
                "Cell coverage adequate in town but limited in surrounding hills. "
                "Napa County OES alert system with Nixle/Everbridge notifications. "
                "PG&E PSPS can knock out cell towers lacking backup power."
            ),
            "medical": (
                "No hospital in Calistoga. Adventist Health St. Helena (~10 mi south) "
                "is nearest -- but this hospital was evacuated during Glass Fire. "
                "Queen of the Valley Medical Center in Napa (~30 mi south) is the "
                "fallback. Isolation at head of valley means extended response times."
            ),
        },
        "demographics_risk_factors": {
            "population": 5228,
            "seasonal_variation": (
                "SIGNIFICANT. Peak wine country tourism season (Sep-Oct) coincides "
                "exactly with peak fire season. Thousands of tourists in wineries, "
                "resorts, and vacation rentals -- unfamiliar with evacuation routes, "
                "roads, or fire behavior. Harvest workers also increase population."
            ),
            "elderly_percentage": "est. 20-24% (wine country retirement destination)",
            "mobile_homes": (
                "Limited within city limits. Some manufactured housing on outskirts. "
                "Calistoga has more resort and second-home properties than mobile homes."
            ),
            "special_needs_facilities": (
                "Calistoga Joint Unified School District serves as evacuation gathering "
                "point. Several resort/spa properties house tourists with potential "
                "mobility limitations. Calistoga is a popular retirement destination."
            ),
        },
    },

    "kenwood_ca": {
        "center": [38.4039, -122.5519],
        "terrain_notes": (
            "Tiny unincorporated community (pop. 852 per 2020 census) in the upper "
            "Sonoma Valley, east of Sonoma Creek at the base of the Mayacamas "
            "Mountains. Elevation ~409 ft on the valley floor, with steep mountain "
            "terrain rising immediately to the east. Kenwood lies in the 'Valley of "
            "the Moon' -- a narrow north-south valley flanked by Sonoma Mountain "
            "(2,295 ft) to the west and the Mayacamas (2,700 ft crest) to the east. "
            "The Nuns Fire (Oct 8, 2017) devastated Kenwood: originating in the "
            "Mayacamas near Nuns Canyon, the fire burned 56,556 acres, destroying "
            "1,355 structures including 639 homes. In Kenwood specifically, 139 "
            "homes were destroyed. The fire raced down the Mayacamas' western slopes "
            "driven by extreme Diablo winds, overrunning neighborhoods before "
            "residents could evacuate. Over 25% of the land in Sonoma Valley burned. "
            "The KLD Associates SAFE (Sonoma Area Fire Evacuation) Study (2025) "
            "modeled evacuation from Kenwood and found devastating results: only two "
            "N-S routes (Highway 12 and Arnold Drive) serve the entire valley, with "
            "almost no east-west escape over the flanking mountains. The study "
            "projected 4-9 hours of gridlock during full-valley evacuation, with "
            "speeds dropping to 1-2 mph. Kenwood's location at the narrow upper end "
            "of the valley makes it among the most vulnerable."
        ),
        "key_features": [
            "Highway 12 -- primary N-S route through Sonoma Valley, 2 lanes through Kenwood",
            "Mayacamas Mountains (east) -- steep chaparral/oak slopes rising 2,000+ ft above valley",
            "Sonoma Mountain (west) -- 2,295 ft peak forming western valley wall",
            "Sonoma Creek -- runs N-S through the valley, riparian corridor",
            "Warm Springs Road -- connects Kenwood to Bennett Valley, secondary route",
            "Numerous wineries -- Kenwood Vineyards, Chateau St. Jean, Kunde Estate on WUI edge",
            "Sugarloaf Ridge State Park -- 4,020 acres of chaparral/oak woodland NE of Kenwood",
            "Adobe Canyon Road -- dead-end road into Sugarloaf Ridge, trapped residents in 2017",
        ],
        "elevation_range_ft": [380, 500],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Nuns Fire",
                "year": 2017,
                "acres": 56556,
                "details": (
                    "Ignited ~10 PM Oct 8 by power equipment contacting a toppled alder "
                    "tree near Nuns Canyon. Driven by extreme Diablo winds. 1,355 structures "
                    "destroyed including 639 homes, 32 commercial, 684 outbuildings. "
                    "In Kenwood: 139 homes destroyed. 2 fatalities. Over 25% of Sonoma "
                    "Valley burned. Fire merged with Norrbom and Adobe fires. 6th most "
                    "destructive fire in CA history at the time."
                ),
            },
            {
                "name": "Glass Fire",
                "year": 2020,
                "acres": 67484,
                "details": (
                    "Originated in the Mayacamas Sep 27. Burned into upper Sonoma Valley. "
                    "Kenwood evacuated. Fire destroyed structures along the Mayacamas "
                    "foothills. Community experienced second major fire threat in 3 years."
                ),
            },
            {
                "name": "Tubbs Fire (peripheral)",
                "year": 2017,
                "acres": 36810,
                "details": (
                    "Simultaneous with Nuns Fire. While Tubbs primarily tracked toward "
                    "Santa Rosa, the combined smoke and evacuation demands affected Kenwood. "
                    "Multiple fires burning simultaneously overwhelmed resources."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 12 south toward Sonoma/Hwy 121",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Two-lane highway through the narrow Sonoma Valley. SAFE Study (2025) "
                    "projected 4-9 hours of gridlock during full-valley evacuation. "
                    "Merges with all Glen Ellen, Boyes Hot Springs, and Sonoma traffic."
                ),
                "risk": (
                    "Fire from Mayacamas (east) or Sonoma Mountain (west) can cross "
                    "Hwy 12 at multiple points. During Nuns Fire, Hwy 12 was closed "
                    "east of Kenwood. Essentially a 2-lane bottleneck for entire valley."
                ),
            },
            {
                "route": "Highway 12 north toward Santa Rosa",
                "direction": "N",
                "lanes": 2,
                "bottleneck": (
                    "Two-lane road north through narrow valley gap to Santa Rosa. "
                    "Passes through burned areas from 2017 fires."
                ),
                "risk": (
                    "Fire from the Mayacamas crosses this route easily. During Nuns Fire, "
                    "road was impassable north of Kenwood. Santa Rosa may also be burning "
                    "(as in 2017 when Tubbs Fire hit simultaneously)."
                ),
            },
            {
                "route": "Warm Springs Road west to Bennett Valley / Sonoma Mountain Road",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "Narrow rural road climbing over Sonoma Mountain to Bennett Valley. "
                    "Winding, steep grades, no shoulders. Single-lane in places."
                ),
                "risk": (
                    "Crosses through fire-prone grassland and oak woodland on Sonoma "
                    "Mountain. Was closed during Nuns Fire. Not viable for mass evacuation."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Diablo winds dominate fire weather. NE offshore winds accelerate over "
                "the Mayacamas crest and descend into Sonoma Valley at 30-65 mph. "
                "Valley orientation (NW-SE) aligns with Diablo flow direction, creating "
                "a wind tunnel effect. Nuns Fire demonstrated extreme downslope-driven "
                "fire propagation from the Mayacamas directly into Kenwood."
            ),
            "critical_corridors": [
                "Mayacamas western slopes -- steep chaparral, fire descends directly into town",
                "Nuns Canyon / Adobe Canyon -- drainages channeling fire from the Mayacamas",
                "Sonoma Creek valley -- N-S wind corridor amplifying Diablo flow",
                "Sugarloaf Ridge -- chaparral-covered terrain NE of Kenwood, fire reservoir",
            ],
            "rate_of_spread_potential": (
                "Extreme during Diablo wind events. Nuns Fire spread downslope through "
                "chaparral and oak at 100-200+ chains/hour with wind. Valley floor "
                "vineyards provide moderate fuel break but embers spot across them. "
                "Grass on hillsides cures by June and remains explosive until winter rains."
            ),
            "spotting_distance": (
                "0.5-2 miles. Nuns Fire embers crossed Sonoma Valley floor and ignited "
                "structures on both sides of the valley. Wind-driven embers from the "
                "Mayacamas reached the western side of the valley during extreme events."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Small community water system and private wells. No fire hydrant system "
                "outside the immediate commercial area. Firefighters rely on water tenders "
                "and drafting from Sonoma Creek during wildfire events."
            ),
            "power": (
                "PG&E distribution through fire-prone terrain. PSPS events affect the "
                "area regularly. The Nuns Fire was caused by power equipment -- the "
                "intersection of electrical infrastructure and vegetation is a persistent "
                "ignition risk."
            ),
            "communications": (
                "Limited cell coverage in the narrow valley. Sonoma County SoCo Alert "
                "system provides emergency notifications. Coverage gaps in canyon areas."
            ),
            "medical": (
                "No medical facilities. Nearest hospital: Kaiser Permanente or Sutter "
                "Santa Rosa (~15 min north on Hwy 12 if passable). During fire, access "
                "to hospitals may be cut off entirely."
            ),
        },
        "demographics_risk_factors": {
            "population": 852,
            "seasonal_variation": (
                "Wine country tourism peaks Sep-Oct (harvest season = fire season). "
                "Wineries along Hwy 12 draw thousands of visitors daily. Tourist "
                "population may exceed resident population on peak weekends."
            ),
            "elderly_percentage": "est. 22-28% (affluent wine country, many retirees)",
            "mobile_homes": "Minimal. Primarily single-family homes and winery estates.",
            "special_needs_facilities": (
                "None in Kenwood. Scattered rural elderly residents with limited mobility. "
                "Winery workers (many seasonal/immigrant labor) may face language barriers "
                "in evacuation communication."
            ),
        },
    },

    "glen_ellen_ca": {
        "center": [38.3641, -122.5241],
        "terrain_notes": (
            "Small unincorporated community (pop. ~784, estimated from 2010-2020 "
            "census trend) in Sonoma Valley, straddling Sonoma Creek along Arnold "
            "Drive and Highway 12. Elevation ~253 ft on the valley floor. Glen Ellen "
            "is Jack London's 'Valley of the Moon' -- the famous author lived and "
            "wrote here, and Jack London State Historic Park occupies 1,400 acres of "
            "the hillside above town. The Nuns Fire (Oct 8, 2017) devastated Glen "
            "Ellen more than any other Sonoma Valley community: 237 homes destroyed "
            "in the Glen Ellen area alone (compared to 139 in Kenwood). Fire came "
            "roaring over the Mayacamas from Napa Valley in the early morning hours "
            "of Oct 8-9, burning through neighborhoods along Warm Springs Road, "
            "Trinity Road, and homes south of Arnold Drive. The nearby Bouverie "
            "Preserve lost 7 buildings. The Nuns Fire ultimately destroyed 639 homes "
            "and killed 2 people across the entire Sonoma Valley footprint. The 2025 "
            "KLD SAFE Study found that Glen Ellen residents face up to 9 HOURS of "
            "evacuation congestion during a full-valley event -- the worst in the "
            "valley. Arnold Drive evacuation time: 171 minutes under current "
            "conditions. The community's position in the mid-valley, where the "
            "valley narrows between Sonoma Mountain and the Mayacamas, creates a "
            "pinch point for both fire and evacuation."
        ),
        "key_features": [
            "Arnold Drive -- 2-lane road through Glen Ellen, parallel to Hwy 12, key evacuation route",
            "Highway 12 -- primary N-S route through Sonoma Valley, 2 lanes here",
            "Jack London State Historic Park (1,400 acres) -- hillside above town, oak/chaparral",
            "Sonoma Mountain (west) -- steep eastern face above Glen Ellen",
            "Mayacamas Mountains (east) -- source of Nuns Fire, steep western slopes",
            "Sonoma Creek -- runs through town, riparian corridor",
            "Warm Springs Road -- connects to Kenwood, heavily impacted in Nuns Fire",
            "Trinity Road -- narrow mountain road over Mayacamas to Napa, dead-end risk",
            "Bouverie Preserve (242 acres) -- Audubon preserve, burned in Nuns Fire",
            "Sonoma Valley Regional Park (202 acres) -- burned in Nuns Fire",
        ],
        "elevation_range_ft": [200, 400],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Nuns Fire",
                "year": 2017,
                "acres": 56556,
                "details": (
                    "Ignited ~10 PM Oct 8. Fire descended from the Mayacamas into Glen "
                    "Ellen in early morning hours Oct 9. 237 homes destroyed in Glen "
                    "Ellen -- the highest single-community loss in Sonoma Valley. 1,355 "
                    "total structures across entire fire footprint. 2 fatalities. "
                    "Neighborhoods on Warm Springs Road, south of Arnold Drive, and along "
                    "Trinity Road hit hardest. Bouverie Preserve lost 7 buildings. "
                    "Jack London SHP partially burned but historic buildings survived."
                ),
            },
            {
                "name": "Glass Fire",
                "year": 2020,
                "acres": 67484,
                "details": (
                    "Fire again approached from the Mayacamas. Glen Ellen evacuated. "
                    "Some structures destroyed along the eastern foothills. Community "
                    "experienced second major fire in 3 years."
                ),
            },
            {
                "name": "Nuns Fire area re-burn potential",
                "year": 2017,
                "acres": 56556,
                "details": (
                    "Post-Nuns Fire vegetation recovery has created a new fuel matrix: "
                    "fast-growing brush and grass have colonized the burned hillsides, "
                    "creating potentially more homogeneous and flammable fuel than the "
                    "pre-fire mosaic. Re-burn in this terrain could be faster than 2017."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Arnold Drive south toward Sonoma/Hwy 121",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Two-lane rural road through the valley. SAFE Study: 171-minute "
                    "evacuation time under current conditions. Glen Ellen residents face "
                    "up to 9 hours of congestion during full-valley evacuation. Road "
                    "passes through other communities also evacuating."
                ),
                "risk": (
                    "Fire can cross Arnold Drive from either Sonoma Mountain (W) or "
                    "Mayacamas foothills (E). Road runs through narrow valley with "
                    "fuel on both sides. During Nuns Fire, portions were impassable."
                ),
            },
            {
                "route": "Highway 12 north toward Santa Rosa",
                "direction": "N",
                "lanes": 2,
                "bottleneck": (
                    "Two-lane highway through narrow valley gap. Merges with Kenwood "
                    "evacuation traffic. Passes through area heavily burned in 2017."
                ),
                "risk": (
                    "Fire from the Mayacamas can cut this route. During Nuns Fire, "
                    "Hwy 12 was closed in multiple locations. Santa Rosa may also "
                    "be under fire threat."
                ),
            },
            {
                "route": "Trinity Road east over Mayacamas toward Napa",
                "direction": "E",
                "lanes": 2,
                "bottleneck": (
                    "Narrow, extremely winding mountain road climbing over the Mayacamas "
                    "to reach the Napa Valley. Steep grades, blind corners, no shoulders. "
                    "Single-lane in sections."
                ),
                "risk": (
                    "EXTREMELY DANGEROUS during fire. Passes directly through the terrain "
                    "that burned in both Nuns Fire and Glass Fire. Not viable for mass "
                    "evacuation but could be a last-resort escape if valley routes are "
                    "blocked -- assuming fire is not actively burning on the mountain."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Diablo winds accelerate over the Mayacamas and descend into Sonoma "
                "Valley. Glen Ellen's mid-valley position receives channeled flow from "
                "both the NE (Mayacamas drainages) and N (valley alignment). The narrow "
                "valley creates a venturi effect amplifying wind speed. Nuns Fire "
                "demonstrated catastrophic downslope fire driven by 40-60+ mph Diablo winds."
            ),
            "critical_corridors": [
                "Mayacamas west-facing drainages -- multiple canyons funnel fire directly into Glen Ellen",
                "Sonoma Mountain east face -- fire runs downslope toward valley floor and town",
                "Sonoma Creek corridor -- channels wind and fire N-S through valley",
                "Moon Mountain drainages -- steep terrain E of Glen Ellen, heavy WUI",
                "Jack London SHP slopes -- 1,400 acres of fuel above town on Sonoma Mountain",
            ],
            "rate_of_spread_potential": (
                "Extreme. Nuns Fire demonstrated >100 chains/hour through chaparral on "
                "steep slopes. Valley floor grass reaches 50-100 chains/hour when cured. "
                "The 2017 fires burned 30,000+ acres (>25% of Sonoma Valley) in a single "
                "night. Structure-to-structure fire spread documented in Glen Ellen "
                "neighborhoods where homes were within 30 ft of each other."
            ),
            "spotting_distance": (
                "0.5-2 miles. Nuns Fire embers spotted across the valley floor from the "
                "Mayacamas to Sonoma Mountain slopes. Burning debris carried by extreme "
                "winds ignited homes far from the wildland fire front."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Valley of the Moon Water District serves parts of the area. Many "
                "residents on private wells with electric pumps. No pressurized fire "
                "hydrant system in rural areas. Firefighters relied on water tenders "
                "and creek drafting during Nuns Fire."
            ),
            "power": (
                "PG&E lines through dense oak woodland and along ridgelines. Power "
                "equipment contact with downed tree caused the Nuns Fire. PSPS events "
                "are frequent. Many older homes lack backup power."
            ),
            "communications": (
                "Limited cell coverage in the narrow valley and surrounding hills. "
                "SoCo Alert system provides emergency notifications. Some canyon-area "
                "residents receive delayed or no alerts."
            ),
            "medical": (
                "No medical facilities. Nearest hospitals in Santa Rosa (~15-20 min "
                "north) or Sonoma (~15 min south). Both routes may be compromised "
                "during fire. Glen Ellen has a volunteer fire station."
            ),
        },
        "demographics_risk_factors": {
            "population": 784,
            "seasonal_variation": (
                "Wine country tourism is significant. Jack London State Historic Park "
                "draws visitors. Numerous B&Bs, vacation rentals, and winery tasting "
                "rooms add transient population. Harvest season (Sep-Oct) peaks coincide "
                "with fire season."
            ),
            "elderly_percentage": "est. 25-30% (rural, affluent wine country community)",
            "mobile_homes": "Minimal. Primarily single-family homes, some ranch properties.",
            "special_needs_facilities": (
                "None. Rural community with scattered elderly residents. Some winery "
                "workers in seasonal housing. Dunbar Elementary School serves as community "
                "gathering point."
            ),
        },
    },

    # =========================================================================
    # MENDOCINO / NORTH COAST -- Mendocino Complex / Redwood Complex zone
    # =========================================================================

    "ukiah_outskirts_ca": {
        "center": [39.1502, -123.2078],
        "terrain_notes": (
            "Mendocino County seat (pop. 16,607 per 2020 census) in the upper "
            "Russian River valley at ~627 ft elevation. Ukiah sits in a relatively "
            "broad valley drained by the Russian River, flanked by hills to the east "
            "(rising toward the Mendocino National Forest) and west (toward the "
            "Coast Range). The city itself on the valley floor is at moderate fire "
            "risk, but the outskirts and surrounding WUI communities (Redwood Valley "
            "to the north, Talmage to the east, Hopland to the south) are in Very "
            "High Fire Hazard Severity Zones. The Mendocino Complex (2018) was the "
            "defining fire event: the Ranch Fire burned 8 miles NE of Ukiah while "
            "the River Fire burned 6 miles north of Hopland (south of the Ranch "
            "Fire). The complex ultimately burned 459,123 combined acres -- the "
            "largest wildfire in modern California history at the time. The Ranch "
            "Fire alone burned 410,203 acres. 280 structures destroyed, 37 damaged, "
            "one firefighter killed, $257M+ in damages. The Redwood Complex Fire "
            "(2017) killed 9 people and destroyed 546 structures primarily in "
            "Redwood Valley, just 8 miles north of Ukiah. Highway 101 was closed "
            "south of Willits during the Redwood Fire, isolating communities. "
            "Ukiah's WUI is primarily along the eastern and northern edges where "
            "suburban development pushes into oak woodland and chaparral-covered "
            "hills. The Russian River corridor itself provides limited fuel break "
            "through irrigated agriculture and riparian vegetation."
        ),
        "key_features": [
            "US Highway 101 -- primary N-S corridor, 4-lane freeway through valley",
            "Russian River -- flows S through valley, provides riparian corridor and agricultural buffer",
            "Highway 20 east -- 2-lane road toward Lake County, Potter Valley, fire corridor",
            "Highway 253 east toward Boonville/Anderson Valley -- mountain route",
            "Mendocino National Forest -- vast wildland to the NE, source of large fires",
            "Redwood Valley (8 mi N) -- community devastated by 2017 Redwood Fire",
            "Hopland (14 mi S) -- community threatened by Mendocino Complex River Fire",
            "Eastern hills -- chaparral/oak woodland rising above valley, WUI interface",
            "Ukiah Municipal Airport -- small regional airport on valley floor",
        ],
        "elevation_range_ft": [580, 800],
        "wui_exposure": "high",
        "historical_fires": [
            {
                "name": "Mendocino Complex (Ranch Fire + River Fire)",
                "year": 2018,
                "acres": 459123,
                "details": (
                    "Largest wildfire in modern CA history at the time. Ranch Fire "
                    "(410,203 acres) burned NE of Ukiah; River Fire (48,920 acres) "
                    "burned near Hopland/south Ukiah. Started Jul 27. Caused by a "
                    "hammer spark on a metal fence post. 280 structures destroyed, "
                    "1 firefighter killed, $257M+ damages. Evacuations across Lake, "
                    "Mendocino, Colusa, Glenn counties. Ranch Fire crossed Hwy 20."
                ),
            },
            {
                "name": "Redwood Complex Fire",
                "year": 2017,
                "acres": 36523,
                "details": (
                    "Ignited Oct 8 when tree branches struck a power line near Potter "
                    "Valley. 9 fatalities (deadliest fire in Mendocino County history). "
                    "546 structures destroyed, 387 homes. 7,620 people evacuated for "
                    "up to 5 days. Highway 101 closed south of Willits. Burned primarily "
                    "in Redwood Valley and Potter Valley, 8 miles north of Ukiah."
                ),
            },
            {
                "name": "River Fire (standalone context)",
                "year": 2018,
                "acres": 48920,
                "details": (
                    "Component of Mendocino Complex. Burned near Old River Road south "
                    "of Ukiah/Hopland. Closed Hwy 101 at points. Threatened Hopland "
                    "Rancheria (tribal community). Evacuations for Hopland and south Ukiah."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "US-101 south toward Santa Rosa/San Francisco",
                "direction": "S",
                "lanes": 4,
                "bottleneck": (
                    "4-lane freeway with generally good capacity. However, narrows through "
                    "canyon sections south of Hopland and can be threatened by fire from "
                    "the surrounding hills. River Fire (2018) threatened Hwy 101 corridor."
                ),
                "risk": (
                    "Fire from the eastern hills can reach the highway. During multiple "
                    "events, Hwy 101 has been narrowed or closed near Ukiah/Hopland."
                ),
            },
            {
                "route": "US-101 north toward Willits/Eureka",
                "direction": "N",
                "lanes": 4,
                "bottleneck": (
                    "4-lane freeway north through Russian River valley. Passes through "
                    "Redwood Valley (devastated 2017). Willits bypass completed but "
                    "corridor remains vulnerable to fire closure."
                ),
                "risk": (
                    "Redwood Fire (2017) closed Hwy 101 south of Willits, isolating "
                    "northern communities. Fire from Mendocino National Forest can reach "
                    "the highway corridor."
                ),
            },
            {
                "route": "Highway 20 east toward Lake County/I-5",
                "direction": "E",
                "lanes": 2,
                "bottleneck": (
                    "Two-lane mountain road through Potter Valley and over to Lake County. "
                    "Narrow, winding, remote. Ranch Fire (2018) crossed this highway."
                ),
                "risk": (
                    "Extremely vulnerable to fire closure. Passes through the terrain "
                    "that burned in both Mendocino Complex and Redwood Fire."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Diablo winds affect the region but are moderated by distance from the "
                "Mayacamas crest. Afternoon thermal winds drive upslope fire runs on "
                "eastern hills. During the Mendocino Complex, high heat (100F+), low "
                "humidity, and gusty winds created extreme fire behavior in rugged "
                "terrain. The Russian River valley can channel both N-S winds."
            ),
            "critical_corridors": [
                "Russian River valley -- N-S wind and fire corridor through Ukiah/Redwood Valley",
                "Eastern hills toward Mendocino NF -- vast wildland, source of Ranch Fire",
                "Potter Valley / Hwy 20 corridor -- fire path from NE into valley",
                "Hopland corridor (Hwy 101 south) -- River Fire approach vector",
            ],
            "rate_of_spread_potential": (
                "High in eastern hills (chaparral 30-100 chains/hour). Valley floor "
                "moderate (grass/agriculture 20-50 chains/hour). Mendocino Complex "
                "demonstrated sustained extreme fire behavior for weeks in the "
                "mountainous terrain NE of Ukiah."
            ),
            "spotting_distance": (
                "0.5-1 mile in chaparral. Longer-range spotting (1-2 mi) documented "
                "during extreme Mendocino Complex fire behavior. Burning embers jumped "
                "the Russian River during vegetation fires near Ukiah."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "City of Ukiah water from Russian River and Ranney collectors. Generally "
                "adequate but outlying areas on wells. Redwood Valley community water "
                "system was damaged in 2017 fire."
            ),
            "power": (
                "PG&E distribution through fire-prone terrain. Redwood Fire (2017) "
                "caused by tree-on-powerline. Frequent PSPS shutoffs for eastern "
                "foothill areas. Gas service also disrupted during fires -- Willits "
                "lost gas supply during Redwood Fire."
            ),
            "communications": (
                "Cell coverage adequate on valley floor but degrades in surrounding "
                "hills. Mendocino County OES emergency notifications. During Redwood "
                "Fire, AT&T set up temporary cell tower in Willits after permanent "
                "towers were damaged."
            ),
            "medical": (
                "Adventist Health Ukiah Valley hospital provides local care. Adequate "
                "for normal operations but strained during major evacuations. Howard "
                "Memorial Hospital (Willits) is secondary option to the north. Nearest "
                "Level II trauma center in Santa Rosa (~60 min south)."
            ),
        },
        "demographics_risk_factors": {
            "population": 16607,
            "seasonal_variation": (
                "Moderate tourism, primarily transit to coast. Grape harvest (Sep-Oct) "
                "adds seasonal workers. Hopland has wine tasting tourism."
            ),
            "elderly_percentage": "est. 18-20% (county seat with mixed demographics)",
            "mobile_homes": (
                "Significant manufactured housing in Redwood Valley and rural outskirts. "
                "Many Redwood Fire losses were manufactured homes."
            ),
            "special_needs_facilities": (
                "Multiple assisted living facilities and the Ukiah Senior Center. "
                "Tribal communities (Hopland Rancheria, Big Valley Rancheria) require "
                "coordinated evacuation. Significant homeless population."
            ),
        },
    },

    "willits_ca": {
        "center": [39.4096, -123.3556],
        "terrain_notes": (
            "Small city (pop. 4,988 per 2020 census) in Little Lake Valley at "
            "~1,391 ft elevation, essentially the gateway between the Bay Area "
            "and the North Coast. Willits sits in a small mountain-ringed valley "
            "along US-101, which is the SOLE major north-south highway connecting "
            "the North Coast (Humboldt, Del Norte counties) to the rest of "
            "California. This single-highway dependency defines Willits' fire "
            "vulnerability: when Highway 101 closes, communities to the north are "
            "cut off from southbound evacuation and supply lines. The Redwood "
            "Complex Fire (Oct 8, 2017) demonstrated this catastrophically -- fire "
            "burned along Highway 101 south of Willits, closing the highway and "
            "isolating the community. 9 people died in the Redwood Valley/Potter "
            "Valley area south of Willits. 546 structures destroyed. Gas service "
            "to Willits was cut off. AT&T had to deploy a temporary cell tower "
            "after permanent infrastructure was damaged. The Willits bypass (completed "
            "2016) routes Hwy 101 around the east side of the city, but the "
            "underlying vulnerability remains: fires from the east (Redwood Valley "
            "direction) or south threaten the single corridor. Sherwood Road "
            "northwest of Willits serves 5,500 residents of Brooktrails Township "
            "and surrounding communities -- ALL served by a single emergency access "
            "road through heavily forested terrain. The Oak Fire (2020, 700 acres) "
            "and Walker Fire (2022) both threatened this area and closed Hwy 101. "
            "Fuel types include a mosaic of grass, oak woodland, chaparral, and "
            "mixed timber -- transitioning from interior to coastal vegetation types."
        ),
        "key_features": [
            "US Highway 101 -- SOLE major N-S route, lifeline to North Coast communities",
            "Willits Bypass (2016) -- Hwy 101 rerouted east of city, controversial wetland impact",
            "Highway 20 west to Fort Bragg -- 2-lane mountain road to coast, secondary escape",
            "Sherwood Road -- single access road serving 5,500+ residents in Brooktrails/Sherwood area",
            "Little Lake Valley -- small mountain-ringed valley, agricultural land/wetlands",
            "Brooktrails Township (NW) -- 5,500 residents, heavily forested, single road access",
            "Ridgewood Ranch (S) -- historic ranch (Seabiscuit's home), grassland/oak terrain",
            "Redwood Valley (8 mi S) -- community devastated 2017, on the Hwy 101 corridor",
            "Northwestern Pacific Railroad (historic) -- Skunk Train tourist rail to Fort Bragg",
        ],
        "elevation_range_ft": [1300, 1500],
        "wui_exposure": "high",
        "historical_fires": [
            {
                "name": "Redwood Complex Fire",
                "year": 2017,
                "acres": 36523,
                "details": (
                    "Ignited Oct 8, caused by tree-on-powerline near Potter Valley. "
                    "9 fatalities (deadliest Mendocino County fire). 546 structures "
                    "destroyed (387 homes). Burned along Hwy 101 corridor south of "
                    "Willits. Highway 101 closed, isolating Willits and all communities "
                    "to the north. Gas supply to Willits cut off. 7,620 evacuated."
                ),
            },
            {
                "name": "Oak Fire",
                "year": 2020,
                "acres": 700,
                "details": (
                    "Sep 2020. Burned near Brooktrails' Third Gate Road area, threatening "
                    "the Sherwood Road communities. Closed Highway 101. Evacuations ordered. "
                    "Demonstrated vulnerability of Brooktrails' single-road access."
                ),
            },
            {
                "name": "Walker Fire",
                "year": 2022,
                "acres": 250,
                "details": (
                    "Sep 2022. Burned south of Willits near Hwy 101. Highway closed. "
                    "Two firefighters injured. Showed continued pattern of fires "
                    "threatening the Hwy 101 lifeline corridor."
                ),
            },
            {
                "name": "Mendocino Complex (indirect)",
                "year": 2018,
                "acres": 459123,
                "details": (
                    "While centered east/south of Willits, the massive complex "
                    "impacted regional resources and demonstrated the extreme fire "
                    "potential of the surrounding Mendocino National Forest terrain."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "US-101 south toward Ukiah/Santa Rosa",
                "direction": "S",
                "lanes": 4,
                "bottleneck": (
                    "4-lane freeway (Willits bypass) but narrows through mountain "
                    "terrain south of the bypass. Passes through Redwood Valley -- "
                    "the exact area that burned in 2017."
                ),
                "risk": (
                    "CRITICAL. Redwood Fire (2017) closed this route, isolating Willits "
                    "and all North Coast communities. Fires from the east can reach "
                    "Hwy 101 in the narrow Russian River canyon south of the bypass."
                ),
            },
            {
                "route": "US-101 north toward Laytonville/Eureka",
                "direction": "N",
                "lanes": 2,
                "bottleneck": (
                    "Narrows to 2 lanes north of Willits through mountainous terrain. "
                    "Winding mountain highway with steep grades for ~70 miles to Garberville."
                ),
                "risk": (
                    "Long, remote route through fire-prone terrain. Limited services. "
                    "During major fires, this may be the only viable route out."
                ),
            },
            {
                "route": "Highway 20 west toward Fort Bragg/Coast",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "Two-lane mountain road over the Coast Range to Fort Bragg (~35 mi). "
                    "Winding, steep grades, limited passing opportunities."
                ),
                "risk": (
                    "Fire in the Coast Range can block this route. However, it provides "
                    "a critical alternative when Hwy 101 is blocked. Coastal fog reduces "
                    "fire risk on the western half of the route."
                ),
            },
            {
                "route": "Sherwood Road (Brooktrails access)",
                "direction": "NW",
                "lanes": 2,
                "bottleneck": (
                    "SINGLE road serving 5,500+ residents of Brooktrails Township, "
                    "Sherwood Valley, and surrounding areas. Passes through heavily "
                    "forested terrain. Sherwood Firewise Communities identified this "
                    "as a critical single-point-of-failure."
                ),
                "risk": (
                    "Any fire on Sherwood Road traps 5,500+ people. Dense forest "
                    "canopy over roadway creates ember tunnel. No alternative access "
                    "routes for Brooktrails community."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Mixed regime. Diablo wind influence is moderated by distance from "
                "the Mayacamas but NE offshore events still occur. Afternoon thermal "
                "winds drive upslope runs on surrounding hills. Transition zone between "
                "interior and coastal climate -- marine layer penetration can reduce "
                "fire risk but when absent, inland heat creates extreme conditions."
            ),
            "critical_corridors": [
                "Hwy 101 corridor (N-S) -- fire can run along the Russian River valley",
                "Sherwood Road corridor -- single access through dense forest to Brooktrails",
                "Ridgewood Grade (south) -- fire path through oak/grass terrain toward Hwy 101",
                "Outlet Creek drainage -- channels fire through Little Lake Valley",
            ],
            "rate_of_spread_potential": (
                "Moderate to high. Oak woodland and chaparral burn at 30-80 chains/hour. "
                "Grass at 50-100 chains/hour when cured. Dense timber in Brooktrails area "
                "supports crown fire at 40-100 chains/hour. Redwood Fire demonstrated "
                "rapid spread in mixed fuel types."
            ),
            "spotting_distance": (
                "0.25-1 mile in chaparral/oak. Longer in timber when crowning. "
                "Embers can cross Highway 101 and the Russian River during extreme events."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "City of Willits water system. Brooktrails Township has independent "
                "water system. Both have limited fire suppression capacity during "
                "extended events. Rural areas on wells (electric pumps fail during "
                "power outage)."
            ),
            "power": (
                "PG&E distribution through heavily forested terrain. Tree-on-line "
                "caused the Redwood Fire (2017). Frequent PSPS shutoffs. Willits "
                "is at the end of a long distribution line -- extended outages common. "
                "Gas supply was cut off during Redwood Fire."
            ),
            "communications": (
                "Cell coverage limited. During Redwood Fire, permanent cell towers "
                "were damaged and AT&T deployed a temporary tower. Mendocino County "
                "emergency alert system covers the area but mountainous terrain "
                "creates coverage gaps."
            ),
            "medical": (
                "Adventist Health Howard Memorial Hospital in Willits. Hospital was "
                "NOT evacuated during Redwood Fire but was on standby. Limited "
                "capacity for major disaster. Nearest backup is Ukiah (~20 mi south "
                "on the potentially-closed Hwy 101)."
            ),
        },
        "demographics_risk_factors": {
            "population": 4988,
            "seasonal_variation": (
                "Summer tourism (Skunk Train, cannabis tourism). Brooktrails adds "
                "~5,500 residents to the evacuation demand. Total area population "
                "~10,000-12,000 including surrounding communities."
            ),
            "elderly_percentage": "est. 22-25% (rural, aging community)",
            "mobile_homes": (
                "Significant manufactured housing in Brooktrails and surrounding "
                "areas. Many Redwood Fire losses were manufactured homes in "
                "Redwood Valley."
            ),
            "special_needs_facilities": (
                "Willits Senior Center. Howard Memorial Hospital. Small school "
                "district. Sherwood Valley Rancheria (tribal community) requires "
                "coordinated evacuation. Significant unhoused population."
            ),
        },
    },
}
