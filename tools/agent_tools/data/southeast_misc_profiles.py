"""Southeast, Black Hills, Midwest & Hawaii Fire-Vulnerable City Profiles
===============================================================

Comprehensive terrain, evacuation, fire behavior, infrastructure, and demographic
data for 25 fire-vulnerable cities across the Southeast US, Black Hills,
Midwest, and Hawaii.

Usage:
    from tools.agent_tools.data.southeast_misc_profiles import (
        SE_MISC_TERRAIN_PROFILES,
        SE_MISC_IGNITION_SOURCES,
        SE_MISC_CLIMATOLOGY,
    )

Cities covered (25 entries across 8 states):
    HAWAII (4 cities):
        Kula
        Lahaina
        Wailea Kihei
        Waimea
    TENNESSEE (3 cities):
        Crossville
        Gatlinburg
        Pigeon Forge
    NORTH CAROLINA (5 cities):
        Asheville
        Blowing Rock
        Boone
        Bryson City
        Lake Lure
    GEORGIA (1 cities):
        Athens
    FLORIDA (1 cities):
        Panama City
    SOUTH DAKOTA (BLACK HILLS) (8 cities):
        Custer
        Deadwood
        Hill City
        Hot Springs
        Keystone
        Rapid City
        Spearfish
        Sturgis
    MISSOURI (OZARKS) (2 cities):
        Branson
        Table Rock Lake
    MINNESOTA (1 cities):
        Duluth

Sources:
    - NIST Chimney Tops 2 Fire investigation
    - USFA/FEMA 2023 Maui Wildfire After-Action Report
    - USGS Jasper Fire fuels data
    - SD Wildland Fire Division historical records
    - NCFS wildfire statistics
    - WRCC / IEM / ASOS climatology archives
"""

# =============================================================================
# TERRAIN PROFILES -- 25 entries organized by state
# =============================================================================

