"""
Oregon Fire-Vulnerable City Profiles — Research-Paper Quality
=============================================================

Enhanced profiles for 6 existing cities and 8 new fire-vulnerable towns.
Incorporates real fire history, evacuation constraints, demographics,
infrastructure vulnerabilities, and fire-spread characteristics.

Key context:
- September 8, 2020 "Labor Day Fires" was the worst day in Oregon fire history
- Five simultaneous megafires with extreme east winds (gusts 50-60 mph, 100+ mph
  at ridgetops) driven by an anomalous offshore pressure gradient
- Beachie Creek, Holiday Farm, Almeda, Riverside, and Archie Creek all blew up
  simultaneously, burning over 1 million acres across Oregon in 72 hours
- Detroit and Gates were effectively erased (80%+ structures destroyed)
- Almeda Fire was an unprecedented urban interface event — 9-mile corridor of
  destruction through Bear Creek Valley, 2,800+ structures, 3 fatalities
- Holiday Farm Fire destroyed Blue River and Vida/Nimrod communities along
  the McKenzie River corridor

Data sources: USFS, ODF, InciWeb, NOAA, US Census, Oregon State Fire Marshal,
              DOGAMI, peer-reviewed literature (Abatzoglou et al. 2021, Mass &
              Ovens 2021), local CWPP documents
"""

