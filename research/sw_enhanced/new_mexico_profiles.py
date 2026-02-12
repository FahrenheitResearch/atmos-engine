"""New Mexico Fire-Vulnerable City Profiles
=============================================

Comprehensive terrain, evacuation, fire behavior, infrastructure, and demographic
data for 14 fire-vulnerable cities across New Mexico.

Profiles derived from NWCG after-action reports, NIFC historical records,
state forestry data, CWPPs, InciWeb, and peer-reviewed literature.

Cities covered (14 entries):
    Santa Fe, Los Alamos, Ruidoso, Las Vegas NM, Silver City, Taos, Cloudcroft,
    Angel Fire, Jemez Springs, Red River, Ruidoso Downs, Reserve/Glenwood,
    Tres Piedras, Pecos/Terrero
"""

NM_ENHANCED = {

    # =========================================================================
    # 1. SANTA FE
    # =========================================================================
    "santa_fe_nm": {
        "center": (35.687, -105.938),
        "terrain_notes": (
            "Santa Fe sits at roughly 7,000 ft in the foothills of the southern Sangre de Cristo "
            "Mountains, where pinon-juniper woodland at lower elevations transitions rapidly into "
            "ponderosa pine, mixed conifer, and spruce-fir forests above 8,500 ft on the eastern "
            "escarpment. The northeast quadrant of the city is the most fire-exposed, where "
            "subdivisions have pushed into steep arroyos and ridge fingers along the Hyde Park Road "
            "(NM-475) corridor. Slopes of 30-50% face predominantly west and southwest, funneling "
            "terrain-driven upslope winds during afternoon heating. The Santa Fe River canyon and "
            "numerous arroyos act as natural chimneys that accelerate fire spread downslope toward "
            "dense residential neighborhoods. Fuel loads in the surrounding Santa Fe National Forest "
            "are critically high due to over a century of fire suppression; ponderosa stands that "
            "historically burned every 5-15 years now carry heavy ladder fuels of Gambel oak, "
            "mountain mahogany, and dense regeneration. The WUI boundary is exceptionally convoluted, "
            "with an estimated 23,500+ homes at high to extreme wildfire risk and reconstruction "
            "costs exceeding $7 billion. During spring wind events (March-June), southwest winds of "
            "40-60 mph channeled through the Sangre de Cristo passes can push crown fire downslope "
            "toward the city at rates of 1-3 miles per hour. The 2022 Hermits Peak/Calf Canyon Fire "
            "burned 341,471 acres of Santa Fe National Forest northeast of the city, demonstrating "
            "the catastrophic potential when escaped prescribed burns meet extreme drought and wind. "
            "Post-fire debris flow risk from burned watersheds above the city threatens water supply "
            "infrastructure along the Santa Fe River and Nichols/McClure reservoirs."
        ),
        "key_features": [
            {"name": "Sangre de Cristo Escarpment", "bearing": "NE", "distance_mi": 3,
             "type": "mountain_front", "notes": "Steep 30-50% slopes with dense mixed conifer; "
             "primary fire threat vector for northeast neighborhoods"},
            {"name": "Atalaya Mountain", "bearing": "E", "distance_mi": 2,
             "type": "mountain", "notes": "9,121 ft peak immediately above residential areas; "
             "popular trail system through dense pinon-juniper fuel beds"},
            {"name": "Santa Fe Baldy / Lake Peak", "bearing": "NE", "distance_mi": 14,
             "type": "mountain", "notes": "12,622 ft summit of Sangre de Cristo Range above city; "
             "alpine terrain transitions to dense spruce-fir and mixed conifer forests below"},
            {"name": "Sun Mountain", "bearing": "E", "distance_mi": 3,
             "type": "ridge", "notes": "Ridge south of Atalaya forming eastern skyline; dense "
             "pinon-juniper with scattered ponderosa creating continuous fuel bed"},
            {"name": "Santa Fe River Canyon", "bearing": "E", "distance_mi": 1,
             "type": "canyon", "notes": "Primary drainage from mountains through city center; "
             "acts as fire chimney and post-fire debris flow corridor"},
            {"name": "Hyde Memorial State Park", "bearing": "NE", "distance_mi": 8,
             "type": "recreation", "notes": "Along NM-475 in heavily forested canyon; evacuation "
             "funnel point for mountain communities above"},
        ],
        "elevation_range_ft": (6800, 12622),
        "wui_exposure": (
            "extreme -- ranked 12th nationally among Western metro areas for WUI risk; "
            "23,500+ homes at high-to-extreme risk along northeast escarpment, arroyos, and "
            "ridge-finger subdivisions; $7.28 billion estimated reconstruction exposure"
        ),
        "historical_fires": [
            {
                "name": "Pacheco Fire",
                "year": 2011,
                "acres": 9800,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "unknown",
                "notes": (
                    "Burned in Santa Fe National Forest east of Santa Fe ski area. "
                    "Demonstrated extreme fire behavior in dense mixed-conifer stands "
                    "with limited access for suppression crews on steep terrain."
                ),
            },
            {
                "name": "Hermits Peak / Calf Canyon Fire",
                "year": 2022,
                "acres": 341471,
                "structures_destroyed": 903,
                "fatalities": 0,
                "cause": "escaped prescribed burn (USFS)",
                "notes": (
                    "Largest wildfire in New Mexico history. Two USFS prescribed burns merged "
                    "during extreme wind event on April 22, 2022. Burned 341,471 acres across "
                    "San Miguel, Mora, and Taos counties. Destroyed 903 structures and damaged "
                    "85 more. Severely impacted Gallinas watershed supplying Las Vegas NM water. "
                    "Federal government accepted liability and established claims fund exceeding "
                    "$4 billion. Fire burned through Santa Fe National Forest northeast of city, "
                    "demonstrating catastrophic potential for Santa Fe proper."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "NM-475 (Hyde Park Road)",
                "direction": "south from ski basin to city",
                "lanes": 2,
                "bottleneck": "Narrow winding mountain road with no shoulders; single-lane "
                              "bridges at Artist Road and Gonzales Road intersections",
                "risk": "Only exit for communities above Hyde Memorial State Park; complete "
                        "gridlock during mass evacuation as thousands converge on single road",
            },
            {
                "route": "I-25 South",
                "direction": "south toward Albuquerque",
                "lanes": 4,
                "bottleneck": "La Bajada Hill grade south of Santa Fe; merge points at "
                              "St. Francis Drive and Cerrillos Road on-ramps",
                "risk": "Primary regional evacuation corridor; capacity adequate but access "
                        "roads from northeast neighborhoods are narrow two-lane residential streets",
            },
            {
                "route": "I-25 North",
                "direction": "north toward Las Vegas NM / Raton",
                "lanes": 4,
                "bottleneck": "Glorieta Pass and Apache Canyon narrows",
                "risk": "Route may be cut if fire is northeast of city between Santa Fe "
                        "and Pecos/Glorieta area",
            },
            {
                "route": "US-285 / NM-599",
                "direction": "south and west via bypass",
                "lanes": 4,
                "bottleneck": "NM-599 bypass intersection with US-285 at single interchange",
                "risk": "Good alternate route but requires traversing south side of city; "
                        "smoke and congestion may impede access",
            },
        ],
        "fire_spread_characteristics": (
            "Terrain-driven upslope fire behavior dominates afternoon hours as solar heating "
            "creates strong anabatic winds on west-facing escarpment slopes. Spring wind events "
            "(March-June) produce 40-60 mph sustained southwest winds that align with major "
            "drainages, creating extreme rates of spread (2-4 mph in timber, 5+ mph in grass). "
            "Crown fire potential is very high in untreated mixed-conifer stands above 8,000 ft. "
            "Night-time drainage winds reverse fire direction, pushing fire downslope toward city. "
            "Spotting distances of 0.5-1 mile common in pinon-juniper with volatile oils."
        ),
        "infrastructure_vulnerabilities": (
            "Municipal water supply dependent on Santa Fe River watershed and Nichols/McClure "
            "reservoirs, all highly vulnerable to post-fire debris flows and contamination. "
            "Buckman Direct Diversion from Rio Grande provides backup but has limited capacity. "
            "Natural gas distribution lines run through forested arroyos. Above-ground power "
            "lines along NM-475 corridor serve mountain communities and are ignition sources. "
            "Hospital (Christus St. Vincent) located on city's east side near WUI boundary."
        ),
        "demographics_risk_factors": (
            "Population 87,505 (2020 metro). Significant elderly population with 22% over 65. "
            "Many northeast foothill homes are high-value properties with wooden construction, "
            "shake roofs, and dense ornamental vegetation. Large seasonal/tourism population "
            "unfamiliar with evacuation routes. Substantial low-income and Spanish-speaking "
            "communities in south and west sectors may face language barriers in emergency "
            "communications. Many homes lack defensible space despite city WUI ordinances."
        ),
    },

    # =========================================================================
    # 2. LOS ALAMOS
    # =========================================================================
    "los_alamos_nm": {
        "center": (35.888, -106.307),
        "terrain_notes": (
            "Los Alamos occupies a narrow series of finger mesas (Pajarito Plateau) at 7,200-7,400 ft "
            "elevation, carved by deep canyons running east from the Jemez Mountains to the Rio Grande. "
            "The town is uniquely vulnerable because it is built on mesa tops separated by steep-walled "
            "canyons (Los Alamos Canyon, Pueblo Canyon, Acid Canyon, DP Canyon) that act as natural "
            "fire chimneys. Dense ponderosa pine and mixed-conifer forests blanket the Jemez Mountains "
            "immediately west of town, rising to 10,000+ ft on Pajarito Mountain and the Valles Caldera "
            "rim. The Cerro Grande Fire (2000) and Las Conchas Fire (2011) demonstrated that fire can "
            "travel from the Jemez highlands down-canyon to the mesa tops with devastating speed. "
            "Fuel loads on the western slopes above town include dense stands of ponderosa, white fir, "
            "Douglas fir, and aspen, with heavy understory of Gambel oak. The Pajarito Plateau itself "
            "carries pinon-juniper transitioning to ponderosa at higher elevations. Deep canyons create "
            "extreme fire behavior: flame lengths can exceed 200 ft in canyon confinement, and turbulent "
            "eddies at canyon rims throw embers onto mesa-top structures. Southwest winds are the primary "
            "driver, pushing fire from the Jemez Mountains directly toward the townsite. The plateau "
            "drops off sharply to the east into the Rio Grande valley, creating a natural firebreak on "
            "the east side but funneling all evacuation traffic through limited corridors. Los Alamos "
            "National Laboratory (LANL) occupies much of the surrounding mesa complex, storing nuclear "
            "materials and hazardous waste that add catastrophic risk dimensions beyond normal WUI fire."
        ),
        "key_features": [
            {"name": "Pajarito Mountain / Jemez Crest", "bearing": "W", "distance_mi": 5,
             "type": "mountain", "notes": "10,440 ft; dense spruce-fir and mixed conifer above town; "
             "primary fire approach vector from west/southwest"},
            {"name": "Valles Caldera", "bearing": "W", "distance_mi": 12,
             "type": "caldera", "notes": "89,000-acre volcanic caldera with extensive grasslands; "
             "fire can traverse caldera floor rapidly then enter timber on east rim above Los Alamos"},
            {"name": "Los Alamos Canyon", "bearing": "through town", "distance_mi": 0,
             "type": "canyon", "notes": "Deep canyon bisecting townsite; acts as fire chimney with "
             "extreme updrafts and turbulence at canyon rim"},
            {"name": "Bandelier National Monument", "bearing": "SW", "distance_mi": 6,
             "type": "monument", "notes": "Origin point of Cerro Grande prescribed burn; steep "
             "canyons with dense pinon-juniper and ponderosa connect directly to town"},
            {"name": "White Rock", "bearing": "SE", "distance_mi": 6,
             "type": "community", "notes": "Bedroom community of 6,000 on lower mesa; connected to "
             "Los Alamos by single road (NM-4) through canyon"},
        ],
        "elevation_range_ft": (6200, 10440),
        "wui_exposure": (
            "extreme -- entire town of 13,179 surrounded by forest on three sides with canyon "
            "interfaces; LANL nuclear facilities add unique hazmat risk; Cerro Grande proved "
            "400+ families can lose homes in single event; limited evacuation capacity"
        ),
        "historical_fires": [
            {
                "name": "La Mesa Fire",
                "year": 1977,
                "acres": 15270,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "human",
                "notes": (
                    "Burned through Bandelier National Monument and onto LANL property. "
                    "First modern warning of catastrophic fire potential on Pajarito Plateau."
                ),
            },
            {
                "name": "Dome Fire",
                "year": 1996,
                "acres": 16516,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "human",
                "notes": (
                    "Burned in Bandelier and Santa Fe NF south of Valles Caldera. "
                    "Raised awareness of fuel loading but no structures threatened."
                ),
            },
            {
                "name": "Oso Fire",
                "year": 1998,
                "acres": 5185,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "unknown",
                "notes": "Burned in canyons near LANL, providing fire scars later used as "
                         "fuel breaks during Cerro Grande and Las Conchas fires.",
            },
            {
                "name": "Cerro Grande Fire",
                "year": 2000,
                "acres": 47650,
                "structures_destroyed": 235,
                "fatalities": 0,
                "cause": "escaped prescribed burn (NPS Bandelier)",
                "notes": (
                    "Prescribed burn on May 4, 2000 in Bandelier escaped control due to high "
                    "winds and extreme drought. Fire raced up canyons onto Los Alamos mesa tops "
                    "at speeds estimated over 50 mph. 235 structures destroyed but many were "
                    "multi-family units, displacing 400+ families. Entire populations of Los Alamos "
                    "and White Rock (18,000 people) evacuated. LANL facilities threatened with "
                    "nuclear material storage areas. Fire burned for over a month. Estimated $1 "
                    "billion in damages. Deadfall moisture content was lower than kiln-dried lumber."
                ),
            },
            {
                "name": "Las Conchas Fire",
                "year": 2011,
                "acres": 156593,
                "structures_destroyed": 63,
                "fatalities": 0,
                "cause": "tree fell on power line",
                "notes": (
                    "Started June 26, 2011, southwest of Valles Caldera. Became largest NM fire "
                    "at the time. Burned 156,593 acres across Santa Fe NF, Bandelier, Valles "
                    "Caldera, Santa Clara Pueblo, and Jemez Pueblo lands. Destroyed 63 structures. "
                    "Again threatened Los Alamos and LANL. Fire used Cerro Grande and Oso burn "
                    "scars as partial firebreaks. Massive post-fire flooding devastated Santa Clara "
                    "Pueblo and Cochiti Pueblo watersheds."
                ),
            },
            {
                "name": "Cerro Pelado Fire",
                "year": 2022,
                "acres": 45605,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "debris burning / prescribed burn residual",
                "notes": (
                    "Started April 22, 2022, about 7 miles east of Jemez Springs near Cerro Pelado. "
                    "Burned 45,605 acres south of Valles Caldera. Prompted evacuations of Sierra Los "
                    "Pinos and nearby communities. Investigation concluded probable cause was USFS "
                    "debris pile burning from January-February 2022."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "NM-502 East (Truck Route)",
                "direction": "east to US-84/285 at Pojoaque",
                "lanes": 2,
                "bottleneck": "Single two-lane road descending steep mesa edge with sharp curves; "
                              "only primary exit for 13,000+ residents plus LANL workforce",
                "risk": "During Cerro Grande, fire flanked NM-502 at speeds over 50 mph; road can "
                        "be cut by fire approaching from south canyons",
            },
            {
                "route": "NM-4 West",
                "direction": "west through Jemez Mountains to Jemez Springs",
                "lanes": 2,
                "bottleneck": "Narrow mountain road through dense forest; passes directly through "
                              "highest-risk fire terrain",
                "risk": "Route into fire origin zone; likely first road closed; not viable for "
                        "evacuation when fire approaches from west",
            },
            {
                "route": "NM-4 East (to White Rock)",
                "direction": "southeast to White Rock and NM-502",
                "lanes": 2,
                "bottleneck": "Canyon road connecting mesas; single route for White Rock residents",
                "risk": "Can be cut by fire in canyons between Los Alamos and White Rock; "
                        "merges all White Rock traffic onto same NM-502 corridor",
            },
            {
                "route": "East Jemez Road / Pajarito Road (LANL internal)",
                "direction": "south through LANL to NM-4/NM-501",
                "lanes": 2,
                "bottleneck": "Security checkpoints; restricted access; narrow roads through LANL campus",
                "risk": "May be opened for emergency evacuation but normally restricted; "
                        "passes through forested LANL technical areas",
            },
        ],
        "fire_spread_characteristics": (
            "Canyon-driven fire behavior is the defining characteristic. Southwest winds push fire "
            "from Jemez highlands down and through deep canyons at extreme rates of spread. Canyon "
            "confinement produces flame lengths of 100-200+ ft with intense radiant heat. Turbulent "
            "eddies at canyon rims loft firebrands onto mesa-top structures 0.25-0.5 mi from active "
            "fire front. Transition from surface to crown fire is rapid in dense ponderosa/fir stands. "
            "Fire can cross the 5-mile distance from Jemez crest to townsite in 2-4 hours under "
            "extreme conditions. Cerro Grande demonstrated 50+ mph fire runs down-canyon. Night-time "
            "inversions can temporarily halt fire but morning breakup produces explosive blowup conditions."
        ),
        "infrastructure_vulnerabilities": (
            "Los Alamos National Laboratory stores nuclear materials, radioactive waste, and chemical "
            "hazards across numerous technical areas in forested settings. Water supply from Pajarito "
            "Plateau wells and reservoir system vulnerable to contamination. Single electrical feed "
            "from PNM along NM-502 corridor. Natural gas pipeline follows canyon bottoms. Two water "
            "treatment plants serve town; both in fire-exposed locations. Hospital (Los Alamos Medical "
            "Center) requires evacuation of patients during fire events."
        ),
        "demographics_risk_factors": (
            "Population 13,179 (2020). Highly educated scientific community but many residents "
            "commute and may not be present during daytime evacuation. Significant elderly "
            "population in retirement. LANL daytime workforce of 14,000+ adds to evacuation "
            "load. White Rock community of 6,000 funnels onto same escape routes. Tourism "
            "traffic on NM-4 to Valles Caldera and Bandelier adds unfamiliar drivers. Limited "
            "hotel/shelter capacity means evacuees must travel 35+ miles to Santa Fe/Espanola."
        ),
    },

    # =========================================================================
    # 3. RUIDOSO
    # =========================================================================
    "ruidoso_nm": {
        "center": (33.332, -105.673),
        "terrain_notes": (
            "Ruidoso is nestled in a narrow mountain valley along the Rio Ruidoso at 6,700-7,000 ft "
            "in the Sacramento Mountains / Sierra Blanca range of south-central New Mexico. The town "
            "stretches linearly along the canyon bottom for approximately 6 miles, with steep forested "
            "slopes rising 2,000-4,000 ft on both sides. Sierra Blanca Peak (11,981 ft) dominates the "
            "northwest skyline, while the Mescalero Apache Reservation borders the town to the south "
            "and west. The terrain creates an exceptionally dangerous fire environment: the narrow "
            "canyon acts as a chimney, accelerating fire spread; steep south-facing slopes on the north "
            "side of the valley receive maximum solar heating and carry drier fuels; and the linear town "
            "layout means fire can approach from multiple directions simultaneously. Vegetation ranges "
            "from pinon-juniper on lower south-facing slopes through ponderosa pine at mid-elevations "
            "to dense mixed conifer and spruce-fir above 9,000 ft. Decades of fire suppression have "
            "created heavy fuel loads with dense understory and ladder fuels. The Mescalero Reservation "
            "lands south of town carry additional fuel loads with limited management. The 2012 Little "
            "Bear Fire (44,330 acres, 254 structures) and the catastrophic 2024 South Fork Fire "
            "(~24,000 acres, ~1,400 structures destroyed) demonstrated that Ruidoso faces existential "
            "wildfire threat. The South Fork Fire burned through the town itself, destroying "
            "neighborhoods and businesses along Sudderth Drive. Multiple drainages funnel directly "
            "into the town center, and post-fire flooding has caused additional devastation."
        ),
        "key_features": [
            {"name": "Sierra Blanca Peak", "bearing": "NW", "distance_mi": 12,
             "type": "mountain", "notes": "11,981 ft; highest peak in southern NM; Ski Apache "
             "resort on north flank; dense spruce-fir forests above timberline"},
            {"name": "Mescalero Apache Reservation", "bearing": "S", "distance_mi": 2,
             "type": "tribal_land", "notes": "460,000 acres bordering Ruidoso on south and west; "
             "dense timber with limited fuel management; South Fork and Salt fires originated here"},
            {"name": "Rio Ruidoso Canyon", "bearing": "through town", "distance_mi": 0,
             "type": "canyon", "notes": "Narrow canyon carrying town's main axis; acts as fire "
             "chimney and post-fire flood channel; Sudderth Drive follows canyon bottom"},
            {"name": "Grindstone Canyon/Reservoir", "bearing": "NW", "distance_mi": 3,
             "type": "canyon", "notes": "Municipal water supply reservoir in forested canyon; "
             "vulnerable to contamination from fire and post-fire debris flows"},
            {"name": "Alto / Bonito Lake Area", "bearing": "N", "distance_mi": 5,
             "type": "community", "notes": "Mountain residential community north of Ruidoso; "
             "dense forest at 7,500-8,000 ft; Little Bear Fire destroyed many homes here"},
        ],
        "elevation_range_ft": (6200, 11981),
        "wui_exposure": (
            "extreme -- entire town of 7,679 is within WUI; linear canyon development means "
            "no separation between wildland fuels and structures; 2024 South Fork Fire destroyed "
            "~1,400 structures proving catastrophic vulnerability; many homes built in steep "
            "timbered drainages with wooden construction and no defensible space"
        ),
        "historical_fires": [
            {
                "name": "Gavilan Fire",
                "year": 2003,
                "acres": 15240,
                "structures_destroyed": 4,
                "fatalities": 0,
                "cause": "human",
                "notes": "Burned northwest of Ruidoso threatening Alto and Gavilan Canyon communities.",
            },
            {
                "name": "Little Bear Fire",
                "year": 2012,
                "acres": 44330,
                "structures_destroyed": 254,
                "fatalities": 0,
                "cause": "lightning",
                "notes": (
                    "Lightning-caused fire discovered June 4, 2012. On June 9 a wind event "
                    "blew embers outside fireline causing explosive growth. Destroyed 224 "
                    "residential structures and 30 outbuildings across subdivisions north of "
                    "Ruidoso along NM-48 and NM-37. Forced evacuation of hundreds. At the time, "
                    "most destructive fire in NM history."
                ),
            },
            {
                "name": "South Fork Fire",
                "year": 2024,
                "acres": 24403,
                "structures_destroyed": 1400,
                "fatalities": 2,
                "cause": "under investigation",
                "notes": (
                    "Started June 17, 2024 on Mescalero Apache Reservation south of Ruidoso. "
                    "Grew explosively to 15,000+ acres within hours driven by extreme winds and "
                    "drought. Entire village of Ruidoso (8,000 people) ordered to evacuate at "
                    "7 PM on June 17, less than 10 hours after ignition. Approximately 1,400 "
                    "structures destroyed or damaged, including ~500 homes. Two fatalities. "
                    "Governor declared state of emergency. Fire burned directly through town "
                    "neighborhoods. Post-fire flooding caused additional devastation in July."
                ),
            },
            {
                "name": "Salt Fire",
                "year": 2024,
                "acres": 5557,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "under investigation",
                "notes": (
                    "Burned simultaneously with South Fork Fire on Mescalero Reservation "
                    "east of Ruidoso. Combined with South Fork to create complex emergency."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Sudderth Drive / NM-48 South to US-70",
                "direction": "southeast to Ruidoso Downs and US-70 toward Roswell",
                "lanes": 2,
                "bottleneck": "Sudderth Drive narrows to single lane in commercial district; "
                              "merges with US-70 at congested intersection in Ruidoso Downs",
                "risk": "Only viable evacuation route during 2024 South Fork Fire; extreme "
                        "congestion with 8,000 evacuees on two-lane road; fire can cut route "
                        "from south-approaching fire",
            },
            {
                "route": "NM-48 North (Mechem Drive)",
                "direction": "north toward Capitan via Alto",
                "lanes": 2,
                "bottleneck": "Winds through mountain communities; narrow and steep",
                "risk": "Route through heavily forested terrain; likely cut by fire approaching "
                        "from north or west; Little Bear Fire blocked this corridor in 2012",
            },
            {
                "route": "US-70 West (Apache Summit)",
                "direction": "west toward Tularosa Basin via Mescalero",
                "lanes": 2,
                "bottleneck": "Climbs over Apache Summit (7,585 ft) through dense forest; "
                              "narrow with steep grades and sharp curves",
                "risk": "Closed during 2024 fires due to fire on Mescalero Reservation; "
                        "passes directly through fire origin zone",
            },
        ],
        "fire_spread_characteristics": (
            "Canyon-aligned fire spread is dominant, with the narrow Rio Ruidoso valley acting as a "
            "chimney that accelerates fire spread toward and through town. Southwest winds push fire "
            "from the Mescalero Reservation directly into town; the 2024 South Fork Fire demonstrated "
            "fire can traverse from reservation boundary to downtown in under 6 hours. Steep south-facing "
            "slopes on the north side of the valley carry extremely dry fuels and support rapid uphill runs. "
            "Crown fire transitions occur readily in dense ponderosa and mixed conifer. Spotting across "
            "the narrow valley is common with distances of 0.25-0.5 mile. Fire can approach simultaneously "
            "from multiple drainages, cutting off escape routes."
        ),
        "infrastructure_vulnerabilities": (
            "Municipal water from Grindstone and Alto Lake reservoirs; both in heavily forested "
            "watersheds vulnerable to contamination and post-fire debris flows. 2024 post-fire "
            "flooding severely damaged water infrastructure. Sewage treatment plant in canyon bottom "
            "flooded after fire. Natural gas lines along Sudderth Drive. Above-ground power lines "
            "throughout forested areas are ignition sources. Lincoln County Medical Center serves "
            "as only hospital. Many small bridges on Sudderth Drive vulnerable to debris flows."
        ),
        "demographics_risk_factors": (
            "Year-round population 7,679 (2020) but swells to 25,000+ during summer tourism "
            "and horse racing season. Large elderly and retirement community. Many properties are "
            "vacation/seasonal homes with absentee owners who cannot prepare for fire. Significant "
            "Mescalero Apache population on adjacent reservation with sovereign land management. "
            "Post-2024 fire displacement has created ongoing housing crisis. Low-income residents "
            "face difficulty rebuilding. Horse racing industry (Ruidoso Downs) employs large "
            "transient workforce in temporary housing."
        ),
    },

    # =========================================================================
    # 4. LAS VEGAS, NM (Hermits Peak / Calf Canyon)
    # =========================================================================
    "las_vegas_nm": {
        "center": (35.594, -105.223),
        "terrain_notes": (
            "Las Vegas NM sits at 6,424 ft on the eastern edge of the southern Sangre de Cristo "
            "Mountains where the foothills meet the Great Plains. The city straddles the Gallinas River, "
            "which flows east out of the heavily forested Gallinas Canyon from the mountains. West and "
            "northwest of the city, terrain rises steeply through pinon-juniper, ponderosa pine, and "
            "mixed-conifer forests to peaks exceeding 10,000 ft, including Hermit Peak (10,212 ft) and "
            "Elk Mountain. The Gallinas Canyon corridor is the primary fire threat vector: it funnels "
            "southwest winds directly from the forested mountains toward the city, and the Gallinas "
            "River watershed provides the city's entire municipal water supply. The 2022 Hermits "
            "Peak/Calf Canyon Fire -- the largest in New Mexico history at 341,471 acres -- burned "
            "directly through the forests west and north of Las Vegas, devastating the Gallinas "
            "watershed and creating severe post-fire flooding and water contamination. The eastern "
            "portion of the city transitions to shortgrass prairie, which provides some natural "
            "firebreak but carries grass fire risk during spring wind events. Rural communities in the "
            "mountains west of Las Vegas (Pendaries, Rociada, Sapello, Mora) were devastated by the "
            "2022 fire, with entire villages destroyed. Dense fuel accumulations from a century of fire "
            "suppression in the Santa Fe National Forest created conditions for extreme fire behavior, "
            "with extensive crown runs and spotting. The steep terrain with slopes exceeding 40% in "
            "Gallinas Canyon amplifies fire behavior, creating upslope runs that exceeded suppression "
            "capacity. Post-fire debris flows have repeatedly flooded Las Vegas, requiring evacuations "
            "along the Gallinas River corridor through the city center."
        ),
        "key_features": [
            {"name": "Hermit Peak", "bearing": "NW", "distance_mi": 14,
             "type": "mountain", "notes": "10,212 ft; namesake of 2022 fire; origin area of "
             "escaped prescribed burn; dense mixed-conifer forests"},
            {"name": "Gallinas Canyon", "bearing": "W", "distance_mi": 5,
             "type": "canyon", "notes": "Primary drainage from mountains through city; carries "
             "municipal water supply; fire chimney effect funnels flames toward city; post-fire "
             "flooding corridor"},
            {"name": "Elk Mountain", "bearing": "NW", "distance_mi": 18,
             "type": "mountain", "notes": "11,661 ft; high point of southern Sangre de Cristos "
             "west of Las Vegas; dense spruce-fir and mixed conifer"},
            {"name": "Montezuma / United World College", "bearing": "NW", "distance_mi": 6,
             "type": "community", "notes": "Historic hot springs area along NM-65 in Gallinas Canyon; "
             "heavily forested setting directly in fire path"},
            {"name": "Storrie Lake", "bearing": "N", "distance_mi": 4,
             "type": "reservoir", "notes": "State park reservoir north of city; post-fire "
             "sedimentation has impacted water storage capacity"},
        ],
        "elevation_range_ft": (6200, 11661),
        "wui_exposure": (
            "high -- western neighborhoods and Gallinas Canyon communities (Montezuma, Hot Springs) "
            "directly at WUI boundary; 2022 fire destroyed 903 structures in surrounding mountain "
            "communities; city center at risk from post-fire flooding; population 13,166"
        ),
        "historical_fires": [
            {
                "name": "Hermits Peak / Calf Canyon Fire",
                "year": 2022,
                "acres": 341471,
                "structures_destroyed": 903,
                "fatalities": 0,
                "cause": "escaped prescribed burn (USFS)",
                "notes": (
                    "Largest wildfire in New Mexico history. Hermits Peak Fire began April 6 when "
                    "USFS Las Dispensas prescribed burn escaped control. Calf Canyon Fire began "
                    "April 9 when improperly extinguished January pile burn rekindled. Fires merged "
                    "during extreme wind event April 22. Burned 341,471 acres across San Miguel, "
                    "Mora, and Taos counties. Destroyed 903 structures, damaged 85 more. Devastated "
                    "Gallinas watershed supplying Las Vegas water. Rural communities of Rociada, "
                    "Pendaries, Sapello, and parts of Mora heavily damaged or destroyed. Federal "
                    "government accepted liability; $4+ billion claims fund established. Fire burned "
                    "April through August 2022."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "I-25 South",
                "direction": "south toward Santa Fe (65 miles)",
                "lanes": 4,
                "bottleneck": "Glorieta Pass section; on-ramp congestion at Grand Avenue and "
                              "University Avenue interchanges",
                "risk": "Primary evacuation corridor; adequate capacity but may be affected by "
                        "smoke from fires west of I-25 corridor",
            },
            {
                "route": "I-25 North",
                "direction": "north toward Raton (110 miles)",
                "lanes": 4,
                "bottleneck": "Passes through Wagon Mound area; limited services",
                "risk": "Good alternate evacuation route away from fire area; long distance "
                        "to major services",
            },
            {
                "route": "NM-65 West (Hot Springs Blvd)",
                "direction": "west into Gallinas Canyon toward Montezuma",
                "lanes": 2,
                "bottleneck": "Narrow canyon road; follows Gallinas River; no alternate routes",
                "risk": "Route directly into fire area; closed during 2022 fire; also floods "
                        "during post-fire rain events requiring evacuation of residents along route",
            },
            {
                "route": "NM-518 North",
                "direction": "north toward Mora and Taos",
                "lanes": 2,
                "bottleneck": "Mountain road through Sapello and Mora valleys",
                "risk": "Route was cut during 2022 fire as it passed through burned area; "
                        "communities along route were destroyed",
            },
        ],
        "fire_spread_characteristics": (
            "Wind-driven fire from southwest through Gallinas Canyon is the primary threat. "
            "The 2022 fire demonstrated extreme rates of spread with 20,000-acre days during "
            "wind events. Crown fire in dense mixed conifer propagated through continuous canopy "
            "with spotting distances exceeding 1 mile. Canyon topography created fire whirls and "
            "extreme turbulence. Post-fire conditions create secondary threat: bare burned slopes "
            "generate catastrophic debris flows during monsoon rains, flooding Las Vegas along "
            "Gallinas River corridor."
        ),
        "infrastructure_vulnerabilities": (
            "Municipal water supply entirely dependent on Gallinas River watershed, which was "
            "severely burned in 2022. Post-fire contamination required emergency water treatment "
            "and alternate supply measures. Bradner and Peterson Dams above city vulnerable to "
            "debris flows. Wastewater treatment along Gallinas River at flood risk. NM Highlands "
            "University campus in city center. Aging infrastructure in historic downtown district. "
            "NM State Hospital located in city."
        ),
        "demographics_risk_factors": (
            "Population 13,166 (2020). High poverty rate (~30%) with significant elderly and "
            "Hispanic/Latino population. Many residents in surrounding mountain communities lost "
            "everything in 2022 fire and face ongoing displacement. Limited local economy heavily "
            "dependent on government and education. Many homes are older adobe and frame construction "
            "without modern fire-resistant features. Post-fire PTSD and mental health impacts are "
            "significant. Federal claims process has been slow for many residents."
        ),
    },

    # =========================================================================
    # 5. SILVER CITY
    # =========================================================================
    "silver_city_nm": {
        "center": (32.770, -108.280),
        "terrain_notes": (
            "Silver City sits at 5,935 ft in the foothills of the Pinos Altos Range at the southern "
            "edge of the Gila National Forest, the sixth-largest national forest in the continental US "
            "at 2.7 million acres. The town occupies an alluvial fan where mountain drainages meet the "
            "high desert, with terrain rising sharply to the north and northeast into dense ponderosa "
            "and mixed-conifer forests. Pinos Altos (7,840 ft) sits just 6 miles north on NM-15, a "
            "historic mining town in dense timber. The Gila Wilderness and Black Range lie to the north "
            "and northeast, containing some of the most rugged and remote terrain in the Southwest with "
            "peaks exceeding 10,000 ft. Steep canyons draining south from the Pinos Altos and Black "
            "Range -- including Bear Creek, Sapillo Creek, and the Mimbres River -- carry fire toward "
            "Silver City and the Mimbres Valley. Vegetation transitions from Chihuahuan desert "
            "grassland and mesquite at lower elevations through pinon-juniper woodland into ponderosa "
            "pine, Douglas fir, and spruce-fir at higher elevations. The Gila NF has experienced "
            "extraordinary fire activity: the 2012 Whitewater-Baldy Fire (297,845 acres), the 2022 "
            "Black Fire (325,133 acres, second-largest in NM history), the 2013 Silver Fire (138,542 "
            "acres), and the 2025 Trout Fire (43,500+ acres) and Buck Fire (58,000+ acres) which "
            "together burned over 100,000 acres just 12 miles north of town. The remote, rugged "
            "terrain makes suppression extremely difficult, and fires can grow explosively before "
            "threatening the WUI interface around Silver City and the Mimbres Valley."
        ),
        "key_features": [
            {"name": "Pinos Altos Range", "bearing": "N", "distance_mi": 6,
             "type": "mountain", "notes": "Historic mining area at 7,840 ft in dense ponderosa; "
             "NM-15 passes through as only route to Gila Cliff Dwellings; primary fire approach"},
            {"name": "Black Range", "bearing": "NE", "distance_mi": 25,
             "type": "mountain_range", "notes": "Rugged range reaching 10,011 ft; site of 2022 "
             "Black Fire (325,133 acres); remote terrain makes suppression nearly impossible"},
            {"name": "Gila Wilderness", "bearing": "N", "distance_mi": 30,
             "type": "wilderness", "notes": "558,014 acres; first designated wilderness in US (1924); "
             "contains headwaters of Gila River; Whitewater-Baldy Fire burned here"},
            {"name": "Mimbres Valley", "bearing": "E", "distance_mi": 15,
             "type": "valley", "notes": "Agricultural valley with scattered rural homes; fire descends "
             "from mountains through multiple drainages; evacuation concerns for valley residents"},
            {"name": "Continental Divide", "bearing": "N", "distance_mi": 20,
             "type": "geographic", "notes": "CDT passes through Gila NF; divide creates complex wind "
             "patterns with fire able to approach from multiple directions"},
        ],
        "elevation_range_ft": (5900, 10895),
        "wui_exposure": (
            "high -- northern edge of town meets pinon-juniper and ponderosa directly; Pinos Altos "
            "community is deep WUI surrounded by dense forest; Mimbres Valley homes scattered in "
            "timbered foothills; 9,704 population in town plus surrounding rural communities"
        ),
        "historical_fires": [
            {
                "name": "Whitewater-Baldy Complex Fire",
                "year": 2012,
                "acres": 297845,
                "structures_destroyed": 19,
                "fatalities": 0,
                "cause": "lightning (two strikes)",
                "notes": (
                    "Two lightning-caused fires merged on May 24, 2012 in Gila Wilderness. "
                    "Burned 297,845 acres making it largest NM fire until 2022. Extreme fire "
                    "behavior in steep rugged terrain with 10,000-20,000 acre days and two "
                    "40,000+ acre days. Destroyed 12 homes and 7 outbuildings. Evacuated "
                    "Willow Creek cabins and village of Mogollon. Forced closure of Gila Cliff "
                    "Dwellings and Catwalk Recreation Area. Contained July 31, 2012."
                ),
            },
            {
                "name": "Silver Fire",
                "year": 2013,
                "acres": 138542,
                "structures_destroyed": 8,
                "fatalities": 0,
                "cause": "lightning",
                "notes": (
                    "Burned in Gila NF north and east of Silver City starting June 2013. "
                    "138,542 acres in steep terrain. Threatened Mimbres Valley communities. "
                    "Strong winds and rugged terrain made suppression extremely difficult."
                ),
            },
            {
                "name": "Black Fire",
                "year": 2022,
                "acres": 325133,
                "structures_destroyed": 2,
                "fatalities": 0,
                "cause": "human",
                "notes": (
                    "Started May 13, 2022 in Black Range northeast of Silver City. Burned "
                    "325,133 acres becoming second-largest fire in NM history. Surpassed "
                    "Whitewater-Baldy on June 9. Despite enormous size, remote terrain meant "
                    "limited structural damage (2 structures destroyed, 51 threatened)."
                ),
            },
            {
                "name": "Trout Fire",
                "year": 2025,
                "acres": 43547,
                "structures_destroyed": 5,
                "fatalities": 0,
                "cause": "under investigation",
                "notes": (
                    "Started in Gila NF 12 miles north of Silver City in June 2025. Forced "
                    "closure of NM-15. Governor declared emergency. Combined with nearby Buck "
                    "Fire (58,063 acres) to burn over 100,000 acres. Evacuations ordered for "
                    "multiple zones including Mimbres Valley communities."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "US-180 South",
                "direction": "south toward Deming (53 miles) and I-10",
                "lanes": 2,
                "bottleneck": "Two-lane highway through open terrain; long distance to services",
                "risk": "Primary evacuation route; generally viable as fires approach from north; "
                        "smoke may reduce visibility",
            },
            {
                "route": "NM-90 South",
                "direction": "south toward Lordsburg (65 miles) and I-10",
                "lanes": 2,
                "bottleneck": "Two-lane highway; sparse services",
                "risk": "Good alternate route away from fire area; long drive through desert",
            },
            {
                "route": "US-180 North",
                "direction": "north toward Glenwood and Reserve",
                "lanes": 2,
                "bottleneck": "Passes through heavily forested Gila NF; narrow and winding",
                "risk": "Route directly into fire area; likely closed during fires north of town; "
                        "not viable for evacuation from Gila NF fires",
            },
            {
                "route": "NM-15 North",
                "direction": "north through Pinos Altos toward Gila Cliff Dwellings",
                "lanes": 2,
                "bottleneck": "Extremely narrow, winding mountain road through dense forest; "
                              "no shoulders; sharp switchbacks",
                "risk": "Closed during 2025 Trout Fire; passes through most fire-prone terrain; "
                        "evacuation route for Pinos Altos community only in outbound direction",
            },
        ],
        "fire_spread_characteristics": (
            "Terrain-driven fire in extremely rugged canyon country. Fires in the Gila can grow to "
            "enormous size in remote wilderness before threatening WUI. Southwest winds push fire from "
            "Gila Wilderness toward Silver City through multiple drainages. Crown fire in continuous "
            "ponderosa and mixed-conifer canopy. Large boulders and steep slopes make direct attack "
            "impossible in many areas. Spotting distances of 1+ mile in extreme conditions. Fires can "
            "burn for weeks in remote terrain before threatening populated areas."
        ),
        "infrastructure_vulnerabilities": (
            "Water supply from Bear Creek and Gila River diversions vulnerable to post-fire "
            "contamination and debris flows. Western New Mexico University campus in town center. "
            "Gila Regional Medical Center is sole hospital for vast region. NM-15 is only access "
            "to Gila Cliff Dwellings and northern recreation areas. Mining infrastructure (Chino "
            "Mine / Santa Rita open pit) nearby. Limited telecommunications in surrounding areas."
        ),
        "demographics_risk_factors": (
            "Population 9,704 (2020 town) plus surrounding unincorporated communities. Significant "
            "retirement and artist community. University students at WNMU. High poverty rate. "
            "Remote location 110 miles from nearest interstate (I-10 at Deming or I-25 at "
            "Truth or Consequences). Many rural residents in surrounding mountains and Mimbres "
            "Valley live on unpaved roads with limited communication. Large area of Gila NF "
            "attracts backcountry recreationists who may need rescue during fire events."
        ),
    },

    # =========================================================================
    # 6. TAOS
    # =========================================================================
    "taos_nm": {
        "center": (36.408, -105.573),
        "terrain_notes": (
            "Taos sits at 6,969 ft on a high-desert mesa at the base of the Sangre de Cristo "
            "Mountains, with the Rio Grande Gorge to the west and the Taos Mountains rising "
            "dramatically to the east and northeast. Wheeler Peak (13,161 ft), the highest point "
            "in New Mexico, dominates the skyline to the northeast. The town is situated where "
            "three major watersheds converge: the Rio Pueblo de Taos, Rio Fernando de Taos, and "
            "Rio Hondo, all draining west from the Sangre de Cristos through forested canyons. "
            "These canyons are the primary fire threat corridors, funneling fire from dense mountain "
            "forests toward the populated mesa. Vegetation follows classic elevation gradients: "
            "sagebrush and pinon-juniper on the mesa (6,500-7,500 ft), ponderosa pine at mid "
            "elevations (7,500-9,000 ft), mixed conifer and aspen (9,000-11,500 ft), and alpine "
            "tundra above timberline. Fire-scar studies show the Taos Valley historically "
            "experienced frequent low-severity surface fires on 9-29 year intervals, but fire "
            "exclusion since 1899 has left all forest types without fire for over 125 years, "
            "creating dangerous fuel accumulations. The Hondo Fire (1996, 7,527 acres) burned with "
            "high severity north of town, and the Encebado Fire (2003, 5,400 acres) burned on Taos "
            "Pueblo lands in the Rio Pueblo de Taos watershed. The 2022 Hermits Peak/Calf Canyon Fire "
            "reached into Taos County, demonstrating that mega-fires can burn from the southern "
            "Sangre de Cristos to within threatening distance of Taos. 70% of the Sangre de Cristo "
            "forests near Taos are rated high to very high wildfire risk. Taos Pueblo, a 1,000-year-old "
            "UNESCO World Heritage Site, is surrounded by forested tribal lands and faces extreme fire "
            "threat to irreplaceable cultural resources."
        ),
        "key_features": [
            {"name": "Wheeler Peak", "bearing": "NE", "distance_mi": 15,
             "type": "mountain", "notes": "13,161 ft; highest point in New Mexico; alpine zone above "
             "dense spruce-fir forests that extend down to populated areas"},
            {"name": "Taos Pueblo", "bearing": "NE", "distance_mi": 3,
             "type": "cultural", "notes": "1,000-year-old UNESCO World Heritage Site; adobe structures "
             "surrounded by forested tribal lands; irreplaceable cultural resource at fire risk"},
            {"name": "Rio Grande Gorge", "bearing": "W", "distance_mi": 8,
             "type": "gorge", "notes": "800 ft deep basalt gorge; natural firebreak on west side of "
             "town; sagebrush plateau between town and gorge carries grass fire risk"},
            {"name": "Taos Ski Valley", "bearing": "NE", "distance_mi": 18,
             "type": "community", "notes": "Resort community at 9,207 ft in Hondo Canyon; dense "
             "spruce-fir forest; single-road access via NM-150; significant evacuation challenge"},
            {"name": "Rio Hondo Canyon", "bearing": "NE", "distance_mi": 5,
             "type": "canyon", "notes": "Deep canyon connecting Taos Ski Valley to Taos; major fire "
             "chimney with dense mixed conifer; Hondo Fire (1996) burned here"},
        ],
        "elevation_range_ft": (6500, 13161),
        "wui_exposure": (
            "high -- eastern neighborhoods and canyon communities (Arroyo Seco, Valdez, Arroyo Hondo, "
            "Taos Ski Valley) embedded in dense forest; Taos Pueblo surrounded by forested tribal "
            "lands; population ~6,500 in town plus substantial surrounding communities"
        ),
        "historical_fires": [
            {
                "name": "Hondo Fire",
                "year": 1996,
                "acres": 7527,
                "structures_destroyed": 1,
                "fatalities": 0,
                "cause": "unknown",
                "notes": (
                    "Burned with primarily high severity in Rio Hondo Canyon north of Taos "
                    "in May 1996. Demonstrated crown fire potential in dense mixed-conifer "
                    "stands. Threatened Arroyo Seco and canyon communities."
                ),
            },
            {
                "name": "Encebado Fire",
                "year": 2003,
                "acres": 5400,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "unknown",
                "notes": (
                    "Burned in Rio Pueblo de Taos watershed on Taos Pueblo lands in July "
                    "2003. Raised concerns about fire threat to Taos Pueblo cultural sites. "
                    "Demonstrated that fire can burn through tribal lands toward town."
                ),
            },
            {
                "name": "Hermits Peak / Calf Canyon Fire",
                "year": 2022,
                "acres": 341471,
                "structures_destroyed": 903,
                "fatalities": 0,
                "cause": "escaped prescribed burn (USFS)",
                "notes": (
                    "While centered in San Miguel and Mora counties, the fire extended into "
                    "Taos County. The 45-mile north-south footprint reached within threatening "
                    "distance of southern Taos County communities. Demonstrated mega-fire "
                    "potential in Sangre de Cristo forests near Taos."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "NM-68 South (Low Road to Santa Fe)",
                "direction": "south through Rio Grande canyon to Espanola",
                "lanes": 2,
                "bottleneck": "Narrow canyon road along Rio Grande; rock fall and flood risk; "
                              "winding with limited passing",
                "risk": "Primary route to Espanola and Santa Fe; can be cut by rockslides; "
                        "congestion in Pilar and Dixon sections",
            },
            {
                "route": "NM-518 South",
                "direction": "south toward Mora and Las Vegas NM",
                "lanes": 2,
                "bottleneck": "Mountain pass road through forested terrain",
                "risk": "Route through fire-prone forest; cut during 2022 Hermits Peak fire; "
                        "not reliable during fire events south of Taos",
            },
            {
                "route": "US-64 West",
                "direction": "west across Rio Grande Gorge toward Tres Piedras/Chama",
                "lanes": 2,
                "bottleneck": "Rio Grande Gorge Bridge (single span); open sagebrush plateau",
                "risk": "Good evacuation route away from mountain fire; bridge is single point "
                        "of failure; low fire risk on western plateau",
            },
            {
                "route": "NM-150 to Taos Ski Valley",
                "direction": "northeast into Hondo Canyon",
                "lanes": 2,
                "bottleneck": "Dead-end canyon road; no through route; narrows severely above Arroyo Seco",
                "risk": "Not an evacuation route -- endpoint; Ski Valley and canyon residents must "
                        "evacuate DOWN canyon on single road; extreme congestion risk",
            },
        ],
        "fire_spread_characteristics": (
            "Canyon-driven fire from three major drainages (Rio Hondo, Rio Pueblo, Rio Fernando) "
            "converging on town from the east. Southwest winds drive fire down-canyon toward mesa. "
            "Crown fire potential is extreme in dense mixed-conifer and ponderosa stands that have "
            "not burned in 125+ years. Surface fire in sagebrush-grassland on western mesa can spread "
            "rapidly toward town with rates of 3-5 mph in grass. Widespread fires historically burned "
            "synchronously across multiple watersheds during drought years. Spot fire distances of "
            "0.5-1 mile in conifer fuels."
        ),
        "infrastructure_vulnerabilities": (
            "Water supply from mountain watersheds at fire risk; Taos Pueblo's acequia system "
            "and sacred Blue Lake watershed at extreme risk. Holy Cross Hospital is sole hospital "
            "for region. Kit Carson Electric Cooperative lines through forested canyons are ignition "
            "sources. Natural gas service limited; many homes use propane tanks (explosion risk). "
            "Historic adobe buildings in Taos Plaza more fire-resistant but surrounding structures "
            "are wood-frame. NM-150 dead-end serves Ski Valley with no alternate exit."
        ),
        "demographics_risk_factors": (
            "Population ~6,500 in town, ~35,000 in county. Strong arts/tourism economy means "
            "large seasonal visitor population unfamiliar with fire risk. Taos Pueblo community "
            "of ~1,000 with sovereign governance. Significant elderly population. High poverty "
            "rate (~20%). Many homes in mountain communities accessible only by unpaved roads. "
            "Ski Valley population swells from ~100 year-round to thousands during season. "
            "Spanish-speaking communities may face language barriers in emergency communications."
        ),
    },

    # =========================================================================
    # 7. CLOUDCROFT
    # =========================================================================
    "cloudcroft_nm": {
        "center": (32.957, -105.742),
        "terrain_notes": (
            "Cloudcroft perches at 8,676 ft near the crest of the Sacramento Mountains in the "
            "Lincoln National Forest, making it one of the highest communities in southern New Mexico. "
            "The village is surrounded by dense mixed-conifer forest (Douglas fir, white fir, ponderosa "
            "pine, southwestern white pine, and Engelmann spruce) on all sides, with the terrain "
            "dropping steeply to the Tularosa Basin (4,300 ft) to the west along US-82. This dramatic "
            "3,500-4,000 ft elevation change over roughly 16 miles creates extreme topographic fire "
            "behavior: afternoon upslope winds driven by differential heating of the basin push fire "
            "rapidly up the western escarpment toward the village. The Sacramento Mountain escarpment "
            "faces west with 30-60% slopes, creating some of the most aggressive upslope fire "
            "conditions in New Mexico. Fuel loads in the Lincoln NF are critically high, with dense "
            "understory and heavy down timber from bark beetle mortality. The Scott Able Fire (2000) "
            "burned 20,717 acres and destroyed approximately 20 structures in the Sacramento Mountains "
            "southeast of Cloudcroft, while the Moser Fire (2024) burned 145 acres just 4 miles east "
            "of the village. The 2025 Gail Fire (235 acres) burned along US-82 east of Cloudcroft, "
            "forcing evacuations along the highway. Cloudcroft's position atop the narrow mountain "
            "crest means fire can approach from the west (Tularosa Basin upslope), east (Sacramento "
            "Valley side), or south (Sunspot Highway / NM-6563 corridor). The village is effectively "
            "a mountaintop island of development in continuous forest, with US-82 as the sole paved "
            "access route -- a narrow, winding two-lane mountain highway that serves as the single "
            "evacuation corridor for 750+ year-round residents and thousands of summer visitors."
        ),
        "key_features": [
            {"name": "Sacramento Peak / Sunspot", "bearing": "S", "distance_mi": 15,
             "type": "mountain", "notes": "9,255 ft; National Solar Observatory; accessed by "
             "NM-6563 through dense forest; remote fire risk"},
            {"name": "Tularosa Basin Escarpment", "bearing": "W", "distance_mi": 3,
             "type": "escarpment", "notes": "4,000 ft elevation drop creating extreme upslope "
             "fire behavior; US-82 descends through this zone"},
            {"name": "Bluff Springs", "bearing": "S", "distance_mi": 4,
             "type": "recreation", "notes": "Forested recreation area south of village; "
             "Scott Able Fire area; dense mixed conifer"},
            {"name": "Timberon", "bearing": "SE", "distance_mi": 20,
             "type": "community", "notes": "Remote mountain community at 6,800 ft; evacuated "
             "during 2025 Oakmont Fire; unpaved access roads"},
            {"name": "Fresnal Canyon", "bearing": "W", "distance_mi": 2,
             "type": "canyon", "notes": "Major drainage on west escarpment; US-82 follows this "
             "canyon; terrain-amplified upslope fire corridor"},
        ],
        "elevation_range_ft": (4300, 9255),
        "wui_exposure": (
            "extreme -- entire village of 750 residents embedded in continuous mixed-conifer forest "
            "at 8,676 ft; single access road (US-82); structures built among trees with minimal "
            "defensible space; summer tourist population multiplies fire evacuation challenge"
        ),
        "historical_fires": [
            {
                "name": "Scott Able Fire",
                "year": 2000,
                "acres": 20717,
                "structures_destroyed": 20,
                "fatalities": 0,
                "cause": "unknown",
                "notes": (
                    "Burned southeast of Cloudcroft in Sacramento Mountains. Destroyed "
                    "approximately 20 structures including several at Sivells Baptist Retreat. "
                    "Fire was seriously out of control for first 3-4 hours. Never directly "
                    "threatened Cloudcroft village but demonstrated extreme fire potential "
                    "in surrounding forest."
                ),
            },
            {
                "name": "Moser Fire",
                "year": 2024,
                "acres": 145,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "under investigation",
                "notes": (
                    "Burned approximately 4 miles east of Cloudcroft in May 2024. Prompted "
                    "evacuation orders for homes along US-82 from mile marker 21-23. "
                    "Contained relatively quickly but demonstrated ongoing fire risk."
                ),
            },
            {
                "name": "Gail Fire",
                "year": 2025,
                "acres": 235,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "under investigation",
                "notes": (
                    "Burned east of Cloudcroft along US-82 in March 2025. Prompted evacuations "
                    "in Otero County. Contained at 235 acres."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "US-82 West",
                "direction": "west descending to Alamogordo (16 miles, 4,000 ft descent)",
                "lanes": 2,
                "bottleneck": "Narrow winding mountain road with steep grades, sharp switchbacks, "
                              "and no shoulders; single-lane sections near village",
                "risk": "Only paved evacuation route; descent through fire-prone forest and canyon; "
                        "gridlock guaranteed during mass evacuation; fire can cut road from either side",
            },
            {
                "route": "US-82 East / NM-24 / NM-244",
                "direction": "east toward Weed, Pinon, and Artesia",
                "lanes": 2,
                "bottleneck": "Narrow mountain roads through forested terrain; limited services; "
                              "long distance to safety",
                "risk": "Alternate route through forest; may also be cut by fire; 80+ miles to "
                        "major services in Artesia",
            },
            {
                "route": "NM-130 (Sunspot Highway / NM-6563)",
                "direction": "south toward Sunspot Observatory",
                "lanes": 2,
                "bottleneck": "Dead-end scenic road; no through route",
                "risk": "Not a viable evacuation route; dead end at observatory",
            },
        ],
        "fire_spread_characteristics": (
            "Upslope fire behavior dominates from the Tularosa Basin. Differential heating creates "
            "strong afternoon upslope winds (15-30 mph) that push fire from lower-elevation grass and "
            "brush into continuous forest on the escarpment. Rates of spread of 2-4 mph upslope in "
            "timber are common during afternoon blowup periods. Ridge-top fires at Cloudcroft elevation "
            "can be driven by synoptic southwest winds creating extreme crown fire in dense mixed conifer. "
            "Night-time drainage winds reverse direction, potentially driving fire back toward basin "
            "communities. Bark beetle-killed timber throughout Lincoln NF has created extremely high "
            "fuel loads with standing dead snags and heavy down woody debris."
        ),
        "infrastructure_vulnerabilities": (
            "Water supply from mountain wells and springs; vulnerable to post-fire contamination. "
            "Single power feed along US-82 corridor. No hospital; nearest is Gerald Champion "
            "Regional Medical Center in Alamogordo (16 miles down mountain on congested road). "
            "Limited cellular coverage in surrounding forest. Septic systems throughout village; "
            "no central sewer. Many structures are older wooden cabins and lodges. Propane tanks "
            "common for heating."
        ),
        "demographics_risk_factors": (
            "Year-round population 750 (2020) but swells to 5,000+ during summer weekends and "
            "holidays. Tourism-dependent economy with many vacation cabins and rental properties. "
            "Significant elderly resident population. Many summer visitors unfamiliar with fire "
            "risk and evacuation routes. Remote location: 16 winding mountain miles from Alamogordo. "
            "Limited emergency services; volunteer fire department. Many properties have wooden "
            "construction, wood-shake roofs, and no defensible space in dense forest setting."
        ),
    },

    # =========================================================================
    # 8. ANGEL FIRE
    # =========================================================================
    "angel_fire_nm": {
        "center": (36.394, -105.285),
        "terrain_notes": (
            "Angel Fire occupies the heart of the Moreno Valley, a 15-mile-long, 3-mile-wide high "
            "alpine valley at 8,382 ft in the Sangre de Cristo Mountains of northern New Mexico. "
            "The valley is a broad synclinal basin bounded by uplifted mountain ranges on all sides: "
            "Agua Fria Peak (11,086 ft) anchors the south end, Wheeler Peak (13,161 ft) and the "
            "Taos Range rise to the northwest, and Baldy Mountain (12,441 ft) crowns the north end "
            "of the valley. The surrounding mountains are heavily forested with mixed conifer, "
            "spruce-fir, and aspen groves above 9,000 ft, transitioning to ponderosa pine and "
            "pinon-juniper on drier south-facing slopes at lower elevations. The valley floor is "
            "predominantly mountain grassland and sagebrush, but the western and eastern margins "
            "where residential development pushes into timber are high-risk WUI zones. The village "
            "borders Carson National Forest to the west, providing immediate exposure to expansive "
            "forested public lands identified by the federal government in 2022 as part of the "
            "Enchanted Circle Landscape -- one of the top 10 areas nationally most at-risk for "
            "catastrophic wildfire. The Moreno Valley's orientation creates a north-south wind "
            "tunnel during spring wind events, with gusts exceeding 50 mph channeled between the "
            "mountain walls. Fire approaching from the south through timber on Agua Fria Peak's "
            "slopes or from the west through Carson NF would be pushed rapidly up-valley by "
            "prevailing winds. The 2022 Hermits Peak/Calf Canyon Fire burned within 20 miles of "
            "Angel Fire to the south, prompting evacuation preparations. Angel Fire Resort's ski "
            "area and golf courses create some fuel breaks on the western valley edge, but "
            "residential subdivisions extending into timbered slopes above the valley floor remain "
            "extremely vulnerable. The valley's enclosed geography would trap smoke, reducing "
            "visibility and complicating evacuation during fire events."
        ),
        "key_features": [
            {"name": "Wheeler Peak", "bearing": "NW", "distance_mi": 12,
             "type": "mountain", "notes": "13,161 ft; highest point in NM; massive spruce-fir "
             "forests on eastern flanks drain toward Moreno Valley"},
            {"name": "Baldy Mountain", "bearing": "N", "distance_mi": 10,
             "type": "mountain", "notes": "12,441 ft; Philmont Scout Ranch on east slopes; dense "
             "mixed conifer and spruce-fir; headwaters of Cimarron watershed"},
            {"name": "Agua Fria Peak", "bearing": "S", "distance_mi": 5,
             "type": "mountain", "notes": "11,086 ft; south wall of Moreno Valley; fire from "
             "south would crest this ridge and descend into valley"},
            {"name": "Angel Fire Resort / Ski Area", "bearing": "W", "distance_mi": 1,
             "type": "recreation", "notes": "Ski mountain creating partial fuel break on western "
             "valley edge; cleared ski runs interspersed with dense timber"},
            {"name": "Coyote Creek Canyon", "bearing": "SE", "distance_mi": 4,
             "type": "canyon", "notes": "Drainage south from Moreno Valley through forested canyon; "
             "NM-434 follows this corridor as primary evacuation route"},
        ],
        "elevation_range_ft": (8200, 13161),
        "wui_exposure": (
            "high -- residential subdivisions extend into timbered slopes on valley margins; "
            "Carson NF borders village to west; population 1,192 plus substantial seasonal/resort "
            "population; Enchanted Circle identified as top-10 nationally at-risk fire landscape"
        ),
        "historical_fires": [
            {
                "name": "Hermits Peak / Calf Canyon Fire (threat)",
                "year": 2022,
                "acres": 341471,
                "structures_destroyed": 903,
                "fatalities": 0,
                "cause": "escaped prescribed burn (USFS)",
                "notes": (
                    "While the fire did not reach Angel Fire, it burned within 20 miles to "
                    "the south in the Sangre de Cristos, prompting evacuation preparations "
                    "and demonstrating that mega-fire in the range can threaten the Moreno Valley."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "NM-434 South",
                "direction": "south through Coyote Creek canyon toward Mora and I-25",
                "lanes": 2,
                "bottleneck": "Narrow canyon road through forested terrain; limited passing; "
                              "50+ miles to I-25 via Mora",
                "risk": "Primary exit route; passes through fire-prone canyon with dense timber; "
                        "can be cut by fire from south or west; very long evacuation distance",
            },
            {
                "route": "US-64 West (via NM-434 to Taos)",
                "direction": "west to Taos (24 miles) via Palo Flechado Pass",
                "lanes": 2,
                "bottleneck": "Palo Flechado Pass (9,107 ft) through dense forest on Carson NF; "
                              "steep and winding with no shoulders",
                "risk": "Route through highest-risk forest; pass can be closed by fire or snow; "
                        "merges with Taos traffic creating congestion",
            },
            {
                "route": "US-64 East",
                "direction": "east toward Eagle Nest and Cimarron",
                "lanes": 2,
                "bottleneck": "Open valley road to Eagle Nest; then narrow Cimarron Canyon",
                "risk": "Best route away from forest fire; open valley reduces fire risk; but "
                        "Cimarron Canyon beyond Eagle Nest is narrow with no alternate routes",
            },
        ],
        "fire_spread_characteristics": (
            "Valley wind tunnel effect channels strong north-south winds through the Moreno Valley, "
            "capable of driving fire rapidly along the valley axis. Fire descending from surrounding "
            "mountain slopes into the valley grassland can spread at 3-5 mph in grass/sage fuels. "
            "Crown fire in dense mixed-conifer on valley walls would produce extreme flame lengths "
            "and heavy spotting into the valley. The enclosed valley geometry traps smoke, creating "
            "zero-visibility conditions. Nighttime cold air drainage into the valley can create "
            "inversions that temporarily suppress fire but morning breakup produces explosive conditions."
        ),
        "infrastructure_vulnerabilities": (
            "Water supply from mountain wells and small reservoirs; limited capacity during high "
            "demand. No hospital; nearest is Holy Cross Hospital in Taos (24 miles over mountain "
            "pass). Single power feed from Kit Carson Electric. Propane tanks ubiquitous for heating "
            "at 8,400 ft elevation. Resort infrastructure (hotel, golf course, ski lifts) represents "
            "concentrated economic value. Many homes are vacation/seasonal with wooden construction."
        ),
        "demographics_risk_factors": (
            "Year-round population 1,192 (2020) but resort swells population to 5,000+ during ski "
            "season and summer events. Large proportion of vacation homes with absentee owners. "
            "Significant elderly retirement community. Tourism workforce in seasonal housing. "
            "Limited year-round emergency services; Moreno Valley Fire Department is volunteer. "
            "Remote location: 24 miles from Taos, 90+ miles from major hospitals in Santa Fe."
        ),
    },

    # =========================================================================
    # 9. JEMEZ SPRINGS
    # =========================================================================
    "jemez_springs_nm": {
        "center": (35.772, -106.690),
        "terrain_notes": (
            "Jemez Springs sits at 6,200 ft in a narrow canyon along the Jemez River in the heart "
            "of the Jemez Mountains, a volcanic mountain complex centered on the Valles Caldera. "
            "The village is confined to the narrow canyon bottom with steep forested walls rising "
            "1,500-3,000 ft on both sides. NM-4, the only road through the village, threads through "
            "this canyon and is the sole vehicular link to the outside world for Jemez Springs and "
            "numerous upstream communities. The Jemez Mountains have experienced an extraordinary "
            "series of catastrophic wildfires: the Las Conchas Fire (2011, 156,593 acres) burned "
            "across the entire eastern Jemez including Bandelier and threatened Los Alamos; the "
            "Thompson Ridge Fire (2013, 23,965 acres) burned on Valles Caldera lands above the "
            "village; and the Cerro Pelado Fire (2022, 45,605 acres) burned 7 miles east of Jemez "
            "Springs. Vegetation on the surrounding slopes includes dense ponderosa pine, mixed "
            "conifer (Douglas fir, white fir, blue spruce), and extensive stands of aspen, with "
            "pinon-juniper on drier south-facing slopes at lower elevations. The volcanic geology "
            "creates steep, cliffy terrain with numerous side canyons that funnel fire behavior. "
            "The Jemez River canyon acts as a chimney, channeling winds and fire drafts along its "
            "axis. Upcanyon (north) winds during afternoon heating push fire through the canyon "
            "toward the village and downstream communities including Jemez Pueblo. The village's "
            "position at the bottom of a narrow canyon makes it extremely vulnerable to fire "
            "descending from either canyon wall, with virtually no defensible space between the "
            "forested slopes and structures. Post-fire debris flows and flooding in the canyon "
            "have caused repeated devastation following upslope burns, as burned volcanic soils "
            "are highly erodible. The Thompson Ridge Fire burn scar above the village continues "
            "to produce debris flows during monsoon storms."
        ),
        "key_features": [
            {"name": "Valles Caldera", "bearing": "NE", "distance_mi": 8,
             "type": "caldera", "notes": "89,000-acre volcanic caldera; grassland interior but "
             "dense forest on rim; Thompson Ridge Fire burned caldera slopes above village"},
            {"name": "Redondo Peak", "bearing": "NE", "distance_mi": 10,
             "type": "mountain", "notes": "11,253 ft resurgent dome in Valles Caldera; dense "
             "spruce-fir forests; Thompson Ridge Fire burned around it"},
            {"name": "Jemez River Canyon", "bearing": "through village", "distance_mi": 0,
             "type": "canyon", "notes": "Narrow canyon confining village to riverbed floor; acts "
             "as fire chimney; NM-4 follows canyon as sole access road"},
            {"name": "Jemez Pueblo", "bearing": "S", "distance_mi": 12,
             "type": "tribal_land", "notes": "Pueblo community downstream on Jemez River; fire "
             "and debris flows from upstream affect pueblo; sovereign land management"},
            {"name": "Sierra Los Pinos", "bearing": "E", "distance_mi": 5,
             "type": "community", "notes": "Mountain subdivision east of Jemez Springs; evacuated "
             "during 2022 Cerro Pelado Fire; dense forest setting"},
        ],
        "elevation_range_ft": (6000, 11253),
        "wui_exposure": (
            "extreme -- tiny village (population 198) confined to narrow canyon bottom with "
            "forested canyon walls immediately adjacent to structures; no defensible space; "
            "single road (NM-4) for access and evacuation; repeated fire impacts"
        ),
        "historical_fires": [
            {
                "name": "Las Conchas Fire",
                "year": 2011,
                "acres": 156593,
                "structures_destroyed": 63,
                "fatalities": 0,
                "cause": "tree fell on power line",
                "notes": (
                    "Massive fire that burned across the eastern Jemez Mountains. Started "
                    "June 26, 2011. Burned 156,593 acres including Santa Fe NF, Bandelier, "
                    "Valles Caldera, and tribal lands. Threatened Los Alamos and prompted "
                    "evacuations. Catastrophic post-fire flooding devastated drainages."
                ),
            },
            {
                "name": "Thompson Ridge Fire",
                "year": 2013,
                "acres": 23965,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "downed power line",
                "notes": (
                    "Burned 23,965 acres on Valles Caldera National Preserve above Jemez "
                    "Springs starting May 31, 2013. Steep, rugged terrain with mixed conifer "
                    "and spruce-fir fuels. Burned primarily at moderate severity with mosaic "
                    "pattern. Only 640 of 24,000 acres burned at high intensity. Topographic "
                    "features helped limit fire momentum. Burn scar continues to produce "
                    "debris flows during monsoon storms threatening village below."
                ),
            },
            {
                "name": "Cerro Pelado Fire",
                "year": 2022,
                "acres": 45605,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "debris burning / prescribed burn residual",
                "notes": (
                    "Burned 45,605 acres about 7 miles east of Jemez Springs starting April "
                    "22, 2022. Prompted evacuations of Sierra Los Pinos and Los Griegos "
                    "communities. USFS investigation concluded probable cause was debris pile "
                    "burning from logging activity ignited months earlier."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "NM-4 South (downstream)",
                "direction": "south through Jemez Pueblo to US-550 at San Ysidro",
                "lanes": 2,
                "bottleneck": "Narrow canyon road following Jemez River; rock fall and flood "
                              "risk; passes through Jemez Pueblo; 35 miles to San Ysidro",
                "risk": "Only viable evacuation route for most fire scenarios; can be cut by "
                        "fire crossing canyon or debris flows from burned slopes above; "
                        "long distance through canyon to open terrain",
            },
            {
                "route": "NM-4 North / NM-126",
                "direction": "north toward La Cueva / Fenton Lake and east toward Los Alamos",
                "lanes": 2,
                "bottleneck": "Mountain road climbing through dense forest to Valles Caldera; "
                              "narrow with sharp curves; high elevation pass",
                "risk": "Route directly through highest-risk fire terrain; passes through "
                        "Thompson Ridge and Las Conchas burn scars; likely first route closed "
                        "during fire events; not viable evacuation route for most fire scenarios",
            },
        ],
        "fire_spread_characteristics": (
            "Canyon-chimney effect dominates: afternoon heating drives strong upcanyon winds that "
            "push fire through the narrow Jemez River canyon at accelerated rates. Fire descending "
            "from either canyon wall can reach the village in minutes due to steep slopes and short "
            "horizontal distance. Crown fire on the volcanic canyon slopes produces extreme radiant "
            "heat in the confined space. Spotting across the narrow canyon is common. Fires on the "
            "Valles Caldera rim above the village can burn rapidly in spruce-fir and then descend "
            "through mixed conifer into the canyon. Post-fire debris flows from burned slopes are a "
            "secondary catastrophic hazard, with volcanic soils extremely prone to erosion."
        ),
        "infrastructure_vulnerabilities": (
            "Village water from Jemez River and mountain springs; contaminated by fire debris and "
            "ash flows. NM-4 is sole road link and is frequently damaged by debris flows and "
            "flooding. No hospital; nearest is in Los Alamos (40 miles) or Albuquerque (90 miles). "
            "Geothermal hot springs (Bath House) are primary economic asset. Limited power "
            "infrastructure with above-ground lines through forest. No cellular coverage in parts "
            "of canyon. Historic structures vulnerable to fire."
        ),
        "demographics_risk_factors": (
            "Tiny year-round population of 198 (2020) but day visitors to hot springs and recreation "
            "areas swell numbers significantly. Many seasonal residents. Surrounding communities "
            "(Sierra Los Pinos, La Cueva, Jemez Pueblo) depend on same NM-4 corridor. Limited "
            "emergency services. Isolated canyon location means long response times from outside "
            "agencies. Many residents are elderly or have limited mobility."
        ),
    },

    # =========================================================================
    # 10. RED RIVER
    # =========================================================================
    "red_river_nm": {
        "center": (36.708, -105.406),
        "terrain_notes": (
            "Red River is a narrow mountain town at 8,671 ft squeezed into the Red River canyon at "
            "the base of the Sangre de Cristo Mountains in northern New Mexico. The town stretches "
            "linearly for approximately 2 miles along the Red River, which originates from the "
            "northern slopes of Wheeler Peak (13,161 ft). Canyon walls rise steeply on both sides "
            "to ridgelines at 10,000-12,000 ft, with the town occupying a canyon floor barely "
            "0.25 miles wide at its narrowest points. The surrounding Carson National Forest is "
            "densely forested with Engelmann spruce, subalpine fir, Douglas fir, and aspen at "
            "higher elevations, transitioning to ponderosa pine and mixed conifer at the canyon "
            "floor. The canyon geometry creates an extreme fire trap: the steep walls funnel winds "
            "along the canyon axis, and fire burning on either wall would produce intense radiant "
            "heat and spotting across the narrow canyon directly into town structures. Red River is "
            "part of the Enchanted Circle, identified in 2022 by federal authorities as one of the "
            "top 10 landscapes nationally most at-risk for catastrophic wildfire. The Enchanted "
            "Circle Scenic Byway (NM-38) is the only through road, entering from the west via "
            "Questa and exiting east toward Eagle Nest through a narrow mountain pass. Both "
            "approaches traverse dense forest through narrow canyons. A century of fire suppression "
            "has left the surrounding forests critically overloaded with fuels; the natural fire "
            "return interval for these mid-elevation forests was historically 10-25 years, but "
            "many stands have not burned in 120+ years. Dense understory, heavy down timber, and "
            "beetle-killed standing dead trees create conditions for extreme crown fire runs. The "
            "town's position in a narrow, east-west trending canyon means fire approaching from "
            "the south (from Wheeler Peak drainage) would be pushed directly into town by "
            "prevailing upslope afternoon winds."
        ),
        "key_features": [
            {"name": "Wheeler Peak", "bearing": "S", "distance_mi": 6,
             "type": "mountain", "notes": "13,161 ft; highest point in NM; Red River originates from "
             "northern slopes; massive spruce-fir forests above town"},
            {"name": "Red River Ski Area", "bearing": "SE", "distance_mi": 1,
             "type": "recreation", "notes": "Ski runs on south-facing slopes above town; cleared "
             "terrain provides partial fuel break but surrounded by dense forest"},
            {"name": "Goose Lake", "bearing": "NE", "distance_mi": 4,
             "type": "alpine", "notes": "Alpine lake at 11,600 ft above town; spruce-fir forests "
             "on approach; backcountry area with no road access"},
            {"name": "Red River Canyon Narrows", "bearing": "W", "distance_mi": 2,
             "type": "canyon", "notes": "Narrowest section of canyon west of town where NM-38 "
             "threads between steep walls; critical evacuation choke point"},
            {"name": "Enchanted Circle Scenic Byway", "bearing": "through town", "distance_mi": 0,
             "type": "road", "notes": "NM-38 loop connecting Red River, Eagle Nest, Angel Fire, "
             "Taos, and Questa; sole through-road for the community"},
        ],
        "elevation_range_ft": (8400, 13161),
        "wui_exposure": (
            "extreme -- entire town of 594 residents in narrow canyon with forested walls; "
            "structures immediately adjacent to dense timber; no defensible space possible in "
            "narrow canyon setting; part of nationally identified top-10 at-risk fire landscape"
        ),
        "historical_fires": [
            {
                "name": "Enchanted Circle prescribed burns (ongoing)",
                "year": 2024,
                "acres": 900,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "prescribed burn (USFS Carson NF)",
                "notes": (
                    "Carson National Forest has been conducting prescribed burns near Angel Fire "
                    "and Red River communities to reduce fuel loads. Part of multi-year effort to "
                    "protect Enchanted Circle communities from catastrophic wildfire."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "NM-38 West",
                "direction": "west through canyon to Questa (12 miles)",
                "lanes": 2,
                "bottleneck": "Narrow canyon road with steep walls; rock fall risk; narrows to "
                              "near single-lane at canyon pinch points; follows Red River",
                "risk": "Primary evacuation route; canyon can be blocked by fire, rockfall, or "
                        "flooding; limited passing opportunities; dense forest on both sides",
            },
            {
                "route": "NM-38 East",
                "direction": "east over Bobcat Pass to Eagle Nest (16 miles)",
                "lanes": 2,
                "bottleneck": "Climbs to Bobcat Pass (9,820 ft) through dense spruce-fir forest; "
                              "steep grades with sharp switchbacks",
                "risk": "Alternate evacuation route but passes through highest-elevation, densest "
                        "forest; pass may be impassable in winter; fire on south-facing slopes "
                        "above road could cut route quickly",
            },
        ],
        "fire_spread_characteristics": (
            "Canyon-channeled winds accelerate fire along the Red River corridor. The narrow canyon "
            "geometry creates intense radiant heating across the canyon floor when either wall is "
            "burning. Upslope afternoon winds from the south (from Wheeler Peak drainage) push fire "
            "into town. Crown fire in dense spruce-fir at these elevations (8,600-12,000 ft) produces "
            "extreme flame lengths and prolific spotting. The high-elevation fuels burn with exceptional "
            "intensity once ignited. Mass spotting across the 0.25-mile canyon width is likely during "
            "crown fire events. Steep terrain creates fire whirls and extreme turbulence."
        ),
        "infrastructure_vulnerabilities": (
            "Water from Red River and mountain wells; vulnerable to post-fire contamination and "
            "debris flows. No hospital; nearest is Holy Cross Hospital in Taos (35 miles). Kit "
            "Carson Electric power lines through forest are ignition risk. Propane tanks throughout "
            "town for heating at high elevation. NM-38 is sole road link and vulnerable to rockfall, "
            "flood, and fire closure. Limited cell service. Town economy entirely tourism-dependent."
        ),
        "demographics_risk_factors": (
            "Year-round population 594 (2020) but tourist population swells to several thousand "
            "during ski season and summer. Many vacation homes and cabins. Significant elderly "
            "residents. Tourism workforce in seasonal housing. Very limited emergency services; "
            "volunteer fire department. Remote mountain location 35 miles from nearest hospital. "
            "Many visitors unfamiliar with fire risk and evacuation routes."
        ),
    },

    # =========================================================================
    # 11. RUIDOSO DOWNS
    # =========================================================================
    "ruidoso_downs_nm": {
        "center": (33.328, -105.604),
        "terrain_notes": (
            "Ruidoso Downs sits at 6,417 ft at the eastern mouth of the Rio Ruidoso canyon where "
            "the mountains open onto the Hondo Valley, approximately 3 miles east-southeast of "
            "Ruidoso. The city occupies the transition zone where the Sacramento Mountains meet the "
            "high plains, with forested slopes rising to the west and north and open ranchland "
            "spreading east along the Rio Hondo. US-70 runs east-west through the city as the main "
            "commercial corridor. The terrain is less steep than Ruidoso proper, but the city remains "
            "highly vulnerable as it lies directly in the path of fire funneling out of the Rio "
            "Ruidoso canyon. The 2024 South Fork Fire demonstrated this catastrophically: fire that "
            "originated on the Mescalero Apache Reservation south of Ruidoso burned through the "
            "canyon and threatened Ruidoso Downs, forcing evacuation of the entire community. The "
            "Ruidoso Downs Race Track and Casino, home of the world's richest quarter horse race "
            "(the All American Futurity), is a major economic anchor employing hundreds and housing "
            "approximately 1,000 horses during racing season. The horse racing facility's barns, "
            "while built of concrete and steel with fire suppression, required emergency evacuation "
            "of 1,000 horses to facilities as far as Albuquerque during the 2024 fires. Vegetation "
            "around Ruidoso Downs includes pinon-juniper woodland on surrounding hills and valley "
            "grassland, with denser ponderosa and mixed conifer on slopes to the west. The Hondo "
            "Valley east of town carries grass and agricultural fuels that can spread fire rapidly. "
            "The city's position at the canyon mouth makes it a funnel point where fire, smoke, and "
            "post-fire debris flows from the entire upper Rio Ruidoso watershed converge."
        ),
        "key_features": [
            {"name": "Ruidoso Downs Race Track", "bearing": "central", "distance_mi": 0,
             "type": "facility", "notes": "Major horse racing facility; 1,000+ horses during season; "
             "concrete/steel barns with fire suppression; All American Futurity $3M purse"},
            {"name": "Rio Ruidoso Canyon Mouth", "bearing": "W", "distance_mi": 2,
             "type": "canyon", "notes": "Fire funnel point where canyon opens to valley; 2024 "
             "South Fork Fire approached through this corridor"},
            {"name": "Sierra Blanca", "bearing": "NW", "distance_mi": 15,
             "type": "mountain", "notes": "11,981 ft; massive forested peak feeding fire and "
             "debris flows down Rio Ruidoso drainage toward Ruidoso Downs"},
            {"name": "Mescalero Apache Reservation", "bearing": "SW", "distance_mi": 5,
             "type": "tribal_land", "notes": "460,000 acres bordering area; South Fork and Salt "
             "fires originated here; dense timber with limited access for suppression"},
            {"name": "Hondo Valley", "bearing": "E", "distance_mi": 3,
             "type": "valley", "notes": "Agricultural valley along US-70; grass fuels can carry "
             "fire rapidly; primary evacuation corridor toward Roswell"},
        ],
        "elevation_range_ft": (6200, 7500),
        "wui_exposure": (
            "high -- population 2,620 at canyon mouth transition zone; directly in path of fire "
            "exiting Rio Ruidoso canyon; 2024 South Fork Fire proved catastrophic fire can reach "
            "Ruidoso Downs from Mescalero lands; horse racing facility with 1,000 animals adds "
            "unique mass-evacuation challenge"
        ),
        "historical_fires": [
            {
                "name": "South Fork Fire",
                "year": 2024,
                "acres": 24403,
                "structures_destroyed": 1400,
                "fatalities": 2,
                "cause": "under investigation",
                "notes": (
                    "Fire that devastated Ruidoso on June 17, 2024, forced evacuation of Ruidoso "
                    "Downs on June 18. Approximately 1,000 horses evacuated from race track to "
                    "state fairgrounds in Albuquerque and other facilities. Track barns survived "
                    "due to concrete/steel construction and fire suppression. Some employees lost "
                    "homes. Combined with Salt Fire on Mescalero Reservation. Two fatalities, "
                    "~1,400 structures destroyed across broader area."
                ),
            },
            {
                "name": "Little Bear Fire",
                "year": 2012,
                "acres": 44330,
                "structures_destroyed": 254,
                "fatalities": 0,
                "cause": "lightning",
                "notes": (
                    "Burned primarily north of Ruidoso but ash and smoke impacted Ruidoso Downs. "
                    "Demonstrated wildfire threat to the broader Ruidoso area."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "US-70 East",
                "direction": "east through Hondo Valley toward Roswell (75 miles)",
                "lanes": 2,
                "bottleneck": "Two-lane highway through open terrain; long distance to major services; "
                              "merges with all Ruidoso evacuation traffic",
                "risk": "Primary and most viable evacuation route; away from fire area; but absorbs "
                        "all traffic from both Ruidoso and Ruidoso Downs; gridlock during mass evacuation",
            },
            {
                "route": "US-70 West (through Ruidoso)",
                "direction": "west toward Tularosa via Mescalero and Apache Summit",
                "lanes": 2,
                "bottleneck": "Must pass through Ruidoso; climbs Apache Summit through dense forest",
                "risk": "Route through fire area; closed during 2024 fires; not viable when fire "
                        "approaches from south/west",
            },
            {
                "route": "NM-48 North (via Ruidoso)",
                "direction": "north toward Capitan",
                "lanes": 2,
                "bottleneck": "Must first transit through Ruidoso; mountain road through forest",
                "risk": "Requires passing through Ruidoso which may already be evacuating; "
                        "forested terrain along route",
            },
        ],
        "fire_spread_characteristics": (
            "Fire funneling out of the Rio Ruidoso canyon is the primary threat. The canyon mouth "
            "creates a natural convergence zone where fire, smoke, and embers concentrate. South and "
            "southwest winds push fire from Mescalero Reservation through the canyon directly toward "
            "Ruidoso Downs. Grass and pinon-juniper fuels around the city can carry fire at 3-5 mph. "
            "Post-fire debris flows from burned upper watershed are a secondary catastrophic threat, "
            "as demonstrated by July 2024 flooding. Ember showers from crown fire upcanyon can ignite "
            "structures in Ruidoso Downs well ahead of the fire front."
        ),
        "infrastructure_vulnerabilities": (
            "Ruidoso Downs Race Track and Casino is major economic asset employing hundreds. "
            "Horse evacuation requires specialized trailers and receiving facilities -- 2024 "
            "evacuation moved 1,000 horses 200 miles to Albuquerque. Water supply shares Ruidoso "
            "system from mountain reservoirs; vulnerable to post-fire contamination. US-70 serves "
            "as both commercial lifeline and sole reliable evacuation route. Limited medical "
            "facilities; depends on Lincoln County Medical Center in Ruidoso."
        ),
        "demographics_risk_factors": (
            "Population 2,620 (2020) but swells significantly during racing season (May-September). "
            "Large horse industry workforce in temporary and low-income housing. Significant "
            "Hispanic/Latino community. Many seasonal workers with limited English. Lower median "
            "income than Ruidoso; many older mobile homes and frame construction. Post-2024 fire "
            "housing crisis affects both communities. Racing industry provides major employment "
            "but workforce housing is often substandard and in fire-vulnerable locations."
        ),
    },

    # =========================================================================
    # 12. RESERVE / GLENWOOD
    # =========================================================================
    "reserve_nm": {
        "center": (33.713, -108.758),
        "terrain_notes": (
            "Reserve is the county seat of Catron County -- New Mexico's third-least-populous county "
            "(3,579 people in 6,928 sq mi) -- situated at 5,771 ft in the upper San Francisco River "
            "valley in the remote mountains of western New Mexico. Glenwood, 38 miles south on US-180, "
            "sits at 4,712 ft where Whitewater Creek enters the San Francisco River. Both communities "
            "are surrounded by the Gila National Forest, with the Gila Wilderness to the east and the "
            "Mogollon Mountains to the south. The terrain is spectacularly rugged: deep canyons (San "
            "Francisco River Box, Whitewater Canyon, Mogollon Creek) cut through volcanic and "
            "sedimentary formations, with peaks reaching over 10,000 ft in the Mogollon Range "
            "(Whitewater Baldy at 10,895 ft, Mogollon Baldy at 10,770 ft). Vegetation ranges from "
            "cottonwood riparian forest in canyon bottoms through pinon-juniper and ponderosa pine at "
            "mid-elevations to dense mixed conifer and spruce-fir on the highest peaks. This area has "
            "experienced some of the most extreme fire behavior in New Mexico history. The 2012 "
            "Whitewater-Baldy Complex Fire burned 297,845 acres with explosive growth of 10,000-40,000 "
            "acres per day, destroying homes and forcing evacuation of Willow Creek and Mogollon. The "
            "2022 Black Fire burned 325,133 acres to the east in the Black Range. The extreme "
            "remoteness and rugged terrain make fire suppression nearly impossible in the initial "
            "stages; fires routinely burn for weeks before threatening communities. Canyon topography "
            "creates extreme fire behavior with flame lengths exceeding 200 ft in confined spaces. "
            "Large boulders falling in steep burning canyons endanger firefighters. Reserve and Glenwood "
            "are connected to the outside world by US-180 and NM-12, both narrow two-lane highways "
            "that traverse heavily forested terrain for 60-100 miles before reaching a town of any size. "
            "This extreme isolation means evacuation distances are enormous and mutual aid response "
            "times are measured in hours."
        ),
        "key_features": [
            {"name": "Whitewater Baldy", "bearing": "SE", "distance_mi": 20,
             "type": "mountain", "notes": "10,895 ft; namesake of 2012 fire; Gila Wilderness "
             "high point; dense spruce-fir forests; extremely rugged and remote"},
            {"name": "Mogollon Baldy", "bearing": "S", "distance_mi": 25,
             "type": "mountain", "notes": "10,770 ft in Mogollon Range; historic mining town of "
             "Mogollon below; dense mixed conifer; fire lookout tower"},
            {"name": "Catwalk Recreation Area (Glenwood)", "bearing": "S", "distance_mi": 38,
             "type": "recreation", "notes": "Whitewater Canyon suspended walkway above Glenwood; "
             "destroyed by post-fire flooding 2013, rebuilt 2016; major tourist attraction"},
            {"name": "San Francisco River Box", "bearing": "through Reserve", "distance_mi": 0,
             "type": "canyon", "notes": "Deep canyon carrying San Francisco River; Reserve built "
             "along narrow valley floor; confines fire behavior and limits escape routes"},
            {"name": "Mogollon (ghost town)", "bearing": "S", "distance_mi": 15,
             "type": "community", "notes": "Historic mining town at 6,500 ft in narrow canyon; "
             "evacuated during Whitewater-Baldy Fire; extremely limited access"},
        ],
        "elevation_range_ft": (4700, 10895),
        "wui_exposure": (
            "moderate-high -- small population (Reserve 293, Glenwood ~150) but completely embedded "
            "in Gila NF with no buffer; extreme remoteness means no rapid mutual aid; surrounding "
            "forest has experienced 600,000+ acres of fire in past decade; structures scattered along "
            "river valleys with forest immediately adjacent"
        ),
        "historical_fires": [
            {
                "name": "Whitewater-Baldy Complex Fire",
                "year": 2012,
                "acres": 297845,
                "structures_destroyed": 19,
                "fatalities": 0,
                "cause": "lightning (two separate strikes)",
                "notes": (
                    "Two lightning-caused fires (Whitewater detected May 16, Baldy detected May 9) "
                    "merged on May 24, 2012. Burned 297,845 acres in Gila NF and Gila Wilderness. "
                    "Explosive growth with 10,000-20,000 acre days and two 40,000+ acre days. "
                    "Destroyed 12 homes and 7 outbuildings. Evacuated 57 Willow Creek cabins and "
                    "village of Mogollon. Forced closure of Gila Cliff Dwellings and Catwalk "
                    "Recreation Area. Extreme terrain with large boulders falling in burning canyons "
                    "forced crew evacuations. Fully contained July 31, 2012. Was largest NM fire "
                    "until surpassed by Hermits Peak/Calf Canyon in 2022."
                ),
            },
            {
                "name": "Black Fire",
                "year": 2022,
                "acres": 325133,
                "structures_destroyed": 2,
                "fatalities": 0,
                "cause": "human",
                "notes": (
                    "Burned 325,133 acres in Black Range east of Reserve, May-July 2022. "
                    "Second-largest fire in NM history. Despite enormous area, remote terrain "
                    "meant limited structural loss. Impacted watersheds draining toward "
                    "communities in the Mimbres Valley and Rio Grande."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "US-180 South (to Silver City)",
                "direction": "south through Glenwood toward Silver City (99 miles from Reserve)",
                "lanes": 2,
                "bottleneck": "Narrow mountain highway through Gila NF; 99 miles of forested "
                              "terrain to Silver City; limited services; Alma and Glenwood only stops",
                "risk": "Extremely long evacuation distance through fire-prone terrain; route may "
                        "be cut by fire between Reserve and Glenwood; no alternate roads",
            },
            {
                "route": "NM-12 East",
                "direction": "east through Apache Creek toward Datil and US-60",
                "lanes": 2,
                "bottleneck": "Narrow mountain road; crosses Continental Divide; 60+ miles to Datil; "
                              "no services",
                "risk": "Long distance through remote terrain; limited cell service; passes through "
                        "areas burned by Black Fire; road condition varies",
            },
            {
                "route": "US-180 North",
                "direction": "north toward Luna and Alpine AZ (50 miles to Arizona line)",
                "lanes": 2,
                "bottleneck": "Extremely remote; crosses into Arizona high country; forested terrain",
                "risk": "Route through very remote forest; crosses state line complicating "
                        "jurisdictional response; limited services for 100+ miles",
            },
        ],
        "fire_spread_characteristics": (
            "Extremely rugged canyon-driven fire behavior in some of the most inaccessible terrain "
            "in the Southwest. Fires can grow to 10,000-40,000 acres per day during wind events in "
            "the Mogollon Range. Canyon confinement produces flame lengths exceeding 200 ft. Large "
            "boulders dislodge from steep slopes during burning, creating additional hazards. Spotting "
            "distances of 1+ mile in mixed conifer. Fire can burn for weeks in wilderness before "
            "threatening communities. Once burning, the terrain makes direct suppression impossible "
            "in most areas, and containment depends on weather changes or existing burn scars."
        ),
        "infrastructure_vulnerabilities": (
            "Water from San Francisco River and mountain wells; vulnerable to post-fire contamination "
            "and debris flows. No hospital; nearest is 100+ miles away in Silver City or Socorro. "
            "Single power feed for each community. Cell service extremely limited or nonexistent "
            "in surrounding forest. Volunteer fire departments with minimal equipment. Catwalk "
            "Recreation Area (major tourist draw for Glenwood) destroyed once by post-fire flooding. "
            "US-180 and NM-12 are sole links to outside world; damage or closure isolates communities."
        ),
        "demographics_risk_factors": (
            "Reserve population 293 (2020), Glenwood ~150. Catron County population just 3,579 in "
            "area larger than Connecticut. Extremely low-density rural ranching and retirement "
            "community. Significant elderly population with limited mobility. Many residents on "
            "fixed incomes in older housing. Nearest hospital 100+ miles away. Volunteer emergency "
            "services only. Strong self-reliance culture but limited evacuation capacity. Scattered "
            "ranch properties and summer cabins in remote forest settings are virtually indefensible."
        ),
    },

    # =========================================================================
    # 13. TRES PIEDRAS / CARSON NF COMMUNITIES
    # =========================================================================
    "tres_piedras_nm": {
        "center": (36.648, -105.965),
        "terrain_notes": (
            "Tres Piedras is a small settlement at 8,081 ft at the crossroads of US-64 and US-285 "
            "on the Taos Plateau, approximately 30 miles northwest of Taos. The community sits on "
            "the western edge of the Carson National Forest in a transition zone between the forested "
            "Sangre de Cristo and Tusas Mountains to the east and the open sagebrush plateau dropping "
            "toward the Rio Grande Gorge to the south. The surrounding Carson NF lands carry dense "
            "ponderosa pine and mixed conifer on north-facing slopes, with pinon-juniper woodland on "
            "drier exposures and sagebrush grassland on the plateau. The Tres Piedras Ranger District "
            "of Carson NF is the local administrative unit managing fire risk in the area. Forest "
            "restoration and prescribed burning have been ongoing priorities, with the Rio Chama "
            "Collaborative Forest Landscape Restoration Project spanning 3.8 million acres across "
            "northern New Mexico and southern Colorado, including lands around Tres Piedras. This "
            "massive project focuses on restoring watersheds that serve as major drinking water "
            "suppliers for downstream cities including Santa Fe and Albuquerque. Despite these "
            "efforts, the surrounding forests remain critically overloaded with fuels from a century "
            "of fire suppression. The Tres Lagunas Fire (2013, 10,219 acres) burned 10 miles north "
            "of Pecos in the Santa Fe NF, demonstrating that fires started by downed power lines "
            "can grow rapidly in the Sangre de Cristo forests that also surround Tres Piedras. The "
            "2025 Tusas Fire burned near Las Tablas, southwest of Tres Piedras, on Carson NF lands. "
            "The flat-to-rolling plateau terrain around Tres Piedras allows fire to spread rapidly "
            "in grass and sage during spring wind events (April-June), while the forested mountain "
            "slopes to the east can produce crown fire in dense conifer stands. The community's "
            "position at a major highway intersection provides better evacuation options than most "
            "mountain communities, but surrounding scattered rural homes and cabins in the forest "
            "are highly vulnerable."
        ),
        "key_features": [
            {"name": "Tusas Mountains", "bearing": "NE", "distance_mi": 10,
             "type": "mountain_range", "notes": "Forested range northeast of Tres Piedras; "
             "Carson NF lands with dense mixed conifer; fire threat to communities on western slopes"},
            {"name": "Rio Grande Gorge", "bearing": "S", "distance_mi": 12,
             "type": "gorge", "notes": "800 ft deep basalt gorge; natural firebreak but plateau "
             "grasses between Tres Piedras and gorge carry fire in wind"},
            {"name": "Carson NF Tres Piedras Ranger District", "bearing": "E", "distance_mi": 2,
             "type": "forest", "notes": "Local forest management unit; ongoing prescribed burns "
             "and restoration work; Willow and Dorado/Canada del Agua treatment areas"},
            {"name": "US-64 / US-285 Intersection", "bearing": "central", "distance_mi": 0,
             "type": "road", "notes": "Major highway crossroads providing four-direction evacuation "
             "options; better access than most mountain communities"},
            {"name": "Rio Chama Watershed", "bearing": "NW", "distance_mi": 15,
             "type": "watershed", "notes": "Critical drinking water supply for Santa Fe and "
             "Albuquerque; 3.8M-acre restoration project includes Tres Piedras area"},
        ],
        "elevation_range_ft": (7500, 10720),
        "wui_exposure": (
            "moderate -- small population (~1,000 in surrounding area) scattered in forest and "
            "plateau setting; Carson NF immediately adjacent; scattered rural homes and cabins "
            "in forest are indefensible; highway crossroads provides evacuation advantage"
        ),
        "historical_fires": [
            {
                "name": "Tres Lagunas Fire",
                "year": 2013,
                "acres": 10219,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "downed power line",
                "notes": (
                    "Burned 10 miles north of Pecos in Santa Fe NF (not directly at Tres Piedras "
                    "but in the same Sangre de Cristo forest system). Started May 30, 2013, growing "
                    "to 10,219 acres. Evacuated 134 summer homes and 6-10 residences along NM-63. "
                    "No structures burned. Demonstrated fire potential in northern NM forests."
                ),
            },
            {
                "name": "Tusas Fire",
                "year": 2025,
                "acres": 3,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "under investigation",
                "notes": (
                    "Small fire near Las Tablas community southwest of Tres Piedras on Carson NF "
                    "in August 2025. Quickly suppressed at approximately 2.5 acres. Demonstrated "
                    "ongoing ignition risk in area."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "US-64 East",
                "direction": "east toward Taos (30 miles)",
                "lanes": 2,
                "bottleneck": "Open plateau road; passes through forested foothills near Taos",
                "risk": "Best evacuation route; open terrain for most of distance reduces fire "
                        "risk; but Taos itself may be congested during regional fire event",
            },
            {
                "route": "US-64 West",
                "direction": "west toward Chama and Tierra Amarilla (45 miles)",
                "lanes": 2,
                "bottleneck": "Open plateau transitioning to forested mountains near Chama; "
                              "limited services",
                "risk": "Good alternate route; mostly open terrain; but long distance to services",
            },
            {
                "route": "US-285 South",
                "direction": "south toward Ojo Caliente and Espanola (50 miles)",
                "lanes": 2,
                "bottleneck": "Open plateau road; passes through small communities",
                "risk": "Viable route toward larger population centers; mostly open terrain",
            },
            {
                "route": "US-285 North",
                "direction": "north toward Antonito CO (40 miles)",
                "lanes": 2,
                "bottleneck": "Open plateau; crosses state line into Colorado",
                "risk": "Good route away from fire; open terrain; but crosses into different "
                        "state jurisdiction for emergency services",
            },
        ],
        "fire_spread_characteristics": (
            "Dual fire regime: plateau grassland and sagebrush carries rapid surface fire (3-7 mph) "
            "during spring wind events when grass is cured and winds exceed 30 mph; forested mountain "
            "slopes to the east produce crown fire in dense ponderosa and mixed conifer. Transition "
            "zone between these regimes creates complex fire behavior where grass fire can push into "
            "timber interface. Wind patterns on the plateau are consistent and strong, particularly "
            "during spring (March-June) when southwest to west winds regularly exceed 40 mph."
        ),
        "infrastructure_vulnerabilities": (
            "Water from wells; vulnerable to drought but not directly to fire contamination in most "
            "scenarios. No hospital; nearest in Taos (30 miles). Electric co-op power lines through "
            "forest are ignition risk (Tres Lagunas started from downed line). Propane heating "
            "universal. Limited cell service outside highway corridors. Highway crossroads is both "
            "asset (evacuation) and liability (through-traffic, accident potential)."
        ),
        "demographics_risk_factors": (
            "Approximately 1,000 people in surrounding area. Low-income rural community with "
            "significant Hispanic population. Many elderly residents on fixed incomes. Scattered "
            "homes and cabins in forest settings with unpaved access roads. Limited emergency "
            "services. Strong ranching and artistic community. Summer and seasonal residents "
            "in forest cabins are particularly vulnerable."
        ),
    },

    # =========================================================================
    # 14. PECOS / TERRERO
    # =========================================================================
    "pecos_nm": {
        "center": (35.574, -105.674),
        "terrain_notes": (
            "Pecos sits at 7,041 ft in the Pecos River valley on the western slope of the southern "
            "Sangre de Cristo Mountains, serving as the gateway to the Pecos Wilderness. The village "
            "is built along the Pecos River which flows south from the mountains through increasingly "
            "narrow, forested canyon. NM-63 follows the river north from the village through Pecos "
            "Canyon toward the Terrero area and the wilderness trailheads. Terrero, the former "
            "mining community 13 miles up-canyon, is accessible only by this single road and is one "
            "of the most fire-exposed communities in New Mexico. The Pecos Canyon walls rise steeply "
            "1,500-3,000 ft above the river, covered in dense ponderosa pine, Douglas fir, white fir, "
            "and blue spruce. The canyon acts as a natural fire chimney: afternoon upslope winds drive "
            "fire from the valley toward the wilderness, while synoptic southwest winds can push fire "
            "down-canyon toward Pecos village. The Pecos area has experienced repeated wildfire "
            "trauma: the Viveash Fire (2000, 25,283 acres) burned 5 miles northwest of the village "
            "and forced evacuation of hundreds, the Tres Lagunas Fire (2013, 10,219 acres) burned "
            "10 miles north along NM-63 evacuating 140+ structures, and most devastatingly, the 2022 "
            "Hermits Peak/Calf Canyon Fire burned directly through the forests surrounding Pecos, "
            "with backburning operations conducted east of Terrero. The Hermits Peak fire originated "
            "from a USFS prescribed burn at the base of Hermit Peak, approximately 12 miles northwest "
            "of Las Vegas NM but only 15 miles from Pecos, and the fire's 341,471-acre footprint "
            "encompassed much of the forest north and east of the village. The Pecos River watershed "
            "above the village was heavily impacted, creating ongoing post-fire flooding and debris "
            "flow hazards. The village's position at the mouth of the canyon makes it a convergence "
            "point for fire, smoke, and flood debris from the entire upper watershed. Pecos National "
            "Historical Park, preserving a major Pueblo ruin and Civil War battlefield, lies just "
            "south of the village."
        ),
        "key_features": [
            {"name": "Pecos Wilderness", "bearing": "N", "distance_mi": 10,
             "type": "wilderness", "notes": "223,667 acres of rugged mountain terrain; peaks to "
             "13,103 ft (Truchas Peak); dense spruce-fir and mixed conifer; headwaters of Pecos River"},
            {"name": "Hermit Peak", "bearing": "NE", "distance_mi": 15,
             "type": "mountain", "notes": "10,212 ft; origin area of 2022 Hermits Peak Fire; "
             "dense forest on all flanks; USFS prescribed burn site"},
            {"name": "Terrero", "bearing": "N", "distance_mi": 13,
             "type": "community", "notes": "Former mining town up-canyon; extremely fire-exposed; "
             "single road (NM-63) access; backburning conducted here during 2022 fire"},
            {"name": "Pecos River Canyon", "bearing": "N", "distance_mi": 3,
             "type": "canyon", "notes": "Deep forested canyon carrying Pecos River and NM-63; "
             "fire chimney effect; sole access to Terrero and wilderness trailheads"},
            {"name": "Pecos National Historical Park", "bearing": "S", "distance_mi": 2,
             "type": "monument", "notes": "Major pueblo ruin and Glorieta Pass Civil War "
             "battlefield; cultural resource at fire risk; pinon-juniper fuel setting"},
        ],
        "elevation_range_ft": (6800, 13103),
        "wui_exposure": (
            "high -- village of ~1,400 at canyon mouth with forest on three sides; Terrero and "
            "canyon communities with single-road access deep in forest; 2022 fire burned surrounding "
            "forests extensively; Tres Lagunas Fire evacuated 140+ structures along NM-63"
        ),
        "historical_fires": [
            {
                "name": "Viveash Fire",
                "year": 2000,
                "acres": 25283,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "human",
                "notes": (
                    "Burned 25,283 acres in Santa Fe NF five miles northwest of Pecos. Fire "
                    "tripled in size in 24 hours. Forced evacuation of hundreds from Pecos "
                    "Canyon. 1,004 firefighters deployed. Impacted Gallinas watershed 22 miles "
                    "downstream. Part of catastrophic 2000 fire season that also included "
                    "Cerro Grande."
                ),
            },
            {
                "name": "Tres Lagunas Fire",
                "year": 2013,
                "acres": 10219,
                "structures_destroyed": 0,
                "fatalities": 0,
                "cause": "downed power line",
                "notes": (
                    "Burned 10,219 acres 10 miles north of Pecos starting May 30, 2013. Caused "
                    "by downed power line. Evacuated 134 summer homes and 6-10 primary residences "
                    "along NM-63 from El Macho church north to Jacks Creek Campground. No "
                    "structures burned. 90% contained by late June. Post-fire flooding and "
                    "debris flows impacted Pecos River water quality."
                ),
            },
            {
                "name": "Hermits Peak / Calf Canyon Fire",
                "year": 2022,
                "acres": 341471,
                "structures_destroyed": 903,
                "fatalities": 0,
                "cause": "escaped prescribed burn (USFS)",
                "notes": (
                    "The 341,471-acre fire burned extensively through forests surrounding Pecos. "
                    "Backburning operations conducted east of Terrero along Lone Pine Mesa and "
                    "Blue Bell Ridge into the Pecos Wilderness. Fire originated from USFS "
                    "prescribed burn near Hermit Peak, 15 miles from Pecos. Pecos River "
                    "watershed heavily impacted with ongoing post-fire flooding and debris flow "
                    "hazards. While Pecos village was not destroyed, surrounding forest was "
                    "extensively burned, fundamentally altering the landscape."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "NM-63 South to I-25",
                "direction": "south from Pecos to I-25 at Glorieta/Rowe (8 miles)",
                "lanes": 2,
                "bottleneck": "Narrow two-lane road through Pecos valley; intersects NM-50; "
                              "old town section narrows further",
                "risk": "Primary evacuation route; short distance to I-25 is advantage; but "
                        "absorbs all traffic from Terrero and canyon communities above",
            },
            {
                "route": "NM-50 West",
                "direction": "west toward Santa Fe via Glorieta Pass",
                "lanes": 2,
                "bottleneck": "Mountain road over Glorieta Pass; connects to I-25 at multiple points",
                "risk": "Alternate route to Santa Fe; forested terrain but connects to interstate "
                        "relatively quickly",
            },
            {
                "route": "NM-63 North (Pecos Canyon)",
                "direction": "north toward Terrero, Cowles, and wilderness trailheads",
                "lanes": 2,
                "bottleneck": "Narrow dead-end canyon road; no through route; narrows to one lane "
                              "in places; single bridge crossings",
                "risk": "NOT an evacuation route -- dead end; Terrero and canyon residents must "
                        "evacuate DOWN canyon on single road; can be cut by fire from either wall; "
                        "140+ structures require evacuation through single canyon corridor",
            },
        ],
        "fire_spread_characteristics": (
            "Canyon-chimney fire behavior in Pecos Canyon is the primary threat. Southwest winds "
            "push fire down-canyon toward Pecos village, while afternoon upslope winds drive fire "
            "up-canyon toward Terrero. Crown fire in dense mixed conifer on canyon walls produces "
            "extreme flame lengths and cross-canyon spotting. The 2000 Viveash Fire demonstrated "
            "rates of spread tripling fire size in 24 hours. Fire can approach from multiple "
            "directions: north from wilderness, west from Santa Fe NF, east from Hermit Peak area. "
            "Post-fire debris flows from burned slopes above are catastrophic secondary hazard."
        ),
        "infrastructure_vulnerabilities": (
            "Water from Pecos River and mountain wells; heavily impacted by post-2022 fire debris "
            "and ash flows. NM-63 is sole access to upper canyon and dead-ends at wilderness; "
            "single bridge crossings are vulnerable to flood damage. No hospital; nearest is in "
            "Santa Fe (25 miles via I-25) or Las Vegas NM (30 miles). Lisboa Springs Trout Hatchery "
            "depends on clean water. Pecos National Historical Park cultural resources at risk. "
            "Limited cell service in upper canyon. Power lines through forest are ignition sources."
        ),
        "demographics_risk_factors": (
            "Pecos village population ~1,400 (2010) with substantial seasonal and weekend population "
            "in upper canyon summer homes and cabins. Significant Hispanic community with deep "
            "multi-generational ties to land. Many residents in upper canyon are seasonal/weekend "
            "with limited fire preparedness. Terrero and Cowles communities are extremely isolated "
            "with single-road access. Post-2022 fire trauma is ongoing; many residents lost access "
            "to traditional forest uses. Land grant communities in area have complex property "
            "rights and cultural connections to forest that complicate evacuation decisions."
        ),
    },
}
