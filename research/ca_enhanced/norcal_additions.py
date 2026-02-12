"""
Northern California Fire-Vulnerable City Additions
===================================================

Research-quality profiles for 12 additional NorCal fire-vulnerable communities
grouped into four geographic clusters:

  1. Santa Cruz Mountains / San Lorenzo Valley (CZU Lightning Complex zone)
     - Boulder Creek, Ben Lomond, Felton, Bonny Doon
     - San Lorenzo Valley Communities cluster (Brookdale, Lompico, Zayante)

  2. Far Northern California (Siskiyou / Trinity Counties)
     - Weed, Dunsmuir, Hayfork, Weaverville

  3. Central Sierra (Yosemite / Sequoia gateway communities)
     - Mariposa, Groveland, Three Rivers

These entries supplement the 5 existing profiles in norcal_terrain.py
(Paradise, Magalia, Santa Rosa, Sonoma, Redding).

Sources:
    - CAL FIRE incident reports: CZU Lightning Complex, Boles, Mill, Rim,
      Detwiler, Oak, KNP Complex, Monument, Helena, McFarland, Delta fires
    - NIST & CAL FIRE post-incident damage inspections
    - Santa Cruz County Grand Jury CZU Report (2024)
    - San Lorenzo Valley Water District infrastructure assessments (2020-2024)
    - Siskiyou County Community Wildfire Protection Plan
    - City of Dunsmuir Safety Element Update (Board of Forestry)
    - Trinity County CWPP (Fire Safe Trinity, est. 1998)
    - KLD Associates / First Street Foundation wildfire risk reports
    - USGS / USFS post-fire erosion & debris flow assessments
    - US Census Bureau 2020 Decennial Census, ACS 5-year estimates
    - Lookout Santa Cruz, Mercury News, SF Chronicle investigative reporting
    - NPS KNP Complex incident updates (2021)
    - Tuolumne County / Mariposa County emergency management plans
"""

