"""
Enhanced Northern California Fire-Vulnerable City Terrain Profiles
==================================================================

Deep-research profiles for 5 NorCal cities: Paradise, Magalia, Santa Rosa,
Sonoma, and Redding. Written with operationally relevant detail derived from
NIST case studies, CAL FIRE incident reports, county after-action reviews,
and post-fire infrastructure assessments.

These entries are drop-in replacements for the corresponding keys in
CA_TERRAIN_PROFILES in california_profiles.py.

Sources:
    - NIST TN 2135 / TN 2252: Camp Fire case study & fire progression timeline
    - Lareau et al. 2018 (GRL): Carr Fire pyrotornadogenesis
    - Sonoma County AAR (June 2018): October 2017 Complex Fires
    - Sonoma County CWPP 2023 Update (Fire Safe Sonoma)
    - KLD Associates SAFE Study (Feb 2025): Sonoma Valley evacuation modeling
    - CAL FIRE incident reports: Camp, Tubbs, Nuns, Glass, Carr, Zogg, Fawn
    - Paradise Irrigation District water quality reports (2019-2020)
    - Butte County Grand Jury 2008 evacuation findings
    - NWS Sacramento post-event summaries (Jarbo Gap wind events)
    - Shasta County Fire Safe Council / CWPP documentation
    - Press Democrat / Chico Enterprise-Record investigative reporting
"""

