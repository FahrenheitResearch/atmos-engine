"""
Enhanced Washington State Fire-Vulnerable City Profiles
========================================================
Research-grade profiles for 12 fire-vulnerable communities in eastern Washington.

Data sources:
- USDA Forest Service wildfire records
- WA DNR Community Wildfire Protection Plans
- NOAA/NWS fire weather observations
- US Census Bureau (2020 Census)
- HistoryLink.org historical fire records
- Headwaters Economics / Community Planning Assistance for Wildfire (CPAW)
- First Street Foundation wildfire risk assessments
- InciWeb incident reports
- Okanogan County Long Term Recovery Group

Key historical context:
- 2014 Carlton Complex: 256,108 acres — largest single WA fire in recorded history
- 2015 WA fire season: >1 million acres statewide, worst season on record
- 2015 Twisp River Fire: 3 firefighter LODD (Wheeler, Zajac, Zbyszewski)
- East Cascades gap winds: Bernoulli-effect acceleration through Cascade passes
- Kittitas Valley: Snoqualmie Pass gap winds regularly exceed 60 mph

Generated: 2026-02-09
"""

PNW_WASHINGTON_ENHANCED = {

    # =========================================================================
    # 1. CHELAN, WA — Lakeside town, 2015 Chelan Complex
    # =========================================================================
    "chelan_wa": {
        "center": [47.8407, -120.0160],
        "terrain_notes": (
            "Chelan sits at the southeastern tip of Lake Chelan, a 50.5-mile-long glacially "
            "carved fjord-like lake that is the third-deepest lake in the United States (1,486 ft). "
            "The city occupies a narrow bench between the lakeshore (elev ~1,100 ft) and steep, "
            "south-facing hillsides of Chelan Butte (elev ~3,892 ft) that rise abruptly 2,800 ft "
            "above town. These south- and west-facing slopes are covered in dry cheatgrass, "
            "sagebrush, and scattered ponderosa pine — classic flashy fuels that carry fire rapidly "
            "uphill. The Chelan River gorge to the east channels winds between the Columbia River "
            "corridor and the lake basin. The combination of steep terrain, solar-heated south "
            "aspects, and wind acceleration through the lake-valley convergence zone creates "
            "extreme fire behavior conditions. During the 2015 Chelan Complex, five fires ignited "
            "simultaneously around the south end of the lake and merged into a wind-driven "
            "firestorm that overran the town, destroying 82 structures including the Chelan Lumber "
            "Company and multiple residences within the urban growth boundary. The town's WUI "
            "boundary extends directly into high-hazard fuels on Chelan Butte. Tourism population "
            "in summer can triple the year-round population, with thousands of visitors in "
            "lakeside resorts, RV parks, and vacation rentals — many unfamiliar with evacuation "
            "routes. The orchard economy (apples, cherries) also brings seasonal agricultural "
            "workers housed in temporary structures."
        ),
        "key_features": [
            {"name": "Lake Chelan", "bearing": "NW", "type": "water/terrain", "notes": "50.5-mi glacial lake, 1,486 ft deep; provides water supply but lake-effect winds can accelerate fire spread along shoreline corridors"},
            {"name": "Chelan Butte", "bearing": "S", "type": "terrain", "notes": "3,892 ft prominence directly above town; south-facing slopes with flashy fuels, fire runs uphill toward summit then crowns over into town"},
            {"name": "Columbia River / US 97A corridor", "bearing": "SE", "type": "terrain/transport", "notes": "Major wind corridor; gap winds funnel between Chelan basin and Columbia Plateau"},
            {"name": "Chelan River Gorge", "bearing": "E", "type": "terrain", "notes": "Narrow gorge connecting Lake Chelan outlet to Columbia River; channels wind and creates venturi acceleration"},
            {"name": "Lakeside Park / Downtown", "bearing": "center", "type": "urban", "notes": "Dense commercial/tourist core at lakeshore; limited defensible space on south edge"},
        ],
        "elevation_range_ft": [1079, 3892],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Chelan Complex", "year": 2015, "acres": 95000, "details": "Five fires merged on Aug 14; wind-driven firestorm destroyed 82 structures; 1,000+ evacuated; Chelan Lumber Company lost; $100M+ damages; fires burned into city limits"},
            {"name": "Chelan Butte Fire", "year": 2015, "acres": 500, "details": "Part of the complex; started on Chelan Butte's south face and raced uphill into structures on the ridge"},
            {"name": "Apple Acres Fire", "year": 2025, "acres": 2000, "details": "Forced Level 2 evacuations; closed Highway 97; demonstrated continued vulnerability of US 97 corridor"},
            {"name": "First Creek Fire", "year": 2015, "acres": 800, "details": "One of five fires in the Chelan Complex; burned near First Creek drainage west of town"},
        ],
        "evacuation_routes": [
            {"route": "US 97A south to Wenatchee", "direction": "S/SE", "lanes": 2, "bottleneck": "Single 2-lane highway along Columbia River; only 2,800-12,000 ADT capacity; closures during 2015 and 2025 fires", "risk": "Route passes through fire-prone terrain for 40 miles; multiple fires have closed this corridor"},
            {"route": "SR 150 west to Manson", "direction": "W", "lanes": 2, "bottleneck": "Dead-end route to Manson; no through-connection; evacuees must return to Chelan to exit", "risk": "Leads into another fire-vulnerable community with single-road access; closed during 2015 fires"},
            {"route": "US 97 north to Pateros", "direction": "N", "lanes": 2, "bottleneck": "Passes through steep canyon terrain along Columbia; historically closed by Carlton Complex fires", "risk": "Narrow canyon road vulnerable to rockfall and fire closure simultaneously"},
            {"route": "Lake Chelan boat evacuation", "direction": "NW", "lanes": 0, "bottleneck": "Lady of the Lake ferry has limited capacity; no nighttime service; dock congestion", "risk": "Weather-dependent; smoke reduces visibility; not viable for mass evacuation"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Diurnal lake-valley circulation with strong afternoon upslope/upvalley winds; synoptic events produce gap winds from Columbia Plateau funneling through Chelan River gorge at 25-40 mph; east wind events push fire westward into town from Chelan Butte",
            "critical_corridors": [
                "Chelan Butte south-facing slope — flashy fuels carry fire from US 97A corridor directly into south-side neighborhoods",
                "Chelan River gorge — wind acceleration zone connecting Columbia River to lake basin",
                "Lake Chelan south shore — fire can spread along steep shoreline slopes above lakeside resorts",
                "First Creek and vicinity — drainage channels funnel fire uphill into developed areas"
            ],
            "rate_of_spread_potential": "Extreme in grass/sage on Chelan Butte (3-5 mph with 20-ft flame lengths); moderate-high in mixed conifer on surrounding ridges; 2015 Complex demonstrated 10,000+ acre runs in single burning periods",
            "spotting_distance": "1-2 miles in grass/sage with 30+ mph winds; bark/ember transport from ponderosa pine can reach 0.5 mile; upslope terrain enhances lofting"
        },
        "infrastructure_vulnerabilities": {
            "water_system": "Chelan Water Department serves 9,355 connections from surface water; East Chelan Reservoir Project ($9M) addresses pressure issues; system stressed during simultaneous firefighting and domestic demand; gravity-fed from lake is reliable but distribution capacity limits concurrent fire suppression",
            "power": "Chelan County PUD hydroelectric (Lake Chelan Dam); above-ground distribution lines vulnerable to fire damage; 2015 fires caused widespread outages; limited backup generation for critical facilities",
            "communications": "Cell towers on Chelan Butte vulnerable to fire damage; 2015 fires degraded cell service during peak evacuation; limited landline redundancy in rural areas around lake",
            "medical": "Lake Chelan Community Hospital (25-bed critical access); nearest Level II trauma is Central Washington Hospital in Wenatchee (40 mi south on fire-vulnerable US 97A); medical helicopter operations limited by smoke"
        },
        "demographics_risk_factors": {
            "population": 4222,
            "seasonal_variation": "Summer tourism triples effective population to 12,000+; Labor Day and 4th of July peak periods coincide with peak fire season; vacation rental occupants unfamiliar with evacuation procedures",
            "elderly_percentage": "~22% over 65 (median age 46.7); significant retiree population in lakeside communities",
            "mobile_homes": "Several mobile home parks on south and east edges of town in high-exposure WUI zones; limited defensible space",
            "special_needs_facilities": "Heritage Heights assisted living; Lake Chelan Community Hospital long-term care; seasonal agricultural worker housing with limited fire notification systems"
        }
    },

    # =========================================================================
    # 2. WENATCHEE, WA — East Cascades city, 2015 Sleepy Hollow Fire
    # =========================================================================
    "wenatchee_wa": {
        "center": [47.4235, -120.3103],
        "terrain_notes": (
            "Wenatchee (pop 35,508) is the largest city in north-central Washington, located at "
            "the confluence of the Wenatchee and Columbia Rivers at the eastern base of the "
            "Cascade Range. The city sits in a broad valley (elev ~630-700 ft at river level) "
            "surrounded by steep, sage-covered hillsides to the west and south that rise sharply "
            "1,500-2,500 ft above the valley floor. These west-facing hillsides, covered in "
            "cheatgrass, sagebrush, bitterbrush, and scattered ponderosa pine, form a classic "
            "WUI interface where residential development has pushed directly into high-hazard "
            "fuels. The Cascade gap-wind phenomenon is pronounced here: as marine air pushes "
            "through Cascade passes (particularly Blewett Pass and Stevens Pass corridors), it "
            "accelerates via the Bernoulli effect as it descends the eastern slopes, reaching "
            "30-40 mph in the Wenatchee Valley. These desiccating east-slope winds combine with "
            "triple-digit summer temperatures and single-digit humidity to create extreme fire "
            "weather. The 2015 Sleepy Hollow Fire demonstrated this vulnerability when a wind-"
            "driven grass fire raced 3 miles from open rangeland into dense residential areas in "
            "hours, destroying 28 homes and 3 commercial warehouses. The fire started in open "
            "sage west of town and burned directly into 'a pretty dense urban interface area,' "
            "forcing evacuation of 1,000+ residents. Wenatchee's role as a regional commercial "
            "and medical hub means fire impacts cascade through the broader region."
        ),
        "key_features": [
            {"name": "Western hillsides (Sleepy Hollow area)", "bearing": "W", "type": "terrain/WUI", "notes": "Steep sage/grass slopes where 2015 fire originated; dense residential development extends into flashy fuels; south/west-facing aspects maximize solar heating"},
            {"name": "Columbia River corridor", "bearing": "E", "type": "terrain/transport", "notes": "Major north-south wind corridor; US 2/97 runs along river; provides some firebreak but wind channeling"},
            {"name": "Wenatchee River corridor", "bearing": "W", "type": "terrain", "notes": "River valley extends west toward Leavenworth; gap wind corridor from Cascade crest"},
            {"name": "Saddle Rock / Number 2 Canyon", "bearing": "S", "type": "terrain", "notes": "Prominent ridgeline south of town; fire can approach from Number 2 Canyon drainage; communication towers on ridge"},
            {"name": "Downtown / commercial core", "bearing": "center", "type": "urban", "notes": "Regional commercial hub at river level; relatively protected by flat terrain but smoke impacts severe"},
        ],
        "elevation_range_ft": [630, 3100],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Sleepy Hollow Fire", "year": 2015, "acres": 3000, "details": "Started June 28 in grass/sage 3 mi W of town; wind-driven (gusts 30+ mph) with triple-digit temps; destroyed 28 homes and 3 commercial warehouses; 1,000+ evacuated; burned into dense residential WUI; arson — juvenile arrested"},
            {"name": "Number 2 Canyon Fire", "year": 2012, "acres": 400, "details": "Fast-moving grass fire in canyon south of town; threatened homes on south benchlands; demonstrated vulnerability of southern approach"},
            {"name": "Wenatchee hillside fires", "year": 2024, "acres": 150, "details": "Recurring grass fires on western slopes demonstrate ongoing ignition risk from human activity and equipment"},
        ],
        "evacuation_routes": [
            {"route": "US 2/97 north along Columbia River", "direction": "N", "lanes": 4, "bottleneck": "4-lane divided highway provides best capacity; narrows to 2 lanes north of East Wenatchee", "risk": "Route parallels fire-prone hillsides for first 5 miles; smoke can reduce visibility on river bridge"},
            {"route": "US 2 west to Leavenworth/Stevens Pass", "direction": "W", "lanes": 2, "bottleneck": "2-lane highway through Tumwater Canyon; single-point failure at canyon narrows; historically closed by fire", "risk": "Passes through heavily forested canyon with no alternate routes for 25+ miles"},
            {"route": "US 97A south to Ellensburg via Blewett Pass", "direction": "S", "lanes": 2, "bottleneck": "Mountainous 2-lane road over Blewett Pass (4,102 ft); slow-moving traffic with trucks", "risk": "Pass road through dense forest; fire or landslide closure creates 100+ mile detour"},
            {"route": "SR 285 / US 2 east to East Wenatchee", "direction": "E", "lanes": 4, "bottleneck": "Columbia River bridge is single point of failure; 2 bridges available but converge at interchanges", "risk": "Bridge evacuation bottleneck if fire threatens from west simultaneously; East Wenatchee has own fire exposure"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Cascade gap winds (Bernoulli effect) accelerate through Stevens Pass and Blewett Pass corridors, reaching 30-40 mph at valley floor; diurnal upslope/downslope cycle on western hillsides; east wind events less common but devastating when they occur",
            "critical_corridors": [
                "Western benchlands (Sleepy Hollow) — grass/sage slopes funnel fire directly into residential areas within 30 min",
                "Number 2 Canyon — south-facing drainage channels fire uphill into developed ridgeline",
                "Wenatchee River corridor — gap wind acceleration zone connecting Cascade crest to valley",
                "Squilchuck Creek drainage — southwest approach through mixed fuels to south Wenatchee"
            ],
            "rate_of_spread_potential": "Extreme in grass/sage (3-6 mph with 20+ ft flame lengths during wind events); the 2015 Sleepy Hollow Fire covered 3 miles of sage into residential areas in ~4 hours; ponderosa stringers on hillsides enable crown fire runs",
            "spotting_distance": "0.5-1.5 miles in sage/grass with wind; bark transport from ponderosa can exceed 0.5 mile; downslope rollout of burning material on steep slopes extends effective spotting range"
        },
        "infrastructure_vulnerabilities": {
            "water_system": "City of Wenatchee water from Columbia River treatment plant and wells; system adequate for normal demand but simultaneous structure protection across the WUI strains hydrant pressure in upper-elevation neighborhoods; 2015 fire revealed pressure drops in hillside areas",
            "power": "Chelan County PUD hydroelectric; above-ground distribution extensively damaged in 2015 fire; hillside transformer stations in high-exposure areas; limited underground infrastructure in WUI zones",
            "communications": "Cell towers on Saddle Rock and western ridges vulnerable to fire; 2015 Sleepy Hollow Fire degraded communications during critical evacuation period; county emergency notification system (CodeRED) dependent on cell/internet",
            "medical": "Central Washington Hospital (Level II trauma, 210 beds) — regional medical center serving 250,000+ across 5 counties; hospital itself not in direct fire path but smoke impacts air quality; medical helicopter ops limited by smoke; loss of this facility cascades across entire region"
        },
        "demographics_risk_factors": {
            "population": 35508,
            "seasonal_variation": "Apple harvest season (Aug-Oct) brings 5,000-10,000 seasonal agricultural workers, many in temporary housing; summer recreation increases population; regional hub draws workers from surrounding communities",
            "elderly_percentage": "~15% over 65; multiple senior living facilities on benchlands in WUI-adjacent areas",
            "mobile_homes": "Multiple manufactured home parks, particularly on east and south edges; many lack defensible space; older units with combustible siding and roofing",
            "special_needs_facilities": "Central Washington Hospital; multiple assisted living facilities; seasonal worker camps with language barriers for fire notification (Spanish-speaking workforce ~30%); homeless population along river corridor"
        }
    },

    # =========================================================================
    # 3. LEAVENWORTH, WA — Tumwater Canyon bottleneck, Bavarian village
    # =========================================================================
    "leavenworth_wa": {
        "center": [47.5962, -120.6615],
        "terrain_notes": (
            "Leavenworth (pop 2,263) is a Bavarian-themed tourist village nestled in a narrow "
            "valley at the confluence of the Wenatchee River and Icicle Creek, flanked by steep, "
            "forested mountain slopes rising 4,000-6,000 ft above the valley floor. The town sits "
            "at 1,168 ft elevation at a critical geographic chokepoint: US Highway 2 — the only "
            "east-west highway between Stevens Pass and Blewett Pass (a 70-mile gap) — threads "
            "through Tumwater Canyon immediately west of town, a narrow, deeply forested gorge "
            "with vertical rock walls where the Wenatchee River has carved through bedrock. This "
            "canyon is the single most critical evacuation bottleneck in the central Cascades: "
            "when fire or debris closes US 2 through Tumwater Canyon, Leavenworth is effectively "
            "cut off from western Washington. The only alternative route is Chumstick Highway "
            "(SR 209) north to US 2 at Coles Corner — a narrow, winding rural road with bridge "
            "restrictions. The valley's steep, south-facing slopes above town are covered in "
            "dense mixed conifer (Douglas fir, ponderosa pine) with heavy dead fuel loads from "
            "decades of fire suppression and insect kill (mountain pine beetle). Fires run uphill "
            "at extreme rates on these slopes and crown easily in the dense canopy. Icicle Creek "
            "corridor to the south provides another fire approach vector through the Alpine Lakes "
            "Wilderness interface. Tourism drives the economy: the village hosts over 2 million "
            "visitors annually for Oktoberfest, Christmas Lighting Festival, and summer recreation, "
            "with peak weekend populations exceeding 30,000 — potentially catastrophic for "
            "evacuation on a 2-lane highway system."
        ),
        "key_features": [
            {"name": "Tumwater Canyon", "bearing": "W", "type": "terrain/transport", "notes": "Narrow rock-walled gorge carrying US 2 and Wenatchee River; 21-mile section from Coles Corner; fires have closed this corridor multiple times; single-point evacuation failure"},
            {"name": "Icicle Creek corridor", "bearing": "S", "type": "terrain", "notes": "Valley extending south into Alpine Lakes Wilderness; Icicle Road provides access to campgrounds and trailheads; fire approach vector from south through dense forest"},
            {"name": "Tumwater Mountain", "bearing": "W/NW", "type": "terrain", "notes": "Steep forested slopes above canyon; fire on these slopes can close US 2 and trap town"},
            {"name": "Wedge Mountain / Chumstick area", "bearing": "N/NE", "type": "terrain", "notes": "North valley slopes; Chumstick Highway runs through this area; alternative evacuation route through fire-prone pine forest"},
            {"name": "Bavarian Village downtown", "bearing": "center", "type": "urban", "notes": "Dense tourist commercial district with timber-frame construction; narrow streets; limited fire breaks; 2M+ annual visitors"},
        ],
        "elevation_range_ft": [1100, 7000],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Tumwater Canyon fires (multiple)", "year": 2024, "acres": 200, "details": "Two sudden wildfires in Tumwater Canyon closed US 2; fires devoured timber in hot/breezy conditions; demonstrated canyon closure vulnerability"},
            {"name": "Icicle Creek Fire", "year": 2015, "acres": 500, "details": "Fire near Icicle Road prompted evacuations and closure of US 2 from Icicle Road junction to Coles Corner; 49-mile highway section affected"},
            {"name": "Rat Creek Fire", "year": 2018, "acres": 6800, "details": "Burned in Wenatchee River drainage upstream of town; closed Highway 2; threatened water supply watershed"},
            {"name": "Hatchery Creek Fire", "year": 2012, "acres": 6200, "details": "Started near Leavenworth National Fish Hatchery on Icicle Creek; rapid uphill spread in steep terrain; forced level 3 evacuations; hundreds of homes threatened"},
        ],
        "evacuation_routes": [
            {"route": "US 2 east to Wenatchee", "direction": "E", "lanes": 2, "bottleneck": "Best available route but passes through fire-prone pine/sage transition zone for 20 miles", "risk": "Heavy tourist traffic creates congestion; 2-lane with limited passing; smoke visibility issues"},
            {"route": "US 2 west through Tumwater Canyon to Stevens Pass", "direction": "W", "lanes": 2, "bottleneck": "CRITICAL: Narrow canyon, single 2-lane road, no shoulders, vertical rock walls; closed by fire multiple times (2015, 2018, 2024, 2025)", "risk": "When closed, eliminates access to western WA for 70+ miles of Cascade crest; no alternate highway"},
            {"route": "Chumstick Highway (SR 209) north to Coles Corner", "direction": "N", "lanes": 2, "bottleneck": "Narrow rural road with bridge restrictions; low-speed winding alignment; limited capacity", "risk": "Passes through fire-prone pine forest; convergence with US 2 at Coles Corner can create secondary bottleneck; not designed for mass evacuation"},
            {"route": "Icicle Road south", "direction": "S", "lanes": 2, "bottleneck": "Dead-end road into Alpine Lakes Wilderness; no through-route; leads to campgrounds with trapped visitors", "risk": "Becomes a trap during fire; no exit at end of road; fire approach from south traps recreationists"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Cascade gap winds accelerating through Stevens Pass corridor descend through Tumwater Canyon; diurnal upvalley winds from Wenatchee Valley reach 15-25 mph by afternoon; east wind (foehn-type) events produce hot, dry downslope winds exceeding 35 mph",
            "critical_corridors": [
                "Tumwater Canyon — fire in canyon closes the sole westward evacuation route; steep canyon walls create extreme updrafts",
                "Icicle Creek drainage — south approach through dense conifer; fire runs upcanyon on afternoon winds directly toward town",
                "Chumstick drainage — north approach through ponderosa/Douglas fir; threatens alternate evacuation route",
                "Wenatchee River corridor east — fire spread along river valley toward town on diurnal valley winds"
            ],
            "rate_of_spread_potential": "Extreme on steep forested slopes (crown fire at 1-3 mph with 100+ ft flame lengths); terrain-driven fire runs on 40-60% slopes can achieve rates of 3-5 mph; decades of fire suppression have created continuous canopy fuels with heavy dead ladder fuels",
            "spotting_distance": "1-3 miles from crown fire in dense conifer; Tumwater Canyon creates chimney-effect lofting that can transport embers extraordinary distances; cross-canyon spotting can trap firefighters and evacuees"
        },
        "infrastructure_vulnerabilities": {
            "water_system": "City water from Wenatchee River and wells; treatment plant at valley floor is defensible but distribution lines to hillside homes vulnerable; fire flow capacity limited in upper-elevation residential areas; drought years reduce river levels",
            "power": "Chelan County PUD; overhead transmission lines through Tumwater Canyon extremely vulnerable to fire and tree-fall; loss of transmission isolates town from regional grid; limited emergency generation for extended outages",
            "communications": "Mountain terrain limits cell coverage to valley floor; towers on surrounding ridges vulnerable to fire; Tumwater Canyon has dead zones; satellite communication limited by steep terrain; radio repeater sites on ridges in fire-prone areas",
            "medical": "Cascade Medical Center (small critical access hospital/clinic); nearest major hospital is Central Washington Hospital in Wenatchee, 22 miles east on fire-vulnerable US 2; medical helicopter operations severely limited by canyon terrain and smoke"
        },
        "demographics_risk_factors": {
            "population": 2263,
            "seasonal_variation": "EXTREME: 2M+ annual visitors; peak weekends (Oktoberfest, Christmas Lighting) bring 30,000+ visitors to 2,300-person town; summer weekends 10,000-15,000; campgrounds and vacation rentals add thousands unfamiliar with evacuation routes",
            "elderly_percentage": "~20% over 65; retirement community character; Bavarian Village condo complexes have senior-heavy populations",
            "mobile_homes": "Limited within city; some manufactured housing in Peshastin (3 mi east) and along Chumstick Highway; rural homesteads with limited defensible space",
            "special_needs_facilities": "Cascade Medical Center long-term care; Mountain Meadows senior campus; multiple campgrounds with families and disabled visitors; Leavenworth National Fish Hatchery staff housing in fire zone"
        }
    },

    # =========================================================================
    # 4. ELLENSBURG, WA — Kittitas Valley wind corridor
    # =========================================================================
    "ellensburg_wa": {
        "center": [46.9965, -120.5478],
        "terrain_notes": (
            "Ellensburg (pop 21,210) sits in the heart of the Kittitas Valley, a broad east-west "
            "trending valley between the Cascade Range to the west and the Manastash and Umtanum "
            "Ridges to the south. The valley is the outlet of the Snoqualmie Pass wind corridor, "
            "one of the most powerful gap-wind features in the Pacific Northwest. When pressure "
            "gradients develop across the Cascades, marine air funnels through Snoqualmie Pass "
            "(elev 3,022 ft) and accelerates as it descends 2,000+ ft into the Kittitas Valley, "
            "regularly producing sustained winds of 40-60 mph with gusts exceeding 80 mph at the "
            "pass and 50-60 mph in the valley. These winds are the defining fire risk factor for "
            "Ellensburg: the 2012 Taylor Bridge Fire demonstrated how a small ignition (welding "
            "sparks during bridge construction on SR 10) can explode into a 23,500-acre wind-"
            "driven fire that destroys 61 homes in conditions that overwhelm suppression efforts. "
            "The city is surrounded by a sea of dryland wheat stubble, CRP grassland, and "
            "sagebrush — flashy fuels that burn at highway speed in wind events. Central "
            "Washington University (10,000 students) is located in the city center. I-90 runs "
            "east-west through the valley, providing evacuation capacity but also serving as a "
            "fire corridor when grass fires cross the interstate. The Yakima River canyon to the "
            "south (SR 821) is another confined route vulnerable to closure."
        ),
        "key_features": [
            {"name": "Snoqualmie Pass wind corridor", "bearing": "W", "type": "meteorological", "notes": "Gap wind acceleration zone; sustained 40-60 mph winds during pressure gradient events; primary fire driver for entire Kittitas Valley"},
            {"name": "Manastash Ridge", "bearing": "S", "type": "terrain", "notes": "Ridge forming southern valley wall; sagebrush and grassland on north slopes; Manastash Creek drainage provides fire approach vector"},
            {"name": "Umtanum Ridge", "bearing": "SW", "type": "terrain", "notes": "Basalt ridge with grass/sage fuels; L.T. Murray Wildlife Area on slopes; fire can approach from Yakima Training Center"},
            {"name": "I-90 / SR 10 corridor", "bearing": "W-E", "type": "transport", "notes": "Interstate provides evacuation capacity but grass fires cross I-90 in wind events; SR 10 follows Yakima River and was site of Taylor Bridge Fire ignition"},
            {"name": "Central Washington University", "bearing": "center", "type": "institutional", "notes": "10,000 students and staff; campus in city center; evacuation of student body compounds traffic"},
        ],
        "elevation_range_ft": [1500, 3022],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Taylor Bridge Fire", "year": 2012, "acres": 23500, "details": "Welding sparks on SR 10 bridge ignited grass during Red Flag Warning (Aug 13); winds 5-30 mph drove fire; 61 homes destroyed; 1,000 firefighters; $59.75M settlement; burned for 15 days"},
            {"name": "Vantage Highway fires", "year": 2018, "acres": 45000, "details": "Wind-driven grass fire east of Ellensburg; I-90 closures; demonstrated vast extent of flashy fuels surrounding city"},
            {"name": "Kittitas Valley grass fires", "year": 2024, "acres": 500, "details": "Wind-driven fire SW of Ellensburg quickly contained; gap winds accelerated spread; ongoing pattern of wind-driven grass fires"},
        ],
        "evacuation_routes": [
            {"route": "I-90 east to Moses Lake/Spokane", "direction": "E", "lanes": 4, "bottleneck": "Best capacity route but grass fires have crossed I-90 during wind events; visibility reduced by smoke", "risk": "Wide-open grassland on both sides; fire can cross divided highway in extreme wind; wildfire closures have occurred"},
            {"route": "I-90 west to Cle Elum/Seattle", "direction": "W", "lanes": 4, "bottleneck": "4-lane interstate but climbs into forested terrain toward Snoqualmie Pass; winter closures; wind events", "risk": "Heading into wind corridor during gap-wind events; Cle Elum area has own fire risk; pass can close"},
            {"route": "US 97 north to Wenatchee via Blewett Pass", "direction": "N", "lanes": 2, "bottleneck": "2-lane mountain road over 4,102-ft pass; slow with truck traffic; limited capacity", "risk": "Forested route through fire-prone terrain; pass closure creates long detour"},
            {"route": "SR 821 south through Yakima River Canyon", "direction": "S", "lanes": 2, "bottleneck": "Narrow canyon road; 23 miles of confined route with no alternate exits; scenic but deadly if fire enters canyon", "risk": "Basalt walls, grass/sage fuels on slopes, limited turnouts; fire in canyon would trap evacuees"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Snoqualmie Pass gap winds dominate: marine push events create pressure gradient that accelerates westerly flow to 40-60+ mph in valley; thermal low development over Columbia Basin enhances afternoon winds; nocturnal drainage winds from surrounding ridges",
            "critical_corridors": [
                "I-90 corridor from Cle Elum to Vantage — wind-aligned grass fire runway spanning 60+ miles",
                "Manastash Creek drainage — channels fire from forested ridges into south edge of city",
                "Yakima River canyon (SR 821) — confined fire spread corridor with no escape",
                "SR 10 / Taylor Creek area — proven ignition zone where fire reached city outskirts in 2012"
            ],
            "rate_of_spread_potential": "EXTREME in grass/sage: 5-10+ mph spread rates documented during gap-wind events; flame lengths 15-25 ft in sagebrush; Taylor Bridge Fire spread 10+ miles in first 12 hours; CRP grasslands provide continuous fine fuels across entire valley floor",
            "spotting_distance": "2-4 miles in grass with 50+ mph winds; firebrands from sage can travel 1+ mile; fires routinely cross I-90 (4 lanes + median) during wind events, indicating spotting distances exceed 200 ft even across firebreaks"
        },
        "infrastructure_vulnerabilities": {
            "water_system": "City of Ellensburg water from Yakima River and wells; adequate supply but hillside areas south and west of town have reduced pressure during high-demand events; CWU campus has independent fire suppression system",
            "power": "Kittitas County PUD and Puget Sound Energy; extensive above-ground transmission lines extremely vulnerable to wind damage (gap winds regularly down power lines, causing ignitions); wind farm infrastructure on ridges adds to grid complexity",
            "communications": "Cell towers on surrounding ridges vulnerable to wind damage and fire; gap-wind events can knock out communication infrastructure; CWU campus has independent systems; rural areas east and south have limited coverage",
            "medical": "Kittitas Valley Healthcare Hospital (25-bed critical access); nearest Level II trauma is Yakima (36 mi) or Wenatchee (65 mi); both routes traverse fire-vulnerable terrain; medical helicopter ops limited by wind events"
        },
        "demographics_risk_factors": {
            "population": 21210,
            "seasonal_variation": "CWU academic year adds ~10,000 students (Sept-June); Ellensburg Rodeo (Labor Day) brings 25,000+ visitors; irrigation season brings agricultural workers; summer recreation traffic on I-90",
            "elderly_percentage": "~12% over 65 (lower due to university; but surrounding rural areas have higher elderly populations)",
            "mobile_homes": "Significant manufactured housing stock on east and south edges of town; many older units; mobile home parks in wind-exposed locations",
            "special_needs_facilities": "Kittitas Valley Healthcare extended care; Hal Holmes Community Center (evacuation shelter); CWU dormitories with 3,000+ students requiring coordinated evacuation; multiple rural homesteads with elderly residents"
        }
    },

    # =========================================================================
    # 5. WINTHROP, WA — Methow Valley, Carlton Complex
    # =========================================================================
    "winthrop_wa": {
        "center": [48.4793, -120.1861],
        "terrain_notes": (
            "Winthrop (pop 504) is a small Western-themed tourist town at the confluence of the "
            "Methow and Chewuch Rivers in the upper Methow Valley, surrounded by the Okanogan-"
            "Wenatchee National Forest. The town sits at approximately 1,765 ft elevation in a "
            "relatively broad portion of the valley, but is hemmed in by steep, forested mountain "
            "slopes rising to 7,000-8,500 ft on all sides. The Methow Valley runs roughly north-"
            "south for 50 miles from Mazama to Pateros, forming a natural fire corridor that "
            "channels wind and fire along its length. Highway 20 (North Cascades Highway) is the "
            "sole east-west route, but it is CLOSED from mid-November to mid-April due to snow, "
            "leaving SR 153 south through Twisp and Pateros as the only year-round access. During "
            "the 2014 Carlton Complex — the largest fire in Washington history at 256,108 acres — "
            "lightning ignited four fires near Carlton, Twisp, and Winthrop on July 14. Hot winds "
            "turned them into a firestorm on July 17 that raced 25 miles south to Pateros, "
            "destroying 353 homes. The fire approached Winthrop from multiple directions. The "
            "valley's fire ecology includes dry ponderosa pine/Douglas fir forests at lower "
            "elevations transitioning to dense mixed conifer at higher elevations, with extensive "
            "grass and shrub understory. Decades of fire suppression have created heavy fuel "
            "loading. The town's economy depends entirely on tourism and recreation, with summer "
            "population increasing 5-10x."
        ),
        "key_features": [
            {"name": "Methow River valley corridor", "bearing": "N-S", "type": "terrain", "notes": "50-mile fire corridor from Mazama to Pateros; channels wind and fire; 2014 Carlton Complex raced entire length in 3 days"},
            {"name": "Chewuch River valley", "bearing": "N", "type": "terrain", "notes": "North-trending valley with dense forest; fire approach from Pasayten Wilderness; Chewuch Road provides limited access to dispersed residences"},
            {"name": "North Cascades Highway (SR 20)", "bearing": "W", "type": "transport", "notes": "Sole westward route; CLOSED Nov-April; when open, provides access to Skagit Valley but crosses remote mountain terrain"},
            {"name": "Goat Peak / Sun Mountain area", "bearing": "W/SW", "type": "terrain", "notes": "Steep, south-facing slopes above town; Sun Mountain Lodge and resort community in extreme WUI position"},
            {"name": "Methow Valley floor (Carlton/Benson Creek)", "bearing": "S", "type": "terrain", "notes": "Open grassland and rangeland south of town; route of Carlton Complex fire spread; flashy fuels connect to Twisp"},
        ],
        "elevation_range_ft": [1700, 8500],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Carlton Complex", "year": 2014, "acres": 256108, "details": "Largest WA fire in recorded history; 4 lightning-caused fires merged July 17; destroyed 353 homes; $98M damage; firestorm raced 25 mi from Winthrop area to Pateros; hot winds (gusts 40+ mph) created 100+ ft flame lengths"},
            {"name": "Okanogan Complex", "year": 2015, "acres": 304782, "details": "Surpassed Carlton Complex acreage (but was multiple fires); 5 lightning-caused fires; forced evacuations of Twisp and Winthrop; included fatal Twisp River Fire"},
            {"name": "Cedar Creek/Cub Creek fires", "year": 2021, "acres": 8000, "details": "Forced Level 3 (GO NOW) evacuations in Methow Valley; demonstrated continued fire vulnerability; rapid response prevented structure loss"},
            {"name": "Crescent Mountain Fire", "year": 2018, "acres": 3600, "details": "Burned northwest of Winthrop; closed portions of SR 20; threatened Mazama community"},
        ],
        "evacuation_routes": [
            {"route": "SR 20 east to Okanogan/Omak", "direction": "E", "lanes": 2, "bottleneck": "2-lane highway through Loup Loup Pass (4,020 ft); winding mountain road with limited capacity; fire can close pass", "risk": "Route passes through fire-prone pine forest; 2015 Okanogan Complex threatened this route; only viable year-round eastern exit"},
            {"route": "SR 20 west to Skagit Valley (seasonal)", "direction": "W", "lanes": 2, "bottleneck": "CLOSED mid-November to mid-April; when open, remote mountain highway with no services for 75 miles; Washington/Rainy Pass at 5,477 ft", "risk": "Not available during shoulder fire season (Oct-Nov); closures for any reason eliminate western escape; extremely remote"},
            {"route": "SR 153 south through Twisp to Pateros", "direction": "S", "lanes": 2, "bottleneck": "Primary year-round route but passes directly through Twisp (another fire-vulnerable town) and down the Methow Valley fire corridor to Pateros (destroyed in 2014)", "risk": "EXTREME: During Carlton Complex, this entire corridor was simultaneously on fire; fleeing south meant driving toward the fire"},
            {"route": "Chewuch Road north", "direction": "N", "lanes": 2, "bottleneck": "Dead-end road into national forest; no through-route; leads to dispersed residences and campgrounds", "risk": "Becomes a trap; no exit; fire approach from any direction blocks retreat"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Valley-channeled winds from north or south at 15-30 mph; synoptic events produce dry east winds (foehn-type) descending Cascade eastern slopes at 30-50 mph; thermal belt effects create overnight warming and drying on mid-slope positions; convective column-generated winds during large fires exceed 50 mph",
            "critical_corridors": [
                "Methow Valley north-south axis — 50-mile fire corridor from Mazama to Pateros; Carlton Complex demonstrated full-length fire run",
                "Chewuch River drainage — north-south corridor; fire approach from Pasayten Wilderness",
                "Twisp River drainage — east-west corridor connecting to main valley; site of 2015 fatal fire",
                "Benson Creek / Carlton area — open grassland/sage south of Winthrop; flashy fuels connect town to valley fire runs"
            ],
            "rate_of_spread_potential": "EXTREME: Carlton Complex traveled 25 miles in one burning period (July 17, 2014); crown fire in dense conifer at 2-4 mph; grass/sage at valley floor at 5-8 mph; terrain-driven runs on steep slopes can exceed 5 mph; fire whirls documented during Carlton Complex",
            "spotting_distance": "2-5 miles documented during Carlton Complex; convective column lofted embers across ridges; cross-valley spotting ignited fires on opposite slopes simultaneously; ember showers reported in Winthrop during 2014 and 2015 fires"
        },
        "infrastructure_vulnerabilities": {
            "water_system": "Town of Winthrop water from wells and Methow River; limited storage capacity; fire demand can exceed system capacity for extended operations; rural properties on individual wells lose water if power fails",
            "power": "Okanogan County PUD; extensive above-ground lines through forested terrain; Carlton Complex destroyed miles of power infrastructure; weeks-long outages common during major fires; limited backup generation",
            "communications": "Cell coverage limited to valley floor (single AT&T/Verizon tower); fire can destroy repeater sites on mountain peaks; 2014 Carlton Complex caused communication blackouts; satellite phones needed for backcountry; Methow Valley News serves as community information hub",
            "medical": "Aero Methow Rescue (volunteer EMS); nearest hospital is Mid-Valley Hospital in Omak (55 mi east) or Central Washington Hospital in Wenatchee (95 mi south); medical helicopter operations impossible during active fire/smoke; 911 response times exceed 20 min for rural areas"
        },
        "demographics_risk_factors": {
            "population": 504,
            "seasonal_variation": "EXTREME: Summer population increases 5-10x to 3,000-5,000; vacation rentals, campgrounds, and Sun Mountain Lodge bring tourists unfamiliar with fire risk; winter population drops with SR 20 closure; wildfire season (July-Sept) coincides exactly with peak tourism",
            "elderly_percentage": "~25% over 65; significant retiree/second-home population; remote rural properties with long driveways and limited mobility",
            "mobile_homes": "Scattered manufactured housing in valley; some without defensible space; older units with combustible materials; rural sites with limited road access",
            "special_needs_facilities": "No hospital; limited medical facilities; elderly residents in remote properties; seasonal visitors with no local knowledge; backcountry recreationists (hikers, campers) difficult to notify and evacuate"
        }
    },

    # =========================================================================
    # 6. TWISP, WA — 2015 Twisp River Fire (3 LODD)
    # =========================================================================
    "twisp_wa": {
        "center": [48.3635, -120.1223],
        "terrain_notes": (
            "Twisp (pop 992) sits at the confluence of the Twisp River and Methow River in the "
            "heart of the Methow Valley at 1,903 ft elevation. The town occupies a narrow bench "
            "where the Twisp River valley opens into the main Methow Valley — a geography that "
            "creates a wind funnel effect as winds channeling down the Twisp River drainage "
            "accelerate into the broader valley. This exact configuration contributed to the "
            "August 19, 2015 tragedy: the Twisp River Fire started when tree branches struck a "
            "powerline in the Twisp River corridor, and strong shifting winds drove walls of "
            "flames and smoke onto a team of USFS firefighters attempting initial attack. "
            "Firefighters Richard Wheeler, Andrew Zajac, and Tom Zbyszewski were killed when "
            "their engine crashed in zero-visibility smoke on a winding dirt road. A fourth "
            "firefighter, Daniel Lyon, survived with 60-65% third-degree burns after exiting "
            "the vehicle and running through flames. The fire grew to 11,922 acres and reached "
            "the outskirts of Twisp within hours. The town is flanked by steep, forested slopes "
            "rising 3,000-5,000 ft above the valley floor on both east and west sides. The "
            "Twisp River valley extends west into the Okanogan-Wenatchee National Forest with "
            "dense mixed conifer under heavy fuel loading from fire suppression. TwispWorks "
            "(former ranger station campus) serves as a community hub. The town has the character "
            "of an arts community with historic downtown, but its geographic position in a "
            "narrow valley convergence zone makes it one of the most fire-vulnerable towns in "
            "the state."
        ),
        "key_features": [
            {"name": "Twisp River valley", "bearing": "W", "type": "terrain", "notes": "Narrow valley extending west into national forest; wind funnel effect at valley mouth; site of 2015 fatal fire; dense conifer with heavy fuel loading"},
            {"name": "Methow River main valley", "bearing": "N-S", "type": "terrain", "notes": "Main valley axis; fire corridor connecting Winthrop (7 mi N) to Pateros (30 mi S); Carlton Complex fire path"},
            {"name": "Twisp Butte / eastern slopes", "bearing": "E", "type": "terrain", "notes": "Steep slopes rising above town; south/west-facing aspects with dry grass and scattered pine; fire can race uphill and crown over into town"},
            {"name": "Balky Hill / western slopes", "bearing": "W", "type": "terrain", "notes": "Forested slopes above town; fire approach from Twisp River drainage drops into town; 2015 fire reached these slopes"},
            {"name": "TwispWorks campus / downtown", "bearing": "center", "type": "urban", "notes": "Former USFS ranger station converted to community campus; historic downtown with wood-frame structures; limited fire breaks"},
        ],
        "elevation_range_ft": [1750, 6500],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Twisp River Fire", "year": 2015, "acres": 11922, "details": "LODD: Richard Wheeler, Andrew Zajac, Tom Zbyszewski killed Aug 19; started from powerline contact; shifting winds trapped firefighter engine in zero visibility; Daniel Lyon survived with 60-65% burns; fire reached Twisp outskirts within hours; part of Okanogan Complex"},
            {"name": "Carlton Complex", "year": 2014, "acres": 256108, "details": "Fires ignited near Twisp and burned south; town threatened from multiple directions; evacuations ordered; 353 homes destroyed across complex; fire behavior exceeded all predictions"},
            {"name": "Okanogan Complex (broader)", "year": 2015, "acres": 304782, "details": "Twisp River Fire was component of larger complex; 5 fires burning simultaneously; forced evacuations of Twisp and surrounding areas; worst fire season in WA history"},
            {"name": "Cub Creek Fire", "year": 2021, "acres": 2000, "details": "Level 3 evacuations in Twisp River area; rapid response prevented structure loss; demonstrated persistent vulnerability of Twisp River corridor"},
        ],
        "evacuation_routes": [
            {"route": "SR 153 south to Pateros / US 97", "direction": "S", "lanes": 2, "bottleneck": "Primary route but 30 miles through narrow Methow Valley to Pateros; single 2-lane road; fire can close valley simultaneously", "risk": "During Carlton Complex (2014), this entire valley was on fire; route passes through burned area; Pateros was destroyed at the end of this road"},
            {"route": "SR 20 north to Winthrop, then east to Okanogan", "direction": "N/E", "lanes": 2, "bottleneck": "Must pass through Winthrop (7 mi) then over Loup Loup Pass; 2-lane mountain roads; Winthrop itself may be threatened", "risk": "Route through another fire-vulnerable town; Loup Loup Pass in fire-prone forest; 2015 Okanogan Complex threatened this route"},
            {"route": "Twisp River Road west", "direction": "W", "lanes": 2, "bottleneck": "DEAD END into national forest; narrow winding road; becomes a trap; SITE OF 2015 FIREFIGHTER FATALITIES", "risk": "EXTREME: This is the exact road where 3 firefighters died attempting to flee the 2015 fire; no exit; DO NOT evacuate west"},
            {"route": "SR 20 west (seasonal) via Winthrop", "direction": "W", "lanes": 2, "bottleneck": "Must drive north to Winthrop first, then west; SR 20 closed Nov-April; adds 20+ miles and passes through fire zones", "risk": "Not available during shoulder season; extremely indirect route; dependent on Winthrop being accessible"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Twisp River valley creates a wind funnel effect at the confluence with Methow Valley; afternoon upvalley winds 15-25 mph; synoptic events produce erratic wind shifts as Twisp River drainage interacts with main valley flow; foehn-type east winds create extreme fire weather; the 2015 fatal fire was characterized by strong, shifting winds that changed direction without warning",
            "critical_corridors": [
                "Twisp River drainage — wind funnel at valley mouth; 2015 fatal fire spread through this corridor; dense forest fuels",
                "Methow Valley main axis — north-south fire corridor; connects Twisp to both Winthrop and Pateros fire zones",
                "Buttermilk Creek / eastern slopes — steep terrain above town; afternoon heating drives upslope fire toward ridgeline above residences",
                "Beaver Creek area — northwest approach through mixed forest/grassland; connects to broader Okanogan fire landscape"
            ],
            "rate_of_spread_potential": "Extreme: 2015 Twisp River Fire grew from ignition to 7,231 acres in 18 hours; wind-driven crown fire in Twisp River valley at 2-3 mph; fire reached town outskirts from 5+ miles up-valley in single burning period; valley convergence zone creates unpredictable wind shifts that can redirect fire toward town without warning",
            "spotting_distance": "1-3 miles; 2015 fire demonstrated long-range spotting from crown fire in Twisp River drainage; embers lofted by convergence-zone updrafts; cross-ridge spotting from Methow Valley fires into Twisp River drainage and vice versa"
        },
        "infrastructure_vulnerabilities": {
            "water_system": "Town of Twisp water from wells; limited storage capacity; rural properties on individual wells dependent on power for pumps; fire demand during simultaneous structure protection can exceed system capacity; no redundant supply",
            "power": "Okanogan County PUD; overhead lines through forested terrain were the CAUSE of the 2015 Twisp River Fire (tree-to-powerline contact); extensive line exposure to fire damage; week+ outages during major fires; limited backup generation in town",
            "communications": "Limited cell coverage (single tower area); 2015 fire caused communication failures during critical period; firefighters reported radio dead zones in Twisp River valley; no redundant communication paths; terrain blocks signals in side drainages",
            "medical": "No hospital in Twisp; Aero Methow Rescue (volunteer EMS); nearest hospital is Mid-Valley Hospital in Omak (40 mi east) or Three Rivers Hospital in Brewster (50 mi south); medical helicopter operations impossible during active fire/smoke; Port Field Airport (WS87) for fixed-wing only"
        },
        "demographics_risk_factors": {
            "population": 992,
            "seasonal_variation": "Summer tourism doubles population; arts festivals and outdoor recreation bring visitors; Methow Valley trail system draws hikers/bikers; winter ski tourism (Methow Valley Nordic ski area) brings more manageable numbers",
            "elderly_percentage": "~22% over 65; artist/retiree community character; rural properties with long access roads and limited mobility options",
            "mobile_homes": "Some manufactured housing on town edges; older units; limited defensible space; rural manufactured homes in Twisp River corridor in extreme risk zone",
            "special_needs_facilities": "No hospital; limited medical facilities; TwispWorks community campus serves as informal gathering point; Methow Valley School District facilities in Twisp; elderly and disabled residents in remote valley properties with single-road access"
        }
    },

    # =========================================================================
    # 7. PATEROS, WA — Destroyed by Carlton Complex 2014
    # =========================================================================
    "pateros_wa": {
        "center": [48.0514, -119.9030],
        "terrain_notes": (
            "Pateros (pop 593) is the smallest and perhaps most fire-devastated town in Washington "
            "State, located at the confluence of the Methow and Columbia Rivers at approximately "
            "900 ft elevation. The town was literally rebuilt in the 1960s when Wells Dam construction "
            "flooded the original commercial district, and then devastated again when the 2014 "
            "Carlton Complex destroyed 111 homes in and around town — representing roughly one-"
            "third of all housing in the community. The fire arrived on July 17, 2014, when hot "
            "winds propelled a firestorm 25 miles south from the Winthrop/Carlton area down the "
            "Methow Valley corridor, reaching Pateros at approximately 8 PM. The entire town was "
            "successfully evacuated with no casualties. Pateros is situated in a bowl where the "
            "Methow River meets the Columbia, surrounded by steep, barren hillsides covered in "
            "cheatgrass and sagebrush — some of the flashiest fuels in the state. The terrain "
            "creates a natural funnel: fire racing down the Methow Valley accelerates as the "
            "valley narrows approaching the Columbia, and wind corridors from both rivers converge "
            "at the town site. The community was still rebuilding infrastructure 5+ years after "
            "the fire, with a new well to improve water pressure and ongoing recovery efforts "
            "coordinated by the Okanogan County Long Term Recovery Group. SR 153 is the sole "
            "route north into the Methow Valley; US 97 runs north-south along the Columbia."
        ),
        "key_features": [
            {"name": "Methow River / Columbia River confluence", "bearing": "center", "type": "terrain", "notes": "Two river corridors converge at town; wind from both valleys meets here; fire funnel effect from Methow Valley corridor"},
            {"name": "Methow Valley corridor (north)", "bearing": "N", "type": "terrain", "notes": "50-mile fire corridor through which the Carlton Complex firestorm traveled 25 miles in one burning period to reach Pateros"},
            {"name": "Columbia River / Lake Pateros (Wells Dam pool)", "bearing": "E", "type": "water/terrain", "notes": "Columbia River impoundment provides water but surrounding hillsides are steep and covered in flashy fuels; Wells Dam 8 mi downstream"},
            {"name": "Chiliwist Valley", "bearing": "W", "type": "terrain", "notes": "Side valley west of Pateros; Carlton Complex burned homes and ranches in this drainage; fire approach vector from west"},
            {"name": "Alta Lake area", "bearing": "SW", "type": "terrain", "notes": "Recreational area southwest of town; multiple homes destroyed in 2014 fire; dispersed rural residences in high-fire-risk terrain"},
        ],
        "elevation_range_ft": [780, 3500],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Carlton Complex", "year": 2014, "acres": 256108, "details": "Firestorm reached Pateros July 17; destroyed 111 homes in and around town (~1/3 of housing stock); entire town evacuated successfully; fire arrived at 8 PM after 25-mile run; destroyed homes in Chiliwist Valley, Alta Lake, and within city limits; $98M total damage across complex"},
            {"name": "Okanogan Complex", "year": 2015, "acres": 304782, "details": "Threatened Pateros area again just one year after Carlton Complex; demonstrated that the rebuilt community faces the same fire exposure; evacuations ordered"},
        ],
        "evacuation_routes": [
            {"route": "US 97 south to Chelan/Wenatchee", "direction": "S", "lanes": 2, "bottleneck": "Primary evacuation route; 2-lane highway along Columbia River; passes through steep terrain for 30+ miles to Chelan", "risk": "Canyon road vulnerable to fire closure; Apple Acres Fire (2025) closed US 97 in this corridor; terrain amplifies fire spread along highway"},
            {"route": "US 97 north to Okanogan/Omak", "direction": "N", "lanes": 2, "bottleneck": "2-lane highway along Columbia/Okanogan Rivers; passes through fire-prone terrain", "risk": "Carlton Complex and Okanogan Complex fires threatened this route; leads to another fire-vulnerable area"},
            {"route": "SR 153 north into Methow Valley", "direction": "N", "lanes": 2, "bottleneck": "CLOSED during Carlton Complex; the fire was COMING FROM this direction; single 2-lane road up narrow Methow Valley", "risk": "EXTREME: During 2014 Carlton Complex, this road was the fire corridor itself; evacuating north meant driving INTO the firestorm; SR 153 and SR 20 were closed simultaneously"},
            {"route": "Wells Dam Road east", "direction": "E", "lanes": 2, "bottleneck": "Limited local road; crosses Wells Dam but restricted access; not a primary evacuation route", "risk": "Dam security restrictions may limit evacuation use; road not designed for mass traffic"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Methow Valley corridor funnels north winds directly into Pateros; Columbia River corridor provides east-west wind component; convergence of two wind corridors at town site creates accelerated and turbulent wind patterns; synoptic events produce 30-50 mph winds through valley",
            "critical_corridors": [
                "Methow Valley corridor — 50-mile fire runway from Winthrop/Carlton to Pateros; Carlton Complex firestorm traveled this route in hours",
                "Chiliwist Valley — western approach; fire burned homes in this side valley in 2014",
                "Columbia River corridor — wind channeling from east or south; steep barren hillsides above river carry fire rapidly",
                "Alta Lake drainage — southwestern approach through dispersed rural residences"
            ],
            "rate_of_spread_potential": "EXTREME: Carlton Complex documented 25-mile fire run in single burning period reaching Pateros; flashy cheatgrass/sage fuels on surrounding slopes carry fire at 5-10 mph; steep terrain above town creates uphill fire acceleration; rate of spread exceeded all predictive models in 2014",
            "spotting_distance": "2-5 miles during Carlton Complex; wind-driven embers crossed ridges and valleys; firebrands ignited spot fires well ahead of main fire front; entire town was threatened simultaneously from multiple directions"
        },
        "infrastructure_vulnerabilities": {
            "water_system": "SEVERELY IMPACTED by 2014 fire: water reservoirs and telemetry equipment damaged; new well constructed post-fire to improve water pressure; system rebuilt but remains small-community scale; simultaneous fire suppression demand can overwhelm capacity",
            "power": "Okanogan County PUD / Douglas County PUD; above-ground lines destroyed in 2014 fire; rebuilt but same exposure to future fires; town experienced weeks-long outage during Carlton Complex",
            "communications": "Cell service limited; 2014 fire destroyed communication infrastructure; rebuilt but single points of failure remain; rural areas around town have poor coverage; emergency notification dependent on cell/internet",
            "medical": "No medical facilities in Pateros; nearest hospital is Mid-Valley Hospital in Omak (30 mi north) or Three Rivers Hospital in Brewster (15 mi south); medical helicopter impossible during fire; 911 response times 15+ min"
        },
        "demographics_risk_factors": {
            "population": 593,
            "seasonal_variation": "Summer recreation increases population with Lake Pateros visitors and Methow Valley travelers; hydroplane races bring weekend visitors; agricultural season brings orchard workers",
            "elderly_percentage": "~20% over 65; small-town demographics with aging population; many residents who survived 2014 fire are aging in place",
            "mobile_homes": "Manufactured housing represents significant portion of rebuilt housing stock post-2014; some replacement homes are manufactured; limited defensible space on small lots",
            "special_needs_facilities": "No hospital or medical facility; no assisted living; elderly residents in rebuilt homes; community still dealing with fire-related PTSD and mental health impacts from 2014; Okanogan County Long Term Recovery Group continues to assist"
        }
    },

    # =========================================================================
    # 8. ENTIAT, WA — Entiat River valley, Mills Canyon Fire 2014
    # =========================================================================
    "entiat_wa": {
        "center": [47.6731, -120.2050],
        "terrain_notes": (
            "Entiat (pop 1,326) is a small city at the confluence of the Entiat and Columbia Rivers "
            "in Chelan County, situated between the eastern foothills of the Cascade Range, Lake "
            "Entiat (Columbia River impoundment), and the mouth of the Entiat River valley. The "
            "city sits at approximately 750 ft elevation on a narrow bench between the river and "
            "steep hillsides that rise sharply to the Entiat Mountains (4,000-6,000 ft) to the "
            "west and southwest. The Entiat River valley extends 50+ miles west into the Glacier "
            "Peak Wilderness, through progressively denser forest that provides continuous fuel "
            "from the wilderness boundary to the city. The valley has a documented history of "
            "catastrophic fire: the 1988 Dinkelmann Fire burned through Mills Canyon (3 miles up "
            "the Entiat Valley), and the area was replanted only to be burned again by the 2014 "
            "Mills Canyon Fire (22,571 acres). The combination of young replanted trees, "
            "flammable shrubs, and residual dead fuel from the 1988 fire created what fire "
            "managers described as 'a Molotov cocktail' of fuels. Highway 97A is the sole "
            "through-route along the Columbia River, and Entiat River Road provides the only "
            "access up the valley. The town's original commercial district was flooded by Rocky "
            "Reach Dam construction, and the rebuilt town has limited redundancy in its infrastructure."
        ),
        "key_features": [
            {"name": "Entiat River valley", "bearing": "W", "type": "terrain", "notes": "50+ mile fire corridor from Glacier Peak Wilderness to Columbia River; 1988 and 2014 fires demonstrate recurring fire runs down valley; dense forest transitions to grass/sage at town"},
            {"name": "Mills Canyon", "bearing": "W/SW", "type": "terrain", "notes": "3 miles up-valley; burned 1988 (Dinkelmann Fire) and 2014 (Mills Canyon Fire, 22,571 acres); reburn area with high fuel loading from dead replanted trees"},
            {"name": "Columbia River / Lake Entiat", "bearing": "E", "type": "water/terrain", "notes": "River provides some firebreak on east side but steep hillsides above lake carry fire; Rocky Reach Dam downstream"},
            {"name": "Entiat Mountains", "bearing": "W/SW", "type": "terrain", "notes": "Cascade foothills rising 4,000-6,000 ft; steep south-facing slopes with grass/sage at lower elevations transitioning to conifer"},
            {"name": "US 97A corridor", "bearing": "N-S", "type": "transport", "notes": "Sole through-highway along Columbia River; fire can close this route; passes through steep terrain between Wenatchee (18 mi south) and Chelan (25 mi north)"},
        ],
        "elevation_range_ft": [720, 6000],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Mills Canyon Fire", "year": 2014, "acres": 22571, "details": "Started from structure fire west of Columbia River July 8; burned through grass, sagebrush, and scattered timber; forced evacuations of Entiat area; reburn of 1988 Dinkelmann Fire area created extreme fire behavior in accumulated fuels"},
            {"name": "Dinkelmann Fire", "year": 1988, "acres": 6000, "details": "Burned Mills Canyon area; Forest Service replanted; young trees grew into dense fuel load that fed 2014 reburn — demonstrating 25-year fire cycle"},
            {"name": "Duncan Fire", "year": 2009, "acres": 1600, "details": "Burned south of Entiat along Columbia; grass/sage fire driven by winds; threatened structures along US 97A"},
        ],
        "evacuation_routes": [
            {"route": "US 97A south to Wenatchee", "direction": "S", "lanes": 2, "bottleneck": "Primary route; 18 miles along Columbia River to Wenatchee; 2-lane highway with limited passing", "risk": "Route passes through fire-prone terrain along river; steep hillsides above road can carry fire across highway; smoke visibility issues"},
            {"route": "US 97A north to Chelan", "direction": "N", "lanes": 2, "bottleneck": "25 miles to Chelan; 2-lane highway; passes through similar terrain vulnerability", "risk": "Leads to another fire-vulnerable community; terrain similar to southbound route; both directions may be simultaneously threatened"},
            {"route": "Entiat River Road west (up-valley)", "direction": "W", "lanes": 2, "bottleneck": "DEAD END into national forest; narrow road; no through-route; becomes a trap", "risk": "Leads deeper into fire zone; Mills Canyon Fire originated from this direction; road passes through reburn area; absolutely not an evacuation route — it's a trap"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Entiat Valley creates a natural wind funnel connecting Cascade foothills to Columbia River corridor; afternoon upvalley winds bring fire toward town from forest interface; Columbia River gap winds from east during pressure gradient events; nocturnal downvalley drainage flows push fire toward Columbia and town",
            "critical_corridors": [
                "Entiat River valley — 50-mile fire corridor from wilderness to town; 1988 and 2014 fires burned down this valley",
                "Mills Canyon reburn area — accumulated fuels from two fire cycles create extreme fire behavior potential",
                "US 97A Columbia corridor — fire can approach from north or south along river; steep hillsides carry fire across highway",
                "Mad River drainage — parallel valley to the south; fire can cross ridges between drainages"
            ],
            "rate_of_spread_potential": "High to extreme: Mills Canyon Fire grew from ignition to 5,000 acres overnight; reburn fuels (dead young trees + shrubs + residual logs) create extreme fire behavior; grass/sage transition zone at valley mouth carries fire at 3-6 mph; upvalley wind events can push crown fire down-valley toward town",
            "spotting_distance": "1-2 miles in mixed fuels; bark and ember transport from ponderosa pine and Douglas fir; valley terrain channels embers toward Columbia corridor; reburn fuel structure creates intense convection columns that loft embers"
        },
        "infrastructure_vulnerabilities": {
            "water_system": "City of Entiat water system; town was rebuilt after dam construction flooded original district; system is modern but small-capacity; fire suppression demand during major incident can stress supply; rural properties up-valley on individual wells",
            "power": "Chelan County PUD; above-ground distribution lines through fire-prone terrain; 2014 fire caused outages; lines along Entiat River Road particularly vulnerable; limited backup generation",
            "communications": "Limited cell coverage especially up-valley; single cell tower serves town; fire can damage repeater sites; rural areas along Entiat River Road have poor coverage; emergency notification system dependent on cell connectivity",
            "medical": "No hospital in Entiat; nearest is Central Washington Hospital in Wenatchee (18 mi south); Cascade Medical Center in Leavenworth (25 mi west — requires mountain road); medical helicopter limited by smoke; new fire station built post-2014 for improved local response"
        },
        "demographics_risk_factors": {
            "population": 1326,
            "seasonal_variation": "Summer recreation (Entiat River fishing, camping) increases population; orchard season brings agricultural workers; Lake Entiat boating activity; 100% rural census designation",
            "elderly_percentage": "~18% over 65; small-town demographics; aging agricultural community",
            "mobile_homes": "Manufactured housing in town and along Entiat River Road; older units in fire-prone locations; limited defensible space on many properties",
            "special_needs_facilities": "No hospital; no assisted living; school facilities serve as community shelter; US Aluminum Castings workforce (largest employer) concentrated in single location; agricultural worker housing with limited fire notification"
        }
    },

    # =========================================================================
    # 9. CLE ELUM, WA — I-90 corridor, upper Kittitas Valley
    # =========================================================================
    "cle_elum_wa": {
        "center": [47.1954, -120.9383],
        "terrain_notes": (
            "Cle Elum (pop 2,078) sits at the western gateway of the Kittitas Valley where I-90 "
            "descends from Snoqualmie Pass into the upper Yakima River basin at 1,909 ft elevation. "
            "The city is flanked by dense conifer forest on three sides — the Cascade Range to the "
            "west, Teanaway drainage to the northeast, and Cle Elum Ridge to the south — creating "
            "a forested bowl with the town at its bottom. This is the transition zone between the "
            "wet western Cascades and the dry eastern slopes, producing a 'humidity cliff' where "
            "relative humidity can drop 30-40% in 10 miles during east wind events. Cle Elum is "
            "directly in the Snoqualmie Pass wind corridor, experiencing the same gap winds as "
            "Ellensburg (40-60+ mph) but with the added danger of dense forest fuels rather than "
            "grass. The 2012 Table Mountain Fire (near the Liberty/Swauk area north of town) "
            "forced evacuations and demonstrated vulnerability of the north approach. The 2017 "
            "Jolly Mountain Fire burned nearly 31,000 acres in the Teanaway drainage just "
            "northeast of town, forcing emergency evacuations and threatening the Cle Elum Lake "
            "watershed. Adjacent to Roslyn (1.5 miles west) and South Cle Elum, the combined "
            "communities share fire risk. The Suncadia Resort development west of town has pushed "
            "luxury WUI development into heavy forest. I-90 provides the primary evacuation "
            "corridor but can be overwhelmed by wind-driven fire crossing the interstate."
        ),
        "key_features": [
            {"name": "Snoqualmie Pass / I-90 corridor", "bearing": "W", "type": "transport/meteorological", "notes": "Primary evacuation route AND primary wind corridor; gap winds descend pass into town; fire can close I-90"},
            {"name": "Teanaway River drainage", "bearing": "NE", "type": "terrain", "notes": "Dense forest extending northeast; 2017 Jolly Mountain Fire burned 31,000 acres in this drainage; fire approach from NE through continuous conifer"},
            {"name": "Cle Elum Ridge / South side", "bearing": "S", "type": "terrain", "notes": "Forested ridge south of town; steep slopes; fire can run uphill and crown over into developed areas"},
            {"name": "Suncadia Resort / Roslyn interface", "bearing": "W", "type": "urban/WUI", "notes": "Luxury resort development pushed into heavy forest; Roslyn (100th percentile wildfire risk nationally) is 1.5 miles west; continuous forest connects both communities"},
            {"name": "Cle Elum Lake / dam", "bearing": "NW", "type": "water/infrastructure", "notes": "Bureau of Reclamation reservoir; watershed threatened by 2017 fire; dam infrastructure provides some firebreak but surrounding forest is dense"},
        ],
        "elevation_range_ft": [1900, 6500],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Jolly Mountain Fire", "year": 2017, "acres": 31000, "details": "Lightning-caused Aug 11 in Teanaway; grew to 31,000 acres over 3+ months; emergency evacuations of Cle Elum area; threatened Cle Elum Lake watershed; 15% contained at peak; overwhelmed local suppression capacity"},
            {"name": "Table Mountain / Liberty fires", "year": 2012, "acres": 2500, "details": "Wildfires in Swauk/Table Mountain area N of town; Level 1-3 evacuations; Liberty and surrounding communities evacuated; national forest closures east of SR 97"},
            {"name": "Taylor Bridge Fire", "year": 2012, "acres": 23500, "details": "Ignited on SR 10 east of Cle Elum; gap winds drove fire east; 61 homes destroyed in Kittitas Valley; demonstrated how quickly fire moves through this corridor"},
        ],
        "evacuation_routes": [
            {"route": "I-90 east to Ellensburg", "direction": "E", "lanes": 4, "bottleneck": "Best capacity; 4-lane interstate; 25 miles to Ellensburg through open valley", "risk": "Grass fire can cross I-90 in wind events; Taylor Bridge Fire demonstrated fire spread across the corridor; wind-driven smoke reduces visibility to near-zero"},
            {"route": "I-90 west over Snoqualmie Pass to Seattle", "direction": "W", "lanes": 4, "bottleneck": "4-lane interstate but climbs 1,100 ft to pass summit through dense forest; pass closures for fire, wind, or winter weather", "risk": "Heading INTO wind corridor during gap-wind events; dense forest on pass; wildfire closure of I-90 over pass would be catastrophic for all east-side communities"},
            {"route": "SR 903 north to Cle Elum Lake", "direction": "N", "lanes": 2, "bottleneck": "Dead-end road to lake/campgrounds; no through-route; leads into forest fire zone", "risk": "TRAP: leads deeper into forest; Jolly Mountain Fire threatened this area; no exit beyond lake; campground visitors can be trapped"},
            {"route": "SR 10 / local roads south through South Cle Elum", "direction": "S", "lanes": 2, "bottleneck": "Local roads with limited capacity; converge back to I-90 or valley roads", "risk": "Fire from south approaches through Cle Elum Ridge; limited alternative to I-90"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Snoqualmie Pass gap winds (identical mechanism to Ellensburg but with forest fuels): marine push events create 40-60+ mph westerly winds descending pass; east wind (foehn) events bring hot, dry downslope winds from east; transition-zone humidity gradient means fuels dry rapidly during east wind events",
            "critical_corridors": [
                "I-90 / Snoqualmie Pass corridor — wind-aligned fire runway through dense forest; gap winds push fire east at extreme rates",
                "Teanaway River drainage — 2017 Jolly Mountain Fire demonstrated this corridor; fire approach from NE through continuous conifer",
                "Cle Elum Ridge — south-facing slopes with afternoon solar heating; fire runs uphill toward ridgetop then crowns over",
                "Roslyn-Cle Elum forest interface — continuous dense forest between communities; fire in this zone threatens both towns simultaneously"
            ],
            "rate_of_spread_potential": "Extreme in dense conifer: crown fire at 1-3 mph; gap-wind-driven fire in forest can exceed 3 mph; Jolly Mountain Fire grew 4,000 acres in a single day; transition-zone fuels (dry grass understory + conifer overstory) create ladder fuel conditions that facilitate rapid crown fire initiation",
            "spotting_distance": "1-3 miles from crown fire; gap winds can transport embers across I-90 (200+ ft); Jolly Mountain Fire demonstrated long-range spotting into Teanaway drainage; dense conifer produces abundant firebrand material"
        },
        "infrastructure_vulnerabilities": {
            "water_system": "City of Cle Elum water from wells and Cle Elum River; Bureau of Reclamation infrastructure (Cle Elum Dam) provides watershed storage; fire threatening watershed could contaminate supply; hillside homes may have pressure issues during fire",
            "power": "Kittitas County PUD and Puget Sound Energy; major transmission lines cross Snoqualmie Pass through fire-prone forest; gap-wind events damage above-ground distribution; power loss triggers loss of individual well pumps in rural areas",
            "communications": "Cell coverage limited in surrounding valleys; towers on ridges in fire-prone locations; I-90 corridor has coverage but side drainages (Teanaway, Cle Elum Lake) have gaps; emergency notification for recreationists in national forest is limited",
            "medical": "No hospital in Cle Elum; nearest is Kittitas Valley Healthcare in Ellensburg (25 mi east) or hospitals in west-side communities via I-90 (80+ mi); medical helicopter operations limited by smoke and wind; Suncadia Resort has first-aid but no emergency care"
        },
        "demographics_risk_factors": {
            "population": 2078,
            "seasonal_variation": "Suncadia Resort and outdoor recreation dramatically increase summer/weekend population; I-90 corridor travelers use Cle Elum as rest/fuel stop; Cle Elum Lake campgrounds add seasonal population; winter ski traffic at Snoqualmie Pass creates year-round visitor patterns",
            "elderly_percentage": "~20% over 65; retirement community development (Suncadia); historic town character attracts retirees",
            "mobile_homes": "Manufactured housing in Cle Elum and South Cle Elum; older units from logging/mining era; some in flood-prone and fire-prone locations",
            "special_needs_facilities": "No hospital; no assisted living in city; Suncadia Resort guests may include mobility-limited visitors; campground visitors with no local knowledge; South Cle Elum has separate jurisdiction complicating unified evacuation"
        }
    },

    # =========================================================================
    # 10. MANSON, WA — Lake Chelan north shore, single road access
    # =========================================================================
    "manson_wa": {
        "center": [47.8853, -120.1583],
        "terrain_notes": (
            "Manson (pop 1,523) is an unincorporated agricultural community on the north shore of "
            "Lake Chelan, approximately 7 miles northwest of the city of Chelan. The community is "
            "built on bench terraces between the lakeshore (elev ~1,100 ft) and steep, forested "
            "hillsides rising to 4,000-5,000 ft above. Manson is designated as an 'at-risk "
            "community of catastrophic wildfire' in its Community Wildfire Protection Plan, and "
            "its most critical vulnerability is ACCESS: there is essentially a single road (SR 150 / "
            "Manson Highway) providing the only way in or out, connecting to Chelan 7 miles "
            "southeast along the lakeshore. This single-road access means that a fire between "
            "Manson and Chelan would trap the entire community with no vehicular escape route. "
            "The surrounding terrain is covered in dry grass, sagebrush, and scattered ponderosa "
            "pine on south-facing slopes, transitioning to mixed conifer forest at higher elevations. "
            "The community economy is based on orchards (apples, cherries, grapes/wine) and tourism, "
            "with significant agricultural worker populations in seasonal housing. Wapato Point "
            "Resort and other lakeside developments add tourist population during summer. "
            "The hillsides above Manson received fire during the 2015 Chelan Complex season, and "
            "the community has experienced multiple evacuation scares."
        ),
        "key_features": [
            {"name": "SR 150 / Manson Highway (sole access road)", "bearing": "SE", "type": "transport", "notes": "CRITICAL: Only road connecting Manson to Chelan and the highway network; fire on this 7-mile corridor traps entire community; shut down during past fires"},
            {"name": "Lake Chelan north shore", "bearing": "S", "type": "water/terrain", "notes": "Lake provides potential boat evacuation but limited capacity; steep terrain above lakeshore carries fire; north-shore developments in WUI zone"},
            {"name": "Manson hillsides (north/west)", "bearing": "N/W", "type": "terrain", "notes": "Steep slopes with grass/sage transitioning to conifer; south/east-facing aspects maximize solar heating; fire runs uphill above town"},
            {"name": "Wapato Point Resort / waterfront developments", "bearing": "S/SE", "type": "urban", "notes": "Tourist resort complex on lake; adds summer population; evacuation dependent on SR 150"},
            {"name": "Orchard benchlands", "bearing": "W/NW", "type": "agricultural", "notes": "Apple and cherry orchards provide some fuel break but irrigated only during growing season; dormant orchard vegetation can burn; worker housing in orchard areas"},
        ],
        "elevation_range_ft": [1079, 5000],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Chelan Complex (Manson threats)", "year": 2015, "acres": 95000, "details": "Complex of fires on south end of Lake Chelan; SR 150 between Chelan and Manson shut down; Manson threatened; community evacuations considered; smoke impacts severe"},
            {"name": "Pioneer Fire", "year": 2024, "acres": 1500, "details": "Fire on north shore of Lake Chelan prompted Level 3 (GO NOW) evacuation orders for areas north of Manson; SR 150 threatened; demonstrated single-road vulnerability"},
            {"name": "Manson grassland fires", "year": 2024, "acres": 7, "details": "Small 7-acre fire prompted immediate Level 3 evacuation due to proximity to structures and single evacuation route; shows how even small fires trigger emergency response in single-access community"},
        ],
        "evacuation_routes": [
            {"route": "SR 150 southeast to Chelan", "direction": "SE", "lanes": 2, "bottleneck": "THE ONLY VEHICULAR EXIT: 7-mile 2-lane road along lakeshore to Chelan; fire between Manson and Chelan traps entire community; has been closed during fires", "risk": "EXTREME: Single point of failure; road passes through fire-prone terrain; closure means NO vehicular evacuation possible; CWPP identifies this as the community's primary vulnerability"},
            {"route": "Lake Chelan boat evacuation", "direction": "S/SE", "lanes": 0, "bottleneck": "Limited marina capacity; no organized boat evacuation plan; weather/wave conditions variable; smoke reduces visibility", "risk": "Not a reliable mass evacuation option; dependent on boat availability; no nighttime capability; cannot evacuate mobility-limited residents by boat"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Lake-valley diurnal circulation: afternoon upslope winds drive fire toward ridgetops; lake breeze effects create variable wind at shoreline; synoptic events channel winds along lake axis (NW-SE); gap winds from Cascade passes reach Lake Chelan basin",
            "critical_corridors": [
                "SR 150 corridor — fire along this 7-mile route cuts off the ONLY evacuation route for the entire community",
                "North-shore hillsides — steep grass/sage slopes above lakeside developments; fire runs uphill above Manson toward ridgeline",
                "Roses Lake / Grade Creek area — fire approach from north/west through forested terrain above orchards",
                "Lake Chelan south shore fire interaction — fires on opposite shore (2015 Complex) can spot across narrow lake sections"
            ],
            "rate_of_spread_potential": "High to extreme: grass/sage on hillsides carries fire at 3-5 mph; even small fires (7-acre 2024 incident) prompt Level 3 evacuations due to single-road vulnerability; steepness of terrain above town accelerates uphill spread; transition to conifer at higher elevation enables crown fire",
            "spotting_distance": "0.5-1.5 miles in grass/sage with wind; cross-lake spotting possible in extreme events (lake narrows to <1 mile at points); upslope terrain enhances lofting"
        },
        "infrastructure_vulnerabilities": {
            "water_system": "Community water system from wells and lake intake; agricultural irrigation demand in summer competes with fire suppression; system designed for residential/agricultural use, not mass fire suppression; limited hydrant coverage in rural orchard areas",
            "power": "Chelan County PUD; above-ground distribution lines along SR 150 vulnerable to fire; power loss would affect well pumps and emergency communications; limited backup generation",
            "communications": "Cell coverage limited on north shore; single tower area; terrain blocks signals in valleys above Manson; emergency notification must reach agricultural workers (language barriers) and tourists; SR 150 closure isolates community from cell towers in Chelan",
            "medical": "No medical facility in Manson; dependent on Lake Chelan Community Hospital in Chelan (7 mi via fire-vulnerable SR 150); medical helicopter operations limited by terrain and smoke; ambulance service from Chelan; if SR 150 is closed, NO medical access"
        },
        "demographics_risk_factors": {
            "population": 1523,
            "seasonal_variation": "Summer tourism at Wapato Point Resort and lakeside rentals doubles population; orchard season brings agricultural workers (significant Spanish-speaking population); 4th of July / summer weekends peak; seasonal residents may not know evacuation procedures",
            "elderly_percentage": "~18% over 65; retirement community element; lakeside homes with elderly residents; limited mobility options during evacuation",
            "mobile_homes": "Agricultural worker housing includes manufactured homes and temporary structures; some orchard housing in fire-prone hillside areas; limited defensible space",
            "special_needs_facilities": "No medical facility; no assisted living; agricultural worker housing with language barriers; Wapato Point Resort guests unfamiliar with local conditions; boat-dependent waterfront properties may resist vehicular evacuation"
        }
    },

    # =========================================================================
    # 11. ROSLYN, WA — Former coal town surrounded by forest
    # =========================================================================
    "roslyn_wa": {
        "center": [47.2235, -120.9931],
        "terrain_notes": (
            "Roslyn (pop 984) is a former coal mining town at 2,247 ft elevation in the Cascade "
            "Mountains of Kittitas County, about 80 miles east of Seattle and 1.5 miles west of "
            "Cle Elum. Founded in 1886 when Northern Pacific Railway prospectors found coal veins, "
            "the town reached a peak population of 4,000 during its mining heyday and produced "
            "over 50 million tons of coal before the last mine closed in 1963. Today Roslyn is "
            "famous as the filming location for the TV show 'Northern Exposure' and for its "
            "historic downtown listed on the National Register. The town ranks in the 100th "
            "percentile of wildfire risk to homes in Washington State and the 99th percentile "
            "nationally, according to the U.S. Forest Service. Roslyn is COMPLETELY SURROUNDED "
            "by dense forest: the city acquired a 300-acre 'Urban Forest' in 2004, and thousands "
            "of additional acres of Okanogan-Wenatchee National Forest and private timberland "
            "encircle the community. The forest consists of dense stands of Douglas fir, ponderosa "
            "pine, and grand fir with heavy dead fuel loads from decades of fire suppression and "
            "insect mortality. Nearby Ronald (a small community 1 mile west) was destroyed by fire "
            "in 1928 — an event that nearly spread to Roslyn and was only stopped by 2,000 "
            "volunteers and a fortuitous wind shift. The community has become a national model "
            "for community-led wildfire management through controlled burns and fuel reduction in "
            "the Urban Forest, but the surrounding landscape remains a continuous forest fuel bed."
        ),
        "key_features": [
            {"name": "Roslyn Urban Forest (300 acres)", "bearing": "surrounding", "type": "terrain/fuel", "notes": "City-owned forest encircling town; active fuel reduction program (controlled burns, thinning); serves as buffer but also fire approach vector if treatments lapse"},
            {"name": "Okanogan-Wenatchee National Forest", "bearing": "W/N/S", "type": "terrain", "notes": "Dense conifer forest on all sides; heavy dead fuel loads from fire suppression and beetle kill; continuous fuel from wilderness to town"},
            {"name": "Ronald / western approach", "bearing": "W", "type": "urban", "notes": "Small community 1 mile west; destroyed by fire in 1928; fire nearly spread to Roslyn; corridor between Ronald and Roslyn remains forested"},
            {"name": "Suncadia Resort development", "bearing": "E/SE", "type": "urban/WUI", "notes": "Luxury resort between Roslyn and Cle Elum; pushed development into forest; connected by continuous forest fuel"},
            {"name": "Coal Creek drainage", "bearing": "N", "type": "terrain", "notes": "Historic mining area with legacy coal seam exposure; drainage provides fire approach from north through dense forest"},
        ],
        "elevation_range_ft": [2100, 5500],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Ronald Fire", "year": 1928, "acres": 500, "details": "Fire devastated neighboring Ronald (1 mi west) on Aug 18, destroying 32 houses and businesses; spread into forest threatening Roslyn; 2,000 miners, railroaders, and citizens fought fire; wind abatement saved Roslyn"},
            {"name": "Jolly Mountain Fire (nearby)", "year": 2017, "acres": 31000, "details": "Burned in Teanaway drainage NE of Cle Elum; threatened broader area; demonstrated massive fire potential in forests surrounding Roslyn/Cle Elum; emergency evacuations"},
            {"name": "Taylor Bridge Fire (nearby)", "year": 2012, "acres": 23500, "details": "Burned east in Kittitas Valley; demonstrated wind-driven fire behavior in the Snoqualmie Pass corridor that includes Roslyn"},
        ],
        "evacuation_routes": [
            {"route": "SR 903 east to Cle Elum, then I-90", "direction": "E", "lanes": 2, "bottleneck": "1.5 miles to Cle Elum; then access I-90; route passes through Suncadia Resort development in forest", "risk": "Short but forested corridor between towns; fire in Suncadia/Roslyn forest interface blocks this primary route; converges at Cle Elum with all other evacuees"},
            {"route": "SR 903 west through Ronald", "direction": "W", "lanes": 2, "bottleneck": "Passes through Ronald; continues to dead end at Cle Elum Lake; NO THROUGH ROUTE", "risk": "TRAP: Road leads to Cle Elum Lake with no exit; forest surrounds entire route; Ronald burned in 1928 on this corridor; not a viable evacuation"},
            {"route": "Local roads south", "direction": "S", "lanes": 2, "bottleneck": "Limited local roads converge back to SR 903 and I-90 through Cle Elum; no independent southern exit", "risk": "All routes funnel through Cle Elum; forest surrounds all roads; no alternative to SR 903"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Snoqualmie Pass gap winds descend through Cle Elum area at 30-50+ mph; Roslyn's valley position creates sheltering from worst gap winds but also traps smoke and embers; nocturnal drainage winds from surrounding ridges; east wind (foehn) events bring hot, dry air that rapidly lowers fuel moisture in surrounding dense forest",
            "critical_corridors": [
                "Roslyn-Cle Elum forest corridor — continuous dense conifer between towns; fire here blocks the ONLY evacuation route",
                "Coal Creek drainage north — fire approach from national forest through dense fuel directly to town",
                "Ronald-Roslyn corridor — 1928 fire path; forest has regrown between communities",
                "Suncadia development interface — luxury WUI development in continuous forest connecting to both Roslyn and Cle Elum"
            ],
            "rate_of_spread_potential": "High to extreme in dense conifer: crown fire at 1-3 mph; heavy dead fuel loads from fire suppression create ladder fuels; Urban Forest fuel reduction has reduced immediate risk around town but surrounding untreated forest remains at extreme potential; gap-wind events can turn moderate fire into crown fire rapidly",
            "spotting_distance": "1-3 miles in dense conifer with gap winds; Douglas fir bark produces prolific firebrands; surrounding terrain creates funnel effects for ember transport; Roslyn's valley position may create ember catch basin during wind events"
        },
        "infrastructure_vulnerabilities": {
            "water_system": "City of Roslyn water from Coal Creek watershed; limited storage; fire threatening watershed could contaminate supply; historic mining-era infrastructure; hydrant coverage limited in older neighborhoods; simultaneous fire suppression and domestic demand stresses system",
            "power": "Kittitas County PUD / Puget Sound Energy; above-ground lines through dense forest extremely vulnerable; wind events regularly damage lines; power loss affects well pumps throughout area; limited backup generation; restored historic buildings often have outdated electrical",
            "communications": "Limited cell coverage in valley; terrain blocks signals; single tower serves area; radio repeaters on surrounding ridges in fire-prone locations; historic downtown lacks modern communication infrastructure; fire-related communication failures documented in surrounding area during 2017 Jolly Mountain Fire",
            "medical": "No medical facility in Roslyn; nearest hospital is Kittitas Valley Healthcare in Ellensburg (30 mi east); medical access requires transit through Cle Elum; forest fire blocking SR 903 eliminates medical access entirely; volunteer fire department; limited EMS"
        },
        "demographics_risk_factors": {
            "population": 984,
            "seasonal_variation": "Tourism increases summer population (Northern Exposure filming location, outdoor recreation, Suncadia Resort visitors); weekend/holiday peaks; winter has some ski-related tourism from nearby Snoqualmie Pass",
            "elderly_percentage": "~22% over 65; retirement/artist community character; historic homes with elderly residents; limited mobility in some neighborhoods",
            "mobile_homes": "Some manufactured housing from mining era; older units; limited defensible space in densely treed lots; many historic homes with wood siding and roofing in close proximity to forest",
            "special_needs_facilities": "No hospital; no assisted living; historic town character means narrow streets and older buildings; volunteer fire department with limited capacity for mass evacuation; combined Roslyn/Cle Elum/South Cle Elum evacuation would overwhelm single I-90 corridor"
        }
    },

    # =========================================================================
    # 12. OMAK/OKANOGAN, WA — 2015 Okanogan Complex, most fire-prone area
    # =========================================================================
    "omak_okanogan_wa": {
        "center": [48.4118, -119.5268],
        "terrain_notes": (
            "Omak (pop 4,845) and Okanogan (pop 2,379) are twin cities on the Okanogan River in "
            "Okanogan County — the most fire-prone county in Washington State. Located at "
            "approximately 843 ft elevation in a broad river valley, the cities are the commercial "
            "and governmental hub of Okanogan County (the largest county in WA at 5,315 sq mi). "
            "The Okanogan River valley runs north-south with sagebrush-covered benches and "
            "terraces rising to pine-forested hills on both sides. The Colville Indian Reservation "
            "borders Omak to the east, with its vast open grasslands and timber. Omak Creek enters "
            "from the east, providing a fire corridor from the reservation lands. The 2015 "
            "Okanogan Complex — the largest fire event in WA history by acreage at 304,782 acres — "
            "was composed of five lightning-caused fires that burned across the landscape surrounding "
            "these communities, forcing evacuations and killing three firefighters on the Twisp "
            "River Fire component. The 2014 Carlton Complex also threatened the broader Okanogan "
            "area, burning to the hills around Brewster (20 mi south). The area experiences hot, "
            "dry summers with temperatures regularly exceeding 100F, single-digit humidity, and "
            "frequent dry lightning storms that ignite multiple fires simultaneously. Okanogan "
            "County had the 2014 AND 2015 record-setting fires, plus the Twisp River Fire "
            "fatalities — making it ground zero for Washington wildfire risk. The county's large "
            "area, sparse population, and limited firefighting resources mean fires can grow "
            "unchecked for hours before significant suppression response arrives."
        ),
        "key_features": [
            {"name": "Okanogan River valley", "bearing": "N-S", "type": "terrain", "notes": "Broad valley with river providing some firebreak; sagebrush benches and terraces on both sides; wind corridor; US 97 runs through valley"},
            {"name": "Colville Indian Reservation", "bearing": "E", "type": "terrain", "notes": "Vast open grasslands and timber east of Omak; Omak Creek provides fire corridor from reservation; limited fire suppression resources on reservation lands"},
            {"name": "Conconully / Salmon Creek drainage", "bearing": "NW", "type": "terrain", "notes": "Valley extending northwest to Conconully; 2015 Okanogan Complex fires originated near Conconully; forested terrain with limited road access"},
            {"name": "Omak Lake / eastern benchlands", "bearing": "E/SE", "type": "terrain", "notes": "Arid benchlands east of town; Omak Lake (tribal land); vast grass and sagebrush with scattered pine; fire can approach from east across open terrain"},
            {"name": "US 97 / downtown corridor", "bearing": "N-S", "type": "transport/urban", "notes": "Primary highway through both cities; commercial strip development; evacuation route and fire exposure simultaneously"},
        ],
        "elevation_range_ft": [780, 6774],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Okanogan Complex", "year": 2015, "acres": 304782, "details": "5 lightning-caused fires (Twisp River, Lime Belt, Beaver Lake, Blue Lake, Tunk Block); largest fire event in WA history by acreage; forced evacuations of Conconully, Twisp, Winthrop; 3 firefighters killed (Twisp River Fire component); 1,250+ firefighters deployed"},
            {"name": "Carlton Complex (area impacts)", "year": 2014, "acres": 256108, "details": "Burned to hills around Brewster (20 mi south of Omak); threatened Malott on Okanogan River; fire approached from Methow Valley; demonstrated vulnerability of entire Okanogan River corridor"},
            {"name": "Tunk Block Fire (component)", "year": 2015, "acres": 55000, "details": "Component of Okanogan Complex that burned closest to Omak; threatened communities north and east of city; burned through tribal lands and private ranch lands"},
            {"name": "Cold Springs Fire", "year": 2020, "acres": 189388, "details": "Burned east of Omak on Colville Reservation; one of largest fires in state that year; killed child; demonstrated continued extreme fire risk from reservation grasslands approaching Omak from east"},
        ],
        "evacuation_routes": [
            {"route": "US 97 south to Brewster/Chelan/Wenatchee", "direction": "S", "lanes": 2, "bottleneck": "Primary route south; 2-lane highway along Okanogan River; passes through Malott, Brewster — both threatened by 2014 Carlton Complex", "risk": "Route through fire-prone river corridor; Carlton Complex burned to Brewster; 80+ miles to Wenatchee through fire-vulnerable terrain"},
            {"route": "US 97 north to Canadian border", "direction": "N", "lanes": 2, "bottleneck": "2-lane highway north through Oroville to Canadian border; passes through fire-prone terrain", "risk": "International border crossing complications; fire can close highway; Oroville area has experienced fires"},
            {"route": "SR 20 west to Methow Valley / North Cascades", "direction": "W", "lanes": 2, "bottleneck": "2-lane mountain road over Loup Loup Pass (4,020 ft); closed by fire during 2015 Okanogan Complex; seasonal closures on North Cascades Highway beyond Winthrop", "risk": "Route through heavily forested terrain; passes through Twisp/Winthrop fire zone; Loup Loup Pass fire closure documented; SR 20 beyond Winthrop closed Nov-April"},
            {"route": "SR 155 south to Coulee Dam / Grand Coulee", "direction": "S/SE", "lanes": 2, "bottleneck": "2-lane highway through Colville Reservation; passes through Nespelem; limited capacity", "risk": "Route through reservation grasslands — 2020 Cold Springs Fire burned 189,000 acres in this area; limited infrastructure along route"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": "Okanogan Valley north-south channeling of synoptic winds; thermal convection creates strong afternoon upvalley winds; dry lightning storms are primary ignition source (2014 and 2015 fires both lightning-caused); east winds from Columbia Plateau bring extreme heat and low humidity; foehn-type winds from Cascades occasional but devastating",
            "critical_corridors": [
                "Okanogan River valley (N-S) — wind corridor connecting communities; fire can travel valley length",
                "Omak Creek drainage (E) — corridor from Colville Reservation grasslands into east side of Omak; Cold Springs Fire approach vector",
                "Salmon Creek / Conconully drainage (NW) — forested corridor; 2015 Okanogan Complex origin area",
                "Tunk Creek / north benchlands — 2015 Tunk Block Fire corridor; fire approaches from north through grass/sage"
            ],
            "rate_of_spread_potential": "EXTREME across multiple fuel types: grass/sage at 5-10+ mph during wind events; timber at 2-4 mph with crown fire; Okanogan Complex demonstrated multiple simultaneous fire runs of 10,000+ acres in single burning periods; dry lightning ignites dozens of starts simultaneously, overwhelming initial attack; area can have 50+ new ignitions in a single storm",
            "spotting_distance": "2-5 miles documented during Okanogan Complex; convective columns from large fires create their own weather; embers cross ridges and valleys; simultaneous spotting in multiple drainages; fires can merge across 10+ mile gaps through spotting alone"
        },
        "infrastructure_vulnerabilities": {
            "water_system": "Omak city water from wells and Okanogan River; adequate for normal use but mass fire suppression in WUI strains capacity; rural areas on individual wells lose water with power failure; tribal lands have separate water systems with varying capacity; Okanogan city water system is separate and smaller",
            "power": "Okanogan County PUD; extensive above-ground distribution across the county's 5,315 sq mi; fires regularly destroy miles of lines; weeks-long outages in rural areas documented during 2014 and 2015 fires; limited backup generation; cost of hardening lines across largest county in WA is prohibitive",
            "communications": "Okanogan County Emergency Management system; cell coverage limited outside of Omak/Okanogan valley; vast county area means many residents unreachable by cell; tribal communication systems separate; repeater sites on mountaintops vulnerable to fire; 2015 fires caused communication failures across county",
            "medical": "Mid-Valley Hospital in Omak (25-bed critical access); the only hospital serving a 5,315 sq mi county; nearest additional hospital is Wenatchee (95 mi south) or Spokane (175 mi east); medical helicopter operations regularly impossible due to smoke; EMS response times exceed 30 minutes for rural calls; tribal health facilities at Nespelem supplement"
        },
        "demographics_risk_factors": {
            "population": 9224,  # Omak 4,845 + Okanogan 2,379 + surrounding areas
            "seasonal_variation": "Omak Stampede (rodeo, Aug) brings thousands; summer recreation on Okanogan River; hunting season (Oct-Nov) brings visitors to rural areas; Colville Reservation events; agricultural season (orchards, ranching) adds workers",
            "elderly_percentage": "~20% over 65; rural aging population; tribal elders on reservation; limited mobility options for rural elderly",
            "mobile_homes": "Significant manufactured housing stock throughout county; older units; many on tribal lands; limited defensible space; some in isolated locations with single-road access; highest percentage of manufactured homes in any WA county",
            "special_needs_facilities": "Mid-Valley Hospital (only hospital in county); tribal health center at Nespelem; limited assisted living; 14.4% of county residents below poverty level; tribal populations with unique emergency management needs; vast rural population (county avg 8 people/sq mi) difficult to notify and evacuate"
        }
    },
}


