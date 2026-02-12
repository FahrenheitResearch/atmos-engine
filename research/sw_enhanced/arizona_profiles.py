"""
Enhanced fire-vulnerable city profiles for Arizona.

Each entry contains expert-level terrain analysis, historical fire data,
evacuation route details, infrastructure vulnerabilities, and demographic
risk factors for 15 fire-vulnerable communities across the state.
"""

AZ_ENHANCED = {

    # =========================================================================
    # 1. PRESCOTT / PRESCOTT VALLEY
    # =========================================================================
    "prescott_az": {
        "center": (34.540, -112.468),
        "terrain_notes": (
            "Prescott and Prescott Valley sit in a high-desert basin at roughly 5,200-5,400 ft "
            "elevation, rimmed by the Bradshaw Mountains to the south and east, the Sierra Prieta "
            "range to the west, and the Granite Dells formation to the northeast. The surrounding "
            "terrain is a mosaic of ponderosa pine at higher elevations transitioning to pinyon-juniper "
            "woodland, interior chaparral, and dense manzanita-oak brush on mid-elevation slopes. "
            "Chaparral fields on south- and west-facing slopes are particularly fire-prone, capable "
            "of producing 20-30 ft flame lengths under wind-driven conditions. The city's western "
            "flank abuts Prescott National Forest directly, creating an abrupt wildland-urban "
            "interface where homes intermix with volatile brush fuels. Thumb Butte (6,514 ft) "
            "anchors the western skyline and channels afternoon upslope winds through saddles "
            "that can accelerate fire spread toward residential areas. Granite Mountain (7,626 ft) "
            "to the northwest is surrounded by dense chaparral identical to the fuels that drove "
            "the Yarnell Hill Fire tragedy. The Granite Dells area northeast of Prescott features "
            "exposed granitic boulder fields interspersed with grassland that can carry fire rapidly "
            "in spring wind events. Prescott Valley, at slightly lower elevation in Lonesome Valley, "
            "faces fire encroachment from the Mingus Mountain complex to the east and Bradshaw "
            "foothills to the south. Seasonal drought patterns from April through late June create "
            "critical fire weather windows when live fuel moistures in chaparral drop below 60% "
            "and fine dead fuel moistures reach 3-5%, conditions under which spotting distances "
            "can exceed one mile. Terrain-driven wind channeling through Lynx Creek, Bannon Creek, "
            "and Granite Creek drainages creates preferential fire pathways directly into developed areas."
        ),
        "key_features": [
            {"name": "Thumb Butte", "bearing": "W", "distance_mi": 3,
             "type": "mountain", "notes": "6,514 ft volcanic plug; channels upslope winds toward city; Prescott NF trailhead area with heavy recreation use"},
            {"name": "Granite Mountain", "bearing": "NW", "distance_mi": 8,
             "type": "mountain", "notes": "7,626 ft; dense chaparral surrounds; site of Granite Mountain Hotshots memorial trail; fire-prone terrain"},
            {"name": "Bradshaw Mountains", "bearing": "S", "distance_mi": 5,
             "type": "mountain_range", "notes": "Rugged range to 7,900 ft with steep chaparral-covered slopes; Senator Highway traverses; Crown King access"},
            {"name": "Granite Dells", "bearing": "NE", "distance_mi": 4,
             "type": "geological_feature", "notes": "Exposed granitic boulders with interspersed grassland; Watson and Willow Lakes; fire can spread through grass corridors"},
            {"name": "Sierra Prieta Range", "bearing": "W", "distance_mi": 6,
             "type": "mountain_range", "notes": "Steep western rampart rising to 7,100+ ft; dense chaparral belt; Doce Fire 2013 burned along this front"},
        ],
        "elevation_range_ft": (5100, 7626),
        "wui_exposure": (
            "extreme -- Prescott's western and southern neighborhoods directly abut Prescott National "
            "Forest with no defensible buffer. Subdivisions like Hassayampa Village, Timber Ridge, "
            "Williamson Valley, and Forest Trails intermix with chaparral and pine fuels. Prescott "
            "Valley's southern fringe extends into Bradshaw Mountain foothills. Over 15,000 homes "
            "are within 1 mile of wildland fuels."
        ),
        "historical_fires": [
            {
                "name": "Indian Fire",
                "year": 2002,
                "acres": 1365,
                "structures_destroyed": 7,
                "fatalities": 0,
                "cause": "human",
                "notes": (
                    "Burned within and adjacent to Prescott city limits on May 15, 2002. "
                    "Forced evacuation of 2,500 residents. Demonstrated the extreme WUI "
                    "risk when fire enters the chaparral belt directly abutting neighborhoods. "
                    "Suppression costs reached $1.2 million with total losses near $3 million."
                ),
            },
            {
                "name": "Doce Fire",
                "year": 2013,
                "acres": 6767,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "human",
                "notes": (
                    "Burned west of Prescott in the Sierra Prieta range in June 2013. "
                    "Granite Basin Homes, Sundown Acres, Old Stage Acres evacuated. "
                    "Nearly 500 firefighters deployed. The Granite Mountain Hotshots "
                    "worked this fire shortly before the Yarnell Hill tragedy."
                ),
            },
            {
                "name": "Goodwin Fire",
                "year": 2017,
                "acres": 28516,
                "structures_destroyed": 17,
                "fatalities": 0,
                "cause": "unknown",
                "notes": (
                    "Ignited June 24, 2017 in the Bradshaw Mountains 14 miles SE of Prescott. "
                    "Grew from 150 to 25,000 acres in 5 days. Mayer and Breezy Pines evacuated. "
                    "19 additional structures damaged. $15 million suppression cost."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "SR-89",
                "direction": "south toward Wickenburg / Phoenix",
                "lanes": 2,
                "bottleneck": "Yarnell Hill grade -- winding descent with 1,300 ft elevation drop in 4 miles",
                "risk": "Single two-lane route south; can be cut off by fire in Peoples Valley or Yarnell area",
            },
            {
                "route": "SR-89A",
                "direction": "north to Chino Valley / Ash Fork / I-40",
                "lanes": 2,
                "bottleneck": "Chino Valley corridor narrows; merges with SR-89 north of town",
                "risk": "Smoke from Prescott NF fires can reduce visibility to near-zero on this corridor",
            },
            {
                "route": "SR-69",
                "direction": "east to Prescott Valley and I-17 via SR-169",
                "lanes": 4,
                "bottleneck": "Mingus Mountain area; merges to 2 lanes approaching Dewey-Humboldt",
                "risk": "Primary east corridor; high traffic volume during evacuations",
            },
            {
                "route": "SR-89A (south)",
                "direction": "south through Bradshaw Mountains toward Crown King / I-17",
                "lanes": 2,
                "bottleneck": "Senator Highway is unpaved beyond Palace Station; impassable in wet weather",
                "risk": "Not a viable mass evacuation route; 4WD required",
            },
        ],
        "fire_spread_characteristics": (
            "Fires in the Prescott area are driven primarily by chaparral fuels on south and west "
            "aspects, with flame lengths routinely reaching 20-30 ft. Wind-driven fires in the "
            "Bradshaw foothills produce extreme rates of spread (ROS) up to 5-10 mph in heavy "
            "chaparral. Upslope afternoon winds channel through creek drainages (Lynx, Bannon, "
            "Granite) into developed areas. Crown fire in ponderosa pine at higher elevations "
            "generates massive ember showers with spotting distances exceeding 1 mile. Dry "
            "thunderstorm outflows in June can shift fire direction 180 degrees within minutes, "
            "as occurred during the Yarnell Hill tragedy 35 miles south."
        ),
        "infrastructure_vulnerabilities": (
            "Prescott's water supply depends on surface reservoirs (Watson, Willow, Goldwater, Lynx) "
            "that are vulnerable to watershed contamination from post-fire runoff and debris flows. "
            "APS and AES power lines traverse Prescott NF on wooden poles through heavy fuel loads. "
            "Cell towers on Thumb Butte and Mingus Mountain are at direct fire risk. The Prescott "
            "Regional Airport at Ernest A. Love Field could be impacted by smoke. Natural gas "
            "infrastructure serves much of the metro area through above-ground segments in WUI zones."
        ),
        "demographics_risk_factors": (
            "Combined Prescott/Prescott Valley metro population exceeds 90,000. High proportion of "
            "retirees (median age ~55) with potential mobility limitations. Significant seasonal "
            "tourism population in summer months swells traffic. Many rural properties on the "
            "outskirts lack defensible space. Volunteer fire departments serve outlying areas "
            "with limited staffing. Large homeless population camps in Prescott NF increase "
            "ignition risk."
        ),
    },

    # =========================================================================
    # 2. FLAGSTAFF
    # =========================================================================
    "flagstaff_az": {
        "center": (35.198, -111.651),
        "terrain_notes": (
            "Flagstaff occupies a high volcanic plateau at 6,900-7,200 ft elevation on the southern "
            "edge of the Colorado Plateau, surrounded by the largest contiguous ponderosa pine forest "
            "in North America. The San Francisco Peaks, Arizona's highest mountains at 12,633 ft "
            "(Humphreys Peak), rise immediately north of the city and are flanked by dense mixed "
            "conifer and spruce-fir forests. Mount Elden (9,301 ft) sits directly northeast of "
            "downtown, separated from residential areas by less than one mile of continuous forest "
            "fuels. The city is built within and around multiple volcanic features including "
            "cinder cones, lava flows, and volcanic meadows that create complex terrain interactions "
            "with wind and fire. Steep slopes on Mount Elden's south face produce extreme upslope "
            "fire behavior during afternoon heating, as demonstrated by the 2019 Museum Fire which "
            "burned to within one mile of homes. Dry Lakebeds (ephemeral meadows) between cinder "
            "cones can funnel winds and serve as natural firebreaks or, conversely, as corridors "
            "for grass-driven fire runs. The eastern side of the city interfaces with the Doney Park "
            "and Timberline areas, where ponderosa pine transitions to pinyon-juniper woodland on "
            "volcanic cinder soils. These areas experienced catastrophic post-fire flooding after "
            "the 2010 Schultz Fire. The northern approach to Flagstaff along US-89 passes through "
            "open grassland-juniper terrain where the 2022 Tunnel Fire destroyed 30 structures. "
            "The volcanic soil and steep terrain create extreme post-fire debris flow hazards, "
            "with burn scars producing flash floods that reach residential areas within minutes "
            "of intense rainfall. Forest density averaging 800-1,200 stems per acre (versus "
            "historical 30-60 stems per acre) creates ladder fuel conditions that convert surface "
            "fires to catastrophic crown fires."
        ),
        "key_features": [
            {"name": "San Francisco Peaks", "bearing": "N", "distance_mi": 10,
             "type": "mountain", "notes": "12,633 ft; Arizona's highest; dense mixed conifer to alpine; massive fuel loads on lower slopes"},
            {"name": "Mount Elden", "bearing": "NE", "distance_mi": 2,
             "type": "mountain", "notes": "9,301 ft; steep south face directly above neighborhoods; Museum Fire 2019 burned here; extreme post-fire flood risk to Flagstaff"},
            {"name": "Dry Lake Hills", "bearing": "S", "distance_mi": 5,
             "type": "volcanic_feature", "notes": "Cinder cones and meadows south of I-40; mixed pine-juniper; fire corridor toward Kachina Village and Mountainaire"},
            {"name": "Doney Park / Sunset Crater area", "bearing": "E", "distance_mi": 8,
             "type": "volcanic_field", "notes": "Cinder cone terrain with sparse juniper; Schultz Fire flood zone; rural residential area on volcanic soils"},
            {"name": "Coconino National Forest", "bearing": "all directions", "distance_mi": 0,
             "type": "forest", "notes": "1.85 million acres surrounding Flagstaff; overly dense ponderosa pine creates extreme crown fire potential"},
        ],
        "elevation_range_ft": (6800, 12633),
        "wui_exposure": (
            "extreme -- Flagstaff is embedded within continuous ponderosa pine forest on all sides. "
            "Neighborhoods including Cheshire, Paradise, Sunnyside, Continental, Coconino Estates, "
            "and University Heights are within or directly adjacent to dense forest. The communities "
            "of Kachina Village, Mountainaire, and Munds Park to the south are islands within the "
            "forest. Over 20,000 structures are at direct wildfire risk."
        ),
        "historical_fires": [
            {
                "name": "Schultz Fire",
                "year": 2010,
                "acres": 15075,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "abandoned campfire",
                "notes": (
                    "Burned June 20-30, 2010 on Mount Elden's north and east slopes. "
                    "750 homes evacuated. No structures burned directly, but post-fire "
                    "monsoon flooding devastated Doney Park, Timberline, and Wupatki Trails "
                    "communities. Over 40 homes flooded. Estimated total cost exceeded "
                    "$133 million including flood mitigation infrastructure."
                ),
            },
            {
                "name": "Museum Fire",
                "year": 2019,
                "acres": 1961,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "human (equipment)",
                "notes": (
                    "Burned July 21 to August 12, 2019, on steep terrain just 1 mile north "
                    "of Flagstaff neighborhoods. Threatened homes in Cheshire, Paradise, "
                    "Sunnyside areas. Created new debris flow hazard above residential areas. "
                    "Post-fire flooding continued for years, requiring millions in mitigation."
                ),
            },
            {
                "name": "Tunnel Fire",
                "year": 2022,
                "acres": 19088,
                "structures_destroyed": 30,
                "fatalities": 0,
                "cause": "under investigation",
                "notes": (
                    "Burned April 17-June 1, 2022, north of Flagstaff along US-89 corridor. "
                    "766 households evacuated, over 1,000 animals displaced. 109 properties "
                    "impacted including 30 residences burned and 24 outbuildings destroyed. "
                    "Fire jumped Highway 89 and spread explosively in wind-driven conditions."
                ),
            },
            {
                "name": "Pipeline Fire",
                "year": 2022,
                "acres": 26532,
                "structures_destroyed": 2,
                "fatalities": 0,
                "cause": "human (arson)",
                "notes": (
                    "Burned June 12-25, 2022, on slopes north of Flagstaff. 690 households "
                    "ordered to evacuate, 2,410 more told to prepare. Burned through dense "
                    "ponderosa pine threatening Wupatki Trails and multiple drainages flowing "
                    "into residential areas. Created massive new post-fire flood hazard."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "I-40 West",
                "direction": "west to Williams / Kingman",
                "lanes": 4,
                "bottleneck": "I-40/I-17 interchange; heavy tourist traffic in summer",
                "risk": "Smoke from fires south of I-40 can close the interstate",
            },
            {
                "route": "I-40 East",
                "direction": "east to Winslow / Holbrook",
                "lanes": 4,
                "bottleneck": "Winona area can be impacted by fires in Walnut Canyon",
                "risk": "Limited services for 60+ miles eastbound",
            },
            {
                "route": "I-17 South",
                "direction": "south to Phoenix via Verde Valley",
                "lanes": 4,
                "bottleneck": "Oak Creek Canyon alternate (SR-89A) is narrow 2-lane; I-17 has steep grades",
                "risk": "Primary Phoenix corridor; massive evacuation traffic; fires in Munds Park area can close I-17",
            },
            {
                "route": "US-89 North",
                "direction": "north toward Page / Lake Powell",
                "lanes": 2,
                "bottleneck": "Two-lane road through open terrain; Tunnel Fire 2022 burned across this route",
                "risk": "Long distance to next city; grassland fires can jump road quickly",
            },
            {
                "route": "US-89A / SR-89A",
                "direction": "south through Oak Creek Canyon to Sedona",
                "lanes": 2,
                "bottleneck": "Narrow switchbacks descending Oak Creek Canyon; Slide Fire 2014 area",
                "risk": "Extremely vulnerable to closure; canyon acts as chimney for fire; not recommended for mass evacuation",
            },
        ],
        "fire_spread_characteristics": (
            "Crown fire in overly dense ponderosa pine (800-1,200 stems/acre vs historical 30-60) "
            "produces extreme flame lengths of 100+ ft with spotting distances exceeding 1 mile. "
            "Volcanic terrain creates complex wind interactions with upslope/downslope diurnal winds "
            "and terrain-channeled gusts through saddles between cinder cones. Dry thunderstorm "
            "outflow boundaries can drive fire rates of spread exceeding 5 mph through continuous "
            "crown fire. Post-fire debris flows are a secondary catastrophic hazard unique to "
            "Flagstaff's volcanic soil, reaching residential areas within 15-30 minutes of intense "
            "rainfall on burn scars."
        ),
        "infrastructure_vulnerabilities": (
            "City water supply is partially sourced from Upper and Lower Lake Mary, both within "
            "forested watersheds at fire risk. Inner Basin spring water supply on San Francisco "
            "Peaks is vulnerable to fire contamination. APS power lines traverse forested corridors. "
            "Cell towers on Mount Elden and Mars Hill are at direct risk. Northern Arizona University "
            "campus houses 30,000+ students. Flagstaff Medical Center is the only Level I trauma "
            "center for northern Arizona. I-17 and I-40 are critical freight corridors for the state."
        ),
        "demographics_risk_factors": (
            "City population ~76,000 with ~30,000 NAU students during academic year. Surrounding "
            "unincorporated areas add 20,000+. Heavy tourism (5+ million visitors/year to Grand "
            "Canyon corridor). Kachina Village and Mountainaire communities (4,000+ residents) are "
            "isolated forest enclaves with limited egress. Mobile home parks in Doney Park area "
            "house lower-income residents in high fire/flood risk zones. Significant Navajo and "
            "Hopi populations transit through Flagstaff."
        ),
    },

    # =========================================================================
    # 3. SEDONA / VILLAGE OF OAK CREEK
    # =========================================================================
    "sedona_az": {
        "center": (34.870, -111.761),
        "terrain_notes": (
            "Sedona sits at 4,300-4,500 ft elevation in a red-rock canyon complex where Oak Creek "
            "has carved through the Mogollon Rim escarpment. The city is dramatically enclosed by "
            "steep sandstone formations (Coconino Sandstone and Supai Formation) rising 500-2,000 ft "
            "above the town floor, with forested mesas and plateaus above. Oak Creek Canyon extends "
            "north from Sedona as a narrow, steep-walled gorge lined with dense riparian vegetation "
            "(Arizona sycamore, cottonwood, box elder) and flanked by ponderosa pine and mixed "
            "conifer on the canyon walls and rim. This canyon acts as a natural chimney that "
            "accelerates fire-driven winds and convective columns. The Wilson Mountain and "
            "Bear Mountain areas northwest of town support dense chaparral and manzanita on south "
            "aspects with pine-juniper woodland above. Village of Oak Creek, 7 miles south, sits "
            "in a broader valley surrounded by red-rock buttes and mesas with pinyon-juniper "
            "woodland extending to the community edges. The Dry Creek drainage west of Sedona "
            "channels winds from the northwest and supports dense chaparral vegetation. Terrain "
            "surrounding Sedona creates complex fire behavior: steep sandstone cliffs create "
            "updrafts and turbulence, narrow canyons funnel winds to extreme velocities, and "
            "the elevation gradient from 4,000 ft in town to 7,000+ ft on the rim supports "
            "continuous fuel beds that connect lowland fires to crown fire in upper-elevation "
            "forests. The Sycamore Canyon Wilderness to the west contains 56,000 acres of "
            "essentially untreated fuels that could produce multi-day fire runs toward Sedona."
        ),
        "key_features": [
            {"name": "Oak Creek Canyon", "bearing": "N", "distance_mi": 1,
             "type": "canyon", "notes": "15-mile steep gorge from Sedona to Flagstaff; natural fire chimney; Slide Fire 2014 burned 21,000 acres here; dense fuel loading"},
            {"name": "Wilson Mountain", "bearing": "NW", "distance_mi": 3,
             "type": "mountain", "notes": "7,122 ft; steep forested slopes above West Sedona; chaparral and pine fuels; difficult access for suppression"},
            {"name": "Sycamore Canyon Wilderness", "bearing": "W", "distance_mi": 8,
             "type": "wilderness", "notes": "56,000 acres of untreated fuels; potential for multi-day fire runs toward Sedona; limited suppression access"},
            {"name": "Mingus Mountain", "bearing": "SW", "distance_mi": 12,
             "type": "mountain", "notes": "7,815 ft; chaparral and pine; fires here can be pushed NE toward Sedona by prevailing winds"},
            {"name": "Munds Mountain Wilderness", "bearing": "E", "distance_mi": 4,
             "type": "wilderness", "notes": "24,400 acres; dense pinyon-juniper and chaparral; flanks Village of Oak Creek"},
        ],
        "elevation_range_ft": (4000, 7122),
        "wui_exposure": (
            "very high -- Sedona and the Village of Oak Creek are nestled within a canyon-mesa "
            "landscape with wildland fuels extending to property lines in many areas. West Sedona "
            "neighborhoods along Dry Creek Road interface directly with chaparral. Oak Creek Canyon "
            "communities (Slide Rock area, Indian Gardens) are completely embedded in forest. "
            "Uptown Sedona is backed against Wilson Mountain slopes. Limited defensible space "
            "in many areas due to terrain constraints."
        ),
        "historical_fires": [
            {
                "name": "Slide Fire",
                "year": 2014,
                "acres": 21150,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "human",
                "notes": (
                    "Ignited May 20, 2014, north of Slide Rock State Park in Oak Creek Canyon. "
                    "Became the largest fire in Coconino NF history at the time. 300+ structures "
                    "threatened. Full evacuation of Oak Creek Canyon from Slide Rock to Sterling "
                    "Springs. Pre-evacuation notices for Kachina Village and Forest Highlands. "
                    "840 personnel deployed with 15 hotshot crews, 33 engines, 3 air tankers."
                ),
            },
            {
                "name": "Rafael Fire",
                "year": 2021,
                "acres": 78065,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "lightning",
                "notes": (
                    "Ignited June 18, 2021, near Perkinsville west of Sedona. Grew by 18,000 acres "
                    "in a single day driven by strong winds and dry fuels. Evacuations ordered west "
                    "of Sedona. Fully contained July 15. Demonstrated the massive scale of fires "
                    "possible in the Sycamore Canyon / Verde Valley wildlands."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "SR-89A south",
                "direction": "south to Cottonwood / Camp Verde / I-17",
                "lanes": 2,
                "bottleneck": "Mingus Mountain descent is steep and winding",
                "risk": "Primary route for most evacuees; heavy tourist traffic year-round",
            },
            {
                "route": "SR-89A north",
                "direction": "north through Oak Creek Canyon to Flagstaff",
                "lanes": 2,
                "bottleneck": "Narrow canyon road with switchbacks; single lane in places; Slide Fire area",
                "risk": "Extremely vulnerable to fire closure; canyon chimney effect makes this route extremely dangerous during fire events",
            },
            {
                "route": "SR-179",
                "direction": "south to Village of Oak Creek and I-17",
                "lanes": 2,
                "bottleneck": "Single traffic circle in VOC; merges onto I-17 at Exit 298",
                "risk": "Only southern escape route for east Sedona; can be congested with tourist traffic",
            },
        ],
        "fire_spread_characteristics": (
            "Canyon-driven fire behavior dominates: Oak Creek Canyon acts as a chimney producing "
            "extreme updrafts and fire-generated winds. Chaparral on south-facing sandstone slopes "
            "produces 20-30 ft flame lengths. Pinyon-juniper woodland carries fire efficiently at "
            "moderate rates of spread (0.5-2 mph) but transitions to high-intensity crown fire when "
            "reaching pine stands on mesas above. Wind reversals from afternoon thunderstorm outflows "
            "can push fire in unexpected directions through the complex terrain. Spotting across "
            "canyon walls can establish new fire heads on opposite slopes simultaneously."
        ),
        "infrastructure_vulnerabilities": (
            "Sedona's water system depends on wells and Oak Creek surface water vulnerable to "
            "post-fire contamination. Cell towers on Wilson Mountain and Schnebly Hill at direct "
            "risk. Sedona Medical Center is a small facility; serious injuries require transport "
            "to Flagstaff or Verde Valley. Power lines traverse forested corridors from Cottonwood. "
            "Tourism infrastructure (hotels, resorts) houses thousands of visitors unfamiliar with "
            "evacuation routes."
        ),
        "demographics_risk_factors": (
            "Permanent population ~10,300 but daily tourist/visitor population can double this. "
            "Over 3 million annual visitors, many unfamiliar with area roads and fire risk. "
            "Significant retiree population in Village of Oak Creek. Oak Creek Canyon residents "
            "include seasonal cabin owners who may not be present during fire events to receive "
            "evacuation orders. Many vacation rental properties house guests with no local knowledge."
        ),
    },

    # =========================================================================
    # 4. PAYSON
    # =========================================================================
    "payson_az": {
        "center": (34.231, -111.325),
        "terrain_notes": (
            "Payson sits at approximately 4,900 ft elevation in a transitional zone at the base "
            "of the Mogollon Rim, one of the most dramatic topographic features in Arizona -- a "
            "200-mile-long escarpment rising 1,000-2,000 ft above the Tonto Basin. The Rim towers "
            "above the town to the north and east, creating a massive wall of ponderosa pine, "
            "Douglas fir, and mixed conifer forest. Below the Rim, the terrain drops through "
            "bands of pinyon-juniper woodland, interior chaparral (manzanita, scrub oak, "
            "mountain mahogany), and Sonoran desert scrub. This vertical zonation of fuels means "
            "fires can transition rapidly from brush to timber as they move upslope, or from "
            "crown fire to chaparral fire moving downslope toward town. The East Verde River "
            "and Tonto Creek drainages cut deep canyons through the Rim country, creating "
            "natural fire corridors with extreme terrain-driven fire behavior. The Rim itself "
            "produces powerful afternoon upslope winds that can drive fires at extreme rates. "
            "Conversely, cold front passages produce strong downslope winds off the Rim that push "
            "fire toward Payson. Pine Creek canyon southeast of town is rated among the top 10 "
            "areas in the US for catastrophic wildfire potential due to specific topographic "
            "features that produce extreme fire behavior. The surrounding Tonto National Forest "
            "contains vast areas of overly dense timber and brush that have missed multiple "
            "historical fire cycles, creating fuel loads far exceeding historical norms. The "
            "Highline Trail area north of town follows the base of the Rim through continuous "
            "fuel beds that connect Payson's fire risk to communities 50+ miles in either direction."
        ),
        "key_features": [
            {"name": "Mogollon Rim", "bearing": "N", "distance_mi": 5,
             "type": "escarpment", "notes": "200-mile limestone escarpment rising 1,000-2,000 ft; massive ponderosa pine forest above; drives powerful upslope and downslope winds"},
            {"name": "East Verde River Canyon", "bearing": "NE", "distance_mi": 4,
             "type": "canyon", "notes": "Deep canyon cutting through Rim country; natural fire corridor; channeling terrain winds"},
            {"name": "Diamond Point", "bearing": "N", "distance_mi": 12,
             "type": "mountain", "notes": "7,038 ft; above the Rim; Dude Fire burned below this area in 1990"},
            {"name": "Tonto Creek drainage", "bearing": "E", "distance_mi": 8,
             "type": "canyon", "notes": "Major drainage from Rim to Roosevelt Lake; carries fire through continuous fuel beds"},
            {"name": "Mazatzal Mountains", "bearing": "SW", "distance_mi": 15,
             "type": "mountain_range", "notes": "Rugged range to 7,903 ft; dense chaparral; Mazatzal Wilderness; fire smoke often impacts Payson"},
        ],
        "elevation_range_ft": (4800, 7800),
        "wui_exposure": (
            "very high -- Payson is surrounded by Tonto National Forest on three sides. Northern "
            "neighborhoods extend to the base of the Rim in continuous fuel beds. Eastern "
            "subdivisions along Houston Mesa Road interface directly with pine-juniper woodland. "
            "Rural properties along East Verde River and in Christopher Creek are fully embedded "
            "in forest. Town population of 16,000+ is concentrated in a narrow valley."
        ),
        "historical_fires": [
            {
                "name": "Dude Fire",
                "year": 1990,
                "acres": 24174,
                "structures_destroyed": 63,
                "fatalities": 6,
                "cause": "lightning",
                "notes": (
                    "Ignited June 25, 1990, beneath the Mogollon Rim 10 miles NE of Payson "
                    "during one of the hottest months in Arizona history (106F in Payson, 122F "
                    "in Phoenix). Killed 6 firefighters -- 5 inmates and 1 supervisor from "
                    "Perryville State Prison -- in Walk Moore Canyon when a plume-dominated fire "
                    "overran their position. Dry thunderstorm blasted the firestorm in four "
                    "directions simultaneously. Destroyed the historic Zane Grey cabin and 63 "
                    "structures. Grew from 5 acres to nearly 30,000 across three national forests. "
                    "Led to major reforms in firefighter safety equipment and communications."
                ),
            },
            {
                "name": "Backbone Fire",
                "year": 2021,
                "acres": 40855,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "lightning",
                "notes": (
                    "Ignited June 16, 2021, 12 miles west of Strawberry near Fossil Creek. "
                    "Burned 40,855 acres across Yavapai, Gila, and Coconino counties. "
                    "Evacuations ordered for Strawberry and Pine. SR-260 and SR-87 closed. "
                    "Rim Country Middle School in Payson served as evacuation center. "
                    "Fully contained July 19, 2021. No structures lost."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "SR-87 (Beeline Highway)",
                "direction": "south to Mesa / Phoenix (90 miles)",
                "lanes": 2,
                "bottleneck": "Steep winding descent through Mazatzal Mountains; single-lane segments",
                "risk": "Primary Phoenix corridor; extremely congested during evacuations; fire can close road in Slate Creek area",
            },
            {
                "route": "SR-260 West",
                "direction": "west to Camp Verde / I-17",
                "lanes": 2,
                "bottleneck": "Narrow two-lane through Star Valley; descends through Fossil Creek area",
                "risk": "Backbone Fire 2021 closed this route; fire in Fossil Creek/Verde River area blocks evacuation",
            },
            {
                "route": "SR-260 East",
                "direction": "east to Heber-Overgaard / Show Low (90 miles)",
                "lanes": 2,
                "bottleneck": "Rim Road climb to 7,500 ft; two-lane through dense forest",
                "risk": "Enters the heart of the Rim country fire corridor; Rodeo-Chediski area",
            },
            {
                "route": "SR-87 North",
                "direction": "north to Winslow via Clints Well and Lake Mary Road",
                "lanes": 2,
                "bottleneck": "Long remote stretch through dense forest; limited services",
                "risk": "Passes through heavy fuel loads on the Rim; rarely used evacuation route",
            },
        ],
        "fire_spread_characteristics": (
            "Rim-driven fire dynamics dominate: powerful afternoon upslope winds push fire up the "
            "2,000 ft Rim escarpment at extreme rates, producing massive convective columns visible "
            "for 100+ miles. Plume-dominated fires can generate their own weather, with erratic "
            "winds exceeding 60 mph. The Dude Fire demonstrated that dry thunderstorm outflows "
            "can blast fire in multiple directions simultaneously at 5-10 mph ROS through dense "
            "chaparral and pine. Topographic channeling through canyons (East Verde, Tonto Creek, "
            "Pine Creek) accelerates fire and funnels it toward developed areas. Night inversions "
            "in the valleys trap smoke and create extreme visibility hazards."
        ),
        "infrastructure_vulnerabilities": (
            "Payson's water supply from Blue Ridge Reservoir and C.C. Cragin Reservoir depends on "
            "a 40-mile pipeline through Rim country forest. Power lines from the north traverse "
            "heavy forest. Payson Regional Medical Center is small; major trauma requires helicopter "
            "transport to Phoenix. Cell towers on the Rim are at direct fire risk. Natural gas "
            "is not available; propane tanks at rural homes create explosion hazards."
        ),
        "demographics_risk_factors": (
            "Population ~16,400 (2020 census) but summer weekend population can reach 40,000+ "
            "with Valley residents escaping Phoenix heat. High retiree proportion with mobility "
            "limitations. Rural properties along the Rim and in East Verde corridor have limited "
            "access. Christopher Creek and Tonto Village are isolated communities dependent on "
            "SR-260. Many properties lack defensible space clearance."
        ),
    },

    # =========================================================================
    # 5. SHOW LOW / PINETOP-LAKESIDE
    # =========================================================================
    "show_low_az": {
        "center": (34.254, -110.030),
        "terrain_notes": (
            "Show Low and Pinetop-Lakeside are situated on the Mogollon Rim at 6,300-7,200 ft "
            "elevation in the heart of the Apache-Sitgreaves National Forests, surrounded by one "
            "of the densest ponderosa pine forests in Arizona. The terrain is a gently rolling "
            "volcanic plateau dissected by shallow drainages (Show Low Creek, Timber Creek, Billy "
            "Creek) that flow northeast toward the Little Colorado River. Unlike the dramatic Rim "
            "escarpment near Payson, the landscape here is a vast continuous forest extending "
            "50+ miles in all directions. This creates an enormous fire-fuel complex with no "
            "natural barriers to fire spread. The communities are connected by SR-260, a two-lane "
            "highway corridor that serves as both the commercial spine and primary evacuation route. "
            "Forest density in the region averages 600-1,000 stems per acre, with heavy downed "
            "woody debris from bark beetle kill and decades of fire suppression. The White Mountain "
            "Apache Reservation borders the communities to the south, and fires originating on "
            "tribal land (as with the Rodeo fire in 2002) can reach city limits within hours "
            "under wind-driven conditions. Pinetop-Lakeside is particularly vulnerable due to "
            "its forest-embedded layout, with ponderosa pines growing within 20 ft of many "
            "structures. Show Low's southern edge interfaces with dense forest along Show Low "
            "Creek. The Heber-Overgaard area 30 miles west is connected by SR-260 through "
            "continuous forest, and fire can travel this entire corridor. Fuel moisture monitoring "
            "stations consistently show this area reaching critical fire danger thresholds by "
            "mid-May, with the highest risk from May through early July before monsoon onset."
        ),
        "key_features": [
            {"name": "White Mountains", "bearing": "S", "distance_mi": 10,
             "type": "mountain_range", "notes": "Extends to 11,420 ft (Mount Baldy); dense mixed conifer and spruce-fir; Wallow Fire origin area"},
            {"name": "Mogollon Rim", "bearing": "SW", "distance_mi": 15,
             "type": "escarpment", "notes": "Rim crest at 7,500+ ft; continuous forest connects Show Low to Payson fire corridor"},
            {"name": "White Mountain Apache Reservation", "bearing": "S", "distance_mi": 3,
             "type": "tribal_land", "notes": "Fort Apache Reservation; Rodeo fire in 2002 originated here; limited federal suppression coordination"},
            {"name": "Fool Hollow Lake", "bearing": "NW", "distance_mi": 3,
             "type": "lake", "notes": "Recreation area surrounded by pine forest; potential fire break but limited width"},
            {"name": "Show Low Creek drainage", "bearing": "N", "distance_mi": 1,
             "type": "drainage", "notes": "Riparian corridor through town; carries fire pathway from surrounding forest into commercial/residential areas"},
        ],
        "elevation_range_ft": (6300, 7500),
        "wui_exposure": (
            "extreme -- Show Low and Pinetop-Lakeside are effectively built within a continuous "
            "ponderosa pine forest with no meaningful buffer on any side. Pinetop-Lakeside is "
            "especially vulnerable with trees growing to within 20 ft of structures throughout "
            "the community. The Rodeo-Chediski Fire of 2002 forced evacuation of the entire "
            "population. Over 10,000 structures are in the direct WUI zone."
        ),
        "historical_fires": [
            {
                "name": "Rodeo-Chediski Fire",
                "year": 2002,
                "acres": 468638,
                "structures_destroyed": 491,
                "fatalities": 0,
                "cause": "arson (Rodeo) / signal fire (Chediski)",
                "notes": (
                    "The Rodeo fire was set by a part-time firefighter on the Fort Apache "
                    "Reservation on June 18, 2002; the Chediski fire was a 'signal fire' lit "
                    "by a stranded motorist on June 20. They merged June 23. Largest fire in "
                    "AZ history at the time. 30,000+ evacuated from Show Low, Pinetop-Lakeside, "
                    "Heber-Overgaard, Clay Springs, and Pinedale. 491 structures destroyed "
                    "including 465 homes. The fire reached the outskirts of Show Low at Hop "
                    "Canyon, triggering evacuation of the entire city of 7,700."
                ),
            },
            {
                "name": "Wallow Fire",
                "year": 2011,
                "acres": 538049,
                "structures_destroyed": 72,
                "fatalities": 0,
                "cause": "abandoned campfire",
                "notes": (
                    "Started May 29, 2011, near Alpine. Became Arizona's largest fire ever, "
                    "surpassing Rodeo-Chediski. Burned 538,049 acres across Apache-Sitgreaves "
                    "NF. Alpine, Greer, and Nutrioso evacuated. 32 residences, 4 commercial "
                    "buildings, and 36 outbuildings destroyed, primarily in Greer. $109 million "
                    "suppression cost. Contained July 8, 2011. Threatened Show Low / Pinetop-"
                    "Lakeside region from the southeast."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "US-60 West",
                "direction": "west to Globe / Phoenix",
                "lanes": 2,
                "bottleneck": "Salt River Canyon -- extremely steep, winding descent with no alternate route",
                "risk": "130+ mile drive to Phoenix through remote terrain; Salt River Canyon is a severe bottleneck",
            },
            {
                "route": "SR-260 West",
                "direction": "west to Heber-Overgaard / Payson",
                "lanes": 2,
                "bottleneck": "Traverses 60 miles of continuous forest along the Rim; Heber-Overgaard is another fire-vulnerable community",
                "risk": "During Rodeo-Chediski, this entire corridor was in the fire zone; not a reliable evacuation route during large fires",
            },
            {
                "route": "US-60 East / US-191 North",
                "direction": "east to Springerville, then north to I-40 at St. Johns",
                "lanes": 2,
                "bottleneck": "Two-lane road through Show Low to Springerville; 60 miles to I-40",
                "risk": "Best evacuation option during fires to the south and west; connects to I-40 via US-191",
            },
            {
                "route": "SR-77 North",
                "direction": "north to Holbrook / I-40",
                "lanes": 2,
                "bottleneck": "Two-lane; transitions from forest to open rangeland; 40 miles to I-40",
                "risk": "Good northern evacuation option; exits forest within 10 miles",
            },
        ],
        "fire_spread_characteristics": (
            "Continuous crown fire in dense ponderosa pine forest is the primary threat. Fire can "
            "spread at 3-8 mph through the canopy under wind-driven conditions, with 100+ ft flame "
            "lengths producing ember showers that spot 1-2 miles ahead. The flat to gently rolling "
            "terrain means wind is the primary driver rather than topography. Fires originating on "
            "the White Mountain Apache Reservation to the south can reach city limits in 4-8 hours "
            "under strong winds. The continuous forest with no natural breaks allows fires to burn "
            "for weeks across hundreds of thousands of acres, as demonstrated by both the "
            "Rodeo-Chediski and Wallow fires."
        ),
        "infrastructure_vulnerabilities": (
            "Show Low and Pinetop-Lakeside share water systems sourced from local wells and "
            "Show Low Lake, both within forested watersheds. APS power lines traverse dozens "
            "of miles of forest to reach the community. Summit Healthcare Regional Medical Center "
            "in Show Low is the only hospital; next nearest is in Springerville (50 mi) or "
            "Flagstaff (170 mi). Cell towers throughout the area are surrounded by forest. "
            "Propane is the primary heating fuel; tank farms and individual tanks are fire risks."
        ),
        "demographics_risk_factors": (
            "Show Low population ~10,660 (2020) and Pinetop-Lakeside ~4,100. Summer population "
            "swells significantly with Phoenix-area residents in second homes and vacation rentals. "
            "Large retiree population with mobility concerns. White Mountain Apache Reservation "
            "borders provide limited mutual aid resources. Heber-Overgaard (3,000+) and other "
            "small communities along SR-260 depend on Show Low for services and evacuation staging."
        ),
    },

    # =========================================================================
    # 6. ALPINE / GREER / NUTRIOSO
    # =========================================================================
    "alpine_greer_az": {
        "center": (33.848, -109.147),
        "terrain_notes": (
            "Alpine, Greer, and Nutrioso are tiny mountain communities at 8,000-8,500 ft elevation "
            "in the White Mountains of eastern Arizona, surrounded by the Apache-Sitgreaves National "
            "Forests. Alpine sits in Bush Valley along US-191 (the Coronado Trail), while Greer "
            "occupies a narrow valley along the Little Colorado River headwaters, and Nutrioso lies "
            "in a small valley along Nutrioso Creek 5 miles north of Alpine. The terrain is "
            "characterized by high-elevation mixed conifer forest (ponderosa pine, Douglas fir, "
            "white fir, blue spruce, and aspen) with dense understory of Gambel oak and New Mexico "
            "locust. Meadow parks break the forest in places, but continuous canopy connects the "
            "communities to millions of acres of national forest. Escudilla Mountain (10,912 ft) "
            "rises to the northeast, while Mount Baldy (11,420 ft, sacred Apache peak) dominates "
            "the southern skyline. The headwaters of the Little Colorado, San Francisco, and Blue "
            "rivers originate in this area, with steep-sided creek drainages creating natural fire "
            "corridors. The Wallow Fire of 2011 -- Arizona's largest wildfire ever at 538,049 "
            "acres -- originated just south of Alpine near Bear Wallow Wilderness, demonstrating "
            "the catastrophic fire potential of this landscape. Greer is particularly vulnerable: "
            "a narrow valley with one road in and one road out, flanked by steep timbered slopes "
            "where fuel treatments had not been completed before the Wallow Fire burned through. "
            "Elevation inversions trap cold air and smoke in valleys, creating hazardous visibility "
            "conditions during fire events. The remote location means suppression resources require "
            "hours to arrive, and the nearest Type I incident management resources are in Tucson "
            "or Phoenix, 200+ miles away."
        ),
        "key_features": [
            {"name": "Escudilla Mountain", "bearing": "NE", "distance_mi": 8,
             "type": "mountain", "notes": "10,912 ft; third-highest in AZ; dense spruce-fir; subject of Aldo Leopold's famous essay; burned in Wallow Fire"},
            {"name": "Mount Baldy / Baldy Peak", "bearing": "S", "distance_mi": 15,
             "type": "mountain", "notes": "11,420 ft; sacred to White Mountain Apache; no public access to summit; headwaters of Little Colorado River"},
            {"name": "Bear Wallow Wilderness", "bearing": "S", "distance_mi": 5,
             "type": "wilderness", "notes": "11,080 acres; origin area of Wallow Fire 2011; dense mixed conifer with heavy fuel loads"},
            {"name": "Blue Range Primitive Area", "bearing": "SE", "distance_mi": 15,
             "type": "wilderness", "notes": "180,000 acres; Arizona's only primitive area; extremely remote; minimal fire suppression capability"},
            {"name": "Nutrioso Creek Valley", "bearing": "N", "distance_mi": 5,
             "type": "valley", "notes": "Small ranching valley; grassland-meadow fuels connect to surrounding forest; Nutrioso evacuated during Wallow Fire"},
        ],
        "elevation_range_ft": (7800, 10912),
        "wui_exposure": (
            "very high -- All three communities are embedded within continuous national forest "
            "with no buffer zones. Greer is in a narrow valley with forest on three sides descending "
            "steeply to the community. Alpine's homes are interspersed with forest along US-191. "
            "Nutrioso's small cluster of ranches and homes borders grassland that connects to forest. "
            "Total combined population is under 500 year-round residents."
        ),
        "historical_fires": [
            {
                "name": "Wallow Fire",
                "year": 2011,
                "acres": 538049,
                "structures_destroyed": 72,
                "fatalities": 0,
                "cause": "abandoned campfire",
                "notes": (
                    "Started May 29, 2011, in Bear Wallow Wilderness south of Alpine. Became "
                    "Arizona's largest wildfire ever. Alpine, Greer, and Nutrioso all evacuated. "
                    "22 homes destroyed in Greer, 5 homes damaged, 24 outbuildings and 4 "
                    "commercial buildings destroyed. Greer suffered worst due to untreated fuels "
                    "on slopes south of town. $109 million suppression cost. Fire crossed into "
                    "New Mexico. Contained July 8, 2011."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "US-191 North (Coronado Trail)",
                "direction": "north to Springerville / Eager (25 miles)",
                "lanes": 2,
                "bottleneck": "Two-lane mountain road through dense forest; limited passing opportunities",
                "risk": "Primary evacuation route; fire south of Alpine could cut this road at multiple points",
            },
            {
                "route": "US-191 South (Coronado Trail)",
                "direction": "south to Clifton / Morenci (90 miles)",
                "lanes": 2,
                "bottleneck": "Extremely winding mountain road with 460+ curves; gains/loses 5,000 ft elevation; not suitable for large vehicles or rapid evacuation",
                "risk": "Essentially impassable for mass evacuation; 3+ hour drive under normal conditions",
            },
            {
                "route": "SR-273 (Greer)",
                "direction": "north from Greer to SR-260 (5 miles)",
                "lanes": 2,
                "bottleneck": "Single road in and out of Greer valley; narrow two-lane through forest",
                "risk": "Dead-end community with one exit; fire on SR-273 or SR-260 traps entire community",
            },
            {
                "route": "US-180 West",
                "direction": "west from Alpine toward Hannagan Meadow and SR-260",
                "lanes": 2,
                "bottleneck": "Remote forest road; connects to SR-260 via Forest Roads",
                "risk": "Not well-known escape route; traverses heavy forest; limited cell service",
            },
        ],
        "fire_spread_characteristics": (
            "High-elevation mixed conifer crown fire produces extreme flame lengths (150+ ft) and "
            "massive ember showers. Dense forest with heavy dead and downed fuel loads supports "
            "fire intensities exceeding 10,000 BTU/ft/s. Wind-driven crown fire can spread at "
            "3-5 mph through continuous canopy. The Wallow Fire demonstrated multi-week fire runs "
            "covering 50+ miles through continuous forest. Valley inversions trap smoke and embers "
            "in community locations. Terrain channeling through creek drainages accelerates fire "
            "movement toward valley communities. Aspen stands provide some fire resistance but "
            "drought-stressed aspen can carry fire."
        ),
        "infrastructure_vulnerabilities": (
            "Extremely remote: nearest hospital is in Springerville (25 miles). No cell service "
            "in many areas; Greer has minimal coverage. Power lines from Springerville traverse "
            "forest on wooden poles. Water systems are small community wells and springs. No natural "
            "gas service; propane and wood heating create fire risk. US-191 is the sole reliable "
            "supply route. Emergency services are volunteer-based with extremely limited resources."
        ),
        "demographics_risk_factors": (
            "Alpine population ~146 (2020 census), Greer ~100, Nutrioso ~50. Summer and fall "
            "seasonal population can be 5-10x the permanent population with cabin owners, hunters, "
            "and tourists. Many properties are unoccupied seasonally, meaning no one is present to "
            "clear defensible space or receive evacuation warnings. Aging population with limited "
            "mobility. No public transportation. Limited mutual aid from surrounding communities."
        ),
    },

    # =========================================================================
    # 7. TUCSON CATALINA FOOTHILLS
    # =========================================================================
    "tucson_foothills_az": {
        "center": (32.340, -110.850),
        "terrain_notes": (
            "The Tucson Catalina Foothills occupy the steep bajada (alluvial fan apron) at the base "
            "of the Santa Catalina Mountains, one of southern Arizona's most dramatic sky island "
            "ranges, rising from 2,500 ft in the Tucson basin to 9,157 ft at Mount Lemmon in just "
            "12 miles horizontal distance. This extreme elevation gradient supports a complete "
            "biome transition from Sonoran Desert (saguaro, palo verde, cholla) through desert "
            "grassland, oak woodland, pinyon-juniper, ponderosa pine, mixed conifer, and spruce-fir "
            "at the summit. The foothills neighborhoods (Catalina Foothills Estates, Ventana Canyon, "
            "Finger Rock, Skyline Country Club) are built on steep, rocky terrain at 2,800-3,500 ft "
            "where Sonoran desert scrub and desertscrub-grassland fuels extend continuously into "
            "canyon mouths that drain the mountain front. These canyons -- Ventana, Finger Rock, "
            "Pontatoc, Romero, Pima -- funnel afternoon upslope winds and serve as natural fire "
            "corridors from the mountain to the WUI. The Bighorn Fire of 2020 burned 119,987 acres "
            "along the entire crest of the range and descended through these canyons to within "
            "evacuation distance of foothill neighborhoods. Oro Valley, northwest of the foothills, "
            "similarly interfaces with the Catalinas. The north side of the range drops to Oracle "
            "and SaddleBrooke at 3,400-4,500 ft. The mountain community of Summerhaven (8,200 ft) "
            "sits in a saddle near the summit and was devastated by the 2003 Aspen Fire. Rocky "
            "terrain on the mountain front produces extreme post-fire debris flows through canyons "
            "that terminate in residential areas. The decomposed granite soil becomes hydrophobic "
            "after fire, producing flash floods 10-100x normal flow volumes."
        ),
        "key_features": [
            {"name": "Mount Lemmon / Santa Catalina Mountains", "bearing": "N", "distance_mi": 8,
             "type": "mountain", "notes": "9,157 ft; sky island range; complete biome transition; Bighorn Fire 2020 burned entire crest; Summerhaven community at 8,200 ft"},
            {"name": "Catalina Highway / Mount Lemmon Highway", "bearing": "NE", "distance_mi": 3,
             "type": "road", "notes": "28-mile road from Tucson to Summerhaven; only access to mountain communities; extremely vulnerable to fire closure"},
            {"name": "Pusch Ridge Wilderness", "bearing": "NW", "distance_mi": 5,
             "type": "wilderness", "notes": "56,933 acres; steep granite terrain with dense chaparral; no suppression access; flanks Oro Valley"},
            {"name": "Sabino Canyon", "bearing": "NE", "distance_mi": 4,
             "type": "canyon", "notes": "Major recreation area; deep canyon draining Santa Catalinas; fire corridor and post-fire flood pathway to foothills"},
            {"name": "Finger Rock Canyon", "bearing": "N", "distance_mi": 3,
             "type": "canyon", "notes": "Steep narrow canyon directly above Catalina Foothills neighborhoods; natural fire chimney; debris flow risk"},
        ],
        "elevation_range_ft": (2600, 9157),
        "wui_exposure": (
            "very high -- Catalina Foothills neighborhoods extend into canyon mouths on the south "
            "face of the Santa Catalina Mountains. High-value homes ($500K-$5M+) are built on steep "
            "rocky lots with desert scrub and grassland fuels extending to structures. Oro Valley's "
            "northern edge directly abuts Pusch Ridge Wilderness. Summerhaven is a mountain "
            "community completely embedded in pine-fir forest. Over 30,000 homes are in the "
            "WUI zone along the mountain front."
        ),
        "historical_fires": [
            {
                "name": "Aspen Fire",
                "year": 2003,
                "acres": 84750,
                "structures_destroyed": 340,
                "fatalities": 0,
                "cause": "human",
                "notes": (
                    "Burned June 17 - July 15, 2003, on Mount Lemmon. Destroyed 340 homes and "
                    "businesses in Summerhaven, essentially wiping out the community. Firefighting "
                    "cost $17 million; damage to infrastructure $4.1 million. Burned through pine, "
                    "mixed conifer, and spruce-fir forests on the mountain crest."
                ),
            },
            {
                "name": "Bighorn Fire",
                "year": 2020,
                "acres": 119987,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "lightning",
                "notes": (
                    "Lightning strike June 5, 2020, grew to 119,987 acres across the entire Santa "
                    "Catalina range. Evacuations ordered for Catalina Foothills neighborhoods in "
                    "Tucson, Oro Valley sections, and Mount Lemmon / Summerhaven. 850 homes "
                    "directly threatened. Fire descended into multiple canyons approaching "
                    "foothills homes. Monsoon rains helped containment. July 23 final containment. "
                    "Burned over much of the 2003 Aspen Fire scar."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Skyline Drive / Sunrise Drive",
                "direction": "west to Oracle Road (SR-77) or east to Houghton Road",
                "lanes": 4,
                "bottleneck": "Foothills collector roads merge into limited east-west arterials",
                "risk": "Only east-west corridors along the mountain front; can be cut off by fires descending canyons",
            },
            {
                "route": "Oracle Road (SR-77)",
                "direction": "south to central Tucson or north to Oro Valley / Oracle",
                "lanes": 4,
                "bottleneck": "Major commercial corridor with heavy traffic; narrows to 2 lanes north of Oro Valley",
                "risk": "Primary north-south route; congestion during evacuations; northern section passes through fire-prone terrain",
            },
            {
                "route": "Catalina Highway (Mt Lemmon Hwy)",
                "direction": "Summerhaven to Tucson (28 miles, one way)",
                "lanes": 2,
                "bottleneck": "Extremely steep, winding two-lane road; only access to Summerhaven; takes 45 min under normal conditions",
                "risk": "Single egress for Summerhaven; fire crossing the road traps mountain community; closures routine during fire",
            },
            {
                "route": "Tanque Verde Road",
                "direction": "east along mountain front to Houghton Road, then south",
                "lanes": 4,
                "bottleneck": "Narrows approaching Saguaro National Park East; limited connectivity",
                "risk": "Eastern foothills route; funnels traffic toward limited I-10 access points",
            },
        ],
        "fire_spread_characteristics": (
            "Sky island fire dynamics: extreme elevation gradient drives powerful afternoon upslope "
            "winds that push fire from lower-elevation desert scrub into progressively heavier fuels "
            "at higher elevation. Canyon chimneys accelerate fire movement dramatically. Crown fire "
            "in mixed conifer at 7,000-9,000 ft produces 100+ ft flame lengths. Descending fire "
            "driven by cold front passages or thunderstorm outflows can push fire downslope through "
            "canyons toward foothills in hours. Post-fire debris flows through steep granite canyons "
            "are a catastrophic secondary hazard, reaching residential areas within minutes of "
            "intense rainfall. Desert grassland at lower elevations can carry fast-moving fire "
            "(3-5 mph) during drought."
        ),
        "infrastructure_vulnerabilities": (
            "Tucson Water serves the foothills from pumped groundwater; post-fire runoff can "
            "contaminate surface recharge areas. APS/TEP power lines traverse fire-prone terrain "
            "along the mountain front. Cell towers on Mount Lemmon serve broad area; fire risk "
            "to towers affects emergency communications. Catalina Highway is the sole access to "
            "Summerhaven and Marshall Gulch recreation areas. Tucson Medical Center and Banner "
            "University Medical Center are 15-20 miles from the foothills."
        ),
        "demographics_risk_factors": (
            "Catalina Foothills population ~50,000; Oro Valley ~47,000. Affluent area with high "
            "property values creating complacency about defensible space. Summerhaven has ~40 "
            "year-round residents but hundreds of cabin owners. Mt. Lemmon attracts 2+ million "
            "recreational visitors annually. Retiree-heavy communities in Oro Valley (Sun City "
            "Oro Valley) have age-related mobility concerns. Many foothills homes have extensive "
            "ornamental desert landscaping that has not been cleared for fire safety."
        ),
    },

    # =========================================================================
    # 8. SIERRA VISTA / HUACHUCA MOUNTAINS
    # =========================================================================
    "sierra_vista_az": {
        "center": (31.545, -110.303),
        "terrain_notes": (
            "Sierra Vista (elevation 4,623 ft) lies at the base of the Huachuca Mountains on the "
            "western edge of the San Pedro River valley in southeastern Arizona. The Huachucas are "
            "a sky island range rising to 9,466 ft at Miller Peak, with a north-south spine "
            "separating the San Pedro and San Rafael valleys. The range's east-facing slopes "
            "directly above Sierra Vista support dense Madrean oak woodland, pinyon-juniper, and "
            "pine-oak forest, with mixed conifer and Douglas fir at the highest elevations. The "
            "lower slopes and bajada interface with desert grassland that extends to the city edge. "
            "Multiple steep canyons (Carr, Miller, Ramsey, Ash, Garden) drain eastward from the "
            "range crest directly toward Sierra Vista, serving as natural fire corridors. The "
            "grassland-woodland interface is extremely fire-prone: desert grassland can carry fire "
            "at rates exceeding 5 mph under windy conditions, and fires ascending into the "
            "Madrean oak woodland produce high-intensity burns in the resinous leaf litter. "
            "Fort Huachuca military installation occupies the northern portion of the mountain "
            "front, providing some buffer but also containing its own WUI challenges with "
            "historic buildings. The Huachuca Mountains are critical habitat for numerous rare "
            "species (Ramsey Canyon Preserve, Garden Canyon), and fire suppression decisions "
            "often balance ecological and structural protection priorities. The San Pedro Riparian "
            "National Conservation Area to the east is one of the last undammed rivers in the "
            "Southwest, and post-fire debris flows threaten this ecologically critical waterway. "
            "Strong southwesterly winds during dry cold fronts drive fires off the mountain crest "
            "and downslope toward Sierra Vista at high rates of spread. The Monument Fire of 2011 "
            "demonstrated this dynamic catastrophically."
        ),
        "key_features": [
            {"name": "Miller Peak / Huachuca Mountains", "bearing": "W", "distance_mi": 8,
             "type": "mountain", "notes": "9,466 ft; sky island range; dense oak-pine-fir forest; Monument Fire 2011 burned southern 30% of range"},
            {"name": "Carr Canyon", "bearing": "W", "distance_mi": 5,
             "type": "canyon", "notes": "Deep canyon with road access to Ramsey Vista; fire corridor to Sierra Vista; debris flow risk"},
            {"name": "Ramsey Canyon Preserve", "bearing": "SW", "distance_mi": 6,
             "type": "canyon", "notes": "Nature Conservancy preserve; rare hummingbird habitat; narrow canyon with dense riparian vegetation"},
            {"name": "Fort Huachuca", "bearing": "NW", "distance_mi": 3,
             "type": "military_installation", "notes": "US Army intelligence center; historic buildings; provides some WUI buffer but has its own fire risk"},
            {"name": "San Pedro River", "bearing": "E", "distance_mi": 8,
             "type": "river", "notes": "Last undammed river in SW; riparian corridor; post-fire debris flows threaten ecosystem"},
        ],
        "elevation_range_ft": (4400, 9466),
        "wui_exposure": (
            "high -- Sierra Vista's western neighborhoods extend to the base of the Huachuca "
            "Mountains with desert grassland and scattered oak connecting to mountain fuels. "
            "Communities south of town along SR-92 (Hereford, Palominas) are directly at the "
            "mountain-grassland interface. The Monument Fire crossed SR-92 and destroyed homes "
            "in Stump Canyon. Over 10,000 homes are in the fire-risk zone."
        ),
        "historical_fires": [
            {
                "name": "Monument Fire",
                "year": 2011,
                "acres": 30526,
                "structures_destroyed": 65,
                "fatalities": 0,
                "cause": "human",
                "notes": (
                    "Burned June 12 - July 12, 2011, across the southern 30% of the Huachuca "
                    "Mountains and into adjacent grasslands. Destroyed 65 houses and businesses "
                    "south of Sierra Vista. Crossed SR-92. Forced evacuation of 10,000+ residents "
                    "south of Sierra Vista. 7 homes lost in Stump Canyon alone. Post-fire debris "
                    "flows in Carr and Miller Canyons caused additional damage."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "SR-90",
                "direction": "north to I-10 at Benson (30 miles)",
                "lanes": 2,
                "bottleneck": "Two-lane highway through Whetstone area; narrows through ranch country",
                "risk": "Primary evacuation route to I-10; relatively safe from mountain fires but grassland fires can reach road",
            },
            {
                "route": "SR-92 South",
                "direction": "south toward Bisbee / Naco (30 miles)",
                "lanes": 2,
                "bottleneck": "Passes directly along mountain front through fire zone; Monument Fire crossed this road",
                "risk": "Extremely vulnerable during Huachuca fires; not recommended for evacuation when mountains are burning",
            },
            {
                "route": "SR-92 East",
                "direction": "east to Palominas / Hereford",
                "lanes": 2,
                "bottleneck": "Dead-end corridor; no through route east",
                "risk": "Leads to communities with no further evacuation options; San Pedro River crossing can flood",
            },
            {
                "route": "Fry Boulevard / SR-90",
                "direction": "east through Fort Huachuca gate to SR-90",
                "lanes": 4,
                "bottleneck": "Military access gate can restrict flow; merges to 2 lanes on SR-90",
                "risk": "Alternate route through Fort Huachuca; military may restrict access during security events",
            },
        ],
        "fire_spread_characteristics": (
            "Grassland-to-woodland fire transition is the primary dynamic. Desert grassland fires "
            "spread at 3-5+ mph under wind and rapidly intensify upon reaching Madrean oak woodland "
            "on the mountain slopes. Canyon channeling drives fire upslope at extreme rates with "
            "flame lengths exceeding 50 ft in heavy fuel. Downslope wind events (cold fronts, "
            "thunderstorm outflows) push fire off the mountain and toward Sierra Vista. Spotting "
            "in grassland ahead of the main fire front creates multiple ignition points. The "
            "Monument Fire demonstrated that fire can cross major highways and enter communities "
            "within hours of reaching the grassland-urban interface."
        ),
        "infrastructure_vulnerabilities": (
            "Sierra Vista water supply from Huachuca City and local wells is vulnerable to post-fire "
            "contamination of the regional aquifer. Fort Huachuca's electronic warfare testing "
            "facilities are critical military infrastructure. Power lines from Benson traverse "
            "open grassland on wooden poles. Sierra Vista Regional Health Center is the only "
            "hospital; Tucson facilities are 75 miles away. Cell towers on the Huachuca crest "
            "serve the entire region and are at direct fire risk."
        ),
        "demographics_risk_factors": (
            "Sierra Vista population ~44,000 including Fort Huachuca military and civilian "
            "personnel. Significant military family population that rotates frequently and may "
            "be unfamiliar with local fire risks. Retirement communities (Sierra Vista South, "
            "Hereford) have elderly populations with mobility concerns. Rural properties south "
            "of town along SR-92 are in the highest risk zone. Cross-border fire risk from "
            "Mexico can complicate suppression coordination."
        ),
    },

    # =========================================================================
    # 9. STRAWBERRY / PINE (Rim Country)
    # =========================================================================
    "strawberry_pine_az": {
        "center": (34.394, -111.478),
        "terrain_notes": (
            "Strawberry and Pine are small unincorporated communities in Gila County strung along "
            "SR-87 (the Beeline Highway) at 5,400-5,900 ft elevation, nestled beneath the towering "
            "Mogollon Rim escarpment. Pine sits at the lower elevation in Pine Creek canyon, one of "
            "the most dangerous fire environments in the United States -- rated among the top 10 "
            "areas nationally for catastrophic wildfire potential. The canyon's narrow geometry, "
            "steep walls, and heavy ponderosa pine fuel loading create chimney-effect fire behavior "
            "that can produce extreme rates of spread and flame lengths. Strawberry is 3 miles "
            "north at slightly higher elevation on more open terrain but still surrounded by "
            "dense ponderosa pine and Gambel oak forest. The Mogollon Rim rises 1,500-2,000 ft "
            "directly east of the communities, creating a massive wall of forest that generates "
            "powerful afternoon upslope winds and nighttime drainage flows. The Dude Fire of 1990, "
            "which killed 6 firefighters just 10 miles to the east, demonstrated the extreme fire "
            "behavior possible beneath the Rim. Fossil Creek canyon to the west provides another "
            "fire corridor: the 2021 Backbone Fire burned 40,855 acres in this area, forcing "
            "evacuation of both communities. The communities are sandwiched between the Rim to "
            "the east and steep canyon terrain to the west, with SR-87 as the only major road "
            "through the area. Dense stands of ponderosa pine grow to within 10-20 ft of many "
            "structures. The Pine-Strawberry Fuel Reduction group has worked to thin forests, "
            "but vast untreated areas remain. Pine Creek canyon acts as a natural fire funnel: "
            "fires entering the lower canyon can accelerate dramatically as they move upslope "
            "through the narrow drainage, with terrain-amplified winds exceeding 40 mph during "
            "active crown fire events. The entire area is within the world's largest contiguous "
            "ponderosa pine forest."
        ),
        "key_features": [
            {"name": "Mogollon Rim", "bearing": "E", "distance_mi": 3,
             "type": "escarpment", "notes": "2,000 ft escarpment directly above communities; drives powerful upslope winds; vast forest above the Rim"},
            {"name": "Pine Creek Canyon", "bearing": "SE", "distance_mi": 1,
             "type": "canyon", "notes": "Top-10 nationally ranked wildfire risk canyon; chimney effect produces extreme fire behavior; dense ponderosa fuel loading"},
            {"name": "Fossil Creek Canyon", "bearing": "W", "distance_mi": 8,
             "type": "canyon", "notes": "Wild & Scenic River canyon; Backbone Fire 2021 origin area; fire corridor connecting Verde Valley to Rim Country"},
            {"name": "Tonto Natural Bridge State Park", "bearing": "N", "distance_mi": 5,
             "type": "state_park", "notes": "World's largest natural travertine bridge; narrow canyon with dense riparian fuel; tourist destination"},
            {"name": "East Verde River", "bearing": "S", "distance_mi": 4,
             "type": "river", "notes": "Riparian corridor connecting Pine to Payson; fire pathway through continuous fuel; flash flood risk"},
        ],
        "elevation_range_ft": (5200, 7600),
        "wui_exposure": (
            "extreme -- Pine and Strawberry are fully embedded in ponderosa pine forest with trees "
            "growing within 10-20 ft of many structures. No meaningful defensible space buffer "
            "exists for many properties. Pine Creek canyon creates a natural fire funnel directly "
            "into Pine's residential areas. The communities fan out along SR-87 with homes "
            "extending into forested side drainages on dead-end roads."
        ),
        "historical_fires": [
            {
                "name": "Dude Fire",
                "year": 1990,
                "acres": 24174,
                "structures_destroyed": 63,
                "fatalities": 6,
                "cause": "lightning",
                "notes": (
                    "Burned 10 miles east of Strawberry/Pine beneath the Mogollon Rim. "
                    "Killed 6 firefighters in Walk Moore Canyon. Same fire environment and "
                    "fuel type as Pine Creek canyon. Demonstrated catastrophic fire potential "
                    "of the Rim Country ponderosa-chaparral fuel complex."
                ),
            },
            {
                "name": "Backbone Fire",
                "year": 2021,
                "acres": 40855,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "lightning",
                "notes": (
                    "Ignited June 16, 2021, near Fossil Creek 12 miles west of Strawberry. "
                    "Both Strawberry and Pine evacuated. SR-260 and SR-87 closed. Rim Country "
                    "Middle School in Payson served as Red Cross evacuation center. Despite "
                    "burning 40,855 acres, no structures were lost. Demonstrated that even "
                    "fires originating miles away can force full evacuation of these communities."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "SR-87 South",
                "direction": "south to Payson (15 miles)",
                "lanes": 2,
                "bottleneck": "Two-lane highway through forested terrain; limited passing zones",
                "risk": "Primary evacuation route; fire along SR-87 corridor can cut off route; heavy traffic during events",
            },
            {
                "route": "SR-87 North",
                "direction": "north to Clints Well / Camp Verde via SR-260 or Lake Mary Road",
                "lanes": 2,
                "bottleneck": "Passes through dense forest for 20+ miles; no services for extended stretch",
                "risk": "Northern route passes through same fire-prone forest; Backbone Fire closed this route",
            },
        ],
        "fire_spread_characteristics": (
            "Canyon-driven crown fire in ponderosa pine is the primary threat. Pine Creek canyon "
            "produces chimney-effect fire behavior with terrain-amplified winds exceeding 40 mph "
            "during active crown fire. Rates of spread can exceed 5 mph in heavy ponderosa pine "
            "under wind-driven conditions. Steep terrain on the Rim face drives extreme upslope "
            "fire runs during afternoon heating. Night drainage winds can push fire downslope "
            "into communities. Dense understory of Gambel oak and manzanita provides ladder fuel "
            "that transitions surface fire to crown fire rapidly. Spotting distances exceed 1 mile "
            "in crown fire conditions."
        ),
        "infrastructure_vulnerabilities": (
            "Pine-Strawberry Fire District provides local services but is a small volunteer-"
            "supplemented department. No hospital; Payson Regional Medical Center is 15 miles south. "
            "Power lines traverse forest on wooden poles. No cell service in Pine Creek canyon. "
            "Water systems are small community wells. Propane is primary heating fuel; tank "
            "placement near forest creates explosion risk. SR-87 is the sole paved route through "
            "the area; damage to this road isolates both communities."
        ),
        "demographics_risk_factors": (
            "Pine population ~1,963 (2010 census), Strawberry ~961. Significant seasonal population "
            "increase in summer with Phoenix-area second-home owners and tourists escaping heat. "
            "Many properties are vacant much of the year with no occupant to maintain defensible "
            "space or respond to warnings. Retiree-heavy permanent population with mobility concerns. "
            "Limited egress options mean evacuation must begin early. Community has organized fuel "
            "reduction efforts through Pine Strawberry Fuel Reduction group."
        ),
    },

    # =========================================================================
    # 10. CROWN KING
    # =========================================================================
    "crown_king_az": {
        "center": (34.205, -112.339),
        "terrain_notes": (
            "Crown King is an extremely remote former mining town at 5,771 ft elevation in the "
            "heart of the Bradshaw Mountains within the Prescott National Forest. The community "
            "of roughly 130 year-round residents occupies a narrow mining gulch surrounded on all "
            "sides by steep, heavily vegetated mountain terrain. Access is only via unpaved forest "
            "roads: Crown King Road from I-17 (28 miles of rough, narrow dirt road) or Senator "
            "Highway from Prescott (37 miles, partially unpaved, requiring high-clearance vehicles). "
            "The surrounding terrain is extremely steep and rugged, with dense interior chaparral "
            "(manzanita, scrub oak, mountain mahogany) on south- and west-facing slopes, and "
            "ponderosa pine and mixed conifer in north-facing drainages and higher elevations. "
            "The Bradshaw Mountains reach 7,979 ft at Mount Union, with numerous peaks and ridges "
            "above 7,000 ft surrounding Crown King. This terrain produces extreme fire behavior: "
            "steep slopes amplify fire spread rates, narrow canyons create chimney effects, and "
            "dense chaparral produces 20-30 ft flame lengths with intense radiant heat. The "
            "Gladiator Fire of 2012 started from a structure fire within Crown King itself and "
            "burned 16,240 acres, forcing complete evacuation. The Horse Fire of 2020 burned "
            "9,537 acres 6 miles NW of town, again forcing evacuation of all 100+ residents. "
            "The combination of remote location, single-track dirt road access, dense fuels on "
            "all sides, and steep terrain makes Crown King one of the most fire-vulnerable "
            "communities in Arizona. Firefighting resources require hours to reach the community, "
            "and aerial suppression is complicated by steep terrain, narrow canyons, and the "
            "small size of the community surrounded by continuous wildland fuel."
        ),
        "key_features": [
            {"name": "Mount Union", "bearing": "NW", "distance_mi": 4,
             "type": "mountain", "notes": "7,979 ft; highest in Bradshaws; dense pine-fir forest; fire lookout tower"},
            {"name": "Senator Highway", "bearing": "NW", "distance_mi": 0,
             "type": "road", "notes": "Historic 37-mile route from Prescott; partially unpaved; narrow, rough; only western access"},
            {"name": "Crown King Road (County Road 59)", "bearing": "E", "distance_mi": 0,
             "type": "road", "notes": "28 miles of dirt road from I-17 at Bumble Bee exit; narrow, rough; only eastern access; washed out sections common"},
            {"name": "Horsethief Basin", "bearing": "NW", "distance_mi": 3,
             "type": "recreation_area", "notes": "Small lake and campground; surrounded by dense chaparral; fire ignition risk from recreation use"},
            {"name": "Minnehaha", "bearing": "S", "distance_mi": 4,
             "type": "settlement", "notes": "Tiny mining settlement south of Crown King; even more isolated; evacuated during Horse Fire and Gladiator Fire"},
        ],
        "elevation_range_ft": (5400, 7979),
        "wui_exposure": (
            "extreme -- Crown King is a tiny community completely surrounded by dense wildland fuel "
            "in extremely steep terrain with no buffer whatsoever. Historic mining-era buildings with "
            "wood construction are packed closely in a narrow gulch. The Gladiator Fire started from "
            "a structure fire within town and spread to 16,240 acres. Access roads are narrow dirt "
            "tracks through heavy fuel, making evacuation inherently dangerous during fire events."
        ),
        "historical_fires": [
            {
                "name": "Gladiator Fire",
                "year": 2012,
                "acres": 16240,
                "structures_destroyed": 3,
                "fatalities": 0,
                "cause": "structure fire (human)",
                "notes": (
                    "Started May 13, 2012, from a house fire within Crown King that spread to "
                    "wildland. Burned 16,240 acres across Prescott National Forest. Crown King "
                    "and three surrounding communities evacuated. 20-30 ft walls of flame in "
                    "chaparral fuels. Type 1 Incident Management team deployed. $14 million "
                    "suppression cost."
                ),
            },
            {
                "name": "Horse Fire",
                "year": 2020,
                "acres": 9537,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "unknown",
                "notes": (
                    "Started October 15, 2020, 6 miles NW of Crown King. Grew from 2,640 to "
                    "8,300 acres in 24 hours. All 100+ Crown King residents evacuated along with "
                    "Minnehaha and Horsethief Cabins. 300 structures threatened. Residents "
                    "allowed to return October 23. No structures damaged."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Crown King Road (east)",
                "direction": "east to I-17 at Bumble Bee / Cordes Junction (28 miles)",
                "lanes": 1,
                "bottleneck": "Unpaved narrow dirt road requiring high-clearance vehicle; single lane in places; multiple creek crossings",
                "risk": "Extremely slow evacuation (1.5-2 hours minimum); road passes through dense chaparral that burns to roadside; impassable in wet weather",
            },
            {
                "route": "Senator Highway (west)",
                "direction": "west/north to Prescott (37 miles)",
                "lanes": 1,
                "bottleneck": "Partially unpaved; narrow; requires high-clearance vehicle for most of route; 2+ hours to Prescott",
                "risk": "Long, slow route through continuous forest and chaparral; fire along this route traps community from western escape",
            },
        ],
        "fire_spread_characteristics": (
            "Extreme steep-slope fire behavior in dense chaparral is the primary dynamic. "
            "South-facing chaparral slopes produce 20-30 ft flame lengths at rates of spread "
            "exceeding 3 mph. The Gladiator Fire demonstrated that structure fires within the "
            "community can spread to wildland within minutes. Narrow canyon terrain produces "
            "chimney effects with fire-generated winds exceeding 50 mph. Night inversions trap "
            "smoke in the gulch, reducing visibility to near zero. Spotting across narrow canyons "
            "can establish fire on multiple slopes simultaneously. Access roads burn from roadside "
            "fuels, making evacuation during active fire extremely hazardous."
        ),
        "infrastructure_vulnerabilities": (
            "No public water system; residents depend on private wells and springs. No power grid "
            "connection; most properties use generators and solar. Cell service is minimal to "
            "nonexistent. No medical facilities of any kind; nearest is in Prescott (2+ hours by "
            "road). Crown King Volunteer Fire Department is the sole fire resource. Historic wooden "
            "structures in the town center are extremely vulnerable. Propane and wood are primary "
            "fuel sources. Both access roads can be rendered impassable by fire, washouts, or snow."
        ),
        "demographics_risk_factors": (
            "Year-round population approximately 130. Weekend and summer population can surge to "
            "500+ with recreational visitors (ATVs, camping, historic tourism). Many residents are "
            "self-reliant rural types who may resist evacuation. No public services, no schools, "
            "no commercial medical care. Many structures are historic mining-era buildings not "
            "built to modern fire codes. The community's extreme isolation means any fire event "
            "requires complete self-evacuation hours before professional resources arrive."
        ),
    },

    # =========================================================================
    # 11. YARNELL / PEEPLES VALLEY
    # =========================================================================
    "yarnell_az": {
        "center": (34.222, -112.749),
        "terrain_notes": (
            "Yarnell is a small unincorporated community at 4,780 ft elevation in the Weaver "
            "Mountains of the Bradshaw Range, perched along Arizona State Route 89 approximately "
            "35 miles south of Prescott and 80 miles NW of Phoenix. The town sits on a ridge "
            "with dramatic views to the south and west, while Peeples Valley lies 3 miles north "
            "in a broader grassland valley at slightly lower elevation. The terrain around Yarnell "
            "is defined by steep, boulder-strewn granite slopes with heavy interior chaparral "
            "vegetation: dense manzanita, scrub oak, mountain mahogany, and turbinella oak. This "
            "chaparral is the same fuel type responsible for some of Arizona's most deadly fire "
            "behavior. Yarnell Hill -- a 1,300 ft elevation change over 4 miles of winding SR-89 "
            "-- connects the community to the desert floor below and creates dramatic terrain "
            "interactions with fire weather. On June 30, 2013, the Yarnell Hill Fire killed 19 "
            "members of the Granite Mountain Hotshots, making it the deadliest US wildland fire "
            "for firefighters since the 1933 Griffith Park Fire. The crew was overrun in a box "
            "canyon with heavy brush when a thunderstorm-generated wind shift reversed the fire "
            "direction, sending it through their position at 10-12 mph. The terrain around Yarnell "
            "features numerous box canyons and boulder-choked drainages that channel and accelerate "
            "fire while creating entrapment hazards. South-facing slopes are especially dangerous "
            "with continuous chaparral fuels on 30-50% grades. The area between Yarnell and Peeples "
            "Valley includes transitional grassland that can carry fire rapidly. The Granite Mountain "
            "Hotshots Memorial State Park now marks the deployment site where the crew perished. "
            "The community has rebuilt since the 2013 fire but remains in an extremely high-risk "
            "fire environment with the same fuel types and terrain that produced the tragedy."
        ),
        "key_features": [
            {"name": "Yarnell Hill (SR-89 grade)", "bearing": "S", "distance_mi": 1,
             "type": "terrain_feature", "notes": "1,300 ft elevation drop over 4 miles of winding road; steep chaparral-covered slopes on both sides; Yarnell Hill Fire descended this feature"},
            {"name": "Granite Mountain Hotshots Memorial", "bearing": "W", "distance_mi": 2,
             "type": "memorial", "notes": "State park marking where 19 hotshots deployed shelters in a box canyon; now a 7-mile memorial trail"},
            {"name": "Weaver Mountains", "bearing": "all directions", "distance_mi": 0,
             "type": "mountain_range", "notes": "Granite peaks and ridges to 6,400+ ft; dense chaparral on all aspects; boulder-strewn slopes create entrapment hazards"},
            {"name": "Peeples Valley", "bearing": "N", "distance_mi": 3,
             "type": "valley", "notes": "Broader grassland valley; transitional fuels between chaparral and open range; 2 structures destroyed in 2013 fire"},
            {"name": "Congress / Stanton mining district", "bearing": "SW", "distance_mi": 8,
             "type": "settlement", "notes": "Small settlements along US-93/SR-89 junction; desert grassland connecting fire risk from Yarnell to the southwest"},
        ],
        "elevation_range_ft": (3400, 6400),
        "wui_exposure": (
            "extreme -- Yarnell is built on a ridge surrounded by dense chaparral with no "
            "defensible buffer. Many homes were destroyed in the 2013 fire and some have been "
            "rebuilt in the same locations within the same fuel types. The steep, rocky terrain "
            "prevents effective fuel breaks on many slopes. Peeples Valley's scattered rural "
            "properties are in grassland-chaparral transition fuels."
        ),
        "historical_fires": [
            {
                "name": "Yarnell Hill Fire",
                "year": 2013,
                "acres": 8400,
                "structures_destroyed": 129,
                "fatalities": 19,
                "cause": "lightning",
                "notes": (
                    "Ignited by lightning June 28, 2013. On June 30, the fire overran and "
                    "killed 19 members of the Granite Mountain Hotshots from the Prescott "
                    "Fire Department -- the deadliest US wildland fire for firefighters since "
                    "1933. A thunderstorm outflow boundary reversed the fire direction, "
                    "pushing it through the crew's position at 10-12 mph in heavy chaparral. "
                    "The crew deployed fire shelters in a box canyon but conditions were "
                    "unsurvivable: direct flame contact and extreme temperatures. Only one "
                    "crew member survived (Brendan McDonough, posted as lookout). 127 buildings "
                    "destroyed in Yarnell, 2 in Peeples Valley. 600+ residents under mandatory "
                    "evacuation. The fire completely changed the community, destroying roughly "
                    "one-quarter of all structures."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "SR-89 North",
                "direction": "north through Peeples Valley toward Prescott (35 miles)",
                "lanes": 2,
                "bottleneck": "Two-lane mountain road; passes through Peeples Valley which can also be in fire zone",
                "risk": "Primary evacuation route; fire in the chaparral between Yarnell and Peeples Valley can block this road entirely",
            },
            {
                "route": "SR-89 South",
                "direction": "south down Yarnell Hill toward Wickenburg / Phoenix",
                "lanes": 2,
                "bottleneck": "1,300 ft descent over 4 miles of steep, winding road; slow for vehicles towing trailers or RVs",
                "risk": "The Yarnell Hill grade is the only southern escape; fire burning downhill toward the grade can cut off this route; the grade itself is flanked by heavy chaparral",
            },
        ],
        "fire_spread_characteristics": (
            "Dense chaparral on steep granite slopes is the defining fuel type. Under wind-driven "
            "conditions, chaparral fires produce 20-30 ft flame lengths at rates of spread exceeding "
            "5 mph, with extreme radiant heat output. Thunderstorm outflow boundaries cause rapid "
            "wind shifts of 180 degrees that reverse fire direction within minutes. Box canyons and "
            "boulder-choked drainages create entrapment hazards by channeling fire and blocking "
            "escape routes. The 2013 fire demonstrated that fire in this terrain can exceed 10 mph "
            "ROS during wind shifts. South-facing slopes preheat rapidly in afternoon sun, "
            "intensifying fire behavior during the critical 1400-1800 window. Spotting in chaparral "
            "is typically short-range (100-500 ft) but persistent."
        ),
        "infrastructure_vulnerabilities": (
            "Yarnell has limited community water (small system); many properties are on private wells. "
            "Power lines from Prescott traverse chaparral-covered terrain. Cell coverage is marginal; "
            "one tower on the ridge. No medical facilities; nearest emergency room is in Wickenburg "
            "(30 miles south) or Prescott (35 miles north). No fire hydrant system for most of the "
            "community. The Yarnell Fire District is small with limited apparatus."
        ),
        "demographics_risk_factors": (
            "Yarnell population approximately 570 (2020 census). Largely retiree community with "
            "high median age and associated mobility limitations. Many residents are on fixed incomes "
            "with limited resources for defensible space maintenance or fire-resistant construction. "
            "Some properties rebuilt after 2013 fire remain in the same fuel types. Peeples Valley "
            "has scattered ranch properties with long driveways through brush. Limited community "
            "resources for organized evacuation. Post-traumatic stress from 2013 tragedy remains "
            "a community concern."
        ),
    },

    # =========================================================================
    # 12. CAREFREE / CAVE CREEK
    # =========================================================================
    "carefree_cave_creek_az": {
        "center": (33.822, -111.918),
        "terrain_notes": (
            "Carefree and Cave Creek are adjacent communities at 2,100-2,500 ft elevation in "
            "the northeastern Sonoran Desert fringe of the Phoenix metropolitan area, situated "
            "where the urbanized Valley gives way to the Tonto National Forest and Sonoran Desert "
            "wildlands to the north and east. The terrain transitions from the flat urban grid of "
            "north Scottsdale and Phoenix to rolling desert hills, granite boulder outcrops, and "
            "shallow washes draining south from the rugged New River Mountains and the Tonto NF "
            "backcountry. Vegetation is upper Sonoran Desert: dense stands of saguaro cactus, "
            "palo verde, ironwood, jojoba, and critically, dense buffelgrass (an invasive species "
            "that has dramatically increased fire connectivity in the Sonoran Desert). Native "
            "desert shrub and brittlebush cover steep north-facing slopes and wash bottoms, while "
            "south-facing rock outcrops support sparser vegetation. The area north of Cave Creek "
            "transitions rapidly into wildland terrain with no urban buffer: the Spur Cross Ranch "
            "Conservation Area, Cave Creek Regional Park, and Tonto National Forest create a "
            "continuous wildland corridor extending 50+ miles north to the Mogollon Rim. The Cave "
            "Creek Complex Fire of 2005 burned 243,950 acres northeast of the communities, and "
            "the 2024 Wildcat Fire burned 14,402 acres near Bartlett Lake demonstrating continued "
            "fire risk. Carefree Highway (SR-74) and Cave Creek Road are the primary access "
            "corridors connecting these communities to the rest of the metro area. The terrain "
            "creates a funnel effect: fire approaching from the north or east has a broad front "
            "that narrows as it encounters development, concentrating fire energy along washes "
            "and drainages that lead into residential areas. Buffelgrass invasion has connected "
            "previously isolated desert shrub fuel patches into continuous fire corridors, "
            "fundamentally changing the Sonoran Desert fire regime."
        ),
        "key_features": [
            {"name": "Tonto National Forest", "bearing": "NE", "distance_mi": 5,
             "type": "forest", "notes": "2.9 million acres; Cave Creek Ranger District; continuous wildland extending to Mogollon Rim; Cave Creek Complex Fire origin area"},
            {"name": "Spur Cross Ranch Conservation Area", "bearing": "N", "distance_mi": 3,
             "type": "conservation_area", "notes": "2,154 acres of Sonoran Desert; connects wildland to community edge; recreation use increases ignition risk"},
            {"name": "New River Mountains", "bearing": "NE", "distance_mi": 8,
             "type": "mountain_range", "notes": "Rocky desert range to 4,000 ft; sparse Sonoran vegetation; fire can spread through buffelgrass-invaded slopes"},
            {"name": "Bartlett Lake / Verde River", "bearing": "E", "distance_mi": 15,
             "type": "lake", "notes": "Verde River corridor; Wildcat Fire 2024 area; recreation access through fire-prone terrain"},
            {"name": "Black Mountain", "bearing": "S", "distance_mi": 3,
             "type": "mountain", "notes": "3,398 ft; within Cave Creek town limits; desert preserve with desert scrub fuels; WUI interface on all sides"},
        ],
        "elevation_range_ft": (2000, 4000),
        "wui_exposure": (
            "high -- Carefree and Cave Creek represent the northeastern WUI edge of the Phoenix "
            "metro area. Custom homes on large lots intermix with desert wildland, especially "
            "north of Carefree Highway and along Cave Creek Road. Many luxury properties feature "
            "desert landscaping that connects to wildland fuels. The 2005 Cave Creek Complex Fire "
            "approached residential areas and destroyed at least 12 homes."
        ),
        "historical_fires": [
            {
                "name": "Cave Creek Complex Fire",
                "year": 2005,
                "acres": 243950,
                "structures_destroyed": 12,
                "fatalities": 0,
                "cause": "lightning",
                "notes": (
                    "Started June 21, 2005, from lightning. Two separate fires merged into "
                    "one massive event burning 243,950 acres northeast of Phoenix. Grew from "
                    "2,000 to 10,000 acres within one hour. Destroyed 12 homes and 12 "
                    "outbuildings. 250 homes evacuated. Largest Sonoran Desert fire in modern "
                    "record, demonstrating that desert terrain can support massive fire events."
                ),
            },
            {
                "name": "Wildcat Fire",
                "year": 2024,
                "acres": 14402,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "human",
                "notes": (
                    "Started May 18, 2024, near Bartlett Lake in Tonto NF. Burned 14,402 acres "
                    "east of Cave Creek. Road closures affected Cave Creek Ranger District access. "
                    "Six hotshot crews, helicopter and air tanker support deployed. Demonstrated "
                    "continued fire risk in the Cave Creek backcountry."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Carefree Highway (SR-74)",
                "direction": "west to I-17 (15 miles)",
                "lanes": 4,
                "bottleneck": "Narrows from 4 to 2 lanes west of Cave Creek Road; traffic signals in commercial areas",
                "risk": "Primary east-west evacuation corridor; heavy traffic during events; brush fires can approach road",
            },
            {
                "route": "Cave Creek Road",
                "direction": "south to Phoenix / Scottsdale (20 miles)",
                "lanes": 2,
                "bottleneck": "Two-lane road through narrow washes; traffic signals increase as approaching metro area",
                "risk": "Primary north-south route; congested under normal conditions; brush fire can cross road in wash areas",
            },
            {
                "route": "Scottsdale Road",
                "direction": "south to Scottsdale (15 miles)",
                "lanes": 4,
                "bottleneck": "Ends at Carefree area; connects to Scottsdale grid system",
                "risk": "Secondary route; handles overflow from Cave Creek Road; relatively protected from wildland fire",
            },
            {
                "route": "Tom Darlington Drive / Bartlett Dam Road",
                "direction": "east toward Bartlett Lake / Rio Verde (dead end)",
                "lanes": 2,
                "bottleneck": "Dead-end road to Bartlett Lake; no through route",
                "risk": "NOT an evacuation route; leads deeper into wildland; Wildcat Fire 2024 area",
            },
        ],
        "fire_spread_characteristics": (
            "Sonoran Desert fire behavior differs from forested terrain: buffelgrass invasion has "
            "created continuous fine fuel beds that carry fire rapidly (2-5 mph) through previously "
            "non-flammable desert. Brittlebush and jojoba produce high-volatility fire when heated. "
            "Palo verde and ironwood trees are not adapted to fire and are killed easily, meaning "
            "desert fires remove canopy cover and promote further buffelgrass invasion (positive "
            "feedback loop). Wind-driven fires through washes and drainages can reach residential "
            "areas with little warning. Low humidity and high temperatures (>110F) in June create "
            "extreme fire weather. The Cave Creek Complex Fire demonstrated that a desert fire can "
            "grow to 10,000 acres within one hour under favorable conditions."
        ),
        "infrastructure_vulnerabilities": (
            "Water supplied by EPCOR Water and Cave Creek Water Company from wells; extended fire "
            "events can exceed water system capacity for fire suppression. APS power lines traverse "
            "desert terrain on exposed poles. Cell towers on Black Mountain and Carefree area ridges. "
            "No hospital in either community; HonorHealth Scottsdale Shea or Thompson Peak facilities "
            "are 15-20 miles south. Natural gas service from SW Gas through desert corridor."
        ),
        "demographics_risk_factors": (
            "Cave Creek population ~5,200; Carefree ~3,700. Affluent communities with high property "
            "values ($500K-$5M+). Large lots (1-5+ acres) with desert landscaping create fire "
            "connectivity. Many residents moved from urban Phoenix and may underestimate wildfire risk "
            "in a desert environment. Significant equestrian community with horse evacuation needs. "
            "Seasonal visitors and Scottsdale tourists frequent the area. Annual events (Renaissance "
            "Festival nearby, Cave Creek rodeo) bring temporary populations."
        ),
    },

    # =========================================================================
    # 13. ORACLE / SADDLEBROOKE
    # =========================================================================
    "oracle_az": {
        "center": (32.611, -110.771),
        "terrain_notes": (
            "Oracle and SaddleBrooke sit on the northern flank of the Santa Catalina Mountains "
            "at 3,400-4,500 ft elevation, approximately 30 miles north of Tucson along State Route "
            "77 (Oracle Road). Oracle is the higher community at ~4,500 ft, an eclectic small town "
            "with a mining and ranching heritage, perched on the oak-grassland transition zone of "
            "the Catalina north slope. SaddleBrooke is a large master-planned retirement community "
            "at ~3,400 ft in the lower foothills, immediately north of Oro Valley. The terrain "
            "descends from the Catalina crest (9,157 ft at Mt. Lemmon) through mixed conifer, "
            "ponderosa pine, Madrean oak woodland, grassland, and finally Sonoran Desert. The "
            "north side of the Catalinas has gentler slopes than the steep south face above Tucson, "
            "but the continuous fuel beds stretching from summit to community make it vulnerable "
            "to large fire runs. The 2020 Bighorn Fire burned the full length of the Catalina "
            "crest and descended the north side to within 2 miles of Oracle and 2.5 miles of "
            "SaddleBrooke, prompting controlled burns south of Oracle to halt the fire's advance. "
            "The Oracle area features rolling hills of Emory oak and grassland interspersed with "
            "manzanita and juniper -- fuels that carry fire efficiently under wind-driven conditions. "
            "The San Pedro River valley to the east creates a terrain gap that channels winds from "
            "the southeast. Apache Peak (5,400 ft) and Oracle Ridge extend northeast of the "
            "community with heavily vegetated slopes. The Biosphere 2 research facility sits 5 "
            "miles north of Oracle in the desert foothills. SaddleBrooke's location at the base "
            "of the northern bajada means fires descending the mountain can reach the community "
            "through continuous grassland-shrub fuels with no buffer. Over 12,000 residents in "
            "SaddleBrooke alone are in this exposure zone."
        ),
        "key_features": [
            {"name": "Santa Catalina Mountains (north face)", "bearing": "S", "distance_mi": 5,
             "type": "mountain", "notes": "9,157 ft; north slope descends through continuous fuel to Oracle; Bighorn Fire 2020 reached within 2 miles of Oracle"},
            {"name": "Oracle Ridge / Apache Peak", "bearing": "NE", "distance_mi": 3,
             "type": "ridge", "notes": "5,400 ft; oak woodland and manzanita; extends fire risk northeast of Oracle"},
            {"name": "Biosphere 2", "bearing": "N", "distance_mi": 5,
             "type": "research_facility", "notes": "University of Arizona facility; unique scientific infrastructure; surrounded by desert grassland fuels"},
            {"name": "SaddleBrooke development", "bearing": "SW", "distance_mi": 5,
             "type": "residential", "notes": "Large master-planned retirement community of 12,500+ residents at base of Catalina north bajada; directly in fire path from mountain"},
            {"name": "San Pedro River Valley", "bearing": "E", "distance_mi": 10,
             "type": "valley", "notes": "Major valley east of Oracle; channels SE winds toward Catalina foothills; grassland fires can approach from the east"},
        ],
        "elevation_range_ft": (3200, 5400),
        "wui_exposure": (
            "high -- Oracle's homes are scattered through oak woodland and grassland on the "
            "Catalina north slope with wildland fuels extending to property lines. SaddleBrooke's "
            "12,500+ residents live at the base of the mountain with desert grassland and scattered "
            "shrub connecting to mountain fuels. The Bighorn Fire of 2020 demonstrated that fire "
            "from the Catalina crest can descend to community-adjacent distances."
        ),
        "historical_fires": [
            {
                "name": "Bighorn Fire",
                "year": 2020,
                "acres": 119987,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "lightning",
                "notes": (
                    "Lightning strike June 5, 2020, on the Catalina crest. Grew to 119,987 acres "
                    "across the entire Santa Catalina range. Fire descended north side to within "
                    "2 miles of Oracle and 2.5 miles of SaddleBrooke by late June. Controlled "
                    "burns set south of Oracle to halt fire advance. SaddleBrooke placed on "
                    "evacuation alert. Oracle community organized to defend properties. Contained "
                    "July 23 with monsoon assistance."
                ),
            },
            {
                "name": "Aspen Fire (indirect)",
                "year": 2003,
                "acres": 84750,
                "structures_destroyed": 340,
                "fatalities": 0,
                "cause": "human",
                "notes": (
                    "Primarily impacted south side (Summerhaven) but burned across the Catalina "
                    "crest, threatening the north side watershed that supports Oracle-area water "
                    "supplies. Demonstrated the range-spanning fire potential of the Catalinas."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "SR-77 South",
                "direction": "south through Oro Valley to Tucson (30 miles)",
                "lanes": 2,
                "bottleneck": "Narrows to 2 lanes through Oracle Junction; widens to 4 lanes in Oro Valley",
                "risk": "Primary evacuation route; passes along mountain front where fire can approach from the west",
            },
            {
                "route": "SR-77 North",
                "direction": "north to Globe / Show Low (80 miles)",
                "lanes": 2,
                "bottleneck": "Two-lane highway through open desert and grassland; long distance to services",
                "risk": "Secondary route; exits fire zone quickly to the north but limited services",
            },
            {
                "route": "Mt. Lemmon Road / Control Road",
                "direction": "south from Oracle toward Catalina Highway (forest road)",
                "lanes": 1,
                "bottleneck": "Unpaved forest road; rough, narrow; not suitable for general evacuation",
                "risk": "Emergency-only route; traverses directly through fire-prone terrain; NOT recommended for evacuation",
            },
        ],
        "fire_spread_characteristics": (
            "Grassland-to-woodland fire transition: fires in desert grassland at lower elevations "
            "spread at 2-4 mph under wind, intensifying as they reach Emory oak and manzanita fuel "
            "at higher elevations. Fires descending the north slope of the Catalinas move through "
            "continuous fuel from mixed conifer through oak woodland to grassland, reaching community "
            "distances in hours. The gentler north slope (compared to the steep south face) means "
            "fires can spread downslope at moderate rates rather than being terrain-limited. Terrain "
            "channeling through drainages on the north slope directs fire toward Oracle and "
            "SaddleBrooke. Post-fire debris flows through Catalina north-side canyons threaten "
            "SaddleBrooke's infrastructure."
        ),
        "infrastructure_vulnerabilities": (
            "Oracle water from community wells and Oracle Water Company; vulnerable to post-fire "
            "watershed contamination. SaddleBrooke served by community water company; limited fire "
            "flow capacity. Power lines from the north traverse open grassland. No hospital in "
            "Oracle; SaddleBrooke Medical Center is a small clinic. Nearest emergency room is in "
            "Oro Valley or Tucson (30+ miles). Cell coverage is limited in Oracle itself. "
            "Biosphere 2's unique scientific infrastructure is at risk from grassland fire."
        ),
        "demographics_risk_factors": (
            "Oracle population ~3,050 (2020 census). SaddleBrooke population ~12,500 -- a large "
            "active-adult retirement community with an elderly population that has mobility concerns "
            "and medical dependencies. SaddleBrooke Ranch adds another 2,000+ residents. Many "
            "SaddleBrooke residents relocated from other states and may be unfamiliar with Arizona "
            "wildfire risk. Oracle has a mixed population of ranchers, artists, and retirees. "
            "Horse and livestock ownership in Oracle complicates evacuation. Limited law enforcement "
            "presence for evacuation management."
        ),
    },

    # =========================================================================
    # 14. PARADISE VALLEY
    # =========================================================================
    "paradise_valley_az": {
        "center": (33.531, -111.943),
        "terrain_notes": (
            "Paradise Valley is an affluent enclave town of approximately 14,000 residents nestled "
            "between Phoenix and Scottsdale, defined by the dramatic presence of Camelback Mountain "
            "(2,704 ft) on its southern border and Mummy Mountain (2,260 ft) within the town. The "
            "Phoenix Mountains Preserve, including Piestewa Peak (2,608 ft) and the North Mountain "
            "recreation area, flanks the community to the west. These desert mountain preserves "
            "support upper Sonoran Desert vegetation: saguaro, palo verde, cholla, brittlebush, "
            "creosote, and critically, invasive buffelgrass and fountain grass that have dramatically "
            "increased fire connectivity on rocky desert slopes. The town occupies a broad, gently "
            "sloping desert bajada between these mountain features at 1,300-1,600 ft elevation. "
            "Unlike most Phoenix suburbs, Paradise Valley has maintained 1-acre minimum lot sizes, "
            "creating a low-density residential landscape with extensive desert landscaping that "
            "connects to mountain preserve wildland fuels. Many homes are built on or adjacent "
            "to the slopes of Camelback Mountain, Mummy Mountain, and the hillside areas along "
            "Tatum Boulevard and Lincoln Drive. These hillside properties have desert vegetation "
            "extending from mountain preserve land to within feet of structures. The Phoenix Fire "
            "Department has identified the WUI zones around Camelback, Piestewa Peak, and the "
            "North Mountains as priority areas and has developed rapid deployment plans for "
            "wildland-urban interface fires. Dry desert vegetation, extreme summer temperatures "
            "(115+F), and the lack of rainfall from March through June create a critical fire "
            "window. Desert fires in the preserves can start from hikers, vehicles, or equipment "
            "and reach hillside homes within minutes due to the steep terrain and proximity of "
            "homes to wildland fuels."
        ),
        "key_features": [
            {"name": "Camelback Mountain", "bearing": "S", "distance_mi": 1,
             "type": "mountain", "notes": "2,704 ft; Phoenix's most iconic peak; steep rocky slopes with Sonoran vegetation; 1.2 million hikers/year; WUI interface on north side"},
            {"name": "Mummy Mountain", "bearing": "central", "distance_mi": 0,
             "type": "mountain", "notes": "2,260 ft; within Paradise Valley town limits; surrounded by homes on all sides; desert scrub fuels; no public hiking access"},
            {"name": "Piestewa Peak / Phoenix Mountains Preserve", "bearing": "W", "distance_mi": 3,
             "type": "mountain_preserve", "notes": "2,608 ft; 7,000-acre preserve; desert vegetation including buffelgrass; heavy recreation use; fires from hikers/vehicles"},
            {"name": "Scottsdale Greenbelt / Indian Bend Wash", "bearing": "E", "distance_mi": 2,
             "type": "park_system", "notes": "Linear park system; irrigated turf provides some fire break on eastern edge; connects to canal system"},
            {"name": "Lincoln Drive corridor", "bearing": "S", "distance_mi": 1,
             "type": "road_corridor", "notes": "Primary east-west road; runs along Camelback Mountain base; luxury homes directly on mountain slopes"},
        ],
        "elevation_range_ft": (1300, 2704),
        "wui_exposure": (
            "moderate to high -- While Paradise Valley is within the Phoenix metro area, its large-"
            "lot hillside development pattern and proximity to mountain preserves creates genuine "
            "WUI exposure. Homes on Camelback Mountain north slope, Mummy Mountain flanks, and "
            "along the Phoenix Mountains Preserve edge are within wildland fuel contact zones. "
            "The rapid deployment fire plan indicates authorities take this risk seriously."
        ),
        "historical_fires": [
            {
                "name": "Camelback Mountain brush fires",
                "year": 2020,
                "acres": 5,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "various",
                "notes": (
                    "Multiple small brush fires on Camelback Mountain and nearby preserves, "
                    "typically 1-10 acres, caused by hikers, vehicles, or equipment. These "
                    "fires are quickly suppressed by Phoenix FD but demonstrate the ignition "
                    "risk from 1.2 million annual hikers on Camelback alone. Any fire exceeding "
                    "initial attack during extreme heat and wind conditions could threaten "
                    "hillside homes."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Lincoln Drive",
                "direction": "east to Scottsdale Road or west to 24th Street",
                "lanes": 4,
                "bottleneck": "Scenic road with limited intersections; floods in monsoon",
                "risk": "Primary east-west corridor along Camelback base; can be blocked by mountain fire approaching road",
            },
            {
                "route": "Tatum Boulevard",
                "direction": "north to Shea or south to Camelback Road",
                "lanes": 4,
                "bottleneck": "Traffic signals at major intersections; limited freeway access",
                "risk": "Primary north-south corridor; passes between Mummy Mountain and Camelback",
            },
            {
                "route": "McDonald Drive",
                "direction": "east-west connecting Scottsdale Road to 44th Street",
                "lanes": 2,
                "bottleneck": "Two-lane residential road; narrow in places",
                "risk": "Secondary route; limited capacity for mass evacuation",
            },
            {
                "route": "SR-51 / SR-101 Freeway access",
                "direction": "west to SR-51 (3 miles) or east to SR-101 (5 miles)",
                "lanes": "freeway",
                "bottleneck": "Must traverse surface streets to reach freeways; no direct freeway access within Paradise Valley",
                "risk": "Multiple-route evacuation via surface streets to freeways; adequate for most scenarios due to urban grid connectivity",
            },
        ],
        "fire_spread_characteristics": (
            "Urban desert fire behavior: steep rocky mountain slopes with buffelgrass and desert "
            "scrub can carry fire upslope at 1-3 mph, accelerating on south-facing aspects. "
            "Extreme heat (115+F) and low humidity (<5%) create conditions where desert vegetation "
            "ignites readily. Fires on Camelback and Mummy Mountains can spread uphill rapidly and "
            "threaten homes on the slopes within minutes of ignition. Wind-driven fires across "
            "flat desert lots with ornamental landscaping connecting to mountain fuels can spread "
            "structure-to-structure. The primary risk is small, fast-moving fires that reach "
            "structures before suppression resources arrive, rather than large landscape-scale fires."
        ),
        "infrastructure_vulnerabilities": (
            "City of Phoenix Water serves the area via pressurized zones; adequate for fire "
            "suppression. APS and SRP provide redundant power service. Multiple cell towers "
            "provide strong coverage. Paradise Valley has its own police department and contracts "
            "fire service from Phoenix FD. The main vulnerability is the concentration of "
            "ultra-high-value properties ($1M-$20M+) where individual structure loss carries "
            "enormous economic impact."
        ),
        "demographics_risk_factors": (
            "Population ~14,000 (2020 census). One of the wealthiest communities in Arizona "
            "(median home value >$2M). Residents may have resources for private fire protection "
            "but large desert lots with ornamental landscaping can create false sense of security. "
            "Aging population in some areas. Heavy recreation use of Camelback Mountain (1.2M "
            "visitors/year) creates ignition risk. Resort properties (Sanctuary, Mountain Shadows, "
            "Omni) house guests unfamiliar with desert fire risk."
        ),
    },

    # =========================================================================
    # 15. KEARNY / WINKELMAN / HAYDEN
    # =========================================================================
    "kearny_winkelman_az": {
        "center": (33.058, -110.910),
        "terrain_notes": (
            "Kearny, Winkelman, and Hayden are small copper mining towns strung along the Gila "
            "River in the Copper Basin of eastern Pinal and southern Gila counties, at elevations "
            "ranging from 1,900 ft (Winkelman) to 2,100 ft (Kearny). The terrain is characteristic "
            "of the Arizona copper country: deeply dissected desert hills and mesas covered in "
            "desert grassland (tobosa, grama grasses, curly mesquite) and Sonoran-Chihuahuan "
            "transition scrub (mesquite, catclaw acacia, palo verde, creosote). The Ray mine, "
            "one of the world's largest open-pit copper mines, sits immediately east of Kearny, "
            "and the Hayden smelter with its iconic 1,000-ft smokestack dominates the town of "
            "Hayden. The Gila River cuts through narrow canyons in this area, and the communities "
            "occupy floodplain and terrace positions along the river and its tributaries. Mineral "
            "Creek flows through Hayden, and Hackberry Wash drains through Kearny. Surrounding "
            "terrain is steep, rugged desert hills rising 500-1,500 ft above the river, covered "
            "in desert grassland that becomes extremely fire-prone during drought. The Telegraph "
            "Fire of 2021 burned 180,757 acres just to the north and west, approaching the "
            "Highway 177 corridor between Superior and Kearny. The fire demonstrated that desert "
            "grassland in this region, combined with mesquite and desert shrub on hillslopes, "
            "can support massive fire events. The Mescal Fire (72,250 acres) burned simultaneously "
            "southeast of Globe. The rugged terrain between Globe, Miami, Superior, and Kearny "
            "creates a broad fire-prone landscape connected by continuous grassland and shrub "
            "fuels. Highway 177, the sole north-south route connecting Kearny to Superior and "
            "US-60, traverses this fire-prone terrain for 30+ miles with no alternate routes. "
            "The copper mining landscape adds unique fire hazards: mine tailings can generate "
            "toxic smoke when involved in fire, and industrial facilities include chemical "
            "storage and processing equipment."
        ),
        "key_features": [
            {"name": "Ray Mine", "bearing": "E", "distance_mi": 2,
             "type": "mine", "notes": "One of world's largest open-pit copper mines; operated by ASARCO; massive disturbance area; tailings ponds"},
            {"name": "Hayden Smelter", "bearing": "S", "distance_mi": 3,
             "type": "industrial", "notes": "1,000-ft smokestack; active copper smelter; chemical storage; industrial fire/explosion risk; air quality concerns"},
            {"name": "Gila River corridor", "bearing": "through towns", "distance_mi": 0,
             "type": "river", "notes": "River flows through all three towns; riparian vegetation (tamarisk, cottonwood) carries fire; post-fire flood risk"},
            {"name": "Dripping Springs Mountains", "bearing": "NW", "distance_mi": 10,
             "type": "mountain_range", "notes": "Desert range to 4,600 ft; grassland and mesquite; Telegraph Fire 2021 burned through this area"},
            {"name": "Troy Mountain", "bearing": "N", "distance_mi": 8,
             "type": "mountain", "notes": "Telegraph Fire 2021 spot fire area; grassland-desert scrub; overlooks Highway 177 corridor"},
        ],
        "elevation_range_ft": (1900, 4600),
        "wui_exposure": (
            "moderate -- The communities themselves are small and partially buffered by the Gila "
            "River floodplain and mining disturbance. However, grassland fires approaching from "
            "surrounding desert hills can reach town edges rapidly. Highway 177 traverses 30+ "
            "miles of fire-prone terrain connecting Kearny to Superior. Winkelman and Hayden "
            "sit in narrow river canyons with steep vegetated slopes above."
        ),
        "historical_fires": [
            {
                "name": "Telegraph Fire",
                "year": 2021,
                "acres": 180757,
                "structures_destroyed": 52,
                "fatalities": 0,
                "cause": "human (under investigation)",
                "notes": (
                    "Started June 4, 2021, south of Superior. Burned 180,757 acres -- largest "
                    "fire in Arizona in 2021 and temporarily the largest in the US that year. "
                    "Communities along SR-177 including Kearny, Winkelman, and Hayden placed on "
                    "evacuation readiness. Highway 77 closed from Globe to Winkelman. Top-of-the-"
                    "World and Oaks Mobile Home Park evacuated. 52 structures destroyed. $32+ "
                    "million suppression cost. Fully contained July 3, 2021."
                ),
            },
            {
                "name": "Mescal Fire",
                "year": 2021,
                "acres": 72250,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "under investigation",
                "notes": (
                    "Started June 1, 2021, 16 miles SE of Globe. Burned 72,250 acres "
                    "simultaneously with the Telegraph Fire, creating a dual-fire crisis "
                    "in the region. Threatened the Globe-Miami corridor from the southeast "
                    "while Telegraph threatened from the west. Contained June 18, 2021."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "SR-177 North",
                "direction": "north to Superior / US-60 (30 miles)",
                "lanes": 2,
                "bottleneck": "Two-lane highway through 30 miles of fire-prone desert grassland and hills; no alternate routes",
                "risk": "Telegraph Fire 2021 directly threatened this corridor; fire can close road for extended periods; sole northern escape route",
            },
            {
                "route": "SR-77 South (from Winkelman)",
                "direction": "south to Tucson via Oracle (75 miles)",
                "lanes": 2,
                "bottleneck": "Two-lane highway through desert; passes through Oracle area; long drive to Tucson",
                "risk": "Southern evacuation option; generally away from regional fire threats; limited services for first 40 miles",
            },
            {
                "route": "SR-77 North (from Winkelman)",
                "direction": "north to Globe (30 miles)",
                "lanes": 2,
                "bottleneck": "Narrow road through Gila River canyon; passes through Dripping Springs area",
                "risk": "Telegraph and Mescal fires threatened this corridor simultaneously in 2021; fire in canyon terrain can close road",
            },
            {
                "route": "Kelvin-Riverside Road",
                "direction": "west along Gila River toward Florence / I-10",
                "lanes": 2,
                "bottleneck": "Narrow, winding river road; not designed for heavy traffic",
                "risk": "Alternate western escape; river corridor provides some buffer from wildland fire; low bridge can flood in monsoon",
            },
        ],
        "fire_spread_characteristics": (
            "Desert grassland fire spread dominates: tobosa and grama grasslands carry fire at "
            "3-5 mph under wind-driven conditions across broad desert hills and mesas. Mesquite "
            "and catclaw acacia on slopes produce higher intensity fire with 10-15 ft flame lengths. "
            "The Telegraph Fire demonstrated that desert grassland-shrub fuels in this region can "
            "support fires exceeding 180,000 acres. Wind-driven runs of 10,000+ acres per day are "
            "possible. Terrain channeling through the Gila River canyon and tributary washes "
            "directs fire toward communities. Tamarisk (salt cedar) in riparian zones burns "
            "intensely and can carry fire along river corridors into towns."
        ),
        "infrastructure_vulnerabilities": (
            "Kearny water from community wells; Hayden/Winkelman from small local systems. The "
            "Hayden smelter and Ray mine contain industrial chemicals and hazardous materials that "
            "could complicate fire response. Power lines from Globe/Miami traverse fire-prone desert. "
            "No hospital in any of the three towns; nearest emergency medical is in Globe (30 miles) "
            "or Florence (40 miles). Cell coverage is limited in canyon terrain. Mining tailings "
            "ponds contain heavy metals that could contaminate water supplies if fire damages "
            "containment infrastructure."
        ),
        "demographics_risk_factors": (
            "Kearny population ~1,950; Hayden ~890; Winkelman ~530. Combined population under "
            "3,500. Economically disadvantaged mining communities with limited resources for fire "
            "mitigation. Aging infrastructure and housing stock. High proportion of elderly and "
            "low-income residents with limited mobility and transportation options. Many residents "
            "are retired mine workers. The mining economy means air quality is already compromised "
            "by smelter emissions; wildfire smoke compounds respiratory health risks. Limited "
            "emergency management capacity."
        ),
    },
}
