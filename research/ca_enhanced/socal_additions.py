"""
Southern California Fire-Vulnerable City Additions
====================================================

13 additional community profiles for SoCal mountain and backcountry WUI zones.
Every entry is built from historical fire records, census data, CAL FIRE
incident reports, USGS debris-flow studies, and local CWPP documents.

Regions covered:
    San Bernardino Mountains (3):
        Running Springs, Big Bear Lake, Forest Falls

    Riverside County Mountains (2):
        Idyllwild, Mountain Center

    San Diego Backcountry (4):
        Alpine, Valley Center, Fallbrook, Pine Valley

    Santa Barbara Coast (2):
        Montecito, Carpinteria

    Tehachapi / Kern (2):
        Frazier Park, Pine Mountain Club

Research sources:
    - Old Fire (2003): CAL FIRE incident report; San Bernardino Sun retrospective
      (Oct 2013); USFS San Bernardino National Forest after-action
    - Line Fire (2024): CAL FIRE final incident report (43,978 acres); San
      Bernardino County Sheriff evacuation orders; CNN/NBC reporting
    - Radford Fire (2022): CAL FIRE; Big Bear Fire Department; KTLA
    - Cedar Fire (2003): CAL FIRE; San Diego Union-Tribune "Firestorm 2003";
      NASA Earth Observatory burned-area imagery near Alpine; Cal OES 20-year
      retrospective (2023); City of San Diego official fire history
    - Witch Creek Fire (2007): CAL FIRE (197,990 acres); USGS Open-File Report
      2008-1080 Valley Center quad perimeter map; San Diego County 2007 AAR
    - Rice Fire (2007): CAL FIRE (9,472 acres, 248 structures); KPBS; North
      County Fire Protection District history
    - Laguna Fire (1970): CAL FIRE; San Diego Reader (1998 retrospective);
      Wildfire Today; SD Union-Tribune 50-year retrospective (2020)
    - Thomas Fire (2017): CAL FIRE (281,893 acres, 1,063 structures); Wikipedia;
      Santa Barbara Bucket Brigade timeline
    - Montecito Debris Flows (2018): USGS Open-File Reports; Geosphere (2019)
      inundation study; Cal OES; Wikipedia (23 dead, 100+ homes destroyed)
    - Mountain Fire (2013): CAL FIRE (27,500 acres); NASA Earth Observatory;
      Press-Enterprise; Idyllwild Town Crier
    - Cranston Fire (2018): CAL FIRE (13,139 acres); CNN; CBS News; San Diego
      Union-Tribune
    - Esperanza Fire (2006): CAL FIRE; NWCG Wildland Fire Lessons Learned Center;
      USFS investigation (5 firefighters killed, 41,173 acres)
    - French Fire (2021): CAL FIRE (26,535 acres); Kern Valley Fire info site
    - Pine Valley CWPP (2019): Pine Valley Fire Safe Council
    - Valley Center Fire Safe Council records; avocado grove fire hazard (SD
      Union-Tribune, Aug 2020)
    - Frazier Park / Mountain Communities of Tejon Pass: Wikipedia; First Street
      Foundation wildfire risk; Kern County Fire Department
    - Pine Mountain Club: PMC HOA fire safety records; Wikipedia; Cal Fire
    - Population / demographics: 2020 US Census via census.gov, city-data.com,
      california-demographics.com, worldpopulationreview.com
    - Coordinates / elevation: USGS topo data; Wikipedia; topographic-map.com
"""

# =============================================================================
# SOUTHERN CALIFORNIA ADDITIONS — 13 COMMUNITIES
# =============================================================================

