"""
Utah & Wyoming Fire-Vulnerable City Profiles -- Research-Paper Quality
======================================================================
12 profiles covering the most fire-vulnerable communities in Utah and Wyoming.
4 enhanced existing cities + 8 new additions. Each profile includes terrain
analysis, historical fire data, evacuation infrastructure, fire spread
characteristics, infrastructure vulnerabilities, and demographic risk factors.

Sources:
- USFS InciWeb incident reports (2017-2025)
- Bridger-Teton, Shoshone, Dixie, Uinta-Wasatch-Cache National Forest records
- Utah Division of Forestry, Fire & State Lands
- Wyoming State Forestry Division
- US Census Bureau (2020 Census, ACS estimates)
- First Street Foundation wildfire risk assessments
- Utah Wildfire Risk Assessment Portal (UWRAP)
- NPS fire management records (Zion, Grand Teton, Yellowstone)
- Wyoming Game & Fish Department wildfire impact assessments
- Teton Interagency Fire Dispatch records
- Community Wildfire Protection Plans (CWPP) for Summit, Wasatch,
  Iron, Washington, Park, Fremont, Sublette, and Sheridan counties
- Peer-reviewed literature on WUI fire risk in Intermountain West
- Jackson Hole News & Guide, Cowboy State Daily, Park Record,
  St. George News, KSL, WyoFile reporting

Generated: 2026-02-09
"""

UT_WY_ENHANCED = {

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