NORCAL_ADDITIONS = {

    # =========================================================================
    # SANTA CRUZ MOUNTAINS -- CZU Lightning Complex Zone
    # San Lorenzo Valley / Hwy 9 corridor
    # =========================================================================

    "boulder_creek_ca": {
        "center": [37.1269, -122.1211],
        "terrain_notes": (
            "Unincorporated mountain community (pop. ~5,400) in the heart of the "
            "San Lorenzo Valley, Santa Cruz Mountains, at the confluence of Boulder "
            "Creek and the San Lorenzo River. Ground zero of the CZU Lightning "
            "Complex (Aug 16 - Sep 22, 2020; 86,509 acres, 1,490 structures "
            "destroyed, 1 fatality). Community sits in a narrow valley bottom along "
            "Highway 9, hemmed in by steep, heavily forested ridges on both sides -- "
            "second-growth redwood, Douglas fir, tanoak, and madrone with deep duff "
            "layers (3+ ft reported by CAL FIRE). Terrain is extremely rugged: "
            "slopes of 40-80% on surrounding ridges, deeply incised drainages, "
            "and limited road access. During CZU, fire approached from the NW "
            "(Waddell Creek/Big Basin) and the west (Empire Grade), racing downhill "
            "through chaparral and mixed forest toward Hwy 9 communities. Over "
            "70,000 people were evacuated across the San Lorenzo Valley. "
            "Firefighters fought to keep flames from crossing Hwy 9 at Boulder "
            "Creek for days. San Lorenzo Valley Water District lost ~80% of its "
            "watershed lands and ~50% of its infrastructure in the CZU fire, "
            "including intakes, raw water pipelines, and the Bennett Spring "
            "treatment facility, which was completely destroyed. Post-fire debris "
            "flow risk is severe: burned hillsides produced mudslides at 30 mph "
            "in subsequent winter storms. The community is the most populated "
            "center in the upper San Lorenzo Valley and the de facto hub for "
            "surrounding hamlets (Brookdale, Ben Lomond, Bonny Doon)."
        ),
        "key_features": [
            "San Lorenzo River confluence -- valley bottom at 480 ft",
            "Surrounded by 1,500-2,500 ft ridges with 40-80% slopes",
            "Second-growth redwood/Douglas fir forest with 3+ ft duff layers",
            "CZU Lightning Complex ground zero (2020, 86,509 acres)",
            "Hwy 9 sole arterial -- single point of failure for 20,000+ residents",
            "SLVWD water system 50% destroyed in CZU fire",
            "Big Basin Redwoods State Park 3 mi NW (97% burned in CZU)",
            "Post-fire debris flow corridors on all surrounding drainages",
        ],
        "elevation_range_ft": [480, 2500],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "CZU Lightning Complex",
                "year": 2020,
                "acres": 86509,
                "details": (
                    "Lightning-caused complex ignited Aug 16, 2020. Destroyed 1,490 "
                    "structures, killed 1. 70,000+ evacuated. Cost $68M+ to suppress. "
                    "Burned 97% of Big Basin Redwoods State Park. Boulder Creek was "
                    "the primary stand-or-lose community; firefighters held Hwy 9 "
                    "corridor for days to prevent fire from entering town center."
                ),
            },
            {
                "name": "Pine Mountain Fire",
                "year": 1948,
                "acres": 2000,
                "details": "Historic fire in Santa Cruz Mountains near Boulder Creek area.",
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 9 south",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Single arterial for entire San Lorenzo Valley (~20,000 "
                    "residents). Narrows through Ben Lomond and Felton. Merges with "
                    "Hwy 17/Hwy 1 traffic in Santa Cruz. During CZU, gridlock "
                    "extended for miles. Many canyons have NO roads heading north -- "
                    "south is the only way out."
                ),
                "risk": (
                    "Catastrophic single-point-of-failure. Fire crossing Hwy 9 "
                    "anywhere cuts off all upstream communities. Road passes through "
                    "dense forest canopy creating ember tunnel conditions."
                ),
            },
            {
                "route": "Highway 9 north to Hwy 35 (Skyline Blvd)",
                "direction": "N",
                "lanes": 2,
                "bottleneck": (
                    "Steep, winding mountain road climbing 1,500+ ft to ridgeline. "
                    "Single lane in places with no shoulders. Not viable for mass "
                    "evacuation. Often closed by fire, slides, or trees."
                ),
                "risk": (
                    "Road runs through dense forest for entire length. Fire on "
                    "either side makes passage lethal. Frequently blocked by "
                    "downed trees during wind events."
                ),
            },
            {
                "route": "Bear Creek Road to Los Gatos",
                "direction": "E",
                "lanes": 2,
                "bottleneck": (
                    "Narrow, winding mountain road over the summit to Santa Clara "
                    "Valley. 30+ minute drive under normal conditions. Steep grades "
                    "and tight switchbacks limit speed and capacity."
                ),
                "risk": (
                    "Exposed to fire on both flanks. Road can be cut by fallen "
                    "trees or landslides. Not a realistic mass evacuation route."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Onshore NW-W marine flow dominates most of year, but dry offshore "
                "NE events (weak Diablo-type) create critical fire weather. CZU "
                "was driven by erratic wind shifts from lightning-storm outflow "
                "boundaries. Topographic channeling through Santa Cruz Mountains "
                "drainages accelerates fire spread regardless of synoptic flow."
            ),
            "critical_corridors": [
                "Waddell Creek drainage (NW approach -- CZU primary path)",
                "Empire Grade ridge (W approach -- fire ran downhill into valley)",
                "San Lorenzo River canyon (N-S axis, fire chimney effect)",
                "Boulder Creek canyon (W approach directly into town center)",
            ],
            "rate_of_spread_potential": (
                "Moderate to extreme depending on terrain alignment. CZU spread "
                "rates of 0.5-1.5 mph through heavy timber, with faster runs "
                "through chaparral on ridge tops. Terrain-driven upslope runs "
                "in steep canyons can produce extreme rates (2+ mph). Deep duff "
                "creates sustained smoldering that can reignite weeks later."
            ),
            "spotting_distance": (
                "0.5-1.0 mi typical in redwood/Douglas fir. Bark strips and "
                "debris lofted by convection column. Shorter range than grass/chaparral "
                "but persistent -- embers lodge in duff and smolder before flaming."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "San Lorenzo Valley Water District: catastrophically damaged in CZU. "
                "Lost ~80% of watershed lands, ~50% of infrastructure. Bennett Spring "
                "Overflow, settling tanks, and related piping completely destroyed. "
                "5-mile raw water pipeline damaged (uninsurable). District implementing "
                "$170K Cal Fire grant for defensible space around 37 infrastructure "
                "sites. Chronic low fire-flow capacity; hydrant coverage gaps."
            ),
            "power": (
                "PG&E distribution through dense forest canopy. Frequent outages "
                "from tree falls. Subject to Public Safety Power Shutoffs (PSPS) "
                "during fire weather. Limited backup generation. Many residents "
                "on propane with tanks in vegetation."
            ),
            "communications": (
                "Limited cell coverage in canyon bottoms. AT&T and Verizon towers "
                "on ridges vulnerable to fire. Landlines serve as backup but "
                "copper infrastructure aging. County reverse-911 system (CodeRED) "
                "failed to reach many residents during CZU due to outdated contact "
                "records and cell dead zones."
            ),
            "medical": (
                "No hospital in San Lorenzo Valley. Nearest ER: Dominican Hospital "
                "in Santa Cruz (15+ mi, 25+ min via Hwy 9). Seton Medical Center "
                "closed 2020. During evacuation, ambulance access severely "
                "constrained by Hwy 9 gridlock. One volunteer fire station in "
                "Boulder Creek."
            ),
        },
        "demographics_risk_factors": {
            "population": 5429,
            "seasonal_variation": (
                "Moderate. Summer tourism to Big Basin (pre-CZU), hiking, and "
                "river recreation. Some seasonal rentals and vacation homes. "
                "Post-CZU reconstruction workers add daytime population."
            ),
            "elderly_percentage": "est. 18-22%",
            "mobile_homes": (
                "Several small mobile home parks in valley bottom areas. "
                "Vulnerable to both fire and post-fire debris flows."
            ),
            "special_needs_facilities": (
                "No major care facilities. Elderly and disabled residents "
                "dispersed throughout community with limited transportation "
                "options. Mountain terrain precludes wheelchair-accessible "
                "evacuation routes."
            ),
        },
    },

    "ben_lomond_ca": {
        "center": [37.0891, -122.0864],
        "terrain_notes": (
            "Unincorporated community (pop. ~6,300) in the San Lorenzo Valley, "
            "4 miles downstream (south) of Boulder Creek on Highway 9. Situated "
            "in a slightly wider section of the San Lorenzo River valley but still "
            "flanked by steep, forested ridges on both sides. Mixed redwood/Douglas "
            "fir forest with dense understory. CZU Lightning Complex (2020) "
            "threatened the community directly; fire crested above town from the "
            "west and moved down toward Hwy 9. CAL FIRE described the terrain as "
            "'the real deal when it comes to inaccessible -- trails, skid roads, "
            "very difficult terrain with 3-foot duff and big timber overlay.' "
            "Volunteer fire department played a heroic role holding fire at Alba "
            "Road for days to prevent entry into Ben Lomond's center. The 125-year-"
            "old one-room Alba Schoolhouse was destroyed. Ben Lomond sits at a "
            "critical midpoint on Hwy 9: evacuation traffic from Boulder Creek, "
            "Brookdale, and points north must pass through town, compounding "
            "congestion. Ben Lomond Mountain (2,660 ft) rises to the west, "
            "creating a significant terrain barrier with dense forest cover."
        ),
        "key_features": [
            "San Lorenzo River valley, midpoint between Boulder Creek and Felton",
            "Ben Lomond Mountain (2,660 ft) to the west -- dense forest barrier",
            "CZU Lightning Complex evacuation zone (2020)",
            "Alba Road fire corridor -- fire held at this line for days",
            "Hwy 9 traffic funnel for all upstream communities",
            "Volunteer fire department (critical local defense)",
            "Deep duff layers (3+ ft) with big timber overlay",
            "Extremely inaccessible terrain on surrounding ridges",
        ],
        "elevation_range_ft": [350, 2660],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "CZU Lightning Complex",
                "year": 2020,
                "acres": 86509,
                "details": (
                    "Fire crested ridges above Ben Lomond from west/northwest. "
                    "Firefighters held fire line at Alba Road for days. Alba "
                    "Schoolhouse (125 years old) destroyed. Entire community "
                    "under mandatory evacuation. CAL FIRE described terrain as "
                    "'the real deal when it comes to inaccessible.'"
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 9 south to Felton/Santa Cruz",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Sole arterial. All Boulder Creek / Brookdale traffic funnels "
                    "through Ben Lomond, adding to local evacuation demand. Road "
                    "narrows through town center with on-street parking reducing "
                    "effective width."
                ),
                "risk": (
                    "Same single-point-of-failure as entire SLV corridor. Fire "
                    "approaching from west can cut Hwy 9 at Ben Lomond, trapping "
                    "all upstream residents."
                ),
            },
            {
                "route": "Alba Road / Empire Grade",
                "direction": "W",
                "lanes": 1,
                "bottleneck": (
                    "Narrow mountain road climbing steeply to ridgeline. Single "
                    "lane in most sections. Very limited capacity."
                ),
                "risk": (
                    "CZU fire burned along this exact corridor. Road passes "
                    "through dense forest. Not a viable evacuation route during "
                    "fire approaching from the west."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Marine-influenced most of year. Offshore NE events create "
                "fire weather. CZU driven by erratic winds from storm outflow. "
                "Terrain channeling in valley amplifies wind speed regardless "
                "of synoptic direction."
            ),
            "critical_corridors": [
                "Alba Road drainage (W approach -- CZU primary threat axis)",
                "San Lorenzo River valley (N-S fire chimney)",
                "Ben Lomond Mountain west slopes (steep upslope fire runs)",
            ],
            "rate_of_spread_potential": (
                "Moderate in heavy timber; faster on chaparral-covered upper "
                "slopes. Terrain-driven upslope runs on Ben Lomond Mountain's "
                "east face would push fire directly toward town."
            ),
            "spotting_distance": (
                "0.5-1.0 mi in redwood/Douglas fir terrain. Deep duff "
                "creates persistent smoldering ignitions."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Served by San Lorenzo Valley Water District. Same system "
                "catastrophically damaged in CZU (see Boulder Creek profile). "
                "Fire-flow capacity remains a concern throughout the valley."
            ),
            "power": (
                "PG&E distribution through dense forest. Frequent PSPS events. "
                "Overhead lines vulnerable to tree falls and fire damage."
            ),
            "communications": (
                "Limited cell coverage in valley. Community relies on volunteer "
                "fire department radio network for supplemental communication."
            ),
            "medical": (
                "No hospital. Nearest ER in Santa Cruz (10+ mi via Hwy 9). "
                "Ambulance response times extended by distance and terrain."
            ),
        },
        "demographics_risk_factors": {
            "population": 6337,
            "seasonal_variation": (
                "Modest seasonal increase from recreation visitors. Some "
                "vacation rentals in surrounding forest."
            ),
            "elderly_percentage": "est. 18-20%",
            "mobile_homes": (
                "Small mobile home parks in valley. Particularly vulnerable "
                "to fire and debris flows."
            ),
            "special_needs_facilities": (
                "No major facilities. San Lorenzo Valley Elementary School "
                "serves as community gathering point / potential shelter."
            ),
        },
    },

    "felton_ca": {
        "center": [37.0515, -122.0558],
        "terrain_notes": (
            "Unincorporated community (pop. ~4,500) at the downstream (southern) "
            "end of the San Lorenzo Valley, where Hwy 9 emerges from the mountains "
            "toward Santa Cruz. Sits at the confluence of Zayante Creek, Bean Creek, "
            "and the San Lorenzo River. Felton occupies a slightly wider valley floor "
            "than upstream communities but is still hemmed by forested ridges. Henry "
            "Cowell Redwoods State Park (4,650 acres of old-growth and second-growth "
            "redwood) borders the community to the south and east. The town serves as "
            "the critical evacuation bottleneck for the entire San Lorenzo Valley: "
            "all traffic from Boulder Creek, Ben Lomond, Brookdale, Lompico, and "
            "Zayante funnels through Felton before reaching Hwy 17 or Hwy 1 to "
            "escape. San Lorenzo Valley High School (7105 Hwy 9) is the designated "
            "evacuation shelter. During CZU (2020), Felton was under evacuation "
            "warning as fire approached from the north and west. Firefighters "
            "protected the community by holding lines along the Hwy 9 corridor. "
            "Post-CZU debris flow risk affected the town significantly -- burned "
            "hillsides above the valley channeled mudflows toward the valley floor."
        ),
        "key_features": [
            "Southern gateway to San Lorenzo Valley -- critical traffic funnel",
            "Confluence of San Lorenzo River, Zayante Creek, and Bean Creek",
            "Henry Cowell Redwoods State Park borders town (4,650 acres)",
            "SLV High School designated evacuation shelter",
            "Felton Fire Protection District (volunteer)",
            "Hwy 9 / Mt. Hermon Rd intersection -- primary bottleneck point",
            "Graham Hill Road alternate route to Santa Cruz",
            "Roaring Camp Railroad historic narrow-gauge in redwood forest",
        ],
        "elevation_range_ft": [250, 1800],
        "wui_exposure": "high",
        "historical_fires": [
            {
                "name": "CZU Lightning Complex",
                "year": 2020,
                "acres": 86509,
                "details": (
                    "Felton placed under evacuation warning. Fire reached Hwy 9 "
                    "corridor north of town. Firefighters held line to prevent "
                    "fire from entering Felton. SLV High School served as "
                    "evacuation shelter. Community was spared direct structure "
                    "loss but experienced severe smoke exposure and subsequent "
                    "debris flow risk."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 9 south to Santa Cruz / Hwy 1",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Carries ALL San Lorenzo Valley evacuation traffic (~20,000 "
                    "residents). Narrows through Felton town center. Intersections "
                    "at Mt. Hermon Rd and Graham Hill Rd create severe congestion "
                    "points. Merges with Hwy 17 traffic near Santa Cruz."
                ),
                "risk": (
                    "Ultimate bottleneck for entire valley. If Hwy 9 is cut at "
                    "Felton, no upstream community can evacuate south."
                ),
            },
            {
                "route": "Graham Hill Road to Santa Cruz",
                "direction": "SE",
                "lanes": 2,
                "bottleneck": (
                    "Alternate route to Santa Cruz bypassing lower Hwy 9. "
                    "Winding road through Henry Cowell Redwoods. Limited capacity."
                ),
                "risk": (
                    "Passes through dense old-growth redwood forest. Fire in "
                    "Henry Cowell would close this route."
                ),
            },
            {
                "route": "Mount Hermon Road to Scotts Valley / Hwy 17",
                "direction": "E",
                "lanes": 2,
                "bottleneck": (
                    "Connects to Hwy 17 freeway via Scotts Valley. Moderate "
                    "capacity but also serves Scotts Valley evacuation traffic."
                ),
                "risk": (
                    "Best alternate route for valley residents. Less fire-exposed "
                    "than Hwy 9 south. But Hwy 17 itself can be gridlocked."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Marine-influenced. Offshore NE events create fire weather. "
                "Valley confluence creates complex wind patterns where Zayante "
                "Creek, Bean Creek, and San Lorenzo River valleys meet."
            ),
            "critical_corridors": [
                "San Lorenzo River valley (N approach from Boulder Creek/Ben Lomond)",
                "Zayante Creek canyon (NE approach from Lompico/Zayante area)",
                "Henry Cowell Redwoods (S/SE -- fire in park threatens town)",
            ],
            "rate_of_spread_potential": (
                "Moderate. Lower elevation and valley-bottom position reduce "
                "some terrain-driven fire behavior. Old-growth redwood in Henry "
                "Cowell is fire-resistant but understory can carry fire."
            ),
            "spotting_distance": (
                "0.5 mi typical. Redwood bark strips are effective firebrands "
                "when lofted. Valley position may receive spot fires from "
                "ridge-top fires above."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "SLVWD service area. Same system-wide vulnerabilities as "
                "Boulder Creek / Ben Lomond. District is hardening 37 sites."
            ),
            "power": (
                "PG&E distribution. PSPS events affect community. Some "
                "undergrounding in town center but overhead lines predominate."
            ),
            "communications": (
                "Better cell coverage than upper valley due to proximity to "
                "Scotts Valley towers. Felton Fire PD has radio network."
            ),
            "medical": (
                "No hospital. Nearest ER: Dominican Hospital in Santa Cruz "
                "(7 mi, 15 min via Hwy 9). Quicker access than upstream towns."
            ),
        },
        "demographics_risk_factors": {
            "population": 4489,
            "seasonal_variation": (
                "Moderate tourist traffic to Henry Cowell Redwoods and Roaring "
                "Camp Railroad, especially summer weekends. Adds to Hwy 9 "
                "congestion during potential evacuation periods."
            ),
            "elderly_percentage": "est. 16-19%",
            "mobile_homes": "Small parks present in valley floor areas.",
            "special_needs_facilities": (
                "SLV High School serves as community evacuation center. "
                "No dedicated special-needs facilities."
            ),
        },
    },

    "bonny_doon_ca": {
        "center": [37.0416, -122.1505],
        "terrain_notes": (
            "Remote, unincorporated ridge-top community (pop. ~2,700) in the "
            "Santa Cruz Mountains, perched on a broad ridge at ~1,500 ft elevation "
            "between the San Lorenzo Valley to the east and the Pacific coast to "
            "the west. Accessed primarily via Bonny Doon Road (from Hwy 1), Pine "
            "Flat Road, and Empire Grade -- all narrow, winding mountain roads. "
            "CZU Lightning Complex (2020) devastated Bonny Doon: over 100 homes "
            "destroyed, with the community suffering some of the highest per-capita "
            "losses. No CAL FIRE presence reached Bonny Doon for 2.5 days after "
            "ignition; amateur resident brigades formed to fight fire themselves. "
            "The community is surrounded by second-growth redwood, Douglas fir, "
            "and mixed hardwoods with heavy fuel loading. Bonny Doon Fire Safe "
            "Council applied for evacuation route fuel break grants along Pine "
            "Flat and Bonny Doon Roads. Empire Grade Road runs along the ridgeline "
            "and was a primary fire corridor during CZU. The community's isolation "
            "and minimal road network make it one of the most vulnerable WUI "
            "communities in the San Francisco Bay Area region."
        ),
        "key_features": [
            "Ridge-top community at ~1,500 ft in Santa Cruz Mountains",
            "CZU Lightning Complex devastation -- 100+ homes destroyed",
            "No CAL FIRE response for 2.5 days; resident brigades fought fire",
            "Empire Grade Road primary fire corridor",
            "Minimal road network -- Pine Flat Rd, Bonny Doon Rd, Ice Cream Grade",
            "Bonny Doon Fire Safe Council (active fuel break program)",
            "Bonny Doon Ecological Reserve (CA DFW) to north",
            "Extremely rural -- large parcels, dispersed development, no town center",
        ],
        "elevation_range_ft": [800, 2200],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "CZU Lightning Complex",
                "year": 2020,
                "acres": 86509,
                "details": (
                    "Bonny Doon suffered some of the worst per-capita losses. "
                    "100+ homes destroyed along Empire Grade, Pine Flat Road, "
                    "and surrounding areas. No professional fire suppression for "
                    "first 2.5 days. Resident brigades formed to defend properties. "
                    "Some families moved away permanently; others rebuilt. Bonny "
                    "Doon Elementary lost students from displacement."
                ),
            },
            {
                "name": "Martin Fire",
                "year": 2008,
                "acres": 250,
                "details": (
                    "Smaller fire near Bonny Doon that prompted evacuations "
                    "and highlighted limited road egress."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Bonny Doon Road to Hwy 1 (coast)",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "Narrow, winding mountain road descending 1,500 ft to coast. "
                    "Single lane in sections. No shoulders. 15-20 min to Hwy 1 "
                    "under normal conditions."
                ),
                "risk": (
                    "Road passes through dense forest. Fire approaching from "
                    "any direction can cut this route. Steep grades limit speed "
                    "for large vehicles and trailers."
                ),
            },
            {
                "route": "Pine Flat Road to Hwy 9 / Felton",
                "direction": "E",
                "lanes": 1,
                "bottleneck": (
                    "Very narrow mountain road, effectively single lane with "
                    "turnouts. Steep grades and blind curves. Connects to Hwy 9 "
                    "system (which has its own capacity problems)."
                ),
                "risk": (
                    "CZU fire burned directly along Pine Flat Road. Fire Safe "
                    "Council seeking grants for 10-ft fuel breaks along this "
                    "escape route. Road closed during CZU."
                ),
            },
            {
                "route": "Empire Grade north to Hwy 236 / Big Basin",
                "direction": "N",
                "lanes": 1,
                "bottleneck": (
                    "Ridge-top road, single lane, extremely winding. Connects "
                    "to Hwy 236 (Big Basin Way) which is itself a dead-end "
                    "mountain road."
                ),
                "risk": (
                    "Empire Grade was the primary fire corridor during CZU. "
                    "This route leads TOWARD the fire origin area. Not viable "
                    "during NW-approaching fires."
                ),
            },
            {
                "route": "Ice Cream Grade to Hwy 9",
                "direction": "SE",
                "lanes": 1,
                "bottleneck": (
                    "Narrow single-lane road connecting to Pine Flat Road and "
                    "ultimately Hwy 9. Minimal capacity."
                ),
                "risk": (
                    "Was under evacuation order and road closure during CZU. "
                    "Passes through dense forest."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Ridge-top position exposed to both marine westerly flow and "
                "offshore NE events. CZU was driven by erratic lightning-storm "
                "outflow. Strong afternoon thermals push fire upslope from "
                "coastal canyons. Fog influence is weaker at 1,500 ft than "
                "at coast, so fuels dry faster on the ridge."
            ),
            "critical_corridors": [
                "Empire Grade ridge (N-S -- primary CZU fire corridor)",
                "Waddell Creek drainage (NW approach from coast)",
                "Laguna Creek drainage (W approach)",
                "Pine Flat Road corridor (E approach from San Lorenzo Valley)",
            ],
            "rate_of_spread_potential": (
                "Extreme during offshore events. Ridge-top position means fire "
                "approaching from any direction encounters steep upslope terrain. "
                "Chaparral and mixed brush on ridge flanks carry fire rapidly. "
                "Deep duff in redwood/Douglas fir sustains long-duration burning."
            ),
            "spotting_distance": (
                "1.0-1.5 mi on ridge top due to convective lofting from steep "
                "slopes. Embers carried by ridge-top winds can ignite structures "
                "well ahead of fire front."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Many properties on private wells and springs -- no municipal "
                "water system. Some areas served by small mutual water companies. "
                "Fire suppression water essentially nonexistent: no hydrants, "
                "no pressurized system. Residents rely on water tanks (if any) "
                "and CAL FIRE water tenders."
            ),
            "power": (
                "PG&E overhead distribution through forest. Extremely vulnerable "
                "to fire damage and tree falls. PSPS events leave community "
                "without power for days. Many residents have generators but "
                "fuel resupply is difficult during evacuations."
            ),
            "communications": (
                "Very limited cell coverage. Many dead zones. Landlines serve "
                "as primary communication but copper infrastructure aging. "
                "During CZU, residents were cut off from emergency communications "
                "for extended periods, contributing to self-organized fire response."
            ),
            "medical": (
                "No medical facilities. Nearest hospital: Dominican, Santa Cruz "
                "(20+ mi, 35+ min). Ambulance response times can exceed 30 min. "
                "Isolated residents with medical needs are extremely vulnerable "
                "during evacuation."
            ),
        },
        "demographics_risk_factors": {
            "population": 2678,
            "seasonal_variation": (
                "Minimal. Primarily year-round residents on large rural parcels. "
                "Some weekend/vacation properties."
            ),
            "elderly_percentage": "est. 20-24%",
            "mobile_homes": (
                "Scattered throughout community. No concentrated parks. "
                "Individual units on rural parcels."
            ),
            "special_needs_facilities": (
                "Bonny Doon Elementary School is the only public facility. "
                "No care homes or special-needs services. Deeply rural "
                "community with self-reliant culture but limited institutional "
                "support for vulnerable populations."
            ),
        },
    },

    # =========================================================================
    # SAN LORENZO VALLEY COMMUNITIES -- Cluster entry
    # (Brookdale, Lompico, Zayante)
    # =========================================================================

    "san_lorenzo_valley_communities": {
        "center": [37.1055, -122.0750],
        "terrain_notes": (
            "Cluster entry covering three smaller communities in the San Lorenzo "
            "Valley fire corridor that share the same CZU Lightning Complex impact "
            "zone, same Hwy 9 bottleneck, and same SLVWD water system vulnerabilities. "
            "\n\n"
            "BROOKDALE (pop. ~2,000, elev. 405 ft): Located on Hwy 9 between Ben "
            "Lomond and Boulder Creek. CZU fire reached Hwy 9 at Brookdale, and "
            "Boulder Creek Fire Department worked to prevent it from crossing the "
            "road. Historic Brookdale Lodge was threatened. Steep, narrow canyon "
            "section of the San Lorenzo River with minimal buildable flat land. "
            "Entirely dependent on Hwy 9 for evacuation. "
            "\n\n"
            "LOMPICO (pop. ~1,150, elev. 968 ft): Census-designated place in a "
            "steep box canyon east of Felton, accessed by Lompico Road -- a single "
            "narrow road that dead-ends in the canyon. CZU fire came within 3 mi "
            "of Lompico. A century of dried vegetation has built up in the steep "
            "box canyon, leaving it extremely vulnerable. Lookout Santa Cruz reported "
            "Lompico has 'one way out' and questioned whether its narrow escape from "
            "CZU left it more vulnerable to the next fire. Lompico Road connects to "
            "Zayante Road, which connects to Hwy 9 -- three serial bottlenecks. "
            "\n\n"
            "ZAYANTE (pop. ~200, elev. ~700 ft): Tiny community on Zayante Road "
            "between Lompico and Felton. Same box canyon geography as Lompico. "
            "Zayante Fire has active community support program. Forested canyon "
            "with single-road access to Hwy 9."
        ),
        "key_features": [
            "Three small SLV communities sharing CZU impact zone",
            "Brookdale: Hwy 9 canyon narrows, CZU fire reached road here",
            "Lompico: dead-end box canyon, 'one way out' via Lompico Road",
            "Zayante: tiny canyon community, single road to Hwy 9",
            "All three funnel through Hwy 9 at Felton bottleneck",
            "SLVWD water system serves all three (damaged in CZU)",
            "Century of fuel buildup in canyons -- extreme fire load",
            "Serial bottleneck evacuation: side road -> Hwy 9 -> Felton -> out",
        ],
        "elevation_range_ft": [350, 1200],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "CZU Lightning Complex",
                "year": 2020,
                "acres": 86509,
                "details": (
                    "Fire reached Hwy 9 at Brookdale. Lompico and Zayante "
                    "narrowly escaped -- CZU came within 3 mi. All communities "
                    "evacuated. Near-miss has not reduced the risk; a century "
                    "of fuel buildup remains in surrounding canyons."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 9 (sole arterial for all three communities)",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "All three communities must reach Hwy 9 via narrow side "
                    "roads, then join 20,000+ residents funneling south through "
                    "Felton. Serial bottleneck: Lompico Rd -> Zayante Rd -> "
                    "Hwy 9 -> Felton -> out. Each connection is a potential "
                    "failure point."
                ),
                "risk": (
                    "Lompico has a single road in and out of a box canyon. "
                    "If Lompico Rd is cut by fire, the community is trapped. "
                    "Brookdale's section of Hwy 9 runs through a narrow canyon "
                    "where fire can burn across the road."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Canyon/valley channeling dominates local fire weather. Offshore "
                "NE events create critical conditions. Marine influence moderates "
                "lower valley but Lompico's box canyon traps heat and creates "
                "its own microclimate."
            ),
            "critical_corridors": [
                "Lompico box canyon (trapped dead-end fire chimney)",
                "Zayante Creek canyon (fire corridor to Hwy 9)",
                "San Lorenzo River canyon at Brookdale (narrow Hwy 9 exposure)",
            ],
            "rate_of_spread_potential": (
                "Extreme in Lompico box canyon -- steep walls, heavy fuel load, "
                "and chimney effect. Fire entering the box canyon from the west "
                "could run to the end in under an hour. Brookdale canyon is "
                "narrower but less steep."
            ),
            "spotting_distance": "0.5-1.0 mi typical in heavy timber terrain.",
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "SLVWD serves all three communities. Same system-wide "
                "vulnerabilities documented under Boulder Creek profile."
            ),
            "power": "PG&E overhead distribution. Frequent PSPS events.",
            "communications": (
                "Poor to nonexistent cell coverage in Lompico box canyon. "
                "Brookdale slightly better due to Hwy 9 corridor."
            ),
            "medical": (
                "No medical facilities in any of the three communities. "
                "Nearest ER: Dominican Hospital, Santa Cruz (12-18 mi "
                "depending on community)."
            ),
        },
        "demographics_risk_factors": {
            "population": 3400,
            "seasonal_variation": "Minimal. Primarily year-round residents.",
            "elderly_percentage": "est. 17-22%",
            "mobile_homes": (
                "Mobile homes present in Lompico canyon and along Zayante "
                "Road. Box canyon location makes these particularly vulnerable."
            ),
            "special_needs_facilities": "None. Deeply rural communities.",
        },
    },

    # =========================================================================
    # FAR NORTHERN CALIFORNIA -- Siskiyou & Trinity Counties
    # =========================================================================

    "weed_ca": {
        "center": [41.4226, -122.3861],
        "terrain_notes": (
            "Small city (pop. ~2,860) at the base of Mt. Shasta (14,179 ft), "
            "the second-highest peak in the Cascade Range. Weed occupies a "
            "sloping bench at ~3,500 ft elevation between the mountain's "
            "southwestern flank and the Shasta Valley to the north. The city "
            "is defined by extreme, persistent wind: founded in 1897 by lumber "
            "baron Abner Weed specifically because the 'furious gusts that "
            "regularly rushed down the Cascade Mountains could blow dry freshly "
            "cut lumber.' Residents report 50-60 mph gusts on 'normal days.' "
            "This same wind regime makes Weed extraordinarily fire-vulnerable. "
            "The Boles Fire (Sep 15, 2014; 479 acres) destroyed 150 homes and "
            "8 commercial structures when wind gusting 40+ mph from the SE "
            "pushed fire through the center of town in under 2 hours -- one of "
            "the most unusual urban wildfires in California history, with the "
            "fire destroying half of downtown including churches, the library, "
            "and the community center. The Mill Fire (Sep 2, 2022; 3,935 acres) "
            "repeated the pattern: ignited at Roseburg Forest Products lumber "
            "mill during a red flag warning, then raced north through the "
            "historically Black community of Lincoln Heights -- one of the "
            "oldest Black communities west of the Mississippi -- destroying ~100 "
            "homes, killing 2, and injuring 3. Lincoln Heights mobile home park "
            "was devastated. Cal Fire determined the cause was mill operations "
            "at the Roseburg property. Wind typically hits Lincoln Heights head-on "
            "from the south. I-5 runs through the east side of town."
        ),
        "key_features": [
            "Base of Mt. Shasta (14,179 ft) -- extreme downslope wind regime",
            "Wind gusts 50-60 mph on normal days (Cascade gap winds)",
            "Boles Fire (2014) destroyed half of downtown in 2 hours",
            "Mill Fire (2022) devastated Lincoln Heights -- 2 killed",
            "Roseburg Forest Products mill -- ignition source for Mill Fire",
            "Lincoln Heights: historic Black community, mobile home park",
            "I-5 corridor runs through east side of town",
            "Lava Fire (2021) burned 26,000+ acres nearby on Mt. Shasta flanks",
        ],
        "elevation_range_ft": [3200, 3800],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Boles Fire",
                "year": 2014,
                "acres": 479,
                "details": (
                    "Arson fire started by homeless man behind Boles Creek "
                    "Apartments. SE wind gusting 40+ mph pushed fire through "
                    "town in <2 hours. 150 homes, 8 commercial structures "
                    "destroyed. Churches, library, community center burned. "
                    "1,500+ evacuated. Sawmill complex partially burned. "
                    "Convicted arsonist: Ronald Beau Marshall."
                ),
            },
            {
                "name": "Mill Fire",
                "year": 2022,
                "acres": 3935,
                "details": (
                    "Ignited at Roseburg Forest Products mill during red flag "
                    "warning (Sep 2, 2022). Rapidly spread north through Lincoln "
                    "Heights neighborhood. 144 structures destroyed/damaged, 2 "
                    "killed, 3 injured. Cal Fire determined cause was mill "
                    "operations. Roseburg pledged $50M community restoration fund. "
                    "Lincoln Heights mobile home park devastated. Predominantly "
                    "wind-driven fire with most damage on day one."
                ),
            },
            {
                "name": "Lava Fire",
                "year": 2021,
                "acres": 26728,
                "details": (
                    "Lightning-caused fire on Mt. Shasta's north flank. Burned "
                    "26,728 acres. Evacuation warnings for Weed. South wind "
                    "could have pushed fire toward town."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Interstate 5 north to Yreka / Oregon",
                "direction": "N",
                "lanes": 4,
                "bottleneck": (
                    "Best evacuation capacity but on-ramps from town are limited. "
                    "I-5 was shut down during Boles Fire. Smoke can reduce "
                    "visibility to near-zero on the freeway."
                ),
                "risk": (
                    "Fire can cut I-5 access from town. Boles Fire forced I-5 "
                    "closure. Wind-driven ember transport can cross the freeway."
                ),
            },
            {
                "route": "Interstate 5 south to Redding",
                "direction": "S",
                "lanes": 4,
                "bottleneck": (
                    "Adequate capacity but leads toward fire-prone terrain. "
                    "Delta Fire (2018) closed I-5 south for 6 days."
                ),
                "risk": (
                    "Southbound evacuation into Sacramento River canyon -- "
                    "itself a high fire risk corridor."
                ),
            },
            {
                "route": "US 97 north to Klamath Falls",
                "direction": "NE",
                "lanes": 2,
                "bottleneck": (
                    "Alternate route east of I-5 toward Oregon. Moderate "
                    "capacity. Passes through open terrain with less fire "
                    "exposure."
                ),
                "risk": (
                    "Less fire-exposed than other routes. Best option for "
                    "NE-directed evacuation."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Extreme gap winds funneling down Mt. Shasta's flanks. SE winds "
                "predominate during fire events, accelerating through the gap "
                "between Mt. Shasta and the Eddy Mountains. 40-60 mph gusts "
                "routine. 'Not uncommon to have 50 to 60 mph gusts on a normal "
                "day.' Both the Boles and Mill fires were wind-driven events. "
                "The town was literally founded because of these winds."
            ),
            "critical_corridors": [
                "Mt. Shasta downslope (S/SE -- primary wind-driven fire axis)",
                "Roseburg mill complex (proven ignition source -- Mill Fire)",
                "I-5 corridor (fire crossed during Boles Fire)",
                "Lincoln Heights (directly in path of S wind)",
            ],
            "rate_of_spread_potential": (
                "Extreme in wind events. Boles Fire consumed half of downtown "
                "in under 2 hours on only 479 acres. Wind-driven structure-"
                "to-structure spread dominates. Mill Fire -- most acreage and "
                "structures lost on day one. Not a wildland spread problem; "
                "this is urban conflagration driven by wind and embers."
            ),
            "spotting_distance": (
                "1.0-2.0 mi in 40-60 mph winds. Embers thrown hundreds of "
                "yards ahead of fire front. Spot fires ignite simultaneously "
                "across neighborhoods, overwhelming suppression capacity."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "City of Weed municipal water system. Relatively modern but "
                "storage capacity limited for simultaneous multi-structure "
                "fire suppression. Hydrant pressure adequate in valley but "
                "drops on slopes."
            ),
            "power": (
                "PacifiCorp (not PG&E) serves Weed. Overhead distribution "
                "vulnerable to wind damage and fire. Power lost during both "
                "Boles and Mill fires."
            ),
            "communications": (
                "Moderate cell coverage. Emergency notification via Siskiyou "
                "County CodeRED system. Community notification boards at "
                "key intersections."
            ),
            "medical": (
                "No hospital in Weed. Nearest: Mercy Mt. Shasta Hospital "
                "(7 mi, Mt. Shasta city). During Mill Fire, 2 fatalities "
                "were residents unable to evacuate Lincoln Heights."
            ),
        },
        "demographics_risk_factors": {
            "population": 2862,
            "seasonal_variation": (
                "Moderate. I-5 traffic and Mt. Shasta recreation bring tourists. "
                "Summer and ski season peaks."
            ),
            "elderly_percentage": "est. 18-22%",
            "mobile_homes": (
                "Lincoln Heights mobile home park was a major concentration of "
                "mobile/manufactured homes -- devastated by Mill Fire 2022. "
                "Extremely vulnerable to wind-driven fire. Low-income residents "
                "with limited insurance and resources for rebuilding."
            ),
            "special_needs_facilities": (
                "Limited. Small-town services. Lincoln Heights had a "
                "disproportionately vulnerable population: elderly, low-income, "
                "mobile homes, limited transportation. Some residents unable "
                "to self-evacuate during Mill Fire."
            ),
        },
    },

    "dunsmuir_ca": {
        "center": [41.2317, -122.2715],
        "terrain_notes": (
            "Small railroad town (pop. ~1,700) in a narrow segment of the "
            "Sacramento River canyon, ~15 mi south of Mt. Shasta. The city is "
            "essentially a single-street town stretched along the canyon bottom "
            "at ~2,350 ft elevation, with I-5 and the railroad running through. "
            "Every home within the Sacramento River Canyon from the Dunsmuir-Mott "
            "Airport to the Shasta County line is classified as Very High Fire "
            "Hazard Severity Zone (VHFHSZ) -- the highest possible designation. "
            "Steep, heavily forested canyon walls rise 1,500-2,000 ft on both "
            "sides with dense mixed conifer (Douglas fir, white fir, ponderosa "
            "pine). Fire behavior depends critically on wind: a south wind can "
            "push fire north through the city via the canyon, while limited-wind "
            "fires may burn up canyon walls and away from structures. Delta Fire "
            "(Sep 2018; 60,277 acres) ignited near Lakehead, forced I-5 closure "
            "for 6 days, and triggered evacuation warnings for all Dunsmuir "
            "residents. Extreme fire behavior was observed: flame lengths to "
            "300 ft, spread rates up to 1 mi/hr, fire front 3 mi wide. "
            "Dunsmuir is California's 900th Firewise Community and the 1st in "
            "Siskiyou County."
        ),
        "key_features": [
            "Sacramento River canyon -- steep, narrow, heavily forested",
            "100% VHFHSZ designation for all structures in canyon",
            "I-5 corridor through town -- closed 6 days during Delta Fire",
            "Railroad town -- single-street linear layout along canyon",
            "California's 900th Firewise Community (1st in Siskiyou County)",
            "Siskiyou Fire Safe Council fuel reduction program (183 acres)",
            "Castle Crags State Park to south (granite spires, 4,350 ft)",
            "Mt. Shasta (14,179 ft) 15 mi north",
        ],
        "elevation_range_ft": [2100, 4350],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Delta Fire",
                "year": 2018,
                "acres": 60277,
                "details": (
                    "Human-caused fire ignited Sep 5 near Lakehead, 20 mi south. "
                    "Crossed and closed I-5 for 6 days. Evacuation warning for "
                    "all Dunsmuir. Extreme fire behavior: 300-ft flame lengths, "
                    "1 mph spread rates, 3-mi-wide fire front. Thick smoke "
                    "covered Dunsmuir for weeks."
                ),
            },
            {
                "name": "Soda Fire",
                "year": 2001,
                "acres": 480,
                "details": (
                    "Fire in the Sacramento River canyon near Dunsmuir. "
                    "Threatened structures along I-5 corridor."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Interstate 5 north to Mt. Shasta / Weed",
                "direction": "N",
                "lanes": 4,
                "bottleneck": (
                    "Best capacity route but I-5 itself runs through the fire-"
                    "prone canyon. Town has limited on-ramp access. Smoke from "
                    "canyon fires reduces visibility to near-zero."
                ),
                "risk": (
                    "I-5 was closed for 6 days during Delta Fire. The freeway "
                    "runs through the same steep, forested canyon as the town. "
                    "Fire can burn across I-5."
                ),
            },
            {
                "route": "Interstate 5 south to Redding",
                "direction": "S",
                "lanes": 4,
                "bottleneck": (
                    "Leads deeper into the Sacramento River canyon toward "
                    "Lakehead and Shasta Lake. Delta Fire origin area was "
                    "between Dunsmuir and Redding."
                ),
                "risk": (
                    "Evacuating south means driving through the canyon toward "
                    "potential fire area. Canyon narrows significantly south of "
                    "Castle Crags."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Canyon winds dominate. South winds channel through Sacramento "
                "River canyon and push fire north through town. North winds are "
                "less common but can push fire from Mt. Shasta area south. "
                "Diurnal upslope/downslope thermals create shifting fire behavior "
                "on canyon walls. Terrain channeling amplifies any ambient wind."
            ),
            "critical_corridors": [
                "Sacramento River canyon (N-S axis -- primary fire corridor)",
                "I-5 / railroad corridor (fire can run along transportation axis)",
                "Side drainages entering canyon (steep fire chimneys)",
                "Castle Crags area to south (rocky but fuel-laden benches)",
            ],
            "rate_of_spread_potential": (
                "Extreme in south-wind canyon channeling. Delta Fire demonstrated "
                "1 mph sustained spread with 300-ft flame lengths. Canyon geometry "
                "creates pre-heating effect on opposite wall. Fire running up "
                "canyon wall can shower town with embers from above."
            ),
            "spotting_distance": (
                "1.0-2.0 mi in wind-driven canyon events. Embers lofted from "
                "canyon walls rain down on town below. Cross-canyon spotting "
                "is a major threat."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "City of Dunsmuir municipal water from Sacramento River and "
                "springs. Canyon location provides adequate water supply but "
                "distribution infrastructure runs along narrow canyon bottom, "
                "vulnerable to fire damage."
            ),
            "power": (
                "PacifiCorp service area. Overhead distribution through "
                "dense forest canopy. Extremely vulnerable to fire and tree "
                "falls. Extended outages during fire events."
            ),
            "communications": (
                "Moderate cell coverage along I-5 corridor. Canyon walls "
                "block signal in side drainages. Emergency communication "
                "via Siskiyou County CodeRED."
            ),
            "medical": (
                "No hospital. Nearest: Mercy Mt. Shasta (15 mi north). "
                "Dunsmuir has a small clinic. Ambulance from Mt. Shasta "
                "or Redding depending on direction of fire."
            ),
        },
        "demographics_risk_factors": {
            "population": 1707,
            "seasonal_variation": (
                "Significant tourism: I-5 travelers, fly fishing on Sacramento "
                "River, Mt. Shasta recreation, Amtrak Coast Starlight stop. "
                "Summer population surges with visitors."
            ),
            "elderly_percentage": "est. 22-26%",
            "mobile_homes": (
                "Mobile home parks present along canyon floor. Vulnerable "
                "position at base of steep, forested canyon walls."
            ),
            "special_needs_facilities": (
                "Minimal. Small-town infrastructure. Aging population with "
                "limited mobility options. Railroad heritage community with "
                "many retirees."
            ),
        },
    },

    "hayfork_ca": {
        "center": [40.5543, -123.1833],
        "terrain_notes": (
            "Remote unincorporated community (pop. ~2,300) in Hayfork Valley, "
            "a broad mountain valley at ~2,310 ft elevation in the heart of "
            "Trinity County -- one of the most fire-prone and least accessible "
            "counties in California. Hayfork sits in a valley ringed by the "
            "Shasta-Trinity National Forest and Trinity Alps Wilderness. The "
            "surrounding terrain is extremely rugged: steep, forested mountains "
            "rising to 5,000-7,000 ft, deeply incised drainages, and very limited "
            "road access. Highway 3 is the primary (and essentially only) paved "
            "road serving Hayfork. Trinity County's Community Wildfire Protection "
            "Plan (one of the first in the US, finalized 2005) identifies Hayfork "
            "as a high-priority area. The Monument Fire (2021; 223,124 acres -- "
            "15th largest in CA history) came within 0.25 mi of Hayfork, forcing "
            "evacuation orders for multiple neighborhoods. The McFarland Fire "
            "(2021; 122,653 acres) also threatened Hayfork. Earlier, the Lime "
            "Complex fires repeatedly impacted the area with 30+ simultaneous "
            "lightning fires. The community is self-reliant out of necessity: "
            "the nearest hospital is 45+ mi away, and fire response is "
            "primarily volunteer-based. Trinity County Fire Safe Council (est. "
            "1998) is one of the oldest in California."
        ),
        "key_features": [
            "Hayfork Valley at 2,310 ft -- open valley ringed by mountains",
            "Trinity County -- among most fire-prone and remote CA counties",
            "Highway 3 only paved access -- extreme isolation",
            "Monument Fire (2021) came within 0.25 mi of town",
            "McFarland Fire (2021) -- 122,653 acres, evacuation center in Hayfork",
            "Shasta-Trinity National Forest surrounds community",
            "Trinity County Fire Safe Council (est. 1998, one of earliest in CA)",
            "Lime Complex lightning fires -- repeated multi-fire events",
            "Hayfork Ranger District (USFS) headquarters in town",
        ],
        "elevation_range_ft": [2200, 7000],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Monument Fire",
                "year": 2021,
                "acres": 223124,
                "details": (
                    "15th largest fire in modern CA history. Came within 0.25 mi "
                    "of Hayfork. Evacuation orders for residences on Ewing Road, "
                    "Brady Road, Farmer's Ranch Road, Sunshine Meadows, and "
                    "Harrison Road. 50 structures destroyed. 5,000 structures "
                    "threatened in Hayfork, Junction City, Weaverville, and "
                    "Douglas City. Fully contained Oct 27 after burning July-Oct."
                ),
            },
            {
                "name": "McFarland Fire",
                "year": 2021,
                "acres": 122653,
                "details": (
                    "Lightning-caused, started Jul 29, 2021 on McFarland Ridge "
                    "south of Hwy 36. 46 structures destroyed. Evacuation center "
                    "established in Hayfork."
                ),
            },
            {
                "name": "Lime Complex",
                "year": 2008,
                "acres": 39000,
                "details": (
                    "30+ simultaneous lightning fires in Hayfork Ranger District, "
                    "Shasta-Trinity National Forest. Largest concentration of "
                    "fires in the north state. Multiple summers of similar "
                    "lightning complex events."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 3 north to Weaverville / Hwy 299",
                "direction": "N",
                "lanes": 2,
                "bottleneck": (
                    "Only paved highway. Winding mountain road through forested "
                    "terrain. 25+ mi to Weaverville. Single-lane bridges. Very "
                    "limited capacity."
                ),
                "risk": (
                    "Monument Fire burned along portions of this route. Road "
                    "passes through dense forest for entire length. Fire on "
                    "either side blocks sole evacuation route."
                ),
            },
            {
                "route": "Highway 3 south to Highway 36",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Winding mountain road south through forest to Hwy 36. "
                    "Even more remote than northbound route. 30+ mi to Hwy 36."
                ),
                "risk": (
                    "McFarland Fire burned south of Hwy 36. Extremely remote "
                    "terrain with no services or alternate routes."
                ),
            },
            {
                "route": "Wildwood Road / County roads",
                "direction": "E",
                "lanes": 1,
                "bottleneck": (
                    "Unpaved or minimally paved county roads through national "
                    "forest. Not viable for mass evacuation. Seasonal closures."
                ),
                "risk": (
                    "Fire roads only. Not maintained for civilian traffic. "
                    "Can be blocked by single downed tree."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Complex terrain-driven winds in mountain valley. Diurnal "
                "upslope/downslope patterns dominate. Summer dry thunderstorms "
                "produce lightning without rain -- the primary ignition source. "
                "Hot, dry continental air mass in summer with extended drought "
                "periods. Valley inversions can trap smoke for weeks."
            ),
            "critical_corridors": [
                "Hayfork Creek drainage (N-S axis through valley)",
                "Mountain ridges surrounding valley (fire runs downslope toward town)",
                "Highway 3 corridor (sole evacuation and access route)",
                "Ewing Road / Brady Road area (Monument Fire approach vector)",
            ],
            "rate_of_spread_potential": (
                "Extreme on steep terrain. Monument Fire demonstrated explosive "
                "growth -- 22,000 acres in a single day. Terrain-driven upslope "
                "runs on surrounding mountains can produce 2+ mph spread rates. "
                "Valley floor is somewhat more moderate (open meadows/grassland)."
            ),
            "spotting_distance": (
                "1.0-2.0 mi in steep terrain with convective fire behavior. "
                "Lightning fires typically start on ridges and run downhill "
                "toward valley communities."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Hayfork Community Services District. Small system serving "
                "valley. Limited fire-flow capacity. Water tanks on valley "
                "edges. No pressurized fire hydrant system in outlying areas."
            ),
            "power": (
                "Trinity Public Utilities District (TPUD). Overhead lines "
                "through dense forest. Helena Fire (2017) started from tree "
                "falling on TPUD power line. Frequent extended outages during "
                "fire events. Limited backup generation."
            ),
            "communications": (
                "Very limited cell coverage. Many dead zones in surrounding "
                "mountains. Satellite phones used by some residents. USFS "
                "radio network provides supplemental communication. County "
                "emergency notification system has gaps in coverage."
            ),
            "medical": (
                "No hospital. Mountain Community Health Center (community clinic) "
                "in Hayfork. Nearest hospital: Trinity Hospital in Weaverville "
                "(25+ mi, 40+ min) or Redding (90+ mi, 2+ hrs). Volunteer "
                "ambulance service. Air ambulance (CalStar/REACH) for critical "
                "patients, weather permitting."
            ),
        },
        "demographics_risk_factors": {
            "population": 2324,
            "seasonal_variation": (
                "Minimal tourism but significant USFS seasonal workforce. "
                "Fire season brings hundreds of firefighters to area who "
                "use Hayfork as a base."
            ),
            "elderly_percentage": "est. 20-25%",
            "mobile_homes": (
                "Significant. Many manufactured/mobile homes on rural parcels. "
                "Low-income community with limited resources for fire-resistant "
                "construction upgrades."
            ),
            "special_needs_facilities": (
                "Hayfork Elementary and Trinity Valley Elementary. Mountain "
                "Community Health Center. No assisted living or nursing "
                "facilities. Very limited institutional support for "
                "vulnerable populations. Median household income $45,918 -- "
                "significantly below state median."
            ),
        },
    },

    "weaverville_ca": {
        "center": [40.7310, -122.9420],
        "terrain_notes": (
            "Trinity County seat (pop. ~3,700) in a mountain valley at ~2,050 ft "
            "elevation where Weaver Creek meets the Trinity River drainage. "
            "Surrounded by Shasta-Trinity National Forest with dense mixed-conifer "
            "forest (Douglas fir, ponderosa pine, white fir, incense cedar) on "
            "all surrounding slopes. More vulnerable than 90% of communities in "
            "California according to wildfire risk assessments. Highway 299 is "
            "the primary east-west route through town, connecting to Redding (45 "
            "mi east) and Eureka (100 mi west). The Helena Fire (Aug 30 - Nov 15, "
            "2017; 21,846 acres) started from a tree falling on a Trinity Public "
            "Utilities District power line near Helena, 8 mi west, and threatened "
            "Weaverville and Junction City. 72 homes destroyed, 2,000 evacuated, "
            "Hwy 299 closed. The Monument Fire (2021; 223,124 acres) also "
            "threatened Weaverville, with evacuation warnings issued. Weaverville "
            "is the commercial and government center for Trinity County, hosting "
            "the county hospital, courthouse, and key services. Community has "
            "embraced prescribed fire: once-time enemies over logging are now "
            "united as a community to prevent wildfire through managed fire."
        ),
        "key_features": [
            "Trinity County seat -- center of government and services",
            "Mountain valley at 2,050 ft, Shasta-Trinity National Forest surrounds",
            "More vulnerable than 90% of CA communities (risk assessment)",
            "Helena Fire (2017) -- 72 homes, 2,000 evacuated, Hwy 299 closed",
            "Monument Fire (2021) -- evacuation warnings for Weaverville",
            "Hwy 299 primary E-W route (Redding 45 mi E, Eureka 100 mi W)",
            "Highway 3 south to Hayfork (25 mi)",
            "Trinity County General Hospital -- only hospital in county",
            "Weaverville Joss House State Historic Park (1874 Chinese temple)",
            "Community prescribed burn advocacy and implementation",
        ],
        "elevation_range_ft": [1900, 5500],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Helena Fire",
                "year": 2017,
                "acres": 21846,
                "details": (
                    "Started Aug 30, 2017 from tree on TPUD power line near "
                    "Helena on Hwy 299, 8 mi west. Merged with Fork Fire "
                    "(3,484 acres). 72 homes destroyed. 2,000 evacuated. "
                    "Hwy 299 closed. Shelter at First Baptist Church, Weaverville. "
                    "Fully extinguished Nov 15."
                ),
            },
            {
                "name": "Monument Fire",
                "year": 2021,
                "acres": 223124,
                "details": (
                    "15th largest in CA history. Evacuation warnings issued "
                    "for Weaverville. Fire threatened 5,000 structures across "
                    "Trinity County including Weaverville, Junction City, "
                    "Hayfork, and Douglas City."
                ),
            },
            {
                "name": "Oregon Fire",
                "year": 2001,
                "acres": 17000,
                "details": (
                    "Burned near Weaverville in the Shasta-Trinity NF. "
                    "Threatened outlying areas of town."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 299 east to Redding",
                "direction": "E",
                "lanes": 2,
                "bottleneck": (
                    "Primary evacuation route. 45 mi winding mountain road to "
                    "Redding through forested terrain. 2 lanes, limited passing. "
                    "Helena Fire and other events have closed this road."
                ),
                "risk": (
                    "Road passes through dense forest for entire length. "
                    "Multiple fires have burned along or across Hwy 299. "
                    "Single-point-of-failure for eastbound evacuation."
                ),
            },
            {
                "route": "Highway 299 west to Eureka",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "100 mi mountain road to coast. Very remote. Helena Fire "
                    "started along this corridor and closed it."
                ),
                "risk": (
                    "Helena Fire demonstrated this route can be cut by fire. "
                    "Extremely long evacuation distance through fire-prone terrain."
                ),
            },
            {
                "route": "Highway 3 south to Hayfork",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "25 mi mountain road to Hayfork. Hayfork itself may be "
                    "under threat from same fire event (Monument Fire 2021)."
                ),
                "risk": (
                    "Evacuating to another fire-threatened community. "
                    "Route passes through national forest."
                ),
            },
            {
                "route": "Highway 3 north to Trinity Center / Scott Valley",
                "direction": "N",
                "lanes": 2,
                "bottleneck": (
                    "Mountain road following Trinity River north. Remote. "
                    "Trinity Lake / Clair Engle Lake area."
                ),
                "risk": (
                    "Remote terrain with limited services. Not a route to "
                    "population centers."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Complex terrain-driven winds. Upvalley/downvalley diurnal "
                "patterns along Trinity River and Weaver Creek drainages. "
                "Summer dry thunderstorms are the primary ignition source. "
                "Offshore NE events can create critical fire weather."
            ),
            "critical_corridors": [
                "Hwy 299 / Trinity River canyon (E-W primary fire corridor)",
                "Weaver Creek drainage (S approach into town center)",
                "Mountain ridges N and S (fire runs downslope toward valley)",
                "Junction City area (Helena Fire approach vector from W)",
            ],
            "rate_of_spread_potential": (
                "Extreme on steep terrain. Helena Fire demonstrated rapid "
                "growth in steep terrain west of town. Monument Fire grew "
                "22,000 acres in a single day. Steep slopes and heavy fuel "
                "loading create extreme fire behavior potential."
            ),
            "spotting_distance": (
                "1.0-2.0 mi in steep terrain with convective activity. "
                "Long-range spotting from pyroCb events possible."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Weaverville Community Services District. Mountain water "
                "supply from Weaver Creek and springs. System is adequate "
                "for community but fire-flow demands during large events "
                "can exceed capacity."
            ),
            "power": (
                "Trinity Public Utilities District (TPUD). Helena Fire was "
                "caused by tree on TPUD line. Overhead distribution through "
                "dense forest. Frequent outages."
            ),
            "communications": (
                "Better than surrounding Trinity County communities due to "
                "county seat status. Cell coverage adequate in town center "
                "but gaps in surrounding hills. County emergency services "
                "headquartered here."
            ),
            "medical": (
                "Trinity Hospital (25-bed critical access hospital) -- the "
                "only hospital in Trinity County. If Weaverville is threatened, "
                "hospital evacuation is a major logistical challenge. Nearest "
                "alternate hospital: Redding (45+ mi)."
            ),
        },
        "demographics_risk_factors": {
            "population": 3667,
            "seasonal_variation": (
                "Tourism: Trinity Lake recreation, historic downtown, gold "
                "rush heritage. Summer population increases with visitors "
                "and USFS seasonal workers."
            ),
            "elderly_percentage": "est. 22-28%",
            "mobile_homes": (
                "Mobile/manufactured homes throughout community and outlying "
                "areas. Low-income population."
            ),
            "special_needs_facilities": (
                "Trinity Hospital is the critical facility. County health "
                "and human services offices. Senior center. Small assisted "
                "living facilities. Hospital evacuation would require "
                "coordinated transport to Redding -- 45+ mi through "
                "fire-prone terrain."
            ),
        },
    },

    # =========================================================================
    # CENTRAL SIERRA -- Yosemite / Sequoia Gateway Communities
    # =========================================================================

    "mariposa_ca": {
        "center": [37.4849, -119.9664],
        "terrain_notes": (
            "Unincorporated community (pop. ~1,500) and Mariposa County seat at "
            "~2,000 ft elevation in the Sierra Nevada foothills, serving as the "
            "primary western gateway to Yosemite National Park via Highway 140. "
            "Terrain consists of rolling oak-woodland and chaparral-covered "
            "foothills deeply incised by Mariposa Creek and its tributaries. "
            "Steep slopes of 30-60% on canyon walls. Vegetation transitions from "
            "grassland/blue oak at lower elevations to mixed chaparral and "
            "foothill pine above 1,500 ft. The Detwiler Fire (Jul 16 - Sep 15, "
            "2017; 81,826 acres) burned east of Lake McClure and directly "
            "threatened Mariposa, forcing mandatory evacuation of the entire "
            "community as 5,000+ structures were threatened. 134 structures "
            "destroyed, 21 damaged. Cause: firearm-related. Four years later, "
            "the Oak Fire (Jul 22 - Sep 2, 2022; 19,244 acres) ignited nearby "
            "and forced 6,000+ evacuations, destroying 193 structures including "
            "127 homes. The Oak Fire's eastward progression was impeded by the "
            "2018 Ferguson Fire burn scar -- a rare positive effect of prior "
            "fire. A 71-year-old man was arrested for arson. Mariposa has a "
            "notably older demographic (median age 49.8, 33.2% age 65+) and "
            "high poverty rate (30.6%) that compound evacuation vulnerability. "
            "Tourism to Yosemite adds significant seasonal population."
        ),
        "key_features": [
            "Mariposa County seat -- primary Yosemite gateway via Hwy 140",
            "Sierra Nevada foothills at 2,000 ft -- oak woodland/chaparral",
            "Detwiler Fire (2017) -- entire town evacuated, 134 structures",
            "Oak Fire (2022) -- 6,000+ evacuated, 193 structures destroyed",
            "Ferguson Fire (2018) burn scar blocked Oak Fire spread east",
            "Extremely high elderly percentage (33.2% age 65+)",
            "High poverty rate (30.6%) limits fire-resistant upgrades",
            "Seasonal Yosemite tourism significantly increases population",
            "Mariposa County Fairgrounds serves as evacuation center",
        ],
        "elevation_range_ft": [1100, 3500],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Detwiler Fire",
                "year": 2017,
                "acres": 81826,
                "details": (
                    "Started Jul 16 near Detwiler Creek, east of Lake McClure. "
                    "Firearm-related cause. Exploded to 25,000 acres in one day. "
                    "State of emergency declared Jul 18. Entire Mariposa town "
                    "under mandatory evacuation. 134 structures destroyed, 21 "
                    "damaged. 5,000+ structures threatened."
                ),
            },
            {
                "name": "Oak Fire",
                "year": 2022,
                "acres": 19244,
                "details": (
                    "Started Jul 22, 2022. Arson (71-year-old arrested). 6,000+ "
                    "under evacuation orders by Jul 23. 193 structures destroyed "
                    "(127 residences, 66 outbuildings), 10 damaged. State of "
                    "emergency declared. Threatened Lushmeadows, Midpines, "
                    "Jerseydale, Bootjack. Eastward spread blocked by 2018 "
                    "Ferguson Fire burn scar."
                ),
            },
            {
                "name": "Ferguson Fire",
                "year": 2018,
                "acres": 96901,
                "details": (
                    "Burned in Merced River canyon on Hwy 140 approach to "
                    "Yosemite. Closed Hwy 140 and Yosemite Valley for weeks. "
                    "2 firefighter fatalities. Burn scar later served as de "
                    "facto fuel break during 2022 Oak Fire."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 140 west to Merced / Central Valley",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "Primary evacuation route descending to Central Valley. "
                    "2-lane mountain road for 30+ mi. Passes through foothill "
                    "terrain with fire exposure."
                ),
                "risk": (
                    "Detwiler Fire burned near Hwy 140. Road can be cut by "
                    "fire approaching from south. Long distance to safety."
                ),
            },
            {
                "route": "Highway 140 east to Yosemite (El Portal)",
                "direction": "E",
                "lanes": 2,
                "bottleneck": (
                    "Leads into Merced River canyon and Yosemite -- essentially "
                    "a dead end for evacuation purposes."
                ),
                "risk": (
                    "Not a viable evacuation route. Ferguson Fire closed "
                    "this road. Evacuating east leads deeper into fire-prone "
                    "terrain with no exit."
                ),
            },
            {
                "route": "Highway 49 south to Oakhurst",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "2-lane foothill road through fire-prone terrain. Connects "
                    "to Hwy 41 (another Yosemite approach). 30 mi to Oakhurst."
                ),
                "risk": (
                    "Passes through same chaparral and oak woodland fuel types "
                    "that feed Mariposa-area fires."
                ),
            },
            {
                "route": "Highway 49 north to Coulterville / Bear Valley",
                "direction": "N",
                "lanes": 2,
                "bottleneck": (
                    "Winding mountain road north. Very limited capacity. "
                    "Remote terrain."
                ),
                "risk": "Remote, fire-prone, no services for long distances.",
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Diurnal upslope/downslope winds dominate in summer. Afternoon "
                "upslope winds push fire from Central Valley toward foothills. "
                "Canyon winds in Merced River and Mariposa Creek drainages "
                "amplify fire behavior. Foehn events from NE less common than "
                "at higher elevations but produce critical conditions."
            ),
            "critical_corridors": [
                "Mariposa Creek drainage (fire chimney through town center)",
                "Hwy 49 corridor (N-S fire spread axis)",
                "Merced River canyon (E approach via Hwy 140)",
                "Bear Creek drainage (S/SW approach -- Oak Fire path)",
            ],
            "rate_of_spread_potential": (
                "Extreme. Detwiler Fire exploded to 25,000 acres in one day. "
                "Oak Fire burned 4,350 acres in first 9 hours. Chaparral and "
                "grass fuels support rapid spread. Steep terrain amplifies "
                "rates of spread significantly."
            ),
            "spotting_distance": (
                "1.0-2.0 mi in chaparral/oak woodland. Longer during convective "
                "column development. Oak and chaparral generate abundant embers."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Mariposa Public Utility District. Small system with limited "
                "storage. Fire-flow capacity is a significant concern during "
                "multi-structure events. Rural properties on wells."
            ),
            "power": (
                "PG&E distribution. Subject to PSPS. Overhead lines through "
                "oak woodland vulnerable to fire and tree contact."
            ),
            "communications": (
                "Moderate cell coverage in town center. Gaps in surrounding "
                "foothills. Mariposa County Sheriff reverse-911 system."
            ),
            "medical": (
                "John C. Fremont Healthcare District -- small critical access "
                "hospital. Limited capacity. Nearest major hospital: Mercy "
                "Medical Center, Merced (40+ mi west). High elderly population "
                "(33.2% age 65+) creates disproportionate medical evacuation "
                "demand."
            ),
        },
        "demographics_risk_factors": {
            "population": 1526,
            "seasonal_variation": (
                "Extreme. Yosemite tourism creates massive seasonal surge: "
                "4M+ annual Yosemite visitors pass through Mariposa. Summer "
                "population of the area can be many times the resident "
                "population. Visitors unfamiliar with fire risk and evacuation "
                "routes. Hotels, vacation rentals, and campgrounds add to "
                "evacuation demand."
            ),
            "elderly_percentage": "33.2% age 65+",
            "mobile_homes": (
                "Mobile/manufactured homes present throughout community. "
                "Affordable housing stock in a high-poverty community."
            ),
            "special_needs_facilities": (
                "John C. Fremont Hospital would require evacuation. Senior "
                "center and county social services in town. High elderly "
                "population with limited mobility. High poverty rate (30.6%) "
                "means many residents lack vehicles or evacuation resources."
            ),
        },
    },

    "groveland_ca": {
        "center": [37.8383, -120.2327],
        "terrain_notes": (
            "Tiny unincorporated community (pop. ~600) in Tuolumne County at "
            "~3,136 ft elevation on the Highway 120 approach to Yosemite "
            "National Park. Perched on a ridge between the Tuolumne River canyon "
            "to the north and the Clavey River to the south. Surrounded by "
            "Stanislaus National Forest with dense mixed-conifer cover (ponderosa "
            "pine, sugar pine, white fir, Douglas fir) and heavy chaparral on "
            "lower slopes. The Rim Fire (Aug 17 - Oct 24, 2013; 257,314 acres) "
            "ignited just 3 mi east of Groveland at the bottom of a canyon near "
            "the confluence of the Tuolumne and Clavey rivers, from an escaped "
            "illegal campfire. It became the 3rd largest fire in California "
            "history at the time and the largest in the Sierra Nevada range. "
            "112 structures destroyed, 78,895 acres burned inside Yosemite. "
            "15,000 residents were under evacuation order/advisory including "
            "Groveland and the Pine Mountain Lake community. Hwy 120 was closed "
            "for weeks. Groveland Community Services District operates 3 water "
            "treatment plants, 5 storage reservoirs, and 70 mi of distribution "
            "piping serving ~3,500 customers in the broader area. Pine Mountain "
            "Lake (private community of ~2,800 adjacent to Groveland) is a "
            "major WUI exposure area with homes in forested settings."
        ),
        "key_features": [
            "Highway 120 gateway to Yosemite -- only northern approach",
            "Ridge-top at 3,136 ft between Tuolumne and Clavey river canyons",
            "Rim Fire ground zero (2013, 257,314 acres -- 3rd largest in CA history at time)",
            "Pine Mountain Lake community (~2,800 pop) -- major WUI exposure",
            "GCSD water system: 3 treatment plants, 5 reservoirs, 70 mi pipe",
            "Stanislaus National Forest -- dense mixed conifer surrounds",
            "Hetch Hetchy water supply infrastructure (San Francisco)",
            "Groveland Ranger Station (USFS) -- threatened by Rim Fire",
        ],
        "elevation_range_ft": [1800, 5000],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Rim Fire",
                "year": 2013,
                "acres": 257314,
                "details": (
                    "3rd largest in CA history at the time. Ignited Aug 17, 2013 "
                    "from escaped campfire in canyon 3 mi east of Groveland. "
                    "112 structures destroyed. 78,895 acres burned inside "
                    "Yosemite National Park. 15,000 under evacuation order/advisory "
                    "including Groveland, Pine Mountain Lake, Big Oak Flat. "
                    "5,000+ firefighters including 650 inmate crews. Hwy 120 "
                    "closed. Contained Oct 24. $127M suppression cost."
                ),
            },
            {
                "name": "Moc Fire",
                "year": 2020,
                "acres": 2800,
                "details": (
                    "Burned near Moccasin along Hwy 120 corridor. Mandatory "
                    "evacuations for Groveland, Pine Mountain Lake, and Hwy 120 "
                    "communities. Demonstrated recurring fire threat to same area."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 120 west to Oakdale / Central Valley",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "Primary evacuation route. 2-lane mountain road descending "
                    "to Central Valley. Passes through Moccasin, Chinese Camp, "
                    "Jamestown (40+ mi to Valley floor). Winding with limited "
                    "passing opportunities."
                ),
                "risk": (
                    "Moc Fire (2020) forced evacuations along this route. "
                    "Road passes through fire-prone foothill terrain. Long "
                    "distance to safety."
                ),
            },
            {
                "route": "Highway 120 east to Yosemite",
                "direction": "E",
                "lanes": 2,
                "bottleneck": (
                    "Dead end into Yosemite -- not an evacuation route. Rim "
                    "Fire burned across Hwy 120 east of Groveland."
                ),
                "risk": (
                    "Rim Fire closed Hwy 120 east. Leads into wilderness with "
                    "no alternate exits."
                ),
            },
            {
                "route": "Ferretti Road / Pine Mountain Lake Roads",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Internal roads serving Pine Mountain Lake community. "
                    "Multiple routes within the subdivision but all funnel "
                    "to Hwy 120."
                ),
                "risk": (
                    "Pine Mountain Lake homes in forested setting. WUI fire "
                    "in the community would gridlock internal roads."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Diurnal canyon winds dominate. Afternoon upslope flow from "
                "Central Valley pushes fire up through foothill-to-montane "
                "transition zone. Canyon winds in Tuolumne and Clavey river "
                "drainages amplify fire behavior dramatically. Rim Fire "
                "named for 'Rim of the World' vista point where canyon winds "
                "drove explosive growth."
            ),
            "critical_corridors": [
                "Tuolumne River canyon (N/NE -- Rim Fire origin area)",
                "Clavey River canyon (S approach)",
                "Hwy 120 corridor (E-W fire spread axis)",
                "Pine Mountain Lake development (WUI ember exposure)",
            ],
            "rate_of_spread_potential": (
                "Extreme. Rim Fire demonstrated explosive growth driven by "
                "canyon winds -- tripled in size overnight. Started at canyon "
                "bottom and raced uphill. Terrain-driven fire runs on steep "
                "canyon walls produce extreme spread rates. Heavy fuel loading "
                "in mixed conifer."
            ),
            "spotting_distance": (
                "1.0-3.0 mi during convective column development. Rim Fire "
                "produced massive convective plume lofting embers for miles. "
                "Pine bark strips are effective long-range firebrands."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Groveland Community Services District: 3 water treatment "
                "plants, 5 storage reservoirs, 70 mi of distribution piping, "
                "~3,500 customers. System is relatively robust for community "
                "size. Hetch Hetchy Aqueduct (San Francisco water supply) "
                "passes through area -- the Rim Fire threatened this critical "
                "infrastructure serving 2.7M people."
            ),
            "power": (
                "PG&E distribution through dense forest. Subject to PSPS "
                "during fire weather. Overhead lines vulnerable. Hetch Hetchy "
                "hydroelectric facilities provide some local power."
            ),
            "communications": (
                "Limited cell coverage. Mountain terrain creates dead zones. "
                "Tuolumne County OES emergency notification system."
            ),
            "medical": (
                "No hospital. Nearest: Sonora Regional Medical Center "
                "(25+ mi west). Very limited medical services in community. "
                "Small, aging population."
            ),
        },
        "demographics_risk_factors": {
            "population": 600,
            "seasonal_variation": (
                "Extreme. Yosemite-bound traffic on Hwy 120 creates massive "
                "summer influx. Pine Mountain Lake (~2,800 residents) adds to "
                "area population. Vacation homes and short-term rentals. "
                "During Rim Fire, 15,000 people were in evacuation zone -- "
                "25x the Groveland CDP population."
            ),
            "elderly_percentage": "est. 30-35% (retirement community character)",
            "mobile_homes": (
                "Some mobile/manufactured homes. Pine Mountain Lake is "
                "primarily site-built homes but many are older construction "
                "not meeting current WUI standards."
            ),
            "special_needs_facilities": (
                "Minimal. Small community with no institutional care "
                "facilities. Pine Mountain Lake has community center."
            ),
        },
    },

    "three_rivers_ca": {
        "center": [36.4388, -118.9045],
        "terrain_notes": (
            "Unincorporated community (pop. ~2,100) in Tulare County at the "
            "western gateway to Sequoia National Park, where the North Fork, "
            "Middle Fork, and South Fork of the Kaweah River converge (hence "
            "the name). Elevation ~840 ft at town center, rising steeply to "
            "6,000+ ft on surrounding ridges. The community stretches linearly "
            "along Highway 198 through the Kaweah River canyon -- a narrow, "
            "steep-walled granite canyon with chaparral, blue oak, and foothill "
            "pine on lower slopes transitioning to mixed conifer above. The "
            "KNP Complex Fire (Sep 9 - Dec 2021; 88,307 acres) ignited by "
            "lightning in Sequoia National Park and threatened Three Rivers "
            "directly, forcing community evacuation. The fire merged at the "
            "Marble Fork of the Kaweah River and moved downhill, crossing the "
            "Middle Fork and threatening the highway corridor. Over 2,000 "
            "firefighters and $170M in suppression costs. The fire killed an "
            "estimated 7,500-10,600 mature giant sequoias (10-14% of species "
            "population). The SQF Complex (2020; 175,019 acres) also forced "
            "partial evacuation of Three Rivers. The Pier Fire (2017; 36,556 "
            "acres) killed 72 large giant sequoias nearby. Three Rivers has "
            "the classic gateway-community problem: massive tourist traffic "
            "through a narrow canyon on a single road."
        ),
        "key_features": [
            "Gateway to Sequoia National Park -- Hwy 198 sole access",
            "Confluence of three Kaweah River forks in steep granite canyon",
            "KNP Complex (2021) -- threatened town, killed thousands of sequoias",
            "SQF Complex (2020) -- partial evacuation, 175,019 acres",
            "Linear canyon community along Hwy 198 -- no cross streets",
            "Three Rivers Fire Safe Council (active fuels program)",
            "Sequoia Parks Conservancy recovery fund operations",
            "Lake Kaweah (Army Corps) downstream provides some buffer",
        ],
        "elevation_range_ft": [600, 6500],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "KNP Complex Fire",
                "year": 2021,
                "acres": 88307,
                "details": (
                    "Lightning-ignited Colony and Paradise fires merged in "
                    "Sequoia National Park. Forced evacuation of Three Rivers, "
                    "Wilsonia, Cedar Grove. 2,000+ firefighters. $170M+ "
                    "suppression cost. Killed est. 7,500-10,600 mature giant "
                    "sequoias (10-14% of species). Fire crossed Marble Fork "
                    "and Middle Fork of Kaweah River. Not contained until "
                    "Dec 2021 atmospheric rivers."
                ),
            },
            {
                "name": "SQF Complex",
                "year": 2020,
                "acres": 175019,
                "details": (
                    "Lightning complex (Castle and Shotgun fires, Aug 19 - "
                    "Jan 6, 2021). Parts of Three Rivers under mandatory "
                    "evacuation. Routes 190 and 198 closed. Sequoia NP closed "
                    "2 weeks. Killed 7,500-10,600 additional sequoias."
                ),
            },
            {
                "name": "Pier Fire",
                "year": 2017,
                "acres": 36556,
                "details": (
                    "Human-caused fire near Springville, burned in Sequoia NF. "
                    "Killed 72 large giant sequoias in Black Mountain Grove, "
                    "31 over 10 ft diameter. Did not directly threaten Three "
                    "Rivers but demonstrated the corridor's fire vulnerability."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 198 west to Visalia / Central Valley",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "SOLE evacuation route. 2-lane road through Kaweah River "
                    "canyon descending to Central Valley. Passes through "
                    "narrow canyon sections with limited width. 35 mi to "
                    "Visalia. Carries all park visitor traffic."
                ),
                "risk": (
                    "Single-point-of-failure. Fire in Kaweah River canyon "
                    "can cut Hwy 198 anywhere along its length. During KNP "
                    "Complex, fire crossed the Kaweah River threatening the "
                    "highway. No alternate routes exist."
                ),
            },
            {
                "route": "Highway 198 east into Sequoia National Park",
                "direction": "E",
                "lanes": 2,
                "bottleneck": (
                    "Leads into the park -- not an evacuation route. Dead "
                    "end at higher elevation."
                ),
                "risk": (
                    "KNP Complex fire was burning IN the park. Evacuating "
                    "east would drive directly into fire."
                ),
            },
            {
                "route": "North Fork Drive / local roads",
                "direction": "N",
                "lanes": 1,
                "bottleneck": (
                    "Narrow local roads into foothill areas. Not connected "
                    "to any through route. Dead ends."
                ),
                "risk": "Dead ends. Potential entrapment areas.",
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Diurnal canyon winds: strong upslope (E) afternoon flow and "
                "downslope (W) nighttime drainage. Kaweah River canyon acts "
                "as a major fire chimney during upslope events. Summer heat "
                "in the Central Valley creates strong upslope convection "
                "pushing fire toward higher terrain. Monsoonal thunderstorms "
                "provide lightning ignition."
            ),
            "critical_corridors": [
                "Kaweah River main canyon (E-W fire chimney along Hwy 198)",
                "North Fork Kaweah (N approach from Sequoia NP)",
                "Middle Fork Kaweah (NE approach -- KNP Complex crossed here)",
                "South Fork Kaweah (SE approach)",
            ],
            "rate_of_spread_potential": (
                "Extreme in steep canyon terrain. Upslope fire runs driven "
                "by canyon thermal winds can produce 2+ mph spread rates. "
                "Chaparral and grass fuels on lower slopes are flashy; mixed "
                "conifer above provides sustained high-intensity fire."
            ),
            "spotting_distance": (
                "1.0-2.0 mi in steep terrain. Canyon winds loft embers "
                "significant distances. Cross-canyon spotting is a major "
                "concern -- embers from one canyon wall ignite the opposite."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Three Rivers community water system. Small, limited storage. "
                "Kaweah River provides raw water but treatment capacity "
                "constrained. Fire-flow demands during structure protection "
                "can exceed system capacity. Many outlying properties on "
                "private wells."
            ),
            "power": (
                "Southern California Edison (SCE) service area. Overhead "
                "distribution through canyon. Subject to PSPS during fire "
                "weather. Power loss during KNP Complex."
            ),
            "communications": (
                "Limited cell coverage in canyon. Terrain blocks signals. "
                "Tulare County emergency notification system. NPS has its "
                "own communication network for park operations."
            ),
            "medical": (
                "No hospital. Nearest: Kaweah Health (formerly Kaweah Delta) "
                "in Visalia (35 mi west). Community has a volunteer fire "
                "department. Air ambulance for critical patients when weather "
                "permits. During major fire events, ambulance access is "
                "constrained by single-road canyon."
            ),
        },
        "demographics_risk_factors": {
            "population": 2053,
            "seasonal_variation": (
                "Extreme. Sequoia National Park receives 1.2M+ annual visitors, "
                "most passing through Three Rivers on Hwy 198. Summer weekends "
                "and holidays create massive traffic on the single road. Visitor "
                "population in the area can exceed resident population 10:1 on "
                "peak days. Visitors unfamiliar with fire risk, evacuation "
                "routes, or canyon hazards."
            ),
            "elderly_percentage": "est. 25-30% (retirement/rural character)",
            "mobile_homes": (
                "Mobile/manufactured homes present along Hwy 198 corridor. "
                "Vulnerable to both fire and river flooding."
            ),
            "special_needs_facilities": (
                "Three Rivers Elementary School. Small community services. "
                "No institutional care facilities. Aging population with "
                "limited transportation options in a single-road canyon "
                "community."
            ),
        },
    },
}