PNW_OREGON_ENHANCED = {

    # =========================================================================
    # 1. BEND, OR — Cascade Edge WUI, Central Oregon's Largest City
    # =========================================================================
    "bend_or": {
        "center": [44.0582, -121.3153],
        "terrain_notes": (
            "Bend sits at 3,623 ft on the eastern flank of the Cascade Range, straddling "
            "the Deschutes River where high-desert juniper/sagebrush transitions to ponderosa "
            "pine and mixed conifer. The western city boundary directly abuts Deschutes National "
            "Forest, creating one of Oregon's most extensive wildland-urban interface zones. "
            "Skyline Forest (3,700 acres of ponderosa pine) borders the northwest city limits "
            "and burned in the 2014 Two Bulls Fire. Tumalo Creek and the Deschutes River "
            "corridors funnel winds from the Cascades into residential areas. The west side "
            "neighborhoods (Century West, Summit West, Shevlin) are built into continuous "
            "forest with heavy fuel loading. Lava rock terrain and volcanic soils create "
            "irregular topography with pockets of dense fuel that complicate fire suppression. "
            "The city has grown rapidly from ~20K (1990) to ~107K (2024), with much of the "
            "growth pushing into forested WUI zones on the west and south sides."
        ),
        "key_features": [
            {"name": "Deschutes River Canyon", "bearing": "N-S through city", "type": "river_corridor",
             "notes": "Major fuel corridor bisecting city; riparian vegetation creates continuous fuel"},
            {"name": "Skyline Forest / Shevlin Park", "bearing": "NW", "type": "forest_interface",
             "notes": "3,700-acre ponderosa forest directly adjoining city; Two Bulls Fire 2014 burned through this area"},
            {"name": "Tumalo Creek Corridor", "bearing": "W", "type": "drainage_corridor",
             "notes": "Funnels downslope winds from Cascades into residential areas; dense riparian fuels"},
            {"name": "Phil's Trailhead / West Bend WUI", "bearing": "W-SW", "type": "recreation_wui",
             "notes": "Heavy recreation use area where forest meets dense housing developments"},
            {"name": "Century Drive / Mt. Bachelor Corridor", "bearing": "SW", "type": "evacuation_corridor",
             "notes": "Single road to Mt. Bachelor resort; corridor through continuous national forest"},
            {"name": "Pilot Butte", "bearing": "E", "type": "landmark",
             "notes": "Cinder cone (4,138 ft) providing panoramic fire-spotting vantage; eastern city boundary"},
        ],
        "elevation_range_ft": [3400, 4200],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Awbrey Hall Fire", "year": 1990, "acres": 3349,
             "details": "Arson-caused fire on August 4; destroyed 22 homes, evacuated 2,800 residents in 12 hours. "
                        "Led directly to Oregon SB 360 (1997) Forestland-Urban Interface Fire Protection Act. "
                        "Burned through ponderosa pine on west side of Bend."},
            {"name": "Two Bulls Fire", "year": 2014, "acres": 6900,
             "details": "Burned through Skyline Forest NW of city; human-caused. No structures lost but forced "
                        "hundreds of evacuations, threatened water supply from Tumalo Creek, degraded air quality. "
                        "Demonstrated vulnerability of west-side WUI."},
            {"name": "Darlene 3 Fire", "year": 2024, "acres": 3900,
             "details": "Burned in Deschutes NF ~30 miles south near La Pine; over 1,000 homes on evacuation "
                        "alert. Demonstrated ongoing regional fire risk."},
            {"name": "Bachelor Complex (Little Lava Fire)", "year": 2024, "acres": 2500,
             "details": "Threatened Sunriver and SW Bend; Level 2 evacuations for Deschutes River communities "
                        "along South Century Drive."},
        ],
        "evacuation_routes": [
            {"route": "US-97 (Bend Parkway)", "direction": "N-S", "lanes": 4,
             "bottleneck": "Interchanges at Revere Ave, Colorado Ave become gridlocked in peak traffic",
             "risk": "Primary N-S corridor; if fire approaches from west, eastward evacuation funnels all traffic to US-97"},
            {"route": "US-20 (Greenwood Ave)", "direction": "E-W", "lanes": 2,
             "bottleneck": "Two-lane highway east of Bend; limited capacity for mass evacuation",
             "risk": "Only east-west route north of city; passes through high-fire-risk juniper terrain"},
            {"route": "Century Drive (OR-372)", "direction": "SW", "lanes": 2,
             "bottleneck": "Single two-lane road through continuous national forest to Mt. Bachelor",
             "risk": "Dead-end corridor; 15,000+ recreation visitors on peak days with no alternative egress"},
            {"route": "OR-97 South (toward La Pine)", "direction": "S", "lanes": 2,
             "bottleneck": "Two-lane highway through ponderosa pine forest; Sunriver and La Pine also evacuating",
             "risk": "Shared corridor with 25,000+ residents and visitors to the south; cascading evacuation failure risk"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "East/northeast winds during offshore (east wind) events drive fires from Cascades into city. "
                "Afternoon SW thermal winds in summer push fires upslope toward west-side neighborhoods. "
                "Diurnal wind shift creates complex fire behavior at WUI boundary."
            ),
            "critical_corridors": [
                "Tumalo Creek drainage — funnels wind and fire from Cascades directly into west Bend",
                "Deschutes River canyon — N-S fire spread corridor through heart of city",
                "Skyline Forest / Shevlin Park — continuous canopy connecting national forest to city",
                "Century Drive corridor — fire can race along highway corridor from Mt. Bachelor area",
            ],
            "rate_of_spread_potential": (
                "High in ponderosa pine / juniper: 50-150 chains/hr under wind-driven conditions. "
                "2014 Two Bulls Fire grew from ignition to 6,000+ acres in 48 hours. "
                "Awbrey Hall Fire burned 3,350 acres in 12 hours with residential involvement."
            ),
            "spotting_distance": (
                "0.5-1.5 miles in ponderosa pine; bark and ember transport from canopy fires "
                "readily ignites shake/wood roofs in older west-side neighborhoods. "
                "Volcanic terrain creates updrafts enhancing spotting distance."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "City water sourced from Bridge Creek and Tumalo Creek; both intakes in forested "
                "watersheds vulnerable to fire contamination. Two Bulls Fire (2014) directly "
                "threatened Tumalo Creek water supply. Post-fire debris flows can compromise "
                "water quality for months."
            ),
            "power": (
                "Pacific Power distribution; overhead lines through forested corridors on west side. "
                "Central Electric Cooperative serves rural areas. Fire-related outages common; "
                "2020 east wind event caused cascading power failures across Central Oregon."
            ),
            "communications": (
                "Cell towers on Awbrey Butte and Pilot Butte; west-side towers in fire-prone "
                "forest. Deschutes 911 center serves entire county. Emergency alert system "
                "tested regularly but coverage gaps exist in canyon areas."
            ),
            "medical": (
                "St. Charles Bend Medical Center — 261 beds, Level II Trauma Center, largest "
                "hospital between Salem and Boise. Only regional hospital for 100+ mile radius; "
                "surge capacity limited during mass-casualty wildfire events."
            ),
        },
        "demographics_risk_factors": {
            "population": 106926,
            "seasonal_variation": (
                "Tourism doubles effective population in summer; 3+ million annual visitors to "
                "Mt. Bachelor, Deschutes River, and Cascade Lakes. Peak fire season coincides "
                "with peak tourism season (July-September)."
            ),
            "elderly_percentage": "~16% over 65",
            "mobile_homes": (
                "Several mobile home parks along US-97 corridor and in south Bend; "
                "approximately 5-7% of housing stock is manufactured homes."
            ),
            "special_needs_facilities": (
                "Multiple assisted living facilities on west side near WUI; Bend Senior Center; "
                "several group care homes in forested neighborhoods requiring evacuation assistance."
            ),
        },
    },

    # =========================================================================
    # 2. MEDFORD / ASHLAND, OR — Rogue Valley, Almeda Fire Corridor
    # =========================================================================
    "medford_ashland_or": {
        "center": [42.3265, -122.8756],
        "terrain_notes": (
            "Medford (1,382 ft) and Ashland (1,949 ft) anchor the Rogue Valley / Bear Creek "
            "Valley in southern Oregon, a 100+ square-mile alluvial basin bounded by the "
            "Siskiyou Mountains to the south, Cascade foothills to the east, and Rogue River "
            "canyon to the north. The Bear Creek corridor (I-5 / OR-99 alignment) is the "
            "primary urban-wildland interface — the 2020 Almeda Fire proved this corridor "
            "can carry fire 9 miles through continuous urban development. Ashland sits in "
            "a narrowing valley at the base of the Siskiyous with steep, forested slopes "
            "rising immediately above the city. Medford occupies the broader valley floor "
            "with irrigated agriculture and orchards (cherry, pear) creating seasonal fuel "
            "variability. The Bear Creek Greenway provides a continuous riparian fuel corridor "
            "connecting all communities from Ashland through Talent, Phoenix, and into Medford."
        ),
        "key_features": [
            {"name": "Bear Creek Greenway", "bearing": "N-S corridor", "type": "riparian_corridor",
             "notes": "26-mile paved path along Bear Creek; riparian vegetation created continuous fuel for Almeda Fire's 9-mile run"},
            {"name": "Ashland Watershed / Siskiyou Slopes", "bearing": "S of Ashland", "type": "steep_terrain",
             "notes": "Steep forested slopes rising 3,000+ ft above city; Ashland Creek drainage feeds directly into downtown"},
            {"name": "Table Rock", "bearing": "N of Medford", "type": "volcanic_mesa",
             "notes": "Prominent volcanic plateau; grassland fire risk in surrounding plains"},
            {"name": "Rogue River / Gold Hill Corridor", "bearing": "NW", "type": "river_canyon",
             "notes": "Deep river canyon with thermal wind effects; fire can race through canyon terrain"},
            {"name": "I-5 / OR-99 Transportation Corridor", "bearing": "N-S", "type": "infrastructure",
             "notes": "Interstate and parallel highway through Bear Creek Valley; Almeda Fire crossed and paralleled both"},
            {"name": "Emigrant Lake", "bearing": "SE of Ashland", "type": "reservoir",
             "notes": "Irrigation reservoir surrounded by grass and oak savanna; seasonal drawdown exposes dry fuel"},
        ],
        "elevation_range_ft": [1300, 2200],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Almeda Fire", "year": 2020, "acres": 3200,
             "details": "September 8 Labor Day fire; human-caused, started in field near Almeda Dr in Ashland. "
                        "Wind-driven (40+ mph gusts from south) 9-mile run through Bear Creek corridor. "
                        "Destroyed 2,800+ structures (including ~1,600 manufactured homes in 18 mobile home "
                        "parks), killed 3 people. Most destructive wildfire in Oregon recorded history. "
                        "Primarily urban interface fire — burned through Talent, Phoenix, and into south Medford."},
            {"name": "Angora Fire (South Ashland)", "year": 2009, "acres": 100,
             "details": "Burned on steep slopes above Ashland; demonstrated vulnerability of Siskiyou foothill interface."},
        ],
        "evacuation_routes": [
            {"route": "I-5", "direction": "N-S", "lanes": 4,
             "bottleneck": "Siskiyou Pass (S) and Sexton Mtn (N) are steep, winding segments with truck slowdowns",
             "risk": "Only interstate through valley; Almeda Fire paralleled I-5 for 9 miles, fire crossed highway at multiple points"},
            {"route": "OR-99 (Pacific Highway)", "direction": "N-S", "lanes": 2,
             "bottleneck": "Parallel to I-5 through Bear Creek Valley; passes directly through fire-destroyed areas",
             "risk": "Alternative to I-5 but passes through same fire corridor; 2020 fire closed both simultaneously"},
            {"route": "OR-66 (Green Springs Hwy)", "direction": "E from Ashland", "lanes": 2,
             "bottleneck": "Winding mountain road over Green Springs summit (4,551 ft); very limited capacity",
             "risk": "Only eastern escape from Ashland; climbs through dense forest with extreme fire risk"},
            {"route": "OR-62 (Crater Lake Hwy)", "direction": "NE from Medford", "lanes": 2,
             "bottleneck": "Traffic backs up at White City / Agate Desert during evacuations",
             "risk": "Route passes through mixed forest/grassland; brush fire risk in Table Rock area"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Rogue Valley channeling effect amplifies wind through the Bear Creek corridor. "
                "During 2020 Almeda Fire, anomalous strong southerly winds (40+ mph) pushed fire "
                "northward through corridor. Normal summer pattern is afternoon NW winds with "
                "thermal upvalley flow. Critical fire weather occurs with offshore (east) events "
                "or strong pressure-gradient winds from the south."
            ),
            "critical_corridors": [
                "Bear Creek riparian corridor — continuous fuel from Ashland to Medford (9+ miles)",
                "I-5 / OR-99 highway margins — grass, brush, and homeless camp fuel accumulation",
                "Ashland Creek drainage — steep, forested canyon directly above downtown Ashland",
                "Griffin Creek / Wagner Creek drainages — fire pathways from wildlands into developed areas",
            ],
            "rate_of_spread_potential": (
                "Almeda Fire demonstrated urban-corridor spread of ~2 mph sustained through "
                "mixed residential/commercial/riparian fuel. In grasslands on valley floor, "
                "rates of 100-300 chains/hr possible. Slope-driven fires on Siskiyou foothills "
                "above Ashland can achieve 50-100 chains/hr upslope."
            ),
            "spotting_distance": (
                "0.25-0.5 miles in Bear Creek corridor; ember transport from structure fires "
                "and riparian vegetation. Almeda Fire spot fires ignited across I-5. "
                "On Siskiyou slopes, 1-2 mile spotting possible from crown fires in mixed conifer."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Medford: Duff Water Treatment Plant on Big Butte Creek pipeline. "
                "Ashland: Ashland Creek watershed (forested, fire-vulnerable). "
                "TAP (Talent-Ashland-Phoenix) water system serves 23,000 people; Almeda Fire "
                "damaged water infrastructure, contaminated lines with benzene from melted "
                "plastic service laterals. Boil-water advisories lasted weeks post-fire."
            ),
            "power": (
                "Pacific Power serves valley; overhead distribution through fire-prone corridors. "
                "Almeda Fire destroyed numerous transformers and poles along Bear Creek. "
                "Power restoration took weeks in destroyed areas."
            ),
            "communications": (
                "Jackson County Emergency alert system had significant gaps during Almeda Fire — "
                "many residents in Talent and Phoenix never received evacuation notices. "
                "Language barriers (large Spanish-speaking population) compounded alert failures."
            ),
            "medical": (
                "Asante Rogue Regional Medical Center (378 beds, Level II Trauma) in Medford; "
                "Providence Medford Medical Center (120 beds). Serves 600,000+ people across "
                "9 counties in southern Oregon and northern California. Surge capacity concern "
                "during regional fire events."
            ),
        },
        "demographics_risk_factors": {
            "population": 113000,
            "seasonal_variation": (
                "Oregon Shakespeare Festival brings 400,000+ visitors to Ashland annually "
                "(Feb-Nov). Summer tourism peaks coincide with fire season. Agricultural "
                "workers (seasonal) increase valley population during harvest."
            ),
            "elderly_percentage": "~18% over 65 (higher in Ashland ~22%)",
            "mobile_homes": (
                "Critical vulnerability: Almeda Fire destroyed ~1,600 manufactured homes in "
                "18 mobile home parks. 65% of homes lost were in mobile home parks. "
                "Many parks housed predominantly Latino families. Pre-fire, ~15% of Talent "
                "and Phoenix housing was manufactured homes."
            ),
            "special_needs_facilities": (
                "Multiple assisted living facilities in Medford; Ashland has retirement "
                "communities. Rogue Valley Manor (continuing care). Spanish-speaking population "
                "in Talent/Phoenix had limited access to English-only emergency alerts."
            ),
        },
    },

    # =========================================================================
    # 3. SISTERS, OR — Cascade Foothills, Ponderosa Pine WUI
    # =========================================================================
    "sisters_or": {
        "center": [44.2910, -121.5494],
        "terrain_notes": (
            "Sisters (3,187 ft) sits at the eastern base of the Cascade Range where "
            "ponderosa pine forest meets high-desert juniper woodland. The town is surrounded "
            "by Deschutes National Forest on three sides (west, north, south). Named for "
            "the Three Sisters volcanic peaks visible to the west, the community occupies "
            "a narrow band of development along the US-20/OR-126 corridor. The landscape "
            "is dominated by fire-adapted ponderosa pine with significant standing dead "
            "timber from bark beetle kill. Whychus Creek (formerly Squaw Creek) runs south "
            "of town through a forested canyon. Black Butte (6,436 ft) rises prominently "
            "to the northwest. Nearly 20 large fires have threatened the greater Sisters "
            "area since 1994, making it one of Oregon's most fire-threatened communities. "
            "In 2025, Sisters passed a wildfire code for new development — one of the first "
            "in Oregon."
        ),
        "key_features": [
            {"name": "Three Sisters Wilderness", "bearing": "W", "type": "wilderness",
             "notes": "242,000-acre wilderness; source of major fires including B&B Complex. No suppression until fire threatens boundary."},
            {"name": "Black Butte", "bearing": "NW", "type": "volcanic_peak",
             "notes": "6,436 ft cinder cone; fire lookout tower. Pine forests on slopes are continuous fuel to town."},
            {"name": "Whychus Creek Canyon", "bearing": "S of town", "type": "drainage_corridor",
             "notes": "Forested canyon corridor that could channel fire and wind toward town from the southwest"},
            {"name": "Indian Ford Meadow / Sage Steppe", "bearing": "E-NE", "type": "grassland_transition",
             "notes": "Transition zone to high desert; grass fires can spread rapidly and ignite adjacent pine stands"},
            {"name": "Camp Sherman / Metolius Basin", "bearing": "NW (10 mi)", "type": "forest_community",
             "notes": "Nearby community in dense forest; shares fire district and evacuation infrastructure"},
            {"name": "McKenzie Pass (OR-242)", "bearing": "W", "type": "mountain_pass",
             "notes": "Seasonal road through lava fields and dense forest; closed Oct-June. Emergency egress only in summer."},
        ],
        "elevation_range_ft": [3100, 3400],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "B&B Complex Fire", "year": 2003, "acres": 90769,
             "details": "Linked pair of lightning-caused fires in central Cascades west of Sisters. "
                        "Burned 90,769 acres Aug-Sep 2003, destroyed 13 structures, cost $38.7M to suppress. "
                        "Eastern side burned through ponderosa and lodgepole pine. Camp Sherman evacuated (~300 people). "
                        "Changed national perception of fire management in Pacific Northwest."},
            {"name": "Black Crater Fire", "year": 2006, "acres": 9300,
             "details": "Burned west of Sisters near Black Crater. Threatened Sisters and Camp Sherman. "
                        "Demonstrated ongoing risk from Cascade fires approaching town."},
            {"name": "Green Ridge Fire", "year": 2020, "acres": 1000,
             "details": "During Labor Day wind event; forced evacuation notices for Camp Sherman area. "
                        "Grew rapidly in east winds before weather moderated."},
            {"name": "Link Fire", "year": 2003, "acres": 400,
             "details": "Small fire near Sisters demonstrating ignition potential in local ponderosa stands."},
        ],
        "evacuation_routes": [
            {"route": "US-20 East (toward Bend)", "direction": "E", "lanes": 2,
             "bottleneck": "Two-lane highway; 20 miles to Bend through forested corridor",
             "risk": "Primary evacuation route; shared with Camp Sherman evacuees. Fire can cut this route."},
            {"route": "US-20/OR-22 West (Santiam Pass)", "direction": "W", "lanes": 2,
             "bottleneck": "Mountain pass (4,817 ft); winter closures. Winding through dense forest.",
             "risk": "Passes through burn scars and heavy forest; B&B Complex fire threatened this corridor."},
            {"route": "OR-126 South (toward Redmond)", "direction": "SE", "lanes": 2,
             "bottleneck": "Shared corridor with US-20 through Sisters then diverges south",
             "risk": "Only connects after reaching US-20; does not provide independent evacuation route from town center."},
            {"route": "OR-242 (McKenzie Pass)", "direction": "W", "lanes": 2,
             "bottleneck": "Seasonal road, closed October-June. Very narrow, winding, no shoulders.",
             "risk": "Summer-only escape route through lava fields and dense forest; not viable for mass evacuation."},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Dominant summer afternoon SW winds push fires from Cascades toward town. "
                "During east wind events (like September 2020), fires in Cascade forests can "
                "be pushed rapidly westward, but town is more protected from east-origin fires. "
                "Thermal belt effects on surrounding buttes create complex local wind patterns."
            ),
            "critical_corridors": [
                "Cascades-to-town corridor via Whychus Creek — channeled wind and continuous forest fuel",
                "Black Butte / Green Ridge approach from NW — dense ponderosa connects wildlands to town",
                "Indian Ford corridor from NE — grass fire transition to pine interface",
                "US-20 highway corridor — fire can travel along road margins through continuous forest",
            ],
            "rate_of_spread_potential": (
                "In ponderosa pine stands with grass understory: 30-80 chains/hr surface fire, "
                "200+ chains/hr with wind-driven crown runs. B&B Complex demonstrated multi-day "
                "runs of 5,000+ acres/day in extreme conditions. Bark beetle-killed stands "
                "dramatically increase crown fire potential."
            ),
            "spotting_distance": (
                "1-2 miles in ponderosa pine crown fires; extensive ember production from "
                "bark and cone material. Shake and wood-sided structures in town center "
                "highly vulnerable to ember ignition."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "City water from 4 wells with 1.6 million gallon reservoir; approximately "
                "32 miles of distribution mains and 1,500 active connections. Well-based "
                "system requires electrical power for pumping; extended power outages "
                "compromise water supply and fire suppression capacity."
            ),
            "power": (
                "Central Electric Cooperative; overhead distribution lines through forested "
                "corridors. Power outages during fire events common. No local generation backup."
            ),
            "communications": (
                "Deschutes County 911 dispatch. Cell coverage adequate in town but degrades "
                "rapidly in surrounding forest. Sisters-Camp Sherman Fire District covers "
                "large rural area with limited stations."
            ),
            "medical": (
                "No hospital in Sisters; nearest is St. Charles Bend (22 miles east). "
                "Sisters has one small medical clinic. Fire evacuation medical needs must "
                "route to Bend or Redmond. Air ambulance dependent on smokefree conditions."
            ),
        },
        "demographics_risk_factors": {
            "population": 3738,
            "seasonal_variation": (
                "Tourism and events (Sisters Outdoor Quilt Show, rodeo, music festivals) can "
                "triple effective population on peak weekends. Vacation rentals and summer "
                "homes add ~2,000 seasonal residents. Camp Sherman adds ~300 permanent / "
                "500 seasonal residents to the fire district."
            ),
            "elderly_percentage": "~25% over 65 (retirement destination)",
            "mobile_homes": (
                "Limited manufactured housing within city limits; more common in "
                "surrounding unincorporated Deschutes County areas."
            ),
            "special_needs_facilities": (
                "Sisters Senior Living; limited assisted-care capacity. Remote location "
                "means extended EMS response times to Bend hospitals."
            ),
        },
    },

    # =========================================================================
    # 4. LA PINE, OR — Embedded in Deschutes National Forest
    # =========================================================================
    "la_pine_or": {
        "center": [43.6801, -121.5039],
        "terrain_notes": (
            "La Pine (4,236 ft) is a small city literally embedded within Deschutes National "
            "Forest, approximately 30 miles south of Bend along US-97. The community is a "
            "loose collection of homes and businesses strung along the highway corridor, "
            "surrounded on all sides by lodgepole and ponderosa pine forest. The Little "
            "Deschutes River and Fall River run through the area, creating riparian corridors "
            "in otherwise continuous coniferous forest. Much of the surrounding forest has "
            "heavy fuel loading from decades of fire suppression and bark beetle mortality. "
            "The greater La Pine area (~20,000 residents in unincorporated Deschutes County) "
            "sprawls through forest with no clear urban boundary — homes are scattered among "
            "trees on large lots with minimal defensible space. Volcanic pumice soils support "
            "lodgepole pine monocultures highly susceptible to stand-replacing fire."
        ),
        "key_features": [
            {"name": "Deschutes National Forest", "bearing": "All directions", "type": "national_forest",
             "notes": "1.6 million acre forest completely surrounds community; continuous canopy fuel"},
            {"name": "Newberry Volcanic Monument", "bearing": "E", "type": "volcanic_terrain",
             "notes": "Paulina Peak (7,985 ft) and volcanic terrain east of town; unique fire behavior in lava flows"},
            {"name": "Little Deschutes River", "bearing": "E of US-97", "type": "riparian_corridor",
             "notes": "Meandering river with grass meadows and riparian vegetation creating fire corridor"},
            {"name": "La Pine State Park", "bearing": "N", "type": "recreation",
             "notes": "Popular campground in forest; seasonal visitors in fire-prone setting"},
            {"name": "Wickiup Reservoir / Crane Prairie", "bearing": "W", "type": "reservoir",
             "notes": "Irrigation reservoirs in forested area; recreation areas with limited egress"},
            {"name": "US-97 Corridor", "bearing": "N-S", "type": "highway",
             "notes": "Primary transportation artery; fire can close highway isolating community"},
        ],
        "elevation_range_ft": [4100, 4500],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Darlene 3 Fire", "year": 2024, "acres": 3900,
             "details": "Exploded to life in Deschutes NF just outside La Pine; over 1,100 buildings "
                        "threatened, 1,000+ homes on evacuation alert. Governor declared emergency conflagration."},
            {"name": "Jackpine Fire", "year": 2024, "acres": 50,
             "details": "Fire on Masten Road led to Level 2 evacuations and 4-mile closure of US-97 south "
                        "of La Pine. Demonstrated how quickly fire can threaten highway lifeline."},
            {"name": "McKay Butte Fire", "year": 2024, "acres": 190,
             "details": "Grew from 90 to 190 acres overnight east of La Pine in lodgepole pine."},
            {"name": "Davis Fire", "year": 2003, "acres": 21000,
             "details": "Large fire in Deschutes NF south of La Pine; demonstrated scale of potential fire events."},
        ],
        "evacuation_routes": [
            {"route": "US-97 North (toward Bend)", "direction": "N", "lanes": 2,
             "bottleneck": "Two-lane highway through continuous forest for 30 miles to Bend; shared with Sunriver evacuees",
             "risk": "Primary escape route; 2024 Jackpine Fire closed 4-mile segment. Fire on either side traps corridor."},
            {"route": "US-97 South (toward Chemult/Klamath)", "direction": "S", "lanes": 2,
             "bottleneck": "Remote two-lane highway through lodgepole forest; 70 miles to Klamath Falls",
             "risk": "Long drive through heavy forest with no services; fire can close multiple segments simultaneously."},
            {"route": "County Roads East (Newberry area)", "direction": "E", "lanes": 2,
             "bottleneck": "Narrow rural roads through forest; dead ends at volcanic terrain",
             "risk": "Not viable evacuation routes; lead deeper into forest and volcanic landscape."},
            {"route": "Forest Roads West (Cascade Lakes)", "direction": "W", "lanes": 2,
             "bottleneck": "Seasonal, unpaved forest roads; not suitable for mass evacuation",
             "risk": "Dead-end roads to reservoirs and trailheads; could become fire traps."},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Afternoon SW thermal winds in summer drive fire from Cascade slopes toward "
                "community. East wind events push fire rapidly across flat lodgepole terrain. "
                "Diurnal drainage flows from Newberry Crater create nighttime wind shifts. "
                "Relatively flat terrain allows fire to spread in any wind direction."
            ),
            "critical_corridors": [
                "US-97 highway corridor — fire can race along road margins through continuous forest",
                "Little Deschutes River — riparian and grass fuel corridor through developed areas",
                "Lodgepole pine flats — uniform fuel allows unimpeded fire spread across landscape",
                "Fall River corridor — drainage connects Cascade highlands to community",
            ],
            "rate_of_spread_potential": (
                "In lodgepole pine with grass understory: 40-100 chains/hr surface fire, "
                "crown fire runs of 200-400 chains/hr possible in bark beetle-killed stands. "
                "Darlene 3 Fire grew explosively to 3,900 acres. Flat terrain with uniform fuel "
                "allows sustained high-rate spread with minimal terrain friction."
            ),
            "spotting_distance": (
                "0.5-1 mile in lodgepole pine; less spotting than ponderosa due to smaller bark "
                "plates, but crown fire ember showers can ignite multiple spots simultaneously. "
                "Pumice soil creates dry litter beds highly receptive to ember ignition."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Municipal water from groundwater wells; limited storage capacity. "
                "Power-dependent pumping system vulnerable to outages. Rural areas "
                "on private wells with no fire flow capability."
            ),
            "power": (
                "Central Electric Cooperative and Pacific Power; long overhead transmission "
                "lines through forest. Extended outages during fire events. No local generation."
            ),
            "communications": (
                "Limited cell coverage in surrounding forest. Deschutes County 911 dispatch. "
                "Emergency alerts depend on cell/internet connectivity that degrades during fire events."
            ),
            "medical": (
                "No hospital; La Pine Community Health Center for basic care. Nearest hospital "
                "is St. Charles Bend (30 miles north). Air ambulance from Bend; smoke conditions "
                "can ground helicopters during fire events."
            ),
        },
        "demographics_risk_factors": {
            "population": 2566,
            "seasonal_variation": (
                "Greater La Pine area ~20,000 including unincorporated Deschutes County. "
                "Summer recreation (Cascade Lakes, Newberry Crater) adds thousands of visitors. "
                "Many vacation homes occupied only seasonally — owners may not receive alerts."
            ),
            "elderly_percentage": "~25% over 65",
            "mobile_homes": (
                "Significant manufactured home presence in unincorporated areas; many on large "
                "forested lots with poor defensible space. Estimated 15-20% of housing stock."
            ),
            "special_needs_facilities": (
                "Limited; one senior center. Nearest hospital and emergency services 30 miles "
                "away in Bend. Large elderly population with limited mobility."
            ),
        },
    },

    # =========================================================================
    # 5. THE DALLES, OR — Columbia Gorge, Eagle Creek Fire Area
    # =========================================================================
    "the_dalles_or": {
        "center": [45.5946, -121.1787],
        "terrain_notes": (
            "The Dalles (elevation ~100-500 ft along the Columbia River, rising to 1,500+ ft "
            "on the benchlands) is the largest city on the Oregon side of the Columbia River "
            "outside the Portland metro area. Situated at the eastern gateway to the Columbia "
            "River Gorge, the terrain transitions dramatically from the wet, forested western "
            "Gorge to the dry, grassland-covered eastern Gorge. The city occupies a series "
            "of terraces and benchlands rising steeply from the Columbia River. Cherry orchards "
            "and dry grasslands surround the city on the south and east. The Columbia River "
            "Gorge creates a massive natural wind tunnel, with persistent strong winds from "
            "the west in summer and periodic powerful east winds in fall/winter. The city was "
            "affected by smoke and fallout from the 2017 Eagle Creek Fire (50,000 acres) in "
            "the western Gorge, and the surrounding terrain of grass and scattered oak presents "
            "significant fire risk during the dry summer months."
        ),
        "key_features": [
            {"name": "Columbia River Gorge", "bearing": "W", "type": "river_canyon",
             "notes": "80-mile canyon creates extreme wind tunnel effect; 2017 Eagle Creek Fire demonstrated Gorge fire risk"},
            {"name": "The Dalles Dam / Lake Celilo", "bearing": "E", "type": "dam_reservoir",
             "notes": "Federal dam and reservoir; infrastructure requiring fire protection"},
            {"name": "Cherry Orchards / Agricultural Lands", "bearing": "S and SE", "type": "agricultural",
             "notes": "Irrigated orchards and dry grasslands create mosaic fuel pattern; grass fires common"},
            {"name": "Chenoweth Creek Drainage", "bearing": "S", "type": "drainage",
             "notes": "Creek corridor rising into dry grass and oak woodland; fire pathway into residential areas"},
            {"name": "Mill Creek Watershed", "bearing": "S-SW", "type": "watershed",
             "notes": "Municipal watershed in forested terrain; fire threatens water supply"},
            {"name": "I-84 / Columbia River Corridor", "bearing": "E-W", "type": "transportation",
             "notes": "Interstate and BNSF Railway along river; Eagle Creek Fire closed I-84 for weeks"},
        ],
        "elevation_range_ft": [100, 1700],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Eagle Creek Fire", "year": 2017, "acres": 50000,
             "details": "Burned 50,000 acres in Columbia River Gorge; caused by teenager with fireworks. "
                        "Burned for 3 months. Closed I-84 for extended periods, forced hundreds of evacuations. "
                        "Subsequent debris flows (268 landslides) from atmospheric rivers hitting burn scar. "
                        "Dense Douglas-fir/western hemlock forest in steep terrain created extreme fire behavior."},
            {"name": "Sevenmile Hill Fire", "year": 2015, "acres": 2100,
             "details": "Grass and brush fire south of The Dalles; threatened homes on benchlands above city."},
            {"name": "Mosier Creek Fire", "year": 2020, "acres": 200,
             "details": "During Labor Day east wind event; burned near Mosier, 15 miles west of The Dalles. "
                        "Level 3 evacuations issued."},
        ],
        "evacuation_routes": [
            {"route": "I-84 West (toward Portland)", "direction": "W", "lanes": 4,
             "bottleneck": "Gorge section with rockfall zones and narrow segments; Eagle Creek Fire closed this for weeks",
             "risk": "Fire in Gorge closes primary east-west route; detour adds 100+ miles via US-97/I-90"},
            {"route": "I-84 East (toward Biggs Junction)", "direction": "E", "lanes": 4,
             "bottleneck": "Open terrain but grass fire risk along highway margins",
             "risk": "Best evacuation direction during Gorge fires; connects to US-97 N-S corridor"},
            {"route": "US-197 South (toward Dufur/Maupin)", "direction": "S", "lanes": 2,
             "bottleneck": "Climbs steeply out of river valley; winding two-lane road through grass and wheat lands",
             "risk": "Grass fires can cut road; limited capacity for mass evacuation. Connects to US-97."},
            {"route": "US-30 (Historic Columbia River Hwy)", "direction": "W", "lanes": 2,
             "bottleneck": "Narrow, scenic road not suitable for mass evacuation",
             "risk": "Parallels I-84 but through more forested terrain; higher fire risk than interstate."},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Columbia Gorge wind tunnel effect dominates: strong westerly winds in summer "
                "(20-40 mph sustained), periodic powerful easterly winds in fall (40-60+ mph). "
                "East wind events are the primary fire weather concern — drive fires westward "
                "through Gorge and can fan grass fires near The Dalles. The 2017 Eagle Creek "
                "Fire was pushed by east winds. Thermal effects from steep canyon walls create "
                "unpredictable local wind patterns."
            ),
            "critical_corridors": [
                "Columbia River Gorge — extreme wind-driven fire corridor with steep terrain",
                "Chenoweth Creek drainage — fire pathway from grass/oak uplands into city",
                "Mill Creek watershed — forested corridor connecting wildlands to water supply",
                "I-84 highway corridor margins — grass and brush fuel along transportation lifeline",
            ],
            "rate_of_spread_potential": (
                "Extremely fast in grass: 200-400 chains/hr with Gorge winds. In forested "
                "Gorge terrain, crown fire runs of 50-100 chains/hr on steep slopes. "
                "Eagle Creek Fire burned ~50,000 acres total with multi-day high-intensity runs. "
                "Post-fire debris flow risk adds secondary hazard."
            ),
            "spotting_distance": (
                "Gorge winds can carry embers 1-3 miles in steep terrain with strong updrafts. "
                "Eagle Creek Fire generated spot fires across the Columbia River into Washington. "
                "In grass near The Dalles, spotting less significant but rate of spread compensates."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "5 deep wells (15-25% of supply), 7 storage reservoirs, 100 miles of water mains, "
                "5,083 connections, 700+ fire hydrants, 16 pressure zones. New aquifer storage and "
                "recovery (ASR) system increases capacity. Mill Creek watershed fire could contaminate "
                "surface water intakes. Google data centers have driven $28M in new water infrastructure."
            ),
            "power": (
                "Northern Wasco County PUD; overhead lines through Gorge subject to wind damage and fire. "
                "Bonneville Power Administration high-voltage transmission through Gorge; Eagle Creek "
                "Fire threatened transmission corridors."
            ),
            "communications": (
                "Wasco County 911; cell towers on bluffs above city. Gorge winds can damage towers. "
                "Emergency alert systems functional but Gorge terrain creates coverage shadows."
            ),
            "medical": (
                "Mid-Columbia Medical Center — 49-bed community hospital. Limited capacity for "
                "mass-casualty events. Nearest Level II trauma center is in Portland (85 miles west) "
                "or Bend (130 miles south) — both routes can be closed by fire."
            ),
        },
        "demographics_risk_factors": {
            "population": 16010,
            "seasonal_variation": (
                "Cherry harvest (June-August) brings seasonal agricultural workers. "
                "Gorge tourism and wind sports attract visitors year-round. "
                "Google data center employees add to daytime population."
            ),
            "elderly_percentage": "~18% over 65",
            "mobile_homes": (
                "Moderate manufactured home presence, particularly on south-side benchlands "
                "and in unincorporated Wasco County. Estimated 8-10% of housing stock."
            ),
            "special_needs_facilities": (
                "Flagstone Senior Living; Orchard View Estates. Mid-Columbia Medical Center "
                "limited capacity. Long transport times to major trauma centers."
            ),
        },
    },

    # =========================================================================
    # 6. KLAMATH FALLS, OR — Bootleg Fire Region, High Desert
    # =========================================================================
    "klamath_falls_or": {
        "center": [42.2249, -121.7817],
        "terrain_notes": (
            "Klamath Falls (4,094 ft) occupies the southeastern shore of Upper Klamath Lake, "
            "Oregon's largest natural freshwater lake, in a high-desert basin surrounded by "
            "mountains. The Klamath Mountains rise to the west with rugged volcanic formations "
            "and mixed conifer forest. To the east, the terrain transitions through rolling "
            "juniper hills to the Fremont-Winema National Forest where the 2021 Bootleg Fire "
            "burned 413,765 acres. The city sits in a broad, relatively flat basin with the "
            "Klamath River running south toward California. The surrounding landscape is a "
            "complex mosaic of irrigated agricultural land (reclamation project), sagebrush "
            "steppe, juniper woodland, and mixed conifer forest — creating varied fire behavior "
            "potential. The high-desert climate features hot, dry summers with frequent lightning "
            "and significant diurnal temperature swings."
        ),
        "key_features": [
            {"name": "Upper Klamath Lake", "bearing": "NW", "type": "lake",
             "notes": "Oregon's largest natural lake; provides some fire buffer on NW side of city"},
            {"name": "Fremont-Winema National Forest", "bearing": "NE and E", "type": "national_forest",
             "notes": "2.2 million acres; Bootleg Fire (413,765 acres) burned in this forest in 2021"},
            {"name": "Klamath River Canyon", "bearing": "S", "type": "river_canyon",
             "notes": "River corridor toward California; channeled winds and fire corridor"},
            {"name": "Oregon Institute of Technology", "bearing": "W edge of city", "type": "campus",
             "notes": "University campus on hilltop; could serve as emergency staging area"},
            {"name": "California-Oregon Intertie", "bearing": "NE", "type": "power_transmission",
             "notes": "500kV transmission corridor; Bootleg Fire burned 8+ miles of corridor, threatened 15 more"},
            {"name": "Stukel Mountain / Hogback Mountain", "bearing": "SE-S", "type": "mountain_terrain",
             "notes": "Forested volcanic ridges south of city; fire can descend slopes toward developed areas"},
        ],
        "elevation_range_ft": [4094, 5000],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Bootleg Fire", "year": 2021, "acres": 413765,
             "details": "Third-largest fire in Oregon history. Started July 6 near Beatty, 30 miles NE "
                        "of Klamath Falls. Burned for 6+ weeks in Fremont-Winema NF. Grew at 1,000 acres/hr "
                        "at peak. Destroyed 408 buildings (161 houses, 247 outbuildings). Threatened 3,000 homes. "
                        "2,200+ personnel deployed. Burned 8 miles of California-Oregon Intertie power corridor. "
                        "Created its own weather (pyrocumulonimbus clouds)."},
            {"name": "Klamathon Fire", "year": 2018, "acres": 38000,
             "details": "Burned along OR-CA border in Klamath River canyon; threatened Hornbrook, CA. "
                        "Demonstrated cross-border fire risk and Klamath River corridor spread potential."},
            {"name": "Substation Fire", "year": 2018, "acres": 77000,
             "details": "Grass fire east of The Dalles; burned at extreme rates in grass/wheat. "
                        "Part of broader Klamath Basin fire risk pattern."},
        ],
        "evacuation_routes": [
            {"route": "US-97 North (toward Chemult/Bend)", "direction": "N", "lanes": 2,
             "bottleneck": "Two-lane highway through forest and rangeland for 60+ miles; fire can close segments",
             "risk": "Long corridor through fire-prone landscape; Bootleg Fire threatened nearby segments"},
            {"route": "US-97 South (toward Weed, CA)", "direction": "S", "lanes": 2,
             "bottleneck": "Climbs through forested terrain to California border; traffic backs up at state line",
             "risk": "Klamath River canyon fire risk; 2018 Klamathon Fire burned along this corridor"},
            {"route": "OR-39 (toward Merrill/Tulelake)", "direction": "SE", "lanes": 2,
             "bottleneck": "Rural two-lane through agricultural land; limited services for 40+ miles",
             "risk": "Grass and brush fire risk; relatively good evacuation route in agricultural terrain"},
            {"route": "OR-140 (toward Lakeview)", "direction": "E", "lanes": 2,
             "bottleneck": "Remote highway through high desert; minimal services for 100+ miles",
             "risk": "Passes through Fremont-Winema NF and Bootleg Fire burn scar; debris flow risk"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Prevailing SW winds from the Sacramento Valley encounter Klamath Mountains, "
                "creating complex terrain-driven wind patterns. Strong diurnal thermal cycles "
                "in the high-desert basin. Summer afternoon thunderstorms produce dry lightning — "
                "primary ignition source. East wind events less pronounced than western Oregon "
                "but still drive critical fire weather."
            ),
            "critical_corridors": [
                "Fremont-Winema NF to city — NE approach through mixed conifer and juniper",
                "Klamath River canyon — channeled winds carry fire S toward California",
                "California-Oregon Intertie power corridor — cleared corridor can carry grass fire",
                "Upper Klamath Lake margins — dry grasslands and tule marshes seasonally flammable",
            ],
            "rate_of_spread_potential": (
                "Bootleg Fire demonstrated extreme spread at 1,000 acres/hr under peak conditions. "
                "In juniper/sagebrush near city: 50-150 chains/hr. In grass/wheat: 200-400 chains/hr. "
                "Mixed conifer in mountains: 30-80 chains/hr surface, 150+ chains/hr crown fire. "
                "Drought conditions amplify all rates significantly."
            ),
            "spotting_distance": (
                "Bootleg Fire created pyrocumulonimbus clouds capable of long-range spotting (3-5+ miles). "
                "In juniper near city: 0.25-0.5 mile spotting. Grass fires rely on continuous "
                "spread rather than spotting. Mixed conifer: 1-2 mile spotting in crown fire."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "City water from Upper Klamath Lake treatment plant and groundwater wells. "
                "Aging infrastructure in some neighborhoods. Agricultural water diversions "
                "(Klamath Reclamation Project) can conflict with firefighting water needs."
            ),
            "power": (
                "Pacific Power; California-Oregon Intertie 500kV transmission serves California load. "
                "Bootleg Fire burned 8 miles of this corridor and threatened to cut power to California. "
                "Local distribution through juniper and forest corridors vulnerable to fire."
            ),
            "communications": (
                "Klamath County 911; cell towers on ridge tops. Basin terrain provides adequate "
                "coverage in city but dead zones in surrounding mountains and forest. "
                "Emergency radio repeaters on mountain sites vulnerable to fire."
            ),
            "medical": (
                "Sky Lakes Medical Center — 176 beds, only hospital in Klamath County. "
                "Nearest alternatives: Medford (75 miles NW) or Redding, CA (200 miles S). "
                "Limited surge capacity for mass-casualty events. Oregon Tech EMS training center."
            ),
        },
        "demographics_risk_factors": {
            "population": 22174,
            "seasonal_variation": (
                "Moderate tourism to Crater Lake (60 miles NW), Upper Klamath Lake, and "
                "Klamath Wildlife Refuges. Seasonal agricultural workers for potato and "
                "cattle operations. Winter snowbird population minimal."
            ),
            "elderly_percentage": "~16% over 65",
            "mobile_homes": (
                "Moderate manufactured home presence, particularly in south and east side "
                "of city and unincorporated county. Estimated 10-12% of housing stock."
            ),
            "special_needs_facilities": (
                "Crystal Terrace Assisted Living; several adult foster homes. "
                "Sky Lakes Medical Center limited capacity. Oregon Institute of Technology "
                "campus population (~5,000) during academic year."
            ),
        },
    },

    # =========================================================================
    # 7. DETROIT, OR — Beachie Creek Fire, Destroyed 2020
    # =========================================================================
    "detroit_or": {
        "center": [44.7317, -122.1531],
        "terrain_notes": (
            "Detroit (~1,500 ft, though Detroit Lake surface is at ~1,569 ft) is a tiny "
            "mountain community in the North Santiam Canyon, perched on the shore of "
            "Detroit Lake, a 3,580-acre reservoir behind Detroit Dam. The town occupies a "
            "narrow strip of flat land between steep, densely forested canyon walls and the "
            "lake. Highway 22 — a two-lane mountain road — is the sole transportation "
            "corridor through the canyon, passing through Mill City, Gates, Detroit, and "
            "Idanha in sequence. The canyon is deeply incised with slopes rising 2,000-3,000 ft "
            "above the river on both sides, covered in dense Douglas-fir, western hemlock, "
            "and western red cedar. On September 8, 2020, the Beachie Creek Fire — which "
            "had been burning since August 16 in the Opal Creek Wilderness — was driven by "
            "extreme east winds (gusts to 60+ mph) down the canyon, destroying approximately "
            "70% of Detroit's businesses and public buildings in a matter of hours. The town "
            "has been slowly rebuilding but remains profoundly vulnerable due to its canyon "
            "geography and single-road access."
        ),
        "key_features": [
            {"name": "Detroit Lake / Detroit Dam", "bearing": "N-NW", "type": "reservoir",
             "notes": "3,580-acre reservoir; provides partial fire break but lake level drops in late summer, exposing fuel"},
            {"name": "North Santiam River Canyon", "bearing": "E-W corridor", "type": "river_canyon",
             "notes": "Deeply incised canyon; Hwy 22 follows river. Fire channeled through canyon at extreme speed on Sept 8, 2020"},
            {"name": "Opal Creek Wilderness", "bearing": "NE", "type": "wilderness",
             "notes": "35,000 acres of old-growth; Beachie Creek Fire originated here Aug 16, 2020"},
            {"name": "Breitenbush Hot Springs", "bearing": "E", "type": "resort_community",
             "notes": "Remote resort community on Forest Rd 46; destroyed by Beachie Creek Fire. Single-road access."},
            {"name": "Idanha", "bearing": "E (4 miles)", "type": "town",
             "notes": "Tiny community (pop ~135) also devastated by Beachie Creek Fire; shared evacuation corridor"},
            {"name": "Blowout Ridge / Coffin Mountain", "bearing": "S", "type": "ridgeline",
             "notes": "Steep terrain above Detroit; fire raced down these slopes into town"},
        ],
        "elevation_range_ft": [1500, 1700],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Beachie Creek Fire (Santiam Fire)", "year": 2020, "acres": 193556,
             "details": "Lightning-caused Aug 16, 2020 in Opal Creek Wilderness. During Sept 7-8 Labor Day "
                        "east wind event (60+ mph gusts), merged with Lionshead Fire and raced down North "
                        "Santiam Canyon. Destroyed 1,288 structures total (470 residences, 35 commercial, "
                        "783 other). Nearly wiped out Detroit and Gates — 70% of Detroit's businesses and "
                        "public buildings destroyed. Killed at least 5 people. 40,000 residents evacuated "
                        "across the canyon. Many residents in Gates received no evacuation warning. "
                        "Total suppression cost exceeded $100M."},
            {"name": "Lionshead Fire", "year": 2020, "acres": 204469,
             "details": "Merged with Beachie Creek Fire during Sept 8 wind event; combined fires burned "
                        "nearly 400,000 acres. Started in Mt. Jefferson Wilderness on Aug 16."},
        ],
        "evacuation_routes": [
            {"route": "OR-22 West (toward Salem)", "direction": "W", "lanes": 2,
             "bottleneck": "Two-lane canyon road for 50+ miles through Gates, Mill City to Salem. "
                          "Curving, mountainous terrain with no passing lanes for long stretches.",
             "risk": "Primary evacuation route. During 2020 fire, residents had to drive THROUGH "
                     "active fire zones. Fire burned on both sides of highway. Canyon geometry "
                     "concentrates smoke and heat on road surface."},
            {"route": "OR-22 East (toward Santiam Junction)", "direction": "E", "lanes": 2,
             "bottleneck": "Climbs over Santiam Pass (4,817 ft); connects to US-20. Mountain curves, winter closures.",
             "risk": "Secondary route; during 2020 fire, some residents sent east to Santiam Junction. "
                     "Road passes through continuous forest the entire distance."},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "North Santiam Canyon acts as a massive wind tunnel during east wind events. "
                "September 2020 demonstrated: east winds of 40-60 mph (gusts higher) channeled "
                "through the canyon, pushing the Beachie Creek Fire ~15 miles in a single night. "
                "Downslope (katabatic) winds accelerate fire descent from ridges into the canyon "
                "floor where the town sits. Normal summer pattern is gentle upvalley afternoon winds."
            ),
            "critical_corridors": [
                "North Santiam Canyon — primary fire corridor; wind tunnel effect during east winds",
                "Breitenbush River drainage — secondary fire approach from east/northeast",
                "Steep canyon walls — fire runs downslope at extreme rates into narrow canyon floor",
                "OR-22 highway corridor — only transportation route acts as fire corridor simultaneously",
            ],
            "rate_of_spread_potential": (
                "Beachie Creek Fire demonstrated catastrophic canyon-driven spread: ~15 miles in "
                "12 hours through dense old-growth and second-growth forest. In steep canyon terrain "
                "with wind alignment, rates exceeding 200 chains/hr observed. Upslope runs on canyon "
                "walls can exceed 300 chains/hr. Crown fire conditions virtually continuous in heavy "
                "Douglas-fir stands."
            ),
            "spotting_distance": (
                "2-5 miles during extreme east wind events; massive ember showers documented "
                "during Beachie Creek Fire. Embers crossed Detroit Lake. Dense forest canopy "
                "produces enormous volumes of firebrands during crown fire. Canyon updrafts "
                "loft embers to extreme heights."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Municipal water system was largely destroyed in 2020 fire; rebuilt with new "
                "infrastructure. Detroit Dam and reservoir managed by Army Corps. Water intakes "
                "in heavily forested watershed vulnerable to contamination. Post-fire sediment "
                "and debris flows into Detroit Lake have degraded water quality."
            ),
            "power": (
                "Pacific Power; overhead lines through canyon destroyed in 2020 fire. "
                "Restoration took months. Single transmission corridor through canyon means "
                "any fire event causes complete power loss to Detroit, Idanha, and Breitenbush."
            ),
            "communications": (
                "Cell coverage extremely limited in canyon; terrain blocks signals. During 2020 "
                "fire, residents in Gates reported receiving no evacuation alerts — power lines "
                "went down before warnings could be sent. Satellite/landline destroyed. "
                "Marion County 911 had difficulty reaching canyon residents."
            ),
            "medical": (
                "No medical facilities in Detroit. Nearest hospital: Salem Hospital (50 miles west "
                "via Hwy 22). During fire events with road closures, community is completely "
                "isolated from medical care. Air ambulance impossible in smoke conditions."
            ),
        },
        "demographics_risk_factors": {
            "population": 202,
            "seasonal_variation": (
                "Detroit Lake attracts 500,000+ visitors annually for recreation (fishing, "
                "boating, camping). Summer population can exceed 5,000+ on peak weekends — "
                "25x the resident population. Visitors unfamiliar with evacuation routes and "
                "may not be signed up for emergency alerts."
            ),
            "elderly_percentage": "~20% over 65 (many retirees)",
            "mobile_homes": (
                "Minimal post-fire; pre-2020, several RV parks and manufactured homes along "
                "Hwy 22 were destroyed. Rebuilding has been slow due to insurance and permit challenges."
            ),
            "special_needs_facilities": (
                "None in Detroit. Nearest care facilities in Salem. Community has no pharmacy, "
                "no medical clinic, no emergency services beyond volunteer fire department."
            ),
        },
    },

    # =========================================================================
    # 8. GATES, OR — Beachie Creek Fire, Destroyed 2020
    # =========================================================================
    "gates_or": {
        "center": [44.7536, -122.4069],
        "terrain_notes": (
            "Gates (elevation ~950 ft) is a small city 15 miles west of Detroit in the North "
            "Santiam Canyon, situated where the canyon begins to narrow as one travels east "
            "from the broader Willamette Valley. The town sits on a small flat along the North "
            "Santiam River, hemmed in by steep forested slopes. On September 8, 2020, the "
            "Beachie Creek Fire raced through the canyon with extreme east winds, but in Gates, "
            "the primary ignition mechanism was downed power lines — Pacific Power infrastructure "
            "failed in the extreme winds, sparking fires throughout town before the main fire "
            "front arrived. Residents received essentially no evacuation warning. The city was "
            "nearly completely destroyed. The town has been slowly rebuilding but population "
            "has not returned to pre-fire levels. Gates is named for the narrow 'gateway' in "
            "the canyon at this point."
        ),
        "key_features": [
            {"name": "North Santiam River", "bearing": "Through town", "type": "river",
             "notes": "River runs through narrow canyon; provided minimal fire break during 2020 fire"},
            {"name": "Gates Hill / Canyon Walls", "bearing": "N and S", "type": "steep_terrain",
             "notes": "Steep forested slopes rise directly above town on both sides; fire descends from above"},
            {"name": "Mill City", "bearing": "W (3 miles)", "type": "town",
             "notes": "Neighboring city (pop ~1,800) also damaged in 2020 fire; shared evacuation route"},
            {"name": "Pacific Power Line Corridor", "bearing": "E-W through canyon", "type": "utility",
             "notes": "Power lines that failed during east wind event, sparking fires in Gates before main fire front arrived"},
            {"name": "Fath Camp / Camp Upward Bound", "bearing": "Adjacent to town", "type": "camp",
             "notes": "Nearly 50-year-old religious camp destroyed in 2020 fire; still recovering as of 2025"},
        ],
        "elevation_range_ft": [850, 1100],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Beachie Creek Fire (Santiam Fire)", "year": 2020, "acres": 193556,
             "details": "Gates was devastated: nearly the entire town destroyed. Unlike Detroit where "
                        "the main fire front arrived from the east, Gates was initially ignited by power "
                        "line failures in the extreme east winds before the fire front reached town. "
                        "Residents received NO evacuation notice — power went down, cell service failed, "
                        "and the fire was still 10+ miles away when local ignitions began. Part of the "
                        "1,288-structure total destruction count. Multiple fatalities in the canyon."},
        ],
        "evacuation_routes": [
            {"route": "OR-22 West (toward Stayton/Salem)", "direction": "W", "lanes": 2,
             "bottleneck": "Two-lane canyon road; passes through Mill City and Lyons which were also under evacuation",
             "risk": "Only viable evacuation direction. During 2020, fire burned on both sides of highway. "
                     "Sheriff requested eastbound closure to allow evacuees passage. Canyon road with no alternatives."},
            {"route": "OR-22 East (toward Detroit)", "direction": "E", "lanes": 2,
             "bottleneck": "Leads deeper into canyon toward Detroit, which was also burning",
             "risk": "NOT a viable evacuation route during 2020 event — driving east meant driving into the fire."},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Canyon funneling of east winds is the critical threat. September 2020 east winds "
                "of 40-60+ mph were amplified through the canyon narrows at Gates. Additionally, "
                "wind-driven power line failures created independent ignition points throughout town "
                "before the main fire front arrived. This dual-ignition mechanism (airborne embers "
                "AND infrastructure failure) is a key lesson from Gates."
            ),
            "critical_corridors": [
                "North Santiam Canyon — wind tunnel from Cascade crest to valley",
                "Power line corridor — infrastructure failure creates ignition sources ahead of fire front",
                "Steep canyon walls — fire descends from above onto canyon floor where town sits",
                "OR-22 road corridor — only access route also serves as fire corridor",
            ],
            "rate_of_spread_potential": (
                "Catastrophic: Beachie Creek Fire covered 15+ miles in the canyon in ~12 hours. "
                "But in Gates, local power-line ignitions destroyed the town even faster than "
                "the main fire front would have. Canyon-channeled winds drove surface and crown "
                "fire at 150-250 chains/hr through mixed conifer forest."
            ),
            "spotting_distance": (
                "2-4 miles with canyon-amplified winds; but the infrastructure-failure ignition "
                "mechanism in Gates effectively created 'spotting' via power lines at distances "
                "of 10+ miles ahead of the fire front."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Municipal water system destroyed in 2020 fire; rebuilt as part of recovery. "
                "Small-scale system serving ~500 people. Well and reservoir infrastructure."
            ),
            "power": (
                "Pacific Power overhead lines through canyon — catastrophic failure during 2020 "
                "east wind event. Lines downed by wind and falling trees CAUSED fires in Gates "
                "ahead of the wildfire front. Utility negligence lawsuit filed by residents. "
                "Single-corridor power supply with no redundancy."
            ),
            "communications": (
                "Cell coverage poor in canyon. During 2020 fire, communication failure was total — "
                "no evacuation warnings reached residents. Power failure eliminated landlines "
                "and cell tower backup power insufficient. This was a primary factor in "
                "near-total town destruction."
            ),
            "medical": (
                "No medical facilities. Nearest hospital: Santiam Hospital in Stayton (25 miles west) "
                "or Salem Hospital (45 miles west). During road closures, completely isolated."
            ),
        },
        "demographics_risk_factors": {
            "population": 471,
            "seasonal_variation": (
                "Some increase from Detroit Lake recreation traffic passing through on Hwy 22. "
                "Summer cabins and vacation properties. Population has not returned to pre-fire "
                "levels; many displaced residents did not rebuild."
            ),
            "elderly_percentage": "~22% over 65",
            "mobile_homes": (
                "Pre-fire: significant manufactured home presence along highway corridor. "
                "Most were destroyed in 2020 fire. Rebuilt housing is primarily stick-built "
                "with improved fire resistance."
            ),
            "special_needs_facilities": (
                "None. No pharmacy, no clinic, no senior center. Community entirely dependent "
                "on services in Stayton, Salem, or Bend."
            ),
        },
    },

    # =========================================================================
    # 9. BLUE RIVER, OR — Holiday Farm Fire, Destroyed 2020
    # =========================================================================
    "blue_river_or": {
        "center": [44.1626, -122.3339],
        "terrain_notes": (
            "Blue River (~1,000 ft) is a small unincorporated community in the McKenzie River "
            "valley of Lane County, approximately 57 miles east of Eugene along Oregon Route 126. "
            "The community sits at the confluence of Blue River and the McKenzie River, in a "
            "narrow valley bounded by steep, heavily forested slopes of the Willamette National "
            "Forest. The terrain is dominated by dense Douglas-fir and western hemlock forest "
            "with heavy understory fuel loads. On September 7-8, 2020, the Holiday Farm Fire "
            "— ignited when power lines fell in extreme east winds — raced 27 miles down the "
            "McKenzie River corridor from near McKenzie Bridge through Blue River, Vida, Nimrod, "
            "and Leaburg. The fire destroyed over 500 homes and 768 total structures, including "
            "most of the structures in Blue River. The community has been slowly rebuilding, "
            "with new housing projects opening in 2025, five years after the fire."
        ),
        "key_features": [
            {"name": "McKenzie River", "bearing": "E-W through community", "type": "river_corridor",
             "notes": "Wild and Scenic River corridor; fire raced 27 miles down this valley in 2020"},
            {"name": "Blue River Reservoir", "bearing": "NE", "type": "reservoir",
             "notes": "Flood control reservoir; forested watershed above. Dam creates narrow canyon below."},
            {"name": "OR-126 (McKenzie Highway)", "bearing": "E-W", "type": "highway",
             "notes": "Only road through valley; Holiday Farm Fire paralleled and crossed highway repeatedly"},
            {"name": "Willamette National Forest", "bearing": "All directions", "type": "national_forest",
             "notes": "1.68 million acres of dense forest surrounds community; continuous canopy fuel from Cascades to valley floor"},
            {"name": "Vida / Nimrod / Leaburg", "bearing": "W (downstream)", "type": "communities",
             "notes": "Small communities downstream along McKenzie River also destroyed or damaged by Holiday Farm Fire"},
            {"name": "McKenzie Bridge", "bearing": "E (10 miles)", "type": "community",
             "notes": "Small community upstream; near fire's origin point. Remote with very limited evacuation options."},
        ],
        "elevation_range_ft": [900, 1200],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Holiday Farm Fire", "year": 2020, "acres": 173393,
             "details": "Started Sept 7, 2020 around 7:45 PM near Holiday Farm RV Resort when power lines "
                        "fell in extreme east winds. Spread 27 miles down McKenzie River valley in ~12 hours. "
                        "Destroyed 768 structures including 517 homes. Killed 1 person (David Scott Perry, "
                        "59, in Vida). Burned 173,393 acres of Lane County forest and communities. "
                        "Federal lawsuit filed against Pacific Power/PacifiCorp for infrastructure failure. "
                        "Most structures in Blue River were destroyed."},
        ],
        "evacuation_routes": [
            {"route": "OR-126 West (toward Springfield/Eugene)", "direction": "W", "lanes": 2,
             "bottleneck": "Two-lane road through narrow river canyon for 50+ miles; passes through Vida, "
                          "Nimrod, Leaburg — all also on fire in 2020",
             "risk": "Only evacuation route for Blue River. During 2020 fire, residents had to drive through "
                     "fire zones. Road was impassable in some sections. ~57 miles to Eugene on winding canyon road."},
            {"route": "OR-126 East (toward McKenzie Bridge/Sisters)", "direction": "E", "lanes": 2,
             "bottleneck": "Climbs into mountains; very remote, no services. McKenzie Pass closed Oct-Jun.",
             "risk": "Leads deeper into forest and mountains. During 2020 fire, this direction led toward "
                     "the fire's origin. Not a viable evacuation route during east wind fire events."},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "McKenzie River valley creates a natural wind funnel during east wind events. "
                "September 2020 demonstrated: east winds of 40-60 mph channeled down the valley, "
                "driving the fire 27 miles westward in approximately 12 hours. Normal summer "
                "pattern is gentle upvalley afternoon winds. The east wind events are episodic "
                "but catastrophic — capable of transforming a remote forest fire into a valley-wide "
                "conflagration in hours."
            ),
            "critical_corridors": [
                "McKenzie River valley — primary fire corridor; wind funnel during east wind events",
                "Blue River tributary drainage — fire pathway from surrounding forest into community",
                "OR-126 highway corridor — fire paralleled road through continuous forest",
                "Power line corridor — infrastructure failure created ignition ahead of fire front",
            ],
            "rate_of_spread_potential": (
                "Holiday Farm Fire demonstrated valley-corridor spread of 27 miles in ~12 hours, "
                "averaging over 2 miles per hour sustained. In the steep, forested terrain of "
                "the McKenzie corridor, crown fire runs exceeding 200 chains/hr. Upslope runs "
                "on valley walls can exceed 300 chains/hr. Continuous dense fuel load with no "
                "natural firebreaks in the valley."
            ),
            "spotting_distance": (
                "2-5 miles during extreme east wind events; massive ember production from "
                "old-growth and second-growth Douglas-fir crown fire. Power line failures "
                "created ignition 10+ miles ahead of fire front. Valley geometry concentrates "
                "embers in the narrow corridor."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Small community water system destroyed in 2020 fire; rebuilt. Blue River "
                "water dependent on local wells and surface intake from Blue River. "
                "Post-fire sediment and debris contaminate watershed for years."
            ),
            "power": (
                "EWEB (Eugene Water & Electric Board) and Pacific Power serve area. "
                "Overhead lines through forested canyon; power line failure started the Holiday Farm Fire. "
                "Federal lawsuit against PacifiCorp for infrastructure failure. Single-corridor "
                "power supply with complete vulnerability to canyon fires."
            ),
            "communications": (
                "Extremely limited cell coverage in McKenzie valley. Canyon terrain blocks signals. "
                "During 2020 fire, power failure eliminated communications before many residents "
                "could be warned. Lane County emergency alerts reached some residents but many missed."
            ),
            "medical": (
                "No medical facilities. Nearest hospital: PeaceHealth Sacred Heart at RiverBend "
                "in Springfield (~55 miles west). During fire with road closures, completely "
                "isolated from medical care."
            ),
        },
        "demographics_risk_factors": {
            "population": 800,
            "seasonal_variation": (
                "McKenzie River recreation (fishing, rafting, hot springs) brings significant "
                "summer visitors. Cougar Reservoir and Blue River Reservoir attract campers. "
                "Population reduced post-fire; rebuilding ongoing as of 2025."
            ),
            "elderly_percentage": "~25% over 65 (rural retirement community character)",
            "mobile_homes": (
                "Pre-fire: significant manufactured homes and RV parks along Hwy 126 and river. "
                "Holiday Farm RV Resort (near fire's origin) destroyed. Rebuilt housing mostly "
                "permanent construction with improved fire resistance."
            ),
            "special_needs_facilities": (
                "None. No pharmacy, clinic, or senior services. Community entirely dependent on "
                "Springfield/Eugene for medical and social services — 55 miles away."
            ),
        },
    },

    # =========================================================================
    # 10. TALENT, OR — Almeda Fire, 700+ Homes Destroyed 2020
    # =========================================================================
    "talent_or": {
        "center": [42.2457, -122.7887],
        "terrain_notes": (
            "Talent (1,635 ft) is a small city in the Rogue Valley of southern Oregon, located "
            "along Interstate 5 and Oregon Route 99 between Ashland (to the south) and Phoenix "
            "(to the north). The city occupies the flat Bear Creek Valley floor, bounded by Bear "
            "Creek to the east and the low hills of the Rogue Valley to the west. Talent was "
            "one of the two communities most devastated by the 2020 Almeda Fire, which destroyed "
            "approximately one-third of the town — 700+ homes, predominantly in mobile home parks "
            "housing lower-income and Latino families. The fire ran through the Bear Creek riparian "
            "corridor and along the I-5/OR-99 transportation corridor, burning through 18 mobile "
            "home parks between Ashland and south Medford. Talent has since emerged as a national "
            "model for wildfire recovery, with new energy-efficient housing and community-owned "
            "mobile home parks replacing destroyed stock."
        ),
        "key_features": [
            {"name": "Bear Creek / Bear Creek Greenway", "bearing": "N-S through east side of town", "type": "riparian_corridor",
             "notes": "Riparian corridor that carried the Almeda Fire; continuous fuel from Ashland to Medford"},
            {"name": "I-5 / OR-99 Corridor", "bearing": "N-S", "type": "transportation",
             "notes": "Interstate and parallel highway bracket town; fire crossed and paralleled both"},
            {"name": "Mobile Home Parks (multiple)", "bearing": "Along OR-99 and Bear Creek", "type": "residential",
             "notes": "18 mobile home parks between Ashland and Medford were destroyed; Talent lost 700+ homes, "
                      "65% were manufactured homes. Talent Mobile Estates (now Talent Community Cooperative) was devastated."},
            {"name": "Wagner Creek", "bearing": "W", "type": "drainage",
             "notes": "Tributary to Bear Creek draining western hills; secondary fire pathway"},
            {"name": "Talent City Park / Schools", "bearing": "Central", "type": "infrastructure",
             "notes": "Community facilities that served as gathering points during and after fire"},
        ],
        "elevation_range_ft": [1550, 1750],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Almeda Fire", "year": 2020, "acres": 3200,
             "details": "September 8, 2020; human-caused fire started in field on Almeda Dr in north Ashland. "
                        "Driven by 40+ mph winds, burned 9 miles through Bear Creek corridor. Talent lost "
                        "700+ homes — approximately one-third of the town. 65% of homes lost valley-wide "
                        "were manufactured homes. 3 fatalities total. Most destructive fire in Oregon "
                        "history. Jackson County alert system failures meant many Talent residents received "
                        "no evacuation warning. Large Spanish-speaking population had no Spanish-language alerts. "
                        "Town has become nationally recognized leader in wildfire resilience and recovery."},
        ],
        "evacuation_routes": [
            {"route": "I-5 North (toward Medford)", "direction": "N", "lanes": 4,
             "bottleneck": "Interstate provides good capacity but fire burned along and crossed I-5",
             "risk": "Almeda Fire paralleled I-5 for 9 miles; evacuees had to flee through smoke and flames on highway"},
            {"route": "I-5 South (toward Ashland)", "direction": "S", "lanes": 4,
             "bottleneck": "Fire originated in this direction; driving south meant driving toward fire origin",
             "risk": "Not viable during Almeda Fire — fire was pushing north FROM Ashland direction"},
            {"route": "OR-99 (Pacific Highway)", "direction": "N-S", "lanes": 2,
             "bottleneck": "Parallel to I-5 through destroyed areas; significantly less capacity than I-5",
             "risk": "Fire burned through OR-99 corridor; road impassable during active fire"},
            {"route": "Talent Avenue / Local Streets West", "direction": "W", "lanes": 2,
             "bottleneck": "Local roads to western hills; limited capacity, lead to rural areas",
             "risk": "Limited capacity escape to western hills; not a primary evacuation route"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "During the Almeda Fire, anomalous strong southerly winds (40+ mph gusts) pushed "
                "the fire northward through the Bear Creek corridor. Normal summer pattern is "
                "afternoon NW winds with thermal upvalley flow. The fire burned primarily through "
                "urban/suburban fuel — structures, vehicles, landscaping, riparian vegetation — "
                "rather than wildland fuel, making it an unprecedented urban-interface event."
            ),
            "critical_corridors": [
                "Bear Creek riparian corridor — continuous fuel connecting all Rogue Valley communities",
                "I-5 / OR-99 highway margins — grass, brush, and structure-to-structure fire spread",
                "Mobile home park corridors — extremely tight spacing allowed structure-to-structure spread",
                "Wagner Creek drainage — secondary fire pathway from wildlands to developed areas",
            ],
            "rate_of_spread_potential": (
                "Almeda Fire demonstrated sustained urban-corridor spread of ~2 mph over 9 miles. "
                "Structure-to-structure spread in mobile home parks was rapid — minutes between "
                "ignition and full involvement. Riparian vegetation along Bear Creek burned at "
                "50-100 chains/hr. Grass along highway margins: 200+ chains/hr."
            ),
            "spotting_distance": (
                "0.25-0.5 miles via ember transport from burning structures and vegetation. "
                "Wind-driven embers from mobile home fires ignited adjacent structures rapidly. "
                "Propane tanks and vehicle fuel added to ember generation."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "TAP (Talent-Ashland-Phoenix) water system serves ~23,000 people. Fire damaged "
                "water infrastructure; melted plastic service laterals contaminated water with "
                "benzene. Boil-water advisories for weeks post-fire. Water pressure dropped "
                "during fire, hampering suppression efforts."
            ),
            "power": (
                "Pacific Power; overhead distribution destroyed through fire corridor. "
                "Power restoration took weeks in destroyed areas. Lack of power hampered "
                "pumping for water system recovery."
            ),
            "communications": (
                "Jackson County emergency alert system had critical gaps — many Talent "
                "residents received NO evacuation warning. Language barriers: large "
                "Spanish-speaking population had no access to Spanish-language emergency "
                "alerts. Cell towers functional but alert system failure was the primary issue."
            ),
            "medical": (
                "No hospital in Talent; served by Asante Rogue Regional (378 beds) and "
                "Providence Medford Medical Center (120 beds), both in Medford, 10 miles north. "
                "During fire, roads to Medford were compromised."
            ),
        },
        "demographics_risk_factors": {
            "population": 6282,
            "seasonal_variation": (
                "Minimal seasonal variation; primarily year-round residents. Agricultural "
                "workers in the Rogue Valley (orchards, vineyards) add to population during harvest."
            ),
            "elderly_percentage": "~23% over 65",
            "mobile_homes": (
                "CRITICAL VULNERABILITY: 65% of homes destroyed valley-wide were manufactured homes. "
                "Talent lost 700+ homes, predominantly in mobile home parks. Pre-fire ~15% of housing "
                "was manufactured. Many parks housed Latino families. Post-fire, Talent Community "
                "Cooperative (resident-owned) replaced destroyed Talent Mobile Estates with ~80 new "
                "energy-efficient manufactured homes (Energy Trust partnership)."
            ),
            "special_needs_facilities": (
                "Limited; small senior housing. Large ESL population requiring multilingual "
                "emergency services. Phoenix-Talent School District serves the area. "
                "Post-fire Gateway housing project provided student housing for displaced families."
            ),
        },
    },

    # =========================================================================
    # 11. PHOENIX, OR — Almeda Fire, Devastated 2020
    # =========================================================================
    "phoenix_or": {
        "center": [42.2751, -122.8178],
        "terrain_notes": (
            "Phoenix (1,560 ft) is a small city in the Rogue Valley immediately north of "
            "Talent and south of Medford, straddling I-5 and OR-99 along the Bear Creek "
            "corridor. Like Talent, Phoenix was devastated by the 2020 Almeda Fire, which "
            "burned through the Bear Creek Greenway and destroyed hundreds of homes and "
            "businesses. The town occupies a flat valley position with Bear Creek and the "
            "Greenway running through its eastern side. Phoenix has a significant Latino "
            "population and had numerous mobile home parks that were particularly vulnerable. "
            "The city's fire exposure comes primarily from the urban-interface corridor along "
            "Bear Creek rather than traditional wildland fire, though grass-covered hills "
            "rise to the west. Recovery has been ongoing for 5+ years with new housing and "
            "infrastructure emerging."
        ),
        "key_features": [
            {"name": "Bear Creek / Greenway", "bearing": "N-S through east side", "type": "riparian_corridor",
             "notes": "Carried the Almeda Fire through town; riparian vegetation was continuous fuel"},
            {"name": "I-5 / OR-99 / CORP Railroad", "bearing": "N-S", "type": "transportation",
             "notes": "Transportation infrastructure through town; fire burned along all corridors"},
            {"name": "Mobile Home Parks", "bearing": "Along OR-99 and Bear Creek", "type": "residential",
             "notes": "Multiple manufactured home communities destroyed; housed predominantly Latino families"},
            {"name": "Phoenix Commercial District", "bearing": "Central on OR-99", "type": "commercial",
             "notes": "Businesses along OR-99 destroyed in Almeda Fire; some still rebuilding as of 2025"},
        ],
        "elevation_range_ft": [1500, 1700],
        "wui_exposure": "high",
        "historical_fires": [
            {"name": "Almeda Fire", "year": 2020, "acres": 3200,
             "details": "September 8, 2020; fire burned through Phoenix as part of the 9-mile corridor "
                        "from Ashland to south Medford. Hundreds of homes and businesses destroyed. "
                        "Part of the 2,800+ structure total. Mobile home parks particularly devastated. "
                        "Latino families disproportionately affected. Recovery continues 5+ years later."},
        ],
        "evacuation_routes": [
            {"route": "I-5 North (toward Medford)", "direction": "N", "lanes": 4,
             "bottleneck": "Best capacity route but fire burned along and crossed I-5",
             "risk": "Fire paralleled I-5; however northward movement was viable as fire pushed from south"},
            {"route": "I-5 South (toward Talent/Ashland)", "direction": "S", "lanes": 4,
             "bottleneck": "Fire origin direction; not viable for southbound evacuation",
             "risk": "Fire was approaching from this direction during Almeda Fire"},
            {"route": "Fern Valley Road / Local Streets West", "direction": "W", "lanes": 2,
             "bottleneck": "Local roads to western hills; limited capacity",
             "risk": "Leads to rural foothill areas; not designed for mass evacuation"},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Same as Talent — anomalous strong southerly winds during Almeda Fire pushed "
                "fire through Bear Creek corridor. Rogue Valley channeling amplifies wind. "
                "Normal summer: afternoon NW winds, thermal upvalley flow."
            ),
            "critical_corridors": [
                "Bear Creek riparian corridor — continuous fuel connecting Talent through Phoenix to Medford",
                "I-5 / OR-99 margins — grass, brush, and structure-to-structure spread corridor",
                "Mobile home park corridors — tight spacing enabled rapid structure-to-structure fire spread",
            ],
            "rate_of_spread_potential": (
                "Consistent with Almeda Fire observations: ~2 mph sustained urban-corridor spread. "
                "Structure-to-structure in mobile home parks: minutes. Riparian corridor: 50-100 chains/hr."
            ),
            "spotting_distance": (
                "0.25-0.5 miles from structure fires and wind-driven embers. Propane tanks "
                "and vehicle fuel tanks added to ember generation and spotting."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "TAP (Talent-Ashland-Phoenix) shared water system; same vulnerability as Talent. "
                "Benzene contamination from melted plastic pipes post-fire."
            ),
            "power": (
                "Pacific Power; overhead distribution destroyed in fire corridor. "
                "Extensive rebuilding of electrical infrastructure ongoing."
            ),
            "communications": (
                "Same Jackson County alert system failures as Talent — many Phoenix residents "
                "received no warning. Spanish-speaking population particularly underserved by "
                "English-only alert systems."
            ),
            "medical": (
                "No hospital; served by Medford hospitals 5-8 miles north. During Almeda Fire, "
                "road access to Medford was compromised by smoke and fire along I-5."
            ),
        },
        "demographics_risk_factors": {
            "population": 4475,
            "seasonal_variation": "Minimal; primarily year-round resident community.",
            "elderly_percentage": "~18% over 65",
            "mobile_homes": (
                "Pre-fire: significant manufactured home population, predominantly housing "
                "Latino families. Majority of homes lost were manufactured. Post-fire recovery "
                "includes new manufactured home communities with improved fire resilience."
            ),
            "special_needs_facilities": (
                "Limited. Phoenix-Talent School District. Significant ESL community requiring "
                "bilingual emergency services. Environmental justice concerns — fire "
                "disproportionately impacted lower-income communities of color."
            ),
        },
    },

    # =========================================================================
    # 12. OAKRIDGE, OR — Middle Fork Willamette, Extreme Isolation Risk
    # =========================================================================
    "oakridge_or": {
        "center": [43.7465, -122.4612],
        "terrain_notes": (
            "Oakridge (~1,200-1,600 ft) is an isolated former timber town on the Middle Fork "
            "of the Willamette River, surrounded by the Willamette National Forest. Located "
            "approximately 40 miles east of Eugene on Oregon Route 58, the city sits in a "
            "narrow valley at the confluence of Salmon Creek, Salt Creek, Hills Creek, and "
            "the Middle and North Forks of the Willamette. Dense Douglas-fir and western hemlock "
            "forest rises steeply on all sides. Highway 58 — the primary route between Eugene "
            "and Central Oregon — is the city's lifeline and sole realistic evacuation route. "
            "Oakridge has experienced recurrent fire threats: the 2023 Bedrock Fire, 2024 "
            "Willamette Complex (Oakridge Lightning Fires), and 2025 Aubrey Mountain and "
            "Dunning Road fires all triggered evacuations and highway closures. The town has "
            "a high poverty rate (30%), significant elderly population, and 25% manufactured "
            "housing — creating a highly vulnerable demographic profile."
        ),
        "key_features": [
            {"name": "Middle Fork Willamette River", "bearing": "E-W through town", "type": "river_corridor",
             "notes": "River corridor connects deep forest to town; riparian fuel continuous upstream"},
            {"name": "Hills Creek Reservoir", "bearing": "SE", "type": "reservoir",
             "notes": "Large reservoir upstream; forested watershed above. Dam downstream of town."},
            {"name": "OR-58 (Willamette Highway)", "bearing": "E-W", "type": "highway",
             "notes": "Only highway through area; repeatedly closed by fires (2023, 2024, 2025). Sole evacuation route."},
            {"name": "Salmon Creek / Salt Creek", "bearing": "S", "type": "drainages",
             "notes": "Steep forested drainages converging on town; fire corridors from Cascade foothills"},
            {"name": "Westfir", "bearing": "W (adjacent)", "type": "town",
             "notes": "Tiny neighbor community (pop ~250) at confluence of North Fork Willamette; shares fire risk and evacuation"},
            {"name": "Willamette National Forest", "bearing": "All directions", "type": "national_forest",
             "notes": "1.68 million acres of dense forest completely surrounds community; heavy fuel loading"},
        ],
        "elevation_range_ft": [1200, 1600],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Aubrey Mountain Fire", "year": 2025, "acres": 35,
             "details": "East of Oakridge off Hwy 58 on Middle Fork Ranger District. Triggered Level 3 "
                        "'Go Now' evacuations for east Oakridge. Highway 58 partially closed. Steep, "
                        "timber terrain. 65% contained before downgrade."},
            {"name": "Dunning Road Fire", "year": 2025, "acres": 100,
             "details": "Prompted evacuation orders for east Oakridge and partial Highway 58 closure. "
                        "Burned in timber on steep terrain."},
            {"name": "Willamette Complex (Oakridge Lightning Fires)", "year": 2024, "acres": 5000,
             "details": "Multiple lightning-caused fires 8-22 miles from Oakridge. Level 2 evacuations "
                        "for Oakridge and Westfir. Demonstrated pattern of recurrent fire threat."},
            {"name": "Bedrock Fire", "year": 2023, "acres": 200,
             "details": "Fall Creek area on Middle Fork District. Active near town."},
            {"name": "Tumblebug Fire", "year": 2009, "acres": 4000,
             "details": "Burned on Middle Fork Ranger District; dead snags from this fire created "
                        "increased fuel loading for subsequent fires."},
        ],
        "evacuation_routes": [
            {"route": "OR-58 West (toward Eugene/Springfield)", "direction": "W", "lanes": 2,
             "bottleneck": "Two-lane highway through narrow Willamette valley for 40 miles to Eugene. "
                          "Passes through forested corridor with fire risk the entire distance.",
             "risk": "Sole primary evacuation route. Repeatedly closed by fires (2023-2025). When Hwy 58 "
                     "closes, Oakridge is effectively stranded with no viable alternative route."},
            {"route": "OR-58 East (toward Willamette Pass/US-97)", "direction": "E", "lanes": 2,
             "bottleneck": "Climbs to Willamette Pass (5,128 ft); mountain road through dense forest",
             "risk": "Secondary route; leads deeper into forest. Passes through areas of recurrent fire. "
                     "Connects to US-97 at Chemult (65 miles). Winter closures."},
            {"route": "Forest Roads", "direction": "N/S", "lanes": 1,
             "bottleneck": "Unpaved forest roads; not suitable for passenger vehicles or mass evacuation",
             "risk": "Dead-end forest roads leading to trailheads; potential fire traps."},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Valley funneling effect concentrates winds along the Middle Fork Willamette "
                "and OR-58 corridor. East wind events push fire from Cascades down the valley "
                "toward town. Afternoon upvalley thermal winds in summer can push fire eastward "
                "into surrounding forest. Multiple tributary drainages create complex wind "
                "interactions. Heavy fuel loading from bark beetle mortality and previous fire "
                "snags amplify fire behavior."
            ),
            "critical_corridors": [
                "Middle Fork Willamette valley — primary fire corridor; wind channeling during east wind events",
                "Salmon Creek and Salt Creek drainages — fire pathways from Cascade foothills into town",
                "OR-58 highway corridor — fire can race along road through continuous forest; sole escape route",
                "Previous burn scars (Tumblebug 2009) — heavy snag loading creates extreme fire behavior zones",
            ],
            "rate_of_spread_potential": (
                "In dense Douglas-fir/hemlock forest on steep slopes: 50-150 chains/hr surface fire, "
                "200-300 chains/hr crown fire runs. Previous burn scars with heavy snag loading "
                "create unpredictable fire behavior — snag fall, spot fires, and jackpot burning. "
                "Continuous fuel from forest floor to canopy enables rapid transition to crown fire."
            ),
            "spotting_distance": (
                "1-3 miles in steep terrain with strong updrafts from canyon walls. Dense "
                "Douglas-fir canopy produces massive ember showers during crown fire. "
                "Valley geometry concentrates embers in the narrow corridor where town sits."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Small municipal water system; vulnerable to contamination from fire in surrounding "
                "watershed. Limited storage capacity. Power-dependent pumping."
            ),
            "power": (
                "Lane Electric Cooperative; overhead lines through forested canyon. "
                "Fire-related outages common and extended. Single transmission corridor "
                "means any fire event can black out the community."
            ),
            "communications": (
                "Limited cell coverage in valley and surrounding forest. Lane County 911. "
                "Emergency alerts depend on power and cell service, both vulnerable during fire. "
                "Remote location means delayed emergency response."
            ),
            "medical": (
                "No hospital. Small community health clinic. Nearest hospital: PeaceHealth "
                "Sacred Heart at RiverBend in Springfield (40 miles west). During Hwy 58 closure, "
                "community is completely isolated from hospital care. Air ambulance grounded by smoke."
            ),
        },
        "demographics_risk_factors": {
            "population": 3206,
            "seasonal_variation": (
                "Mountain biking tourism (Oakridge is known as 'Mountain Biking Capital of Oregon') "
                "and camping/fishing bring summer visitors. Some seasonal timber workers. "
                "Population relatively stable year-round."
            ),
            "elderly_percentage": "~22% over 65",
            "mobile_homes": (
                "25.4% of housing is manufactured homes — one of the highest rates in Oregon. "
                "Many on forested lots with poor defensible space. Aging housing stock "
                "(median construction year 1959). Critical vulnerability."
            ),
            "special_needs_facilities": (
                "Very limited. No pharmacy in town as of recent years. Senior center. "
                "Poverty rate ~30%, median household income ~$35,000. Limited transportation "
                "for elderly and disabled. Environmental justice concern — isolated, low-income "
                "community with extreme fire risk."
            ),
        },
    },

    # =========================================================================
    # 13. SUNRIVER, OR — Resort Community in Deschutes NF
    # =========================================================================
    "sunriver_or": {
        "center": [43.8834, -121.4371],
        "terrain_notes": (
            "Sunriver (~4,164 ft) is a master-planned resort community approximately 15 miles "
            "south of Bend, entirely surrounded by Deschutes National Forest ponderosa pine "
            "forest. Originally a WWII military training camp (Camp Abbot, 1943), the community "
            "was developed as a resort in 1968 and now features ~4,600 homes, a lodge, golf "
            "courses, an airstrip (S21), and extensive recreation facilities. The community is "
            "built within the forest — large ponderosa pines stand in yards and line every "
            "street. The Deschutes River runs along the western boundary. Despite the resort "
            "character, approximately 2,000 people live year-round, with the effective population "
            "swelling to 10,000-30,000 during summer weekends and holidays. The community has "
            "invested significantly in wildfire preparedness through its Community Wildfire "
            "Protection Plan (CWPP) and prescribed burning programs, but the fundamental "
            "vulnerability of thousands of structures embedded in continuous forest remains."
        ),
        "key_features": [
            {"name": "Deschutes National Forest", "bearing": "All directions", "type": "national_forest",
             "notes": "1.6 million acres surrounds community; continuous ponderosa pine forest to boundary"},
            {"name": "Deschutes River", "bearing": "W boundary", "type": "river",
             "notes": "Runs along west side; provides partial fire break but riparian vegetation is fuel"},
            {"name": "Sunriver Airport (S21)", "bearing": "N end", "type": "airport",
             "notes": "3,600 ft paved runway; emergency aircraft access but smoke can close the field"},
            {"name": "Mt. Bachelor", "bearing": "W (15 miles)", "type": "volcanic_peak",
             "notes": "Ski area in national forest; Bachelor Complex Fire (2024) threatened Sunriver from this direction"},
            {"name": "SHARC Recreation Center", "bearing": "Central", "type": "recreation",
             "notes": "$18M aquatic center; potential emergency shelter. 1.4 million visitors in first 5 years."},
            {"name": "Spring River / Fall River", "bearing": "S", "type": "natural_springs",
             "notes": "Spring-fed rivers in forested areas south of resort; fire corridors from south"},
        ],
        "elevation_range_ft": [4100, 4250],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "Bachelor Complex (Little Lava Fire)", "year": 2024, "acres": 2500,
             "details": "Largest fire in Bachelor Complex; threatened Sunriver directly. Level 2 'Get Set' "
                        "evacuation notices issued for Sunriver borders. Multiple fires in Deschutes NF "
                        "threatened community from W and SW."},
            {"name": "Darlene 3 Fire", "year": 2024, "acres": 3900,
             "details": "Burned in Deschutes NF near La Pine; over 1,000 homes on evacuation alert. "
                        "Close proximity to Sunriver demonstrated regional fire exposure."},
            {"name": "Sunriver vicinity fires", "year": 2020, "acres": 100,
             "details": "Multiple small fires during Labor Day east wind event; increased monitoring but "
                        "community was spared direct impact."},
        ],
        "evacuation_routes": [
            {"route": "South Century Drive to US-97", "direction": "N toward Bend", "lanes": 2,
             "bottleneck": "Single access road from resort to US-97; 4,600 homes funneling through limited exits",
             "risk": "Primary evacuation route; passes through national forest. If fire cuts S Century Drive, "
                     "community could be trapped. 10,000-30,000 summer visitors create massive evacuation demand."},
            {"route": "Sunriver-to-La Pine via US-97 South", "direction": "S", "lanes": 2,
             "bottleneck": "Two-lane highway through continuous forest; La Pine also evacuating",
             "risk": "Secondary route south; shared with La Pine evacuees. Forest on both sides of highway."},
            {"route": "Forest Service Roads", "direction": "W", "lanes": 1,
             "bottleneck": "Unpaved forest roads; not suitable for mass evacuation of resort",
             "risk": "Emergency-only routes into forest; potential fire traps rather than evacuation routes."},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Summer afternoon SW winds push fires from Cascade foothills toward community. "
                "East wind events drive fires across flat pine terrain toward the Cascades. "
                "Relatively flat topography allows fire to approach from any direction. "
                "Diurnal thermal patterns create complex wind shifts. Resort is nestled in "
                "the forest with no significant wind breaks."
            ),
            "critical_corridors": [
                "Deschutes River corridor — fire spread pathway along western boundary",
                "South Century Drive / US-97 — evacuation route also serves as fire corridor",
                "Mt. Bachelor / Cascade Lakes area — fire approaches from SW through continuous forest",
                "La Pine direction — fire can approach from south through lodgepole/ponderosa",
            ],
            "rate_of_spread_potential": (
                "In ponderosa pine with grass understory: 50-150 chains/hr surface fire, "
                "200+ chains/hr with wind-driven crown runs. Within the resort, structure-to-"
                "structure spread possible due to tree canopy connecting homes. Well-maintained "
                "defensible space in core resort helps but edges are most vulnerable."
            ),
            "spotting_distance": (
                "0.5-1.5 miles in ponderosa; large bark plates produce firebrands. "
                "Many homes have wood shake roofs (older construction) highly vulnerable "
                "to ember ignition. CWPP has identified this as priority for mitigation."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Sunriver Utilities Company provides water from groundwater wells. Adequate "
                "for normal operations but fire flow demand during a community-wide event "
                "would overwhelm capacity. Power-dependent pumping."
            ),
            "power": (
                "Central Electric Cooperative and Midstate Electric Cooperative; overhead "
                "lines through forest. Fire-related outages can be extended. Limited backup "
                "generation for critical facilities."
            ),
            "communications": (
                "Cell coverage good within resort; degrades in surrounding forest. "
                "Deschutes County emergency alerts functional. Sunriver has internal "
                "communication systems (owner association notifications)."
            ),
            "medical": (
                "Sunriver has a small urgent care clinic (seasonal). No hospital; nearest is "
                "St. Charles Bend (20 miles north). During mass evacuation, medical transport "
                "competes with evacuee traffic on same roads."
            ),
        },
        "demographics_risk_factors": {
            "population": 2023,
            "seasonal_variation": (
                "EXTREME seasonal variation: year-round population ~2,000 but summer weekends "
                "can exceed 30,000 (vacation rentals, resort guests, day visitors). Peak fire "
                "season coincides exactly with peak occupancy. Many visitors unfamiliar with "
                "evacuation routes, not registered for alerts, and may not speak English."
            ),
            "elderly_percentage": "~40-50% over 65 (median age 70.1 — retirement community)",
            "mobile_homes": "Minimal; resort community with primarily permanent single-family structures.",
            "special_needs_facilities": (
                "Extremely elderly population (median age 70.1). Multiple residents with mobility "
                "limitations. No hospital or emergency medical facilities in community. "
                "K-8 school in community; children present during school year."
            ),
        },
    },

    # =========================================================================
    # 14. CAMP SHERMAN, OR — Metolius River, Surrounded by Forest
    # =========================================================================
    "camp_sherman_or": {
        "center": [44.4641, -121.6383],
        "terrain_notes": (
            "Camp Sherman (~2,963 ft) is a tiny unincorporated community in Jefferson County, "
            "nestled along the headwaters of the Metolius River approximately 15 miles northwest "
            "of Sisters. The community of ~250 year-round residents occupies 3.15 square miles "
            "of ponderosa pine forest within the Deschutes National Forest. Access is via Forest "
            "Road 14 off Highway 20, then Forest Road 1419 — approximately 12 miles from the "
            "nearest highway. The community is classified as 'extreme' fire risk in the Sisters "
            "Wildfire Protection Plan, with heavy fuel pockets to the west and north capable of "
            "promoting extreme fire behavior. The Metolius River, one of Oregon's most celebrated "
            "spring-fed streams, emerges from the base of Black Butte nearby. The surrounding "
            "forest has a history of fire suppression leading to dense understory accumulation. "
            "Nearly 20 large fires have threatened the greater Sisters/Camp Sherman area since "
            "1994, and the community was evacuated during the 2003 B&B Complex Fire."
        ),
        "key_features": [
            {"name": "Metolius River", "bearing": "Through community", "type": "spring_fed_river",
             "notes": "Iconic spring-fed river emerging from base of Black Butte; riparian corridor provides some fuel break"},
            {"name": "Black Butte", "bearing": "SE", "type": "volcanic_peak",
             "notes": "6,436 ft cinder cone; fire lookout tower. Dense forest on slopes connects to community."},
            {"name": "Green Ridge", "bearing": "E", "type": "ridgeline",
             "notes": "Prominent forested ridge; Green Ridge Fire (2020) threatened Camp Sherman from this direction"},
            {"name": "Mt. Jefferson Wilderness", "bearing": "NW", "type": "wilderness",
             "notes": "111,177 acres; B&B Complex Fire originated in this wilderness. No suppression until boundary."},
            {"name": "Deschutes National Forest", "bearing": "All directions", "type": "national_forest",
             "notes": "Community completely surrounded by national forest; no defensible perimeter"},
            {"name": "Forest Road 14 / 1419", "bearing": "SE to Hwy 20", "type": "access_road",
             "notes": "Only access road; ~12 miles of forest road to Highway 20. Single-point failure for evacuation."},
        ],
        "elevation_range_ft": [2900, 3100],
        "wui_exposure": "extreme",
        "historical_fires": [
            {"name": "B&B Complex Fire", "year": 2003, "acres": 90769,
             "details": "Two lightning-caused fires that burned 90,769 acres in central Cascades. "
                        "Camp Sherman was evacuated (~300 people). Fire burned ponderosa, lodgepole, "
                        "and Douglas-fir on both sides of Cascades. Cost $38.7M to suppress. "
                        "13 structures destroyed region-wide. Changed fire management philosophy."},
            {"name": "Green Ridge Fire", "year": 2020, "acres": 1000,
             "details": "During Labor Day east wind event. Fire on Green Ridge east of Camp Sherman "
                        "forced evacuation notices. Demonstrated ongoing vulnerability."},
            {"name": "Black Crater Fire", "year": 2006, "acres": 9300,
             "details": "Burned west of Sisters near Black Crater. Threatened broader Sisters/Camp Sherman area."},
        ],
        "evacuation_routes": [
            {"route": "Forest Road 14 South to Hwy 20", "direction": "SE", "lanes": 2,
             "bottleneck": "12 miles of paved forest road through continuous pine forest; ONLY road out. "
                          "Single-lane in sections. No alternative routes.",
             "risk": "CRITICAL: Single point of failure. If fire cuts FR 14, community is completely trapped. "
                     "Road passes through dense forest the entire distance. During B&B Complex evacuation, "
                     "residents drove through smoke on this road."},
            {"route": "Forest Roads North/West", "direction": "N/W", "lanes": 1,
             "bottleneck": "Unpaved forest roads; many are dead ends or lead to wilderness trailheads",
             "risk": "Not viable evacuation routes; lead deeper into forest and wilderness. "
                     "Could become fire traps. Some seasonal closures."},
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Eastern Cascade foothills experience afternoon SW thermal winds in summer and "
                "periodic strong east wind events. The Metolius Basin creates local wind effects "
                "— cold air from the spring-fed river creates inversions that can trap smoke. "
                "During east wind events, fire approaches rapidly from the west (Cascades). "
                "Sisters CWPP rated Camp Sherman 'extreme risk' for fire behavior potential."
            ),
            "critical_corridors": [
                "Forest Road 14 corridor — sole access road through continuous ponderosa forest",
                "Green Ridge — elevated terrain to east; fire can descend toward community",
                "Metolius River drainage — northward fire corridor from Black Butte area",
                "Mt. Jefferson Wilderness approach — B&B Complex fire demonstrated this corridor",
            ],
            "rate_of_spread_potential": (
                "In ponderosa pine with heavy understory: 50-150 chains/hr surface fire, "
                "200+ chains/hr wind-driven crown fire. B&B Complex demonstrated sustained "
                "runs of 5,000+ acres/day in extreme conditions. Dense fuel pockets to west "
                "and north ('heavy pockets capable of extreme fire behavior' per CWPP) could "
                "produce fire intensity exceeding suppression capability."
            ),
            "spotting_distance": (
                "1-2 miles in ponderosa crown fire; bark plates and cones are effective "
                "firebrands. Community buildings and cabins — many with wood construction — "
                "are interspersed in forest canopy. FireFree program has improved some "
                "defensible space but forest connectivity remains continuous."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Private wells and small community water systems; no municipal water. "
                "Power-dependent pumping. Metolius River spring-fed flow is reliable but "
                "not connected to community fire suppression. No fire hydrant system."
            ),
            "power": (
                "Central Electric Cooperative; overhead lines along Forest Road 14 through "
                "12 miles of forest. Single-corridor power supply. Extended outages during "
                "fire events. No backup generation for most residences."
            ),
            "communications": (
                "Very limited cell coverage; forested canyon terrain blocks signals. "
                "Sisters-Camp Sherman Fire District covers the area. Emergency alerts "
                "dependent on power and cell service — both fail simultaneously during fire events."
            ),
            "medical": (
                "No medical facilities. Nearest clinic in Sisters (15 miles). Nearest hospital "
                "in Bend (35 miles). Single access road means any road closure completely "
                "isolates community from medical care."
            ),
        },
        "demographics_risk_factors": {
            "population": 251,
            "seasonal_variation": (
                "Summer recreation (Metolius River fishing, camping, hiking) can triple "
                "effective population. Resort lodges (Lake Creek Lodge, Metolius River Resort) "
                "bring visitors. USFS campgrounds along Metolius add 500+ seasonal occupants. "
                "Many vacation homes occupied only seasonally."
            ),
            "elderly_percentage": "~30% over 65 (retirement/vacation community)",
            "mobile_homes": (
                "Minimal manufactured housing. Most structures are cabins and single-family homes, "
                "many older wood construction with shake roofs — highly ignitable."
            ),
            "special_needs_facilities": (
                "None. No pharmacy, clinic, or senior services. Community entirely dependent "
                "on Sisters (15 miles) for basic services and Bend (35 miles) for hospital care. "
                "Elderly population with potential mobility limitations in very remote setting."
            ),
        },
    },
}