SOCAL_ADDITIONS = {

    # =========================================================================
    # SAN BERNARDINO MOUNTAINS
    # =========================================================================

    "running_springs_ca": {
        "center": [34.2078, -117.1092],
        "terrain_notes": (
            "Mountain community (pop 5,268, 2020 census) at ~6,100 ft elevation "
            "along Highway 18 in the San Bernardino National Forest. Dense mixed-"
            "conifer timber (Jeffrey pine, white fir, sugar pine, black oak) with "
            "decades of fire-suppression-driven fuel accumulation — the surrounding "
            "forest has some of the heaviest fuel loads in Southern California. "
            "Steep terrain on all sides channels upslope fire runs from the San "
            "Bernardino Valley floor (2,000 ft below) directly into the community. "
            "\n\n"
            "The Old Fire (Oct 25, 2003) was an arson-caused inferno that burned "
            "91,281 acres through the San Bernardino Mountains, destroying 993 "
            "homes and killing 6 people. Fanned by 40-60 mph Santa Ana winds, it "
            "forced the evacuation of 80,000+ residents from Running Springs, "
            "Crestline, Lake Arrowhead, and Cedar Glen. Running Springs was under "
            "direct threat as fire climbed Waterman Canyon toward the Rim of the "
            "World Highway corridor. "
            "\n\n"
            "The Line Fire (Sep 5 - Dec 23, 2024) burned 43,978 acres after "
            "arson ignition near Highland. Mandatory evacuation orders covered "
            "Running Springs and Arrowbear Lake — ~4,800 homes affected. The fire "
            "burned in steep, treacherous terrain with massive fuel loads and no "
            "access for ground crews. Terrain was described by firefighters as "
            "'no access and massive amounts of fuel to burn.' "
            "\n\n"
            "Highway 18 (Rim of the World Drive) is the primary corridor but is "
            "narrow, winding, and frequently closed during fire events. The "
            "community sits between Lake Arrowhead (west) and Big Bear Lake "
            "(east) on the same vulnerable mountain highway system."
        ),
        "key_features": [
            "Rim of the World Highway 18 — only through-route, narrow winding mountain road",
            "San Bernardino National Forest — dense mixed-conifer timber surrounds community",
            "Waterman Canyon — primary fire corridor from valley floor to mountaintop",
            "Steep south-facing slopes above San Bernardino Valley — 4,000 ft elevation gain",
            "Arrowbear Lake and Green Valley Lake — nearby communities on same road network",
            "Heavy dead/down fuel loading from drought-killed trees and bark beetle mortality",
        ],
        "elevation_range_ft": [5800, 6400],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Old Fire",
                "year": 2003,
                "acres": 91281,
                "details": (
                    "Arson-caused (Rickie Lee Fowler, convicted). Ignited in Waterman "
                    "Canyon near San Bernardino and raced upslope into mountain "
                    "communities. 993 homes destroyed, 6 deaths. 40-60 mph Santa Ana "
                    "winds. Forced evacuation of 80,000+ from mountain communities "
                    "including Running Springs. Part of the October 2003 Southern "
                    "California firestorm — the most costly natural disaster in CA "
                    "history at the time."
                ),
            },
            {
                "name": "Line Fire",
                "year": 2024,
                "acres": 43978,
                "details": (
                    "Arson-caused (Justin Wayne Halstenberg, convicted May 2025 on "
                    "7 counts including aggravated arson). Ignited near Highland, "
                    "burned into San Bernardino Mountains. Running Springs and "
                    "Arrowbear Lake under mandatory evacuation — ~4,800 homes "
                    "affected. Steep terrain with no access, massive fuel loads. "
                    "100% contained Dec 23, 2024."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 18 West (toward Crestline / Lake Arrowhead)",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "Narrow, winding mountain highway with steep drop-offs. "
                    "Shares corridor with evacuees from Arrowbear Lake, Green "
                    "Valley Lake. Frequently closed during fire events."
                ),
                "risk": (
                    "Fire approaching from south or west through Waterman or "
                    "Cleghorn canyons can cut this route. Single-lane segments "
                    "gridlock rapidly."
                ),
            },
            {
                "route": "Highway 18 East (toward Big Bear Lake)",
                "direction": "E",
                "lanes": 2,
                "bottleneck": (
                    "Long, winding route over the mountain to Big Bear Valley. "
                    "Provides escape only if fire is approaching from west/south. "
                    "During Line Fire 2024, this route led to a dead end at Big "
                    "Bear which was also threatened."
                ),
                "risk": (
                    "Route can dead-end if Big Bear is also under evacuation. "
                    "Only exit from Big Bear is Highway 18 north to Lucerne Valley "
                    "or Highway 38 east — both remote desert routes."
                ),
            },
            {
                "route": "Highway 330 (toward Highland / San Bernardino)",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Very steep, winding descent from 6,000 ft to 1,500 ft in "
                    "~14 miles. Extremely dangerous during fire events — the route "
                    "descends through the exact terrain fires climb."
                ),
                "risk": (
                    "Almost certainly impassable during major upslope fire events. "
                    "Closed during both Old Fire 2003 and Line Fire 2024."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Santa Ana winds (NE, 40-60 mph during major events) drive fire "
                "upslope from San Bernardino Valley into the mountains. Sundowner-"
                "type effects in late afternoon can accelerate fire on south-facing "
                "slopes. Diurnal upslope winds bring fire from lower elevations daily."
            ),
            "critical_corridors": [
                "Waterman Canyon — primary fire chimney from valley floor",
                "Highway 330 corridor — steep canyon with continuous fuels",
                "Cleghorn Canyon — connects to Cajon Pass wind funnel",
                "Deep Creek drainage — northeast approach vector",
            ],
            "rate_of_spread_potential": (
                "Extreme during Santa Ana events. The Old Fire traveled from "
                "Waterman Canyon to mountain communities (~10 mi, 4,000 ft gain) "
                "in hours. Dense timber and steep slopes create explosive upslope "
                "runs with potential for crown fire in conifer stands."
            ),
            "spotting_distance": (
                "1-2 miles in conifer timber. Bark and brand lofting from torching "
                "conifers creates prolific spotting downwind. During Santa Ana "
                "events, spots can establish well ahead of the main fire front."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Crestline-Lake Arrowhead Water Agency (CLAWA) and Running "
                "Springs Water District. Gravity-fed from mountain reservoirs. "
                "Limited storage capacity — extended firefighting demand can "
                "deplete tanks. Distant from major water sources."
            ),
            "power": (
                "SCE serves area. Overhead lines through dense timber are ignition "
                "sources and vulnerable to tree strike. PSPS shutoffs during Red "
                "Flag warnings leave community without power for days. Mountain "
                "communities last to be restored after outages."
            ),
            "communications": (
                "Cell coverage patchy in mountain terrain. Tower sites on ridgelines "
                "are themselves fire-vulnerable. During Line Fire 2024, some "
                "evacuees reported difficulty receiving alerts. Ham radio and "
                "community notification systems supplement cell."
            ),
            "medical": (
                "No hospital in Running Springs. Mountains Community Hospital in "
                "Lake Arrowhead (8 mi west) is the closest facility — a small "
                "critical-access hospital. Major trauma requires helicopter "
                "transport to Loma Linda or San Bernardino (~25 mi, 45+ min by "
                "road on mountain highways)."
            ),
        },
        "demographics_risk_factors": {
            "population": 5268,
            "seasonal_variation": (
                "Significant. Tourist and cabin-rental traffic increases population "
                "on winter weekends (ski season) and summer weekends. Many seasonal "
                "visitors unfamiliar with evacuation routes."
            ),
            "elderly_percentage": "est. 18-22%",
            "mobile_homes": (
                "Several mobile home parks in the community. Mobile homes are "
                "highly vulnerable to radiant heat and ember attack. Older units "
                "lack modern ember-resistant venting."
            ),
            "special_needs_facilities": (
                "No major special-needs facilities. Nearest nursing/assisted "
                "living in valley communities below. Isolated elderly residents "
                "in mountain cabins are particularly vulnerable."
            ),
        },
    },

    "big_bear_lake_ca": {
        "center": [34.2439, -116.9114],
        "terrain_notes": (
            "Incorporated resort city (pop 5,046, 2020 census) at 6,752 ft "
            "elevation on the south shore of Big Bear Lake in the San Bernardino "
            "Mountains. Surrounded by San Bernardino National Forest on all sides. "
            "The community extends ~7 miles along the lakeshore in a relatively "
            "flat valley but is ringed by steep, densely forested mountains "
            "rising to 8,000-9,000 ft. "
            "\n\n"
            "Big Bear has extremely limited egress — only three routes out, all "
            "narrow mountain highways that converge on the valley: Highway 18 "
            "west to Running Springs/Crestline, Highway 38 east through Barton "
            "Flats to Redlands, and Highway 18 north through Baldwin Lake to "
            "Lucerne Valley. During any major fire event, one or more of these "
            "routes is likely closed, potentially trapping thousands. During the "
            "Line Fire (2024), Highway 38 and portions of Highway 18 west were "
            "closed — the only exit was Highway 18 north to Lucerne Valley, a "
            "remote desert route. "
            "\n\n"
            "The Old Fire (2003) forced the entire Big Bear Valley to evacuate. "
            "The Radford Fire (Sep 2022) burned 1,079 acres directly between "
            "Bear Mountain and Snow Summit ski resorts — the heart of the "
            "community — before 471 firefighters achieved containment. No "
            "structures lost but the fire demonstrated that the resort core "
            "is directly threatened. The Holcomb Fire burned ~1,500 acres near "
            "Baldwin Lake threatening Highway 18 north."
        ),
        "key_features": [
            "Big Bear Lake — 7-mile alpine lake, provides water supply and defensible space on north side",
            "Bear Mountain and Snow Summit ski areas — steep forested slopes immediately south of town",
            "Baldwin Lake (dry lakebed) — northeast, sparse vegetation provides natural break",
            "San Bernardino Peak ridgeline — 10,649 ft, walls off southern approach",
            "Only 3 highway exits from the valley — extreme evacuation bottleneck",
            "Dense Jeffrey pine / lodgepole pine forest up to 9,000 ft",
        ],
        "elevation_range_ft": [6700, 6800],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Old Fire",
                "year": 2003,
                "acres": 91281,
                "details": (
                    "While centered on lower mountain communities, the Old Fire "
                    "threatened Big Bear Valley and forced full evacuation. Fire "
                    "burned through San Bernardino National Forest toward the "
                    "valley from the southwest. 40-60 mph Santa Ana winds. Part "
                    "of the 2003 Southern California firestorm."
                ),
            },
            {
                "name": "Radford Fire",
                "year": 2022,
                "acres": 1079,
                "details": (
                    "Burned between Bear Mountain and Snow Summit ski resorts — "
                    "the core of the resort community. 471 firefighters deployed. "
                    "Evacuation orders issued then downgraded to warnings. No "
                    "structures lost but fire reached ski resort slopes. "
                    "Demonstrated direct threat to resort infrastructure."
                ),
            },
            {
                "name": "Line Fire",
                "year": 2024,
                "acres": 43978,
                "details": (
                    "Burned into San Bernardino Mountains from Highland. Mandatory "
                    "evacuation orders for portions of Big Bear Valley (Big Bear "
                    "Dam east to Wildrose Lane). Highway 38 and Highway 18 west "
                    "both closed — only exit was SR-18 north to Lucerne Valley. "
                    "Evacuation orders lifted Oct 11, 2024."
                ),
            },
            {
                "name": "Holcomb Fire",
                "year": 2006,
                "acres": 1500,
                "details": (
                    "Burned near Baldwin Lake and threatened Highway 18 north — "
                    "the backup evacuation route. Over 1,000 firefighters deployed. "
                    "Demonstrated vulnerability of the northern exit."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 18 West (to Running Springs / Crestline)",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "Narrow, steep mountain highway. 35+ miles of winding road "
                    "to reach valley floor. Closed during Line Fire 2024 and "
                    "Old Fire 2003."
                ),
                "risk": (
                    "Most likely route to be cut by fire approaching from "
                    "the south/southwest — the dominant fire approach direction. "
                    "Shares corridor with Running Springs evacuees."
                ),
            },
            {
                "route": "Highway 38 East (to Barton Flats / Redlands)",
                "direction": "E",
                "lanes": 2,
                "bottleneck": (
                    "Extremely winding, narrow road through remote forest. "
                    "~40 miles to Redlands. Closed during Line Fire 2024. "
                    "Sections regularly washed out by winter storms."
                ),
                "risk": (
                    "Fire from the south or east can cut this route at multiple "
                    "points. Road passes through dense timber with no defensible "
                    "space. Remote sections have no cell service."
                ),
            },
            {
                "route": "Highway 18 North (to Lucerne Valley)",
                "direction": "N",
                "lanes": 2,
                "bottleneck": (
                    "Route of last resort. Descends north through Baldwin Lake "
                    "to the Mojave Desert. Remote, limited services. 30+ miles "
                    "to nearest desert community."
                ),
                "risk": (
                    "Least likely to be cut by wildfire (north-facing, desert "
                    "approach) but leads to remote desert with extreme heat. "
                    "Was the ONLY exit during Line Fire 2024. Holcomb Fire "
                    "(2006) threatened this route near Baldwin Lake."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Santa Ana winds from NE drive fire from desert side, but the "
                "primary threat is upslope-driven fire from the south/southwest "
                "climbing 4,000+ ft from San Bernardino Valley. Foehn winds "
                "can exceed 60 mph through mountain passes."
            ),
            "critical_corridors": [
                "Santa Ana River Canyon (south approach from Barton Flats)",
                "Waterman Canyon / Highway 330 corridor (southwest approach)",
                "Mill Creek Canyon (southeast approach from Forest Falls area)",
                "Holcomb Valley (north — less common but threatens escape route)",
            ],
            "rate_of_spread_potential": (
                "High to extreme during wind events. Dense conifer forest allows "
                "crown fire development. Steep slopes south of the valley create "
                "chimney effect. Fire can climb from valley floor to ridgeline "
                "in hours under wind."
            ),
            "spotting_distance": (
                "1-3 miles in conifer timber. High-elevation winds can carry "
                "brands significant distances. Spotting across the lake is "
                "possible during extreme events."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Big Bear Lake Department of Water and Power (BBLDWP). Water "
                "supplied from Big Bear Lake (reservoir) and groundwater wells. "
                "Dam-controlled lake level can drop during drought years, reducing "
                "available firefighting supply. Distribution system is aging."
            ),
            "power": (
                "SCE serves the valley. Long overhead transmission lines through "
                "forested terrain are vulnerable to tree strike and fire damage. "
                "PSPS shutoffs during high-wind events leave community without "
                "power. Ski resorts and tourism economy suffer during extended "
                "outages. Backup generators are critical for water pumping."
            ),
            "communications": (
                "Limited cell coverage — mountainous terrain blocks signal in "
                "many areas. During Line Fire 2024, some residents had difficulty "
                "receiving evacuation alerts. Community relies on local radio "
                "station KBHR 93.3 for emergency information."
            ),
            "medical": (
                "Bear Valley Community Hospital — small critical-access facility. "
                "Limited trauma capability. Serious injuries require helicopter "
                "or long ambulance transport to Loma Linda University Medical "
                "Center (~50 mi, 90+ min by mountain road). During evacuation "
                "events, medical transport is severely delayed."
            ),
        },
        "demographics_risk_factors": {
            "population": 5046,
            "seasonal_variation": (
                "EXTREME seasonal variation. Population can swell to 50,000-"
                "100,000+ on peak winter and summer weekends. Ski season (Nov-Apr) "
                "and summer recreation bring massive day-trip and overnight "
                "visitor populations. Most visitors are unfamiliar with "
                "evacuation routes and mountain driving."
            ),
            "elderly_percentage": "est. 20-24%",
            "mobile_homes": (
                "Several mobile home parks in Big Bear City (unincorporated area "
                "east of the city). Significant vulnerability to ember attack "
                "and radiant heat."
            ),
            "special_needs_facilities": (
                "Limited. Small community hospital. No major nursing homes. "
                "Remote location means special-needs populations face extended "
                "evacuation transport times."
            ),
        },
    },

    "forest_falls_ca": {
        "center": [34.0883, -116.9203],
        "terrain_notes": (
            "Extremely isolated mountain hamlet (pop 1,102, 2020 census) at "
            "5,000-6,000 ft elevation in Mill Creek Canyon in the San "
            "Bernardino Mountains. Forest Falls is one of the most evacuation-"
            "vulnerable communities in California — it is a dead-end canyon "
            "with a SINGLE ROAD in and out (Valley of the Falls Drive / "
            "Highway 38). The community stretches ~5 miles in a narrow band "
            "along the south side of Mill Creek Canyon, which trends slightly "
            "north of east. "
            "\n\n"
            "Terrain is extraordinarily steep and rugged. San Gorgonio Mountain "
            "(11,503 ft — the highest point in Southern California) rises "
            "directly north in the San Gorgonio Wilderness Area. Canyon walls "
            "on both sides are near-vertical in places, covered with dense "
            "mixed-conifer forest and heavy brush. Mill Creek itself is deeply "
            "incised, creating a natural fire chimney that channels winds and "
            "flames up-canyon. "
            "\n\n"
            "The Valley Fire (2018) ignited at the intersection of Valley of "
            "the Falls Drive and Highway 38 — the single access point — "
            "threatening to trap the entire community. During the Line Fire "
            "(2024), Forest Falls was under mandatory evacuation with residents "
            "directed downbound on SR-38 toward Mentone. Highway 38 past Valley "
            "of the Falls Drive was closed in both directions. "
            "\n\n"
            "If a fire blocks the single access road, there is NO alternative "
            "escape. The canyon dead-ends at the wilderness boundary. This "
            "community represents a worst-case evacuation scenario."
        ),
        "key_features": [
            "Dead-end canyon — Valley of the Falls Drive is the ONLY way in or out",
            "Mill Creek Canyon — deep, narrow V-shaped canyon acting as fire chimney",
            "San Gorgonio Mountain (11,503 ft) — towering wilderness directly north",
            "San Gorgonio Wilderness Area — dense unmanaged forest, no access roads",
            "Highway 38 / Valley of the Falls Drive junction — single escape point",
            "Steep canyon walls — near-vertical slopes channel fire and wind",
        ],
        "elevation_range_ft": [5000, 6000],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Valley Fire",
                "year": 2018,
                "acres": 1346,
                "details": (
                    "Ignited at the intersection of Valley of the Falls Drive "
                    "and Highway 38 — the single access/escape point for Forest "
                    "Falls. Fire threatened to trap the entire community. "
                    "Evacuations ordered. Demonstrated the catastrophic "
                    "vulnerability of the single-road community."
                ),
            },
            {
                "name": "Line Fire",
                "year": 2024,
                "acres": 43978,
                "details": (
                    "Massive fire burned into San Bernardino Mountains from "
                    "Highland. Forest Falls under mandatory evacuation. Residents "
                    "directed downbound on SR-38 to Mentone. Highway 38 past "
                    "Valley of the Falls Drive closed in both directions. "
                    "Firefighters worked treacherous terrain with no access."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Valley of the Falls Drive / Highway 38 (to Mentone / Redlands)",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "THIS IS THE ONLY ROUTE. Narrow, winding canyon road descends "
                    "~10 miles through Mill Creek Canyon to the valley floor at "
                    "Mentone. Single point of failure at the Valley of the Falls "
                    "Drive / Hwy 38 junction."
                ),
                "risk": (
                    "CATASTROPHIC. Any fire blocking this road traps the entire "
                    "community with no alternative. The Valley Fire (2018) ignited "
                    "at this exact junction. Canyon walls prevent off-road escape. "
                    "Community has zero redundancy in evacuation capacity."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Upslope afternoon winds channel fire into the canyon. Santa Ana "
                "winds from NE can push fire down-canyon from the wilderness, "
                "while sundowner-type evening winds reverse and push fire up-"
                "canyon from the valley floor. The canyon creates its own wind "
                "dynamics — a natural bellows effect."
            ),
            "critical_corridors": [
                "Mill Creek Canyon — the primary fire corridor, channeling fire and wind",
                "Highway 38 corridor — only access, also the fire corridor",
                "San Gorgonio wilderness drainages — unmanaged fuel descending into community",
                "Santa Ana River drainage — connects to broader fire landscape",
            ],
            "rate_of_spread_potential": (
                "Extreme in the canyon. Steep V-shaped walls create chimney effect "
                "that can double or triple normal spread rates. Dense continuous "
                "fuels from canyon floor to ridgeline provide unbroken fire path. "
                "Crown fire potential in conifer stands."
            ),
            "spotting_distance": (
                "1-2 miles. Canyon winds can loft brands up-canyon ahead of the "
                "fire front. Narrow canyon width means spots on opposite wall "
                "easily coalesce with main fire."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Small local water district. Limited storage capacity. No "
                "connection to major municipal systems. Fire demand would "
                "rapidly deplete available supply. Creek water is seasonal."
            ),
            "power": (
                "SCE overhead lines through the canyon — single feed along the "
                "access road. Extremely vulnerable to fire damage. Loss of power "
                "means loss of water pumping. PSPS shutoffs during Red Flag "
                "warnings cut power to the entire community."
            ),
            "communications": (
                "Virtually no cell coverage in the canyon. Deep terrain blocks "
                "signal from all directions. Residents may not receive wireless "
                "emergency alerts. Community relies on word-of-mouth, landlines "
                "(if working), and physical door-knocking for notification."
            ),
            "medical": (
                "No medical facilities. Nearest hospital is in Redlands (~20 mi, "
                "30-45 min on mountain road). Helicopter access limited by canyon "
                "terrain and potential smoke. During fire events, ambulance access "
                "via the single road may be impossible."
            ),
        },
        "demographics_risk_factors": {
            "population": 1102,
            "seasonal_variation": (
                "Moderate. Weekend hikers and day visitors to San Gorgonio "
                "Wilderness increase population. Big Falls trailhead is a "
                "popular destination. Visitors may be on trails and unreachable "
                "during sudden evacuations."
            ),
            "elderly_percentage": "est. 15-20%",
            "mobile_homes": (
                "Some mobile homes and older cabin-style residences along the "
                "canyon. Many structures are older wood-frame cabins with no "
                "modern fire-resistant construction."
            ),
            "special_needs_facilities": (
                "None. Isolated canyon location means any special-needs "
                "population faces extreme evacuation challenges. Single-road "
                "access makes ambulance evacuation a single-point-of-failure."
            ),
        },
    },

    # =========================================================================
    # RIVERSIDE COUNTY MOUNTAINS
    # =========================================================================

    "idyllwild_ca": {
        "center": [33.7443, -116.7258],
        "terrain_notes": (
            "Mountain art colony and resort community (pop 4,163, 2020 census; "
            "Idyllwild-Pine Cove CDP) at ~5,400 ft in the San Jacinto Mountains "
            "of Riverside County. Nestled in dense conifer forest (Jeffrey pine, "
            "Coulter pine, incense cedar, white fir, black oak) on the western "
            "slope of the San Jacinto range. Mount San Jacinto (10,834 ft) towers "
            "directly east. "
            "\n\n"
            "The community has been repeatedly threatened by major wildfires. The "
            "Mountain Fire (Jul 15, 2013) ignited near the Highway 243/74 junction "
            "and burned 27,500 acres on steep timber and chaparral slopes, forcing "
            "evacuation of ~6,000 Idyllwild and Fern Valley residents. Cost: $20M+. "
            "The Cranston Fire (Jul 25, 2018) was arson-caused (Brandon McGlover, "
            "convicted) and burned 13,139 acres, forcing evacuation of 7,000+ "
            "people from Idyllwild, Mountain Center, and Anza. Five homes destroyed. "
            "The Esperanza Fire (Oct 26, 2006) was an arson-caused wildfire that "
            "burned 41,173 acres near Cabazon; five Engine 57 firefighters were "
            "killed defending an isolated structure — the deadliest California "
            "wildfire for firefighters since 1966. "
            "\n\n"
            "Only two highways exit the community: Highway 243 north (steep descent "
            "through Banning/Idyllwild Panoramic Highway to I-10) and Highway 74 "
            "south/west (through Mountain Center toward Hemet). Both are narrow, "
            "winding 2-lane mountain roads. A fire between these two corridors "
            "— as the Mountain Fire demonstrated — can threaten both escape routes "
            "simultaneously."
        ),
        "key_features": [
            "San Jacinto Mountains — Mount San Jacinto 10,834 ft dominates eastern skyline",
            "Only two exits: Hwy 243 north to I-10, Hwy 74 south/west to Hemet",
            "Dense Jeffrey pine / white fir forest with heavy understory",
            "San Bernardino National Forest surrounds community on all sides",
            "Steep terrain — 5,000 ft elevation gain from desert floor to ridgeline",
            "Mount San Jacinto State Park — wilderness area to the east",
            "Strawberry Creek — local drainage creating fire corridor through town",
        ],
        "elevation_range_ft": [5200, 5600],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Mountain Fire",
                "year": 2013,
                "acres": 27500,
                "details": (
                    "Started at Hwy 243/74 junction from failed electrical equipment "
                    "on private property. Burned for 16 days on steep timber and "
                    "chaparral slopes. ~6,000 Idyllwild/Fern Valley residents "
                    "evacuated. 7 residences, 5 commercial structures destroyed in "
                    "Apple Canyon area. $20M+ suppression cost. Riverside County "
                    "declared emergency."
                ),
            },
            {
                "name": "Cranston Fire",
                "year": 2018,
                "acres": 13139,
                "details": (
                    "Arson-caused (Brandon McGlover, convicted). 7,000+ people "
                    "evacuated from Idyllwild, Mountain Center, Anza. 5 homes "
                    "destroyed. Fire impacted Lake Hemet area and Mount San "
                    "Jacinto State Park. Fully contained Aug 10, 2018."
                ),
            },
            {
                "name": "Esperanza Fire",
                "year": 2006,
                "acres": 41173,
                "details": (
                    "Arson-caused (Raymond Oyler, convicted of first-degree murder). "
                    "Started near Cabazon, burned 41,173 acres. FIVE ENGINE 57 "
                    "FIREFIGHTERS KILLED (Jason McKay, Jess McLean, Daniel Najera, "
                    "Mark Loutzenhiser, Pablo Cerda) when overrun by 30-mph, "
                    "70-ft-high flames at 1,300F. Fire traveled through the broader "
                    "San Jacinto Mountains region."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 243 North (Idyllwild Panoramic Highway to Banning / I-10)",
                "direction": "N",
                "lanes": 2,
                "bottleneck": (
                    "Steep, winding descent from 5,400 ft to 2,300 ft. Multiple "
                    "switchbacks, blind curves, narrow shoulders. 25-mile drive "
                    "to I-10. Extremely slow for traffic volume during evacuation."
                ),
                "risk": (
                    "Fire approaching from north/northeast (desert wind-driven) "
                    "can cut this route. The corridor runs through heavy chaparral "
                    "and timber. Flash floods can also close sections."
                ),
            },
            {
                "route": "Highway 74 South/West (to Mountain Center / Hemet)",
                "direction": "S/W",
                "lanes": 2,
                "bottleneck": (
                    "Narrow mountain highway through the junction at Mountain "
                    "Center. Connects to Highway 74 west toward Hemet or south "
                    "toward Anza. 20+ miles to valley floor."
                ),
                "risk": (
                    "Mountain Fire (2013) started at the Hwy 243/74 junction, "
                    "demonstrating that fire can originate at the critical "
                    "intersection of both escape routes. Fire from any direction "
                    "can close portions of this road."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Dominant fire weather: desert-to-mountain (NE-E) winds push fire "
                "from the Coachella Valley floor upslope into timber. Hot, dry "
                "Santa Ana-type conditions with single-digit humidity. Afternoon "
                "upslope thermals create daily fire weather cycle."
            ),
            "critical_corridors": [
                "San Jacinto River drainage — southwest approach through timber",
                "Strawberry Creek — runs through community center",
                "Highway 243 corridor — fire chimney from desert floor",
                "Highway 74 corridor — connects to Mountain Center fire zone",
                "Tahquitz Creek — steep drainage east of town",
            ],
            "rate_of_spread_potential": (
                "Extreme in wind-driven conditions. Steep terrain multiplies spread "
                "rates 2-3x. Dense conifer forest supports crown fire runs. The "
                "Esperanza Fire traveled at 30 mph with 70-ft flames. Mountain "
                "Fire burned 8,000 acres in first hours with 'extreme growth "
                "potential' designation."
            ),
            "spotting_distance": (
                "1-3 miles in conifer/chaparral mix. Steep terrain and strong "
                "upslope winds create long-range spotting. Bark from torching "
                "conifers can spot across canyons."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Fern Valley Water District and Idyllwild Water District. Local "
                "wells and small reservoirs. Limited storage for prolonged "
                "firefighting demand. No connection to metropolitan water systems. "
                "Drought reduces groundwater availability."
            ),
            "power": (
                "SCE overhead lines through forested mountain terrain. PSPS "
                "shutoffs during Red Flag warnings. Single transmission feed "
                "from valley — loss cuts power to entire community. Power loss "
                "disables water pumps."
            ),
            "communications": (
                "Limited cell coverage in mountain terrain. Deep canyons block "
                "signal. Community relies on Idyllwild Town Crier newspaper, "
                "local notification systems, and physical notification. Some "
                "areas have no wireless service."
            ),
            "medical": (
                "Idyllwild Fire Protection District provides EMS. NO hospital "
                "in community. Nearest hospitals: Hemet Valley Medical Center "
                "(~30 mi, 45-60 min mountain road), Desert Regional Medical "
                "Center in Palm Springs (~40 mi via Hwy 243, 60+ min). "
                "Helicopter access dependent on smoke/weather."
            ),
        },
        "demographics_risk_factors": {
            "population": 4163,
            "seasonal_variation": (
                "Significant. Summer tourism, fall foliage visitors, winter snow "
                "visitors boost population substantially. Annual Jazz in the "
                "Pines festival draws thousands. Many second homes occupied only "
                "weekends/holidays. Transient population unfamiliar with "
                "evacuation procedures."
            ),
            "elderly_percentage": "est. 25-30% (median age high, retirement community character)",
            "mobile_homes": (
                "Limited mobile home presence. Community is primarily single-"
                "family cabins and homes, many older wood-frame construction "
                "with wood shake roofs — highly vulnerable to ember attack."
            ),
            "special_needs_facilities": (
                "No major facilities. Astrocamp (outdoor education) hosts "
                "school groups. Community has high proportion of elderly "
                "residents, including those living alone in remote cabins."
            ),
        },
    },

    "mountain_center_ca": {
        "center": [33.7042, -116.7259],
        "terrain_notes": (
            "Tiny unincorporated crossroads community (pop ~50, 2023 census; "
            "median age 73.1) at 4,518 ft elevation at the junction of Highway "
            "74 and Highway 243 in Riverside County. Despite its minuscule "
            "population, Mountain Center is a critical transportation node — it "
            "is the gateway junction through which all traffic between Idyllwild, "
            "Anza, Hemet, and Palm Springs must pass. The junction sits in a "
            "natural fire funnel where multiple drainages converge. "
            "\n\n"
            "The Mountain Fire (2013) started at this exact junction from failed "
            "electrical equipment and burned 27,500 acres. The Cranston Fire "
            "(2018) also impacted Mountain Center. A fire at or near this "
            "junction can simultaneously cut evacuation routes for Idyllwild "
            "(6 mi north), Anza (12 mi south), and Pine Cove. "
            "\n\n"
            "Terrain is a convergence zone: steep chaparral and timber slopes "
            "from the San Jacinto Mountains funnel down to the valley floor. "
            "The junction sits in a saddle between mountain ridges where wind "
            "is concentrated and fire is channeled. Lake Hemet (1 mi south) "
            "provides limited defensible space."
        ),
        "key_features": [
            "Highway 74/243 junction — critical transportation node for entire San Jacinto region",
            "Fire funnel convergence zone — drainages from multiple directions meet here",
            "Gateway to Idyllwild (6 mi N), Anza (12 mi S), Hemet (25 mi W)",
            "Lake Hemet — small reservoir 1 mi south, limited defensible space",
            "Mountain Fire (2013) origin point — fire started at this junction",
            "San Jacinto Mountains saddle — wind concentration zone",
        ],
        "elevation_range_ft": [4400, 4700],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Mountain Fire",
                "year": 2013,
                "acres": 27500,
                "details": (
                    "STARTED AT THIS JUNCTION (Hwy 243/74). Electrical equipment "
                    "failure ignited dry vegetation. Burned for 16 days in the "
                    "San Jacinto Mountains. Forced evacuation of 6,000 from "
                    "Idyllwild/Fern Valley. 12 structures destroyed. Fire burned "
                    "directly through Mountain Center area."
                ),
            },
            {
                "name": "Cranston Fire",
                "year": 2018,
                "acres": 13139,
                "details": (
                    "Arson-caused fire impacted Mountain Center, Idyllwild, "
                    "and Anza communities. 7,000+ evacuated. Fire burned through "
                    "the San Bernardino National Forest in the immediate area."
                ),
            },
            {
                "name": "Mountain Center Fire",
                "year": 2025,
                "acres": None,
                "details": (
                    "Fire reported Aug 22, 2025 at Highway 74 and Mountain "
                    "Center Community. Immediate threat to life, evacuation "
                    "orders issued. Demonstrates ongoing ignition risk at "
                    "this junction."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 74 West (to Hemet / San Jacinto)",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "Primary escape route toward valley cities. Narrow, winding "
                    "25-mile descent to Hemet. Carries combined traffic from "
                    "Mountain Center, Idyllwild, and Anza during events."
                ),
                "risk": (
                    "Fire from the west (common) can cut this route. Road passes "
                    "through heavy chaparral in multiple drainages."
                ),
            },
            {
                "route": "Highway 243 North (to Idyllwild / Banning)",
                "direction": "N",
                "lanes": 2,
                "bottleneck": (
                    "Leads into Idyllwild (6 mi) then continues to Banning/I-10. "
                    "During fire events, this becomes a shared evacuation corridor "
                    "with Idyllwild's 4,000+ residents."
                ),
                "risk": (
                    "Fire at the junction (as in 2013) blocks access to this "
                    "route entirely. Even if passable, adds 4,000+ Idyllwild "
                    "evacuees to traffic volume."
                ),
            },
            {
                "route": "Highway 74 East / South (to Anza / Temecula)",
                "direction": "S/E",
                "lanes": 2,
                "bottleneck": (
                    "Long route through Anza to Temecula (50+ miles). Remote, "
                    "limited services. Passes through open chaparral."
                ),
                "risk": (
                    "Least likely to be cut by fire from the west/north but "
                    "adds significant distance. Cranston Fire (2018) impacted "
                    "Anza area along this route."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Convergence zone dynamics. Winds funnel through the junction "
                "from multiple canyons. Santa Ana winds from NE drive fire from "
                "desert. Afternoon upslope thermals from Hemet Valley push fire "
                "uphill from the west."
            ),
            "critical_corridors": [
                "Highway 74 corridor (east-west fire path)",
                "Highway 243 corridor (north-south fire path)",
                "San Jacinto River drainage (northwest approach)",
                "Anza Valley drainage (south approach)",
            ],
            "rate_of_spread_potential": (
                "Extreme at the junction due to wind convergence and steep terrain "
                "on multiple sides. Mountain Fire (2013) burned 8,000 acres in "
                "the first hours after igniting here."
            ),
            "spotting_distance": (
                "1-2 miles in chaparral/timber transition zone. Wind convergence "
                "creates erratic fire behavior and unpredictable spot fires."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "No public water system. Rural properties on wells. Lake Hemet "
                "provides limited water but requires pumping. No fire hydrants "
                "in the immediate area."
            ),
            "power": (
                "SCE overhead lines. Single feed through mountain terrain. PSPS "
                "shutoffs during Red Flag warnings. No redundancy."
            ),
            "communications": (
                "Limited to no cell coverage. Remote mountain junction with "
                "poor wireless infrastructure. Residents depend on scanner "
                "monitoring and physical notification."
            ),
            "medical": (
                "No medical facilities. Nearest hospital in Hemet (~25 mi, "
                "40-60 min mountain road). EMS response time from CAL FIRE "
                "station may exceed 20 minutes."
            ),
        },
        "demographics_risk_factors": {
            "population": 50,
            "seasonal_variation": (
                "Very high relative to population. Through-traffic on Hwy 74/243 "
                "creates transient population. Lake Hemet Recreation Area draws "
                "campers and fishermen. Weekend traffic can be substantial."
            ),
            "elderly_percentage": "est. very high (median age 73.1)",
            "mobile_homes": (
                "Several mobile/manufactured homes on rural lots. Minimal "
                "fire-resistant construction standards."
            ),
            "special_needs_facilities": (
                "None. Extremely isolated location with elderly population. "
                "Self-evacuation may be difficult for residents."
            ),
        },
    },

    # =========================================================================
    # SAN DIEGO BACKCOUNTRY
    # =========================================================================

    "alpine_ca": {
        "center": [32.8351, -116.7664],
        "terrain_notes": (
            "Large unincorporated community (pop 14,696, 2020 census) straddling "
            "Interstate 8 at ~2,000 ft elevation on the eastern edge of the "
            "California coastal region, 30 miles east of downtown San Diego. "
            "Bordered by Cleveland National Forest and two Kumeyaay reservations "
            "(Viejas and Sycuan). Alpine sits squarely in the Cedar Fire (2003) "
            "corridor — the most destructive wildfire in San Diego County history. "
            "\n\n"
            "The Cedar Fire (Oct 25, 2003) burned 273,246 acres, destroyed 2,820 "
            "structures (2,232 homes), and killed 15 people — 13 in the first "
            "24 hours. The fire crossed Interstate 8 and Interstate 15, forging "
            "into Alpine, Harbison Canyon, Crest, and Lake Jennings on October 26. "
            "Hundreds of homes burned in Alpine — the same area devastated by the "
            "Laguna Fire 33 years earlier (1970). Alpine's WUI exposure is extreme: "
            "residential development extends directly into chaparral-covered "
            "hillsides with continuous fuel from Cleveland National Forest. "
            "\n\n"
            "I-8 runs through the center of the community, providing rapid "
            "east-west evacuation capacity — the best evacuation infrastructure "
            "of any mountain community in the region. However, fire can cross "
            "I-8 (as Cedar Fire proved), and spot fires from the east/northeast "
            "during Santa Ana events can establish in the community before "
            "evacuation is ordered."
        ),
        "key_features": [
            "Interstate 8 corridor — high-capacity evacuation route through community center",
            "Cleveland National Forest — surrounds community to north, east, and south",
            "Cedar Fire (2003) burn corridor — community was directly impacted",
            "Viejas and Sycuan reservations — adjacent tribal lands",
            "Harbison Canyon — steep terrain to southwest, heavy 2003 losses",
            "Alpine Boulevard — historic main street, WUI transition zone",
            "Japatul Valley — rural WUI area south of I-8",
        ],
        "elevation_range_ft": [1800, 2400],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Cedar Fire",
                "year": 2003,
                "acres": 273246,
                "details": (
                    "Largest and most destructive wildfire in San Diego County "
                    "history. Started in Cuyamaca Mountains, driven by Santa Ana "
                    "winds. Crossed I-8 and I-15. Burned into Alpine, Harbison "
                    "Canyon, Crest, Lake Jennings on Oct 26. 2,820 structures "
                    "destroyed (2,232 homes), 15 deaths. $1.3 billion in damages. "
                    "Sixth-deadliest and fourth-most destructive wildfire in "
                    "CA state history."
                ),
            },
            {
                "name": "Laguna Fire",
                "year": 1970,
                "acres": 175425,
                "details": (
                    "Major fire that burned from Laguna Mountains to outskirts of "
                    "El Cajon. 382 homes destroyed, 8 civilian deaths. Paralleled "
                    "I-8 from Greenfield to Alpine. Many areas burned in both the "
                    "Laguna Fire AND Cedar Fire 33 years later."
                ),
            },
            {
                "name": "West Fire",
                "year": 2018,
                "acres": 504,
                "details": (
                    "Burned 504 acres near Alpine, destroying 8 structures. "
                    "Fast-moving grass and brush fire demonstrating ongoing "
                    "threat to the community even from smaller fires."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Interstate 8 West (to El Cajon / San Diego)",
                "direction": "W",
                "lanes": 4,
                "bottleneck": (
                    "High-capacity freeway but subject to smoke obscuration "
                    "and fire crossing. On-ramps can bottleneck during mass "
                    "evacuation. 20 miles to El Cajon."
                ),
                "risk": (
                    "Cedar Fire crossed I-8. Wind-driven embers can spot across "
                    "the freeway. Smoke can reduce visibility to near-zero. "
                    "However, this is the highest-capacity evacuation route "
                    "of any mountain/backcountry community in the region."
                ),
            },
            {
                "route": "Interstate 8 East (to Pine Valley / El Centro)",
                "direction": "E",
                "lanes": 4,
                "bottleneck": (
                    "Leads deeper into mountain terrain initially, then to "
                    "desert. Less useful for evacuation as it goes toward "
                    "fire source area during east-wind-driven events."
                ),
                "risk": (
                    "During Cedar Fire, fire came from the east. This route "
                    "would lead directly into the fire. Only useful if fire "
                    "approaches from west/south."
                ),
            },
            {
                "route": "Alpine Boulevard / Tavern Road (local roads)",
                "direction": "Various",
                "lanes": 2,
                "bottleneck": (
                    "Local arterials connecting neighborhoods to I-8 on-ramps. "
                    "Can become gridlocked during mass evacuation. Many "
                    "residential streets are dead-end or cul-de-sac."
                ),
                "risk": (
                    "Neighborhoods south of I-8 (Japatul Valley, Harbison Canyon) "
                    "have limited connector roads. During Cedar Fire, residents "
                    "in these areas had extreme difficulty evacuating."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Santa Ana winds (NE/E) are the primary fire-weather driver. "
                "Hot, dry offshore flow with gusts 50-70 mph drives fire from "
                "the mountains/desert toward the coast. Cedar Fire was pushed "
                "by extreme Santa Ana conditions. Diurnal upslope/downslope "
                "winds on the I-8 escarpment."
            ),
            "critical_corridors": [
                "Japatul Valley — steep terrain south of I-8, heavy Cedar Fire impact",
                "Harbison Canyon — southwest approach, hundreds of homes lost in 2003",
                "Alpine Creek / Chocolate Creek drainages — WUI fire paths",
                "I-8 escarpment — fire runs upslope from Viejas area",
                "Cleveland National Forest interface — continuous fuel from forest to homes",
            ],
            "rate_of_spread_potential": (
                "Extreme during Santa Ana events. Cedar Fire burned over 200,000 "
                "acres in the first 48 hours, reaching speeds estimated at 40+ "
                "mph in grass/chaparral with 50-60 mph Santa Ana winds. Alpine-"
                "area losses occurred within hours of fire arrival."
            ),
            "spotting_distance": (
                "2-5 miles during extreme events. Cedar Fire's long-range spotting "
                "across I-8 and I-15 demonstrated multi-mile ember transport in "
                "Santa Ana conditions. Eucalyptus bark brands particularly dangerous."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Padre Dam Municipal Water District. Imported water via pipeline "
                "from San Diego County Water Authority. More reliable than isolated "
                "mountain communities but fire-hydrant spacing varies — rural "
                "areas south of I-8 have limited hydrant coverage."
            ),
            "power": (
                "SDG&E serves area. SDG&E's fire-hardening program has undergrounded "
                "some lines and installed covered conductors in VHFHSZ areas. "
                "However, SDG&E infrastructure failures caused both the 2007 "
                "Witch Creek and Rice fires. PSPS shutoffs during high-wind events."
            ),
            "communications": (
                "Better cell coverage than mountain communities due to proximity "
                "to San Diego metro. Some dead zones in canyons south of I-8. "
                "Reverse 911 and Wireless Emergency Alerts functional in most areas."
            ),
            "medical": (
                "No hospital in Alpine. Sharp Grossmont Hospital in La Mesa "
                "(~15 mi west) is the nearest major facility. East County "
                "ambulance response times can exceed 10 minutes to rural areas."
            ),
        },
        "demographics_risk_factors": {
            "population": 14696,
            "seasonal_variation": (
                "Moderate. Viejas Casino draws visitors. Some seasonal population "
                "increase from outdoor recreation in Cleveland National Forest. "
                "Generally a bedroom community for San Diego."
            ),
            "elderly_percentage": "est. 18-22%",
            "mobile_homes": (
                "Multiple mobile home parks, particularly along Alpine Boulevard "
                "and in Japatul Valley. Significant concentration of manufactured "
                "housing with limited fire resistance."
            ),
            "special_needs_facilities": (
                "Several assisted living facilities in the community. Mobile "
                "home parks with elderly residents. Japatul Valley and Harbison "
                "Canyon have isolated populations requiring longer evacuation times."
            ),
        },
    },

    "valley_center_ca": {
        "center": [33.2184, -117.0342],
        "terrain_notes": (
            "Rural agricultural community (pop 10,087, 2020 census) in inland "
            "San Diego County at ~1,300 ft elevation. Rolling terrain of chaparral-"
            "covered hills interspersed with avocado groves, citrus orchards, and "
            "ranchettes. The community is spread over 27.4 square miles of "
            "low-density WUI — houses on multi-acre lots surrounded by flammable "
            "vegetation. "
            "\n\n"
            "The Witch Creek Fire (Oct 21, 2007) — the second-largest fire of "
            "the devastating 2007 California wildfire season — burned 197,990 "
            "acres across San Diego County, destroying 1,125 homes and killing "
            "2 people. It started near Santa Ysabel when Santa Ana winds downed "
            "a power line. The fire broke out on the outskirts of Valley Center "
            "near Lake Wohlford, threatening to sweep through the community. "
            "500,000 people were evacuated countywide — the largest evacuation "
            "in California history. "
            "\n\n"
            "Valley Center's avocado groves create a paradoxical fire dynamic: "
            "irrigated groves can serve as fire breaks, but abandoned or drought-"
            "stressed groves become extreme fire hazards. Dead and dying avocado "
            "trees surrounded by dry brush along Old Julian Highway and Amigos "
            "Road have been identified as fire hazards by residents. When grove "
            "irrigation systems are destroyed by fire (as in 2007), the trees "
            "become fuel. "
            "\n\n"
            "Valley Center sits between multiple tribal reservations (Rincon, "
            "Pauma, La Jolla) adding jurisdictional complexity to fire response."
        ),
        "key_features": [
            "Witch Creek Fire (2007) corridor — 197,990 acres, 1,125 homes destroyed countywide",
            "Lake Wohlford — small reservoir, limited defensible space",
            "Avocado grove interface — irrigated groves as fire breaks; abandoned groves as fuel",
            "Low-density rural WUI — houses on multi-acre lots surrounded by chaparral",
            "Multiple tribal reservations (Rincon, Pauma, La Jolla) — jurisdictional complexity",
            "Rolling hills and steep drainages — complex fire terrain",
            "Valley Center Road — primary arterial, 2-lane rural road",
        ],
        "elevation_range_ft": [800, 2000],
        "wui_exposure": "high",
        "historical_fires": [
            {
                "name": "Witch Creek Fire",
                "year": 2007,
                "acres": 197990,
                "details": (
                    "Second-largest fire of 2007 CA wildfire season. Started "
                    "near Santa Ysabel from downed power line during Santa Ana "
                    "winds. Broke out on outskirts of Valley Center near Lake "
                    "Wohlford. 1,125 homes destroyed countywide, 2 deaths, "
                    "40 firefighters injured. 500,000 evacuated countywide. "
                    "Flames reached 80-100 ft high. Fire lapped around Valley "
                    "Center. Avocado grove irrigation destroyed."
                ),
            },
            {
                "name": "Valley Center Fire",
                "year": 2010,
                "acres": 200,
                "details": (
                    "Smaller fire near Valley Center demonstrating ongoing "
                    "ignition risk in chaparral terrain."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Valley Center Road South (to Escondido / I-15)",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Primary evacuation route — narrow, winding rural road. "
                    "15+ miles to I-15 at Escondido. Single lane each direction "
                    "with limited passing opportunities. Carries combined traffic "
                    "from the entire north valley."
                ),
                "risk": (
                    "Fire from northeast (Witch Creek direction) must be crossed "
                    "or outrun. Road passes through chaparral-covered hills with "
                    "limited defensible space."
                ),
            },
            {
                "route": "Cole Grade Road / Lilac Road (to I-15 north)",
                "direction": "W/SW",
                "lanes": 2,
                "bottleneck": (
                    "Alternate route to I-15 via Valley Parkway. Narrow, rural "
                    "road through agricultural/WUI terrain."
                ),
                "risk": (
                    "Fire approaching from any direction can cut these rural roads. "
                    "Minimal defensible space along corridors."
                ),
            },
            {
                "route": "Old Castle Road / Lake Wohlford Road (local roads)",
                "direction": "Various",
                "lanes": 2,
                "bottleneck": (
                    "Network of narrow rural roads connecting scattered rural "
                    "properties. Many dead-end roads and single-access canyons."
                ),
                "risk": (
                    "Many homes on private roads with single access. Dead-end "
                    "canyons can trap residents. Long driveways through brush "
                    "create evacuation hazards."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Santa Ana winds (NE/E) are the dominant fire-weather driver. "
                "The Witch Creek Fire was powered by Santa Ana winds that downed "
                "power lines. Hot, dry offshore flow with gusts 50-70 mph. "
                "Terrain channeling through valleys amplifies wind speeds."
            ),
            "critical_corridors": [
                "Lake Wohlford drainage — fire corridor from northeast",
                "San Marcos Creek drainage — fire path from southeast",
                "Old Julian Highway corridor — connects to fire-prone backcountry",
                "Paradise Mountain area — steep terrain with heavy chaparral",
            ],
            "rate_of_spread_potential": (
                "Very high to extreme in chaparral during Santa Ana events. "
                "Witch Creek Fire burned 197,990 acres total, racing across "
                "San Diego County at speeds exceeding 40 mph in grass/chaparral "
                "on flat terrain."
            ),
            "spotting_distance": (
                "1-3 miles in chaparral. Eucalyptus and palm tree brands "
                "can spot 2+ miles. Abandoned avocado grove debris creates "
                "additional spotting material."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Valley Center Municipal Water District. Imported water via "
                "San Diego County Water Authority aqueduct. Distribution system "
                "serves the town center but rural properties rely on private wells. "
                "Fire hydrant spacing inadequate in outlying areas."
            ),
            "power": (
                "SDG&E serves area. Power line failure caused the Witch Creek Fire. "
                "SDG&E has since invested heavily in fire-hardening, covered "
                "conductors, and sectionalizing. PSPS shutoffs during extreme "
                "fire weather."
            ),
            "communications": (
                "Moderate cell coverage in town center; poor coverage in canyons "
                "and rural areas. Valley Center community has active fire safe "
                "council and alert systems."
            ),
            "medical": (
                "No hospital. Nearest: Palomar Medical Center in Escondido "
                "(~15 mi south). Rural ambulance response times can exceed "
                "15 minutes to remote ranch properties."
            ),
        },
        "demographics_risk_factors": {
            "population": 10087,
            "seasonal_variation": (
                "Low. Primarily a permanent residential community with "
                "some agricultural workers. Limited tourism."
            ),
            "elderly_percentage": "est. 18-22%",
            "mobile_homes": (
                "Some mobile/manufactured homes on rural lots. Scattered "
                "throughout the community on agricultural parcels."
            ),
            "special_needs_facilities": (
                "Valley Center is home to several tribal casinos (Harrah's "
                "Resort Southern California at Rincon). Large event crowds "
                "at casino facilities create additional evacuation demand. "
                "Multiple tribal communities have their own emergency services."
            ),
        },
    },

    "fallbrook_ca": {
        "center": [33.3764, -117.2511],
        "terrain_notes": (
            "Sprawling agricultural community (pop 32,267, 2020 census) in "
            "northwestern San Diego County at ~680 ft elevation. Known as the "
            "'Avocado Capital of the World,' Fallbrook's landscape is a patchwork "
            "of avocado groves, citrus orchards, chaparral-covered hills, and "
            "residential development spread across 17.6 square miles. Bordered "
            "by Camp Pendleton Marine Corps Base to the west and rural backcountry "
            "to the east. "
            "\n\n"
            "The Rice Fire (Oct 22, 2007) was part of the devastating October "
            "2007 California wildfire season. Started by downed power lines in "
            "Rice Canyon south of Rainbow at ~4:15 AM, it burned 9,472 acres "
            "and destroyed 248 structures — one of the most destructive fires "
            "of the 2007 season relative to its acreage. 45,000 residents were "
            "evacuated, many directed through Camp Pendleton to the coast. "
            "\n\n"
            "During the same 2007 event, Camp Pendleton itself was battling "
            "multiple fires — the Horno Fire (6,000 acres) and Las Pulgas Fire "
            "(15,000 acres). The Camp Pendleton border both helps (provides "
            "fuel breaks in developed/maintained areas) and hurts (adds "
            "additional fire risk from base fires crossing into Fallbrook). "
            "\n\n"
            "Fallbrook's large, dispersed population makes coordinated "
            "evacuation challenging — 32,000+ people on rural roads."
        ),
        "key_features": [
            "Rice Fire (2007) corridor — 248 structures destroyed in 9,472 acres",
            "Camp Pendleton Marine Corps Base — western border, both buffer and fire source",
            "Avocado and citrus grove interface — irrigated groves as fire breaks when maintained",
            "Large dispersed population (32,000+) — evacuation coordination challenge",
            "Rice Canyon — fire ignition corridor south of Rainbow",
            "Mission Road / S-13 — primary arterial through community",
            "Santa Margarita River — northern boundary",
        ],
        "elevation_range_ft": [400, 1200],
        "wui_exposure": "high",
        "historical_fires": [
            {
                "name": "Rice Fire",
                "year": 2007,
                "acres": 9472,
                "details": (
                    "Started by downed power lines in Rice Canyon south of "
                    "Rainbow at ~4:15 AM on Oct 22, 2007. Despite relatively "
                    "small acreage, destroyed 248 structures — one of the most "
                    "destructive fires of the 2007 season. 45,000 residents "
                    "evacuated, many routed through Camp Pendleton. Fanned by "
                    "extreme Santa Ana winds."
                ),
            },
            {
                "name": "Camp Pendleton Fires (Horno/Las Pulgas)",
                "year": 2007,
                "acres": 21000,
                "details": (
                    "Concurrent with Rice Fire. Horno Fire burned 6,000 acres, "
                    "Las Pulgas Fire burned 15,000+ acres on Camp Pendleton. "
                    "Created complex multi-fire evacuation scenario where the "
                    "evacuation route (through Camp Pendleton) was also on fire."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Mission Road (S-13) South (to Oceanside / I-5)",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Primary evacuation route to coast. 2-lane road for 32,000+ "
                    "people. Passes through Bonsall before reaching I-76/I-5. "
                    "Can gridlock within minutes of mass evacuation order."
                ),
                "risk": (
                    "Fire from the east or northeast can cut the corridor at "
                    "multiple points. Rice Canyon fire spread directly across "
                    "this path."
                ),
            },
            {
                "route": "I-15 via Old Highway 395 / Reche Road",
                "direction": "E",
                "lanes": 2,
                "bottleneck": (
                    "Eastern escape route to I-15 freeway. Narrow rural roads "
                    "through the Pala area. 10+ miles to freeway."
                ),
                "risk": (
                    "Fire from the east (backcountry) threatens this route. "
                    "Passes through chaparral terrain."
                ),
            },
            {
                "route": "Camp Pendleton (emergency military base access)",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "During 2007, evacuees were routed through Camp Pendleton "
                    "to coastal I-5. Requires military cooperation and gate "
                    "access. Not guaranteed during all events."
                ),
                "risk": (
                    "Camp Pendleton fires (2007) demonstrated that the base "
                    "itself can be on fire during regional events. Evacuees "
                    "may be routed through active fire areas."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Santa Ana winds (NE/E) are the primary driver. The 2007 fires "
                "were all driven by extreme Santa Ana conditions. Wind funnel "
                "effects through Rice Canyon and the San Luis Rey River valley "
                "amplify wind speeds."
            ),
            "critical_corridors": [
                "Rice Canyon — 2007 ignition point, fire corridor from east",
                "San Luis Rey River valley — east-west fire path",
                "Camp Pendleton border — fire can spread in either direction",
                "De Luz Creek drainage — northeast approach to community",
                "Gopher Canyon — fire corridor from southeast",
            ],
            "rate_of_spread_potential": (
                "High to extreme in chaparral/grass during Santa Ana events. "
                "Rice Fire destroyed 248 structures in a few hours of morning "
                "wind-driven spread. Terrain is rolling to moderate slopes — "
                "less extreme than mountain communities but large fuel beds."
            ),
            "spotting_distance": (
                "1-3 miles in chaparral. Eucalyptus and avocado debris creates "
                "medium-range spotting. Brand transport across Camp Pendleton "
                "boundary is a concern."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Fallbrook Public Utility District. Imported water from San "
                "Diego County Water Authority plus local Rainbow Municipal "
                "Water District. Distribution system serves developed areas "
                "but rural properties may have limited hydrant access."
            ),
            "power": (
                "SDG&E serves area. Power line failure caused the Rice Fire. "
                "SDG&E has since invested in fire-hardening. PSPS shutoffs "
                "during extreme wind events can last days. Agricultural "
                "operations (refrigeration, irrigation pumps) impacted."
            ),
            "communications": (
                "Moderate cell coverage in developed areas. Rural hillsides "
                "and canyon areas have dead zones. North County Fire "
                "Protection District provides community alerts."
            ),
            "medical": (
                "No hospital in Fallbrook. Tri-City Medical Center in "
                "Oceanside (~18 mi south) is nearest. Camp Pendleton Naval "
                "Hospital is geographically closer but access is restricted "
                "to military personnel."
            ),
        },
        "demographics_risk_factors": {
            "population": 32267,
            "seasonal_variation": (
                "Low to moderate. Primarily a permanent agricultural and "
                "residential community. Some seasonal agricultural workers."
            ),
            "elderly_percentage": "est. 18-22%",
            "mobile_homes": (
                "Multiple mobile home parks throughout the community. "
                "Significant manufactured housing stock. Many agricultural "
                "worker housing units with minimal fire resistance."
            ),
            "special_needs_facilities": (
                "Several assisted living and senior care facilities. Large "
                "Hispanic/Latino population (45.2%) — language barriers can "
                "impede evacuation alert comprehension. Agricultural worker "
                "housing often in isolated, fire-prone locations."
            ),
        },
    },

    "pine_valley_ca": {
        "center": [32.8214, -116.5292],
        "terrain_notes": (
            "Small mountain community (pop 1,645, 2020 census) at 3,736 ft "
            "elevation in the Cuyamaca Mountains of southeastern San Diego "
            "County, along Interstate 8 approximately 45 miles east of San Diego. "
            "Surrounded by Cleveland National Forest in the Mountain Empire area. "
            "\n\n"
            "Pine Valley has a deep and devastating fire history. The Laguna Fire "
            "(Sep 26, 1970) burned 175,425 acres, killing 8 civilians and "
            "destroying 382 homes — at the time the most destructive wildfire in "
            "California history. The fire started from downed power lines in the "
            "Kitchen Creek area of the Laguna Mountains during a Santa Ana event "
            "with 40-60 mph winds. In the first 24 hours it burned 30 miles "
            "from Mount Laguna to the outskirts of El Cajon. The fire reached "
            "Interstate 8 and directly threatened Pine Valley by 1 PM on the "
            "first day. The fire then paralleled I-8 from the Greenfield off-"
            "ramp all the way to Alpine. "
            "\n\n"
            "More recently, the Valley Fire (Aug 22, 2022) started near Pine "
            "Creek Road and Noble Canyon north of Pine Valley off Interstate 8, "
            "and the Pass Fire (2023) burned 10 acres near Ribbonwood Road. "
            "\n\n"
            "The community sits in a mountain pass along I-8 — the major east-"
            "west corridor between San Diego and the Imperial Valley/Arizona. "
            "Pine Valley is the Pine Valley Fire Safe Council's focal area, "
            "and the 2019 CWPP identifies it as a Wildland-Urban Interface "
            "community with extreme fire risk."
        ),
        "key_features": [
            "Interstate 8 mountain pass corridor — high-elevation segment of major freeway",
            "Laguna Fire (1970) burn corridor — 175,425 acres, 382 homes, 8 deaths",
            "Cleveland National Forest — surrounds community on all sides",
            "Cuyamaca Mountains — rugged terrain to north and east",
            "Laguna Mountains — high plateau to the southeast",
            "Pine Creek and Noble Canyon — local drainages and fire corridors",
            "Kitchen Creek Road — connects to fire-prone Laguna Mountain area",
        ],
        "elevation_range_ft": [3500, 4000],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Laguna Fire",
                "year": 1970,
                "acres": 175425,
                "details": (
                    "Started from downed power lines in Kitchen Creek area "
                    "of Laguna Mountains. 40-60 mph Santa Ana winds. Burned "
                    "30 miles in first 24 hours from Mount Laguna to El Cajon. "
                    "382 homes destroyed, 8 civilian deaths. Threatened Pine "
                    "Valley directly. Paralleled I-8 from Greenfield to Alpine. "
                    "Was the most destructive CA wildfire at the time."
                ),
            },
            {
                "name": "Cedar Fire",
                "year": 2003,
                "acres": 273246,
                "details": (
                    "While centered on areas west of Pine Valley, the Cedar "
                    "Fire's eastern flank burned through the Cuyamaca Mountains "
                    "near Pine Valley. The fire started in the mountains to the "
                    "north-northwest and burned through the region's fuel beds."
                ),
            },
            {
                "name": "Valley Fire",
                "year": 2022,
                "acres": 4000,
                "details": (
                    "Started near Pine Creek Road and Noble Canyon north of "
                    "Pine Valley off I-8 on Aug 22, 2022. Burned through "
                    "Cleveland National Forest terrain."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Interstate 8 West (to Alpine / El Cajon / San Diego)",
                "direction": "W",
                "lanes": 4,
                "bottleneck": (
                    "High-capacity freeway descent from 3,736 ft to sea level. "
                    "Long, steep grade with tight curves. Smoke can obscure "
                    "visibility. 45 miles to San Diego."
                ),
                "risk": (
                    "Laguna Fire (1970) paralleled I-8 from Pine Valley area "
                    "westward. Fire approaching from east rides wind directly "
                    "along the freeway corridor. Steep terrain adjacent to "
                    "freeway allows fire to burn right to the road edge."
                ),
            },
            {
                "route": "Interstate 8 East (to Jacumba / El Centro)",
                "direction": "E",
                "lanes": 4,
                "bottleneck": (
                    "Climbs to ~4,200 ft at Laguna Summit before descending "
                    "to the desert floor. 60+ miles to El Centro. Remote with "
                    "limited services."
                ),
                "risk": (
                    "Route ascends through fire-prone Laguna Mountains. Kitchen "
                    "Creek area (where Laguna Fire started) is along this route. "
                    "Fire from east/southeast can cut this corridor."
                ),
            },
            {
                "route": "Pine Valley Road / Old Highway 80",
                "direction": "Various",
                "lanes": 2,
                "bottleneck": (
                    "Local roads connecting to I-8. Limited alternative routing. "
                    "Some local roads are dead-end."
                ),
                "risk": (
                    "Narrow roads through timber and chaparral. Limited "
                    "defensible space. Only connect back to I-8."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Santa Ana winds (NE/E) dominate fire weather. 40-60 mph winds "
                "during the Laguna Fire made aircraft firefighting impossible. "
                "I-8 corridor acts as a wind tunnel through the mountain pass. "
                "Fire weather often accompanied by single-digit humidity."
            ),
            "critical_corridors": [
                "Kitchen Creek drainage — Laguna Fire origin area to southeast",
                "Pine Creek / Noble Canyon — north approach, 2022 Valley Fire",
                "I-8 corridor — wind tunnel through mountain pass",
                "Cuyamaca Rancho State Park drainage — north/northeast approach",
                "Laguna Mountain escarpment — east approach with extreme elevation gain",
            ],
            "rate_of_spread_potential": (
                "Extreme during Santa Ana events. Laguna Fire burned 30 miles in "
                "24 hours through this terrain. Dense chaparral and timber "
                "support high-intensity fire. Steep terrain multiplies spread "
                "rates. Mountain pass wind acceleration effect."
            ),
            "spotting_distance": (
                "2-5 miles during extreme wind events. Laguna Fire demonstrated "
                "multi-mile spot-fire establishment. Terrain creates strong "
                "updrafts that loft brands."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Pine Valley Mutual Water Company. Small local system with "
                "limited storage. No connection to San Diego County Water "
                "Authority main aqueduct. Extended firefighting demand would "
                "exhaust supply."
            ),
            "power": (
                "SDG&E serves area. The Laguna Fire was caused by SDG&E power "
                "line failure. Overhead lines through forested terrain remain "
                "vulnerable. PSPS shutoffs during wind events."
            ),
            "communications": (
                "Limited cell coverage in mountain terrain. Some dead zones "
                "in drainages and canyons. Pine Valley Fire Safe Council "
                "maintains community notification systems."
            ),
            "medical": (
                "No hospital or clinic. Nearest hospital: Sharp Grossmont in "
                "La Mesa (~40 mi west, 45-60 min via I-8). Volunteer fire "
                "department provides basic EMS. Remote location means extended "
                "response times for advanced medical care."
            ),
        },
        "demographics_risk_factors": {
            "population": 1645,
            "seasonal_variation": (
                "Moderate. Weekend recreation traffic (hiking, camping in "
                "Cleveland National Forest). I-8 travelers sometimes stop "
                "in Pine Valley. Summer camping season increases area population."
            ),
            "elderly_percentage": "est. 18-22%",
            "mobile_homes": (
                "Some mobile/manufactured homes on rural lots. Community is "
                "primarily single-family homes on larger parcels. Many older "
                "wood-frame structures."
            ),
            "special_needs_facilities": (
                "None. Very small, isolated mountain community. Elderly residents "
                "living alone in remote areas face elevated evacuation risk."
            ),
        },
    },

    # =========================================================================
    # SANTA BARBARA COAST
    # =========================================================================

    "montecito_ca": {
        "center": [34.4367, -119.6321],
        "terrain_notes": (
            "Affluent unincorporated community (pop 8,638, 2020 census) in "
            "Santa Barbara County, built on a series of alluvial fans at the "
            "base of the Santa Ynez Mountains, extending from the mountain "
            "front down to the Pacific Ocean. Elevation ranges from sea level "
            "to ~1,000 ft at the mountain base, with the Santa Ynez range "
            "rising steeply to 4,000+ ft directly behind the community. "
            "\n\n"
            "Montecito experienced a catastrophic fire-to-flood disaster "
            "sequence in 2017-2018 that killed 25 people total and stands as "
            "one of the most devastating compound-hazard events in California "
            "history. The Thomas Fire (Dec 4, 2017 - Jan 12, 2018) burned "
            "281,893 acres — the largest wildfire in modern California history "
            "at the time — destroying 1,063 structures and killing 2 people "
            "(1 civilian, 1 firefighter). The fire burned through the Santa "
            "Ynez Mountains directly above Montecito, stripping vegetation from "
            "steep slopes. "
            "\n\n"
            "Then on January 9, 2018 — just weeks after the fire — intense "
            "rainfall (0.5 inches in 5 minutes at 3:30 AM) triggered "
            "catastrophic debris flows from the burned mountain slopes. Walls "
            "of mud, boulders, and debris up to 15 ft high traveling at 20 mph "
            "roared down Montecito Creek, San Ysidro Creek, Buena Vista Creek, "
            "and Romero Creek into the sleeping community. The USGS documented "
            "~680,000 cubic meters of mobilized sediment at velocities up to "
            "4 m/s. 23 PEOPLE WERE KILLED, 150+ hospitalized, 100+ homes "
            "destroyed, 300+ damaged. $177M+ in property damage, $7M in "
            "emergency response, $43M in cleanup. "
            "\n\n"
            "Four sediment-retention basins protect the community: Cold Spring "
            "(1964), Montecito (2002), San Ysidro (1964), and Romero (1971). "
            "All four were overwhelmed in the 2018 event. The community sits on "
            "alluvial fans formed by exactly this process over millennia — every "
            "home is built on ancient debris-flow deposits."
        ),
        "key_features": [
            "Thomas Fire (2017) burn scar — 281,893 acres including slopes above community",
            "January 9, 2018 debris flows — 23 killed, 100+ homes destroyed",
            "Santa Ynez Mountains — 4,000+ ft range rising directly behind community",
            "Five major debris-flow channels: Montecito, San Ysidro, Buena Vista, Romero, Cold Spring Creeks",
            "Four sediment-retention basins — all overwhelmed in 2018",
            "Alluvial fan geology — entire community built on historic debris-flow deposits",
            "US 101 corridor — primary east-west evacuation route",
            "Extreme WUI with luxury homes pressed against mountain front",
        ],
        "elevation_range_ft": [20, 1000],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Thomas Fire",
                "year": 2017,
                "acres": 281893,
                "details": (
                    "Largest wildfire in modern CA history at the time. Started "
                    "Dec 4 near Thomas Aquinas College, burned through Santa Ynez "
                    "Mountains above Montecito and Carpinteria. 1,063 structures "
                    "destroyed, 280 damaged. 2 deaths (1 civilian, 1 firefighter). "
                    "$2.2 billion in total damages. Fire stripped vegetation from "
                    "steep mountain slopes, setting up the catastrophic January 9 "
                    "debris flows."
                ),
            },
            {
                "name": "Montecito Debris Flows (post-fire)",
                "year": 2018,
                "acres": 0,
                "details": (
                    "NOT a fire but a direct consequence of Thomas Fire burn scar. "
                    "Jan 9, 2018: intense rain (0.5 in/5min) at 3:30 AM triggered "
                    "debris flows from burned slopes. 680,000 m3 of sediment "
                    "mobilized. Mud/boulder walls 15 ft high at 20 mph. 23 KILLED, "
                    "150+ hospitalized, 100+ homes destroyed, 300+ damaged. $177M+ "
                    "property damage. All four sediment basins overwhelmed. "
                    "Demonstrates that fire risk extends far beyond the burn itself."
                ),
            },
            {
                "name": "Jesusita Fire",
                "year": 2009,
                "acres": 8733,
                "details": (
                    "Burned 8,733 acres in the Santa Barbara front country. "
                    "80 homes destroyed, 15 damaged. Forced evacuation of "
                    "Montecito and nearby communities. Demonstrated recurring "
                    "threat from the Santa Ynez Mountains."
                ),
            },
            {
                "name": "Tea Fire",
                "year": 2008,
                "acres": 1940,
                "details": (
                    "Burned 1,940 acres in the foothills above Montecito. "
                    "210 homes destroyed including structures at Westmont "
                    "College. Sundowner winds drove fire downslope."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "US 101 South/East (to Ventura)",
                "direction": "SE",
                "lanes": 4,
                "bottleneck": (
                    "Primary evacuation route. High-capacity freeway but "
                    "subject to debris flow closure (was buried in 2018) "
                    "and smoke obscuration during fire events."
                ),
                "risk": (
                    "Debris flows in 2018 closed US 101 for weeks. Fire "
                    "approaching from east can create smoke/ember hazard on "
                    "freeway. Both 2018 debris flows and 2017 fire caused "
                    "prolonged US 101 closures."
                ),
            },
            {
                "route": "US 101 North/West (to Santa Barbara)",
                "direction": "NW",
                "lanes": 4,
                "bottleneck": (
                    "Short distance (~7 mi) to Santa Barbara. High capacity "
                    "but Montecito is between fire and Santa Barbara — "
                    "evacuation may flow into the city."
                ),
                "risk": (
                    "Fire from mountains above can cut across US 101 in "
                    "multiple locations. Thomas Fire approached from east, "
                    "making westward evacuation viable, but Jesusita/Tea "
                    "Fire came from directly above."
                ),
            },
            {
                "route": "San Ysidro Road / Hot Springs Road (local arterials)",
                "direction": "Various",
                "lanes": 2,
                "bottleneck": (
                    "Local roads connecting hillside neighborhoods to US 101. "
                    "Narrow, winding, with limited capacity. Many hillside "
                    "homes on private roads."
                ),
                "risk": (
                    "Hillside homes closest to the mountains have the longest "
                    "evacuation times and highest exposure. Debris flows in "
                    "2018 destroyed local road networks. Some roads were "
                    "buried under feet of mud."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Sundowner winds — hot, dry downslope winds unique to the Santa "
                "Barbara area. Unlike Santa Ana winds, sundowners blow from north "
                "to south (mountain to coast), strongest at sunset. They heat and "
                "dry as they descend, creating gale-force hot, dry conditions "
                "that make firefighting impossible. The Thomas Fire was driven "
                "by the 'strongest and longest duration Santa Ana wind event' of "
                "the season per NWS. Standard Santa Ana conditions also affect "
                "the area."
            ),
            "critical_corridors": [
                "Montecito Creek — primary debris/fire corridor from mountains to coast",
                "San Ysidro Creek — steep canyon directly into community",
                "Buena Vista Creek — another steep drainage into residential areas",
                "Romero Creek — eastern debris/fire corridor",
                "Cold Spring Creek — western approach",
                "Santa Ynez Mountain front — entire mountain face above community",
            ],
            "rate_of_spread_potential": (
                "Extreme during sundowner or Santa Ana events. Thomas Fire burned "
                "281,893 acres over 39 days but had explosive runs of thousands "
                "of acres per hour during wind events. Steep chaparral slopes "
                "above Montecito create rapid downslope fire runs."
            ),
            "spotting_distance": (
                "1-3 miles. Steep downslope terrain and strong winds can carry "
                "brands from mountain ridgeline into community. During Thomas "
                "Fire, embers traveled significant distances ahead of the fire "
                "front."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Montecito Water District. 2018 debris flows created 300+ leaks "
                "in the distribution system. Infrastructure is built on alluvial "
                "fans subject to debris-flow damage. Four sediment basins (Cold "
                "Spring 1964, Montecito 2002, San Ysidro 1964, Romero 1971) were "
                "all overwhelmed in 2018."
            ),
            "power": (
                "SCE serves area. Rolling blackouts hit Montecito during Thomas "
                "Fire (starting 1:40 AM Dec 10). Overhead lines through foothill "
                "terrain are vulnerable. Power loss during combined fire/debris "
                "flow events."
            ),
            "communications": (
                "Generally good cell coverage in the developed coastal area. "
                "However, power outages during events disable cell towers. "
                "During the 2018 debris flows at 3:30 AM, many residents were "
                "asleep and did not receive or heed evacuation warnings."
            ),
            "medical": (
                "Cottage Hospital in Santa Barbara (~7 mi). During the 2018 "
                "debris flows, US 101 closure made hospital access from the "
                "south impossible. Helicopters required for emergency transport. "
                "150+ people hospitalized in the debris flow event."
            ),
        },
        "demographics_risk_factors": {
            "population": 8638,
            "seasonal_variation": (
                "Moderate. Tourist destination with resort hotels (Four Seasons, "
                "San Ysidro Ranch). Celebrity residents. Weekend visitors. "
                "Population relatively stable year-round."
            ),
            "elderly_percentage": "est. 25-30% (affluent retirement community)",
            "mobile_homes": (
                "Negligible. Montecito is among the wealthiest communities in "
                "the US (median home value well over $3M). However, high-value "
                "wood-frame estates in the foothills are highly vulnerable to "
                "fire and debris flows."
            ),
            "special_needs_facilities": (
                "Limited institutional facilities. Affluent elderly population "
                "living in large hillside estates may have difficulty with "
                "self-evacuation. Multiple celebrity estates with private "
                "access roads."
            ),
        },
    },

    "carpinteria_ca": {
        "center": [34.3989, -119.5185],
        "terrain_notes": (
            "Small coastal city (pop 13,242, 2020 census) in Santa Barbara "
            "County, ~12 miles east of Santa Barbara. Sits on a narrow coastal "
            "plain between the Santa Ynez Mountains (rising to 4,000+ ft "
            "directly behind the city) and the Pacific Ocean. The mountain-to-"
            "coast distance is extremely compressed — steep chaparral slopes "
            "transition directly to residential neighborhoods with minimal "
            "buffer. Elevation ranges from sea level to ~200 ft in the "
            "developed area. "
            "\n\n"
            "The Thomas Fire (Dec 2017) directly threatened Carpinteria as it "
            "burned westward through Santa Barbara County along the Santa Ynez "
            "Mountain front. On December 10, mandatory evacuations were issued "
            "for large areas of Carpinteria, Summerland, and Montecito at 6 AM "
            "as the fire crept west along mountainsides. Firefighters "
            "concentrated on protecting Carpinteria and Montecito as the fire "
            "burned in difficult foothills terrain. Rolling blackouts hit "
            "Carpinteria starting 1:40 AM that morning. "
            "\n\n"
            "Like Montecito, Carpinteria is built on alluvial fans and is "
            "vulnerable to post-fire debris flows from the burned mountain "
            "slopes. Carpinteria Creek, Santa Monica Creek, and Rincon Creek "
            "carry debris from the mountains through the community."
        ),
        "key_features": [
            "Thomas Fire (2017) threatened — mandatory evacuations Dec 10",
            "Santa Ynez Mountains — 4,000+ ft range immediately behind city",
            "Extremely compressed mountain-to-coast terrain",
            "US 101 corridor — primary east-west route through city",
            "Carpinteria Creek, Santa Monica Creek — potential debris flow channels",
            "Rincon Point — eastern boundary, coastal access",
            "Carpinteria State Beach — potential shelter area during hillside fires",
            "Agricultural greenhouse district — avocado groves on foothills",
        ],
        "elevation_range_ft": [0, 200],
        "wui_exposure": "high",
        "historical_fires": [
            {
                "name": "Thomas Fire",
                "year": 2017,
                "acres": 281893,
                "details": (
                    "Largest fire in modern CA history at the time. Burned along "
                    "Santa Ynez Mountain front directly above Carpinteria. "
                    "Mandatory evacuations Dec 10 for Carpinteria, Summerland, "
                    "Montecito. Rolling blackouts hit at 1:40 AM. Firefighters "
                    "concentrated on structure protection. Santa Ana winds "
                    "described as 'strongest and longest duration event' of season. "
                    "Carpinteria ultimately spared from direct structure loss but "
                    "fire burned to the community's doorstep."
                ),
            },
            {
                "name": "Sherpa Fire",
                "year": 2016,
                "acres": 7474,
                "details": (
                    "Burned 7,474 acres in the mountains west of Carpinteria "
                    "near Refugio State Beach. Demonstrated ongoing fire threat "
                    "along the Santa Barbara south coast mountain front."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "US 101 North/West (to Santa Barbara)",
                "direction": "NW",
                "lanes": 4,
                "bottleneck": (
                    "Primary evacuation route. High-capacity freeway but "
                    "subject to smoke obscuration and potential fire crossing "
                    "during extreme events."
                ),
                "risk": (
                    "Fire from mountains above can approach US 101. During "
                    "Thomas Fire, fire burned in foothills near the freeway "
                    "corridor. Evacuees from Carpinteria, Summerland, and "
                    "Montecito all use the same stretch of 101."
                ),
            },
            {
                "route": "US 101 South/East (to Ventura)",
                "direction": "SE",
                "lanes": 4,
                "bottleneck": (
                    "Eastbound escape to Ventura (~20 mi). Route runs along "
                    "narrow Rincon coast between mountains and ocean. Subject "
                    "to rockslide, mudslide, and fire closure."
                ),
                "risk": (
                    "Thomas Fire threatened this route. Rincon coast section "
                    "has mountains directly adjacent to the freeway. Post-fire "
                    "debris flows can close the corridor (as happened in "
                    "Montecito)."
                ),
            },
            {
                "route": "Casitas Pass Road / Rincon Creek Road (local)",
                "direction": "N/E",
                "lanes": 2,
                "bottleneck": (
                    "Local roads connecting hillside areas to US 101. Narrow, "
                    "limited capacity. Some foothill neighborhoods have single "
                    "access roads."
                ),
                "risk": (
                    "Fire from mountains directly threatens these foothill "
                    "connector roads. Limited defensible space."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Sundowner winds (north-to-south downslope) are the primary "
                "fire-weather threat — unique to the Santa Barbara area. "
                "These hot, dry winds blow from the mountains to the coast "
                "and are strongest in late spring through early winter. Santa "
                "Ana winds also affect the area but sundowners are the "
                "distinctive local hazard."
            ),
            "critical_corridors": [
                "Carpinteria Creek — mountain-to-coast debris/fire corridor",
                "Santa Monica Creek — steep drainage into residential areas",
                "Rincon Creek — eastern fire/debris corridor",
                "Santa Ynez Mountain front — entire steep face above community",
                "Gobernador Creek — foothill approach from northwest",
            ],
            "rate_of_spread_potential": (
                "High to extreme during wind events. Steep chaparral slopes "
                "directly above the city create rapid downslope fire runs. "
                "The Thomas Fire had 'extreme growth potential' designation "
                "as it approached Carpinteria."
            ),
            "spotting_distance": (
                "1-2 miles. Downslope winds can carry brands from mountain "
                "ridgeline into the community. Short mountain-to-coast "
                "distance means ember attack can occur from fires that "
                "appear distant on the ridgeline."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Carpinteria Valley Water District. Combination of local "
                "groundwater and imported water from Cachuma Reservoir. "
                "System is reliable but vulnerable to debris-flow damage "
                "(as demonstrated in nearby Montecito)."
            ),
            "power": (
                "SCE serves area. Rolling blackouts during Thomas Fire (Dec 10). "
                "Overhead lines through foothills are vulnerable. PSPS shutoffs "
                "during wind events."
            ),
            "communications": (
                "Generally good cell coverage in the developed coastal area. "
                "Power outages during events can disable towers. Santa Barbara "
                "County alert systems functional."
            ),
            "medical": (
                "No hospital in Carpinteria. Cottage Hospital in Santa Barbara "
                "(~12 mi west). Santa Barbara Cottage Hospital is Level I "
                "trauma center. US 101 closure would impede access."
            ),
        },
        "demographics_risk_factors": {
            "population": 13242,
            "seasonal_variation": (
                "Moderate. Beach town with summer tourist season. Carpinteria "
                "State Beach draws visitors. Some seasonal agricultural workers "
                "in greenhouse/nursery industry."
            ),
            "elderly_percentage": "est. 18-22% (median age 44.7)",
            "mobile_homes": (
                "Several mobile home parks near the coast. Some are in "
                "tsunami inundation zones as well, creating compound hazard. "
                "Agricultural worker housing in some areas."
            ),
            "special_needs_facilities": (
                "Limited. Small city with some assisted living. Large Hispanic/ "
                "Latino population (43.4%) — language barriers for evacuation "
                "alerts. 22.9% foreign-born population."
            ),
        },
    },

    # =========================================================================
    # TEHACHAPI / KERN COUNTY
    # =========================================================================

    "frazier_park_ca": {
        "center": [34.8228, -118.9448],
        "terrain_notes": (
            "Small mountain village (pop 2,592, 2020 census) at 4,639 ft "
            "elevation in the San Emigdio Mountains of southwestern Kern County, "
            "adjacent to Interstate 5 at the Tejon Pass. Part of the Mountain "
            "Communities of the Tejon Pass, which also includes Lebec, Lake of "
            "the Woods, and Pine Mountain Club. "
            "\n\n"
            "Frazier Park sits in one of the most extreme wind corridors in "
            "Southern California. The Tejon Pass / I-5 corridor funnels air "
            "between the Tehachapi Mountains and the San Emigdio Range, creating "
            "winds that routinely topple trucks on I-5 and create extreme fire "
            "weather conditions. Santa Ana-type northeast winds are amplified "
            "by the topographic constriction, producing sustained winds of "
            "50-70+ mph during major events. The Grapevine (I-5 grade) is one "
            "of the windiest locations in California. "
            "\n\n"
            "The community is surrounded by Los Padres National Forest and the "
            "Tehachapi Mountains — dense chaparral and mixed-conifer forest on "
            "steep mountain slopes. Recent fires include the Frazier Fire (2025, "
            "96 acres with wind-driven flare-ups), the Grand Fire (near Gorman, "
            "west of I-5), and the Tecuya Fire on nearby Tecuya Mountain. "
            "\n\n"
            "The I-5 corridor provides high-capacity evacuation infrastructure "
            "but is itself subject to closure during extreme wind events (truck "
            "tipping) and fire crossing."
        ),
        "key_features": [
            "Tejon Pass / I-5 wind funnel — among the windiest corridors in Southern CA",
            "San Emigdio Mountains — steep, brush-covered terrain on all sides",
            "Los Padres National Forest — dense chaparral and conifer forest",
            "I-5 Grapevine Grade — major freeway but subject to wind/fire closures",
            "Frazier Mountain — namesake peak, fire corridor to south",
            "Lockwood Valley — rural area to the west with limited access",
            "Tehachapi Mountains — northern backdrop, wind generation zone",
        ],
        "elevation_range_ft": [4400, 5000],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Frazier Fire",
                "year": 2025,
                "acres": 96,
                "details": (
                    "Burned 96 acres near Frazier Park. High-wind flare-up "
                    "caused rapid spread despite small size. Demonstrates the "
                    "extreme wind conditions that amplify fire behavior in "
                    "the Tejon Pass corridor."
                ),
            },
            {
                "name": "Grand Fire",
                "year": 2021,
                "acres": 500,
                "details": (
                    "Burned west of I-5 near Gorman in light grass and medium "
                    "brush. Threatened structures near Frazier Park area. "
                    "Spread rapidly in wind-driven conditions."
                ),
            },
            {
                "name": "Tecuya Fire",
                "year": 2020,
                "acres": 20,
                "details": (
                    "Burned on Tecuya Mountain in the San Emigdio Mountains "
                    "near Frazier Park. Moderate rate of spread. Kern County "
                    "Fire Department response."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Interstate 5 South (The Grapevine — to Los Angeles)",
                "direction": "S",
                "lanes": 4,
                "bottleneck": (
                    "Major freeway but the Grapevine grade is routinely closed "
                    "during extreme wind, snow, or fire events. Steep, winding "
                    "grade from 4,000+ ft to valley floor. Wind speeds can "
                    "make driving dangerous — trucks topple regularly."
                ),
                "risk": (
                    "Fire crossing I-5 has occurred in this corridor. Extreme "
                    "winds make the grade treacherous. Combined evacuation with "
                    "Lebec, Gorman, and regular I-5 traffic creates massive "
                    "congestion potential."
                ),
            },
            {
                "route": "Interstate 5 North (to Bakersfield / Central Valley)",
                "direction": "N",
                "lanes": 4,
                "bottleneck": (
                    "High-capacity route to Central Valley. Less steep than "
                    "southbound but still subject to wind closures. 45 miles "
                    "to Bakersfield."
                ),
                "risk": (
                    "Generally the safer direction during fire events as it "
                    "leads away from the mountain interface. Wind-driven fire "
                    "from the south/southwest is the primary threat."
                ),
            },
            {
                "route": "Frazier Mountain Park Road / Lockwood Valley Road",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "Narrow rural road heading west into Lockwood Valley and "
                    "eventually connecting to Highway 33. Remote, limited "
                    "services, very long detour."
                ),
                "risk": (
                    "Passes through dense Los Padres National Forest. Fire "
                    "from the south or west can cut this route. Dead-end "
                    "for evacuees who miss the turn to Hwy 33."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "EXTREME WIND CORRIDOR. The Tejon Pass funnels northeast "
                "winds (Santa Ana analog) between the Tehachapi and San "
                "Emigdio ranges, producing sustained winds of 50-70+ mph. "
                "The I-5 Grapevine corridor is one of the windiest locations "
                "in California. These winds create fire weather that can drive "
                "fires at extraordinary speeds. High-wind events also create "
                "sundowner-type heating on the south-facing slopes above the "
                "community."
            ),
            "critical_corridors": [
                "I-5 / Grapevine Grade — wind tunnel through the pass",
                "Frazier Mountain south face — steep terrain directly above community",
                "Lockwood Valley — wind corridor from the west",
                "Cuddy Canyon — drainage funneling wind and fire from southeast",
                "San Emigdio Creek — drainage connecting to agricultural valley below",
            ],
            "rate_of_spread_potential": (
                "Extreme to catastrophic during high-wind events. The unique "
                "wind acceleration through the Tejon Pass can produce fire "
                "behavior exceeding even Santa Ana-driven events in other "
                "SoCal locations. Short, flashy chaparral fuels combined with "
                "70+ mph winds create extreme ROS."
            ),
            "spotting_distance": (
                "2-5 miles during extreme wind events. The exceptional wind "
                "speeds in the Tejon corridor can carry brands extraordinary "
                "distances. Spot fires can establish miles ahead of the main "
                "fire front."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Small local water district. Limited storage for prolonged "
                "firefighting. No connection to major metropolitan systems. "
                "Mountain springs and wells supplemented by imported water."
            ),
            "power": (
                "SCE serves area. Overhead lines through mountain terrain. "
                "Extreme winds regularly damage power infrastructure — the "
                "Tejon Pass is among the highest wind-damage areas for utility "
                "infrastructure in Southern CA. PSPS shutoffs frequent during "
                "wind events."
            ),
            "communications": (
                "Limited cell coverage in mountain terrain. Cell towers on "
                "exposed ridgelines are vulnerable to wind damage. Community "
                "relies on local radio, scanner monitoring, and community "
                "notification systems."
            ),
            "medical": (
                "No hospital. Nearest major hospital: Kern Medical in "
                "Bakersfield (~45 mi north) or Henry Mayo Newhall Hospital "
                "in Santa Clarita (~40 mi south, over the Grapevine). "
                "Ambulance response from Kern County Fire Station can be "
                "delayed during wind events that close I-5."
            ),
        },
        "demographics_risk_factors": {
            "population": 2592,
            "seasonal_variation": (
                "Moderate. Some seasonal visitors for hiking, camping in Los "
                "Padres National Forest, and skiing at Mt. Pinos. Weekend "
                "traffic on I-5 passes through the area but most do not stop."
            ),
            "elderly_percentage": "est. 18-22%",
            "mobile_homes": (
                "Multiple mobile/manufactured homes. Mountain community with "
                "affordable housing stock that includes older mobile homes "
                "vulnerable to wind and fire."
            ),
            "special_needs_facilities": (
                "None in the immediate community. Isolated mountain location "
                "means extended transport times for special-needs evacuees."
            ),
        },
    },

    "pine_mountain_club_ca": {
        "center": [34.8464, -119.1496],
        "terrain_notes": (
            "Private, gated mountain community (pop 2,422, 2020 census) at "
            "4,900-6,400 ft elevation in the San Emigdio Mountains of "
            "southwestern Kern County. The community sits in a deep valley "
            "on the San Andreas Fault, surrounded by Los Padres National Forest. "
            "\n\n"
            "Pine Mountain Club has a SINGLE PRIMARY ACCESS ROAD — Mil Potrero "
            "Highway, a winding, steep 6.5-mile road connecting the community "
            "to Highway 166 and eventually I-5. This is arguably the most "
            "evacuation-constrained gated community in California. If fire "
            "blocks Mil Potrero Highway, the entire population is trapped "
            "in a mountain valley with no alternative exit. "
            "\n\n"
            "The community is a private HOA with gates, adding potential delay "
            "to emergency vehicle access and evacuation flow. Fire hazard "
            "reduction is required by early June each year, with fire department "
            "inspections and $500 citations for violations — indicating the "
            "community recognizes the extreme risk. "
            "\n\n"
            "The French Fire (2021) burned 26,535 acres in the Kern River area "
            "and placed Pine Mountain Club communities under evacuation warning. "
            "A 2021 fire within PMC itself ('We could have lost everything today' "
            "— Mountain Enterprise headline) demonstrated the direct threat. "
            "The community is surrounded by heavy chaparral and mixed-conifer "
            "forest in Los Padres National Forest, with decades of fuel "
            "accumulation."
        ),
        "key_features": [
            "SINGLE ACCESS ROAD — Mil Potrero Highway (6.5 mi, winding, steep)",
            "Private gated community — HOA controlled access",
            "San Emigdio Mountains valley — deep mountain setting",
            "San Andreas Fault — community built directly on the fault",
            "Los Padres National Forest — surrounds community on all sides",
            "Dense chaparral and mixed-conifer forest with heavy fuel loading",
            "Mandatory fire hazard reduction — $500 citations for violations",
        ],
        "elevation_range_ft": [4900, 6400],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "French Fire",
                "year": 2021,
                "acres": 26535,
                "details": (
                    "Burned 26,535 acres near Shirley Meadows west of Lake "
                    "Isabella. Pine Mountain Club communities placed under "
                    "evacuation warning. 1,600+ firefighters deployed. "
                    "Evacuation warnings covered Glennville, Linns Valley, "
                    "Pine Mountain, Badger Canyon, Poso Flat. Contained "
                    "Oct 24, 2021."
                ),
            },
            {
                "name": "PMC Structure Fire (wildland threat)",
                "year": 2021,
                "acres": None,
                "details": (
                    "Fire within Pine Mountain Club itself. Mountain Enterprise "
                    "headline: 'We could have lost everything today.' Demonstrated "
                    "that the gated community faces direct ignition risk, not just "
                    "wildland fire approach."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Mil Potrero Highway (to Hwy 166 / I-5)",
                "direction": "E/SE",
                "lanes": 2,
                "bottleneck": (
                    "THE ONLY EXIT. 6.5-mile winding, steep mountain road. "
                    "Gate at community entrance adds delay. Single lane each "
                    "direction with limited pullover space. Improved at cost "
                    "of ~$1M but still narrow and winding."
                ),
                "risk": (
                    "CATASTROPHIC SINGLE POINT OF FAILURE. Any fire along this "
                    "6.5-mile corridor traps the entire community of 2,400+ "
                    "people (plus visitors). Chaparral and forest press directly "
                    "against the road. No alternative exit exists. This is one "
                    "of the most dangerous evacuation scenarios in California."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Complex mountain winds in the San Emigdio Range. Northeast "
                "winds (Santa Ana analog) funnel through the I-5 / Tejon Pass "
                "corridor to the east. Sundowner-type winds from the north "
                "descend into the valley. The deep valley setting can trap "
                "smoke and create temperature inversions, but wind events "
                "break the inversion and drive extreme fire behavior."
            ),
            "critical_corridors": [
                "Mil Potrero Highway corridor — only access road, also a fire corridor",
                "Mil Potrero Creek drainage — valley floor fire/smoke path",
                "San Emigdio Mountains south face — steep terrain above community",
                "Cuddy Valley approach — northeast wind corridor from Frazier Park area",
                "Los Padres National Forest interface — continuous fuel on all sides",
            ],
            "rate_of_spread_potential": (
                "High to extreme during wind events. Dense fuel loads combined "
                "with steep terrain create aggressive fire behavior. The valley "
                "setting can channelize fire and wind. Crown fire in conifer "
                "stands is possible at higher elevations."
            ),
            "spotting_distance": (
                "1-2 miles. Mountain terrain creates updrafts that loft brands. "
                "The narrow valley means spots on either slope can quickly "
                "coalesce into a valley-wide fire."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "PMC community water system. Local wells and small reservoirs. "
                "Very limited storage capacity for prolonged firefighting. "
                "No connection to external water systems. Drought reduces "
                "groundwater availability."
            ),
            "power": (
                "SCE serves area via single feed through mountain terrain. "
                "Overhead lines through forest are ignition sources and "
                "vulnerable to tree strike. PSPS shutoffs during wind events "
                "leave entire community without power. Backup generators "
                "essential but create secondary fire risk."
            ),
            "communications": (
                "Very limited cell coverage in the mountain valley. Deep "
                "terrain blocks signal. Community relies on landlines (if "
                "working), PMC HOA notification systems, and physical "
                "door-knocking. Emergency communications dependent on "
                "community organization, not technology."
            ),
            "medical": (
                "No medical facilities. Nearest hospital: Kern Medical in "
                "Bakersfield (~50+ mi). Ambulance must travel the single "
                "Mil Potrero Highway road. Helicopter access limited by "
                "mountain terrain and potential smoke. Medical emergency "
                "response times can exceed 45 minutes."
            ),
        },
        "demographics_risk_factors": {
            "population": 2422,
            "seasonal_variation": (
                "Moderate to significant. Second-home community with weekend "
                "and holiday visitors. Some seasonal variation with summer "
                "and winter recreation. Visitors unfamiliar with the single "
                "access road and evacuation procedures."
            ),
            "elderly_percentage": "est. 25-30% (median age 51.6, retirement character)",
            "mobile_homes": (
                "Some manufactured homes within the community. Mixed housing "
                "stock ranging from cabins to modern homes. Older wood-frame "
                "structures common."
            ),
            "special_needs_facilities": (
                "None. Isolated gated mountain community. Elderly residents "
                "(median age 51.6) living alone face particular evacuation "
                "challenges. Single access road means no EMS redundancy."
            ),
        },
    },
}