SE_MISC_TERRAIN_PROFILES = {

    # =========================================================================
    # HAWAII (4 cities)
    # =========================================================================

    # ---- 2. Kula / Upcountry Maui ----
    "kula_hi": {
        "center": (20.790, -156.330),
        "terrain_notes": (
            "Kula and the broader Upcountry Maui region occupy the western slopes of "
            "Haleakala volcano at approximately 3,000-4,000 ft elevation. The terrain is "
            "characterized by steep volcanic slopes deeply incised by narrow gulches that "
            "run downslope from Haleakala's 10,023 ft summit toward the central isthmus. "
            "These gulches — some hundreds of feet deep — act as fire chimneys, channeling "
            "updrafts and accelerating fire spread upslope at rates far exceeding flat-ground "
            "predictions. Former ranching and diversified agricultural land has been "
            "progressively colonized by invasive eucalyptus (Eucalyptus spp.), strawberry "
            "guava (Psidium cattleianum), and various African grass species. Eucalyptus bark "
            "is highly flammable, sheds in strips that become airborne firebrands, and the "
            "trees produce volatile oils that can cause explosive crown fire runs. The rural "
            "residential pattern features scattered homes along narrow, winding roads with "
            "single-access driveways extending into gulch-side terrain. Kula has a semi-arid "
            "climate on the leeward side of Haleakala with annual rainfall of only 20-30 "
            "inches, punctuated by dry summer months when relative humidity can drop below "
            "20%. The 2023 Olinda Fire started near the Maui Bird Conservation Center on "
            "Olinda Road and burned 1,081 acres through this gulch-and-eucalyptus terrain, "
            "while the separate Kula Fire burned 202 acres closer to the community core, "
            "destroying 19 homes. The combination of steep volcanic terrain, invasive fuel "
            "species, limited road access, and rural water infrastructure makes Upcountry "
            "Maui one of the most fire-vulnerable rural communities in the Hawaiian Islands."
        ),
        "key_features": [
            {"name": "Haleakala volcano slopes", "bearing": "E/NE",
             "type": "volcanic_slope",
             "notes": "Rise to 10,023 ft; steep terrain creates extreme fire behavior with rapid upslope runs"},
            {"name": "Deep gulch network", "bearing": "radial from summit",
             "type": "fire_chimneys",
             "notes": "Gulches hundreds of feet deep channel updrafts and create chimney effect; extremely difficult suppression access"},
            {"name": "Olinda Road corridor", "bearing": "upslope E",
             "type": "fire_origin",
             "notes": "2023 Olinda Fire originated near this road; corridor through eucalyptus-invaded terrain"},
            {"name": "Fallow agricultural land", "bearing": "S/SW",
             "type": "invasive_grassland",
             "notes": "Former ranching land colonized by invasive grasses and eucalyptus; continuous fuel to community edge"},
        ],
        "elevation_range_ft": (2800, 4200),
        "wui_exposure": "high — scattered rural homes along narrow single-access roads in gulch terrain surrounded by invasive eucalyptus and grass fuels",
        "historical_fires": [
            {"name": "Olinda Fire", "year": 2023, "acres": 1081,
             "structures_destroyed": 3, "fatalities": 0,
             "cause": "under investigation — simultaneous with Lahaina fires Aug 8",
             "notes": (
                 "Started near Olinda Road and Maui Bird Conservation Center. Burned through "
                 "deep gulches with invasive eucalyptus fuel. Hot spots in gulches persisted "
                 "for weeks. 85% contained by Aug 27. Extremely difficult terrain for crews."
             )},
            {"name": "Kula Fire", "year": 2023, "acres": 202,
             "structures_destroyed": 19, "fatalities": 0,
             "cause": "under investigation",
             "notes": (
                 "Separate fire closer to Kula community core. Destroyed 19 homes with "
                 "$32M+ damage. 90% contained by Aug 27. Demonstrated vulnerability of "
                 "scattered rural homes in invasive fuel matrix."
             )},
        ],
        "evacuation_routes": [
            {"route": "Kula Highway (HI-37)", "direction": "south toward Pukalani",
             "lanes": 2, "bottleneck": "winding two-lane road through agricultural land",
             "risk": "Single primary route for Upcountry residents; traffic quickly overwhelms capacity"},
            {"route": "Haleakala Highway (HI-377/378)", "direction": "upslope toward crater",
             "lanes": 2, "bottleneck": "dead-end at summit; only useful for short-distance displacement",
             "risk": "Leads to Haleakala summit with no through-route; potential trap"},
            {"route": "Olinda Road", "direction": "upslope through forest",
             "lanes": 2, "bottleneck": "narrow winding road, single-lane in sections",
             "risk": "Road passes through fire origin area; cut off during 2023 fires"},
        ],
        "fire_spread_characteristics": (
            "Eucalyptus-driven spotting is the dominant spread mechanism: bark strips loft "
            "hundreds of feet and ignite new fires downwind. In gulch terrain, convective "
            "updrafts accelerate fire upslope at 2-3x flat-ground rates. Guinea grass and "
            "buffelgrass on lower slopes produce rapid surface spread feeding into eucalyptus "
            "canopy fires. Crown fire runs in eucalyptus can produce flame lengths exceeding "
            "100 ft. The 2023 fires demonstrated that simultaneous ignitions across multiple "
            "gulches can overwhelm suppression resources."
        ),
        "infrastructure_vulnerabilities": (
            "Rural water system with limited pressure and storage; fire hydrant coverage is "
            "sparse outside the Kula community core. MECO overhead power lines along narrow "
            "roads through gulch terrain are vulnerable to tree strikes in high winds. Cell "
            "coverage is spotty in gulch terrain, limiting emergency notifications. Many homes "
            "on single-access driveways that can be cut off by fire within minutes."
        ),
        "demographics_risk_factors": (
            "Population approximately 6,500 in greater Kula area. Mix of long-term agricultural "
            "families and newer rural lifestyle residents. Significant elderly population in "
            "remote homes. Many properties lack fire-hardened construction. Limited local fire "
            "department resources for the large geographic area served."
        ),
    },

    # ---- 1. Lahaina, Maui ----
    "lahaina_hi": {
        "center": (20.878, -156.682),
        "terrain_notes": (
            "Lahaina occupies a narrow coastal strip on leeward west Maui, pressed between "
            "the Pacific Ocean to the west and the steeply rising West Maui Mountains "
            "(Mauna Kahalawai) to the east, which ascend to 5,788 ft at Pu'u Kukui. The "
            "town sits at essentially sea level on an alluvial plain no more than half a "
            "mile wide in most places. Above the town, former sugar cane and pineapple "
            "plantation lands — abandoned since the 1990s — have been colonized by "
            "invasive guinea grass (Megathyrsus maximus), which grows up to six inches "
            "per day during wet periods and then desiccates into continuous flashy fuel "
            "during summer drought. Buffelgrass (Cenchrus ciliaris), another African "
            "invasive, fills gaps on rockier slopes. The terrain is deeply incised by "
            "gulches (Kaua'ula, Kahoma, Lahainaluna) that funnel powerful downslope winds "
            "directly into the town during trade wind disruption events. Pre-colonial "
            "Lahaina was wetland — the 'Venice of the Pacific' — but 150 years of water "
            "diversion for plantations and urban development drained the landscape, "
            "eliminating natural moisture buffers. No managed firebreaks exist between "
            "hillside fuels and the dense wooden structures of the historic Front Street "
            "district. The town's WUI is effectively a zero-setback interface: invasive "
            "grassland directly abuts residential fencing. Honoapiilani Highway (HI-30) "
            "is the sole coastal road, creating a single-point evacuation failure mode. "
            "The Lahaina Bypass (HI-3000) provides a parallel route upslope but is itself "
            "vulnerable to fire from the same hillside fuels. Climate projections show "
            "increasing drought frequency on leeward Maui, with trade wind disruptions "
            "becoming more common during Pacific hurricane season (June-November)."
        ),
        "key_features": [
            {"name": "West Maui Mountains (Mauna Kahalawai)", "bearing": "E/NE",
             "type": "steep_mountain",
             "notes": "Rise from sea level to 5,788 ft; downslope winds accelerate through gulches during trade wind disruptions"},
            {"name": "Kaua'ula Valley / gulch system", "bearing": "E",
             "type": "wind_corridor",
             "notes": "Primary wind corridor funneling katabatic flow into town; 60-80 kt gusts recorded during 2023 event"},
            {"name": "Front Street historic district", "bearing": "through town",
             "type": "dense_historic_structures",
             "notes": "Dense wooden structures, narrow streets; 96% of burned structures were residential; total destruction of historic core"},
            {"name": "Fallow plantation lands", "bearing": "E/NE",
             "type": "invasive_grassland",
             "notes": "Former sugar/pineapple land now thick with guinea grass and buffelgrass — continuous flashy fuel with no managed buffer"},
            {"name": "Honoapiilani Highway (HI-30)", "bearing": "N-S along coast",
             "type": "evacuation_route",
             "notes": "Sole coastal road; became impassable during 2023 fire; many victims trapped"},
        ],
        "elevation_range_ft": (0, 100),
        "wui_exposure": "extreme — zero-setback interface with invasive grassland directly abutting residential structures across entire eastern town boundary",
        "historical_fires": [
            {"name": "Lahaina Fire", "year": 2023, "acres": 2170,
             "structures_destroyed": 2207, "fatalities": 102,
             "cause": "downed power line + hurricane winds",
             "notes": (
                 "Deadliest US wildfire in over 100 years. Hawaiian Electric downed power "
                 "line re-energized at 6:34 AM on Aug 8, igniting invasive grass on "
                 "Lahainaluna Road hillside. Fire crews left scene after apparent knockdown; "
                 "fire reignited in afternoon with 60-80 kt downslope winds driven by "
                 "Hurricane Dora's pressure gradient 700 miles to the south. Fire crossed "
                 "Honoapiilani Highway at 4:46 PM and entered main Lahaina. Civil defense "
                 "sirens were NOT activated despite Hawaii having the world's largest outdoor "
                 "siren system (80+ sirens on Maui). Town destroyed in approximately 5 hours. "
                 "Many residents had no warning; some sheltered in the ocean. Four separate "
                 "fires burned on Maui that day totaling 6,721 acres. $5.5 billion in damages."
             )},
        ],
        "evacuation_routes": [
            {"route": "Honoapiilani Hwy (HI-30) south", "direction": "south toward Olowalu",
             "lanes": 2, "bottleneck": "single coastal road, sharp curves at Olowalu",
             "risk": "Only escape route south; blocked by fire in 2023; residents trapped"},
            {"route": "Honoapiilani Hwy (HI-30) north", "direction": "north toward Kapalua",
             "lanes": 2, "bottleneck": "narrow road along cliffs north of Lahaina",
             "risk": "Cliffside road with no shoulder; congestion during mass evacuation"},
            {"route": "Lahaina Bypass (HI-3000)", "direction": "east/upslope bypass",
             "lanes": 2, "bottleneck": "runs through same hillside fuel as fire origin",
             "risk": "Bypass road traverses invasive grassland; closed at 3:20 PM in 2023 fire before town burned"},
        ],
        "fire_spread_characteristics": (
            "Extremely rapid spread through continuous invasive grass fuel bed on steep terrain. "
            "Guinea grass flame lengths of 15-25 ft with rate of spread exceeding 40 chains/hr "
            "under wind-driven conditions. Downslope katabatic winds through gulch system "
            "created fire whirls and horizontal vortices observed during the 2023 event. Fire "
            "transitioned from wildland to urban conflagration within minutes of crossing "
            "Honoapiilani Highway, with structure-to-structure spread driven by radiant heat "
            "and ember transport in dense wooden building stock. Spotting distances of 0.25-0.5 "
            "miles observed from burning structures."
        ),
        "infrastructure_vulnerabilities": (
            "Hawaiian Electric overhead power lines on Lahainaluna Road hillside caused the "
            "2023 ignition; utility did not implement PSPS despite 80+ mph winds. Water "
            "system lost pressure during fire due to simultaneous demand and infrastructure "
            "damage — hydrants ran dry. Cell towers destroyed, eliminating emergency "
            "communications. Single coastal highway (HI-30) is the only evacuation corridor "
            "for 12,000+ residents. No hospital in Lahaina; nearest is Maui Memorial in "
            "Wailuku, 25 miles away through fire-affected area."
        ),
        "demographics_risk_factors": (
            "Population approximately 12,700 (2020 census) with significant tourist overlay "
            "of 8,000-10,000 visitors daily in peak season. Large elderly population in "
            "historic core and senior housing complexes. Many residents are Native Hawaiian "
            "and Pacific Islander communities with multi-generational ties to place, reducing "
            "willingness to evacuate. High proportion of renters in older wooden structures "
            "without fire-hardened construction. Language barriers exist among immigrant "
            "workforce populations. Many vacation rentals had transient occupants unfamiliar "
            "with evacuation routes."
        ),
    },

    # ---- 3. Wailea / Kihei, South Maui ----
    "wailea_kihei_hi": {
        "center": (20.730, -156.450),
        "terrain_notes": (
            "Wailea and Kihei form a continuous coastal development corridor along South "
            "Maui's leeward coast, stretching approximately 8 miles from Ma'alaea Bay south "
            "to Makena. The terrain rises gradually from sea level beach communities to the "
            "lower western slopes of Haleakala, where elevation reaches 500-800 ft at the "
            "eastern edge of development. This leeward coast receives only 10-15 inches of "
            "annual rainfall — making it one of the driest inhabited areas in Hawaii. The "
            "landscape above the resort/residential corridor is dominated by vast expanses "
            "of invasive guinea grass, buffelgrass, and fountain grass on former rangeland "
            "and undeveloped parcels. During summer drought, these grasslands desiccate into "
            "a continuous, highly flammable fuel bed extending from the upper slopes of "
            "Haleakala down to the edge of suburban development. The August 2023 Pulehu Fire "
            "ignited north of Kihei near Pulehu Road and burned into the northeast portions "
            "of the community, forcing evacuations. Maui County has proposed a 92-acre "
            "hazardous fuels reduction project with firebreaks and nine 50,000-gallon water "
            "cisterns at strategic locations around Kihei and Wailea. The community's "
            "east-facing exposure to the dry leeward slopes of Haleakala, combined with "
            "afternoon onshore-to-offshore wind transitions, creates daily fire weather "
            "windows during drought periods. Kihei's population has grown from 16,749 in "
            "2000 to over 23,000, with continued development pushing eastward into the "
            "grassland fuel matrix. South Maui Road (Pi'ilani Highway) serves as both the "
            "primary transportation corridor and an informal firebreak, though it has proven "
            "insufficient against wind-driven grass fires."
        ),
        "key_features": [
            {"name": "Leeward Haleakala slopes", "bearing": "E/NE",
             "type": "invasive_grassland",
             "notes": "Vast invasive grass fuel bed on dry volcanic slopes above community; continuous fuel from 3,000 ft down to development edge"},
            {"name": "Pi'ilani Highway (HI-31)", "bearing": "N-S through corridor",
             "type": "transportation_corridor",
             "notes": "Primary route; serves as informal firebreak but insufficient against wind-driven grass fires"},
            {"name": "Pulehu Road fire corridor", "bearing": "NE of Kihei",
             "type": "fire_origin",
             "notes": "2023 Pulehu Fire ignited near this agricultural road; invasive grass fuel on both sides"},
            {"name": "Ma'alaea wind gap", "bearing": "NW",
             "type": "wind_corridor",
             "notes": "Isthmus between West Maui and Haleakala creates powerful venturi wind acceleration; gusts regularly exceed 40 mph"},
        ],
        "elevation_range_ft": (0, 800),
        "wui_exposure": "high — suburban development expanding eastward into continuous invasive grassland on dry leeward Haleakala slopes",
        "historical_fires": [
            {"name": "Pulehu Fire (South Maui Fire)", "year": 2023, "acres": 1200,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "under investigation — simultaneous with Lahaina/Kula fires",
             "notes": (
                 "Ignited near Pulehu Road north of Kihei on Aug 8-9, 2023. Burned into "
                 "northeast Kihei forcing evacuations of multiple subdivisions. Invasive grass "
                 "fuel driven by downslope winds. Firefighters prevented structural losses "
                 "but fire demonstrated vulnerability of South Maui corridor."
             )},
            {"name": "Recurring Kihei brush fires", "year": "annual",
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "various — vehicles, equipment, arson, power lines",
             "notes": (
                 "Kihei experiences multiple grass fires annually during dry season. Fire "
                 "department responds to 15-30 wildland fires per year in the South Maui "
                 "area. Most are quickly contained but demonstrate chronic ignition risk."
             )},
        ],
        "evacuation_routes": [
            {"route": "Pi'ilani Hwy (HI-31) north", "direction": "north toward Kahului",
             "lanes": 4, "bottleneck": "merges to 2 lanes at Ma'alaea; wind gap congestion",
             "risk": "Primary evacuation route for 23,000+ residents; single corridor northbound"},
            {"route": "Pi'ilani Hwy south", "direction": "south toward Makena",
             "lanes": 2, "bottleneck": "dead-end at La Perouse Bay; no through-route",
             "risk": "Leads to dead end; only useful for short-distance displacement south"},
            {"route": "Mokulele Hwy (HI-311)", "direction": "NE toward Kahului airport",
             "lanes": 2, "bottleneck": "straight road through sugar cane / grass fields",
             "risk": "Traverses open grassland fuel; potentially cut off by cross-wind grass fire"},
        ],
        "fire_spread_characteristics": (
            "Grass fire dynamics dominate: guinea grass and buffelgrass produce rapid surface "
            "spread rates of 50-100+ chains/hr under wind-driven conditions. The Ma'alaea wind "
            "gap creates venturi acceleration of trade winds across the isthmus, producing "
            "sustained 30-40 mph winds that drive fire downslope toward coastal communities. "
            "Afternoon wind shift from onshore sea breeze to offshore drainage flow creates "
            "daily fire weather transition. Continuous grass fuel with no firebreaks allows "
            "uninterrupted fire runs of 2+ miles from upper slopes to development edge."
        ),
        "infrastructure_vulnerabilities": (
            "Water system adequate for municipal use but limited wildfire suppression capacity "
            "at development edge. MECO power lines along Pi'ilani Highway and internal "
            "subdivision roads are ignition sources. Proposed 92-acre fuels reduction project "
            "with nine 50,000-gallon cisterns not yet implemented as of 2024. Single hospital "
            "(Maui Memorial) is 12 miles north in Wailuku."
        ),
        "demographics_risk_factors": (
            "Population approximately 23,000 with additional 10,000+ tourists in resort hotels "
            "and vacation rentals. Significant retirement community in Wailea. Many condo "
            "complexes with elderly residents. Tourist population unfamiliar with fire risk "
            "and evacuation procedures. Growing workforce housing developments at eastern "
            "edge of community directly adjacent to grassland fuel."
        ),
    },

    # ---- 4. Waimea / Kamuela, Big Island ----
    "waimea_hi": {
        "center": (20.023, -155.672),
        "terrain_notes": (
            "Waimea (also known as Kamuela) is an upland town at approximately 2,670 ft "
            "elevation on the Kohala Mountain saddle between Mauna Kea (13,796 ft) and the "
            "Kohala Mountains (5,480 ft) on the Big Island of Hawaii. The town is the "
            "headquarters of Parker Ranch, one of the largest cattle ranches in the United "
            "States at approximately 130,000 acres. The landscape is dominated by vast "
            "expanses of grassland — both native pili grass and extensive invasive species "
            "including kikuyu grass, fountain grass, and guinea grass — interspersed with "
            "planted windbreaks of Norfolk pine, eucalyptus, and ironwood. The terrain is "
            "gently rolling on the plateau but drops steeply on the Hamakua Coast side to "
            "the northeast and toward the dry Kohala coast to the west. The town has a "
            "unique climate split: the eastern (Hamakua) side receives 75+ inches of annual "
            "rainfall while the western (Kohala) side may receive less than 15 inches, "
            "creating a dramatic fuel moisture gradient across the community. Strong trade "
            "winds funnel through the Kohala-Mauna Kea saddle at sustained speeds of 20-35 "
            "mph, with gusts exceeding 50 mph during winter storm events. The Mana Road "
            "Fire of 2021 burned over 42,000 acres of grassland on Parker Ranch slopes "
            "above Waimea — one of the largest wildfires in recorded Hawaiian history. This "
            "fire demonstrated that the vast open grasslands surrounding the town can "
            "produce fire runs of extraordinary scale when driven by saddle winds. Waimea's "
            "residential areas are largely surrounded by ranch grassland with minimal "
            "firebreak infrastructure between homes and the open range."
        ),
        "key_features": [
            {"name": "Parker Ranch grasslands", "bearing": "all directions",
             "type": "open_grassland",
             "notes": "130,000 acres of cattle ranch; mix of native and invasive grass; continuous fuel surrounding town on all sides"},
            {"name": "Kohala-Mauna Kea saddle wind corridor", "bearing": "E-W",
             "type": "wind_corridor",
             "notes": "Trade winds accelerate through topographic gap; sustained 20-35 mph with 50+ mph gusts"},
            {"name": "Mauna Kea slopes", "bearing": "SE",
             "type": "volcanic_slope",
             "notes": "Grassland extends from town up to treeline at ~6,500 ft; Mana Road fire burned across this terrain"},
            {"name": "Kohala coast descent", "bearing": "W/NW",
             "type": "leeward_slope",
             "notes": "Steep drop to dry Kohala coast; fire can run rapidly downslope toward coastal resorts"},
        ],
        "elevation_range_ft": (2400, 3200),
        "wui_exposure": "high — residential areas surrounded by continuous ranch grassland extending miles in all directions with no structural firebreaks",
        "historical_fires": [
            {"name": "Mana Road Fire", "year": 2021, "acres": 42000,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "under investigation",
             "notes": (
                 "One of the largest wildfires in recorded Hawaiian history. Burned along "
                 "Old Saddle Road on Mauna Kea slopes largely on Parker Ranch land. "
                 "Mostly grassland fire driven by trade winds. Community effort involving "
                 "ranch hands, DLNR, and federal resources. Demonstrated catastrophic "
                 "grass fire potential of the Waimea landscape."
             )},
            {"name": "Recurring Parker Ranch grass fires", "year": "annual",
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "various — equipment, vehicles, power lines",
             "notes": (
                 "Multiple grass fires annually on ranch land surrounding Waimea. Most "
                 "are suppressed quickly but wind-driven events can escalate rapidly "
                 "across the open terrain."
             )},
        ],
        "evacuation_routes": [
            {"route": "Hawaii Belt Road (HI-19) east", "direction": "east toward Honoka'a",
             "lanes": 2, "bottleneck": "winding road along Hamakua Coast cliffs",
             "risk": "Traverses wet forest zone; generally safer from fire but slow evacuation"},
            {"route": "Hawaii Belt Road (HI-19) west", "direction": "west toward Kawaihae/Kohala coast",
             "lanes": 2, "bottleneck": "steep descent through dry grassland",
             "risk": "Road passes through fire-prone grassland on descent to coast; vulnerable to cross-wind fire"},
            {"route": "Kohala Mountain Road (HI-250)", "direction": "north toward Hawi",
             "lanes": 2, "bottleneck": "narrow mountain road, no shoulder",
             "risk": "Open grassland on both sides; exposed to wind-driven fire during saddle wind events"},
        ],
        "fire_spread_characteristics": (
            "Grass fire dynamics with extreme wind-driven spread rates. The Kohala-Mauna Kea "
            "saddle produces some of the strongest sustained surface winds in Hawaii, driving "
            "grass fires at rates exceeding 100 chains/hr in cured fuel. The Mana Road Fire "
            "demonstrated multi-day fire runs across tens of thousands of acres of continuous "
            "grassland. Fire can approach Waimea from any direction given the surrounding "
            "360-degree grassland fuel matrix. Spotting is limited in grassland but rate of "
            "spread compensates. Eucalyptus and Norfolk pine windbreaks can produce intense "
            "localized crown fire behavior and spotting when involved."
        ),
        "infrastructure_vulnerabilities": (
            "Water system serves a dispersed rural community with limited fire suppression "
            "capacity at the wildland interface. HELCO power lines along ranch roads and "
            "highways are potential ignition sources. Parker Ranch access roads are unpaved "
            "in many areas, limiting fire apparatus access. North Hawaii Community Hospital "
            "(25 beds) is the only medical facility; nearest major hospital is Hilo Medical "
            "Center, 55 miles east."
        ),
        "demographics_risk_factors": (
            "Population approximately 10,000 in the greater Waimea area. Mix of ranching "
            "families, retirees, and resort workers commuting to Kohala coast. Significant "
            "Native Hawaiian population. Many homes on large rural parcels with long "
            "driveways through grassland. Limited fire department coverage for the large "
            "geographic area."
        ),
    },

    # =========================================================================
    # TENNESSEE (3 cities)
    # =========================================================================

    # ---- 7. Crossville / Cumberland Plateau, TN ----
    "crossville_tn": {
        "center": (35.949, -85.027),
        "terrain_notes": (
            "Crossville sits atop the Cumberland Plateau at 1,881 ft elevation in Cumberland "
            "County, Tennessee. The Cumberland Plateau is a broad, flat-topped tableland "
            "approximately 50 miles wide, bounded by steep escarpments on both the east "
            "(dropping to the Great Valley) and west (dropping to the Highland Rim). The "
            "plateau surface is dissected by deep gorges cut by streams draining to both "
            "sides, creating knife-edge ridges and steep-walled canyons. The forest is mixed "
            "oak-hickory-pine with significant Virginia pine and shortleaf pine components "
            "on dry ridge tops and south-facing slopes. Fire suppression over decades has "
            "allowed dense understory development and heavy leaf litter accumulation. The "
            "plateau's elevated, exposed position makes it prone to drought stress — soils "
            "are thin and rocky over sandstone caprock, with limited water retention capacity. "
            "Cumberland County experiences recurring drought-driven wildfire outbreaks, "
            "particularly during fall (October-November) when leaf litter is dry, humidity "
            "is low, and atmospheric mixing events bring gusty winds. The Renegade Mountain "
            "residential community, built on a forested ridge in the plateau's dissected "
            "terrain, has experienced repeated fire threats. The broader Upper Cumberland "
            "region has seen dozens of simultaneous fires during severe drought years "
            "(notably 2016), with arson being a significant ignition source. Crossville is "
            "the largest city on the Cumberland Plateau and serves as a retirement "
            "destination with a significant elderly population in ridge-top and mountain "
            "developments surrounded by forest."
        ),
        "key_features": [
            {"name": "Cumberland Plateau escarpments", "bearing": "E and W margins",
             "type": "terrain_feature",
             "notes": "Steep escarpments with updraft fire behavior; fire can race up escarpment faces into ridge-top communities"},
            {"name": "Renegade Mountain community", "bearing": "SE",
             "type": "wui_development",
             "notes": "Residential development on forested ridge with limited access roads; repeated fire threats"},
            {"name": "Dissected gorge terrain", "bearing": "throughout plateau",
             "type": "canyon_system",
             "notes": "Deep gorges cut into plateau create complex fire behavior; steep walls channel wind and fire"},
            {"name": "Catoosa WMA / state forests", "bearing": "N/NE",
             "type": "public_wildland",
             "notes": "Large blocks of public forestland surrounding plateau communities; limited suppression access in gorge terrain"},
        ],
        "elevation_range_ft": (1700, 2100),
        "wui_exposure": "high — retirement communities and subdivisions built on forested ridge-tops in dissected plateau terrain with limited access roads",
        "historical_fires": [
            {"name": "2016 Cumberland Plateau drought fires", "year": 2016,
             "acres": 5000, "structures_destroyed": 12, "fatalities": 0,
             "cause": "arson + drought",
             "notes": (
                 "Dozens of fires across Upper Cumberland during extreme drought. "
                 "Cumberland County firefighters pushed to exhaustion. At least one fire on "
                 "Renegade Mountain threatened and destroyed buildings. Part of the broader "
                 "2016 SE Appalachian drought fire outbreak that burned 119,000+ acres across "
                 "7 states."
             )},
            {"name": "Recurring fall drought fires", "year": "annual",
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "arson, debris burning, lightning",
             "notes": (
                 "Cumberland Plateau experiences chronic fall fire season. Thin soils over "
                 "sandstone dry rapidly. Arson is a significant factor — burn bans frequently "
                 "violated. County fire departments are primarily volunteer with limited "
                 "wildland fire training."
             )},
        ],
        "evacuation_routes": [
            {"route": "I-40", "direction": "E-W across plateau",
             "lanes": 4, "bottleneck": "interstate provides good capacity but exits to local roads limited",
             "risk": "Interstate itself relatively safe but local road connections to ridge-top communities are narrow and forested"},
            {"route": "US-127", "direction": "N-S through Crossville",
             "lanes": 4, "bottleneck": "commercial congestion in town center",
             "risk": "Primary N-S route; passes through forested areas north and south of town"},
            {"route": "Renegade Mountain access road", "direction": "SE from Crossville",
             "lanes": 2, "bottleneck": "single access road to entire community",
             "risk": "One road in/out of large residential community in forested terrain; potential trap during fire event"},
        ],
        "fire_spread_characteristics": (
            "Leaf litter fires in oak-hickory-pine forest with moderate surface spread rates "
            "of 10-30 chains/hr under normal conditions, accelerating dramatically on steep "
            "escarpment faces and in gorge terrain where chimney effects develop. Virginia "
            "pine component provides ladder fuel and crown fire potential. Drought conditions "
            "reduce fuel moisture in thin plateau soils rapidly. Multiple simultaneous "
            "ignitions (often arson) can overwhelm volunteer fire departments."
        ),
        "infrastructure_vulnerabilities": (
            "Primarily volunteer fire departments with limited wildland firefighting equipment "
            "and training. Rural water systems with low-pressure zones on ridge tops. Power "
            "lines through forested terrain vulnerable to tree strikes. Cell coverage gaps in "
            "gorge terrain. Cumberland Medical Center (189 beds) serves broad rural area."
        ),
        "demographics_risk_factors": (
            "Population approximately 12,000 in Crossville, 60,000 in Cumberland County. "
            "Major retirement destination — 25%+ of population over 65 in many communities. "
            "Many retirees in forested ridge-top developments with limited mobility. "
            "Income levels below state median, affecting ability to create defensible space. "
            "Significant mobile home stock in rural areas."
        ),
    },

    # ---- 5. Gatlinburg, TN ----
    "gatlinburg_tn": {
        "center": (35.714, -83.510),
        "terrain_notes": (
            "Gatlinburg is a mountain tourism town (permanent pop ~4,000, but hosting 12+ "
            "million visitors annually) nestled in a narrow valley at 1,289 ft elevation in "
            "the Great Smoky Mountains of eastern Tennessee. The town is built along the "
            "West Prong of the Little Pigeon River in a steep-walled valley surrounded by "
            "ridges rising to 6,000+ ft on three sides — south, east, and southeast. This "
            "valley-and-ridge topography creates a natural chimney effect that funnels and "
            "accelerates wind during meteorological events, particularly when mountain wave "
            "winds develop with strong southerly flow aloft. The surrounding Great Smoky "
            "Mountains National Park — the most visited US national park — has decades of "
            "fire suppression that has allowed extreme fuel accumulation in mixed hardwood "
            "and pine forests. Heavy leaf litter, dense understory, and standing dead timber "
            "from hemlock woolly adelgid mortality (which has killed 80%+ of eastern hemlocks) "
            "create both ground and ladder fuels throughout the park's lower and middle "
            "elevations. Hundreds of vacation rental cabins have been built along forested "
            "ridgelines on steep slopes surrounding the valley, accessed by narrow, winding, "
            "single-lane roads with no turnarounds. Many of these cabins have zero defensible "
            "space, with tree canopy overhanging wooden decks and rooflines. The 2016 Chimney "
            "Tops 2 Fire demonstrated the catastrophic potential of this terrain when fire "
            "descended from Chimney Tops (4,724 ft) into the valley during 87 mph mountain "
            "wave wind gusts, destroying over 2,400 structures and killing 14 people in a "
            "matter of hours. The valley's shape concentrates both smoke and firebrands, "
            "reducing visibility and increasing spot fire ignitions throughout the built "
            "environment during a wind-driven event."
        ),
        "key_features": [
            {"name": "Chimney Tops", "bearing": "S/SE", "type": "mountain_peak",
             "notes": "Origin area of 2016 fire at 4,724 ft; fire ran downslope into town in hours during 87 mph gusts"},
            {"name": "Great Smoky Mountains NP", "bearing": "S/E/SE",
             "type": "national_park",
             "notes": "Most visited US national park; decades of fire suppression; heavy fuel accumulation; hemlock mortality adding standing dead fuel"},
            {"name": "Little Pigeon River valley", "bearing": "through town",
             "type": "river_valley",
             "notes": "Narrow valley funnels wind creating chimney effect; downtown built along river corridor"},
            {"name": "Ridgeline cabin developments", "bearing": "all mountain sides",
             "type": "wui_development",
             "notes": "Hundreds of rental cabins on forested ridgelines; single-access roads, no defensible space; many burned in 2016"},
            {"name": "US-441 corridor", "bearing": "NW-SE", "type": "evacuation_route",
             "notes": "Primary route through town; congested with 14,000 evacuees in 2016; limited alternates"},
        ],
        "elevation_range_ft": (1200, 1600),
        "wui_exposure": "extreme — dense tourist infrastructure and hundreds of ridgeline cabins in continuous forest with zero defensible space on steep terrain",
        "historical_fires": [
            {"name": "Chimney Tops 2 Fire", "year": 2016, "acres": 17000,
             "structures_destroyed": 2400, "fatalities": 14,
             "cause": "arson (two juveniles) + 87 mph mountain wave winds",
             "notes": (
                 "Started Nov 23 by arson on Chimney Tops Trail. Burned in GSMNP for 5 days "
                 "before explosive growth on Nov 28 when mountain wave winds gusting to 87 mph "
                 "drove fire downslope into Gatlinburg and Pigeon Forge. Wind knocked down trees "
                 "onto power lines creating dozens of new ignitions across Sevier County. "
                 "14 killed, 190 injured, 14,000 evacuated. Over 2,400 structures damaged or "
                 "destroyed. NPS and local officials criticized for slow evacuation notification. "
                 "Worst wildfire disaster in the southeastern US in decades. $2 billion damage."
             )},
        ],
        "evacuation_routes": [
            {"route": "US-441 (Parkway) north", "direction": "NW toward Pigeon Forge",
             "lanes": 4, "bottleneck": "signal-controlled intersections through commercial strip",
             "risk": "Primary evacuation route; 14,000 evacuees gridlocked in 2016; commercial development slows throughput"},
            {"route": "US-321 east", "direction": "E toward Cosby",
             "lanes": 2, "bottleneck": "narrow winding mountain road through national park",
             "risk": "Traverses forested terrain that can be cut off by fire; slow speed limits"},
            {"route": "Ski Mountain Road / ridgeline roads", "direction": "various upslope",
             "lanes": 2, "bottleneck": "narrow single-lane roads to cabin developments",
             "risk": "Dead-end roads to ridgeline cabins; residents trapped if fire blocks single access point"},
        ],
        "fire_spread_characteristics": (
            "The 2016 event demonstrated extreme fire behavior driven by mountain wave winds. "
            "Firebrands lofted by 87 mph gusts started spot fires miles ahead of the main "
            "front. Downed trees from wind hit power lines creating secondary ignitions "
            "throughout the developed area simultaneously. Fire ran downslope through mixed "
            "hardwood-pine forest at rates exceeding 1 mile per hour. Structure-to-structure "
            "spread occurred rapidly in dense cabin developments where embers ignited wooden "
            "decks and shake roofs. Heavy leaf litter and dead hemlock fuels supported "
            "sustained ground fire that made reentry by firefighters dangerous for days."
        ),
        "infrastructure_vulnerabilities": (
            "Sevier County 911 center was overwhelmed during 2016 event. Cell towers failed "
            "as fire damaged infrastructure. Power knocked out by wind-downed trees before "
            "fire arrival. Water system lost pressure in several areas during peak firefighting "
            "demand. Many ridgeline cabin roads have no address markers, making emergency "
            "response location identification extremely difficult. Single hospital (LeConte "
            "Medical Center, 79 beds) in neighboring Sevierville, 10 miles north."
        ),
        "demographics_risk_factors": (
            "Permanent population only ~4,000 but 12+ million annual visitors create an "
            "average daily population 10-20x the permanent count. Peak fire risk season "
            "(fall drought) coincides with peak leaf-peeping tourism. Most tourists unfamiliar "
            "with evacuation routes or fire risk. Vacation rental occupants in ridgeline cabins "
            "are most vulnerable — isolated, unfamiliar with terrain, on dead-end roads. "
            "Language barriers among some workforce populations."
        ),
    },

    # ---- 6. Pigeon Forge, TN ----
    "pigeon_forge_tn": {
        "center": (35.788, -83.554),
        "terrain_notes": (
            "Pigeon Forge is a major tourism destination (pop ~6,300 permanent, 11+ million "
            "visitors annually) in Sevier County, Tennessee, located immediately northwest of "
            "Gatlinburg in a broader but still mountainous valley along the Middle Prong and "
            "West Prong of the Little Pigeon River. The town's famous 5-mile commercial strip "
            "along US-441 (the Parkway) is flanked by forested ridges rising 1,000-2,000 ft "
            "above the valley floor. Dollywood theme park and its associated resort complex "
            "sit on the eastern slope at approximately 1,800 ft elevation, directly within "
            "the WUI zone where forest meets development. The Wears Valley community to the "
            "southwest occupies a separate valley accessible via Wears Valley Road (US-321), "
            "surrounded by Great Smoky Mountains NP on three sides. During the November 2016 "
            "Chimney Tops 2 Fire, mountain wave winds gusting to 87 mph blew embers and "
            "downed power lines across the broader Sevier County area, starting multiple "
            "fires in and around Pigeon Forge simultaneously. The Cobbly Nob area to the "
            "east and cabin developments along Wears Valley Road suffered significant losses. "
            "Like Gatlinburg, Pigeon Forge has extensive ridgeline cabin development accessed "
            "by narrow mountain roads. The town's flat valley floor provides somewhat better "
            "evacuation capacity than Gatlinburg, but US-441 becomes a critical bottleneck "
            "when both communities evacuate simultaneously, as occurred in 2016 when 14,000+ "
            "people fled northward through the same corridor."
        ),
        "key_features": [
            {"name": "Dollywood / resort complex", "bearing": "E",
             "type": "tourism_infrastructure",
             "notes": "Major theme park and resort on forested hillside in WUI zone; 3+ million annual visitors; daily capacity 25,000+"},
            {"name": "US-441 Parkway commercial strip", "bearing": "N-S through town",
             "type": "evacuation_corridor",
             "notes": "5-mile strip of hotels, restaurants, and attractions; primary evacuation route shared with Gatlinburg traffic"},
            {"name": "Wears Valley", "bearing": "SW", "type": "mountain_valley",
             "notes": "Residential valley surrounded by GSMNP on 3 sides; single access road; fire forced evacuations in 2016 and 2024"},
            {"name": "Forested ridgeline cabins", "bearing": "E and W ridges",
             "type": "wui_development",
             "notes": "Extensive vacation rental cabins on steep slopes; same vulnerability pattern as Gatlinburg"},
        ],
        "elevation_range_ft": (1050, 1400),
        "wui_exposure": "extreme — Dollywood resort complex in WUI zone; hundreds of ridgeline cabins in continuous forest; Wears Valley surrounded by national park",
        "historical_fires": [
            {"name": "Chimney Tops 2 Fire (Sevier County extent)", "year": 2016,
             "acres": 17000, "structures_destroyed": 2400, "fatalities": 14,
             "cause": "arson + 87 mph mountain wave winds",
             "notes": (
                 "While the fire originated south of Gatlinburg, wind-driven embers and downed "
                 "power lines started fires throughout Pigeon Forge and Wears Valley. Pigeon "
                 "Forge was placed under mandatory evacuation. Multiple structures destroyed in "
                 "the Cobbly Nob area east of town. Dollywood's fire crews defended the property "
                 "but surrounding areas burned. Total Sevier County: 14 killed, 2,400+ structures."
             )},
            {"name": "Wears Valley Fire", "year": 2024, "acres": 1600,
             "structures_destroyed": 75, "fatalities": 0,
             "cause": "under investigation",
             "notes": (
                 "March 2024 wildfire in Wears Valley forced evacuations. Destroyed approximately "
                 "75 structures including cabins and homes. Demonstrated continued vulnerability "
                 "of the valley community surrounded by national park forest."
             )},
        ],
        "evacuation_routes": [
            {"route": "US-441 (Parkway) north", "direction": "N toward Sevierville",
             "lanes": 4, "bottleneck": "shared with Gatlinburg evacuees; signals and commercial congestion",
             "risk": "When both Gatlinburg and Pigeon Forge evacuate simultaneously, corridor capacity is exceeded; 2016 gridlock lasted hours"},
            {"route": "Veterans Blvd / Teaster Lane", "direction": "N parallel to Parkway",
             "lanes": 2, "bottleneck": "limited capacity parallel route",
             "risk": "Alternate route but connects back to US-441; does not provide independent egress"},
            {"route": "Wears Valley Road (US-321 W)", "direction": "SW toward Townsend",
             "lanes": 2, "bottleneck": "narrow mountain road; single access to Wears Valley",
             "risk": "Only route into/out of Wears Valley; if cut off, valley residents trapped; occurred in 2016 and 2024"},
        ],
        "fire_spread_characteristics": (
            "Same mountain wave wind dynamics as Gatlinburg event — 87 mph gusts drove embers "
            "miles ahead of fire front. Power line failures from wind-downed trees created "
            "multiple simultaneous ignitions across a 15-mile front. Fire spread through "
            "continuous mixed hardwood-pine forest with heavy leaf litter and hemlock mortality "
            "fuel loading. Wears Valley's enclosed geography traps smoke and embers, creating "
            "particularly intense fire behavior in that sub-basin."
        ),
        "infrastructure_vulnerabilities": (
            "US-441 is the critical transportation bottleneck for the entire Gatlinburg-Pigeon "
            "Forge corridor. Sevier County 911 center was overwhelmed in 2016 with 4,000+ calls "
            "in 4 hours. Power infrastructure on forested ridgelines is vulnerable to wind-driven "
            "tree failures. Water system pressure drops during high-demand firefighting operations. "
            "Dollywood has its own fire brigade but surrounding residential areas rely on "
            "volunteer departments with limited wildfire training."
        ),
        "demographics_risk_factors": (
            "Permanent population ~6,300 but daily tourist population can exceed 50,000 in peak "
            "season. Dollywood alone draws 3+ million annual visitors. Most tourists have no "
            "knowledge of fire risk or evacuation procedures. Wears Valley has an aging permanent "
            "population with limited mobility. Extensive short-term rental stock means transient, "
            "unfamiliar occupants in high-risk ridgeline locations."
        ),
    },

    # =========================================================================
    # NORTH CAROLINA (5 cities)
    # =========================================================================

    # ---- 8. Asheville, NC ----
    "asheville_nc": {
        "center": (35.595, -82.551),
        "terrain_notes": (
            "Asheville is a mountain city (pop ~94,000 metro ~470,000) at 2,134 ft elevation "
            "in the French Broad River valley of western North Carolina, surrounded by the "
            "Blue Ridge Mountains. The city sits in a broad intermontane basin where the "
            "French Broad and Swannanoa Rivers converge, ringed by forested ridges rising "
            "1,500-3,000 ft above the valley floor. The Blue Ridge Parkway traces the "
            "ridgeline south and east of the city through continuous hardwood and mixed "
            "pine-hardwood forest. North Carolina has more wildland-urban interface acreage "
            "than any other US state, and Asheville exemplifies this — 99% of buildings "
            "have some wildfire risk per First Street Foundation analysis. The surrounding "
            "Pisgah National Forest (500,000+ acres) and Blue Ridge Parkway corridor have "
            "experienced decades of fire suppression, allowing heavy fuel accumulation in "
            "oak-hickory forests with rhododendron and mountain laurel understory. The 2016 "
            "SE Appalachian drought fires burned over 119,000 acres across 7 states, with "
            "multiple fires in counties surrounding Asheville including the Party Rock Fire "
            "(7,171 acres near Lake Lure, 18 miles SE). In September 2024, Hurricane Helene "
            "devastated western NC with catastrophic flooding, but also created a secondary "
            "fire hazard: widespread windthrow and tree damage deposited massive quantities "
            "of woody debris on forest floors throughout the region. This storm-generated "
            "fuel loading — fallen trees, broken limbs, and tangled debris — dries faster "
            "and burns hotter than standing timber, significantly increasing wildfire risk "
            "for years following the storm. The upper French Broad watershed has experienced "
            "drought conditions 52% of weeks since 2000, and climate models project "
            "increasing drought frequency in the southern Appalachians."
        ),
        "key_features": [
            {"name": "Blue Ridge Parkway corridor", "bearing": "E/S/SW",
             "type": "ridgeline_fuel",
             "notes": "Ridgeline road through continuous forest; fire suppression has created heavy fuel; post-Helene debris loading"},
            {"name": "French Broad River valley", "bearing": "through city",
             "type": "river_valley",
             "notes": "Major valley with drought 52% of weeks since 2000; river provides some natural fire break"},
            {"name": "Pisgah National Forest", "bearing": "S/SW",
             "type": "national_forest",
             "notes": "500,000+ acres; post-Helene windthrow debris on forest floor adds massive fuel load"},
            {"name": "Post-Hurricane Helene debris field", "bearing": "throughout region",
             "type": "storm_debris",
             "notes": "2024 Hurricane Helene deposited massive woody debris across WNC forests; dries faster and burns hotter than standing timber"},
        ],
        "elevation_range_ft": (1900, 2500),
        "wui_exposure": "high — 99% of structures at some wildfire risk; expanding mountain development into forested ridgelines; post-Helene debris amplifying fuel loads",
        "historical_fires": [
            {"name": "2016 SE Appalachian Drought Fires (WNC)", "year": 2016,
             "acres": 70000, "structures_destroyed": 30, "fatalities": 0,
             "cause": "drought + arson + human negligence",
             "notes": (
                 "Over 30 forest wildfires burned 70,000+ acres in WNC mountains during "
                 "October-November 2016. Worst drought in southern Appalachians since 1895. "
                 "1,600 firefighters fought 19 fires in NC at cost of $10 million. Poor air "
                 "quality blanketed Asheville for weeks."
             )},
            {"name": "Party Rock Fire", "year": 2016, "acres": 7171,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "arson",
             "notes": (
                 "Started Nov 5 on Party Rock near Chimney Rock/Lake Lure, 18 miles SE of "
                 "Asheville. Evacuated 1,000 people in Bat Cave, Chimney Rock, and Lake Lure "
                 "areas. Contained Nov 29. Part of broader SE drought fire outbreak."
             )},
        ],
        "evacuation_routes": [
            {"route": "I-26 west", "direction": "W toward Johnson City TN",
             "lanes": 4, "bottleneck": "mountain grades on Sams Gap",
             "risk": "Interstate capacity adequate but mountain terrain; Helene damaged sections in 2024"},
            {"route": "I-40 east", "direction": "E toward Hickory/Charlotte",
             "lanes": 4, "bottleneck": "Swannanoa River gorge section",
             "risk": "Major interstate but traverses forested gorge terrain east of Asheville"},
            {"route": "I-40 west", "direction": "W toward Waynesville",
             "lanes": 4, "bottleneck": "Pigeon River gorge",
             "risk": "Deep gorge section through Pisgah NF; vulnerable to fire closure"},
            {"route": "Blue Ridge Parkway", "direction": "S/SW",
             "lanes": 2, "bottleneck": "scenic road not designed for evacuation; closed during fire events",
             "risk": "Ridgeline road through continuous forest; closed during 2016 fires"},
        ],
        "fire_spread_characteristics": (
            "Mixed hardwood-pine forest fires in steep mountain terrain with typical spread "
            "rates of 10-40 chains/hr, accelerating on south-facing slopes and in gorge "
            "terrain. Rhododendron and mountain laurel understory creates dense, difficult-to-"
            "suppress fuel. Post-Helene debris loading increases potential fire intensity by "
            "30-50% due to higher fuel density and lower moisture retention. Mountain wave "
            "wind events (similar to 2016 Gatlinburg) can produce extreme fire behavior with "
            "spotting distances of 0.5-1.0 miles."
        ),
        "infrastructure_vulnerabilities": (
            "Duke Energy and TVA power lines through mountain terrain; Helene damaged "
            "significant distribution infrastructure still being rebuilt. Water system intake "
            "on North Fork Swannanoa damaged by Helene floods. Mission Hospital (733 beds) "
            "is the regional Level II trauma center. Cell infrastructure damaged in 2024 "
            "hurricane with rebuilding ongoing."
        ),
        "demographics_risk_factors": (
            "Metro population ~470,000 with significant tourism overlay (12+ million annual "
            "visitors). Large retirement community in mountain developments. Rapid population "
            "growth pushing development into WUI zones. Post-Helene displaced residents in "
            "temporary housing may have increased vulnerability. Significant low-income "
            "communities in flood-affected areas along rivers."
        ),
    },

    # ---- 11. Blowing Rock / Banner Elk, NC ----
    "blowing_rock_nc": {
        "center": (36.135, -81.678),
        "terrain_notes": (
            "Blowing Rock and Banner Elk are small mountain communities in the High Country "
            "of northwestern North Carolina at elevations of 3,500-4,000 ft on the Blue "
            "Ridge crest. Blowing Rock (pop ~1,300) sits on a narrow ridge with the Johns "
            "River Gorge dropping steeply to the southeast and the Blue Ridge Parkway "
            "traversing nearby ridgelines. Banner Elk (pop ~1,100) occupies the Elk River "
            "valley between Beech Mountain (5,506 ft) and Grandfather Mountain (5,964 ft) "
            "in Avery County. The terrain is characterized by steep, heavily forested mountain "
            "slopes with mixed northern hardwood-oak forest including dense rhododendron and "
            "mountain laurel understory. Both communities are surrounded by Blue Ridge Parkway "
            "corridor lands, Pisgah National Forest, and Grandfather Mountain State Park. The "
            "region experienced severe wildfire during the 2016 SE Appalachian drought, with "
            "fires burning across Watauga and Avery Counties. In November 2025, a 160-acre "
            "wildfire burned in the Elk Valley community near Banner Elk — one of the most "
            "significant fires in recent High Country memory — started by debris burning from "
            "a nearby home during drought conditions. The area's fire history predates European "
            "settlement: Native Americans regularly burned these mountains, and fire exclusion "
            "has allowed mesophytic species and dense understory to encroach on formerly "
            "fire-maintained oak and pine communities on dry slopes. The combination of "
            "steep terrain, dense forest, limited road infrastructure, and growing resort and "
            "retirement development makes the High Country increasingly fire-vulnerable, "
            "especially during fall drought periods when leaf litter accumulations and low "
            "humidity create dangerous conditions."
        ),
        "key_features": [
            {"name": "Blue Ridge Parkway corridor", "bearing": "through / adjacent",
             "type": "ridgeline_fuel",
             "notes": "Scenic parkway along mountain crest; closed during fire events; forested corridor with fire-suppressed fuel loads"},
            {"name": "Grandfather Mountain / Beech Mountain", "bearing": "S and SW",
             "type": "mountain_peaks",
             "notes": "Highest peaks in the area (5,506-5,964 ft); steep forested slopes; spruce-fir forest at highest elevations"},
            {"name": "Johns River Gorge", "bearing": "SE of Blowing Rock",
             "type": "gorge_terrain",
             "notes": "Steep gorge dropping from Blue Ridge crest; chimney-effect fire behavior potential"},
            {"name": "Elk Valley community", "bearing": "near Banner Elk",
             "type": "rural_wui",
             "notes": "Site of 2025 160-acre wildfire; scattered homes in forested mountain terrain"},
        ],
        "elevation_range_ft": (3200, 4200),
        "wui_exposure": "high — resort and retirement communities expanding into forested mountain terrain along Blue Ridge crest with limited access roads",
        "historical_fires": [
            {"name": "Elk Valley Fire", "year": 2025, "acres": 160,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "escaped debris burn during drought",
             "notes": (
                 "One of the most significant wildfires in recent High Country memory. "
                 "Burned near Banner Elk in Avery County. 95% contained after 2 days. "
                 "Started from outdoor debris burning from a nearby home during drought. "
                 "Governor declared state of emergency due to statewide drought and fire."
             )},
            {"name": "2016 High Country drought fires", "year": 2016,
             "acres": 1500, "structures_destroyed": 0, "fatalities": 0,
             "cause": "drought + human causes",
             "notes": (
                 "Part of broader SE Appalachian drought fires. Blue Ridge Parkway sections "
                 "closed. Man charged in connection with NC wildfire near Parkway."
             )},
        ],
        "evacuation_routes": [
            {"route": "US-321 south", "direction": "S toward Blowing Rock / Lenoir",
             "lanes": 2, "bottleneck": "steep descent from Blue Ridge with switchbacks",
             "risk": "Winding mountain road; primary route but slow evacuation speed; fire can close road through forested terrain"},
            {"route": "NC-105 south", "direction": "S toward Boone",
             "lanes": 2, "bottleneck": "two-lane mountain road",
             "risk": "Connects Banner Elk to Boone; traverses forested mountain terrain"},
            {"route": "NC-184 (Beech Mountain Road)", "direction": "S toward Beech Mountain",
             "lanes": 2, "bottleneck": "steep narrow road to ski resort; dead end",
             "risk": "Leads to Beech Mountain ski area; dead end with limited capacity for 3,000+ seasonal residents"},
        ],
        "fire_spread_characteristics": (
            "Steep mountain terrain with hardwood-oak forest and dense rhododendron understory. "
            "Fire runs rapidly upslope on dry south- and west-facing aspects. Leaf litter "
            "accumulations of 3-6 inches after fall provide continuous surface fuel. Mountain "
            "wave wind events can produce gusts exceeding 60 mph along the Blue Ridge crest, "
            "driving fire behavior similar to the 2016 Gatlinburg event. Gorge and ravine "
            "terrain produces chimney effects. Northern hardwood composition limits crown fire "
            "but intense surface fires in drought conditions can be devastating."
        ),
        "infrastructure_vulnerabilities": (
            "Small volunteer fire departments serving large geographic areas. Rural water "
            "systems with limited pressure at higher elevations. Power lines through forested "
            "mountain terrain vulnerable to tree strikes. Cell coverage is spotty in valleys "
            "and gorges. No local hospital — Watauga Medical Center in Boone (17 miles) or "
            "Cannon Memorial in Banner Elk (critical access, 25 beds)."
        ),
        "demographics_risk_factors": (
            "Combined permanent population approximately 2,500 but ski season and summer "
            "tourism bring thousands of visitors unfamiliar with fire risk. Major second-home "
            "and vacation rental market — many properties unoccupied for weeks. Retirement "
            "community with significant elderly population. Beech Mountain seasonal residents "
            "(3,000+) on single-access road. Appalachian State University students in Boone "
            "add to regional evacuation demand."
        ),
    },

    # ---- 12. Boone, NC ----
    "boone_nc": {
        "center": (36.217, -81.674),
        "terrain_notes": (
            "Boone is a college town (pop ~20,000, plus 20,000 Appalachian State University "
            "students) at 3,333 ft elevation in the Blue Ridge Mountains of Watauga County, "
            "northwestern North Carolina. The town sits in a relatively broad mountain valley "
            "at the headwaters of the South Fork of the New River, surrounded by heavily "
            "forested ridges rising 1,000-1,500 ft above the valley floor. Watauga County's "
            "wildfire potential has increased dramatically due to a combination of factors: "
            "decades of fire suppression allowing heavy fuel accumulation in oak-hickory-pine "
            "forests; continued residential development into forested WUI zones on mountain "
            "slopes; and increasing drought frequency with climate change. Boone Fire Chief "
            "Jimmy Isaacs has publicly warned that worsening forest conditions, recent storm "
            "events, and continued development are creating a dangerous combination comparable "
            "to pre-2016 conditions that led to the Gatlinburg disaster. The 2016 Sampson Fire "
            "burned nearly 1,500 acres in eastern Watauga County, causing evacuations and "
            "requiring 150 firefighters at peak. This was one of over 30 wildfires that "
            "scorched thousands of acres across the Southeast during the 2016 drought. "
            "Watauga County coordinates fire protection through 15 fire departments and the "
            "NC Forest Service District 2, but the mountainous terrain and dispersed rural "
            "population create significant response challenges. Hurricane Helene (2024) "
            "deposited massive storm debris on forest floors throughout the county, and fire "
            "officials warn this fuel loading will remain a major threat for years. The "
            "combination of university population, tourism, retirement community, and rural "
            "residents creates complex evacuation planning challenges."
        ),
        "key_features": [
            {"name": "Blue Ridge crest", "bearing": "S/SE",
             "type": "mountain_ridgeline",
             "notes": "Blue Ridge Parkway and associated forested ridges; fire-suppressed hardwood-pine forest with heavy fuel"},
            {"name": "Howard Knob", "bearing": "NE",
             "type": "mountain_peak",
             "notes": "4,396 ft peak adjacent to town; forested slopes with WUI development"},
            {"name": "South Fork New River valley", "bearing": "through town",
             "type": "river_valley",
             "notes": "Headwaters valley; town center relatively open but ridgeline development extends into forest"},
            {"name": "Watauga County forested WUI", "bearing": "all directions",
             "type": "wui_development",
             "notes": "15 fire departments serve county; scattered development in forested terrain; post-Helene debris loading"},
        ],
        "elevation_range_ft": (3000, 3600),
        "wui_exposure": "high — college town with rapid WUI expansion into forested ridgelines; 15 fire departments serving dispersed mountain population",
        "historical_fires": [
            {"name": "Sampson Fire", "year": 2016, "acres": 1500,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "human-caused",
             "notes": (
                 "Burned nearly 1,500 acres in eastern Watauga County. Caused several "
                 "evacuations. 150 firefighters from across the US at peak. One of 30+ "
                 "wildfires across the Southeast during 2016 drought. Demonstrated "
                 "fire vulnerability of Watauga County's forested terrain."
             )},
        ],
        "evacuation_routes": [
            {"route": "US-321/421 south", "direction": "S toward Blowing Rock / Lenoir",
             "lanes": 4, "bottleneck": "steep descent off Blue Ridge; merges to 2 lanes",
             "risk": "Primary evacuation route; mountain descent with forested terrain"},
            {"route": "US-421 north", "direction": "N toward Mountain City TN",
             "lanes": 2, "bottleneck": "narrow mountain road crossing state line",
             "risk": "Winding two-lane through mountain terrain; limited capacity"},
            {"route": "NC-105 south", "direction": "S toward Banner Elk / Linville",
             "lanes": 2, "bottleneck": "mountain road through forested terrain",
             "risk": "Connects to additional mountain communities also evacuating in regional fire event"},
        ],
        "fire_spread_characteristics": (
            "Mixed hardwood-pine forest fires with moderate surface spread in leaf litter "
            "and heavy rhododendron/mountain laurel understory. Virginia pine and pitch pine "
            "on dry ridges provide ladder fuel and crown fire potential. Drought years "
            "dramatically increase fire behavior — 2016 conditions produced 30+ simultaneous "
            "fires across the region. Post-Helene debris loading increases surface fuel "
            "density and potential fire intensity. Mountain wave winds along Blue Ridge crest "
            "can produce 50+ mph gusts."
        ),
        "infrastructure_vulnerabilities": (
            "15 volunteer fire departments serve the county — coordination is complex. "
            "Watauga Medical Center (117 beds) is the only hospital. University campus "
            "requires separate evacuation planning for 20,000 students. Rural water systems "
            "with limited wildfire suppression capacity. Power lines through mountain terrain. "
            "Post-Helene infrastructure damage still being addressed."
        ),
        "demographics_risk_factors": (
            "Population ~20,000 permanent plus 20,000 university students. App State students "
            "are largely transient and may not be aware of fire risk. Tourism and second-home "
            "market brings unfamiliar visitors. Significant retirement community on mountain "
            "slopes. Rural population in dispersed homes with single-access driveways. Income "
            "varies widely from affluent second-home owners to low-income rural residents."
        ),
    },

    # ---- 9. Bryson City, NC ----
    "bryson_city_nc": {
        "center": (35.431, -83.449),
        "terrain_notes": (
            "Bryson City is a small mountain town (pop ~1,800) at 1,736 ft elevation along "
            "the Tuckasegee River in Swain County, western North Carolina. The town is "
            "uniquely positioned at the junction of three major blocks of public wildland: "
            "Great Smoky Mountains National Park to the north, Nantahala National Forest to "
            "the south and west, and additional NF parcels to the east. This placement means "
            "the community is nearly surrounded by heavily forested public land with limited "
            "fire suppression access. The Nantahala National Forest covers 531,000 acres of "
            "steep, rugged terrain with elevations ranging from 1,200 ft in the Hiwassee "
            "River valley to 5,800 ft at Lone Bald. Dense hardwood forests — predominantly "
            "oak-hickory with hemlock, poplar, and rhododendron — blanket steep mountain "
            "slopes that are deeply incised by narrow stream valleys. Firefighting access in "
            "much of this terrain requires helicopter support, as ground access is limited "
            "to few forest roads. The Alarka community near Bryson City has experienced "
            "repeated wildfire threats including the Alarka Five Fire (1,300 acres) and Sam "
            "Davis Road Fire (350+ acres) in 2025. Post-Hurricane Helene debris in the "
            "Nantahala forest has added significant fuel loading. Lightning-caused fires "
            "like the Haoe Lead Fire (3,100+ acres) demonstrate the ignition risk from the "
            "remote, high-elevation terrain surrounding the town. The Tuckasegee River "
            "valley provides the primary transportation corridor but offers limited "
            "evacuation capacity for the scattered rural population."
        ),
        "key_features": [
            {"name": "Nantahala National Forest", "bearing": "S/W/E",
             "type": "national_forest",
             "notes": "531,000 acres of steep, remote terrain; limited suppression access; helicopter-dependent firefighting"},
            {"name": "Great Smoky Mountains NP", "bearing": "N",
             "type": "national_park",
             "notes": "Northern border; same heavy fuel loading as Gatlinburg/Pigeon Forge area"},
            {"name": "Tuckasegee River valley", "bearing": "through town",
             "type": "river_valley",
             "notes": "Primary corridor and transportation route; limited evacuation capacity"},
            {"name": "Alarka community", "bearing": "W",
             "type": "rural_wui",
             "notes": "Scattered rural community with repeated fire threats; 2025 Alarka Five Fire burned 1,300 acres"},
        ],
        "elevation_range_ft": (1700, 2200),
        "wui_exposure": "high — small town nearly surrounded by public wildland (GSMNP + Nantahala NF) with limited fire suppression access in steep terrain",
        "historical_fires": [
            {"name": "Alarka Five Fire", "year": 2025, "acres": 1300,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "under investigation",
             "notes": "Swain County near Bryson City, triggered evacuations of rural communities."},
            {"name": "Sam Davis Road Fire", "year": 2025, "acres": 400,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "under investigation",
             "notes": "4 miles SW of Bryson City. Steep terrain complicated suppression."},
            {"name": "Haoe Lead Fire", "year": 2016, "acres": 3100,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "lightning",
             "notes": "Lightning-caused fire in remote Nantahala NF terrain; burned over 3,100 acres."},
            {"name": "Collett Ridge Fire", "year": 2016, "acres": 5447,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "under investigation",
             "notes": "Large fire in Nantahala NF affecting Cherokee, Macon, and Clay counties during 2016 drought."},
        ],
        "evacuation_routes": [
            {"route": "US-19 south", "direction": "S toward Andrews/Murphy",
             "lanes": 2, "bottleneck": "winding mountain road through Nantahala Gorge",
             "risk": "Traverses heavily forested gorge; potential for fire closure; slow travel speed"},
            {"route": "US-19/74 east", "direction": "E toward Sylva/Waynesville",
             "lanes": 4, "bottleneck": "divided highway but through mountain terrain",
             "risk": "Better capacity route but passes through forested mountain terrain"},
            {"route": "US-19 north", "direction": "N toward Cherokee and GSMNP",
             "lanes": 2, "bottleneck": "through national park; limited capacity",
             "risk": "Enters GSMNP territory; road potentially affected by same fire event threatening Bryson City"},
        ],
        "fire_spread_characteristics": (
            "Steep terrain with predominantly hardwood leaf litter fires augmented by "
            "rhododendron and hemlock mortality fuels. Fire runs rapidly upslope on "
            "south-facing aspects. Remote, steep, and rugged terrain in Nantahala NF makes "
            "ground-based suppression extremely difficult — helicopter bucket drops are often "
            "the only option. Post-Helene storm debris adds additional fuel loading. Gorge "
            "terrain produces chimney effects that accelerate fire spread."
        ),
        "infrastructure_vulnerabilities": (
            "Small volunteer fire department for large geographic area. Rural water system with "
            "limited pressure. Emergency communications hampered by mountain terrain. No local "
            "hospital — nearest is Harris Regional in Sylva, 15 miles east. Many rural roads "
            "have single access points."
        ),
        "demographics_risk_factors": (
            "Population ~1,800 in town, ~15,000 in Swain County. Significant Eastern Band of "
            "Cherokee Indian population on adjacent Qualla Boundary. Tourism economy brings "
            "visitors unfamiliar with fire risk. Low-income county with limited resources for "
            "defensible space creation. Many elderly residents in remote mountain homes."
        ),
    },

    # ---- 10. Lake Lure / Chimney Rock, NC ----
    "lake_lure_nc": {
        "center": (35.428, -82.205),
        "terrain_notes": (
            "Lake Lure and Chimney Rock are small communities (combined pop ~2,500) nestled "
            "in Hickory Nut Gorge, a dramatic canyon carved deep into the Blue Ridge "
            "Escarpment in Rutherford County, North Carolina. The gorge features sheer rock "
            "faces and forested slopes rising 2,000+ ft above the valley floor, with Chimney "
            "Rock — a 315-ft granite monolith — serving as the iconic landmark. Lake Lure "
            "itself is a 720-acre reservoir created by a 1920s dam on the Broad River, "
            "surrounded by steep, forested slopes. The gorge terrain creates extraordinary "
            "fire behavior: narrow canyon walls channel and accelerate wind, creating chimney "
            "effects that drive fire rapidly upslope; thermal convection columns are "
            "intensified by the confined airspace; and suppression access is severely limited "
            "by the steep, rocky terrain. The 2016 Party Rock Fire (7,171 acres) demonstrated "
            "these dynamics, starting atop Party Rock — a popular camping spot overlooking "
            "Chimney Rock State Park — and burning through the gorge for weeks, forcing "
            "evacuation of 1,000 people. In September 2024, Hurricane Helene caused "
            "catastrophic flooding in the Broad River watershed, with nearly two feet of rain "
            "in some areas devastating both communities. Landslides stripped vegetation from "
            "slopes and deposited massive debris fields. This post-Helene landscape presents "
            "a compounded fire risk: exposed mineral soil on landslide scars, extensive "
            "blowdown and debris loading on remaining forested slopes, damaged road "
            "infrastructure limiting evacuation, and compromised water systems. State fire "
            "officials have warned that post-Helene conditions in the gorge significantly "
            "elevate wildfire risk for years to come."
        ),
        "key_features": [
            {"name": "Hickory Nut Gorge", "bearing": "E-W through community",
             "type": "narrow_canyon",
             "notes": "Deep gorge with 2,000+ ft walls; chimney effect on fire behavior; severely limited suppression access"},
            {"name": "Chimney Rock / Party Rock", "bearing": "N side of gorge",
             "type": "rock_formation",
             "notes": "315-ft granite monolith; Party Rock was origin of 2016 fire; state park surrounding"},
            {"name": "Lake Lure reservoir", "bearing": "center of community",
             "type": "reservoir",
             "notes": "720-acre lake provides fire break on water but surrounding slopes are steep forest; dam damaged by Helene"},
            {"name": "Post-Helene debris and landslide scars", "bearing": "throughout gorge",
             "type": "storm_debris",
             "notes": "Hurricane Helene (2024) stripped vegetation, caused landslides, deposited massive woody debris on slopes"},
        ],
        "elevation_range_ft": (900, 1300),
        "wui_exposure": "extreme — residential development in narrow gorge with 2,000 ft walls, limited access, and compounded post-hurricane fire risk",
        "historical_fires": [
            {"name": "Party Rock Fire", "year": 2016, "acres": 7171,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "arson",
             "notes": (
                 "Started Nov 5 on Party Rock, a popular camping/hiking spot above Chimney Rock "
                 "State Park. Burned for nearly a month in steep gorge terrain. Evacuated 1,000 "
                 "people from Bat Cave, Chimney Rock, and Lake Lure. Contained Nov 29. Managed "
                 "by NC Type 2 Incident Management Team. Part of 2016 SE drought fire outbreak. "
                 "Fire behavior intensified in gorge terrain with updraft chimney effects."
             )},
        ],
        "evacuation_routes": [
            {"route": "US-64/74A east", "direction": "E toward Rutherfordton",
             "lanes": 2, "bottleneck": "winding road through gorge; Helene damage to roadbed",
             "risk": "Primary route east through the gorge; road infrastructure damaged by 2024 hurricane; slow and narrow"},
            {"route": "NC-9 north", "direction": "N toward Bat Cave / Black Mountain",
             "lanes": 2, "bottleneck": "narrow mountain road",
             "risk": "Alternate route but winding through steep terrain; limited capacity"},
            {"route": "Buffalo Creek Road / local roads", "direction": "various",
             "lanes": 2, "bottleneck": "narrow rural roads, many unpaved",
             "risk": "Secondary roads in poor condition, many damaged by Helene; single-access dead ends common"},
        ],
        "fire_spread_characteristics": (
            "Gorge terrain produces extreme chimney-effect fire behavior. Narrow canyon walls "
            "concentrate convective heat and channel wind, driving fire upslope at rates far "
            "exceeding open-terrain predictions. The Party Rock Fire demonstrated sustained "
            "upslope runs driven by thermal convection. Post-Helene debris loading adds "
            "significant surface fuel. Exposed landslide mineral soil temporarily reduces fuel "
            "continuity but surrounding forest debris compensates. Spotting across the gorge "
            "from one wall to another is possible with wind-driven ember transport."
        ),
        "infrastructure_vulnerabilities": (
            "Post-Helene road damage severely limits evacuation capacity and fire apparatus "
            "access. Water infrastructure was damaged by flooding; rebuilt capacity uncertain. "
            "Power lines along gorge roads are vulnerable. Cell towers on ridges were damaged. "
            "No local hospital — nearest is Rutherford Regional, 20+ miles east. Town of Lake "
            "Lure and Chimney Rock Village have minimal fire department resources for "
            "wildland fire events."
        ),
        "demographics_risk_factors": (
            "Combined population approximately 2,500 permanent residents. Significant tourist "
            "population visiting Chimney Rock State Park, Lake Lure beach, and filming "
            "locations (Dirty Dancing, Last of the Mohicans). Many seasonal/vacation homes. "
            "Elderly resident population in lakeside and mountain homes. Post-Helene displaced "
            "residents further complicate emergency planning."
        ),
    },

    # =========================================================================
    # GEORGIA (1 cities)
    # =========================================================================

    # ---- 13. Athens, GA ----
    "athens_ga": {
        "center": (33.961, -83.378),
        "terrain_notes": (
            "Athens-Clarke County is a consolidated city-county (pop ~128,000) in the "
            "northeastern Georgia Piedmont at 764 ft elevation, home to the University of "
            "Georgia. The terrain is rolling Piedmont hills transitioning toward the "
            "Appalachian foothills to the north and northeast. Mixed pine-hardwood forests "
            "cover approximately 40% of the county, with loblolly pine, shortleaf pine, "
            "and various oaks dominating. While the city proper has relatively moderate fire "
            "risk, Athens serves as the gateway to northeastern Georgia's highly fire-"
            "vulnerable mountain counties (Rabun, Lumpkin, Dawson, White, Union) where the "
            "Chattahoochee-Oconee National Forest covers 750,000+ acres of steep, forested "
            "terrain. The Oconee National Forest, south of Athens, is the primary Piedmont "
            "national forest and supports significant prescribed fire research at the Athens "
            "Prescribed Fire Lab — a hub with seven scientists studying fire ecology in "
            "Southern Appalachian and Piedmont ecosystems. Georgia's Piedmont forests evolved "
            "with fire on a 2-5 year return interval; decades of suppression have created "
            "heavy fuel accumulation and shifted species composition toward fire-intolerant "
            "mesophytic species. The 2016 drought fire season devastated northeast Georgia "
            "with over 40,000 acres burned, including the Rough Ridge Fire (28,000 acres) in "
            "the Cohutta Wilderness. Firefighters from 21 states responded. Athens itself "
            "experienced smoke impacts and served as a staging area for fire response. The "
            "growing WUI in the NE Georgia foothills — where suburban development from the "
            "Atlanta metro area is pushing into forested mountain terrain — represents one "
            "of the fastest-growing fire risk zones in the southeastern United States."
        ),
        "key_features": [
            {"name": "Chattahoochee National Forest", "bearing": "N/NE",
             "type": "national_forest",
             "notes": "750,000+ acres in N Georgia mountains; Rough Ridge Fire (2016) burned 28,000 acres in Cohutta Wilderness"},
            {"name": "Oconee National Forest", "bearing": "S",
             "type": "national_forest",
             "notes": "Piedmont national forest; major prescribed fire research site; fire-suppressed pine-hardwood"},
            {"name": "NE Georgia foothills WUI", "bearing": "N/NE",
             "type": "expanding_wui",
             "notes": "Rapid suburban development from Atlanta metro pushing into forested mountain terrain; fastest-growing fire risk in SE US"},
            {"name": "Athens Prescribed Fire Lab", "bearing": "in Athens",
             "type": "research_facility",
             "notes": "Seven-scientist fire research hub; prescribed fire ecology for SE ecosystems"},
        ],
        "elevation_range_ft": (600, 900),
        "wui_exposure": "moderate locally, extreme regionally — Athens itself moderate but serves as proxy for NE Georgia foothills with rapidly expanding WUI",
        "historical_fires": [
            {"name": "Rough Ridge Fire", "year": 2016, "acres": 28000,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "human-caused",
             "notes": (
                 "Cohutta Wilderness in N Georgia. One of the largest fires ever recorded "
                 "in Georgia. Part of 2016 SE drought fire outbreak. Burned for weeks in "
                 "remote, steep terrain."
             )},
            {"name": "2016 NE Georgia fires (combined)", "year": 2016,
             "acres": 40000, "structures_destroyed": 12, "fatalities": 0,
             "cause": "drought + multiple human causes",
             "notes": (
                 "Over 40,000 acres burned across NE Georgia counties during extreme fall "
                 "drought. ~12 homes destroyed. Firefighters from 21 states responded. "
                 "Worst fire season in Georgia in decades."
             )},
        ],
        "evacuation_routes": [
            {"route": "US-441/GA-15 north", "direction": "N toward NE Georgia mountains",
             "lanes": 2, "bottleneck": "mountain highway with limited passing",
             "risk": "Corridor into fire-prone NE Georgia; more relevant for mountain communities than Athens proper"},
            {"route": "GA-316 / US-78 west", "direction": "W toward Atlanta",
             "lanes": 4, "bottleneck": "metro congestion approaching Atlanta",
             "risk": "Good capacity route away from fire-prone areas"},
            {"route": "US-29/78 east", "direction": "E toward Augusta",
             "lanes": 2, "bottleneck": "two-lane through rural Piedmont",
             "risk": "Traverses pine-hardwood Piedmont with moderate fire risk"},
        ],
        "fire_spread_characteristics": (
            "Piedmont pine-hardwood fires typically spread at 5-20 chains/hr in leaf litter "
            "and pine needle fuels under normal conditions. In the NE Georgia mountains, "
            "steep terrain and drought conditions dramatically increase spread rates. The "
            "Rough Ridge Fire demonstrated sustained crown fire runs in dense mountain forest. "
            "Piedmont fires can be intense in loblolly pine stands with heavy needle litter "
            "and understory brush accumulated from fire suppression."
        ),
        "infrastructure_vulnerabilities": (
            "NE Georgia mountain communities have limited fire department resources — mostly "
            "volunteer departments. Rural water systems with low pressure. Narrow mountain "
            "roads limit evacuation and fire apparatus access. Athens itself has adequate "
            "urban infrastructure but serves as the regional hospital hub (Piedmont Athens "
            "Regional, 350 beds) for NE Georgia mountain counties."
        ),
        "demographics_risk_factors": (
            "Athens pop ~128,000 including 40,000 UGA students. NE Georgia mountain "
            "communities have growing retirement and second-home populations. Significant "
            "low-income rural populations in mountain counties. Tourism in mountain areas "
            "brings visitors unfamiliar with fire risk."
        ),
    },

    # =========================================================================
    # FLORIDA (1 cities)
    # =========================================================================

    # ---- 14. Panama City, FL ----
    "panama_city_fl": {
        "center": (30.160, -85.660),
        "terrain_notes": (
            "Panama City is a Gulf Coast city (pop ~37,000, metro ~180,000) at near sea "
            "level in Bay County, Florida Panhandle. The surrounding landscape is dominated "
            "by fire-adapted and fire-dependent ecosystems: longleaf pine flatwoods, slash "
            "pine plantations, palmetto scrub, and sand pine scrub. Florida is the nation's "
            "top prescribed burn state (~2.3 million acres/year) because without regular fire "
            "on a 1-4 year cycle, palmetto and gallberry understory can reach 15+ ft and "
            "becomes explosively flammable. In October 2018, Hurricane Michael made landfall "
            "as a Category 5 hurricane near Mexico Beach (just east of Panama City) with "
            "161 mph sustained winds, devastating 2.8 million acres of forest across the "
            "Panhandle. Post-hurricane surveys found over 100 tons per acre of fuel in some "
            "areas — compared to typical loads of less than 10 tons per acre. This 10x fuel "
            "load increase fundamentally altered the fire risk landscape for years. The dead "
            "and damaged standing timber dries into resinous tinder, with dripping pine resin "
            "from structural damage creating vertical fuel pathways that carry surface fires "
            "into the canopy. In March 2022, three wildfires blazed through over 34,000 acres "
            "in the Florida Panhandle, gorging on Hurricane Michael's legacy fuel load and "
            "forcing 1,100+ evacuations. Fire managers reported that areas previously used as "
            "natural fire breaks (hardwood hammocks, creeks, ravines, swamps) no longer "
            "functioned because canopy damage and debris filled these features. The "
            "combination of a fire-dependent ecosystem, catastrophic hurricane fuel loading, "
            "disrupted fire break networks, and growing suburban development creates a "
            "compounded fire risk that is likely the highest in the eastern United States."
        ),
        "key_features": [
            {"name": "Pine flatwoods ecosystem", "bearing": "N/NE/E",
             "type": "fire_dependent_ecosystem",
             "notes": "Longleaf and slash pine with palmetto understory; burn interval 18 months to 4 years; without fire, explosive fuel buildup"},
            {"name": "Hurricane Michael debris zone", "bearing": "all directions",
             "type": "storm_debris",
             "notes": "Cat 5 hurricane (2018) devastated 2.8M acres of forest; 100+ tons/acre fuel load vs normal 10 tons; resinous dead standing timber"},
            {"name": "Tyndall AFB and surrounding wildland", "bearing": "E",
             "type": "military_wildland",
             "notes": "Large undeveloped tracts of pine flatwoods on military lands; burned during 2022 Panhandle fires"},
            {"name": "St. Andrews Bay / Gulf Coast", "bearing": "S",
             "type": "water_boundary",
             "notes": "Provides natural fire break to south; evacuation to coast possible"},
        ],
        "elevation_range_ft": (0, 50),
        "wui_exposure": "extreme — fire-dependent ecosystem with catastrophic hurricane fuel loading (10x normal); disrupted natural fire breaks; expanding suburban development",
        "historical_fires": [
            {"name": "2022 Panhandle Wildfires", "year": 2022, "acres": 34000,
             "structures_destroyed": 100, "fatalities": 0,
             "cause": "various — exploiting Hurricane Michael debris fuel",
             "notes": (
                 "Three major wildfires in March 2022 across the FL Panhandle, burning over "
                 "34,000 acres and forcing 1,100+ evacuations. Fires gorged on downed timber "
                 "from Hurricane Michael (2018). Fire behavior was extreme — natural fire "
                 "breaks (hammocks, creeks, ravines) no longer functioned due to hurricane "
                 "debris filling these features."
             )},
            {"name": "1998 Florida fire season", "year": 1998,
             "acres": 500000, "structures_destroyed": 337, "fatalities": 0,
             "cause": "drought + various ignitions",
             "notes": (
                 "Worst Florida fire season on record. Over 500,000 acres burned statewide. "
                 "Crown fires in heavy palmetto scrub and pine flatwoods across NE and "
                 "central FL. I-95 closed for days."
             )},
        ],
        "evacuation_routes": [
            {"route": "US-231 north", "direction": "N toward Dothan AL",
             "lanes": 4, "bottleneck": "crosses fire-prone pine flatwoods for 30+ miles",
             "risk": "Primary inland evacuation; traverses the worst hurricane-debris fuel loading zone"},
            {"route": "US-98 west", "direction": "W toward Destin/Pensacola",
             "lanes": 4, "bottleneck": "coastal congestion; shared hurricane evacuation route",
             "risk": "Coastal route; also used for hurricane evacuations creating dual-hazard demand conflicts"},
            {"route": "US-98 east", "direction": "E toward Port St. Joe / Apalachicola",
             "lanes": 2, "bottleneck": "two-lane through hurricane-damaged communities",
             "risk": "Passes through Mexico Beach area with extensive hurricane damage; limited capacity"},
        ],
        "fire_spread_characteristics": (
            "Pine flatwoods fire with palmetto understory produces intense surface fire with "
            "flame lengths of 10-25 ft when fuel loads are normal. Post-hurricane fuel loading "
            "(100+ tons/acre) produces fire behavior that is qualitatively different: resinous "
            "dead standing pine acts as vertical fuel pathways carrying surface fire to canopy; "
            "torching and spotting are dramatically increased; natural fire breaks no longer "
            "function because debris fills creeks, ravines, and hammocks. Wind-driven crown "
            "fire runs in pine flatwoods can exceed 100 chains/hr. Sand pine scrub produces "
            "stand-replacing crown fire by design."
        ),
        "infrastructure_vulnerabilities": (
            "Post-Hurricane Michael, significant infrastructure was rebuilt but the surrounding "
            "forest fuel load remains extreme. Gulf Power/NextEra overhead lines through pine "
            "flatwoods create ignition risk. Bay County water system serves dispersed suburban "
            "development with limited hydrant coverage at WUI edge. Tyndall AFB was severely "
            "damaged by Michael and reconstruction is ongoing. Bay Medical Center (323 beds) "
            "serves the region."
        ),
        "demographics_risk_factors": (
            "Metro population ~180,000. Significant military population at Tyndall AFB. "
            "Tourism economy (Panama City Beach) brings visitors during fire-prone spring "
            "season. Low-to-moderate income levels in many areas. Mobile home stock throughout "
            "Bay County. Post-hurricane displaced populations in temporary and rebuilt housing "
            "may have heightened vulnerability."
        ),
    },

    # =========================================================================
    # SOUTH DAKOTA (BLACK HILLS) (8 cities)
    # =========================================================================

    # ---- 16. Custer, SD ----
    "custer_sd": {
        "center": (43.767, -103.599),
        "terrain_notes": (
            "Custer is a small town (pop ~2,000) at 5,315 ft in the southern Black Hills, "
            "named after General George Armstrong Custer whose 1874 expedition discovered "
            "gold here. The town sits in a relatively open valley but is completely encircled "
            "by dense ponderosa pine forest, granite spires, and narrow canyons. Custer State "
            "Park (71,000 acres) lies to the east and northeast, Wind Cave National Park "
            "(28,295 acres) to the southeast, and Black Hills National Forest on all other "
            "sides. The Needles Highway area to the northeast features narrow granite spires "
            "rising from dense pine forest — extremely difficult terrain for fire suppression "
            "with limited ground access and treacherous slopes. The Jasper Fire (2000) — the "
            "largest wildfire in South Dakota and Black Hills history at 83,508 acres — burned "
            "through terrain just west and south of Custer, coming within 6 miles of the town. "
            "At its peak, the Jasper Fire consumed 100 acres per minute. The Legion Lake Fire "
            "(2017, 53,875 acres) burned directly through Custer State Park and Wind Cave NP, "
            "starting when high winds knocked a 70-foot ponderosa pine onto a Black Hills "
            "Energy power line at Wilson's Corner on Needles Highway. That fire occurred in "
            "December, demonstrating year-round fire potential in the Black Hills. Custer sits "
            "at the nexus of these two massive burn scars, and while regeneration is occurring, "
            "the combination of young growth, dead standing timber, and adjacent unburned "
            "dense forest creates a complex and dangerous fuel mosaic. The town's valley "
            "position with forested ridges on all sides means fire can approach from any "
            "direction with limited warning time."
        ),
        "key_features": [
            {"name": "Custer State Park", "bearing": "E/NE",
             "type": "state_park",
             "notes": "71,000 acres; Legion Lake Fire (2017) burned 53,875 acres through park; ponderosa pine and grassland"},
            {"name": "Needles Highway / granite spires", "bearing": "NE",
             "type": "rugged_terrain",
             "notes": "Narrow granite spires in dense pine; extremely difficult suppression; Legion Lake Fire originated here"},
            {"name": "Wind Cave NP", "bearing": "SE",
             "type": "national_park",
             "notes": "28,295 acres of mixed pine/grassland; Cold Fire (2016) burned 1,300 acres; prescribed fire escapes have occurred"},
            {"name": "Jasper Fire scar", "bearing": "W/SW",
             "type": "burn_scar",
             "notes": "83,508-acre 2000 burn scar with regenerating young growth; altered fuel structure on western approach"},
        ],
        "elevation_range_ft": (5100, 5600),
        "wui_exposure": "extreme — town completely encircled by fire-prone forest; within 6 miles of largest SD wildfire ever; two massive burn scars within 10 miles",
        "historical_fires": [
            {"name": "Jasper Fire", "year": 2000, "acres": 83508,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "arson (sentenced to 25 years)",
             "notes": (
                 "Largest wildfire in SD and Black Hills history. Burned Aug 24 - Sep 25, 2000. "
                 "Arsonist Janice Stevenson dropped a lit match while stopped on a road west of "
                 "Hell Canyon. Burned 100 acres/minute at peak. Came within 6 miles of Custer. "
                 "1,160 firefighters deployed. $8.2M suppression cost. 224 million board-feet "
                 "timber consumed. Burned 90% of Jewel Cave NM."
             )},
            {"name": "Legion Lake Fire", "year": 2017, "acres": 53875,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "wind-downed tree on power line",
             "notes": (
                 "Started Dec 11 when 70-ft ponderosa hit Black Hills Energy line at Wilson's "
                 "Corner on Needles Highway. Burned through Custer State Park and Wind Cave NP. "
                 "Third-largest fire in SD/Black Hills history. December fire — demonstrating "
                 "year-round risk. Ponderosa pine is fire-resistant due to thick bark but "
                 "dense young stands are extremely vulnerable."
             )},
        ],
        "evacuation_routes": [
            {"route": "US-16A east", "direction": "E toward Mt Rushmore / Keystone",
             "lanes": 2, "bottleneck": "winding road through Custer State Park forest",
             "risk": "Traverses fire-prone park; Iron Mountain Road section is narrow with pigtail bridges"},
            {"route": "US-385 south", "direction": "S toward Hot Springs",
             "lanes": 2, "bottleneck": "two-lane through forest transitioning to grassland",
             "risk": "Passes through pine-grassland transition zone; fire can cross road"},
            {"route": "US-16 west", "direction": "W toward Jewel Cave / Newcastle WY",
             "lanes": 2, "bottleneck": "narrow road through continuous forest",
             "risk": "Traverses Jasper Fire burn scar with regenerating fuel"},
        ],
        "fire_spread_characteristics": (
            "Ponderosa pine crown fire in dense stands with extreme behavior. Jasper Fire "
            "burned 100 acres/minute at peak — among the fastest fire spread documented in "
            "the Black Hills. Torching, spotting, and crown fire runs are the dominant "
            "fire behavior modes. Legion Lake Fire demonstrated that wind-downed power lines "
            "are a significant ignition source. Year-round fire potential: December fires "
            "in cured grass beneath pine canopy can produce rapid runs. Needles terrain "
            "creates extreme fire behavior with canyon chimney effects."
        ),
        "infrastructure_vulnerabilities": (
            "Black Hills Energy overhead power lines caused the Legion Lake Fire. Small-town "
            "water system with limited wildfire suppression capacity. Volunteer fire department "
            "for large surrounding area. No local hospital — Custer Regional (25 beds, critical "
            "access) provides basic care; nearest full hospital is Monument Health in Rapid "
            "City, 35 miles north. Limited cell coverage in surrounding forest."
        ),
        "demographics_risk_factors": (
            "Population ~2,000 permanent but Custer State Park draws 2+ million annual visitors. "
            "Tourism infrastructure (hotels, campgrounds, cabins) increases exposure. Aging "
            "population in town. Many seasonal and recreational properties in surrounding "
            "forest. Motorcycle tourists (Sturgis rally) bring additional summer visitors."
        ),
    },

    # ---- 17. Deadwood / Lead, SD ----
    "deadwood_sd": {
        "center": (44.377, -103.730),
        "terrain_notes": (
            "Deadwood (pop ~1,300) and Lead (pop ~3,000) are historic mining towns in the "
            "northern Black Hills, sitting at 4,531 ft and 5,280 ft respectively in steep, "
            "V-shaped gulches carved into the Hills. Deadwood occupies the bottom of a narrow "
            "canyon formed by Whitewood Creek, with dense ponderosa pine forest on both sides "
            "rising 500-1,000 ft above the valley floor. The canyon topography creates extreme "
            "fire behavior — during the 2002 Grizzly Gulch Fire, firefighters observed 200-"
            "foot flame lengths as fire raced through the narrow gulch. The town's historic "
            "wooden buildings (1876 Gold Rush era), tight streets, and severely limited road "
            "access make it exceptionally vulnerable to wildfire. Lead, 3 miles south in "
            "similar terrain, was the site of the Homestake Gold Mine — the deepest mine in "
            "North America. The Northern Hills Ranger District of BHNF surrounds both "
            "communities with dense ponderosa pine that has accumulated decades of fire "
            "suppression fuel loading. The Grizzly Gulch Fire (2002) burned 11,500 acres "
            "across national forest and private land, destroying 7 homes and forcing "
            "evacuation of 10,000-15,000 people (mostly tourists visiting Deadwood's casinos). "
            "The fire exhibited extreme behavior: torching, spotting, crown runs, and the "
            "200-ft flame lengths. Black Hills Power lines were suspected as the ignition "
            "source and the utility paid $5.9M in settlements. Since 2002, Deadwood has "
            "invested heavily in a Firewise fuels reduction program, creating defensible "
            "space around the historic district and thinning adjacent forest. However, the "
            "fundamental vulnerability remains: a town built in a narrow, forested canyon "
            "with limited egress. The same chimney-effect dynamics that make Gatlinburg "
            "vulnerable apply here — but the canyon is even narrower."
        ),
        "key_features": [
            {"name": "Deadwood Gulch / Whitewood Creek canyon", "bearing": "through town",
             "type": "narrow_canyon",
             "notes": "Town built in narrow V-shaped gulch; 500-1,000 ft forested walls; chimney effect worse than Gatlinburg (narrower canyon)"},
            {"name": "Northern Hills ponderosa pine", "bearing": "all sides",
             "type": "dense_conifer_forest",
             "notes": "Dense ponderosa pine on steep canyon walls; fire-suppressed with extreme fuel loading; 200-ft flames observed in 2002"},
            {"name": "Historic district (National Historic Landmark)", "bearing": "center",
             "type": "dense_historic_structures",
             "notes": "1876-era wooden buildings; tight streets; Firewise program since 2002 but fundamental vulnerability remains"},
            {"name": "Lead / Homestake mining complex", "bearing": "S",
             "type": "adjacent_community",
             "notes": "3 miles south in similar gulch terrain; combined evacuation demand of 4,300+ residents plus tourists"},
        ],
        "elevation_range_ft": (4400, 5300),
        "wui_exposure": "extreme — historic wooden town in narrow forested canyon with 200-ft flame lengths observed during 2002 fire; chimney-effect terrain",
        "historical_fires": [
            {"name": "Grizzly Gulch Fire", "year": 2002, "acres": 11500,
             "structures_destroyed": 7, "fatalities": 0,
             "cause": "suspected power line (BHP paid $5.9M settlement)",
             "notes": (
                 "Started June 29, burned 13 days. 3,315 acres of NF land on Northern Hills "
                 "Ranger District. 200-foot flame lengths observed. Extreme behavior: torching, "
                 "spotting, crown runs. Evacuated 10,000-15,000 people (mostly tourists). "
                 "7 homes destroyed. $5.5M damage. Catalyzed Deadwood's Firewise program."
             )},
            {"name": "1893 Black Hills fires", "year": 1893, "acres": 0,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "various",
             "notes": "Large forest fires threatened mining camps including Deadwood and Lead."},
        ],
        "evacuation_routes": [
            {"route": "US-85 north", "direction": "N toward Spearfish / I-90",
             "lanes": 2, "bottleneck": "narrow canyon road; only route north for 15 miles",
             "risk": "Primary evacuation route; traverses forested canyon; if fire blocks, no alternative north"},
            {"route": "US-85/14A south", "direction": "S through Lead toward Cheyenne Crossing",
             "lanes": 2, "bottleneck": "winding road through Lead and dense forest",
             "risk": "Through Lead (additional 3,000 evacuees) and into continuous forest; slow and congested"},
            {"route": "US-385 south", "direction": "S toward Hill City",
             "lanes": 2, "bottleneck": "narrow road through forest interior",
             "risk": "Enters deeper into Black Hills fire-prone terrain; not ideal evacuation direction"},
        ],
        "fire_spread_characteristics": (
            "Extreme fire behavior in narrow canyon terrain. The 2002 Grizzly Gulch Fire "
            "produced 200-foot flame lengths — among the most extreme documented in the Black "
            "Hills. Canyon topography channels wind and concentrates convective heat, creating "
            "fire whirls and extreme updrafts. Torching, spotting, and crown fire runs in "
            "dense ponderosa pine. Spotting distances of 0.5-1.0 miles documented. Firewise "
            "fuels reduction since 2002 has improved conditions immediately around town but "
            "surrounding forest retains extreme fuel loads."
        ),
        "infrastructure_vulnerabilities": (
            "Black Hills Energy / Black Hills Power overhead lines through forested canyons "
            "suspected in 2002 fire. Limited water system pressure in upper elevations. "
            "Historic wooden structures despite Firewise upgrades. Volunteer fire department "
            "supplemented by gaming industry resources. No local hospital — Northern Hills "
            "General Hospital in Lead, 3 miles south (limited capacity)."
        ),
        "demographics_risk_factors": (
            "Combined Deadwood-Lead permanent population ~4,300 but Deadwood's casinos draw "
            "1+ million annual visitors. Tourist population unfamiliar with fire risk or "
            "canyon evacuation routes. Aging permanent population. Low-income residents in "
            "Lead. Sturgis motorcycle rally visitors transit through on way to Northern Hills."
        ),
    },

    # ---- 21. Hill City, SD ----
    "hill_city_sd": {
        "center": (43.932, -103.572),
        "terrain_notes": (
            "Hill City (pop ~1,000) sits at 4,979 ft in the geographic center of the Black "
            "Hills along Spring Creek, surrounded by dense ponderosa pine forest of the "
            "Black Hills National Forest. The town is at the heart of the Jasper Fire (2000) "
            "burn area — the 83,508-acre fire, the largest in Black Hills history, burned "
            "extensively in the terrain surrounding Hill City, particularly to the west and "
            "south. Twenty-five years later, the burn scar is regenerating with young "
            "ponderosa pine growth that is itself creating new fuel continuity, while "
            "adjacent unburned stands retain the dense, fire-suppressed conditions that "
            "fueled the original fire. Hill City serves as a central hub for Black Hills "
            "tourism, with the 1880 Train (historic narrow-gauge railroad) running between "
            "Hill City and Keystone through continuous ponderosa pine forest. The town is "
            "also the gateway to Crazy Horse Memorial (9 million tons of rock blasted so "
            "far) and Sylvan Lake in Custer State Park. The surrounding terrain is "
            "moderately steep with granite outcrops and pine-covered slopes. Spring Creek "
            "runs through town providing a narrow natural fire break but the creek valley "
            "also channels wind from the southwest. The Jasper Fire burned 90% of Jewel "
            "Cave National Monument just to the southwest, demonstrating the scale of fire "
            "that can develop in this terrain under extreme conditions. The USGS has "
            "conducted extensive post-fire fuels research in the Jasper Fire area, with "
            "data collection continuing through 2023-2024, indicating the ongoing scientific "
            "and management significance of this landscape."
        ),
        "key_features": [
            {"name": "Jasper Fire burn scar", "bearing": "W/SW/S",
             "type": "burn_scar",
             "notes": "83,508-acre 2000 burn area; regenerating young ponderosa creating new fuel; USGS fuels research ongoing through 2024"},
            {"name": "Black Hills NF central forest", "bearing": "all directions",
             "type": "dense_conifer_forest",
             "notes": "Unburned stands adjacent to Jasper scar retain dense fire-suppressed conditions; continuous fuel"},
            {"name": "1880 Train corridor", "bearing": "E toward Keystone",
             "type": "transportation_corridor",
             "notes": "Historic narrow-gauge railroad through continuous ponderosa pine; tourist attraction with limited emergency capacity"},
            {"name": "Spring Creek valley", "bearing": "through town",
             "type": "river_valley",
             "notes": "Narrow valley providing partial fire break; channels SW wind toward town"},
        ],
        "elevation_range_ft": (4800, 5200),
        "wui_exposure": "high — small town at center of Jasper Fire burn scar with regenerating and adjacent unburned dense forest on all sides",
        "historical_fires": [
            {"name": "Jasper Fire", "year": 2000, "acres": 83508,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "arson",
             "notes": (
                 "Largest wildfire in SD and Black Hills history. Burned extensively around "
                 "Hill City, particularly W and S of town. Burned 90% of Jewel Cave NM. "
                 "100 acres/minute at peak. Town was threatened but not entered. USGS "
                 "continues fuels research in burn area through 2024."
             )},
        ],
        "evacuation_routes": [
            {"route": "US-16/385 north", "direction": "N toward Rapid City",
             "lanes": 2, "bottleneck": "through forest for 20 miles",
             "risk": "Primary route; traverses continuous ponderosa forest; potentially blocked by fire from BHNF"},
            {"route": "US-16/385 south", "direction": "S toward Custer",
             "lanes": 2, "bottleneck": "through Jasper Fire burn scar and regenerating forest",
             "risk": "Traverses Jasper Fire terrain; young growth creating new fuel continuity"},
            {"route": "Deerfield Road west", "direction": "W toward Deerfield Reservoir",
             "lanes": 2, "bottleneck": "narrow forest road; limited throughput",
             "risk": "Leads deeper into forest interior; not a viable mass evacuation route"},
        ],
        "fire_spread_characteristics": (
            "Complex fuel mosaic of regenerating Jasper Fire young growth and adjacent unburned "
            "dense ponderosa stands. Young pine plantations (20-25 years post-fire) can "
            "produce intense fire when they reach pole-stage density. Unburned adjacent stands "
            "retain extreme fuel loads. The Jasper Fire demonstrated 100 acres/minute spread "
            "rates in this terrain. Wind from the southwest channels through Spring Creek "
            "valley toward town."
        ),
        "infrastructure_vulnerabilities": (
            "Small-town infrastructure. Limited water system for wildland fire suppression. "
            "Volunteer fire department. Power lines through forested terrain. 1880 Train "
            "tracks create access corridors but are not useful for evacuation. No hospital — "
            "nearest is Custer Regional (25 beds) 12 miles south or Rapid City 25 miles north."
        ),
        "demographics_risk_factors": (
            "Permanent population ~1,000 but tourism brings thousands daily in summer. "
            "Crazy Horse Memorial and 1880 Train are major draws. Motorcycle tourists "
            "during Sturgis rally. Small elderly resident population."
        ),
    },

    # ---- 18. Hot Springs, SD ----
    "hot_springs_sd": {
        "center": (43.432, -103.474),
        "terrain_notes": (
            "Hot Springs is a small city (pop ~3,500) at 3,464 ft in the southern Black "
            "Hills, named for its natural warm springs along the Fall River. The town "
            "occupies a transition zone where the ponderosa pine forest of the Black Hills "
            "gives way to mixed-grass prairie of the Great Plains. This ecotone position "
            "creates unique fire dynamics: grass fires from the plains can run into pine "
            "forest and produce explosive behavior changes, while forest fires can emerge "
            "from the Hills and race across grassland. Wind Cave National Park (28,295 "
            "acres) lies directly to the north and northwest, with mixed pine and grassland "
            "extending to the edge of the town. The park has experienced multiple fire "
            "events including the Cold Fire (2016, 1,300 acres), which was a prescribed "
            "burn that escaped, and the western extent of the Legion Lake Fire (2017, "
            "53,875 acres). The Alabaugh Fire (2007, 10,324 acres) started just 3 miles "
            "southwest of Hot Springs on a day when temperature reached 109F and relative "
            "humidity was 6% — extreme fire weather that is becoming more frequent. The "
            "Flint Hill Fire (1985, 21,746 acres) burned between Hot Springs and Edgemont "
            "in the pine-grassland transition zone. Hot Springs' Sandstone Historic District "
            "contains distinctive red sandstone buildings from the 1890s health resort era, "
            "offering more fire resistance than wooden structures but still vulnerable to "
            "radiant heat and ember intrusion. The Fall River valley through town provides "
            "a natural drainage and partial fire break but also channels wind from the "
            "southwest — the dominant fire weather wind direction."
        ),
        "key_features": [
            {"name": "Wind Cave NP", "bearing": "N/NW",
             "type": "national_park",
             "notes": "28,295 acres of mixed pine-grassland; Cold Fire (2016) was escaped prescribed burn; Legion Lake Fire reached park"},
            {"name": "Pine-grassland transition zone", "bearing": "all sides",
             "type": "fuel_transition",
             "notes": "Ecotone where grass fires meet pine forest; fuel type transition produces explosive fire behavior changes"},
            {"name": "Fall River valley", "bearing": "through town",
             "type": "river_valley",
             "notes": "Warm springs drainage; partial fire break but channels SW winds; historic district along river"},
            {"name": "Southern Hills open terrain", "bearing": "S/SE",
             "type": "grassland",
             "notes": "Rolling grass prairie south of town; Flint Hill Fire (1985) burned 21,746 acres in this zone"},
        ],
        "elevation_range_ft": (3300, 3800),
        "wui_exposure": "high — pine-grassland transition creates dual fire regime; Wind Cave NP directly adjacent; extreme fire weather events documented",
        "historical_fires": [
            {"name": "Alabaugh Fire", "year": 2007, "acres": 10324,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "lightning",
             "notes": (
                 "Started 3 miles SW of Hot Springs when temp was 109F and RH was 6%. "
                 "Burned through pine-grassland transition zone. Extreme fire weather."
             )},
            {"name": "Flint Hill Fire", "year": 1985, "acres": 21746,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "under investigation",
             "notes": "Burned between Hot Springs and Edgemont in pine-grassland transition."},
            {"name": "Cold Fire", "year": 2016, "acres": 1300,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "escaped prescribed burn",
             "notes": (
                 "Wind Cave NP prescribed burn that escaped. Grew to 6,500 acres before "
                 "containment. Demonstrated risk of prescribed fire escape in wind-prone terrain."
             )},
        ],
        "evacuation_routes": [
            {"route": "US-385 north", "direction": "N toward Custer",
             "lanes": 2, "bottleneck": "through forest along Wind Cave NP boundary",
             "risk": "Traverses pine forest and park boundary; potentially cut off by fire from Wind Cave area"},
            {"route": "US-18 east", "direction": "E toward Pine Ridge / Oglala",
             "lanes": 2, "bottleneck": "long distance to next community through open prairie",
             "risk": "Open prairie route; generally lower fire risk but exposed to grass fire"},
            {"route": "US-385 south", "direction": "S toward Edgemont",
             "lanes": 2, "bottleneck": "through pine-grassland transition zone",
             "risk": "Passes through Flint Hill Fire area; moderate fire risk from grass and scattered pine"},
        ],
        "fire_spread_characteristics": (
            "Dual fire regime at pine-grassland ecotone. Grass fires spread rapidly at 50-100+ "
            "chains/hr on windy days and produce flame lengths of 4-8 ft. When grass fire "
            "reaches pine forest margin, fire behavior transitions dramatically — torching "
            "and crown fire develop as fire enters ladder fuels. The Alabaugh Fire demonstrated "
            "extreme fire weather (109F, 6% RH) that is becoming more common. SW winds channel "
            "through Fall River valley and can drive fire directly toward town."
        ),
        "infrastructure_vulnerabilities": (
            "Small-town water system with limited wildfire capacity. Sandstone historic "
            "buildings more fire-resistant than wooden structures but still vulnerable. "
            "Volunteer fire department. No local hospital — nearest is Fall River Hospital "
            "(critical access) for basic care; Rapid City 60 miles north for trauma."
        ),
        "demographics_risk_factors": (
            "Population ~3,500. Retirement community. VA medical facility (Hot Springs VA) "
            "serves veteran population with mobility limitations. Tourism from Wind Cave NP "
            "and Mammoth Site. Low income levels. Limited community capacity for wildfire "
            "preparedness investment."
        ),
    },

    # ---- 20. Keystone, SD ----
    "keystone_sd": {
        "center": (43.893, -103.424),
        "terrain_notes": (
            "Keystone (pop ~350) is a tiny tourism town at 4,331 ft nestled in a narrow "
            "valley approximately 3 miles northeast of Mount Rushmore National Memorial in "
            "the central Black Hills. The town sits at the bottom of a steep-walled canyon "
            "along Grizzly Bear Creek, surrounded by dense ponderosa pine forest on all "
            "sides. According to wildfire risk analysis, homes and businesses in and around "
            "Keystone have a 95% greater risk from wildfire than communities in all other "
            "parts of South Dakota. This extreme risk stems from the combination of narrow "
            "canyon topography, dense fire-suppressed ponderosa pine, limited access roads, "
            "and the massive tourist population that passes through daily en route to Mt. "
            "Rushmore (2.5+ million annual visitors). The canyon terrain creates the same "
            "chimney effect seen in Deadwood, channeling and accelerating fire through the "
            "narrow valley. SD Highway 16A (Iron Mountain Road) connects Keystone to Mt. "
            "Rushmore via a series of narrow pigtail bridges and one-lane tunnels through "
            "granite — a road designed for scenic driving, not mass evacuation. The floor "
            "of the surrounding ponderosa pine forest accumulates dry dead grass and brush "
            "each spring that historically served as fuel for frequent low-intensity fires; "
            "decades of suppression has allowed this fuel to build to dangerous levels. "
            "During peak summer season, the daytime population of Keystone can swell from "
            "350 to 5,000+ as tourists fill the main street, creating an evacuation "
            "challenge that would be catastrophic if fire entered the canyon during "
            "visitation hours. Mt. Rushmore fireworks displays have been criticized by fire "
            "experts as 'ill-advised' given the surrounding dry ponderosa pine forest and "
            "high fire danger conditions."
        ),
        "key_features": [
            {"name": "Mt. Rushmore National Memorial", "bearing": "SW",
             "type": "national_memorial",
             "notes": "2.5+ million annual visitors; 3 miles from Keystone; forested approach through continuous ponderosa pine"},
            {"name": "Grizzly Bear Creek canyon", "bearing": "through town",
             "type": "narrow_canyon",
             "notes": "Town built in narrow canyon; chimney-effect fire behavior; limited width for evacuation"},
            {"name": "Iron Mountain Road (SD-16A)", "bearing": "S toward Custer SP",
             "type": "scenic_road",
             "notes": "Narrow pigtail bridges and one-lane tunnels; designed for tourism not evacuation; connects to Custer State Park"},
            {"name": "Surrounding ponderosa pine forest", "bearing": "all sides",
             "type": "dense_conifer_forest",
             "notes": "95% greater wildfire risk than rest of SD; fire-suppressed with heavy fuel loading; dry dead grass and brush each spring"},
        ],
        "elevation_range_ft": (4200, 4600),
        "wui_exposure": "extreme — 95th percentile wildfire risk in SD; narrow canyon town with 350 residents hosting 5,000+ daily tourists in peak season",
        "historical_fires": [
            {"name": "Jasper Fire (approach)", "year": 2000, "acres": 83508,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "arson",
             "notes": (
                 "While primarily burning SW of Keystone, the Jasper Fire's 83,508-acre "
                 "extent demonstrated the potential for a major Black Hills fire to reach "
                 "the Keystone corridor."
             )},
            {"name": "Legion Lake Fire (approach)", "year": 2017, "acres": 53875,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "wind-downed tree on power line",
             "notes": (
                 "Burned through Custer State Park south of Keystone. The fire's northern "
                 "extent approached terrain within 5-10 miles of Keystone."
             )},
        ],
        "evacuation_routes": [
            {"route": "SD-16A north (toward Rapid City)", "direction": "N toward US-16",
             "lanes": 2, "bottleneck": "narrow winding road through forest",
             "risk": "Primary evacuation route; forested corridor; if blocked, limited alternatives"},
            {"route": "SD-16A south (Iron Mountain Road)", "direction": "S toward Custer SP",
             "lanes": 2, "bottleneck": "pigtail bridges, one-lane tunnels, 35 mph design speed",
             "risk": "Not viable for mass evacuation; narrow tunnels and bridges create single-point failures"},
            {"route": "SD-244 west (toward Mt Rushmore)", "direction": "W",
             "lanes": 2, "bottleneck": "leads to memorial with limited through-route options",
             "risk": "Dead end at memorial; only useful to access Gutzon Borglum Historic Highway toward Hill City"},
        ],
        "fire_spread_characteristics": (
            "Canyon chimney-effect fire behavior in dense ponderosa pine. Surface fire in pine "
            "needle litter and accumulated dead grass transitions rapidly to crown fire in "
            "dense stands. Narrow canyon concentrates heat and wind. Fire can approach from "
            "Custer State Park (south), BHNF (all directions), or Jasper Fire terrain (west). "
            "Spotting distances of 0.25-0.5 miles in narrow canyon due to updraft lofting of "
            "firebrands."
        ),
        "infrastructure_vulnerabilities": (
            "Minimal infrastructure for a town of 350. No fire hydrant system adequate for "
            "wildland fire. Iron Mountain Road tunnels cannot accommodate large fire apparatus. "
            "Cell coverage limited in canyon. No medical facility — Rapid City 25 miles north. "
            "Power lines through forested canyon are ignition risk."
        ),
        "demographics_risk_factors": (
            "Permanent population only ~350 but peak daily tourist population exceeds 5,000. "
            "Mt. Rushmore draws 2.5+ million annual visitors who must transit Keystone or nearby "
            "corridors. Tourists in vehicles on narrow roads would create immediate gridlock in "
            "evacuation scenario. Motorcycle tourists (Sturgis rally) add summer exposure."
        ),
    },

    # ---- 15. Rapid City, SD ----
    "rapid_city_sd": {
        "center": (44.080, -103.231),
        "terrain_notes": (
            "Rapid City (pop ~78,000, metro ~150,000) is the gateway to the Black Hills at "
            "3,241 ft elevation on the eastern slope where the Hills meet the Great Plains. "
            "The city extends from flat prairie and grassland on the east into ponderosa "
            "pine-covered hills to the west and south. The Black Hills are a geological "
            "anomaly: an isolated mountain range — essentially a 'pine island' — rising "
            "4,000 ft above the surrounding Great Plains. Dense ponderosa pine (Pinus "
            "ponderosa) forest dominates the Hills, and decades of aggressive fire suppression "
            "since the 1940s have created dog-hair thickets with stand densities exceeding "
            "1,000 stems per acre in places — roughly 5-10x the historical density maintained "
            "by frequent low-intensity fire. Black Hills National Forest (1.2 million acres) "
            "averages 92 wildfires per year burning 7,507 acres annually, with approximately "
            "70% lightning-caused. Rapid Creek runs through the city from the Hills to the "
            "prairie, providing a partial fire break but also channeling wind. Western "
            "neighborhoods — Skyline Drive, Chapel Lane, West Rapid — extend directly into "
            "continuous ponderosa pine forest on steep terrain, creating one of the most "
            "extensive WUI zones in the Northern Great Plains. The Schroeder Fire (2021) "
            "burned 2,165 acres just west of the city in the footprint of the 1988 Westberry "
            "Trails Fire. The city falls in the 90th percentile nationally for estimated fire "
            "potential. Spring fire season (March-May) brings dry grass and gusty winds before "
            "green-up; summer fire season (June-September) brings lightning and drought; and "
            "the Black Hills have demonstrated year-round fire potential with the December 2017 "
            "Legion Lake Fire (53,875 acres) burning 30 miles south."
        ),
        "key_features": [
            {"name": "Black Hills ponderosa pine forest", "bearing": "W/SW/NW",
             "type": "dense_conifer_forest",
             "notes": "1.2M acre BHNF; decades of suppression creating 1,000+ stems/acre dog-hair thickets; 92 fires/yr average"},
            {"name": "Rapid Creek corridor", "bearing": "W-E through city",
             "type": "river_valley",
             "notes": "Runs from Hills through city to prairie; partial fire break but channels wind; 1972 flood killed 238"},
            {"name": "Skyline Drive WUI", "bearing": "W",
             "type": "wui_development",
             "notes": "Residential development directly in ponderosa forest on steep terrain; highest-risk WUI zone in city"},
            {"name": "Prairie-forest ecotone", "bearing": "E boundary",
             "type": "fuel_transition",
             "notes": "Grass-to-pine transition; grass fires can ignite pine forest; pine fires can spread to grassland"},
        ],
        "elevation_range_ft": (3000, 3800),
        "wui_exposure": "extreme — western neighborhoods extend directly into dense ponderosa pine forest; 90th percentile nationally for fire potential",
        "historical_fires": [
            {"name": "Schroeder Fire", "year": 2021, "acres": 2165,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "under investigation",
             "notes": (
                 "Burned just west of Rapid City in footprint of 1988 Westberry Trails Fire. "
                 "Mapped at 2,165 acres by aircraft on March 30. Demonstrated continued "
                 "threat to western city neighborhoods."
             )},
            {"name": "Westberry Trails Fire", "year": 1988, "acres": 1500,
             "structures_destroyed": 5, "fatalities": 0,
             "cause": "human-caused",
             "notes": "Burned into western Rapid City neighborhoods. Led to increased WUI awareness."},
        ],
        "evacuation_routes": [
            {"route": "I-90 east", "direction": "E toward Badlands / Sioux Falls",
             "lanes": 4, "bottleneck": "interstate capacity adequate",
             "risk": "Best evacuation route — heads away from Hills into open prairie; good capacity"},
            {"route": "SD-44 west", "direction": "W toward Hill City / Black Hills interior",
             "lanes": 2, "bottleneck": "narrow road through continuous ponderosa forest",
             "risk": "Leads INTO fire-prone area; not an evacuation route during Hills fire event"},
            {"route": "US-16 south", "direction": "S toward Custer / Mt Rushmore",
             "lanes": 2, "bottleneck": "winding road through dense forest",
             "risk": "Traverses highest-risk forest; potential for fire closure"},
        ],
        "fire_spread_characteristics": (
            "Ponderosa pine fires with high crown fire potential in dog-hair thicket stands. "
            "Surface spread in pine needle litter at 10-30 chains/hr under moderate conditions, "
            "accelerating to 50-150 chains/hr in wind-driven crown fire runs. The Jasper Fire "
            "(2000) burned 100 acres per minute at peak intensity. Spotting distances of 0.5-1.5 "
            "miles from crown fire runs in ponderosa pine. Grass-forest ecotone at eastern "
            "city boundary allows fire transition between fuel types. Year-round fire potential "
            "demonstrated by December 2017 Legion Lake Fire."
        ),
        "infrastructure_vulnerabilities": (
            "Black Hills Energy overhead power lines through dense forest on western city margin. "
            "Rapid City water system adequate in city but pressure drops in elevated western "
            "neighborhoods. City fuels mitigation program treated 166 acres in 2024, improved "
            "defensible space on 18 properties, protected 117 structures. Regional Hospital "
            "(Monument Health, 367 beds) is the only major hospital between Sioux Falls and "
            "Billings. Ellsworth AFB 10 miles east provides some emergency resources."
        ),
        "demographics_risk_factors": (
            "Metro population ~150,000 with tourism overlay of 4+ million annual visitors to "
            "Mt. Rushmore and Black Hills. Western neighborhoods have many older homes without "
            "fire-resistant construction in dense forest. Significant Native American population "
            "(~10%). Rapid growth pushing development into WUI zones."
        ),
    },

    # ---- 19. Spearfish, SD ----
    "spearfish_sd": {
        "center": (44.491, -103.859),
        "terrain_notes": (
            "Spearfish (pop ~12,000) sits at 3,642 ft on the northern edge of the Black "
            "Hills where dense ponderosa pine forest meets the northern Great Plains. The "
            "city is famous for extreme chinook (downslope) wind events — the world record "
            "temperature change (49F rise in 2 minutes, January 22, 1943) occurred here when "
            "a chinook descended from the Black Hills. These chinook winds have direct fire "
            "weather implications: they can desiccate fuels from snow-covered to tinder-dry "
            "in hours, producing fire conditions analogous to California's Santa Ana winds. "
            "Spearfish Canyon, a narrow limestone gorge cutting deep into the northern Black "
            "Hills to the south, channels these winds and funnels them across the city. The "
            "canyon's dense ponderosa pine forest, which was partially damaged by tornadoes "
            "that touched down in 2021 leaving significant blowdown debris, represents both "
            "a scenic asset and a significant fire fuel reservoir. Cleanup of tornado debris "
            "helped reduce fuel continuity, but the fundamental fire risk remains. The "
            "northern Black Hills are somewhat lower in elevation and slightly less densely "
            "forested than the central Hills, but the combination of chinook wind exposure, "
            "canyon channeling, and grass-forest transition terrain creates significant fire "
            "vulnerability. Community preparedness research by the US Forest Service has "
            "specifically identified Spearfish and the Northern Black Hills as high fire "
            "risk communities requiring enhanced WUI planning."
        ),
        "key_features": [
            {"name": "Spearfish Canyon", "bearing": "S/SW",
             "type": "narrow_canyon",
             "notes": "Deep limestone gorge; channels chinook winds and fire; dense pine with tornado blowdown debris"},
            {"name": "Chinook wind corridor", "bearing": "SW-NE across city",
             "type": "wind_corridor",
             "notes": "World-record chinook winds; can desiccate fuels from damp to tinder-dry in hours; Santa Ana analog"},
            {"name": "Prairie-forest transition", "bearing": "N/NE",
             "type": "fuel_transition",
             "notes": "Flat to rolling prairie north of city; grass fires can run toward town during SW chinook events"},
            {"name": "Northern Hills forest", "bearing": "S/SW/W",
             "type": "conifer_forest",
             "notes": "Ponderosa pine with some tornado-damaged areas; USFS identified as high fire risk WUI"},
        ],
        "elevation_range_ft": (3500, 4000),
        "wui_exposure": "high — chinook wind exposure creates Santa Ana-like fire weather; canyon channels wind and fire; USFS-identified high-risk WUI community",
        "historical_fires": [
            {"name": "Spearfish Canyon prescribed burns / fuel reduction", "year": "ongoing",
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "management activity",
             "notes": (
                 "200+ hand piles burned in Spearfish Canyon (2022). Active fuels management. "
                 "Tornado debris cleanup helped reduce continuity. Ongoing prescribed fire "
                 "program to reduce wildfire risk."
             )},
            {"name": "1996 Bear Butte Fire", "year": 1996, "acres": 500,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "under investigation",
             "notes": "Burned on Bear Butte, leaving scarred trees still visible on summit."},
        ],
        "evacuation_routes": [
            {"route": "I-90 east", "direction": "E toward Sturgis / Rapid City",
             "lanes": 4, "bottleneck": "good interstate capacity",
             "risk": "Best evacuation route; heads away from Hills toward open prairie"},
            {"route": "I-90 west", "direction": "W toward Wyoming",
             "lanes": 4, "bottleneck": "adequate capacity",
             "risk": "Away from fire zone; good capacity"},
            {"route": "US-14A south", "direction": "S into Spearfish Canyon / Deadwood",
             "lanes": 2, "bottleneck": "narrow canyon road; winding",
             "risk": "Leads INTO fire-prone canyon; not an evacuation route during Hills fire; connects to Deadwood"},
        ],
        "fire_spread_characteristics": (
            "Chinook wind-driven fires are the primary threat — analogous to Santa Ana wind "
            "events in California. Chinook winds can sustain 40-60 mph with gusts exceeding "
            "80 mph, rapidly desiccating fuels. Fire in Spearfish Canyon would exhibit extreme "
            "chimney-effect behavior channeled by canyon walls. Grass fires on northern prairie "
            "can run toward city at 50-100 chains/hr during chinook events. Tornado-damaged "
            "forest has broken canopy that may actually reduce crown fire continuity but "
            "increases surface fuel."
        ),
        "infrastructure_vulnerabilities": (
            "Black Hills Energy power lines through forested terrain and canyon. City water "
            "system adequate but western supply points near forest interface. Black Hills "
            "State University campus requires separate evacuation planning. Spearfish Regional "
            "Hospital (35 beds) is limited; Rapid City 45 miles east for major care."
        ),
        "demographics_risk_factors": (
            "Population ~12,000 plus university students. Tourism from Spearfish Canyon and "
            "Deadwood casinos. Sturgis rally brings additional visitors in August. Growing "
            "retirement community. Western residential development extending toward "
            "forest interface."
        ),
    },

    # ---- 22. Sturgis, SD ----
    "sturgis_sd": {
        "center": (44.410, -103.509),
        "terrain_notes": (
            "Sturgis (pop ~7,000) is located at 3,442 ft on the northeastern edge of the "
            "Black Hills where ponderosa pine forest meets the mixed-grass prairie of the "
            "northern Great Plains. The town is world-famous for the annual Sturgis "
            "Motorcycle Rally, which draws 500,000+ attendees each August — increasing the "
            "local population by roughly 70x during peak fire season. Bear Butte, a "
            "prominent volcanic laccolith rising 1,253 ft above the surrounding prairie 6 "
            "miles northeast of town, is a sacred site for the Lakota and Cheyenne nations "
            "and a South Dakota state park. The butte experienced a wildfire in 1996 that "
            "left charred trees still visible at the summit. The Sturgis Fire Department's "
            "response area includes the city, Fort Meade VA Medical Complex, Fort Meade "
            "Recreation Area, Bear Butte State Park, and the northern edge of Black Hills "
            "National Forest. During the annual rally, vast temporary campgrounds fill with "
            "hundreds of thousands of people in fire-prone terrain — the Full Throttle "
            "Saloon, billed as the world's largest biker bar, burned to the ground in "
            "September 2015 due to a faulty electrical cord on a cooler, highlighting the "
            "fire risk at primitive rally campground infrastructure. The fire risk during "
            "the rally is compounded by August's typically dry conditions, thousands of "
            "campfires at rally sites, fireworks, and the massive temporary population in "
            "areas with minimal fire suppression infrastructure. The northern Black Hills "
            "forest south and west of town presents the same ponderosa pine fire risk as "
            "the broader Hills, while grass fires from the prairie to the north and east "
            "can run toward town during strong SW wind events."
        ),
        "key_features": [
            {"name": "Bear Butte State Park", "bearing": "NE",
             "type": "volcanic_laccolith",
             "notes": "Sacred site; 1996 fire scarred summit; state park within fire department response area; 1,253 ft above plain"},
            {"name": "Rally campgrounds and venues", "bearing": "throughout area",
             "type": "temporary_infrastructure",
             "notes": "500,000+ attendees in August; primitive campgrounds; Full Throttle Saloon burned 2015; minimal fire suppression"},
            {"name": "Northern Black Hills forest edge", "bearing": "S/SW/W",
             "type": "forest_interface",
             "notes": "Ponderosa pine with fire-suppressed fuel loading; transition to prairie at town boundary"},
            {"name": "Fort Meade complex", "bearing": "E",
             "type": "military_facility",
             "notes": "VA medical complex and recreation area; within fire department response area"},
        ],
        "elevation_range_ft": (3300, 3700),
        "wui_exposure": "extreme during rally — 500,000+ people in temporary campgrounds with minimal fire infrastructure during peak fire season (August); moderate year-round",
        "historical_fires": [
            {"name": "Bear Butte Fire", "year": 1996, "acres": 500,
             "structures_destroyed": 0, "fatalities": 0,
             "cause": "under investigation",
             "notes": "Burned on Bear Butte; charred trees still visible at summit."},
            {"name": "Full Throttle Saloon Fire", "year": 2015, "acres": 0,
             "structures_destroyed": 1, "fatalities": 0,
             "cause": "faulty electrical cord on cooler",
             "notes": (
                 "World's largest biker bar burned to the ground in September 2015. "
                 "Highlighted fire risk at primitive rally campground infrastructure. "
                 "Rebuilt at new 600-acre site near Bear Butte."
             )},
        ],
        "evacuation_routes": [
            {"route": "I-90 east", "direction": "E toward Rapid City",
             "lanes": 4, "bottleneck": "interstate adequate but congested during rally",
             "risk": "Primary evacuation route; during rally, 500,000 additional people overwhelm road capacity"},
            {"route": "I-90 west", "direction": "W toward Spearfish",
             "lanes": 4, "bottleneck": "adequate capacity normally; extreme during rally",
             "risk": "Good route away from forest; congested during rally week"},
            {"route": "SD-34/79 south", "direction": "S toward Deadwood / Black Hills interior",
             "lanes": 2, "bottleneck": "narrow road into forest",
             "risk": "Leads INTO fire-prone Black Hills; not viable evacuation during forest fire"},
        ],
        "fire_spread_characteristics": (
            "Dual fire regime: grass fires from northeastern prairie can reach town at 50-100 "
            "chains/hr during strong wind events; ponderosa pine fires from the south and west "
            "present crown fire risk. During the August rally, thousands of campfires and "
            "temporary electrical hookups at primitive campgrounds create ignition risk across "
            "a huge temporary city. Grass around Bear Butte cures in late summer, increasing "
            "fire risk at the sacred site and surrounding state park."
        ),
        "infrastructure_vulnerabilities": (
            "Sturgis Fire Department response area includes town, Fort Meade, Bear Butte SP, "
            "and BHNF edge — large area for a small department. During rally, temporary "
            "infrastructure (generators, electrical hookups, cooking facilities) vastly "
            "increases ignition risk. Water system not designed for 500,000+ population. "
            "Rally campgrounds have minimal fire suppression equipment. Fort Meade VA Medical "
            "Center has limited capacity."
        ),
        "demographics_risk_factors": (
            "Permanent population ~7,000. During rally (first full week of August annually), "
            "population swells to 500,000+ — one of the largest temporary population events "
            "in the US. Rally attendees are in tents, RVs, and primitive campgrounds with "
            "no shelter-in-place capability. Many attendees consuming alcohol. Elderly "
            "veteran population at Fort Meade VA. Rural/small-town year-round demographics."
        ),
    },

    # =========================================================================
    # MISSOURI (OZARKS) (2 cities)
    # =========================================================================

    # =========================================================================
    # MISSOURI (OZARKS)
    # =========================================================================
    "branson_mo": {
        "center": (36.644, -93.218),
        "terrain_notes": (
            "Ozark Mountain resort city at 800-1400 ft in Taney County, Missouri, situated "
            "in deeply dissected limestone/dolomite terrain along Lake Taneycomo and Table Rock "
            "Lake. The Ozark Plateau here is cut by steep hollows, narrow ridgetops, and karst "
            "terrain with sinkholes. Eastern red cedar (Juniperus virginiana) has invaded former "
            "oak-hickory forest and open glades at alarming rates — cedar density has increased "
            "300-500% since fire suppression began in the 1930s. Cedar is extremely flammable "
            "with volatile oils that produce 30-50 ft flame lengths and prolific spot fire "
            "ember production. The cedar glade fire regime is adapted to frequent low-intensity "
            "burns (3-7 year return), but 80+ years of suppression have created dense cedar "
            "thickets with continuous canopy. Branson's terrain channels wind through hollows "
            "and valleys, creating erratic fire behavior. The city straddles multiple ridgetops "
            "connected by winding mountain roads. Table Rock Lake and Lake Taneycomo provide "
            "some natural firebreaks but steep bluffs above the lakes are heavily forested. "
            "Major wildfire events have included the 2011 drought fires that burned across SW "
            "Missouri and NW Arkansas, and recurring cedar fires in Mark Twain National Forest. "
            "Tourism infrastructure (theaters, hotels, attractions) lines narrow SR-76 corridor "
            "('The Strip') with limited alternative routes. Seasonal population can exceed "
            "100,000 visitors per day during peak season in a city of 12,000 permanent residents."
        ),
        "key_features": [
            {"name": "Table Rock Lake", "bearing": "SW/W", "distance_mi": 3,
             "type": "lake_firebreak",
             "notes": "Large reservoir provides some firebreak but bluffs above are heavily forested cedar/oak"},
            {"name": "Mark Twain National Forest", "bearing": "S/SE", "distance_mi": 10,
             "type": "forest_wui",
             "notes": "1.5 million acre NF, cedar invasion creating extreme fire loads in Ozark glades"},
            {"name": "Roark Creek Valley", "bearing": "through city", "type": "fire_corridor",
             "notes": "Deep valley through central Branson channels wind and fire, limited crossing points"},
            {"name": "SR-76 Strip corridor", "bearing": "E-W", "type": "evacuation_bottleneck",
             "notes": "Primary tourist corridor, 4 lanes but gridlocked during events and emergencies"},
        ],
        "elevation_range_ft": (700, 1400),
        "wui_exposure": "high — cedar-invaded hillsides directly adjoin resort hotels, theaters, and residential areas on ridgetops",
        "historical_fires": [
            {
                "name": "2011 SW Missouri drought fires",
                "year": 2011,
                "acres": 5000,
                "structures_destroyed": 12,
                "fatalities": 0,
                "cause": "multiple — arson, debris burning",
                "notes": (
                    "Exceptional drought (D4) across SW Missouri/NW Arkansas. Multiple fires "
                    "burned across Taney, Stone, and Barry counties. Cedar thickets produced "
                    "extreme fire behavior with rapid spread through continuous canopy."
                ),
            },
        ],
        "evacuation_routes": [
            {"route": "US-65", "direction": "north to Springfield", "lanes": 4,
             "bottleneck": "Branson Hills interchange congestion",
             "risk": "Primary route, heavy traffic during tourist season"},
            {"route": "SR-76 (The Strip)", "direction": "east/west", "lanes": 4,
             "bottleneck": "Gridlock common during peak hours",
             "risk": "Only east-west corridor through central Branson"},
            {"route": "SR-265 (Shepherd of the Hills Expy)", "direction": "north", "lanes": 4,
             "bottleneck": "Limited connections to US-65",
             "risk": "Newer bypass but still funnels to US-65"},
            {"route": "SR-13", "direction": "south to Arkansas", "lanes": 2,
             "bottleneck": "Narrow mountain road, sharp curves",
             "risk": "Only southern escape, winding through forested hollows"},
        ],
        "fire_spread_characteristics": (
            "Cedar-dominated fire spreads rapidly through continuous canopy with prolific spotting "
            "from volatile cedar oil. Hollow terrain channels wind creating erratic runs. Ridge-to-ridge "
            "fire spread accelerated by upslope heating on south-facing aspects. Limestone karst "
            "terrain creates uneven fuel moisture patterns. Night recovery limited on south/west "
            "aspects during drought."
        ),
        "infrastructure_vulnerabilities": (
            "SR-76 tourist strip with dense commercial buildings. Branson entertainment district "
            "on ridgetop with limited water supply for fire suppression. Many older wooden structures "
            "in original downtown. Resort/hotel concentration means thousands of visitors unfamiliar "
            "with evacuation routes. Cell service congestion during events. Branson airport is small "
            "with limited capacity for emergency operations."
        ),
        "demographics_risk_factors": (
            "Permanent population ~12,000 but daily tourist population can reach 50,000-100,000+. "
            "Significant elderly visitor demographic (retirement tourism). Many visitors in hotels "
            "and rental cabins unfamiliar with area geography. Seasonal workforce housing in "
            "vulnerable areas. Large number of cabin/vacation rental properties in wooded hollows "
            "with single-access roads."
        ),
    },

    "table_rock_lake_mo": {
        "center": (36.580, -93.350),
        "terrain_notes": (
            "Table Rock Lake communities (Hollister, Kimberling City, Shell Knob, Indian Point) "
            "in Stone and Barry counties sit on heavily forested ridgetops and steep bluffs above "
            "the 43,100-acre reservoir. Terrain is deeply dissected Ozark Plateau with limestone "
            "bluffs rising 200-400 ft above lake level. Eastern red cedar invasion has transformed "
            "formerly open oak-hickory-cedar glades into dense cedar thickets with continuous "
            "canopy. The lake itself provides firebreaks along its 745 miles of shoreline, but "
            "the steep timbered bluffs above create extreme fire behavior with rapid upslope "
            "runs. Hundreds of lakefront cabins, resorts, and marinas sit on narrow peninsula "
            "ridges with water access on 2-3 sides but only single-road land access. The "
            "Hollister area south of Branson is particularly vulnerable as it occupies a narrow "
            "ridge between Turkey Creek and Lake Taneycomo. Shell Knob on the southwestern arm "
            "is a retirement community on a peninsula accessible via a single 2-lane road. "
            "Indian Point near Silver Dollar City is another narrow peninsula with thousands of "
            "resort units. Mark Twain National Forest borders the lake on the south and east, "
            "providing continuous wildland fuels. The 2012 drought saw multiple grass/cedar fires "
            "across Stone County that threatened lakefront communities."
        ),
        "key_features": [
            {"name": "Table Rock Lake", "bearing": "surrounding", "type": "lake_partial_firebreak",
             "notes": "43,100-acre reservoir with 745 mi shoreline, provides firebreaks but bluffs above are fuel-loaded"},
            {"name": "Indian Point Peninsula", "bearing": "W", "distance_mi": 5,
             "type": "evacuation_trap",
             "notes": "Narrow peninsula with Silver Dollar City and hundreds of cabins, single road in/out"},
            {"name": "Shell Knob Peninsula", "bearing": "SW", "distance_mi": 15,
             "type": "retirement_wui",
             "notes": "Retirement community on peninsula with single 2-lane access road"},
            {"name": "Mark Twain National Forest", "bearing": "S/SE", "type": "forest_wui",
             "notes": "Continuous wildland fuels from NF border to lakefront communities"},
        ],
        "elevation_range_ft": (700, 1200),
        "wui_exposure": "high — lakefront cabins and resorts on forested ridgetops and peninsulas with limited access",
        "historical_fires": [
            {
                "name": "2012 Stone County drought fires",
                "year": 2012,
                "acres": 2000,
                "structures_destroyed": 5,
                "fatalities": 0,
                "cause": "multiple ignitions during drought",
                "notes": "Multiple grass/cedar fires across Stone County during exceptional drought, threatened lakefront communities",
            },
        ],
        "evacuation_routes": [
            {"route": "US-65", "direction": "north to Branson/Springfield", "lanes": 4,
             "bottleneck": "Branson interchange congestion",
             "risk": "Primary route, shared with Branson tourist traffic"},
            {"route": "SR-13", "direction": "south through Kimberling City", "lanes": 2,
             "bottleneck": "Narrow mountain road, single bridge over James River arm",
             "risk": "Only route for SW lake communities"},
            {"route": "SR-39", "direction": "east to Shell Knob", "lanes": 2,
             "bottleneck": "Single 2-lane road to peninsula communities",
             "risk": "Only access for Shell Knob, no alternative if blocked"},
        ],
        "fire_spread_characteristics": (
            "Cedar-oak fire on steep bluffs above lake produces rapid upslope runs with extreme "
            "flame lengths. Spotting across narrow lake arms is possible during high wind events. "
            "Peninsula terrain traps fire on 3 sides with lake evacuation as last resort. Night "
            "recovery limited on south-facing bluffs."
        ),
        "infrastructure_vulnerabilities": (
            "Hundreds of lakefront cabins with wood construction and propane tanks. Many marinas "
            "with fuel storage. Rural water districts with limited fire suppression capacity. "
            "Cell service gaps in hollows. Single-road access to peninsulas easily blocked. "
            "Volunteer fire departments cover large, steep terrain areas."
        ),
        "demographics_risk_factors": (
            "Mix of retirement communities (Shell Knob median age ~65), seasonal vacation rentals, "
            "and weekend tourists. Many elderly residents with limited mobility. Seasonal population "
            "triples in summer. Vacation renters unfamiliar with area. Many properties are seasonal-use "
            "with no permanent occupant to maintain defensible space."
        ),
    },

    # =========================================================================
    # MINNESOTA (1 cities)
    # =========================================================================

    # =========================================================================
    # MINNESOTA
    # =========================================================================
    "duluth_mn": {
        "center": (46.787, -92.100),
        "terrain_notes": (
            "Lake Superior port city climbing from harbor level (602 ft) up a steep escarpment "
            "to hilltop neighborhoods at 1400+ ft — a 800-ft climb in under 2 miles. The city "
            "occupies a narrow strip between Lake Superior and the boreal forest of the Superior "
            "National Forest / BWCAW (Boundary Waters Canoe Area Wilderness) to the north. "
            "Terrain is steep basalt/gabbro bedrock from ancient volcanic activity (North Shore "
            "Volcanic Group), creating a dramatic escarpment that channels wind and fire. The "
            "boreal forest (jack pine, spruce, birch, aspen) to the north and west is adapted "
            "to stand-replacing crown fires on a 50-200 year return interval. The 1918 Cloquet "
            "Fire killed 453 people and burned 250,000 acres just 20 miles west, driven by "
            "drought and extreme winds through slash-filled cutover land. The Pagami Creek Fire "
            "(2011, 93,000 acres) in the BWCAW demonstrated that large fires still occur in "
            "this forest type. Climate change is extending fire seasons and increasing drought "
            "frequency in the boreal zone. The Greenwood Fire (2021, 26,000 acres) forced "
            "evacuations along the North Shore. Duluth's western neighborhoods (Hermantown, "
            "Proctor, Spirit Mountain area) are expanding into jack pine and aspen forest WUI. "
            "Steep terrain above the harbor creates extreme downslope wind events during "
            "northwest wind patterns. Chester Creek, Tischer Creek, and Lester River corridors "
            "create fire pathways from hilltop forest down to lake-level neighborhoods."
        ),
        "key_features": [
            {"name": "Superior National Forest", "bearing": "N/NW", "distance_mi": 10,
             "type": "boreal_forest_wui",
             "notes": "3.9 million acre NF with fire-adapted boreal species, crown fire regime"},
            {"name": "Lake Superior escarpment", "bearing": "through city", "type": "terrain_amplifier",
             "notes": "800-ft basalt escarpment channels wind and creates extreme slope-driven fire behavior"},
            {"name": "Spirit Mountain area", "bearing": "SW", "distance_mi": 5,
             "type": "forest_wui",
             "notes": "Western suburbs expanding into jack pine forest, high WUI exposure"},
            {"name": "Creek corridors", "bearing": "multiple", "type": "fire_pathway",
             "notes": "Chester, Tischer, Lester creek valleys carry fire from hilltop forest to harbor neighborhoods"},
            {"name": "BWCAW", "bearing": "N", "distance_mi": 50,
             "type": "wilderness_fire",
             "notes": "1.1 million acre wilderness, natural fire regime, Pagami Creek Fire 2011 (93,000 ac)"},
        ],
        "elevation_range_ft": (602, 1500),
        "wui_exposure": "high — western and hilltop neighborhoods expand directly into boreal forest with crown fire potential",
        "historical_fires": [
            {
                "name": "Cloquet Fire",
                "year": 1918,
                "acres": 250000,
                "structures_destroyed": 4000,
                "fatalities": 453,
                "cause": "railroad sparks in slash-filled cutover land + drought + extreme winds",
                "notes": (
                    "One of the worst natural disasters in Minnesota history. Killed 453 people, "
                    "destroyed Cloquet and Moose Lake. Fire burned through 20 miles of slash "
                    "to threaten Duluth's western outskirts. Driven by extreme winds and "
                    "months of drought. Led to creation of Minnesota's fire management system."
                ),
            },
            {
                "name": "Pagami Creek Fire",
                "year": 2011,
                "acres": 93000,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "lightning",
                "notes": "Large wilderness fire in BWCAW demonstrated continued crown fire potential in boreal forest",
            },
            {
                "name": "Greenwood Fire",
                "year": 2021,
                "acres": 26000,
                "structures_destroyed": 14,
                "fatalities": 0,
                "cause": "lightning",
                "notes": "Forced evacuations along North Shore (MN-61), closed BWCAW entry points, demonstrated growing WUI risk",
            },
        ],
        "evacuation_routes": [
            {"route": "I-35", "direction": "south/southwest to Twin Cities", "lanes": 4,
             "bottleneck": "Thompson Hill interchange, steep grade",
             "risk": "Primary route, vulnerable to smoke from western fires"},
            {"route": "MN-61 (North Shore)", "direction": "northeast", "lanes": 2,
             "bottleneck": "Narrow coastal road between lake and escarpment",
             "risk": "Single route along North Shore, Greenwood Fire forced closure in 2021"},
            {"route": "US-2", "direction": "west to Proctor/Hermantown", "lanes": 2,
             "bottleneck": "Through western WUI zone",
             "risk": "Passes through highest fire risk neighborhoods"},
            {"route": "I-535 (Blatnik Bridge)", "direction": "east to Superior WI", "lanes": 4,
             "bottleneck": "Single bridge crossing to Wisconsin",
             "risk": "Bridge closure would eliminate eastern evacuation option"},
        ],
        "fire_spread_characteristics": (
            "Boreal crown fire regime — jack pine and spruce support stand-replacing fires "
            "that spread at 50-100 chains/hr during blow-up conditions. Steep escarpment "
            "terrain amplifies fire runs from hilltop to harbor level. Creek corridors act "
            "as chimney-effect fire pathways. Wind channeling along Lake Superior shore "
            "creates unpredictable shifts. Extended daylight in summer (16+ hours) prolongs "
            "burning period. Climate change extending fire season into October."
        ),
        "infrastructure_vulnerabilities": (
            "Aging wooden housing stock in hilltop and West Duluth neighborhoods. Many homes "
            "built before wildfire codes existed. Steep terrain makes fire suppression difficult "
            "— apparatus access limited on many hillside streets. Municipal water pressure drops "
            "at higher elevations. Power lines through forested corridors vulnerable to fire damage. "
            "Natural gas infrastructure on steep terrain. Duluth has limited mutual aid resources "
            "given its geographic isolation."
        ),
        "demographics_risk_factors": (
            "Population ~90,000 (metro ~130,000). University of Minnesota Duluth campus (11,000 "
            "students) in hilltop forest area. Significant elderly population in steep hillside "
            "neighborhoods with limited mobility. Tourism and seasonal population (Canal Park, "
            "North Shore). Lower-income neighborhoods in most fire-vulnerable western areas. "
            "Geographic isolation — nearest major city (Minneapolis) is 150 miles south."
        ),
    },

}