# =============================================================================
# Utility: summary statistics
# =============================================================================
def print_summary():
    """Print summary statistics for all profiled cities."""
    total_pop = sum(
        p["demographics_risk_factors"]["population"]
        for p in PNW_WASHINGTON_ENHANCED.values()
    )
    print(f"Washington Enhanced Profiles: {len(PNW_WASHINGTON_ENHANCED)} cities")
    print(f"Total population at risk: {total_pop:,}")
    print()
    for key, profile in PNW_WASHINGTON_ENHANCED.items():
        pop = profile["demographics_risk_factors"]["population"]
        wui = profile["wui_exposure"]
        n_fires = len(profile["historical_fires"])
        n_routes = len(profile["evacuation_routes"])
        print(
            f"  {key:20s}  pop={pop:>6,}  WUI={wui:8s}  "
            f"fires={n_fires}  evac_routes={n_routes}"
        )
    print()
    # Total historical fire acreage (unique fires only, avoid double-counting)
    fire_names_seen = set()
    total_acres = 0
    for profile in PNW_WASHINGTON_ENHANCED.values():
        for fire in profile["historical_fires"]:
            fire_key = (fire["name"], fire["year"])
            if fire_key not in fire_names_seen:
                fire_names_seen.add(fire_key)
                total_acres += fire.get("acres", 0)
    print(f"Unique historical fires tracked: {len(fire_names_seen)}")
    print(f"Total historical fire acreage (unique): {total_acres:,}")


if __name__ == "__main__":
    print_summary()