ENHANCED_NORCAL_PROFILES = {

    # =========================================================================
    # FEATHER RIVER CANYON CORRIDOR -- Camp Fire
    # =========================================================================
    "paradise_ca": {
        "center": (39.7596, -121.6219),
        "elevation_ft": 1775,
        "terrain_notes": (
            "Ridge-top community (pop. ~26,000 pre-fire; ~11,000 as of late 2025) "
            "perched on a narrow basalt-capped mesa between the West Branch Feather "
            "River Canyon to the west and Butte Creek Canyon to the east. The ridge "
            "runs roughly N-S, 1.5-2 mi wide, with 1,000+ ft of relief on both "
            "flanks. Camp Fire (Nov 8, 2018) destroyed 18,804 structures and killed "
            "85 people in Paradise proper. Fire ignited at 06:33 on the Caribou-"
            "Palermo 115kV transmission line (Tower 27/222) near Pulga in the "
            "Feather River Canyon, then raced 7 mi downwind in <90 min driven by "
            "NE Jarbo Gap winds (sustained 35-45 mph, gusts to 50+ mph). NIST "
            "documented ember spotting up to 6.3 km (3.9 mi) ahead of the fire "
            "front, igniting spot fires in Paradise before the main front arrived. "
            "Average fire spread through wildland fuels south and west of Paradise "
            "was 1 m/s (~2.2 mph / 180 chains/hr). Within Paradise, spread rates "
            "could not be computed due to pervasive spot-fire coalescence -- the "
            "town was effectively burning simultaneously from hundreds of ignition "
            "points. Softball-sized embers lofted over the ridge and into Butte "
            "Creek Canyon. Terrain fundamentally limits evacuation: 3 primary "
            "routes (Skyway, Pentz Rd, Clark Rd) all drain south toward Chico, "
            "merging into 2-lane bottlenecks. During Camp Fire, 27,000 people "
            "attempted simultaneous evacuation; trips normally 25 min took 3-4 "
            "hours. Cars were abandoned on Skyway as flames overran the roadway. "
            "19 documented burnovers on roads. 17 cell towers destroyed in first "
            "hours, crippling emergency communications. Water system contaminated "
            "with benzene (up to 2,217 ug/L, 440x EPA chronic limit) after fire "
            "melted PVC service lines and vacuum-drew VOCs into the distribution "
            "system. 10,500 service lines affected; $300M+ to replace. PG&E has "
            "since de-energized the Caribou-Palermo line permanently and committed "
            "to undergrounding distribution lines in the rebuilt town."
        ),
        "danger_quadrants": ["west", "southwest", "northwest", "northeast"],
        "safe_quadrants": [],
        "key_features": [
            {
                "name": "Feather River Canyon (West Branch)",
                "bearing": "W/SW",
                "distance_mi": 1,
                "type": "major_canyon",
                "notes": (
                    "1,500+ ft deep canyon running NW-SE. Camp Fire ignition point "
                    "was at Pulga, 10 mi NE up-canyon. Canyon acts as wind tunnel "
                    "during NE foehn events, accelerating Jarbo winds to 50+ mph. "
                    "PG&E's now-decommissioned Caribou-Palermo 115kV transmission "
                    "line ran through this canyon. The canyon's steep, chaparral-"
                    "and-oak slopes create extreme pre-heating for upslope fire runs. "
                    "Highway 70 follows the canyon floor -- impassable during fire."
                ),
            },
            {
                "name": "Butte Creek Canyon",
                "bearing": "E",
                "distance_mi": 2,
                "type": "canyon",
                "notes": (
                    "Parallel canyon on east side of Paradise ridge, 800-1,000 ft "
                    "deep. During Camp Fire, embers lofted over the entire ridge "
                    "and ignited spot fires in Butte Creek Canyon. Centerville Rd "
                    "drops into this canyon -- steep, narrow, not viable for mass "
                    "evacuation. Canyon contains scattered rural residences with "
                    "minimal defensible space."
                ),
            },
            {
                "name": "Jarbo Gap",
                "bearing": "NE",
                "distance_mi": 8,
                "type": "wind_gap",
                "notes": (
                    "Critical topographic constriction where the Feather River "
                    "Canyon narrows between Jarbo Gap Ridge and Table Mountain. "
                    "NE winds from the Great Basin funnel through this gap and "
                    "accelerate via the Venturi effect, creating the locally-named "
                    "'Jarbo winds' -- katabatic foehn events reaching 50-70 mph. "
                    "The NWS Sacramento office has documented multiple Jarbo wind "
                    "events producing red flag conditions on the Paradise ridge. "
                    "When winds align NE-to-SW through Jarbo Gap, the entire "
                    "Feather River Canyon becomes a blowtorch aimed at Paradise."
                ),
            },
            {
                "name": "Concow / Concow Reservoir",
                "bearing": "N/NW",
                "distance_mi": 5,
                "type": "canyon_community",
                "notes": (
                    "Mountain community in a bowl-shaped valley at 2,100 ft. "
                    "Burned early in Camp Fire (07:30, ~1 hr after ignition). "
                    "4 residents killed. Concow Rd provides only access -- "
                    "narrow, winding, no shoulders. Concow Reservoir (PG&E) "
                    "provides limited water supply but no fire suppression "
                    "capacity. Community is a sentinel: if Concow is burning, "
                    "Paradise has 30-60 min before fire arrival in Jarbo wind events."
                ),
            },
            {
                "name": "Skyway (SR 191)",
                "bearing": "S",
                "type": "access_route",
                "notes": (
                    "Primary evacuation route -- 4-lane divided highway through "
                    "downtown Paradise that was NARROWED TO 2 LANES in 2014 as a "
                    "'complete streets' project (bike lanes, parking, pedestrian "
                    "improvements). A 2008 Butte County Grand Jury had warned about "
                    "inadequate evacuation capacity. During Camp Fire, all lanes "
                    "were converted to outbound but gridlock persisted for 3-4 "
                    "hours. Skyway narrows further to 2 lanes south of Paradise "
                    "at Wagstaff Rd, creating the worst bottleneck. Carries ~60% "
                    "of evacuation traffic. Post-fire: town plans to convert to "
                    "one-way outbound during emergencies with contraflow. Road "
                    "connects to SR 99 in Chico (12 mi south)."
                ),
            },
            {
                "name": "Pentz Road",
                "bearing": "SW",
                "type": "access_route",
                "notes": (
                    "Secondary evacuation route. 2-lane road running SW from "
                    "Paradise to Durham/Hwy 99. During Camp Fire, used as "
                    "alternate when Skyway gridlocked. Road passes through "
                    "open rangeland south of town -- less fire exposure than "
                    "Skyway but no shoulders, limited capacity. Post-fire plan: "
                    "contraflow to create 2 outbound lanes during evacuation. "
                    "Carries ~25% of evacuation traffic."
                ),
            },
            {
                "name": "Clark Road",
                "bearing": "S",
                "type": "access_route",
                "notes": (
                    "Tertiary evacuation route. 2-lane road running S through "
                    "forest, parallel to Skyway. Passes through the most heavily "
                    "treed section of the ridge. During Camp Fire, fire burned "
                    "across Clark Rd early, trapping evacuees. Multiple burnovers "
                    "documented. Carries ~15% of evacuation traffic."
                ),
            },
            {
                "name": "South Libby Road Extension (planned)",
                "bearing": "S/SW",
                "type": "access_route",
                "notes": (
                    "NEW road planned post-Camp Fire to create cross-town "
                    "connection between Skyway and Pentz Rd. Site chosen because "
                    "multiple fatalities occurred at dead-end roads nearby. "
                    "Funded through FEMA Hazard Mitigation Grant. When completed, "
                    "will provide a 4th evacuation corridor and reduce Skyway "
                    "bottleneck by 15-20%."
                ),
            },
            {
                "name": "Neal Road",
                "bearing": "SW",
                "type": "access_route",
                "notes": (
                    "Narrow 2-lane mountain road dropping into Neal Rd / "
                    "Butte Creek Canyon area. Steep grades, tight curves, no "
                    "shoulders. Useful for residents on SW side of town but "
                    "limited capacity. Fire burned over this road during Camp Fire."
                ),
            },
            {
                "name": "Paradise Irrigation District Reservoirs",
                "bearing": "N",
                "distance_mi": 2,
                "type": "water_supply",
                "notes": (
                    "Paradise Reservoir and Magalia Reservoir (combined 12,293 "
                    "acre-feet capacity) fed by Little Butte Creek watershed. "
                    "Magalia Dam (1918) rated 'poor' by Division of Dam Safety, "
                    "storage limited to 796 acre-feet (vs designed volume) due "
                    "to seismic concerns. Camp Fire destroyed distribution system; "
                    "benzene contamination rendered water unusable for 2+ years. "
                    "System largely rebuilt by 2022 with $300M+ investment."
                ),
            },
        ],
        "historical_fires": [
            "Camp Fire 2018 (85 killed, 18,804 structures, 153,336 acres, deadliest CA fire in modern history)",
            "Ponderosa Fire 2017 (23 structures, same general area)",
            "Dixie Fire 2021 (963,309 acres, largest single-source CA fire, threatened rebuilt Paradise)",
            "Park Fire 2024 (429,000+ acres, evacuation warnings issued for Paradise/Magalia)",
            "Humboldt Fire 2008 (87 structures, triggered Grand Jury evacuation review)",
        ],
        "wui_class": "extreme",
        "population": {
            "pre_fire_2018": 26000,
            "post_fire_low": 1000,
            "current_2025": 11000,
            "pct_elderly_65plus": 25,
            "growth_rate_annual_pct": 6.57,
            "notes": (
                "Named fastest-growing town in California (2024-2025). "
                "3,000+ homes rebuilt, 1,500+ under construction as of early 2025. "
                "Town expects 75% of pre-fire population by 2035. Median age "
                "skews older; pre-fire ~38% were 55+."
            ),
        },
        "post_fire_changes": [
            "PG&E Caribou-Palermo 115kV line permanently de-energized (2019)",
            "PG&E committed to undergrounding distribution lines in rebuilt areas",
            "Town adopted Chapter 15 fire-resistant building codes (ember/radiant heat)",
            "Skyway contraflow evacuation plan adopted",
            "South Libby Rd extension funded (new cross-town evacuation connector)",
            "Road widening and shoulder improvements on Skyway south of town",
            "Butte County Fire Safe Council expanded with FIREWISE communities",
            "Prescribed burns in Magalia watershed (USFS, ongoing)",
            "AlertWildfire camera network expanded on ridge",
            "$300M+ water system rebuild completed (new PVC-free service lines)",
            "Cell tower hardening with backup generators (17 destroyed in Camp Fire)",
        ],
    },

    "magalia_ca": {
        "center": (39.8113, -121.5783),
        "elevation_ft": 2221,
        "terrain_notes": (
            "Unincorporated community (pop. 7,795 per 2020 census, down from "
            "11,310 in 2010) on the same narrow basalt ridge as Paradise but "
            "3 mi farther north and 450 ft higher. Denser mixed-conifer forest "
            "(ponderosa pine, Douglas fir, incense cedar) with heavier fuel "
            "loading than lower-elevation Paradise. Camp Fire killed at least "
            "7 Magalia residents and destroyed hundreds of homes. Even more "
            "isolated than Paradise: primary egress is south through Paradise "
            "on Skyway, meaning any fire approaching from the south can cut off "
            "the main escape route entirely. Secondary northern egress via "
            "Skyway north to Stirling City/Inskip is a narrow, winding mountain "
            "road. During the Park Fire (July 2024), evacuation warnings were "
            "issued for Magalia, and the northern Skyway was already degraded -- "
            "a 185-ft section narrowed to only 11.5 ft wide from winter storm "
            "damage (2022-23), creating a severe single-lane bottleneck for both "
            "evacuation traffic and inbound fire apparatus. FEMA repair funding "
            "approved but not yet released as of early 2025. Demographics "
            "compound risk: median age 45.2, with 20.8% age 65+, many with "
            "mobility limitations. Forest canopy closes over roads, creating "
            "ember tunnels. USFS initiated prescribed burns in the Magalia "
            "watershed (2024-25) to reduce fuel loads around the reservoir and "
            "protect Paradise Irrigation District water supply."
        ),
        "danger_quadrants": ["west", "southwest", "south", "northwest"],
        "safe_quadrants": [],
        "key_features": [
            {
                "name": "Feather River Canyon (West Branch)",
                "bearing": "W",
                "distance_mi": 2,
                "type": "major_canyon",
                "notes": (
                    "Same canyon system that channeled Camp Fire. Magalia's "
                    "western flank drops steeply into the canyon with 1,200+ ft "
                    "of relief over ~1 mi. Dense brush and oak woodland on slopes. "
                    "Any fire running up-canyon from the W/SW will hit Magalia "
                    "with pre-heated, wind-driven flames. Less defensible than "
                    "Paradise because of denser tree cover and narrower ridge."
                ),
            },
            {
                "name": "Butte Creek Canyon",
                "bearing": "E",
                "distance_mi": 2,
                "type": "canyon",
                "notes": (
                    "Eastern canyon paralleling the ridge. 800+ ft deep. "
                    "During Camp Fire, embers crossed the entire Paradise-Magalia "
                    "ridge and spotted into this drainage. Rural homes in canyon "
                    "bottom have extremely limited egress."
                ),
            },
            {
                "name": "Paradise (downhill, south)",
                "bearing": "S",
                "distance_mi": 3,
                "type": "community",
                "notes": (
                    "Critical dependency: Magalia's primary evacuation route "
                    "runs THROUGH Paradise on Skyway. If Paradise is burning "
                    "(as in Camp Fire), Magalia residents face a lethal trap -- "
                    "fire below on the only high-capacity road out. During Camp "
                    "Fire, Magalia residents had to drive through active fire "
                    "zones in Paradise to reach Chico. This is the single most "
                    "dangerous evacuation geometry in California."
                ),
            },
            {
                "name": "Magalia Reservoir / Dam",
                "bearing": "NW",
                "distance_mi": 1,
                "type": "water_supply",
                "notes": (
                    "Part of Paradise Irrigation District system. Dam built 1918, "
                    "rated 'poor' structurally. Storage limited to 796 acre-feet "
                    "(fraction of design capacity) by Division of Dam Safety. "
                    "Watershed is the target of ongoing USFS prescribed burn "
                    "program to reduce fuel loads and protect water supply. "
                    "Little Butte Creek feeds the reservoir from forested "
                    "headwaters to the north."
                ),
            },
            {
                "name": "Skyway south (through Paradise to Chico)",
                "bearing": "S",
                "type": "access_route",
                "notes": (
                    "PRIMARY evacuation route. 2-lane road through dense forest "
                    "north of Paradise, then through Paradise itself (see Paradise "
                    "profile for Skyway bottleneck details). From Magalia to "
                    "Chico is ~18 mi. During Camp Fire, this route was the "
                    "only viable option for most residents, taking 3-5 hours. "
                    "Canopy-covered sections trap smoke and embers. No alternate "
                    "parallel road exists."
                ),
            },
            {
                "name": "Skyway north / Stirling City Road",
                "bearing": "N",
                "type": "access_route",
                "notes": (
                    "SECONDARY evacuation route -- narrow, winding 2-lane "
                    "mountain road climbing NE toward Stirling City and Inskip. "
                    "Currently DEGRADED: 185-ft section narrowed to 11.5 ft "
                    "(single lane) from 2022-23 storm damage. FEMA repair "
                    "funding approved but stalled. During Park Fire (2024), "
                    "this route was needed for Forest Ranch evacuees heading "
                    "to the valley while fire apparatus moved in the opposite "
                    "direction -- severe conflict. Road eventually connects to "
                    "Hwy 32 but adds 25+ mi and 45+ min to valley floor. "
                    "Not a realistic mass-evacuation route."
                ),
            },
            {
                "name": "Coutolenc Road",
                "bearing": "NE",
                "type": "access_route",
                "notes": (
                    "Narrow mountain road providing limited alternate access "
                    "to the NE. Steep grades, unpaved sections, tight switchbacks. "
                    "May be passable for local residents who know the road but "
                    "not viable for mass evacuation. Can be blocked by single "
                    "downed tree."
                ),
            },
            {
                "name": "Concow",
                "bearing": "NW",
                "distance_mi": 4,
                "type": "canyon_community",
                "notes": (
                    "Sentinel community. When fire reaches Concow from the NE "
                    "(as in Camp Fire), Magalia has 20-40 min warning depending "
                    "on wind speed. Concow burned at 07:30 during Camp Fire; "
                    "fire reached Magalia by 09:00-10:00."
                ),
            },
        ],
        "historical_fires": [
            "Camp Fire 2018 (7+ killed in Magalia, hundreds of structures destroyed)",
            "Park Fire 2024 (429,000+ acres, evacuation warnings issued for Magalia)",
            "Dixie Fire 2021 (963,309 acres, smoke/ember concerns)",
        ],
        "wui_class": "extreme",
        "population": {
            "census_2010": 11310,
            "census_2020": 7795,
            "pct_elderly_65plus": 20.8,
            "median_age": 45.2,
            "notes": (
                "Population dropped 31% from Camp Fire displacement. "
                "Rebuilding slower than Paradise due to more remote location, "
                "older housing stock, and higher forest density. Large elderly "
                "population with mobility limitations complicates evacuation."
            ),
        },
        "post_fire_changes": [
            "USFS prescribed burns in Magalia watershed (2024-25, ongoing)",
            "Butte County evacuation zone system adopted (replaces ad-hoc orders)",
            "AlertWildfire camera network expanded",
            "Skyway contraflow plan includes Magalia",
            "Skyway north (Stirling City Rd) repair funded but stalled (FEMA)",
        ],
    },

    # =========================================================================
    # SONOMA / NAPA WINE COUNTRY CORRIDOR
    # =========================================================================
    "santa_rosa_ca": {
        "center": (38.4404, -122.7141),
        "elevation_ft": 167,
        "terrain_notes": (
            "Sonoma County seat (pop. 178,127 per 2020 census) on the Santa Rosa "
            "Plain, a broad valley floor backed by the Mayacamas Mountains to the "
            "east and Sonoma Mountains to the SE. The WUI interface is concentrated "
            "on the NE and N edges of the city where suburban development climbs "
            "into oak-woodland and chaparral hillsides. Tubbs Fire (Oct 8-9, 2017) "
            "ignited near Tubbs Lane in Calistoga and raced 12 miles in 3 hours "
            "driven by extreme Diablo winds (gusts 60-65+ mph recorded in northern "
            "Santa Rosa). Fire entered the city at ~1 AM via the Mark West Springs "
            "corridor, a steep drainage system that channels NE winds directly from "
            "the Napa Valley side of the Mayacamas into the NE edge of Santa Rosa. "
            "Fire moved down ravines between Mark West Springs Road and Fountaingrove "
            "Parkway, incinerating the Fountaingrove hilltop development (Very High "
            "FHSZ, 201.7 acres of wildlands within the 600-acre development) and "
            "then spotting across Hwy 101 into Coffey Park at ~3 AM, where 1,300+ "
            "wood-frame homes were destroyed in roughly 3 hours. The Coffey Park "
            "devastation demonstrated that urban conflagration can occur miles from "
            "the WUI -- embers carried across a 6-lane freeway. Glass Fire (2020) "
            "again threatened the eastern edge along the same NE approach vector. "
            "Historical precedent: the 1964 Hanly Fire took the identical path -- "
            "Calistoga to Porter Creek/Mark West Springs into Sonoma County. "
            "Water system failed during Tubbs Fire: Fountaingrove storage tanks "
            "were at 33% capacity (2 of 10 tanks offline for seismic retrofit). "
            "Firefighters repeatedly lost hydrant pressure on hilltops and had to "
            "retreat to valley floor to refill engines. Post-fire, PVC pipes that "
            "melted contaminated the water system with benzene; $43M replacement "
            "of 350 service lines, 210 valves, 70 hydrants in 184-acre advisory "
            "zone. Approximately 18.6% of population is 65+."
        ),
        "danger_quadrants": ["northeast", "east", "north"],
        "safe_quadrants": ["west", "southwest"],
        "key_features": [
            {
                "name": "Mark West Springs corridor",
                "bearing": "NE",
                "distance_mi": 5,
                "type": "major_canyon",
                "notes": (
                    "THE critical fire corridor for Santa Rosa. Steep drainage "
                    "running NE-to-SW from the Mayacamas crest down to the Santa "
                    "Rosa Plain. Tubbs Fire (2017) and Hanly Fire (1964) both "
                    "followed this exact path. Mark West Springs Road winds through "
                    "the drainage with dense WUI development on both sides -- "
                    "homes intermixed with oak woodland and chaparral. During "
                    "Diablo wind events, NE winds accelerate through this corridor "
                    "at 40-65 mph, pushing fire downslope directly into Fountaingrove "
                    "and northern Santa Rosa. Road was closed during Tubbs Fire at "
                    "Mark West Springs @ Old Redwood Hwy and @ Sutter Hospital. "
                    "Multiple residential communities along the corridor have "
                    "only one way in/out."
                ),
            },
            {
                "name": "Mayacamas Mountains",
                "bearing": "E/NE",
                "distance_mi": 10,
                "type": "mountain",
                "notes": (
                    "2,700 ft crest separating Sonoma and Napa valleys. Source "
                    "terrain for Diablo wind events. Steep west-facing slopes "
                    "covered in mixed chaparral, manzanita, and oak woodland. "
                    "Glass Fire (2020) originated in this range. Tubbs Fire "
                    "crossed the crest from the Napa side. Cavedale Road fuel "
                    "break project (100-ft shaded fuel break + fire road reopening) "
                    "completed post-fires to improve access and slow fire spread."
                ),
            },
            {
                "name": "Sonoma Mountains",
                "bearing": "SE",
                "distance_mi": 8,
                "type": "mountain",
                "notes": (
                    "Source terrain for Nuns Fire (2017). Chaparral and oak "
                    "woodland on steep slopes. Bennett Ridge community lost "
                    "92 of 129 homes in Nuns Fire."
                ),
            },
            {
                "name": "Fountaingrove",
                "bearing": "NE",
                "distance_mi": 2,
                "type": "wui_neighborhood",
                "notes": (
                    "Hilltop development on Santa Rosa's NE edge, designated "
                    "Very High Fire Hazard Severity Zone. 600-acre development "
                    "with 201.7 acres of intermixed wildlands. Sits on a "
                    "prominent ridgeline at 600-900 ft elevation. Destroyed by "
                    "Tubbs Fire when flames came down ravines from Mark West "
                    "Springs corridor. Water tanks serving Fountaingrove were "
                    "at 33% capacity when fire hit; firefighters lost hydrant "
                    "pressure. Still rebuilding as of 2025 (Fir Ridge area "
                    "mostly rebuilt, scattered lots under construction). "
                    "Fountaingrove II CWPP adopted with fuels management plan."
                ),
            },
            {
                "name": "Coffey Park",
                "bearing": "N/NW",
                "distance_mi": 3,
                "type": "wui_neighborhood",
                "notes": (
                    "Suburban neighborhood WEST of Hwy 101 that was devastated "
                    "by urban conflagration -- 1,300+ wood-frame homes destroyed "
                    "between 3-6 AM during Tubbs Fire. This was NOT a WUI fire; "
                    "embers crossed the 6-lane Hwy 101 freeway and ignited homes "
                    "in a purely urban setting. Demonstrated that Diablo wind-"
                    "driven ember transport can cause conflagration miles from "
                    "wildland fuels. Now 96-97% rebuilt with improved fire-"
                    "resistant construction. City adopted ordinance banning "
                    "'gorilla hair' redwood mulch within 30 ft of structures "
                    "(ember-catching material)."
                ),
            },
            {
                "name": "Hwy 101 corridor",
                "bearing": "N-S",
                "type": "access_route",
                "notes": (
                    "Primary N-S evacuation route through Santa Rosa. 6-lane "
                    "freeway with generally adequate capacity for the valley "
                    "floor, but on-ramps from eastern neighborhoods (Fountaingrove, "
                    "Rincon Valley) were gridlocked during Tubbs Fire. During "
                    "Tubbs Fire the freeway itself was traversed by embers, so "
                    "it does not serve as a firebreak. Multiple interchanges "
                    "serve as evacuation collection points: Mendocino Ave, "
                    "Bicentennial Way, Old Redwood Hwy."
                ),
            },
            {
                "name": "Hwy 12 (east)",
                "bearing": "E",
                "type": "access_route",
                "notes": (
                    "Connects Santa Rosa to Sonoma Valley and Napa. 2-4 lane "
                    "road through narrow valley. Intersections at Farmers Ln "
                    "and Hoen Ave gridlock during heavy traffic. During Nuns "
                    "Fire, Hwy 12 was closed east of Kenwood. NOT a viable "
                    "eastbound evacuation route during fires approaching from NE."
                ),
            },
        ],
        "historical_fires": [
            "Tubbs Fire 2017 (22 killed Sonoma County, 5,643 structures, 36,807 acres)",
            "Glass Fire 2020 (1,555 structures, 67,484 acres, mostly outside city limits)",
            "Nuns Fire 2017 (54,382 acres, merged with Norrbom Fire, burned to city edge)",
            "Hanly Fire 1964 (identical Mark West Springs corridor path to Tubbs Fire)",
        ],
        "wui_class": "high",
        "population": {
            "census_2020": 178127,
            "pct_elderly_65plus": 18.6,
            "notes": (
                "Largest city in Sonoma County. 34.3% Hispanic/Latino. "
                "Significant homeless population (~3,000 county-wide) in "
                "urban-wildland fringe areas, complicating evacuation notification."
            ),
        },
        "post_fire_changes": [
            "Coffey Park 96-97% rebuilt with improved fire-resistant construction",
            "Fountaingrove rebuilding ongoing (Fir Ridge mostly complete)",
            "City adopted 2019 fuels ordinance (dead tree removal, gorilla-hair mulch ban within 30 ft)",
            "SoCo Alert emergency notification system deployed county-wide",
            "Networked wildfire cameras installed across eastern hills",
            "Sonoma County CWPP 2023 Update adopted (Fire Safe Sonoma)",
            "Fountaingrove II CWPP with fuels management plan",
            "Cavedale Road fuel break (100-ft shaded) along Mayacamas crest",
            "$43M water system rebuild in Fountaingrove contamination zone",
            "Sonoma County evacuation zone system (replaces ad-hoc warnings)",
            "Ballot Measure H funded additional fire engine company",
            "COPE and CERT community preparedness programs expanded",
        ],
    },

    "sonoma_ca": {
        "center": (38.2920, -122.4580),
        "elevation_ft": 75,
        "terrain_notes": (
            "Historic wine country town (pop. 10,739 per 2020 census) on the "
            "floor of Sonoma Valley -- a narrow N-S valley flanked by Sonoma "
            "Mountain (2,295 ft) to the west and the Mayacamas Mountains "
            "(2,700 ft crest) to the east. The valley is sometimes called the "
            "'Valley of the Moon.' Town sits at the southern end of the valley "
            "where it widens slightly toward San Pablo Bay. Nuns Fire (2017) "
            "burned 56,000+ acres through the eastern mountains, destroyed 400+ "
            "homes in the upper valley (Glen Ellen, Kenwood, Bennett Ridge), "
            "and came within a few miles of Sonoma town. The valley's fundamental "
            "evacuation problem was quantified by the 2025 KLD Associates SAFE "
            "(Sonoma Area Fire Evacuation) Study: only two parallel N-S routes "
            "exist -- Highway 12 and Arnold Drive -- with almost no lateral "
            "east-west escape over the flanking mountains. Modeling shows 4-9 "
            "hours of gridlock during a full-valley evacuation, with speeds "
            "dropping to 1-2 mph on both routes. Arnold Drive evacuation time: "
            "171 min under current conditions. Glen Ellen residents face up to "
            "9 hours of congestion. The valley floor itself is lower-fuel "
            "(vineyards, irrigated pasture), but the surrounding hillsides are "
            "dense chaparral and oak woodland that burn with high intensity. "
            "Sonoma Mountain's east face and the Mayacamas' west face both "
            "drain into the valley through multiple steep canyons that channel "
            "Diablo winds. The town is essentially in a topographic bowl with "
            "two straws to drink from -- both inadequate."
        ),
        "danger_quadrants": ["east", "northeast", "north", "northwest"],
        "safe_quadrants": ["south"],
        "key_features": [
            {
                "name": "Sonoma Valley floor",
                "bearing": "N-S",
                "type": "valley",
                "notes": (
                    "Narrow valley (~2-3 mi wide at Sonoma, narrowing to <1 mi "
                    "at Glen Ellen). Vineyards and irrigated pasture on valley "
                    "floor provide reduced fuel loads and moderate buffer, but "
                    "surrounding hillsides are highly combustible chaparral, "
                    "manzanita, and oak woodland. Diablo winds channel through "
                    "the valley at 30-60 mph during offshore events. Valley "
                    "orientation (NW-SE) aligns with prevailing Diablo wind "
                    "direction, amplifying wind exposure."
                ),
            },
            {
                "name": "Mayacamas Mountains (east wall)",
                "bearing": "E/NE",
                "distance_mi": 5,
                "type": "mountain",
                "notes": (
                    "Steep, chaparral-covered range rising to 2,700 ft. Source "
                    "zone for Nuns Fire (2017) and Glass Fire (2020). Multiple "
                    "drainages cut west from the crest into the valley: Sonoma "
                    "Creek, Calabazas Creek, Arroyo Seco. Each drainage acts as "
                    "a fire chimney during NE wind events. Moon Mountain sub-"
                    "range on the eastern valley wall has heavy WUI development "
                    "in fire-prone terrain."
                ),
            },
            {
                "name": "Sonoma Mountain",
                "bearing": "W/NW",
                "distance_mi": 5,
                "type": "mountain",
                "notes": (
                    "2,295 ft peak forming the western valley wall. East-facing "
                    "slopes are steep, dry, and covered in grass/oak/chaparral. "
                    "Fire on Sonoma Mountain would run downslope into the valley "
                    "under afternoon thermal winds or NW wind events. Jack London "
                    "State Historic Park occupies slopes above Glen Ellen."
                ),
            },
            {
                "name": "Glen Ellen / Kenwood (upper valley)",
                "bearing": "N/NW",
                "distance_mi": 5,
                "type": "community",
                "notes": (
                    "Small communities at the narrow throat of Sonoma Valley. "
                    "Nuns Fire destroyed parts of Glen Ellen and burned along "
                    "the edge of Sonoma Developmental Center (SDC). Mandatory "
                    "evacuations covered everything north of Madrone Rd to "
                    "Hwy 12 & Dunbar Rd. SAFE Study projects 9 hours of "
                    "congestion for Glen Ellen residents in a future evacuation. "
                    "SDC redevelopment plan controversial -- would add population "
                    "to the most evacuation-constrained part of the valley "
                    "(Arnold Dr time to 285 min if SDC built out)."
                ),
            },
            {
                "name": "Highway 12",
                "bearing": "N-S",
                "type": "access_route",
                "notes": (
                    "PRIMARY evacuation route running NW-SE through the valley. "
                    "2 lanes for most of its length through the valley. Connects "
                    "to Santa Rosa (NW) and Napa/Hwy 121 (SE). Intersections "
                    "gridlock during heavy traffic. Was closed with northbound "
                    "roadblock during Nuns Fire. SAFE Study: speeds drop to "
                    "1-2 mph for 2-3 hours during full evacuation. Carries ~60% "
                    "of valley evacuation traffic."
                ),
            },
            {
                "name": "Arnold Drive",
                "bearing": "N-S",
                "type": "access_route",
                "notes": (
                    "SECONDARY evacuation route, parallel to Hwy 12 but ~1 mi "
                    "west. Narrow 2-lane road through Glen Ellen, running from "
                    "Kenwood south to Hwy 121 near Schellville. 171 min "
                    "evacuation time under current conditions per SAFE Study. "
                    "No shoulders in many sections. Passes through residential "
                    "and vineyard areas. Critical for Glen Ellen residents since "
                    "Hwy 12 may be cut off by fire from the east."
                ),
            },
            {
                "name": "Sonoma Creek / watershed",
                "bearing": "N",
                "type": "water_supply",
                "notes": (
                    "Primary drainage through Sonoma Valley. Not a municipal "
                    "water supply (city uses Sonoma County Water Agency / Russian "
                    "River). However, Sonoma County Water Agency supplies come "
                    "from Lake Sonoma (83,000-acre watershed) which faces its "
                    "own fire risk from heavy fuel loading due to decades of "
                    "fire suppression and reduced grazing."
                ),
            },
        ],
        "historical_fires": [
            "Nuns Fire 2017 (56,000+ acres, 400+ homes, evacuations to edge of Sonoma town)",
            "Glass Fire 2020 (67,484 acres, 1,555 structures, eastern Mayacamas)",
            "Valley Fire 2015 (76,067 acres, 1,955 structures, nearby Lake County)",
        ],
        "wui_class": "high",
        "population": {
            "census_2020": 10739,
            "notes": (
                "Historic town with significant tourism population (wineries, "
                "Sonoma Plaza). Seasonal and weekend visitor surges add to "
                "evacuation demand. Many visitors unfamiliar with local roads "
                "and evacuation routes. Large vacation-rental population in "
                "surrounding hills."
            ),
        },
        "post_fire_changes": [
            "Sonoma County zone-based evacuation system adopted (replaces blanket orders)",
            "SoCo Alert notification system deployed",
            "SAFE Study (KLD Associates, Feb 2025) quantified evacuation bottlenecks",
            "Cavedale Fire Readiness Project (100-ft shaded fuel break, fire road reopening)",
            "Fire Safe Sonoma CWPP Hub Site with real-time risk data",
            "Sonoma Valley Fire District vegetation management projects active",
            "SDC redevelopment debate ongoing (evacuation capacity vs. housing)",
            "Community CERT/COPE programs expanded in valley",
        ],
    },

    # =========================================================================
    # SHASTA COUNTY / SACRAMENTO VALLEY -- Carr Fire
    # =========================================================================
    "redding_ca": {
        "center": (40.5865, -122.3917),
        "elevation_ft": 495,
        "terrain_notes": (
            "Sacramento Valley city (pop. 93,611 per 2020 census) at the "
            "northernmost extent of the Central Valley, where the valley floor "
            "meets the Klamath Mountains to the west and Cascade Range foothills "
            "to the north. The western city boundary directly abuts steep, "
            "forested terrain -- 40-70% slopes covered in chaparral, foothill "
            "pine, and mixed oak that transitions to dense mixed-conifer (Douglas "
            "fir, ponderosa) within 5 mi. The Sacramento River bisects the city "
            "N-S. Carr Fire (July 23 - Aug 30, 2018) ignited from trailer-wheel "
            "sparks on Hwy 299 near Whiskeytown NRA, 10 mi west of the city. "
            "Fire burned east through extremely steep, inaccessible terrain of "
            "decomposed granite soils with flashy fuels. On July 26, the fire "
            "exploded: a pyro-cumulonimbus (pyroCb) developed and a fire-"
            "generated vortex (FGV) formed along the NE fire flank at 7:30 PM "
            "with surface winds of 143 mph (EF3 tornado equivalent). The "
            "vortex -- reaching 18,000 ft in height and 2,700 deg F internal "
            "temp -- was on the ground for 30 minutes, uprooting trees, "
            "toppling transmission towers, and debarking trees in areas not "
            "even touched by flame. It killed 3 people directly. The fire then "
            "jumped the Sacramento River and burned into western Redding "
            "neighborhoods (Stanford Hills, Land Park, River Ridge, Mary Lake, "
            "Keswick). 38,000 people were evacuated overnight. 1,604 structures "
            "destroyed, 8 killed total. The fire consumed half of historic "
            "French Gulch and all but 2 structures in Keswick. Terrain-driven "
            "winds in the steep drainages west of the city (Brandy Creek, "
            "Boulder Creek, Whiskey Creek, Clear Creek) are unpredictable and "
            "shift rapidly. Soil burn severity was extreme: 41% moderate-to-high "
            "in Brandy Creek, 93% in Boulder Creek, 78% in Whiskey Creek "
            "watersheds. Post-fire debris flows and flooding risk in these "
            "basins. Redding averages 100+ wildland fires per year. Summer "
            "temperatures regularly exceed 105 deg F with single-digit humidity."
        ),
        "danger_quadrants": ["west", "northwest", "southwest", "north"],
        "safe_quadrants": ["east", "southeast"],
        "key_features": [
            {
                "name": "Whiskeytown NRA / Hwy 299 corridor",
                "bearing": "W",
                "distance_mi": 10,
                "type": "major_canyon",
                "notes": (
                    "Carr Fire origin area. Extremely steep terrain (40-70% "
                    "slopes) with decomposed granite soils and dense chaparral "
                    "transitioning to mixed conifer. Hwy 299 is the only E-W "
                    "road through this area, following Clear Creek canyon. Steep "
                    "basins (Brandy Creek, Boulder Creek, Whiskey Creek) drain "
                    "into Whiskeytown Lake with no sediment storage -- post-fire "
                    "debris flows are severe. Terrain is largely inaccessible to "
                    "ground crews and heavy equipment; suppression relies on air "
                    "attack and indirect methods. Hwy 299 is also a major "
                    "ignition corridor (vehicle sparks, equipment, roadside fires)."
                ),
            },
            {
                "name": "Sacramento River corridor",
                "bearing": "N-S through city",
                "distance_mi": 0,
                "type": "river_canyon",
                "notes": (
                    "River bisects Redding N-S. Carr Fire JUMPED the Sacramento "
                    "River on July 26, carried by the fire-generated vortex and "
                    "extreme wind-driven ember transport. River does NOT serve as "
                    "a reliable firebreak during extreme events. I-5 and the "
                    "railroad parallel the river. Lake Redding park/golf course "
                    "area burned after the river crossing. Bridges at "
                    "South Bonnyview, Hwy 44, Diestelhorst provide limited "
                    "cross-river evacuation options."
                ),
            },
            {
                "name": "Shasta-Trinity foothills / Klamath Mountains",
                "bearing": "NW",
                "distance_mi": 5,
                "type": "forest_wui",
                "notes": (
                    "Dense mixed-conifer forest on steep terrain transitioning "
                    "from oak woodland at 1,000 ft to Douglas fir/ponderosa at "
                    "2,500+ ft. Extreme fire behavior potential due to slope, "
                    "fuel loading, and channeling through drainages. This is the "
                    "primary fire threat vector for Redding's western and northern "
                    "neighborhoods. Fuel breaks planned: Hwy 44, West Redding, "
                    "and China Gulch fuel breaks (CAL FIRE priority projects)."
                ),
            },
            {
                "name": "Stanford Hills / Land Park / River Ridge",
                "bearing": "W",
                "distance_mi": 2,
                "type": "wui_neighborhood",
                "notes": (
                    "Western Redding neighborhoods directly impacted by Carr "
                    "Fire. Stanford Hills (gated community): ~50% of homes "
                    "burned. Land Park and River Ridge also lost hundreds of "
                    "homes. These neighborhoods are nestled into wooded hills "
                    "east of the Sacramento River -- classic WUI intermix with "
                    "oak canopy overhead and limited defensible space. First "
                    "Firewise USA community within Redding city limits being "
                    "established here (2025, ~18 households initial enrollment)."
                ),
            },
            {
                "name": "Keswick / French Gulch",
                "bearing": "W/NW",
                "distance_mi": 8,
                "type": "community",
                "notes": (
                    "Small historic communities west of Redding. Keswick: all "
                    "but 2 structures destroyed by Carr Fire. French Gulch "
                    "(historic gold mining town): half the town burned. Both "
                    "communities are on narrow mountain roads with single-lane "
                    "bridges and no alternate egress. Essentially indefensible "
                    "during wind-driven fire."
                ),
            },
            {
                "name": "Fire-generated vortex formation zone",
                "bearing": "W/NW",
                "distance_mi": 3,
                "type": "terrain_feature",
                "notes": (
                    "The Carr Fire vortex formed along the NE flank of the fire "
                    "in a region of pre-existing cyclonic wind shear where the "
                    "fire perimeter intersected steep terrain above the Sacramento "
                    "River. Radar data showed the convective plume grew from "
                    "6 km to 12 km in 15 min, releasing moist instability in a "
                    "pyroCb that stretched the underlying vorticity column to "
                    "the surface. This mechanism (pyrotornadogenesis) is distinct "
                    "from typical fire whirls and has dynamical similarities to "
                    "non-mesocyclonic tornadoes. The terrain configuration west "
                    "of the Sacramento River -- steep canyons converging at the "
                    "river valley -- may predispose this area to vortex formation "
                    "under extreme fire conditions. (Lareau et al. 2018, GRL)"
                ),
            },
            {
                "name": "Hwy 299 (west)",
                "bearing": "W",
                "type": "ignition_corridor",
                "notes": (
                    "Major E-W highway from coast through Whiskeytown to Redding. "
                    "Carr Fire started from vehicle sparks on 299. High vehicle "
                    "traffic through steep terrain with dry fuels. Multiple "
                    "historical ignitions along this corridor. Also serves as "
                    "critical evacuation route for communities west of Redding "
                    "(French Gulch, Lewiston), but can be cut off by fire."
                ),
            },
            {
                "name": "I-5 corridor",
                "bearing": "N-S",
                "type": "access_route",
                "notes": (
                    "Primary N-S evacuation route. 4-lane freeway through Redding "
                    "paralleling the Sacramento River. Adequate capacity for urban "
                    "Redding evacuation. 38,000 people evacuated via I-5 and Hwy "
                    "44 during Carr Fire. However, communities north (Shasta Lake "
                    "City, Lakehead) and south (Anderson, Cottonwood) may also "
                    "be evacuating simultaneously, straining capacity."
                ),
            },
            {
                "name": "Hwy 44 (east)",
                "bearing": "E",
                "type": "access_route",
                "notes": (
                    "E-W highway connecting Redding to Shingletown and Lassen. "
                    "Serves as primary eastbound evacuation route away from "
                    "western fire threats. Also threatened by fires from the "
                    "NE (Fawn Fire 2021 burned to Hwy 44). Fuel break planned "
                    "along Hwy 44 corridor (CAL FIRE priority project)."
                ),
            },
        ],
        "historical_fires": [
            "Carr Fire 2018 (8 killed, 1,604 structures, 229,651 acres, EF3 fire tornado, $1.7B damage)",
            "Zogg Fire 2020 (4 killed, 204 structures, 56,338 acres, PG&E caused)",
            "Fawn Fire 2021 (185 structures, arson, burned to Hwy 44)",
            "McKinney Fire 2022 (4 killed, 60,138 acres, nearby Siskiyou County)",
            "Park Fire 2024 (429,000+ acres, originated near Chico, smoke/ash impacts on Redding)",
        ],
        "wui_class": "extreme",
        "population": {
            "census_2020": 93611,
            "notes": (
                "Largest city in the far north Sacramento Valley. 100+ wildland "
                "fires annually in Shasta County. Summer heat regime: 40+ days "
                "above 100F, with occasional 115F+ events. Median household "
                "income $72,208. City operates its own electric utility (Redding "
                "Electric) separate from PG&E -- relevant for PSPS events."
            ),
        },
        "post_fire_changes": [
            "Hwy 44, West Redding, and China Gulch fuel breaks (CAL FIRE priority projects)",
            "City water treatment plant: 2 MW backup generator installed",
            "Portable generators purchased for pump stations",
            "AlertShasta notification system deployed",
            "First Firewise USA community within city limits (Stanford Hills area, 2025)",
            "Shasta County Fire Safe Council expanded fuel treatment programs",
            "CWPP updated with post-Carr fire risk data",
            "Erosion control program: $10M for Sacramento River watersheds above Keswick Dam",
            "Creek drainage clearing (fire debris) to reduce flood risk",
            "Redding Fire Dept community risk reduction division expanded",
        ],
    },
}