# =============================================================================
# Ignition Sources — Southeast, Black Hills, Midwest, Hawaii
# =============================================================================

SE_MISC_IGNITION_SOURCES = {
    # =========================================================================
    # HAWAII
    # =========================================================================
    "lahaina_hi": {
        "lat": 20.88,
        "lon": -156.68,
        "radius_km": 30,
        "primary": [
            {
                "source": "Power lines (Hawaiian Electric / HECO)",
                "risk": "EXTREME",
                "detail": (
                    "Hawaiian Electric downed power lines caused the 2023 Lahaina "
                    "fire. Broken overhead line on Lahainaluna Road was re-energized "
                    "at 6:34 AM, sparking fire in unmaintained invasive grass. HECO "
                    "acknowledged its lines caused the morning blaze. Infrastructure "
                    "is aging and exposed to hurricane-force winds. Utility did not "
                    "implement Public Safety Power Shutoffs (PSPS) despite extreme "
                    "wind conditions."
                ),
            },
            {
                "source": "Invasive grass fuel bed",
                "risk": "EXTREME",
                "detail": (
                    "Guinea grass (grows 6 inches/day) and buffelgrass from Africa "
                    "cover former sugar/pineapple plantation slopes above town. "
                    "These grasses dry out in summer drought and create continuous "
                    "flashy fuel from hillside to town edge. Post-plantation "
                    "abandonment (1990s) left thousands of acres unmanaged."
                ),
            },
            {
                "source": "Arson / human negligence",
                "risk": "MODERATE",
                "detail": (
                    "Some Maui fires historically human-caused through campfires, "
                    "vehicles, or equipment. Dry conditions make any spark dangerous."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Lahainaluna Road hillside",
                "direction": "E-W (upslope)",
                "risk": (
                    "Fire origin corridor — power lines along road above town. "
                    "Invasive grass on both sides of road."
                ),
            },
            {
                "name": "Honoapiilani Highway (HI-30)",
                "direction": "N-S along coast",
                "risk": (
                    "Primary evacuation route. Became impassable during 2023 fire. "
                    "Many victims trapped on highway."
                ),
            },
        ],
    },
    "kula_hi": {
        "lat": 20.79,
        "lon": -156.33,
        "radius_km": 25,
        "primary": [
            {
                "source": "Power lines (Maui Electric / MECO)",
                "risk": "HIGH",
                "detail": (
                    "Rural overhead lines through gulch terrain. Vulnerable to "
                    "high wind events. Limited vegetation management around lines."
                ),
            },
            {
                "source": "Invasive species fuel load",
                "risk": "HIGH",
                "detail": (
                    "Invasive eucalyptus, guava, and African grasses have colonized "
                    "former agricultural land. Eucalyptus bark is highly flammable "
                    "and creates spot fire risk."
                ),
            },
            {
                "source": "Agricultural equipment / operations",
                "risk": "MODERATE",
                "detail": (
                    "Upcountry ranching and farming operations. Equipment sparks, "
                    "controlled burns for pasture management."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Kula Highway (HI-37)",
                "direction": "N-S along Haleakala slope",
                "risk": "Primary access road, evacuation route, power line corridor.",
            },
        ],
    },

    # =========================================================================
    # SOUTHEAST — Appalachian / Smokies
    # =========================================================================
    "gatlinburg_tn": {
        "lat": 35.71,
        "lon": -83.51,
        "radius_km": 40,
        "primary": [
            {
                "source": "Arson / juvenile fire-setting",
                "risk": "HIGH",
                "detail": (
                    "2016 Chimney Tops 2 Fire was arson — two juveniles dropped "
                    "lit matches on Chimney Tops Trail despite burn ban. Arson is "
                    "a significant ignition source across the southern Appalachians. "
                    "Heavy tourist traffic brings millions of visitors into fire-prone "
                    "areas annually."
                ),
            },
            {
                "source": "Power lines (high winds)",
                "risk": "HIGH",
                "detail": (
                    "87 mph wind gusts during 2016 fire knocked down power lines "
                    "throughout Gatlinburg, creating new ignition points ahead of "
                    "the main fire front. Mountain terrain amplifies wind speeds."
                ),
            },
            {
                "source": "Campfires / tourist activity",
                "risk": "MODERATE",
                "detail": (
                    "Great Smoky Mountains NP receives 12+ million visitors/year. "
                    "Campfires, cigarettes, and outdoor cooking are persistent "
                    "ignition sources."
                ),
            },
            {
                "source": "Prescribed burn escapes",
                "risk": "LOW",
                "detail": (
                    "NPS and USFS conduct prescribed burns in the Smokies. "
                    "Escapes are rare but possible in the Appalachian terrain."
                ),
            },
        ],
        "corridors": [
            {
                "name": "US-441 (Newfound Gap Road)",
                "direction": "NW-SE through Smokies",
                "risk": (
                    "Major tourist route through national park. Primary "
                    "evacuation corridor — bottleneck during 2016 disaster."
                ),
            },
            {
                "name": "Chimney Tops Trail corridor",
                "direction": "S from Sugarlands",
                "risk": "Fire origin area. Steep terrain channels fire downhill.",
            },
        ],
    },
    "asheville_nc": {
        "lat": 35.60,
        "lon": -82.55,
        "radius_km": 50,
        "primary": [
            {
                "source": "Arson / debris burning",
                "risk": "HIGH",
                "detail": (
                    "Human-caused fires are the leading ignition source in western "
                    "NC. 'We're our own worst enemy' — NC Forest Service official. "
                    "Illegal debris burning, especially during burn bans."
                ),
            },
            {
                "source": "Power lines (mountain terrain)",
                "risk": "HIGH",
                "detail": (
                    "Mountain terrain exposes overhead lines to high winds and "
                    "falling trees. Hurricane Helene (2024) damaged extensive "
                    "infrastructure."
                ),
            },
            {
                "source": "Lightning (summer convection)",
                "risk": "MODERATE",
                "detail": (
                    "Afternoon thunderstorms in mountain terrain produce lightning "
                    "that can start fires in remote, inaccessible areas."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Blue Ridge Parkway",
                "direction": "NE-SW along ridgeline",
                "risk": (
                    "Tourist traffic on mountain road. Cigarettes, campfires. "
                    "Fire along parkway hard to access for suppression."
                ),
            },
            {
                "name": "I-40 through Pigeon River Gorge",
                "direction": "E-W",
                "risk": "Vehicle-related ignition in narrow mountain gorge.",
            },
        ],
    },
    "bryson_city_nc": {
        "lat": 35.43,
        "lon": -83.45,
        "radius_km": 40,
        "primary": [
            {
                "source": "Human-caused fires (arson, debris burning)",
                "risk": "HIGH",
                "detail": (
                    "Leading cause of wildfires in western NC. Rural areas with "
                    "limited fire enforcement."
                ),
            },
            {
                "source": "Lightning",
                "risk": "MODERATE",
                "detail": (
                    "Haoe Lead Fire (3,100+ acres) in Joyce Kilmer-Slickrock "
                    "Wilderness was lightning-caused. Remote terrain makes "
                    "lightning fires difficult to detect and suppress."
                ),
            },
        ],
        "corridors": [
            {
                "name": "US-19/74 corridor",
                "direction": "E-W through mountains",
                "risk": "Primary route, vehicle ignition source.",
            },
        ],
    },
    "athens_ga": {
        "lat": 33.96,
        "lon": -83.38,
        "radius_km": 60,
        "primary": [
            {
                "source": "Arson / debris burning",
                "risk": "HIGH",
                "detail": (
                    "Human-caused fires dominate NE Georgia ignitions. 2016 drought "
                    "amplified escaped debris burns into major fires."
                ),
            },
            {
                "source": "Lightning",
                "risk": "MODERATE",
                "detail": (
                    "Rough Ridge Fire in Cohutta Wilderness (28,000 acres) was "
                    "lightning-caused (started Oct 16, 2016)."
                ),
            },
            {
                "source": "Power lines (rural)",
                "risk": "MODERATE",
                "detail": (
                    "Rural power infrastructure in hilly, forested terrain. "
                    "Falling trees during wind events damage lines."
                ),
            },
        ],
        "corridors": [],
    },

    # =========================================================================
    # SOUTHEAST — Florida / Gulf
    # =========================================================================
    "panama_city_fl": {
        "lat": 30.16,
        "lon": -85.66,
        "radius_km": 50,
        "primary": [
            {
                "source": "Prescribed burns (escaped)",
                "risk": "HIGH",
                "detail": (
                    "Florida is the #1 prescribed burn state (~2.3 million "
                    "acres/year). Escaped prescribed burns are a leading wildfire "
                    "cause. Pine flatwoods require fire every 18 months to 4 years "
                    "— prescribed fire is essential but carries escape risk."
                ),
            },
            {
                "source": "Lightning",
                "risk": "HIGH",
                "detail": (
                    "Florida is the lightning capital of the US. Summer convection "
                    "produces frequent lightning in pine flatwoods."
                ),
            },
            {
                "source": "Power lines (hurricane damage)",
                "risk": "HIGH",
                "detail": (
                    "Hurricane Michael (2018) devastated power infrastructure. "
                    "Rebuilding ongoing. Wind-damaged poles and lines are "
                    "vulnerable to subsequent storms."
                ),
            },
            {
                "source": "Arson / debris burning",
                "risk": "MODERATE",
                "detail": (
                    "Illegal burning, especially during drought. Campfires in "
                    "state and national forest lands."
                ),
            },
        ],
        "corridors": [
            {
                "name": "US-231 / US-98",
                "direction": "N-S / E-W",
                "risk": "Vehicle-related ignition through pine flatwoods.",
            },
        ],
    },

    # =========================================================================
    # SOUTHEAST — Central Texas
    # =========================================================================
    "bastrop_tx": {
        "lat": 30.11,
        "lon": -97.31,
        "radius_km": 40,
        "primary": [
            {
                "source": "Power lines (wind events)",
                "risk": "EXTREME",
                "detail": (
                    "2011 Bastrop Complex Fire ignited when tropical storm-force "
                    "winds snapped trees onto power lines, starting 3 separate "
                    "fires in the WUI. Power line infrastructure through heavy "
                    "pine forest is the #1 ignition risk."
                ),
            },
            {
                "source": "Prescribed burns (escaped)",
                "risk": "HIGH",
                "detail": (
                    "2015 Hidden Pines Fire (4,600 acres, 64 structures) likely "
                    "caused by escaped prescribed burn. Prescribed fire is "
                    "essential for Lost Pines ecosystem health but carries risk "
                    "in the WUI."
                ),
            },
            {
                "source": "Vehicle / equipment sparks",
                "risk": "MODERATE",
                "detail": (
                    "TX-21 and TX-71 corridors through pine forest. Mowing, "
                    "chainsaws, and vehicle-related sparks in dry conditions."
                ),
            },
        ],
        "corridors": [
            {
                "name": "TX-21",
                "direction": "NW-SE through Lost Pines",
                "risk": "Bisects pine forest. Vehicle and equipment ignition source.",
            },
            {
                "name": "TX-71",
                "direction": "E-W",
                "risk": "Major highway through WUI. Austin commuter traffic.",
            },
        ],
    },

    # =========================================================================
    # BLACK HILLS — South Dakota
    # =========================================================================
    "rapid_city_sd": {
        "lat": 44.08,
        "lon": -103.23,
        "radius_km": 60,
        "primary": [
            {
                "source": "Lightning",
                "risk": "HIGH",
                "detail": (
                    "~70% of Black Hills fires are lightning-caused. Summer "
                    "thunderstorms produce dry lightning over the Hills. Average "
                    "92 wildfires/year in Black Hills NF."
                ),
            },
            {
                "source": "Recreational / campfires",
                "risk": "HIGH",
                "detail": (
                    "Black Hills is a major recreation destination — Mt. Rushmore, "
                    "Crazy Horse, Custer State Park. Campfires, fireworks (July 4 "
                    "at Mt. Rushmore), and careless recreation are significant "
                    "ignition sources."
                ),
            },
            {
                "source": "Power lines",
                "risk": "MODERATE",
                "detail": (
                    "Rural power infrastructure through dense pine forest. "
                    "Wind events cause tree-on-line contact."
                ),
            },
            {
                "source": "Arson",
                "risk": "MODERATE",
                "detail": (
                    "Jasper Fire (2000, 83,508 acres) was arson-caused. Arsonist "
                    "sentenced to 25 years in prison."
                ),
            },
        ],
        "corridors": [
            {
                "name": "I-90",
                "direction": "E-W along north edge of Hills",
                "risk": "Major interstate, vehicle-related ignition.",
            },
            {
                "name": "US-16 / Mt. Rushmore Road",
                "direction": "SW from Rapid City into Hills",
                "risk": "Heavy tourist traffic through ponderosa pine forest.",
            },
        ],
    },
    "custer_sd": {
        "lat": 43.77,
        "lon": -103.60,
        "radius_km": 40,
        "primary": [
            {
                "source": "Arson",
                "risk": "HIGH",
                "detail": (
                    "Jasper Fire (2000) was arson — the largest fire in SD history "
                    "(83,508 acres). Came within 6 miles of Custer."
                ),
            },
            {
                "source": "Lightning",
                "risk": "HIGH",
                "detail": (
                    "Dominant natural ignition source in Black Hills. Legion Lake "
                    "Fire (2017) started in December — demonstrating year-round "
                    "lightning risk."
                ),
            },
            {
                "source": "Recreational / campfires",
                "risk": "MODERATE",
                "detail": (
                    "Custer State Park and surrounding public lands are heavily "
                    "recreated. Campground fires, equipment sparks."
                ),
            },
        ],
        "corridors": [
            {
                "name": "US-16A (Iron Mountain Road)",
                "direction": "NE toward Mt. Rushmore",
                "risk": "Tourist corridor through dense pine.",
            },
            {
                "name": "SD-87 (Needles Highway)",
                "direction": "N into Custer State Park",
                "risk": "Narrow mountain road, tourist traffic in pine forest.",
            },
        ],
    },
    "deadwood_sd": {
        "lat": 44.38,
        "lon": -103.73,
        "radius_km": 30,
        "primary": [
            {
                "source": "Human-caused (recreation, tourists)",
                "risk": "HIGH",
                "detail": (
                    "Historic tourist town with casinos and outdoor recreation. "
                    "Campfires, cigarettes, fireworks in narrow gulch terrain "
                    "with dense pine forest on canyon walls."
                ),
            },
            {
                "source": "Power lines (canyon terrain)",
                "risk": "HIGH",
                "detail": (
                    "Overhead lines through narrow canyon. Wind events cause "
                    "tree-on-line contact on steep slopes."
                ),
            },
            {
                "source": "Lightning",
                "risk": "MODERATE",
                "detail": "Summer storms over northern Black Hills.",
            },
        ],
        "corridors": [
            {
                "name": "US-85",
                "direction": "N-S through Deadwood",
                "risk": "Primary access road. Vehicle ignition in canyon.",
            },
            {
                "name": "US-14A (Spearfish Canyon Road)",
                "direction": "NW to Spearfish",
                "risk": (
                    "Scenic route through narrow limestone canyon with dense "
                    "pine forest."
                ),
            },
        ],
    },
    "hot_springs_sd": {
        "lat": 43.43,
        "lon": -103.47,
        "radius_km": 40,
        "primary": [
            {
                "source": "Lightning",
                "risk": "HIGH",
                "detail": (
                    "Alabaugh Fire (2007, 10,324 acres) was lightning-caused "
                    "3 miles SW of Hot Springs on a 109F / 6% RH day."
                ),
            },
            {
                "source": "Human-caused (campfires, vehicles)",
                "risk": "MODERATE",
                "detail": "Wind Cave NP and surrounding recreation areas.",
            },
        ],
        "corridors": [
            {
                "name": "US-18 / US-385",
                "direction": "E-W / N-S",
                "risk": "Routes through pine-grassland transition.",
            },
        ],
    },
    "spearfish_sd": {
        "lat": 44.49,
        "lon": -103.86,
        "radius_km": 30,
        "primary": [
            {
                "source": "Lightning",
                "risk": "HIGH",
                "detail": "Summer storms over northern Black Hills. Dry lightning events.",
            },
            {
                "source": "Human-caused (recreation)",
                "risk": "MODERATE",
                "detail": (
                    "Spearfish Canyon is a popular recreation destination. "
                    "Campfires, hiking, rock climbing activities."
                ),
            },
            {
                "source": "Chinook wind-driven ember transport",
                "risk": "HIGH",
                "detail": (
                    "Extreme chinook (downslope) winds can carry embers miles. "
                    "Spearfish holds the world record for temperature change "
                    "(49F in 2 min) from chinook winds. These events create "
                    "RH drops and wind speeds comparable to Santa Ana conditions."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Spearfish Canyon (US-14A)",
                "direction": "SW-NE",
                "risk": (
                    "Narrow canyon channels chinook winds. Dense pine fuel on "
                    "canyon walls. Tourist traffic."
                ),
            },
            {
                "name": "I-90",
                "direction": "E-W",
                "risk": "Interstate on northern edge of Black Hills.",
            },
        ],
    },

    # =========================================================================
    # MIDWEST — Missouri Ozarks
    # =========================================================================
    "branson_mo": {
        "lat": 36.64,
        "lon": -93.22,
        "radius_km": 40,
        "primary": [
            {
                "source": "Arson / debris burning",
                "risk": "HIGH",
                "detail": (
                    "Human-caused fires dominate the Missouri Ozarks. Illegal "
                    "burning, debris disposal, and arson are the leading ignition "
                    "sources in rural SW Missouri."
                ),
            },
            {
                "source": "Power lines (ice storms)",
                "risk": "MODERATE",
                "detail": (
                    "Ice storms damage power infrastructure in the Ozarks. "
                    "Subsequent dry conditions + downed lines = ignition risk."
                ),
            },
            {
                "source": "Lightning (summer convection)",
                "risk": "MODERATE",
                "detail": (
                    "Summer and fall thunderstorms produce lightning in cedar-oak "
                    "forest. Dry lightning possible during drought years."
                ),
            },
        ],
        "corridors": [
            {
                "name": "US-65 / US-76 ('The Strip')",
                "direction": "N-S / E-W",
                "risk": "Major tourist traffic through hilly cedar-oak terrain.",
            },
        ],
    },

    # =========================================================================
    # MIDWEST — Minnesota Boreal
    # =========================================================================
    "duluth_mn": {
        "lat": 46.79,
        "lon": -92.10,
        "radius_km": 60,
        "primary": [
            {
                "source": "Lightning (boreal convection)",
                "risk": "HIGH",
                "detail": (
                    "Summer thunderstorms ignite fires in boreal forest. Dry "
                    "lightning events during drought can spark multiple fires "
                    "simultaneously in remote areas. Pagami Creek Fire (2011, "
                    "93,000 acres) was lightning-caused."
                ),
            },
            {
                "source": "Human-caused (campfires, recreation)",
                "risk": "HIGH",
                "detail": (
                    "BWCA Wilderness and Superior NF are heavily recreated. "
                    "Campfire escapes, especially during drought conditions. "
                    "Limited enforcement in remote wilderness."
                ),
            },
            {
                "source": "Power lines (wind/ice events)",
                "risk": "MODERATE",
                "detail": (
                    "Rural power infrastructure through boreal forest. Severe "
                    "wind events (derechos) and ice storms damage lines."
                ),
            },
            {
                "source": "Railroad (BNSF/CN)",
                "risk": "MODERATE",
                "detail": (
                    "Major railroad hub. BNSF and CN lines through forested "
                    "corridors north and west of Duluth."
                ),
            },
        ],
        "corridors": [
            {
                "name": "I-35",
                "direction": "N-S through city",
                "risk": "Major corridor, vehicle ignition in forested terrain.",
            },
            {
                "name": "US-53 north corridor",
                "direction": "N toward Iron Range",
                "risk": "Route through boreal forest to Iron Range communities.",
            },
        ],
    },
}


# =============================================================================
# Fire Climatology — Southeast, Black Hills, Midwest, Hawaii
# =============================================================================

SE_MISC_CLIMATOLOGY = {
    # =========================================================================
    # SOUTHEAST — Appalachian / Smokies
    # =========================================================================
    "southeast_appalachian_fall": {
        "months": [10, 11, 12],
        "regions": ["TN_smokies", "NC_western", "GA_northeast", "VA_sw"],
        "lat_range": (33.5, 37.0),
        "lon_range": (-85.0, -80.0),
        "fuel_type": "Hardwood leaf litter, pine understory, mountain laurel/rhododendron",
        "base_condition": (
            "Fall drought season — southern Appalachians are vulnerable to "
            "extreme fire during periodic fall drought cycles. Leaf drop creates "
            "deep litter beds. Decades of fire suppression have created heavy "
            "understory fuel loading in mountain laurel and rhododendron thickets. "
            "The 2016 drought was the worst in the region since 1895 and burned "
            "119,000+ acres across 7 states, killing 14 people in Gatlinburg."
        ),
        "key_factors": [
            "Fall drought cycles are the primary fire driver — precipitation drops 50%+ below normal",
            "2016 Appalachian drought was worst since 1895 — 119,000+ acres burned across 7 states",
            "Steep terrain accelerates fire spread upslope and channels wind through valleys",
            "Chimney effect in narrow mountain valleys (Gatlinburg, Deadwood Gulch) amplifies winds",
            "Decades of fire suppression created heavy fuel loading in traditionally fire-free ecosystems",
            "Leaf drop (Oct-Nov) creates deep, dry litter beds that carry fire through hardwood forests",
            "Mountain laurel and rhododendron understory retains dead material and burns intensely",
            "WUI development on mountain ridgelines and in narrow valleys maximizes exposure",
            "Limited evacuation routes in mountain communities create life-safety emergencies",
            "Arson is a leading ignition source — 2016 Gatlinburg fire was arson-caused",
        ],
        "critical_thresholds": {
            "precip_deficit_pct": "50%+ below normal for 2+ months = extreme fire conditions",
            "rh_below_20": "Daytime RH <20% with wind = critical fire weather in mountains",
            "wind_above_40mph": "40+ mph gusts = Gatlinburg-type firestorm conditions (87 mph in 2016)",
            "drought_monitor": "D3-D4 (Extreme/Exceptional) = catastrophic fire potential",
            "keetch_byram_index": "KBDI >600 = critical fire potential in Appalachian hardwoods",
        },
    },
    "southeast_appalachian_spring": {
        "months": [3, 4, 5],
        "regions": ["TN_smokies", "NC_western", "GA_northeast"],
        "lat_range": (33.5, 37.0),
        "lon_range": (-85.0, -80.0),
        "fuel_type": "Dead leaf litter before green-up, dormant understory",
        "base_condition": (
            "Secondary fire season before spring green-up. Dead leaf litter "
            "from fall/winter is dry. Understory has not leafed out, allowing "
            "solar drying of forest floor. Prescribed burns are conducted during "
            "this window by USFS and NPS."
        ),
        "key_factors": [
            "Before green-up (March-April), forest floor litter is dry and continuous",
            "Lower sun angle means less moisture recovery than summer",
            "Prescribed burns are common — escaped burns occasionally become wildfires",
            "Spring wind events can be strong but rarely as extreme as fall drought events",
            "Green-up by late April typically ends the spring fire window",
        ],
        "critical_thresholds": {
            "green_up_pct": "Below 20% green-up = fire behavior similar to fall",
            "precip_free_days": "10+ days without precip = dry litter beds",
        },
    },

    # =========================================================================
    # SOUTHEAST — Florida Pine Flatwoods
    # =========================================================================
    "florida_panhandle_yearround": {
        "months": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "regions": ["FL_panhandle", "FL_north", "FL_central"],
        "lat_range": (27.5, 31.0),
        "lon_range": (-87.5, -80.0),
        "fuel_type": "Longleaf/slash pine flatwoods, palmetto, gallberry, sand pine scrub",
        "base_condition": (
            "Florida has year-round fire potential. Pine flatwoods are fire-dependent "
            "and require prescribed fire every 18 months to 4 years. Without fire, "
            "palmetto understory grows to 15 ft and becomes explosively flammable. "
            "Florida is the #1 prescribed burn state (~2.3M acres/year) because "
            "the ecosystem demands it. Lightning is abundant (FL is the US lightning "
            "capital). The 1998 fire season burned 500,000+ acres across Florida."
        ),
        "key_factors": [
            "Year-round fire potential — no safe 'off season'",
            "Spring drought (Feb-May) is the primary wildfire season",
            "Summer thunderstorms provide abundant lightning ignition",
            "Palmetto (saw palmetto) is the dominant understory — extremely flammable",
            "Gallberry, wax myrtle, and invasive Melaleuca add volatile fuel",
            "Sand pine scrub is serotinous (requires fire to reproduce) and burns intensely",
            "Hurricane debris (Michael 2018) created multi-year fuel loading crisis",
            "Florida's WUI is extensive — development throughout pine flatwoods",
            "Prescribed fire is the primary management tool but escaped burns are a risk",
        ],
        "critical_thresholds": {
            "palmetto_height_ft": "Palmetto >6 ft without recent fire = extreme fuel",
            "kbdi_above_500": "KBDI >500 = elevated fire potential in FL fuels",
            "kbdi_above_700": "KBDI >700 = extreme fire potential (1998-type conditions)",
            "days_since_rain": "14+ days = critically dry flatwoods",
        },
    },

    # =========================================================================
    # CENTRAL TEXAS — Lost Pines
    # =========================================================================
    "central_texas_summer_fall": {
        "months": [6, 7, 8, 9, 10],
        "regions": ["TX_central", "TX_bastrop"],
        "lat_range": (29.5, 31.5),
        "lon_range": (-98.5, -96.5),
        "fuel_type": "Loblolly pine (Lost Pines), post oak savanna, grassland",
        "base_condition": (
            "Summer heat and periodic drought create extreme fire conditions "
            "in the Lost Pines ecosystem and surrounding post oak savanna. The "
            "2011 Bastrop Complex Fire burned during one of the worst droughts "
            "in Texas history (exceptional drought statewide). Pine litter and "
            "understory in the Lost Pines are highly flammable during drought."
        ),
        "key_factors": [
            "Exceptional drought years (2011, 2022-2023) create catastrophic fire potential",
            "Lost Pines is an isolated, fire-vulnerable pine ecosystem",
            "100+ degree days cure vegetation rapidly",
            "Tropical storm/hurricane wind events can knock trees onto power lines (2011 trigger)",
            "Post oak savanna surrounding Lost Pines carries grass fire to pine interface",
            "WUI development throughout the pine forest maximizes exposure",
        ],
        "critical_thresholds": {
            "drought_level": "D3+ drought = extreme fire potential in Lost Pines",
            "days_above_100f": "Extended 100F+ heat = fuels critically dry",
            "tropical_wind_event": "Tropical storm winds + drought + power lines = 2011 scenario",
        },
    },

    # =========================================================================
    # BLACK HILLS — South Dakota
    # =========================================================================
    "black_hills_spring_summer": {
        "months": [3, 4, 5, 6, 7, 8, 9],
        "regions": ["SD_black_hills", "WY_northeast"],
        "lat_range": (43.0, 45.0),
        "lon_range": (-104.5, -103.0),
        "fuel_type": "Ponderosa pine, grass understory, mixed pine-grass transition",
        "base_condition": (
            "The Black Hills fire season extends from March through September, "
            "with peak risk in late spring (May-June) and mid-summer (July-Aug). "
            "Ponderosa pine dominates with dense stands from decades of fire "
            "suppression. The BHNF averages 92 wildfires/year burning 7,507 "
            "acres/year. ~70% are lightning-caused. The Jasper Fire (2000, "
            "83,508 acres) was the largest fire in SD history. The Legion Lake "
            "Fire (2017) burned 53,875 acres in December, proving year-round risk."
        ),
        "key_factors": [
            "Spring: increasing temperatures + decreasing humidity = rising fire risk",
            "Late spring (May-June): grass cures before pine transpiration peaks",
            "Summer: dry thunderstorms provide abundant lightning ignition",
            "Chinook (downslope) winds on east slope create extreme drying events",
            "Ponderosa pine dog-hair thickets (1,000+ stems/acre) from fire suppression",
            "Grass-pine transition allows fire to move from prairie into forest",
            "Year-round fire potential demonstrated by December 2017 Legion Lake Fire",
            "Isolated mountain range creates its own weather — dry thunderstorms common",
            "Narrow granite canyons (Deadwood, Spearfish, Needles) channel and amplify fire",
            "Heavy recreation use creates human ignition risk throughout fire season",
        ],
        "critical_thresholds": {
            "rh_below_15": "Daytime RH <15% = extreme fire conditions in pine",
            "wind_above_30mph": "30+ mph sustained = crown fire potential in dense pine",
            "temp_above_90f": "90F+ with <20% RH = very high fire danger",
            "drought_level": "D2+ drought = large fire potential across Hills",
            "1000hr_fm_below_13": "1000-hr fuel moisture <13% = extreme timber fire potential",
        },
        "normal_temps_f": {
            "rapid_city_may": 64,
            "rapid_city_jul": 87,
            "custer_may": 59,
            "custer_jul": 82,
        },
    },
    "black_hills_winter": {
        "months": [10, 11, 12, 1, 2],
        "regions": ["SD_black_hills"],
        "lat_range": (43.0, 45.0),
        "lon_range": (-104.5, -103.0),
        "fuel_type": "Ponderosa pine, dormant grass",
        "base_condition": (
            "Not traditionally considered fire season, but the Legion Lake Fire "
            "(December 2017, 53,875 acres) proved catastrophic winter fires are "
            "possible in the Black Hills. Chinook wind events can create extreme "
            "drying — Spearfish holds the world record for temperature change "
            "(49F in 2 minutes). When chinook winds combine with dry pine forest "
            "and no snow cover, winter fires can rapidly become large."
        ),
        "key_factors": [
            "Chinook (downslope) wind events create extreme warming and drying",
            "No snow cover + chinook = fire conditions equivalent to spring/summer",
            "Ponderosa pine retains needles year-round — always available as fuel",
            "Dormant grass under pine cures in autumn and remains fire-receptive all winter",
            "December 2017 Legion Lake Fire: 53,875 acres — one of the largest winter fires in US history",
        ],
        "critical_thresholds": {
            "chinook_wind_kt": "35+ kt sustained downslope wind = extreme drying",
            "snow_cover": "No snow cover + chinook = fire weather conditions",
            "temp_spike": "30+ degree temperature rise in hours = chinook event",
        },
    },

    # =========================================================================
    # HAWAII — Leeward Dry Season
    # =========================================================================
    "hawaii_leeward_summer_fall": {
        "months": [6, 7, 8, 9, 10, 11],
        "regions": ["HI_maui_leeward", "HI_big_island_leeward", "HI_oahu_leeward"],
        "lat_range": (19.5, 21.5),
        "lon_range": (-156.8, -155.0),
        "fuel_type": "Invasive guinea grass, buffelgrass, fountain grass, dried native dryland forest",
        "base_condition": (
            "Leeward (western) sides of Hawaiian islands experience extended dry "
            "seasons. Invasive African grasses (guinea grass, buffelgrass) that "
            "replaced native dryland forest and abandoned plantation land create "
            "continuous flashy fuels. Guinea grass grows 6 inches per day during "
            "wet season, then cures into tinder during summer drought. The 2023 "
            "Lahaina fire killed 102 people — the deadliest US wildfire in over "
            "100 years. Hurricane-force downslope winds from passing tropical "
            "cyclones can turn any ignition into a catastrophe."
        ),
        "key_factors": [
            "Invasive grass fuel bed is the fundamental vulnerability — continuous flashy fuel",
            "Guinea grass and buffelgrass replaced native dryland forest on leeward slopes",
            "Abandoned sugar/pineapple plantation land left unmanaged since 1990s",
            "Water diversion for development dried out formerly wet landscapes",
            "Hurricane/tropical storm pressure gradient creates downslope wind events",
            "2023 Lahaina: Hurricane Dora south + high pressure north = 60-80 kt downslope winds",
            "Trade wind disruption (Kona pattern) creates anomalous wind directions",
            "Kona winds (Oct-Apr) bring wind from normally leeward direction",
            "Power line infrastructure vulnerable to extreme winds — no PSPS program in 2023",
            "Steep volcanic terrain channels wind through gulches into coastal communities",
            "Limited evacuation routes — single coastal highway in many areas",
        ],
        "critical_thresholds": {
            "wind_above_40mph": "40+ mph downslope = extreme fire spread in grass fuels",
            "wind_above_60mph": "60+ mph = Lahaina-type catastrophe conditions (2023 had 60-80 kt)",
            "rh_below_15": "Dry downslope air can drop RH below 10%",
            "grass_cured_pct": "Guinea/buffel grass 80%+ cured = continuous flashy fuel",
            "tropical_cyclone_proximity": (
                "Tropical cyclone within 500 miles creates pressure gradient for "
                "extreme downslope winds — the 2023 trigger"
            ),
        },
    },

    # =========================================================================
    # MIDWEST — Missouri Ozarks
    # =========================================================================
    "ozarks_spring_fall": {
        "months": [3, 4, 5, 10, 11],
        "regions": ["MO_sw", "AR_nw", "OK_ne"],
        "lat_range": (35.5, 37.5),
        "lon_range": (-95.0, -91.0),
        "fuel_type": "Oak-hickory-cedar forest, eastern redcedar understory, leaf litter",
        "base_condition": (
            "The Ozarks have two fire seasons: spring (Mar-May) before green-up "
            "and fall (Oct-Nov) after leaf drop. Eastern redcedar (Juniperus "
            "virginiana) has expanded dramatically across the Ozarks due to 60+ "
            "years of fire suppression. Cedar is extremely flammable — volatile "
            "oils, retained dead branches, ladder fuel structure. The historic "
            "fire regime was frequent low-intensity fire in oak-hickory savanna. "
            "Without fire, cedar has converted open woodland to dense forest."
        ),
        "key_factors": [
            "Eastern redcedar encroachment is the #1 fuel concern — doubled in extent since 1950",
            "Cedar volatile oils make it extremely flammable even when live",
            "Cedar retains dead branches creating natural ladder fuel to canopy",
            "Spring before green-up: deep leaf litter from oak/hickory caries fire",
            "Fall after leaf drop: similar conditions as spring but with drought potential",
            "Karst terrain (limestone sinkholes, bluffs) creates variable fire behavior",
            "Prescribed fire is the primary management tool — Mark Twain NF burns regularly",
            "WUI expansion (Branson area) puts more structures in cedar-oak forest",
        ],
        "critical_thresholds": {
            "cedar_canopy_pct": "Cedar >30% of canopy = extreme fire intensity",
            "rh_below_25": "Daytime RH <25% in spring/fall = elevated fire risk in Ozarks",
            "precip_free_days": "10+ days without rain = dry litter beds",
            "wind_above_25mph": "25+ mph with dry fuels = rapid fire spread in cedar-oak",
        },
    },

    # =========================================================================
    # MIDWEST — Minnesota Boreal Edge
    # =========================================================================
    "minnesota_boreal_summer": {
        "months": [5, 6, 7, 8, 9],
        "regions": ["MN_northeast", "MN_arrowhead"],
        "lat_range": (46.0, 48.5),
        "lon_range": (-93.0, -89.5),
        "fuel_type": "Boreal conifer (black spruce, jack pine), birch, aspen",
        "base_condition": (
            "Southern edge of the North American boreal forest. Climate change "
            "is warming northern latitudes 3-4x faster than the global average, "
            "lengthening fire seasons and increasing fire-risk days. Boreal "
            "forests historically burn in stand-replacing crown fires every "
            "100-150 years, but this cycle is accelerating. 2021 was the worst "
            "boreal fire year on record globally — fires produced 25% of global "
            "wildfire CO2 emissions. 140+ buildings destroyed in St. Louis "
            "County fires north of Duluth."
        ),
        "key_factors": [
            "Climate change warming boreal zone 3-4x faster than global average",
            "Fire seasons lengthening — earlier snowmelt, later freeze-up",
            "Black spruce is highly flammable — resinous needles, dense stands",
            "Jack pine is serotinous (cones open with fire heat) — fire-adapted",
            "Stand-replacing crown fires are the natural fire regime — extreme behavior",
            "2021 boreal fires set records across North America",
            "Drought + heat = rapidly accelerating fire potential in boreal forest",
            "Lightning is the primary natural ignition source",
            "Lake Superior moderates climate along shore but interior is unprotected",
            "1918 Cloquet-Moose Lake Fire killed 453 — demonstrates catastrophic potential",
        ],
        "critical_thresholds": {
            "drought_level": "D2+ drought in boreal zone = extreme fire potential",
            "days_above_85f": "Extended 85F+ unusual for boreal — signals extreme drying",
            "canadian_fwi": "Canadian FWI >25 = high fire danger in boreal fuels",
            "1000hr_fm_below_15": "1000-hr fuel moisture <15% = large fire potential",
        },
    },
}
