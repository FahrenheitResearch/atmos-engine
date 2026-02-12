"""
California Fire-Vulnerable City Profiles
=========================================

Comprehensive terrain, evacuation, fire behavior, infrastructure, and demographic
data for 62 fire-vulnerable cities, towns, and community clusters across California.
Profiles are derived from NIST case studies, CAL FIRE incident reports, county
after-action reviews, CWPP documents, and post-fire infrastructure assessments.

Usage:
    from tools.agent_tools.data.california_profiles import (
        CA_TERRAIN_PROFILES,
        CA_IGNITION_SOURCES,
        CA_CLIMATOLOGY,
    )

Cities covered (62 entries across 13 regions):
    FEATHER RIVER CANYON / CAMP FIRE CORRIDOR:
        Paradise
        Magalia
        Paradise Satellite Communities
    SIERRA FOOTHILLS (GOLD COUNTRY):
        Grass Valley
        Nevada City
        Alta Sierra
        Colfax
        Foresthill
        Pollock Pines
        Georgetown
        Diamond Springs
    SONOMA / NAPA WINE COUNTRY:
        Santa Rosa
        Sonoma
        Angwin
        Calistoga
        Kenwood
        Glen Ellen
    LAKE COUNTY / MENDOCINO:
        Middletown
        Cobb
        Clearlake
        Lower Lake
        Ukiah Outskirts
        Willits
    FAR NORTHERN CA:
        Redding
        Weed
        Dunsmuir
        Weaverville
        Hayfork
    CENTRAL SIERRA / YOSEMITE GATEWAY:
        Mariposa
        Groveland
        Three Rivers
    SANTA CRUZ MOUNTAINS:
        Boulder Creek
        Ben Lomond
        Felton
        Bonny Doon
        San Lorenzo Valley Communities
    LA BASIN / SAN GABRIEL FOOTHILLS:
        Malibu
        Pacific Palisades
        Topanga
        Altadena
        Lanada Flintridge
    VENTURA / SANTA BARBARA COAST:
        Ojai
        Ventura
        Thousand Oaks
        Montecito
        Carpinteria
    SAN BERNARDINO MOUNTAINS:
        Lake Arrowhead
        Crestline
        Running Springs
        Big Bear Lake
        Forest Falls
        Wrightwood
    RIVERSIDE COUNTY MOUNTAINS:
        Idyllwild
        Mountain Center
    SAN DIEGO BACKCOUNTRY:
        Julian
        Ramona
        Alpine
        Valley Center
        Fallbrook
        Pine Valley
    TEHACHAPI / KERN MOUNTAINS:
        Frazier Park
        Pine Mountain Club

Sources:
    - NIST Technical Notes 2135, 2252 (Camp Fire case study & timeline)
    - Lareau et al. 2018 (GRL): Carr Fire pyrotornadogenesis
    - CAL FIRE incident reports (Camp, Tubbs, Nuns, Glass, Carr, Zogg, Fawn,
      Woolsey, Palisades, Eaton, Thomas, Cedar, Witch Creek, CZU, Rim, etc.)
    - Sonoma County AAR (June 2018): October 2017 Complex Fires
    - Sonoma County CWPP 2023 Update (Fire Safe Sonoma)
    - Paradise Irrigation District water quality reports (2019-2020)
    - Butte County Grand Jury 2008 evacuation findings
    - NWS Sacramento post-event summaries (Jarbo Gap wind events)
    - San Diego County post-fire analyses (2003, 2007)
    - Santa Cruz County CZU Lightning Complex AAR
    - Lake County Valley Fire AAR (2015)
    - NOAA/NWS ISD normals, IEM ASOS archive, WRCC climate summaries
"""

# =============================================================================
# TERRAIN PROFILES -- 62 entries organized by 13 regions
# =============================================================================

CA_TERRAIN_PROFILES = {

    # =========================================================================
    # FEATHER RIVER CANYON / CAMP FIRE CORRIDOR
    # =========================================================================

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
    # 7. PARADISE SATELLITE COMMUNITIES -- Feather River Canyon Fire Corridor
    #    Concow, Berry Creek, Stirling City, Yankee Hill
    # =========================================================================
    "paradise_satellite_communities": {
        "center": [39.73, -121.49],
        "terrain_notes": (
            "Cluster of four tiny, remote communities in the Feather River Canyon "
            "fire corridor of Butte County, all within 15 miles of Paradise and all "
            "devastated by the 2018 Camp Fire and/or the 2020 North Complex (Bear) "
            "Fire. These communities share extreme vulnerability: minimal population, "
            "single-road access via narrow winding mountain roads, heavy fuel loading "
            "in continuous mixed conifer and oak woodland, and direct exposure to the "
            "Jarbo Gap NE foehn wind regime that drives the most destructive fires in "
            "this corridor. Combined population ~2,000-2,500 (pre-fire; significantly "
            "reduced post-fire). These communities are rebuilding slowly with minimal "
            "resources -- the Bear Fire survivors notably received far less rebuild "
            "assistance than Camp Fire survivors in Paradise despite similar devastation."
        ),
        "key_features": [
            "Four communities in Feather River Canyon fire corridor: Concow, Berry Creek, Stirling City, Yankee Hill",
            "All devastated by Camp Fire (2018) and/or North Complex/Bear Fire (2020)",
            "Combined pre-fire population ~2,500; significantly reduced post-fire",
            "Jarbo Gap NE foehn wind regime -- most destructive fire weather in NorCal",
            "Single-road access for each community via narrow, winding mountain roads",
            "Berry Creek: 14 of 16 North Complex Fire fatalities were Berry Creek residents",
            "Concow: 95% of structures destroyed in first 6 hours of Camp Fire",
            "Yankee Hill: devastated by both Camp Fire (2018) and Bear Fire (2020)",
            "Stirling City: sawmill siren installed as evacuation warning system",
            "Slow rebuild: Berry Creek survivors lack rebuild resources compared to Paradise",
            "Park Fire (2024, 429,000+ acres) again threatened Stirling City and upper corridor",
        ],
        "sub_profiles": {
            "concow": {
                "center": [39.7302, -121.5266],
                "elevation_ft": 1759,
                "population_2020": 402,
                "population_pre_fire": 710,
                "terrain_notes": (
                    "Unincorporated community in a bowl-shaped valley surrounding "
                    "Concow Reservoir (PG&E), at ~1,759 ft elevation. Located 5 miles "
                    "NW of Paradise on the same narrow ridge system. Access via Concow "
                    "Road -- narrow, winding, no shoulders. During the 2018 Camp Fire, "
                    "Concow was reached by fire within ~1 hour of ignition (by 07:30) "
                    "and lost ~95% of structures. Four residents killed. The community "
                    "is a sentinel for Paradise: if Concow is burning, Paradise has "
                    "30-60 minutes before fire arrival during Jarbo wind events. "
                    "The 2020 Census counted only 402 people (305 households), a 43% "
                    "decline from 710 in 2010. Was also evacuated during the 2020 "
                    "North Complex/Bear Fire. Rebuilding has been extremely slow."
                ),
                "access_roads": [
                    "Concow Road (2-lane, narrow, winding, no shoulders -- only paved route)",
                    "Hoffman Road (narrow connecting road to Yankee Hill area)",
                ],
                "historical_fires": [
                    "Camp Fire 2018 (95% of structures destroyed in first 6 hours, 4 killed)",
                    "North Complex / Bear Fire 2020 (second evacuation in 2 years)",
                    "Park Fire 2024 (evacuation orders issued for Concow area)",
                ],
            },
            "berry_creek": {
                "center": [39.6652, -121.4250],
                "elevation_ft": 2000,
                "population_2020": 1637,
                "population_pre_fire": 1200,
                "terrain_notes": (
                    "Census-designated place 25 miles NE of Oroville at ~2,000 ft "
                    "elevation, in hilly terrain on the western slope of the Sierra "
                    "Nevada. On September 9, 2020, the Bear Fire (North Complex West "
                    "Zone) reached Berry Creek at 10 PM with virtually no warning -- "
                    "evacuation orders were issued at 3:15 PM the same day with no "
                    "prior warning. The fire destroyed nearly the entire town, leaving "
                    "only 3 houses standing. 14 of the 16 North Complex Fire fatalities "
                    "were Berry Creek residents. The community has been described as "
                    "'leveled by a wall of fire.' Three years post-fire, rebuilding "
                    "efforts remain slow, with survivors lacking the rebuild resources "
                    "that other fire communities (like Paradise) received. The 2020 "
                    "Census population figure of 1,637 was recorded before the Bear Fire."
                ),
                "access_roads": [
                    "Bald Rock Road / Oroville-Quincy Highway (2-lane, winding, 25 mi to Oroville)",
                    "Forbestown Road (narrow mountain road connecting to Forbestown/Clipper Mills)",
                ],
                "historical_fires": [
                    "North Complex / Bear Fire 2020 (town nearly 100% destroyed, 14 killed, 2,352 structures across complex)",
                ],
            },
            "stirling_city": {
                "center": [39.9077, -121.5280],
                "elevation_ft": 3570,
                "population_2020": 284,
                "population_pre_fire": 300,
                "terrain_notes": (
                    "Tiny unincorporated community (pop. 284, 2020 census) at 3,570 ft "
                    "elevation, 32 miles NE of Chico, nestled in timberland in the "
                    "Sierra Nevada foothills. The community is surrounded by dense "
                    "conifer forest and was historically a lumber mill town. Access is "
                    "via Skyway northbound from Paradise/Magalia -- the same road that "
                    "serves as Paradise's primary evacuation route, creating a cascading "
                    "vulnerability where Stirling City's evacuation depends on the "
                    "road through communities that may already be on fire. The "
                    "community installed a sawmill siren on the volunteer fire station "
                    "roof as a wildfire evacuation warning system after the 2018 Camp "
                    "Fire demonstrated the inadequacy of cell/internet-based "
                    "notification in remote mountain communities. Threatened by Camp "
                    "Fire (2018), evacuated during Park Fire (2024, 429,000+ acres). "
                    "At 3,570 ft, Stirling City is in the dense montane conifer zone "
                    "with extremely heavy fuel loads."
                ),
                "access_roads": [
                    "Skyway (SR 191) north from Paradise/Magalia (2-lane, narrow, winding mountain road)",
                    "Inskip Road (narrow connecting road to Inskip and surrounding forest)",
                ],
                "historical_fires": [
                    "Camp Fire 2018 (evacuation orders issued, fire threatened community)",
                    "Park Fire 2024 (evacuation warnings issued, 429,000+ acres)",
                ],
            },
            "yankee_hill": {
                "center": [39.73, -121.48],
                "elevation_ft": 1982,
                "population_2020": 260,
                "population_pre_fire": 800,
                "terrain_notes": (
                    "Unincorporated community (pop. 260, 2020 census; ~800 pre-fire) "
                    "at ~1,982 ft elevation, 6.5 miles ESE of Paradise. Devastated "
                    "by BOTH the 2018 Camp Fire AND the 2020 North Complex/Bear Fire, "
                    "making it one of only a handful of American communities to be "
                    "largely destroyed by two separate wildfires in a 2-year period. "
                    "The community lost its Grange Hall (main community center) in "
                    "2018 and it is not being rebuilt. Current development is primarily "
                    "re-development as the community slowly recovers. The Yankee Hill "
                    "Fire Safe Council annex to the 2024 Butte County Local Hazard "
                    "Mitigation Plan documents the ongoing vulnerability. Population "
                    "in 2023 estimated at 384 with a median age of 53.5, indicating "
                    "an aging population rebuilding in place. Access is via narrow "
                    "connecting roads to Concow and Paradise -- same road network that "
                    "proved inadequate during Camp Fire."
                ),
                "access_roads": [
                    "Yankee Hill Road / connecting roads to Concow Road (narrow, winding)",
                    "Routes through Paradise to Skyway (dependent on Paradise being passable)",
                ],
                "historical_fires": [
                    "Camp Fire 2018 (community largely destroyed along with Paradise/Concow)",
                    "North Complex / Bear Fire 2020 (second destruction in 2 years)",
                ],
            },
        },
        "elevation_range_ft": [1600, 3600],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Camp Fire",
                "year": 2018,
                "acres": 153336,
                "details": (
                    "Deadliest and most destructive wildfire in California history. "
                    "85 fatalities, 18,804 structures destroyed, 153,336 acres. "
                    "Ignited on PG&E's Caribou-Palermo 115kV line near Pulga. "
                    "Destroyed Paradise, Concow, and Yankee Hill within 6 hours. "
                    "Driven by NE Jarbo Gap foehn winds sustained 35-45 mph with "
                    "gusts to 50+. Ember spotting documented up to 6.3 km ahead of "
                    "fire front. 27,000 people evacuated simultaneously; trips "
                    "normally 25 min took 3-4 hours. 19 documented burnovers on roads."
                ),
            },
            {
                "name": "North Complex / Bear Fire",
                "year": 2020,
                "acres": 318935,
                "details": (
                    "North Complex Fire complex (318,935 acres total) including the "
                    "Bear Fire component that devastated Berry Creek, Feather Falls, "
                    "and areas near Concow and Yankee Hill. 16 fatalities (14 in "
                    "Berry Creek, 2 in Feather Falls). 2,352 structures destroyed. "
                    "Berry Creek was destroyed with virtually no warning -- evacuation "
                    "orders issued same day fire arrived, 'wall of fire' reached town "
                    "at 10 PM on Sep 9, 2020. Only 3 houses left standing in Berry "
                    "Creek. Survivors received far less rebuild assistance than Camp "
                    "Fire survivors."
                ),
            },
            {
                "name": "Park Fire",
                "year": 2024,
                "acres": 429000,
                "details": (
                    "California's 5th largest wildfire in recorded history. 429,000+ "
                    "acres in Butte and Tehama counties. Evacuation orders/warnings "
                    "issued for Concow, Stirling City, Magalia, and Paradise areas. "
                    "Arson-caused. At least 209 homes destroyed. Demonstrated that "
                    "the Feather River Canyon corridor remains under persistent, "
                    "recurring mega-fire threat."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Concow Road to Paradise / Skyway (Concow, Yankee Hill)",
                "direction": "S/SW",
                "lanes": 2,
                "bottleneck": (
                    "Narrow, winding, no shoulders. Must transit through Paradise "
                    "to reach Skyway and ultimately Chico. If Paradise is on fire "
                    "(as in 2018), this route is a death trap. During Camp Fire, "
                    "most Concow residents could not evacuate before fire arrived."
                ),
                "risk": (
                    "Extreme. Dependent on Paradise being passable. Single route "
                    "for Concow and Yankee Hill. 23 life-threatening entrapment "
                    "events documented during Camp Fire, 17 involving civilians "
                    "on evacuation roads."
                ),
            },
            {
                "route": "Bald Rock Road / Oroville-Quincy Hwy to Oroville (Berry Creek)",
                "direction": "SW",
                "lanes": 2,
                "bottleneck": (
                    "25-mile, 2-lane winding mountain road from Berry Creek to "
                    "Oroville. Only paved route out. Passes through heavily "
                    "forested terrain and descends steeply to the Sacramento Valley. "
                    "During Bear Fire, evacuation orders came with no prior warning "
                    "on the same day fire destroyed the town."
                ),
                "risk": (
                    "Extreme. Single route for ~1,200 residents. 25 miles of narrow "
                    "mountain road through fire-prone forest. Zero-warning evacuation "
                    "demonstrated in 2020."
                ),
            },
            {
                "route": "Skyway north from Paradise/Magalia (Stirling City)",
                "direction": "N",
                "lanes": 2,
                "bottleneck": (
                    "2-lane mountain road extending Skyway northward from Magalia. "
                    "Narrow, winding, passes through dense forest. A 185-ft section "
                    "was narrowed to only 11.5 ft wide (single lane) from 2022-23 "
                    "winter storm damage -- creating severe bottleneck for both "
                    "evacuation and fire apparatus access. FEMA repair funded but "
                    "not yet completed as of early 2025."
                ),
                "risk": (
                    "Extreme. Stirling City's evacuation route runs THROUGH "
                    "Paradise and Magalia, both of which are known to be in the "
                    "direct fire path during Jarbo wind events. If fire is "
                    "approaching from the NE, Stirling City residents must drive "
                    "south toward and through the fire to escape."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "NE Jarbo Gap foehn winds. Katabatic foehn events where dry Great "
                "Basin air descends the western Sierra slope, funneling through "
                "Jarbo Gap -- a topographic constriction where the Feather River "
                "Canyon narrows between Jarbo Gap Ridge and Table Mountain. Venturi "
                "effect accelerates winds to 50-70 mph. These events drive the "
                "most catastrophic fires in the corridor: Camp Fire (2018) spread "
                "at 1 m/s (~2.2 mph / 180 chains/hr) through wildland fuels. When "
                "winds align NE-to-SW through Jarbo Gap, the entire Feather River "
                "Canyon becomes a blowtorch aimed at Paradise and its satellite "
                "communities."
            ),
            "critical_corridors": [
                "Feather River Canyon (NE-SW -- primary fire corridor for Camp Fire, Park Fire)",
                "West Branch Feather River (N-S -- parallel canyon channeling wind and fire)",
                "Concow valley bowl (trapped topography creating extreme fire behavior)",
                "Berry Creek / Bald Rock drainage (N-S -- Bear Fire spread corridor)",
                "Butte Creek Canyon (E -- parallel to Paradise ridge, ember receptor)",
            ],
            "rate_of_spread_potential": (
                "Extreme. Camp Fire: 1 m/s (180 chains/hr) sustained through wildland "
                "fuels during Jarbo wind event. Within communities, fire spread could "
                "not be computed due to simultaneous spotting from hundreds of ignition "
                "points. Bear Fire: 8-mile-long flank swept through Berry Creek in "
                "hours. Park Fire: grew to 429,000+ acres, one of the fastest-growing "
                "fires in CA history. These are among the highest fire spread rates "
                "documented in North American wildfire history."
            ),
            "spotting_distance": (
                "Up to 6.3 km (3.9 miles) documented during Camp Fire per NIST study. "
                "Softball-sized embers lofted over the Paradise/Magalia ridge and into "
                "Butte Creek Canyon during Camp Fire. During Bear Fire, ember transport "
                "distances of 1-3 miles were observed ahead of the fire front."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Varied by sub-community. Concow: PG&E's Concow Reservoir provides "
                "limited water but no fire suppression capacity. Berry Creek: rural "
                "well systems, no municipal water. Stirling City: small community "
                "water system. Yankee Hill: rural wells. None of these communities "
                "have water infrastructure adequate for wildfire suppression."
            ),
            "power": (
                "PG&E overhead distribution through dense forest. Camp Fire was "
                "ignited by failure of PG&E's Caribou-Palermo 115kV transmission "
                "line -- the very infrastructure that powered these communities. "
                "That line has been permanently de-energized. Remaining distribution "
                "lines are subject to PSPS de-energization. Extended outages during "
                "fire weather are routine."
            ),
            "communications": (
                "Minimal to none. Cell coverage is spotty to nonexistent in canyon "
                "and mountain areas. 17 cell towers destroyed during Camp Fire. "
                "Stirling City installed a sawmill siren as a backup notification "
                "system because cell/internet-based alerts are unreliable. Berry "
                "Creek received evacuation orders on the same day fire destroyed "
                "the town -- notification came too late."
            ),
            "medical": (
                "No medical facilities in any of these communities. Nearest hospital "
                "is Enloe Medical Center in Chico (30-50 miles depending on community) "
                "or Oroville Hospital (25 miles from Berry Creek). During fire events, "
                "road access to hospitals may be cut off. Aging populations with "
                "medical needs in all four communities."
            ),
        },
        "demographics_risk_factors": {
            "population": 2500,
            "seasonal_variation": (
                "Minimal seasonal variation. These are primarily permanent-resident "
                "communities with little tourism infrastructure. Population has "
                "declined post-fire in all four communities."
            ),
            "elderly_percentage": "~25-30% age 65+ (estimated, skews older post-fire as younger residents relocate)",
            "mobile_homes": (
                "Significant mobile home presence in all four communities, "
                "especially Concow and Yankee Hill. Post-fire rebuilding has "
                "included mobile/manufactured homes as the most affordable option. "
                "These structures are extremely vulnerable to the ember attack "
                "fire regime documented during Camp Fire."
            ),
            "special_needs_facilities": (
                "None. No senior care, assisted living, medical clinics, or "
                "special needs facilities in any of the four communities. "
                "Yankee Hill lost its only community center (Grange Hall) in "
                "2018 and it is not being rebuilt. Residents with special needs "
                "are entirely dependent on private resources and neighborly "
                "assistance during emergencies."
            ),
        },
    },

    # =========================================================================
    # SIERRA FOOTHILLS (GOLD COUNTRY)
    # =========================================================================

    "grass_valley_ca": {
        "center": (39.2193, -121.0610),
        "elevation_ft": 2411,
        "terrain_notes": (
            "Sierra foothills city (pop 14,016, 2020 census) in Nevada County "
            "at 2,411 ft elevation. Widely considered one of the most vulnerable "
            "communities in California — same topographic profile as Paradise "
            "(ridge-top settlement above deep canyons with limited escape routes). "
            "63% of incorporated area classified as WUI. Dense mixed pine/oak "
            "forest with decades of fire-suppression-driven fuel accumulation: "
            "heavy ladder fuels, dense understory, continuous canopy throughout "
            "residential areas. Underlying geology is granitic (quartz diorite "
            "under downtown core) with metavolcanic rock and diabase on margins; "
            "ultramafic soils near Nevada County Golf Course support sparser "
            "vegetation but surrounding areas are heavily forested. "
            "\n\n"
            "The city is bracketed by three major canyon systems: South Yuba "
            "River Canyon (north, 5 mi), Bear River drainage (south, 3 mi), "
            "and Wolf Creek (east, running directly through WUI). Any fire "
            "entering these canyons gains rapid upslope momentum toward "
            "populated ridges. The 49er Fire (1988) proved this conclusively: "
            "ignited by a man burning toilet paper near Hwy 49, it destroyed "
            "312 structures (144 homes, 219 outbuildings, 89 vehicles, 17 "
            "boats/trailers) across 33,700 acres in 5 days, driven by severe "
            "drought and strong dry winds. Estimated damage: $22.7 million "
            "(1988 dollars). Fire impinged on Lake Wildwood, Rough and Ready, "
            "and Smartsville. Jones Fire (2020) burned 712 acres in South "
            "Yuba River Canyon after lightning ignition, forcing evacuation "
            "of 4,000 residents with 11,600 more under warnings. Highway 49 "
            "was closed between Newtown and Tyler Foote during the incident. "
            "\n\n"
            "Caltrans has recognized the evacuation crisis: the $107.4 million "
            "SR-49 Grass Valley Wildfire Evacuation Route Project (SB 1 funds "
            "plus Nevada County Transportation Commission) will widen shoulders "
            "and add a center two-way left-turn lane from Wolf Road/Combie Road "
            "to Ponderosa Pines Way. Construction anticipated fall 2027 through "
            "end of 2030 — meaning the community remains highly vulnerable for "
            "at least several more fire seasons."
        ),
        "population": {
            "total_2020_census": 14016,
            "density_per_sq_mi": 2670,
            "median_age": None,
            "note": (
                "Population has grown significantly in recent decades. "
                "42.6% single-person households; 25.5% single-person "
                "aged 65+, creating evacuation vulnerability for elderly "
                "living alone."
            ),
        },
        "danger_quadrants": ["north", "northeast", "east", "southeast"],
        "safe_quadrants": ["west"],
        "key_features": [
            {
                "name": "South Yuba River Canyon",
                "bearing": "N/NE",
                "distance_mi": 5,
                "type": "major_canyon",
                "notes": (
                    "Deep, heavily forested canyon — the primary fire corridor "
                    "threatening Grass Valley and Nevada City from the north. "
                    "Jones Fire (2020) burned 712 acres here, ignited by "
                    "lightning. Heavy recreational use (swimming holes, hiking, "
                    "camping) creates ignition risk in summer. Sierra Nevada "
                    "Conservancy prescribed burn projects ongoing to reduce "
                    "fuel loads in the canyon. Steep slopes with dense "
                    "understory channel fire uphill toward populated ridges."
                ),
            },
            {
                "name": "Bear River drainage",
                "bearing": "S",
                "distance_mi": 3,
                "type": "river_valley",
                "notes": (
                    "Canyon terrain to south of city. Combined with South "
                    "Yuba Canyon to the north, Grass Valley sits on a ridge "
                    "between two major drainages — the same topographic "
                    "configuration that made Paradise so vulnerable. Fire "
                    "approaching from either canyon gains upslope acceleration."
                ),
            },
            {
                "name": "Wolf Creek",
                "bearing": "E",
                "distance_mi": 2,
                "type": "canyon",
                "notes": (
                    "Local canyon running directly through the WUI. The SR-49 "
                    "evacuation improvement project begins at the Wolf Road/"
                    "Combie Road intersection specifically because fire entering "
                    "Wolf Creek could cut off eastbound evacuation. Dense "
                    "residential development along canyon margins."
                ),
            },
            {
                "name": "SR-49 corridor",
                "bearing": "N-S",
                "type": "access_route",
                "notes": (
                    "Primary evacuation route — narrow, winding 2-lane highway "
                    "through Gold Country. Closed during Jones Fire 2020. "
                    "Caltrans $107.4M widening project (2027-2030) will add "
                    "shoulders and center turn lane from Wolf/Combie to Ponderosa "
                    "Pines Way. Until then, severe bottleneck during mass "
                    "evacuation. Connects to Nevada City (4 mi north) creating "
                    "combined evacuation demand of ~17,000+ people on same roads."
                ),
            },
            {
                "name": "SR-20 corridor",
                "bearing": "E-W",
                "type": "access_route",
                "notes": (
                    "East-west escape route, also narrow 2-lane mountain road. "
                    "Provides alternate evacuation toward I-80 (east) or Penn "
                    "Valley/Marysville (west). Limited capacity. During mass "
                    "evacuation both SR-49 and SR-20 would carry combined "
                    "traffic from Grass Valley and Nevada City."
                ),
            },
        ],
        "evacuation": {
            "primary_routes": ["SR-49 south to Auburn/I-80", "SR-20 west to Penn Valley"],
            "secondary_routes": ["SR-49 north toward Downieville", "SR-20 east to I-80 via Emigrant Gap"],
            "bottlenecks": [
                "SR-49/SR-20 intersection in town",
                "Wolf Road/Combie Road intersection",
                "Narrow shoulders prevent pullover for emergency vehicles",
            ],
            "capacity_notes": (
                "Combined Grass Valley + Nevada City evacuation demand: ~17,000+ "
                "people on 2-lane roads. During Jones Fire 2020, 4,000 evacuated "
                "with 11,600 under warning. Evacuation centers established at "
                "Magnolia School (22431 Kingston Lane), Cottage Hill Elementary, "
                "Ready Springs School (Penn Valley), Nevada County Fairgrounds "
                "(animals). Full-community evacuation would overwhelm road "
                "capacity within minutes."
            ),
            "caltrans_project": (
                "SR-49 Grass Valley Wildfire Evacuation Route Project: $107.4M "
                "(SB 1 + NCTC funds). Widen shoulders, add center TWLTL from "
                "Wolf/Combie to Ponderosa Pines Way. Construction: fall 2027 "
                "to end 2030. Draft environmental document published Jan 2026."
            ),
        },
        "infrastructure": {
            "utility": "PG&E",
            "psps_exposure": "EXTREME",
            "psps_notes": (
                "Nevada County is one of the most PSPS-impacted counties in "
                "California. A single event can affect 43,000+ PG&E customers "
                "countywide. PSPS criteria: RH below 20%, sustained winds >25 "
                "mph, gusts >45 mph, Red Flag Warning, dry fuels. Shutoffs "
                "create secondary hazards: residents use generators (fire risk) "
                "and warming fires. In one 2019 event a generator caused a "
                "brush fire during a PSPS shutoff. Access and Functional Needs "
                "populations lose medication refrigeration, life-sustaining "
                "device charging, dialysis access. Community Resource Centers "
                "activated at 400 Idaho Maryland Rd for charging, ice, WiFi."
            ),
            "water_system": "NID (Nevada Irrigation District) municipal supply",
            "cell_coverage": (
                "87.6% land area covered by wireless service but canyon terrain "
                "creates dead zones. Poor cellular coverage documented as "
                "dangerous for emergency alerts — residents in canyons may "
                "miss evacuation orders. Nevada County OES identified "
                "communication gaps as critical vulnerability."
            ),
        },
        "community_preparedness": {
            "cwpp": (
                "2025 Nevada County CWPP adopted by Board of Supervisors Feb "
                "2025 after 2+ years of planning. Includes City of Grass "
                "Valley annex with place-based solutions for fuels reduction."
            ),
            "firewise": (
                "Fire Safe Council of Nevada County coordinates 107 Firewise "
                "USA communities countywide (as of Jan 2025). Western Nevada "
                "County Firewise coordinator covers Grass Valley, Nevada City, "
                "Penn Valley, South County, North San Juan, Hwy 174 corridor."
            ),
            "fuel_reduction": (
                "CAL FIRE planning 1,802-acre fire break in SW Nevada County "
                "in terrain that hasn't burned in a century, protecting both "
                "Grass Valley and Nevada City. Prescribed burn programs in "
                "South Yuba Canyon ongoing through Sierra Nevada Conservancy."
            ),
        },
        "historical_fires": [
            "49er Fire 1988 (312 structures, 144 homes, 33,700 acres, $22.7M damage, "
            "caused by burning toilet paper near Hwy 49, driven by drought/wind)",
            "Jones Fire 2020 (712 acres, South Yuba Canyon, lightning ignition, "
            "4,000 evacuated, 11,600 warned, Hwy 49 closed, 4 homes destroyed)",
            "River Fire 2021 (2,619 acres, nearby Colfax area, Bear River corridor)",
        ],
        "wui_class": "extreme",
        "compound_hazards": [
            "PG&E infrastructure failure (same aging lines that caused Camp Fire)",
            "PSPS shutoffs create secondary ignition risk from generators",
            "Combined evacuation demand with Nevada City on shared roads",
            "Diablo wind events (same pattern that drives Butte County fires)",
            "Terrain trap: ridge between two deep canyons mirrors Paradise geometry",
        ],
    },

    "nevada_city_ca": {
        "center": (39.2615, -121.0164),
        "elevation_ft": 2525,
        "terrain_notes": (
            "Historic Gold Rush city (pop 3,152, 2020 census; median age 49.4) "
            "at 2,525 ft in Nevada County, 4 miles northeast of Grass Valley. "
            "Nevada City is arguably the most fire-vulnerable historic district "
            "in California: the downtown core is a National Register Historic "
            "District (16 acres, 70 contributing buildings, listed 1985) with "
            "dense wooden Gold Rush-era structures, narrow steep streets, and "
            "heavy urban tree canopy pressed directly against commercial and "
            "residential buildings. The city has been destroyed by fire "
            "repeatedly in its history: the first great fire leveled the town "
            "in March 1851, and the worst catastrophe struck July 19, 1856, "
            "destroying 400+ buildings including the new courthouse and all "
            "county records, killing 10 people. By 1859, the city had been "
            "rebuilt and releveled by fire four additional times. Fire companies "
            "were finally formed in 1860 and two firehouses built by 1861. "
            "\n\n"
            "The National Exchange Hotel on Broad Street — the oldest "
            "continuously-operated hotel in California — was built in three "
            "brick buildings and opened August 1856 immediately after the "
            "great fire. In less than a month after the 1856 fire, 65 new "
            "frame buildings were erected and a half-dozen brick ones begun. "
            "Many of these 1850s-era wooden structures remain standing today, "
            "creating a downtown that looks authentic but is catastrophically "
            "vulnerable to fire. "
            "\n\n"
            "Modern wildfire risk comes from the surrounding terrain: dense "
            "forest presses against the city on all sides. Deer Creek runs "
            "through/near town creating a local fire corridor. South Yuba "
            "River Canyon is 3 miles north. Steep hillsides, narrow "
            "residential streets, ancient wooden homes, and thick urban tree "
            "canopy make this a textbook WUI ignition scenario. The "
            "Washington Post (2018) described the community as 'living under "
            "a time bomb.' Nevada City ran a 'Goat Fund Me' campaign raising "
            "$25,000 to hire goat farmers to graze brush on 450+ acres of "
            "city-owned greenbelt — creative but indicative of the scale of "
            "the fuel problem."
        ),
        "population": {
            "total_2020_census": 3152,
            "median_age": 49.4,
            "note": (
                "Small population but very high tourist traffic. Broad Street "
                "draws visitors year-round. Combined with Grass Valley (14,016) "
                "total evacuation demand on shared road network is ~17,000+."
            ),
        },
        "danger_quadrants": ["north", "northeast", "east", "south"],
        "safe_quadrants": ["west", "southwest"],
        "key_features": [
            {
                "name": "South Yuba River Canyon",
                "bearing": "N",
                "distance_mi": 3,
                "type": "major_canyon",
                "notes": (
                    "Primary fire corridor from the north. Terrain hasn't burned "
                    "in a century in some areas (CAL FIRE 1,802-acre fire break "
                    "planned for SW Nevada County). Jones Fire 2020 burned 712 "
                    "acres in this canyon. Prescribed burns ongoing through "
                    "Sierra Nevada Conservancy. Deep canyon with heavy recreational "
                    "use — swimming holes, hiking trails — creating summer "
                    "ignition risk."
                ),
            },
            {
                "name": "Deer Creek drainage",
                "bearing": "S",
                "distance_mi": 1,
                "type": "canyon",
                "notes": (
                    "Runs through/near town, creating a local fire corridor "
                    "that could carry fire directly into the city. Riparian "
                    "vegetation along creek is surrounded by residential "
                    "development. Fire in Deer Creek drainage could reach "
                    "downtown within minutes given upslope terrain."
                ),
            },
            {
                "name": "Historic Downtown (Broad Street)",
                "bearing": "center",
                "type": "structure_vulnerability",
                "notes": (
                    "National Register Historic District: 16 acres, 70 "
                    "contributing buildings (NR #85002520, listed 1985). "
                    "Dense wooden buildings from 1850s-1880s, many with "
                    "roofed balconies, verandas, and shed canopies. The "
                    "National Exchange Hotel (1856), Firehouse No. 1, and "
                    "numerous wood-frame commercial buildings. Narrow streets "
                    "with continuous fuel connections between structures. "
                    "One ember shower on downtown could recreate the 1856 "
                    "conflagration."
                ),
            },
            {
                "name": "SR-49 / SR-20 corridors",
                "bearing": "multiple",
                "type": "access_route",
                "notes": (
                    "Both routes are narrow 2-lane mountain roads with limited "
                    "capacity. SR-49 runs through downtown on narrow historic "
                    "streets. During mass evacuation, Nevada City traffic merges "
                    "with Grass Valley traffic on same roads. Jones Fire 2020 "
                    "closed SR-49. No 4-lane evacuation route exists. Community "
                    "is functionally a dead-end if fire cuts SR-49 to the south "
                    "and SR-20 to the west simultaneously."
                ),
            },
        ],
        "evacuation": {
            "primary_routes": ["SR-49 south through Grass Valley to Auburn/I-80"],
            "secondary_routes": ["SR-20 west to Penn Valley", "SR-49 north (limited)"],
            "critical_vulnerability": (
                "Nevada City sits upstream of Grass Valley on the road network. "
                "During evacuation, Nevada City traffic must flow THROUGH or "
                "around Grass Valley to reach I-80. If Grass Valley is also "
                "evacuating simultaneously, the combined 17,000+ people on "
                "2-lane roads creates an extremely dangerous scenario similar "
                "to the Camp Fire gridlock on Skyway in Paradise."
            ),
        },
        "infrastructure": {
            "utility": "PG&E",
            "psps_exposure": "EXTREME",
            "psps_notes": (
                "Same PG&E PSPS impacts as Grass Valley. 43,000+ customers "
                "affected countywide during events. Aging PG&E infrastructure "
                "throughout forested terrain. City sent formal letter of "
                "concern to CPUC (jointly with Grass Valley and Nevada County) "
                "detailing PSPS impacts on the community."
            ),
            "cell_coverage": (
                "Canyon topography creates significant dead zones. The Union "
                "(local newspaper) reported that poor cellular coverage is "
                "'not just inconvenient, it's dangerous' — residents in rural "
                "areas may miss evacuation alerts or be unable to make 911 "
                "calls. Nevada County OES identified communication gaps as "
                "critical emergency management vulnerability."
            ),
        },
        "community_preparedness": {
            "cwpp": (
                "2025 Nevada County CWPP includes City of Nevada City annex. "
                "Nevada City CWPP also available on city website. Focus on "
                "hazardous fuel reduction and community preparedness."
            ),
            "firewise": (
                "Part of Fire Safe Council of Nevada County's 107-community "
                "Firewise USA network. Nevada City Wildfire Preparedness "
                "program through city government."
            ),
            "creative_programs": (
                "Goat Fund Me campaign raised $25,000 to hire goat farmers "
                "to graze brush on 450+ acres of city-owned greenbelt. "
                "Creative approach but illustrates the massive scale of the "
                "fuel management challenge."
            ),
        },
        "historical_fires": [
            "1851 great fire (first major fire, leveled the town)",
            "1856 catastrophe (July 19 — 400+ buildings destroyed, courthouse + all "
            "county records lost, 10 killed; rebuilt within a month: 65 frame + 6 brick)",
            "1856-1859 (four additional fires leveled the city; fire companies formed 1860)",
            "49er Fire 1988 (33,700 acres, 312 structures, burned through western Nevada County, "
            "caused by burning toilet paper near Hwy 49)",
            "Jones Fire 2020 (712 acres, South Yuba Canyon, lightning ignition, "
            "SR-49 closed, 4,000 evacuated)",
        ],
        "wui_class": "extreme",
        "compound_hazards": [
            "Historic wooden downtown: one ember shower could destroy irreplaceable "
            "Gold Rush-era structures (National Register district, 70 buildings)",
            "Dead-end road geometry: must evacuate through Grass Valley",
            "PG&E infrastructure failure risk (same aging system as Camp Fire cause)",
            "Diablo wind events accelerate fires from east/northeast",
            "Terrain-channeled fire from Deer Creek or South Yuba Canyon",
            "Tourist traffic inflates road demand beyond resident population",
        ],
    },

    # =========================================================================
    # 1. ALTA SIERRA, CA -- PRIORITY TARGET
    #    "One of the most likely to burn down" per fire weather meteorologists
    # =========================================================================
    "alta_sierra_ca": {
        "center": [39.1416, -121.0538],
        "terrain_notes": (
            "Census-designated place (pop. 7,204, 2020 census) on a forested ridge "
            "between the Bear River drainage to the south and Greenhorn Creek to the "
            "north/east, in western Nevada County. Elevation averages ~2,300 ft with "
            "the ridge crest near 2,500 ft, dropping 400-600 ft into surrounding "
            "drainages. Dense mixed conifer and hardwood forest (ponderosa pine, "
            "Douglas fir, incense cedar, black oak, live oak) with heavy understory "
            "fuel loading -- much of the area has not experienced fire in 50+ years. "
            "The community was built in the 1960s-1980s as a subdivision carved into "
            "continuous forest, with winding roads, cul-de-sacs, and homes set among "
            "dense tree canopy. The road network is labyrinthine: crooked foothill "
            "roads wind through the forested neighborhood, and it is easy to become "
            "disoriented even without smoke. Fire weather meteorologists have "
            "specifically identified Alta Sierra as 'one of the most likely to burn "
            "down' communities in the Sierra Foothills -- it shares the same fire "
            "weather regime, vegetation type, and WUI geometry as pre-2018 Paradise "
            "but sits on an even narrower ridge with fewer evacuation options. "
            "Nevada County conducted emergency evacuation drills here in 2019, "
            "identifying it as one of the two most vulnerable communities in the "
            "county (along with Lake Wildwood). PG&E Public Safety Power Shutoffs "
            "(PSPS) affect the area multiple times per fire season, and mobile home "
            "park residents on master meters do not receive individual PSPS "
            "notifications -- a critical communication gap identified by local "
            "reporting."
        ),
        "key_features": [
            "Forested ridge between Bear River and Greenhorn Creek drainages",
            "Labyrinthine subdivision roads with cul-de-sacs carved into dense forest",
            "Same fire weather regime as Paradise (NE foehn/Diablo-like winds)",
            "No recent fire history -- heavy fuel accumulation over 50+ years",
            "NID (Nevada Irrigation District) water supply with aging infrastructure",
            "Alta Sierra Reservoir (1976) with deteriorating Hypalon liner",
            "PG&E PSPS notification gap for mobile home park master-meter residents",
            "Identified by Nevada County OES as one of top 2 vulnerable communities",
            "Dense mixed conifer/hardwood canopy closes over roads creating ember tunnels",
            "Proximity to Grass Valley/Nevada City fire corridor but isolated access",
        ],
        "elevation_range_ft": [1800, 2500],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "49 Fire",
                "year": 2009,
                "acres": 80,
                "details": (
                    "Grass fire near Highway 49 and Alta Sierra Drive that "
                    "demonstrated the rapid spread potential in the area's "
                    "dry grass and brush. Quickly contained but served as a "
                    "warning for the community."
                ),
            },
            {
                "name": "River Fire",
                "year": 2021,
                "acres": 2619,
                "details": (
                    "Burned near Bear River west of Colfax, 10 mi south of Alta "
                    "Sierra. Destroyed 142 structures. Same Bear River drainage "
                    "system; demonstrated fire spread potential in the corridor."
                ),
            },
            {
                "name": "Jones Fire",
                "year": 2015,
                "acres": 305,
                "details": (
                    "Burned in Nevada County near Grass Valley. Forced evacuations "
                    "in the greater Grass Valley area. Demonstrated vulnerability "
                    "of the broader Nevada County foothill communities."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Alta Sierra Drive to SR 49",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "Primary egress. Narrow, winding 2-lane road through dense "
                    "forest for ~3 miles to Highway 49. No shoulders, no turnouts. "
                    "During an active fire, this road would be flanked by burning "
                    "forest on both sides. Merge onto SR 49 is a T-intersection, "
                    "not an interchange -- creates bottleneck under mass evacuation."
                ),
                "risk": (
                    "Extreme. Single primary route for 7,000+ residents. Road "
                    "winds through continuous forest canopy that would create "
                    "ember tunnels and radiant heat exposure during fire."
                ),
            },
            {
                "route": "Dog Bar Road / You Bet Road",
                "direction": "S/SE",
                "lanes": 2,
                "bottleneck": (
                    "Secondary escape via narrow mountain roads dropping south "
                    "toward Bear River and eventually Colfax/I-80. Extremely "
                    "steep, winding, and narrow -- not suitable for mass evacuation. "
                    "Portions are single-lane with pullouts."
                ),
                "risk": (
                    "High. These roads drop into the Bear River canyon, which "
                    "is itself a fire corridor. Evacuees heading south into the "
                    "canyon could drive directly into a fire approaching from "
                    "the south or southwest."
                ),
            },
            {
                "route": "Local subdivision roads to Grass Valley",
                "direction": "N/NW",
                "lanes": 2,
                "bottleneck": (
                    "Network of winding residential streets connecting north "
                    "toward Grass Valley via various routes. Confusing network "
                    "of unnamed roads and cul-de-sacs. Residents unfamiliar "
                    "with alternative routes may become trapped."
                ),
                "risk": (
                    "Moderate to high. Routes are circuitous and unsigned. "
                    "In smoke conditions, navigation would be extremely difficult. "
                    "Color-coded evacuation route signs were proposed in 2019 but "
                    "implementation has been slow."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "NE foehn winds (Diablo-like). Dry northeasterly flow from the "
                "Great Basin descends the western Sierra slope, warming and drying "
                "adiabatically. At Alta Sierra's 2,300 ft elevation, these events "
                "produce sustained winds of 25-40 mph with gusts to 55+ mph, RH "
                "dropping below 10%, and temperatures spiking 10-15F above normal. "
                "Events most common Oct-Dec but can occur Sep-Jan."
            ),
            "critical_corridors": [
                "Bear River Canyon (S/SW approach -- upslope fire runs toward ridge)",
                "Greenhorn Creek drainage (N/NE approach -- wind-driven during foehn events)",
                "Highway 49 corridor (grass/brush fires can climb from roadside into forest)",
                "Wolf Creek drainage (SE approach connecting to broader American River watershed)",
            ],
            "rate_of_spread_potential": (
                "Extreme in grass/brush fuels at lower elevations (80-150 chains/hr "
                "in Diablo wind events). Moderate to high in continuous mixed conifer "
                "canopy (20-60 chains/hr) with potential for crown fire runs on steep "
                "slopes above Bear River. Ember transport distances of 0.5-2 mi "
                "expected given terrain-channeled winds."
            ),
            "spotting_distance": (
                "0.5-2.0 miles in moderate wind events; up to 3+ miles in extreme "
                "NE wind events given the terrain channeling through Bear River and "
                "Greenhorn Creek drainages. Dense conifer canopy provides abundant "
                "firebrands (bark plates, pine cones) for long-range spotting."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Served by Nevada Irrigation District (NID). The Alta Sierra "
                "Reservoir (3 million gallon capacity, built 1976) has a deteriorating "
                "Hypalon liner nearing end of useful life, with increasing risk of "
                "contamination from leaks. NID has allocated funding for a reservoir "
                "replacement project but construction timeline extends years out. "
                "Distribution system relies on gravity-fed pressure from the "
                "reservoir; if the reservoir fails or is compromised by fire, water "
                "pressure for firefighting drops to zero. No backup supply."
            ),
            "power": (
                "PG&E overhead distribution lines through dense forest canopy. "
                "Subject to frequent PSPS de-energization during fire weather events "
                "(multiple times per fire season). Potential PSPS events can affect "
                "~7,345 customers across Nevada County. Mobile home parks on master "
                "meters receive NO individual PG&E notification of shutoffs -- "
                "residents may lose power without warning. Medical baseline customers "
                "may not be reached for in-person notification."
            ),
            "communications": (
                "Limited cell coverage in canyon areas surrounding the ridge. "
                "PG&E PSPS events knock out cell towers without backup generators. "
                "Nevada County has invested in AlertWildfire camera network but "
                "notification systems depend on cell/internet connectivity that may "
                "be unavailable during combined fire + PSPS events."
            ),
            "medical": (
                "No medical facilities within the community. Nearest hospital is "
                "Sierra Nevada Memorial Hospital in Grass Valley, ~7 miles by road. "
                "Significant elderly population with mobility limitations. During a "
                "fire, the evacuation route to the hospital would likely be through "
                "or near the fire zone."
            ),
        },
        "demographics_risk_factors": {
            "population": 7204,
            "seasonal_variation": (
                "Modest summer increase from vacation properties and seasonal "
                "residents. Population fairly stable year-round as primarily a "
                "residential/retirement community."
            ),
            "elderly_percentage": "~22% age 65+",
            "mobile_homes": (
                "Multiple mobile home parks within the CDP, housing a significant "
                "portion of the elderly population. Mobile homes are extremely "
                "vulnerable to ember intrusion and radiant heat. Master-meter "
                "billing means residents are invisible to PG&E's PSPS notification "
                "system -- a documented and unresolved safety gap."
            ),
            "special_needs_facilities": (
                "No dedicated senior care facilities within Alta Sierra. Elderly "
                "residents dependent on home medical equipment (oxygen concentrators, "
                "CPAP, etc.) are at extreme risk during PSPS events and evacuations."
            ),
        },
    },

    # =========================================================================
    # 2. COLFAX, CA -- I-80 Corridor, Steep Ravines
    # =========================================================================
    "colfax_ca": {
        "center": [39.1007, -120.9533],
        "terrain_notes": (
            "Small city (pop. 1,995, 2020 census) at the crossroads of Interstate 80 "
            "and State Route 174 in Placer County, where I-80 begins its climb into "
            "the Sierra Nevada. Elevation ~2,425 ft. The town sits on a narrow ridge "
            "between steep ravines cut by the Bear River to the south, Canyon Creek, "
            "and numerous smaller drainages. The surrounding terrain is deeply "
            "dissected -- ravines drop 500-800 ft within a mile of the town center. "
            "Vegetation transitions from grass/oak woodland at lower elevations to "
            "mixed conifer (ponderosa pine, Douglas fir, black oak) on the ridge and "
            "in the ravines. The I-80 corridor through Colfax narrows to what locals "
            "call the 'Colfax Narrows' -- a constricted section where the freeway, "
            "rail corridor (historic Central Pacific / Union Pacific mainline), and "
            "town are squeezed onto the ridge between canyons. This concentration of "
            "infrastructure on a narrow ridge above steep, fuel-laden ravines creates "
            "extreme vulnerability. The 2021 River Fire demonstrated this: igniting "
            "at a campground on the Bear River west of town, it burned 2,619 acres "
            "and destroyed 142 structures before containment, forcing evacuation of "
            "the entire city and 7,000+ people across Nevada and Placer counties."
        ),
        "key_features": [
            "I-80 / SR 174 crossroads on narrow ridge between deep ravines",
            "Bear River canyon to south -- 2021 River Fire origin point",
            "Canyon Creek and Long Ravine flank the town on multiple sides",
            "Historic railroad corridor (Union Pacific mainline) through town center",
            "Colfax Fire Station documented 22 vegetation fires along I-80 corridor",
            "Hot-summer Mediterranean climate: 90F+ July/Aug with very low RH",
            "Rollins Lake Road provides secondary access to SR 174",
            "Gateway between Sacramento Valley and Sierra Nevada -- wind funnel",
        ],
        "elevation_range_ft": [1600, 2600],
        "wui_exposure": "high",
        "historical_fires": [
            {
                "name": "River Fire",
                "year": 2021,
                "acres": 2619,
                "details": (
                    "Ignited Aug 4 at Bear River campground west of Colfax. Human-caused. "
                    "Burned 2,619 acres in Placer and Nevada counties. Destroyed 142 "
                    "structures (102 single-family homes, 1 commercial, 39 outbuildings), "
                    "damaged 21 more. Forced evacuation of entire city of Colfax and "
                    "7,000+ people. Terrain and drought-stressed fuels enabled rapid "
                    "uphill spread from the Bear River canyon toward the ridge-top town. "
                    "Contained Aug 13."
                ),
            },
            {
                "name": "Lowell Fire",
                "year": 2015,
                "acres": 2038,
                "details": (
                    "Burned in Nevada County near Rollins Lake, just north of Colfax. "
                    "Forced evacuations in the SR 174 corridor. Demonstrated fire spread "
                    "potential in the ravine systems connecting Colfax to surrounding "
                    "wildlands."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Interstate 80 westbound",
                "direction": "W",
                "lanes": 4,
                "bottleneck": (
                    "Primary evacuation route toward Auburn and Sacramento. I-80 is "
                    "4 lanes (2 each direction) through the Colfax area but narrows "
                    "at the Colfax Narrows where the freeway, railroad, and town "
                    "are compressed onto the ridge. During River Fire, I-80 was "
                    "used for evacuation but traffic congestion was severe."
                ),
                "risk": (
                    "Moderate. I-80 provides high-capacity evacuation but the "
                    "Colfax Narrows constrain capacity. A fire burning from the "
                    "Bear River canyon to the south could push smoke and flames "
                    "directly across or adjacent to I-80."
                ),
            },
            {
                "route": "Interstate 80 eastbound",
                "direction": "E",
                "lanes": 4,
                "bottleneck": (
                    "Eastbound toward Emigrant Gap and Donner Pass. Gains elevation "
                    "rapidly. During winter, chains may be required, but fire season "
                    "this route is viable. Leads further into forest, which may not "
                    "be advisable during a large fire."
                ),
                "risk": (
                    "Moderate. Route climbs into denser forest and higher elevations, "
                    "potentially driving evacuees into worse fire conditions."
                ),
            },
            {
                "route": "SR 174 northbound to Grass Valley",
                "direction": "N",
                "lanes": 2,
                "bottleneck": (
                    "Two-lane highway running 13 miles north through the western "
                    "Sierra foothills to Grass Valley/SR 20/SR 49 junction. Follows "
                    "the old Lincoln Highway alignment. Narrow, winding, no shoulders "
                    "for most of its length. Passes through forest and rural areas."
                ),
                "risk": (
                    "High. Narrow 2-lane road through forest with no alternative "
                    "if blocked by fire. During River Fire, this corridor was "
                    "threatened. Connects to additional at-risk communities "
                    "(Grass Valley, Nevada City, Alta Sierra)."
                ),
            },
            {
                "route": "Rollins Lake Road / Canyon Way",
                "direction": "N/NW",
                "lanes": 2,
                "bottleneck": (
                    "Local roads providing alternative access to SR 174 corridor. "
                    "Narrow, rural, no capacity for mass evacuation. Drops into "
                    "ravines before climbing back to the ridge."
                ),
                "risk": (
                    "High. Roads pass through canyons with heavy fuel loads. "
                    "Could be cut off by fire simultaneously with SR 174."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Terrain-channeled upslope/downslope winds through Bear River and "
                "Canyon Creek ravines. During NE foehn events, winds accelerate "
                "through the ravine systems and up the steep canyon walls toward the "
                "ridge-top town. Afternoon upslope thermal winds during summer create "
                "daily fire weather windows (1400-1800 PDT) with RH below 15%."
            ),
            "critical_corridors": [
                "Bear River canyon (S -- upslope fire runs directly at town, as in River Fire 2021)",
                "Canyon Creek / Long Ravine (W/NW -- steep-sided ravines channeling fire toward I-80 corridor)",
                "I-80 right-of-way (ignition risk from vehicles, sparks from railroad, power lines)",
                "SR 174 corridor toward Rollins Lake (N -- continuous forest fuel bed)",
            ],
            "rate_of_spread_potential": (
                "Extreme in grass/brush fuels on canyon slopes (100-200 chains/hr "
                "during wind events). The 2021 River Fire demonstrated rapid upslope "
                "runs from the Bear River canyon bottom to the ridge in drought-stressed "
                "fuels. Moderate in mixed conifer (30-60 chains/hr). The steep terrain "
                "geometry (500-800 ft ravines) creates a chimney effect amplifying "
                "upslope spread rates by 2-3x."
            ),
            "spotting_distance": (
                "0.5-1.5 miles typical. Embers lofted from ravine fires land on the "
                "ridge top, igniting structures. The 2021 River Fire produced extensive "
                "spotting ahead of the main front."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "City of Colfax municipal water system. Limited storage capacity "
                "for a simultaneous structure protection and civilian supply scenario. "
                "System depends on treated water from limited reservoir capacity."
            ),
            "power": (
                "PG&E overhead distribution and transmission lines through forest "
                "and along I-80 corridor. Subject to PSPS de-energization. Union "
                "Pacific railroad mainline creates additional spark/ignition risk "
                "during dry conditions."
            ),
            "communications": (
                "Adequate cell coverage along I-80 corridor but degraded in "
                "surrounding ravines. Canyon terrain creates radio shadows. During "
                "River Fire, communications were strained by volume of 911 calls "
                "and evacuation notifications."
            ),
            "medical": (
                "No hospital in Colfax. Nearest hospital is Sutter Auburn Faith "
                "Hospital in Auburn, ~18 miles west on I-80. Fire station in town "
                "but limited staffing for simultaneous fire suppression and EMS."
            ),
        },
        "demographics_risk_factors": {
            "population": 1995,
            "seasonal_variation": (
                "Modest increase during summer recreation season due to Rollins Lake "
                "visitors and campground use along Bear River. Campground-related "
                "ignitions are a documented risk (River Fire origin)."
            ),
            "elderly_percentage": "~18% age 65+",
            "mobile_homes": (
                "Mobile home parks present in and around Colfax. Structures are "
                "vulnerable to ember intrusion and radiant heat. Low-income residents "
                "may lack resources for evacuation or hardening."
            ),
            "special_needs_facilities": (
                "No dedicated senior care or special needs facilities. Small-town "
                "resources are limited for assisting mobility-impaired residents "
                "during rapid evacuation."
            ),
        },
    },

    # =========================================================================
    # 3. FORESTHILL, CA -- Remote Peninsula Ridge Above American River
    # =========================================================================
    "foresthill_ca": {
        "center": [39.0202, -120.8180],
        "terrain_notes": (
            "Unincorporated community (pop. 1,692, 2020 census) perched on a broad "
            "ridge -- the Foresthill Divide -- between the North Fork and Middle Fork "
            "of the American River in Placer County. Elevation ~3,228 ft. The "
            "community sits on an ancient gold-bearing river gravel bed atop a "
            "geological peninsula: the ridge narrows and drops off steeply on three "
            "sides into canyons with 2,000+ ft of relief. Access is essentially via a "
            "single road -- Foresthill Road -- which runs 17 miles west from the "
            "community to Auburn and I-80, crossing the 730-ft-high Auburn-Foresthill "
            "Bridge over the North Fork American River. This bridge, the tallest in "
            "California, is the critical lifeline: if Foresthill Road or the bridge "
            "is closed by fire, the only alternatives are two dirt roads through steep "
            "canyon terrain -- essentially impassable for mass evacuation. The 2022 "
            "Mosquito Fire (76,788 acres, largest CA fire of 2022) burned out of the "
            "Middle Fork American River canyon and threatened Foresthill directly, "
            "forcing evacuation of ~11,000 people from Foresthill, Georgetown, and "
            "surrounding communities. The fire destroyed 78 structures in the area "
            "and took 46 days to contain. Firefighters described 'extremely steep and "
            "inaccessible terrain' in the canyon systems. The community has multiple "
            "mobile home parks (4+ parks with 40-134 sites each, oldest dating to "
            "1960) housing vulnerable populations."
        ),
        "key_features": [
            "Geological peninsula ridge -- steep drop-offs on 3 sides into 2,000+ ft canyons",
            "Single paved access: Foresthill Road (17 mi to Auburn/I-80)",
            "Auburn-Foresthill Bridge: tallest bridge in CA (730 ft), critical lifeline",
            "North Fork American River canyon to north (2,000+ ft relief)",
            "Middle Fork American River canyon to south (2,500+ ft relief)",
            "2022 Mosquito Fire origin: Oxbow Reservoir on Middle Fork",
            "Ancient gold mining area -- deep gravel beds, altered hydrology",
            "Multiple mobile home parks (4+, 40-134 sites each, 1960s vintage)",
            "Foresthill Public Utility District -- 2,034 water connections",
            "Dense mixed conifer forest: ponderosa pine, Douglas fir, white fir, incense cedar",
        ],
        "elevation_range_ft": [2800, 3600],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Mosquito Fire",
                "year": 2022,
                "acres": 76788,
                "details": (
                    "Largest California wildfire of 2022. Ignited Sep 6 on north shore "
                    "of Oxbow Reservoir in Middle Fork American River drainage. Burned "
                    "76,788 acres in Placer and El Dorado counties across Tahoe and "
                    "Eldorado National Forests. Destroyed 78 structures in Michigan "
                    "Bluff, Foresthill, and Volcanoville. Forced evacuation of ~11,000 "
                    "residents. Burned in 'extremely steep and inaccessible terrain' "
                    "for 46 days before full containment on Oct 22. Jumped the American "
                    "River and advanced on Foresthill from the south."
                ),
            },
            {
                "name": "Bridge Fire",
                "year": 2021,
                "acres": 411,
                "details": (
                    "Burned directly under the Auburn-Foresthill Bridge in Sep 2021. "
                    "Arson-caused. Demonstrated the vulnerability of the single "
                    "critical access point -- a fire at the bridge effectively cuts "
                    "off Foresthill from any high-capacity evacuation route. Burned "
                    "411 acres and caused temporary road closures."
                ),
            },
            {
                "name": "Foresthill Fire (Trailhead Fire)",
                "year": 2016,
                "acres": 130,
                "details": (
                    "Wildfire near Foresthill that prompted evacuations. Demonstrated "
                    "the rapid response challenges given the remote single-road access."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Foresthill Road westbound to Auburn / I-80",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "THE critical evacuation route. 17-mile, 2-lane mountain road "
                    "winding along the ridge to Auburn, crossing the 730-ft-high "
                    "Auburn-Foresthill Bridge. No shoulders for most of its length. "
                    "Steep grades, sharp curves, and forest canopy on both sides. "
                    "If fire reaches Foresthill Road at any point along its 17-mile "
                    "length, the community is cut off from its only viable evacuation "
                    "route. During the 2022 Mosquito Fire, residents were escorted "
                    "by law enforcement on Foresthill Road subject to fire conditions."
                ),
                "risk": (
                    "Extreme. Single point of failure. 1,692+ residents dependent "
                    "on one 17-mile, 2-lane road. The bridge itself is a choke point: "
                    "the 2021 Bridge Fire burned directly beneath it, demonstrating "
                    "that an arson or accidental fire could simultaneously cut off "
                    "evacuation and destroy critical infrastructure."
                ),
            },
            {
                "route": "Mosquito Ridge Road / secondary dirt roads",
                "direction": "E/NE",
                "lanes": 1,
                "bottleneck": (
                    "Narrow dirt/gravel forest roads leading east deeper into the "
                    "Sierra Nevada (toward French Meadows, Hell Hole Reservoir). "
                    "Single-lane, steep, winding, no services. Essentially unusable "
                    "for mass evacuation -- leads further from civilization into "
                    "National Forest. Only viable for individual vehicles with "
                    "high clearance and local knowledge."
                ),
                "risk": (
                    "Extreme. These roads lead into the wilderness, not toward "
                    "safety. Evacuees would be driving deeper into forest with "
                    "no services, cell coverage, or population centers."
                ),
            },
            {
                "route": "Yankee Jims Road to canyon bottom",
                "direction": "N",
                "lanes": 1,
                "bottleneck": (
                    "Steep, narrow, partially unpaved road dropping into the North "
                    "Fork American River canyon. Historic gold mining road. Not "
                    "suitable for standard vehicles or mass evacuation. Gains/loses "
                    "2,000 ft of elevation in a few miles."
                ),
                "risk": (
                    "Extreme. Canyon-bottom roads are death traps during fire. "
                    "This route would only be used as an absolute last resort."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Complex terrain-driven winds. Canyon winds from both the North Fork "
                "and Middle Fork drainages create convergent upslope flow on the "
                "Foresthill Divide ridge during afternoon heating. NE foehn events "
                "produce strong downslope winds channeling through the American River "
                "canyons. The deep canyons (2,000+ ft) create extreme pre-heating "
                "on steep slopes, enabling explosive upslope fire runs from canyon "
                "bottoms to the ridge top."
            ),
            "critical_corridors": [
                "Middle Fork American River canyon (S -- Mosquito Fire approach vector 2022)",
                "North Fork American River canyon (N -- Bridge Fire 2021 approach)",
                "Foresthill Road corridor (W -- single evacuation route, flanked by forest)",
                "Oxbow Reservoir / Volcanoville drainage (SE -- fire approach from Eldorado NF)",
            ],
            "rate_of_spread_potential": (
                "Extreme on steep canyon slopes (100-300 chains/hr during upslope "
                "runs). The Mosquito Fire demonstrated multi-day runs through "
                "'extremely steep and inaccessible terrain' where direct attack "
                "was impossible. Crown fire potential is high in the dense mixed "
                "conifer stands on the ridge. Moderate to high along the ridge top "
                "(20-50 chains/hr in timber fuels). The 2,000+ ft of canyon relief "
                "creates massive pre-heating zones that can accelerate fire spread "
                "rates far beyond flat-ground predictions."
            ),
            "spotting_distance": (
                "1-3 miles. The deep canyons create powerful convection columns "
                "that loft firebrands to extreme heights. Embers carried by terrain-"
                "channeled winds can cross the 1-2 mile wide ridge and ignite spots "
                "on the opposite canyon slope. During Mosquito Fire, fire jumped the "
                "entire American River canyon."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Foresthill Public Utility District (FPUD), formed 1950, operates "
                "2,034 water service connections. Water treatment and distribution "
                "depend on infrastructure that is 50+ years old in places. System "
                "capacity is limited for simultaneous firefighting water demand and "
                "civilian supply. Remote location means mutual aid response times "
                "are long (30+ min from Auburn)."
            ),
            "power": (
                "PG&E overhead lines along Foresthill Road -- the single power "
                "supply corridor mirrors the single road access. A fire along "
                "Foresthill Road could simultaneously cut power and evacuation "
                "route. Subject to PSPS de-energization during fire weather."
            ),
            "communications": (
                "Limited cell coverage on the Divide; effectively zero in surrounding "
                "canyons. Satellite phone or ham radio may be the only communication "
                "during a combined fire + power outage. AlertWildfire cameras provide "
                "remote monitoring but local notification depends on cell/internet."
            ),
            "medical": (
                "No hospital, no urgent care. Foresthill Fire Protection District "
                "provides first response but is a volunteer/paid-call department "
                "with limited resources. Nearest hospital is Sutter Auburn Faith "
                "in Auburn, 20+ miles and 30+ minutes away via Foresthill Road -- "
                "assuming the road is open."
            ),
        },
        "demographics_risk_factors": {
            "population": 1692,
            "seasonal_variation": (
                "Significant summer increase from recreation visitors to American "
                "River canyon, Foresthill Divide trails, and OHV areas. French "
                "Meadows and Hell Hole reservoirs draw campers through Foresthill "
                "on the single access road."
            ),
            "elderly_percentage": "~23% age 65+",
            "mobile_homes": (
                "Four or more mobile home parks totaling 200+ sites, with the "
                "oldest dating to 1960-1962. Mobile homes constitute a significant "
                "fraction of local housing stock. These structures are highly "
                "vulnerable to ember intrusion and have limited structural resistance "
                "to radiant heat. Many elderly residents live in these parks."
            ),
            "special_needs_facilities": (
                "No dedicated senior care, assisted living, or special needs "
                "facilities. Remote location and single-road access make "
                "emergency medical transport extremely challenging."
            ),
        },
    },

    # =========================================================================
    # 4. POLLOCK PINES, CA -- Highway 50 Corridor, El Dorado NF
    # =========================================================================
    "pollock_pines_ca": {
        "center": [38.7614, -120.5891],
        "terrain_notes": (
            "Census-designated place (pop. 7,112, 2020 census) straddling U.S. "
            "Highway 50 in El Dorado County, approximately 13 miles east of "
            "Placerville and 58 miles east of Sacramento. Elevation ~3,980 ft. "
            "The community is embedded within the Eldorado National Forest at the "
            "transition from Sierra foothill woodland to montane conifer forest. "
            "Terrain is moderately steep, with the South Fork American River drainage "
            "to the north and the Cosumnes River headwaters to the south. Pollock "
            "Pines has been threatened or directly impacted by two of California's "
            "most significant wildfires: the 2014 King Fire (97,717 acres, arson-caused, "
            "$100M+ suppression cost) and the 2021 Caldor Fire (221,835 acres), which "
            "forced mandatory evacuation of the entire community. During Caldor, the "
            "fire burned to within 2 miles of Pollock Pines before prescribed burn "
            "treatments on the 'Fire Adapted 50' project area slowed its advance and "
            "protected the community. Highway 50 is the lifeline and the bottleneck: "
            "it narrows from a 4-lane divided highway west of Placerville to a 2-lane "
            "undivided highway through the Pollock Pines area, creating extreme "
            "congestion during evacuations. During Caldor, a nearly 50-mile closure "
            "of Highway 50 from Sly Park Road to Meyers stranded communities east of "
            "the fire."
        ),
        "key_features": [
            "Highway 50 corridor: 4-lane divided W of Placerville, 2-lane through Pollock Pines",
            "Embedded within Eldorado National Forest -- surrounded by continuous forest",
            "Sly Park Reservoir (Jenkinson Lake) -- major recreation/water supply 3 mi S",
            "Fire Adapted 50 fuel treatment project -- proved effective during Caldor Fire",
            "Transition zone: foothill woodland to montane conifer forest at 4,000 ft",
            "King Fire (2014) burned 97,717 acres from arson ignition at King of the Mountain Road",
            "Caldor Fire (2021) burned 221,835 acres, forced full evacuation of community",
            "Multiple mobile home parks (9.6% of housing stock)",
            "El Dorado County Fire Protection District coverage",
        ],
        "elevation_range_ft": [3400, 4400],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Caldor Fire",
                "year": 2021,
                "acres": 221835,
                "details": (
                    "Ignited Aug 14 near Little Mountain, south of Pollock Pines. "
                    "Burned 221,835 acres across El Dorado, Amador, and Alpine "
                    "counties. On Aug 17, mandatory evacuations were ordered for "
                    "Pollock Pines, Sly Park, Grizzly Flats, and Somerset. Fire "
                    "grew from 6,500 acres to 30,000 acres in a single day driven "
                    "by high winds. By Aug 20, fire reached Highway 50, forcing "
                    "its closure. Fire eventually crossed Highway 50 near Kyburz and "
                    "advanced to within 5 miles of South Lake Tahoe. The Fire Adapted "
                    "50 prescribed burn project is credited with slowing the fire's "
                    "advance and protecting Pollock Pines structures. Caldor destroyed "
                    "over 1,000 structures overall, including the near-total destruction "
                    "of Grizzly Flats (pop. ~1,200). Contained Oct 21."
                ),
            },
            {
                "name": "King Fire",
                "year": 2014,
                "acres": 97717,
                "details": (
                    "Arson fire ignited Sep 13 along King of the Mountain Road in "
                    "Pollock Pines. Burned 97,717 acres primarily in Eldorado National "
                    "Forest. Suppression cost exceeded $100 million and engaged 8,000+ "
                    "personnel at peak. Most of the forest burned had no recent fire "
                    "history, with the last major fire being the 1992 Cleveland Fire "
                    "(22,500 acres). King Fire forced evacuations along the Highway 50 "
                    "corridor and demonstrated the extreme fire behavior possible in "
                    "these fuel-heavy forests."
                ),
            },
            {
                "name": "Cleveland Fire",
                "year": 1992,
                "acres": 22500,
                "details": (
                    "Last major fire in the area before the King Fire. Burned ~22,500 "
                    "acres in the Eldorado National Forest, establishing the baseline "
                    "for 22+ years of fuel accumulation that made the King Fire so "
                    "devastating."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "US Highway 50 westbound toward Placerville/Sacramento",
                "direction": "W",
                "lanes": 2,
                "bottleneck": (
                    "Primary evacuation route. Highway 50 is only 2 lanes (undivided) "
                    "through the Pollock Pines area, expanding to 4-lane divided west "
                    "of Placerville. This lane reduction is the critical bottleneck: "
                    "7,000+ residents plus highway through-traffic compress into 2 "
                    "lanes. During Caldor Fire, evacuation traffic from Pollock Pines "
                    "traveled westbound on Highway 50 with severe congestion."
                ),
                "risk": (
                    "Extreme. The 2-lane section creates a severe capacity constraint. "
                    "During Caldor, Highway 50 was eventually closed entirely (Sly Park "
                    "Road to Meyers, ~50 miles) as fire crossed the highway."
                ),
            },
            {
                "route": "Sly Park Road southbound to Mormon Emigrant Trail / Hwy 88",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Secondary evacuation route. 2-lane road running 5 miles south to "
                    "Mormon Emigrant Trail (Iron Mountain Road), then to Highway 88 via "
                    "a 30+ mile winding mountain route. Narrow, steep, and slow. "
                    "Used as official detour when Highway 50 was closed during Caldor."
                ),
                "risk": (
                    "High. Long, winding detour through forest. The Caldor Fire burned "
                    "across portions of this route. Not viable for rapid mass evacuation "
                    "-- adds 2+ hours to reach Sacramento compared to Highway 50 direct."
                ),
            },
            {
                "route": "US Highway 50 eastbound toward Tahoe",
                "direction": "E",
                "lanes": 2,
                "bottleneck": (
                    "Eastbound escape toward Kyburz, Echo Summit, and South Lake Tahoe. "
                    "2 lanes, mountain grades, and during Caldor Fire, this route was "
                    "completely closed as fire burned across Highway 50 near Kyburz. "
                    "Driving east during a Caldor-type event means driving toward "
                    "the fire."
                ),
                "risk": (
                    "Extreme during major fires. Route leads deeper into National "
                    "Forest and toward higher elevations with no alternative roads."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Afternoon upslope thermal winds from the Sacramento Valley drive "
                "fire spread from SW to NE up the Highway 50 corridor during summer. "
                "NE foehn (Diablo-like) events in fall produce strong downslope winds "
                "that can push fire rapidly from E to W. The Caldor Fire's explosive "
                "growth was driven by a combination of low humidity, high temperatures, "
                "and terrain-channeled winds through the South Fork American River and "
                "Cosumnes River drainages."
            ),
            "critical_corridors": [
                "Highway 50 corridor (E-W axis -- fire can approach from either direction)",
                "South Fork American River drainage (N -- deep canyon channeling winds)",
                "Cosumnes River headwaters (S -- Caldor Fire approach vector)",
                "Sly Park / Jenkinson Lake drainage (S -- secondary fire approach corridor)",
            ],
            "rate_of_spread_potential": (
                "Extreme. Caldor Fire grew from 6,500 to 30,000 acres in 24 hours. "
                "King Fire expanded rapidly through fuel-heavy forest with no recent "
                "fire history. In continuous conifer forest at this elevation, crown "
                "fire runs of 50-100 chains/hr are possible during wind events. The "
                "Fire Adapted 50 treatments demonstrated that fuel reduction can "
                "reduce spread rates to manageable levels (surface fire vs. crown fire)."
            ),
            "spotting_distance": (
                "1-3 miles in terrain-channeled winds. King Fire produced extensive "
                "spotting through continuous conifer canopy. Caldor Fire's spotting "
                "across Highway 50 demonstrated 1+ mile ember transport."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "El Dorado Irrigation District (EID) serves the community. Sly Park "
                "Reservoir (Jenkinson Lake, ~41,000 acre-feet) provides both water "
                "supply and recreation. Distribution system is adequate for normal "
                "operations but may be overwhelmed by simultaneous wildfire suppression "
                "demand. Fire can damage exposed water infrastructure (above-ground "
                "pipes, pump stations) along the Highway 50 corridor."
            ),
            "power": (
                "PG&E overhead distribution lines through continuous forest. Subject "
                "to PSPS de-energization. Power lines along Highway 50 are vulnerable "
                "to fire damage. The King Fire was ignited near power infrastructure. "
                "Extended PSPS events can last days, affecting medical equipment users."
            ),
            "communications": (
                "Cell coverage along Highway 50 corridor is adequate but degrades "
                "rapidly in side drainages and forest. During Caldor Fire, emergency "
                "communications were challenged by the volume and pace of evacuations. "
                "Loss of power (PSPS or fire damage) can take down cell towers."
            ),
            "medical": (
                "No hospital in Pollock Pines. Nearest is Marshall Medical Center in "
                "Placerville, 13 miles west on Highway 50. During fire events when "
                "Highway 50 is congested or closed, medical transport times increase "
                "dramatically. Multiple mobile home parks house elderly residents "
                "with medical needs."
            ),
        },
        "demographics_risk_factors": {
            "population": 7112,
            "seasonal_variation": (
                "Significant summer recreation population from Sly Park Reservoir "
                "(Jenkinson Lake) visitors, campgrounds in Eldorado National Forest, "
                "and Highway 50 through-traffic to Lake Tahoe. Summer population "
                "can effectively double on peak weekends."
            ),
            "elderly_percentage": "~19% age 65+",
            "mobile_homes": (
                "Mobile homes account for 9.6% of housing (328 units). Multiple "
                "mobile home parks including senior (55+) communities. These "
                "structures are highly vulnerable to ember attack and radiant heat. "
                "Parks include Bonanza MHP, Ponderosa Estates, and Dogwood MHP."
            ),
            "special_needs_facilities": (
                "55+ senior mobile home communities with elderly residents. No "
                "dedicated medical or assisted living facilities. Elderly residents "
                "on medical equipment are at extreme risk during PSPS events."
            ),
        },
    },

    # =========================================================================
    # 5. GEORGETOWN, CA -- Georgetown Divide, Limited Access
    # =========================================================================
    "georgetown_ca": {
        "center": [38.9068, -120.8385],
        "terrain_notes": (
            "Census-designated place (pop. 2,580, 2023 estimate; 2,255 per 2020 "
            "census) situated on the Georgetown Divide, a broad ridge between the "
            "Middle Fork and South Fork of the American River in El Dorado County. "
            "Elevation ~2,654 ft with the surrounding Georgetown Divide reaching "
            "3,409 ft. The community is the northeastern-most town in the California "
            "Mother Lode and is surrounded by Eldorado National Forest. The Georgetown "
            "Divide Public Utility District (GDPUD) serves 3,800 connections across "
            "72,000 acres (112.5 sq mi) of unincorporated western El Dorado County, "
            "serving ~10,000 residents across Georgetown, Garden Valley, Kelsey, and "
            "surrounding areas. Access is limited: Highway 193 from Placerville is "
            "the primary route (2-lane, winding, 15 miles), with Wentworth Springs "
            "Road, Marshall Road, and Greenwood Road providing narrow secondary access. "
            "The 2022 Mosquito Fire (76,788 acres) forced evacuation of Georgetown and "
            "surrounding communities when the fire jumped the American River and "
            "advanced from the north. In 2024, the Crozier Fire (1,960 acres) burned "
            "between the Caldor and Mosquito Fire scars, again forcing evacuations in "
            "the Georgetown Divide area."
        ),
        "key_features": [
            "Georgetown Divide ridge between Middle Fork and South Fork American River",
            "GDPUD serves 72,000 acres (112.5 sq mi) of unincorporated western El Dorado County",
            "Highway 193 is primary access -- 2-lane, winding, 15 mi from Placerville",
            "Surrounded by Eldorado National Forest on three sides",
            "2022 Mosquito Fire forced full evacuation of Georgetown area",
            "2024 Crozier Fire burned between Caldor and Mosquito Fire scars nearby",
            "GDPUD water infrastructure damaged by Mosquito Fire (flume, stream gages, levee roads)",
            "Stumpy Meadows Reservoir (21,206 acre-feet) is cornerstone water supply",
            "Walton Lake water treatment plant (built 1974) serves Georgetown proper",
            "Garden Valley, Kelsey, Volcanoville are satellite communities on the Divide",
        ],
        "elevation_range_ft": [1800, 3500],
        "wui_exposure": "extreme",
        "historical_fires": [
            {
                "name": "Mosquito Fire",
                "year": 2022,
                "acres": 76788,
                "details": (
                    "Largest CA wildfire of 2022. Ignited Sep 6 at Oxbow Reservoir on "
                    "Middle Fork American River. Burned 76,788 acres in Placer and El "
                    "Dorado counties. Jumped the American River and advanced on "
                    "Georgetown from the north. Forced evacuation of ~11,000 residents "
                    "across Foresthill and Georgetown areas. Destroyed 78 structures "
                    "in Michigan Bluff, Foresthill, and Volcanoville. Directly damaged "
                    "GDPUD water infrastructure: destroyed 3 stream gages, charred the "
                    "wooden flume covering at a tunnel entrance, damaged levee roads. "
                    "GDPUD declared emergency. Contained Oct 22."
                ),
            },
            {
                "name": "Crozier Fire",
                "year": 2024,
                "acres": 1960,
                "details": (
                    "Ignited Aug 7 near Slate Mountain, northwest of Placerville. Burned "
                    "1,960 acres between the Caldor and Mosquito Fire burn scars. Forced "
                    "evacuations in Georgetown, Garden Valley, Volcanoville, Mosquito, "
                    "and Quintet areas. Arson-caused (man convicted). No structures "
                    "destroyed, but demonstrated the ongoing fire risk in the Georgetown "
                    "Divide even in areas adjacent to recent burn scars."
                ),
            },
            {
                "name": "Georgetown Fire",
                "year": 2016,
                "acres": 75,
                "details": (
                    "Small wildfire near Georgetown that prompted evacuations and "
                    "demonstrated response challenges given limited access routes."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 193 southwest to Placerville / US 50",
                "direction": "SW",
                "lanes": 2,
                "bottleneck": (
                    "Primary evacuation route. 2-lane, winding highway running ~15 "
                    "miles through forest and rural areas from Georgetown to "
                    "Placerville and Highway 50. Narrow, steep sections with no "
                    "shoulders. Passes through Garden Valley and Kelsey. Becomes "
                    "congested during evacuations when 10,000+ Divide residents "
                    "attempt to use the single highway simultaneously."
                ),
                "risk": (
                    "High. A fire between Georgetown and Placerville could cut "
                    "the primary evacuation route. The Crozier Fire demonstrated "
                    "this risk, burning near the Highway 193 corridor."
                ),
            },
            {
                "route": "Wentworth Springs Road northeast",
                "direction": "NE",
                "lanes": 2,
                "bottleneck": (
                    "Secondary route leading northeast deeper into the Sierra "
                    "and Eldorado National Forest. Narrow, winding mountain road. "
                    "Leads toward Stumpy Meadows Reservoir and eventually dead-ends "
                    "in the forest. Not a viable mass evacuation route."
                ),
                "risk": (
                    "High. Route leads deeper into National Forest, not toward "
                    "safety. Only useful for escaping a fire approaching from the "
                    "southwest if the route itself is not threatened."
                ),
            },
            {
                "route": "Marshall Road / Greenwood Road south",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "Narrow rural roads connecting Georgetown area south through "
                    "Garden Valley to SR 193. These provide alternative routing "
                    "but are narrow (no shoulders), slow, and pass through "
                    "forested areas with heavy fuel loads."
                ),
                "risk": (
                    "High. Narrow roads through continuous forest. Not designed "
                    "for mass evacuation. Provides some redundancy to Highway 193 "
                    "but can be simultaneously threatened by the same fire."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Complex terrain-driven winds from American River canyon systems. "
                "Afternoon upslope flow from both the Middle Fork and South Fork "
                "drainages creates convergent wind patterns on the Georgetown Divide. "
                "NE foehn events produce strong downslope winds through the canyon "
                "systems. The deep canyons (1,500-2,500 ft) create massive pre-heating "
                "zones and channel winds toward the ridge-top community."
            ),
            "critical_corridors": [
                "Middle Fork American River canyon (N -- Mosquito Fire approach vector)",
                "South Fork American River canyon (S -- fire approach from Caldor Fire territory)",
                "Highway 193 corridor (SW -- connects fire threat to evacuation route)",
                "Volcanoville / Michigan Bluff drainage (NE -- direct path to Georgetown)",
            ],
            "rate_of_spread_potential": (
                "Extreme on steep canyon slopes. The Mosquito Fire demonstrated "
                "multi-mile runs through canyon terrain at rates exceeding 100 "
                "chains/hr. On the Divide ridge, spread rates moderate in timber "
                "fuels (20-50 chains/hr) but crown fire potential remains high in "
                "untreated areas. The 2024 Crozier Fire growth showed that even in "
                "areas adjacent to recent burn scars, sufficient fuel exists for "
                "rapid fire spread."
            ),
            "spotting_distance": (
                "1-3 miles. The Mosquito Fire jumped the entire American River "
                "canyon, demonstrating spotting distances of 1+ mile across deep "
                "terrain. Terrain-channeled winds through the canyon systems can "
                "transport embers onto the Georgetown Divide from fires burning "
                "in canyon bottoms."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "Georgetown Divide Public Utility District (GDPUD). Cornerstone "
                "supply is Stumpy Meadows Reservoir (21,206 acre-feet). Walton Lake "
                "treatment plant (built 1974) serves Georgetown, Garden Valley, and "
                "part of Greenwood. The 2022 Mosquito Fire directly damaged GDPUD "
                "infrastructure: destroyed 3 stream gages, charred wooden flume "
                "covering at tunnel entrance, damaged levee roads used for "
                "maintenance access. GDPUD declared emergency and has received "
                "$1.5M for Water Reliability and Fire Resiliency Storage Tank Project "
                "but reconstruction is ongoing. Raw water conveyance system "
                "includes exposed flumes and tunnels vulnerable to fire."
            ),
            "power": (
                "PG&E overhead distribution through forest canopy. Subject to "
                "PSPS de-energization. Power infrastructure in remote areas of "
                "the Divide is particularly vulnerable to fire and wind damage. "
                "Extended outages common during fire weather events."
            ),
            "communications": (
                "Limited cell coverage across the Divide, especially in canyon "
                "areas and remote communities like Volcanoville. During Mosquito "
                "Fire, communications were strained. Georgetown Divide Fire Safe "
                "Council has worked to improve community notification systems."
            ),
            "medical": (
                "No hospital on the Georgetown Divide. Nearest is Marshall Medical "
                "Center in Placerville, 15+ miles via Highway 193. Garden Valley "
                "and Georgetown fire stations provide first response. During fire "
                "events with Highway 193 congested or closed, medical access is "
                "severely compromised for 10,000 Divide residents."
            ),
        },
        "demographics_risk_factors": {
            "population": 2580,
            "seasonal_variation": (
                "Summer recreation visitors to Stumpy Meadows Reservoir, Georgetown "
                "OHV trail system, and surrounding National Forest. Small increase "
                "compared to year-round population."
            ),
            "elderly_percentage": "~20% age 65+",
            "mobile_homes": (
                "Mobile and manufactured homes present throughout the Divide, "
                "particularly in unincorporated areas around Georgetown and Garden "
                "Valley. Limited building code enforcement in rural county areas."
            ),
            "special_needs_facilities": (
                "No dedicated senior care or medical facilities on the Divide. "
                "Elderly and mobility-impaired residents are dependent on private "
                "transportation for evacuation. Georgetown Divide's remote location "
                "means ambulance response times are 20-30+ minutes."
            ),
        },
    },

    # =========================================================================
    # 6. PLACERVILLE OUTSKIRTS / DIAMOND SPRINGS, CA -- WUI Edge along El Dorado NF
    # =========================================================================
    "diamond_springs_ca": {
        "center": [38.6946, -120.8149],
        "terrain_notes": (
            "Census-designated place (pop. ~11,000; 11,037 per 2010 census, ~12,600 "
            "estimated 2023) in El Dorado County, immediately south and east of "
            "Placerville along the Highway 49 and Pleasant Valley Road corridors. "
            "Elevation ~1,791 ft, at the lower boundary of the Sierra foothill "
            "woodland zone transitioning into the Eldorado National Forest. Diamond "
            "Springs is the quintessential WUI edge community: residential "
            "development directly abuts wildland fuels (grass, oak woodland, "
            "mixed conifer) along the El Dorado National Forest boundary. The Diamond "
            "Springs-El Dorado Fire Protection District serves ~11,731 residents "
            "across 65.5 square miles of semi-urban and rural terrain. The area's "
            "fire history reflects its position at the NF boundary: the 2014 Sand "
            "Fire (3,800 acres) burned near Highway 49 at the Amador-El Dorado "
            "county line, destroying 13 homes and forcing 1,083 evacuations. The "
            "2024 Crozier Fire (1,960 acres) burned northeast of Diamond Springs "
            "toward Georgetown. More ominously, the 2021 Caldor Fire (221,835 acres) "
            "and 2014 King Fire (97,717 acres) burned in the forests just east of "
            "Diamond Springs, and a westward-running fire of similar magnitude would "
            "directly threaten the community."
        ),
        "key_features": [
            "WUI edge community: residential development directly abutting El Dorado NF",
            "Diamond Springs-El Dorado Fire Protection District: 65.5 sq mi, ~11,731 residents",
            "Highway 49 and Pleasant Valley Road corridors provide primary access",
            "Elevation ~1,800 ft -- lower foothill zone with grass/oak/conifer transition",
            "Proximity to Caldor Fire (2021, 221,835 acres) and King Fire (2014, 97,717 acres) burn areas",
            "2014 Sand Fire burned near Highway 49 at county line",
            "2024 Crozier Fire burned northeast toward Georgetown",
            "Semi-urban density transitions rapidly to rural/wildland within 1-2 miles",
            "El Dorado County government services concentrated in Placerville/Diamond Springs",
            "Gateway community for Highway 50 corridor eastbound to Pollock Pines and Tahoe",
        ],
        "elevation_range_ft": [1500, 2200],
        "wui_exposure": "high",
        "historical_fires": [
            {
                "name": "Sand Fire",
                "year": 2014,
                "acres": 3800,
                "details": (
                    "Ignited near Highway 49 and Sand Ridge Road at the Amador-El "
                    "Dorado county line. Burned 3,800 acres of grassland and timber. "
                    "Destroyed 13 homes and 38 outbuildings. Forced 606 voluntary "
                    "and 477 mandatory evacuations (1,083 total). Demonstrated fire "
                    "spread potential in the dry grass and oak woodland fuels at the "
                    "lower-elevation WUI edge."
                ),
            },
            {
                "name": "Crozier Fire",
                "year": 2024,
                "acres": 1960,
                "details": (
                    "Arson fire ignited Aug 7 near Slate Mountain. Burned 1,960 acres "
                    "between the Caldor and Mosquito Fire burn scars northeast of "
                    "Diamond Springs. Forced evacuations in Garden Valley, Georgetown, "
                    "and surrounding areas. No structures destroyed. Diamond Springs "
                    "El Dorado County shelter at 6435 Capitol Ave was activated."
                ),
            },
            {
                "name": "Caldor Fire (nearby threat)",
                "year": 2021,
                "acres": 221835,
                "details": (
                    "Burned 221,835 acres east of Diamond Springs in El Dorado, "
                    "Amador, and Alpine counties. While Diamond Springs was not directly "
                    "in the fire's path, the fire burned within 15-20 miles of the "
                    "community and a westward shift in wind could have pushed the fire "
                    "toward the Placerville/Diamond Springs area. Forced extended "
                    "closure of Highway 50, affecting Diamond Springs as a gateway "
                    "community."
                ),
            },
            {
                "name": "King Fire (nearby threat)",
                "year": 2014,
                "acres": 97717,
                "details": (
                    "Arson fire that burned 97,717 acres in the Eldorado National "
                    "Forest east of Diamond Springs. While burning mostly in NF "
                    "lands, the fire demonstrated the potential for large, fast-moving "
                    "fires in the forests immediately upslope of the community."
                ),
            },
        ],
        "evacuation_routes": [
            {
                "route": "Highway 49 / Pleasant Valley Road to Highway 50",
                "direction": "W/NW",
                "lanes": 2,
                "bottleneck": (
                    "Primary route connecting Diamond Springs to Highway 50 and "
                    "Placerville. 2-lane in Diamond Springs area with moderate "
                    "traffic volume. Merges with Highway 50 which provides 4-lane "
                    "divided highway access westbound toward Sacramento. Intersection "
                    "congestion during peak evacuation."
                ),
                "risk": (
                    "Moderate. Route is at lower elevation and passes through less "
                    "densely forested terrain. However, grass fires along Highway 49 "
                    "could threaten the corridor, as demonstrated by the Sand Fire."
                ),
            },
            {
                "route": "Highway 49 southbound toward Plymouth / Amador County",
                "direction": "S",
                "lanes": 2,
                "bottleneck": (
                    "2-lane highway heading south through El Dorado and Amador "
                    "counties. Winding, rural road through grass and oak woodland. "
                    "Lower traffic volume but limited capacity."
                ),
                "risk": (
                    "Moderate. Passes through fire-prone grass/oak terrain. The "
                    "Sand Fire burned near this corridor in 2014."
                ),
            },
            {
                "route": "Highway 50 westbound from Placerville",
                "direction": "W",
                "lanes": 4,
                "bottleneck": (
                    "4-lane divided highway from Placerville westbound toward "
                    "El Dorado Hills and Sacramento. Primary high-capacity "
                    "evacuation route. Accessible via surface streets through "
                    "Placerville (~3 miles from Diamond Springs center)."
                ),
                "risk": (
                    "Low to moderate. Highway 50 west of Placerville provides "
                    "good capacity and leads away from the forest. However, the "
                    "3-mile surface street connection through Placerville can "
                    "congest during mass evacuation."
                ),
            },
        ],
        "fire_spread_characteristics": {
            "primary_wind_regime": (
                "Afternoon upslope thermal winds from the Sacramento Valley push "
                "fire from SW to NE, from the lower grass/oak zone into the forest "
                "zone. NE foehn events reverse the pattern, pushing fire from the "
                "forest downslope toward Diamond Springs. The lower-elevation "
                "position (~1,800 ft) means Diamond Springs is in the path of "
                "downslope-driven fires running out of the Eldorado NF."
            ),
            "critical_corridors": [
                "Highway 49 corridor (N-S -- grass/oak fire spread axis)",
                "Weber Creek drainage (N -- connects forest fuels to town edge)",
                "Eldorado NF boundary (E -- continuous forest fuel bed within 1-2 mi)",
                "Pleasant Valley (S/SE -- open grassland enabling rapid spread toward community)",
            ],
            "rate_of_spread_potential": (
                "Very high in grass/oak fuels at this elevation (80-200 chains/hr "
                "in wind-driven grass fires). The 2014 Sand Fire demonstrated rapid "
                "spread through this fuel type. Lower in mixed conifer (20-50 "
                "chains/hr) but crown fire potential exists on steeper slopes to "
                "the east. The primary risk is a fast-moving grass fire from the "
                "south/southeast or a forest fire running downslope from the east."
            ),
            "spotting_distance": (
                "0.5-1.5 miles in grass/brush fuels. Longer (1-3 miles) from "
                "timber fires running downslope from the Eldorado NF. The WUI "
                "edge position means ember showers from forest fires can reach "
                "residential structures even if the main fire front is still in "
                "the forest."
            ),
        },
        "infrastructure_vulnerabilities": {
            "water_system": (
                "El Dorado Irrigation District (EID) serves Diamond Springs. "
                "Adequate water infrastructure for normal operations. District "
                "headquarters and animal services shelter are located in Diamond "
                "Springs, making it a hub for emergency operations."
            ),
            "power": (
                "PG&E distribution with overhead lines in rural/WUI areas. Subject "
                "to PSPS de-energization. Lower-elevation location means less "
                "frequent PSPS than higher-elevation communities but still affected "
                "during major wind events."
            ),
            "communications": (
                "Good cell and internet coverage in the semi-urban Diamond Springs "
                "area. Degrades in rural areas east of town toward the NF boundary. "
                "El Dorado County emergency notification systems cover the area."
            ),
            "medical": (
                "Marshall Medical Center in Placerville (~3 miles) provides "
                "hospital-level care. Diamond Springs Fire Protection District "
                "stations at 501 Pleasant Valley Rd and other locations provide "
                "rapid first response. Better medical access than most foothill "
                "communities."
            ),
        },
        "demographics_risk_factors": {
            "population": 11037,
            "seasonal_variation": (
                "Modest variation. Diamond Springs functions primarily as a "
                "residential/commercial area for Placerville commuters. Some "
                "increase from Highway 50 corridor recreation traffic in summer."
            ),
            "elderly_percentage": "~18% age 65+",
            "mobile_homes": (
                "Mobile and manufactured homes present, particularly in rural "
                "areas at the WUI edge. These homes are most vulnerable to ember "
                "attack from wildland fires approaching from the east."
            ),
            "special_needs_facilities": (
                "El Dorado County services in Placerville/Diamond Springs area "
                "include senior services and the county shelter. Better "
                "institutional support than most foothill communities due to "
                "proximity to Placerville county seat."
            ),
        },
    },

    # =========================================================================
    # SONOMA / NAPA WINE COUNTRY
    # =========================================================================

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
    # LAKE COUNTY / MENDOCINO
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

    # =========================================================================
    # FAR NORTHERN CA
    # =========================================================================

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

    # =========================================================================
    # CENTRAL SIERRA / YOSEMITE GATEWAY
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

    # =========================================================================
    # SANTA CRUZ MOUNTAINS
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
    # LA BASIN / SAN GABRIEL FOOTHILLS
    # =========================================================================

    "malibu_ca": {
        "center": (34.0259, -118.7798),
        "elevation_ft": 40,
        "terrain_notes": (
            "27-mile coastal strip backed by the Santa Monica Mountains, population "
            "~10,300 (median age 50.7). Burns on a ~10-15 year cycle: 1993, 2007, "
            "2018, 2024, 2025. PCH is the ONLY east-west through-route and reduces "
            "to one lane in places; during Woolsey Fire (2018) and Palisades Fire "
            "(2025), PCH gridlocked completely and residents abandoned cars, some "
            "fleeing to the ocean. Roughly 200 abandoned vehicles had to be "
            "bulldozed off PCH during the Palisades Fire to clear access for "
            "engines. North-south canyon roads (Malibu Canyon Rd, Kanan Dume Rd, "
            "Las Virgenes Rd, Topanga Canyon Blvd) each connect PCH to US-101 but "
            "are narrow 2-lane mountain roads that close during fire events -- "
            "during Franklin Fire (Dec 2024), Malibu Canyon Rd and PCH were both "
            "closed simultaneously, trapping residents. "
            "\n\n"
            "Terrain is dominated by steep chaparral-covered canyons that run "
            "north-to-south from the Santa Monica Mountains ridgeline (up to "
            "3,111 ft at Saddle Peak) down to the coast. Each canyon acts as a "
            "fire chimney during Santa Ana events: NE winds accelerate through "
            "the canyons, pre-heating fuel on the lee slopes. Key fire corridors: "
            "Topanga Canyon, Malibu Canyon, Corral Canyon, Solstice Canyon, "
            "Santa Ynez Canyon, Las Virgenes Canyon, and Latigo Canyon. Woolsey "
            "Fire (2018) burned from Simi Valley to the Pacific Ocean in roughly "
            "36 hours, crossing US-101 and consuming 96,949 acres with 50-60 mph "
            "sustained winds (gusts 70+ mph). 1,643 structures destroyed, 400+ "
            "in Malibu proper. Fire reached the coast through multiple canyons "
            "simultaneously. "
            "\n\n"
            "Franklin Fire (Dec 9, 2024) ignited on Malibu Canyon Rd at 11 PM, "
            "burned 4,037 acres in central Malibu, destroyed 20 structures. "
            "~3,000 people sheltered in place at Pepperdine University in "
            "fireproofed buildings -- evacuation was impossible due to PCH "
            "congestion. Pepperdine's shelter-in-place protocol is unique in "
            "SoCal: campus was purpose-built with steel, concrete, stucco, and "
            "no exposed wood. "
            "\n\n"
            "Water infrastructure: LADWP serves eastern Malibu; Las Virgenes "
            "Municipal Water District serves central/western Malibu. Both systems "
            "rely on pumped pressure to hilltop tanks that drain rapidly under "
            "firefighting demand. During Woolsey Fire, water supply to parts of "
            "Malibu was threatened. No cell towers exist in many Malibu canyon "
            "areas; during fires, cell service drops entirely, cutting off "
            "evacuation alerts. LAFD Station 71 (Malibu) and LACoFD Station 88 "
            "(in the mountains) cover 27 miles of coastline -- response times "
            "can exceed 15 minutes to remote canyon homes."
        ),
        "danger_quadrants": ["north", "northeast", "east"],
        "safe_quadrants": ["south"],
        "key_features": [
            {
                "name": "Santa Monica Mountains",
                "bearing": "N",
                "distance_mi": 1,
                "type": "mountain",
                "notes": (
                    "Chaparral-covered range rising to 3,111 ft (Saddle Peak). "
                    "Ridgeline runs E-W; N-S canyons cut perpendicular, each a "
                    "fire chimney during Santa Ana events. 88% of the Santa Monica "
                    "Mountains NRA (>150,000 acres) burned in Woolsey Fire 2018."
                ),
            },
            {
                "name": "Malibu Canyon",
                "bearing": "N",
                "distance_mi": 2,
                "type": "major_canyon",
                "notes": (
                    "Primary N-S fire corridor from San Fernando Valley to coast. "
                    "Malibu Canyon Road is 2-lane, closes during fire events. "
                    "Franklin Fire (Dec 2024) ignited on this road. Fire can "
                    "transit the full 7-mile canyon in under 2 hours in Santa Ana."
                ),
            },
            {
                "name": "Corral Canyon",
                "bearing": "NE",
                "distance_mi": 1,
                "type": "canyon",
                "notes": (
                    "Steep, narrow fire corridor to coast. Corral Canyon Fire "
                    "(2007) destroyed 53 structures in hours. Canyon funnels "
                    "Santa Ana winds directly onto coastal homes."
                ),
            },
            {
                "name": "Solstice Canyon",
                "bearing": "NE",
                "distance_mi": 3,
                "type": "canyon",
                "notes": (
                    "N-S canyon ~1 mile east of Point Dume. Has burned repeatedly "
                    "-- historic Tropical Terrace (built to withstand fire) was "
                    "destroyed in 2007 Corral Canyon Fire. No road access beyond "
                    "trailhead; fire arrives without warning."
                ),
            },
            {
                "name": "Latigo Canyon",
                "bearing": "N/NE",
                "distance_mi": 5,
                "type": "canyon",
                "notes": (
                    "Remote canyon with scattered homes on ridgelines. Latigo "
                    "Canyon Road is single-lane in sections. Woolsey Fire burned "
                    "through here in 2018; homes had no defensible space."
                ),
            },
            {
                "name": "PCH / Hwy 1",
                "bearing": "E-W",
                "type": "access_route",
                "notes": (
                    "Only coastal through-route for 27 miles. 2-4 lanes, narrows "
                    "at multiple points. Gridlocked during every major fire. "
                    "During Palisades Fire (2025), ~200 abandoned cars bulldozed "
                    "off road. Residents fled into the ocean when PCH was "
                    "impassable. Post-Palisades Fire reduced to 1 lane each way "
                    "for months during recovery."
                ),
            },
            {
                "name": "Kanan Dume Road",
                "bearing": "N",
                "distance_mi": 8,
                "type": "access_route",
                "notes": (
                    "2-lane mountain road connecting PCH to US-101. 7+ miles of "
                    "switchbacks through chaparral. Only western escape route to "
                    "the Valley if PCH is blocked. Closes in fire conditions."
                ),
            },
            {
                "name": "LADWP / Las Virgenes Water Systems",
                "bearing": "N/A",
                "type": "infrastructure",
                "notes": (
                    "Hilltop gravity tanks drain rapidly under firefighting demand. "
                    "Pump stations lose suction when trunk line pressure drops. "
                    "No redundancy -- if one pump station fails, entire pressure "
                    "zone goes dry. Woolsey Fire threatened Malibu water supply."
                ),
            },
            {
                "name": "Pepperdine University",
                "bearing": "N",
                "distance_mi": 3,
                "type": "shelter_in_place",
                "notes": (
                    "Only viable shelter-in-place site in Malibu. Purpose-built "
                    "with fireproof materials. 3,000 sheltered during Franklin "
                    "Fire (Dec 2024). Campus has survived every fire since 1985. "
                    "Defensible space maintained by professional crews."
                ),
            },
        ],
        "historical_fires": [
            "Palisades Fire 2025 (burned into western Malibu, 6,837 total structures across fire)",
            "Franklin Fire Dec 2024 (4,037 acres, 20 structures, Pepperdine shelter-in-place)",
            "Woolsey Fire 2018 (96,949 acres, 1,643 structures, 400+ in Malibu, 3 killed)",
            "Corral Canyon Fire 2007 (53 structures destroyed)",
            "Old Topanga Fire 1993 (18,000 acres, 359 homes, 3 killed)",
        ],
        "wui_class": "extreme",
        "population": 10298,
        "median_home_value": 3200000,
        "post_2025_status": (
            "Palisades Fire destroyed beach houses from Topanga to Carbon Beach. "
            "Western Malibu heavily damaged. PCH reduced to 1 lane each direction "
            "for months. Insurance crisis: multiple carriers pulling out of Malibu "
            "zip codes. Rebuilding hampered by coastal development permit requirements."
        ),
    },

    "pacific_palisades_ca": {
        "center": (34.0472, -118.5268),
        "elevation_ft": 300,
        "terrain_notes": (
            "Affluent LA neighborhood of ~23,000-29,000 residents (25.8% over 65) "
            "wedged between Santa Monica Mountains and the Pacific. Palisades Fire "
            "(Jan 7-31, 2025) was the most destructive fire in LA history: 6,837 "
            "structures destroyed, 12 killed, 23,448 acres. Fire started ~10:30 AM "
            "Jan 7 near Skull Rock trailhead on Temescal Ridge in Topanga State Park, "
            "possibly a rekindling of a Jan 1 fireworks-sparked brush fire (the "
            "'Lachman Fire'). Wind-driven spread rate: 5 football fields per minute "
            "at peak, growing from 10 acres to 200 acres in 20 minutes. Embers "
            "transported 2-3 miles ahead of the fire front in every direction, "
            "creating simultaneous spot fires that overwhelmed suppression. "
            "\n\n"
            "ONLY 3 EVACUATION ROUTES for ~28,000 people: Sunset Blvd (east), "
            "Chautauqua Blvd (south to PCH), and Temescal Canyon Rd (south to PCH). "
            "Pacific Palisades is in the worst 1% statewide for population-to-"
            "evacuation-route ratio. During the Palisades Fire, all three routes "
            "gridlocked within 30 minutes of evacuation orders. PCH was closed "
            "southbound at Temescal, routing all cars through the mandatory "
            "evacuation zone on Sunset -- directly toward the fire. Residents "
            "abandoned cars on Sunset Blvd and Palisades Drive; LAPD deployed ~140 "
            "officers but could not clear gridlock. Bulldozers removed ~200 "
            "abandoned vehicles. Some residents fled on foot. "
            "\n\n"
            "Terrain: three sides are steep brush-covered hillsides. Temescal "
            "Canyon, Santa Ynez Canyon, and Rustic Canyon are fire corridors "
            "that funnel directly into residential areas from the north. The "
            "Castellammare and Riviera neighborhoods sit on steep canyon walls "
            "with homes accessed by narrow, dead-end roads -- essentially "
            "indefensible during a wind-driven fire. Almost every structure north "
            "of Sunset Blvd was destroyed. "
            "\n\n"
            "WATER SYSTEM FAILURE: LADWP's three Palisades pumping stations "
            "depend on the Westgate Trunk Line. Firefighting demand (4x normal) "
            "plus residents leaving sprinklers/hoses running during evacuation "
            "collapsed trunk line pressure. Pump stations auto-shut-down due to "
            "insufficient suction. Three hilltop tanks drained without replenishment. "
            "By early morning Jan 8, all hydrants in the Palisades were dry. "
            "The Santa Ynez Reservoir (117M gallon capacity) had been emptied "
            "for repairs in Feb 2024 and was offline during the fire -- but "
            "state analysis concluded that even a full reservoir would not have "
            "maintained hydrant pressure under the demand. "
            "\n\n"
            "COMMUNICATIONS FAILURE: No cell towers exist in Pacific Palisades. "
            "The Green Mountain radio repeater site was shut down during the fire. "
            "LAPD officers could not reach dispatchers by radio and had to hand-"
            "deliver paper documents 20 miles to a Zuma Beach staging area. "
            "Residents with dead cell service could not receive evacuation alerts. "
            "LAFD and LAPD had no shared communications or unified command "
            "structure for the first critical hours. "
            "\n\n"
            "Santa Ana winds during Palisades Fire: sustained 40-60 mph, gusts "
            "80+ mph. Aerial firefighting was grounded. The fire created its own "
            "weather, with erratic wind shifts that drove fire in unexpected "
            "directions."
        ),
        "danger_quadrants": ["north", "northeast", "east", "west"],
        "safe_quadrants": ["south"],
        "key_features": [
            {
                "name": "Temescal Canyon",
                "bearing": "N",
                "distance_mi": 0.5,
                "type": "major_canyon",
                "notes": (
                    "Primary fire corridor into the Palisades. Palisades Fire "
                    "ignited near Skull Rock on the Temescal Ridge Trail. Canyon "
                    "funnels NE winds directly into the most densely built part "
                    "of the neighborhood. Temescal Canyon Rd is also a critical "
                    "evacuation route -- serves dual and conflicting purposes."
                ),
            },
            {
                "name": "Santa Ynez Canyon",
                "bearing": "N/NW",
                "distance_mi": 1,
                "type": "canyon",
                "notes": (
                    "Parallel fire corridor west of Temescal. Site of the offline "
                    "Santa Ynez Reservoir (117M gal, emptied Feb 2024 for repairs). "
                    "Drains into the Riviera neighborhood. Dense chaparral with "
                    "no fuel break between wildland and homes."
                ),
            },
            {
                "name": "Rustic Canyon",
                "bearing": "NE",
                "distance_mi": 1,
                "type": "canyon",
                "notes": (
                    "Deep, narrow canyon east of the Palisades. Single-lane access "
                    "road. Homes built on steep slopes with heavy tree canopy. "
                    "Fire spread through here during the Palisades Fire's eastward "
                    "advance. Many homes are architectural landmarks with no "
                    "defensible space."
                ),
            },
            {
                "name": "Topanga State Park",
                "bearing": "NW",
                "distance_mi": 1,
                "type": "wildland",
                "notes": (
                    "~11,000 acres of undeveloped chaparral immediately above "
                    "the Palisades. Palisades Fire ignited within the park. No "
                    "fuel management -- park service does not conduct prescribed "
                    "burns. This is the fuel source for every Palisades fire."
                ),
            },
            {
                "name": "Sunset Blvd",
                "bearing": "E-W",
                "type": "access_route",
                "notes": (
                    "Primary east-west evacuation route. 4 lanes. During Palisades "
                    "Fire, cars were routed east on Sunset directly through the "
                    "mandatory evacuation zone. Gridlocked within 30 minutes. "
                    "Homes burned on both sides of Sunset at Chautauqua. "
                    "Bulldozers needed to clear abandoned vehicles."
                ),
            },
            {
                "name": "Chautauqua Blvd",
                "bearing": "S",
                "type": "access_route",
                "notes": (
                    "Steep, narrow connector from Sunset Blvd to PCH. 2 lanes, "
                    "one of only 3 exits. Bottleneck at PCH intersection. "
                    "Homes burned at Sunset/Chautauqua corner during Palisades Fire."
                ),
            },
            {
                "name": "Temescal Canyon Road",
                "bearing": "S",
                "type": "access_route",
                "notes": (
                    "3rd evacuation route to PCH. PCH was closed southbound at "
                    "Temescal during the Palisades Fire, forcing northbound "
                    "Temescal traffic onto Sunset through the fire zone."
                ),
            },
            {
                "name": "LADWP Westgate Trunk Line / Pump Stations",
                "bearing": "N/A",
                "type": "infrastructure",
                "notes": (
                    "Three pump stations and three hilltop tanks serve all "
                    "Palisades hydrants. System failed by early Jan 8, 2025. "
                    "4x normal demand collapsed trunk line pressure; pumps "
                    "auto-shut; tanks drained. All hydrants went dry. "
                    "No redundant water source. Santa Ynez Reservoir was offline."
                ),
            },
            {
                "name": "SCE / LADWP Power Grid",
                "bearing": "N/A",
                "type": "ignition_source",
                "notes": (
                    "LADWP overhead lines run through Temescal and Rustic Canyons. "
                    "A second ignition point from downed power lines was alleged "
                    "in March 2025 lawsuits. Power loss cascaded through the "
                    "neighborhood, disabling evacuation alerts and well pumps."
                ),
            },
            {
                "name": "Castellammare / The Riviera",
                "bearing": "W/NW",
                "distance_mi": 0.5,
                "type": "residential_exposure",
                "notes": (
                    "Hilltop neighborhoods accessed by narrow, steep, dead-end "
                    "roads. Homes perched on canyon walls with no defensible space. "
                    "Near-total destruction during Palisades Fire. Evacuation "
                    "required descending to Sunset Blvd via single-lane switchbacks."
                ),
            },
        ],
        "historical_fires": [
            "Palisades Fire 2025 (12 killed, 6,837 structures, 23,448 acres, most destructive in LA history)",
            "Palisades Fire 2021 (contained at ~1 acre -- same general area)",
            "Woolsey Fire 2018 (burned nearby areas, 96,949 acres total)",
        ],
        "wui_class": "extreme",
        "population": 27000,
        "schools_in_fire_zone": [
            "Marquez Charter Elementary",
            "Canyon Charter Elementary",
            "Palisades Charter High School (2,991 students)",
        ],
        "post_2025_status": (
            "Near-total destruction north of Sunset Blvd. As of Jan 2026, 3,090 "
            "rebuild permits approved but few residents have returned. Insurance "
            "payout gap averages ~$600/sq ft below actual rebuild cost. State "
            "moratorium on policy cancellations expires Jan 2026. Rebuilt homes "
            "in VHFHSZ must meet CA wildfire building code (Class-A roof, ember-"
            "resistant vents/windows). LADWP committed to rebuilding Santa Ynez "
            "Reservoir and adding redundant trunk line. No plans to add cell towers."
        ),
    },

    "topanga_ca": {
        "center": (34.0394, -118.6015),
        "elevation_ft": 1100,
        "terrain_notes": (
            "Unincorporated canyon community of ~8,560 residents (2020 census) "
            "deep in the Santa Monica Mountains. ~3,200 residential dwellings, "
            "mostly wood-frame bungalows built before modern fire codes. Burns "
            "on a ~25-30 year cycle (25+ fires since 1925). The 1993 Old Topanga "
            "Fire killed 3, destroyed 359 homes, and drove from Mulholland to PCH "
            "in hours with 60 mph Santa Ana gusts. Average interval between major "
            "fires is 28 years per NPS; last major burn was 1993, meaning Topanga "
            "was statistically overdue when the Palisades Fire (2025) arrived. "
            "\n\n"
            "EVACUATION IS THE CORE PROBLEM: Topanga Canyon Blvd (SR-27) is the "
            "only through-road, running N-S through the entire canyon for ~8 miles. "
            "It narrows to a single lane in places (especially near the community "
            "center and the old bridge). Old Topanga Canyon Road is a secondary "
            "route but dead-ends at Mulholland and is itself a fire corridor. "
            "LA County Fire Dept has openly discussed that for an 8,000+ person "
            "community with a multi-hour evacuation window and a single road, "
            "shelter-in-place may be the only option if fire arrives too fast. "
            "During the 1993 fire, eastbound PCH gridlocked with evacuees -- "
            "traffic 'mercifully resolved before cars were overrun by flames.' "
            "Construction work on Topanga Canyon Blvd (underground cable "
            "installation) periodically reduces it to one lane, further "
            "degrading evacuation capacity. "
            "\n\n"
            "Palisades Fire (2025) burned through the lower portion of the "
            "Topanga community. Most homes near Topanga State Beach were "
            "destroyed. Fire also burned the La Costa and Rambla neighborhoods "
            "(same areas that burned in 1993) and crossed PCH to destroy beach "
            "houses from Topanga to Carbon Beach. Fire pushed north toward "
            "Old Topanga and Calabasas at Saddle Peak Rd. Topanga Canyon Blvd "
            "closed from Grand View Drive to PCH for months. "
            "\n\n"
            "Terrain: community sits in the bottom and on the walls of a deep "
            "V-shaped canyon. Homes are built on steep slopes accessed by narrow "
            "private roads, many unpaved. Canyon walls are dense chaparral and "
            "coastal sage scrub. The canyon acts as a chimney during Santa Ana "
            "events -- winds accelerate through the narrows and pre-heat fuel "
            "on both walls. No defensible perimeter exists around any part of "
            "the community. Topanga State Park (11,000+ acres) and Santa Monica "
            "Mountains NRA surround the community on all sides. "
            "\n\n"
            "Topanga is a FireWise community with active brush clearance programs "
            "run by the Topanga Coalition for Emergency Preparedness (TCEP). "
            "But defensible space is limited by terrain: many homes have less "
            "than 30 feet of clearance to wildland fuel on steep slopes. "
            "No fire stations within the canyon; nearest LACoFD stations are "
            "at the canyon mouth (PCH) and at Mulholland."
        ),
        "danger_quadrants": ["north", "east", "west", "northeast", "south"],
        "safe_quadrants": [],
        "key_features": [
            {
                "name": "Topanga Canyon",
                "bearing": "N-S",
                "type": "major_canyon",
                "notes": (
                    "Deep V-shaped canyon, ~8 miles long. Acts as a fire chimney "
                    "during Santa Ana events. Winds accelerate through narrows, "
                    "pre-heating fuel on both canyon walls. Homes built on slopes "
                    "throughout. No defensible perimeter. Old Topanga Fire (1993) "
                    "swept the full canyon in hours."
                ),
            },
            {
                "name": "Old Topanga Canyon Road",
                "bearing": "NE",
                "distance_mi": 1,
                "type": "canyon",
                "notes": (
                    "Secondary canyon and road that connects to Mulholland Hwy. "
                    "Not a viable alternate evacuation route -- dead-ends at "
                    "Mulholland and is itself a fire corridor. Palisades Fire "
                    "pushed through here toward Calabasas."
                ),
            },
            {
                "name": "Santa Monica Mountains NRA",
                "bearing": "all",
                "type": "wildland",
                "notes": (
                    "Community is surrounded on all sides by undeveloped chaparral "
                    "and coastal sage scrub. Topanga State Park (11,000+ acres) "
                    "to the east, NRA lands to the north and west. No fuel "
                    "management by NPS -- no prescribed burns. 88% of SMMNRA "
                    "burned in Woolsey Fire (2018)."
                ),
            },
            {
                "name": "Saddle Peak / Stunt Road Ridge",
                "bearing": "N",
                "distance_mi": 3,
                "type": "ridgeline",
                "notes": (
                    "Highest point in Santa Monica Mtns (3,111 ft). Ridgeline "
                    "separates Topanga from San Fernando Valley. Fires crest "
                    "this ridge and run downslope into the canyon. Palisades "
                    "Fire burned to Saddle Peak Rd."
                ),
            },
            {
                "name": "Topanga Canyon Blvd (SR-27)",
                "bearing": "N-S",
                "type": "access_route",
                "notes": (
                    "Only road in or out for 8,500+ residents. 8 miles of winding "
                    "2-lane road that narrows to 1 lane in places. Multi-hour "
                    "full-canyon evacuation. LACoFD has discussed shelter-in-place "
                    "as the only viable option if fire moves too fast. During "
                    "Palisades Fire (2025), road was closed from Grand View Dr "
                    "to PCH for months."
                ),
            },
            {
                "name": "La Costa / Rambla neighborhoods",
                "bearing": "S",
                "distance_mi": 2,
                "type": "residential_exposure",
                "notes": (
                    "Lower canyon neighborhoods near PCH. Burned in 1993 Old "
                    "Topanga Fire and again in 2025 Palisades Fire. Homes rebuilt "
                    "after 1993 were destroyed again 32 years later. Many were "
                    "non-compliant with modern fire codes."
                ),
            },
        ],
        "historical_fires": [
            "Palisades Fire 2025 (destroyed lower Topanga, beach houses Topanga to Carbon Beach, pushed to Saddle Peak)",
            "Woolsey Fire 2018 (burned surrounding wildland, 88% of SMMNRA)",
            "Old Topanga Fire 1993 (18,000 acres, 359 homes, 3 killed, Mulholland to PCH in hours)",
            "Topanga Fire 1958 (74 homes destroyed)",
        ],
        "wui_class": "extreme",
        "population": 8560,
        "post_2025_status": (
            "Lower Topanga heavily damaged by Palisades Fire. Topanga Canyon Blvd "
            "closed for months. Homes in La Costa/Rambla that were rebuilt after "
            "1993 were destroyed again. TCEP and FireWise programs remain active "
            "but terrain limits defensible space. LACoFD shelter-in-place planning "
            "underway for future events. No new evacuation routes planned."
        ),
    },

    "altadena_ca": {
        "center": (34.1897, -118.1312),
        "elevation_ft": 1358,
        "terrain_notes": (
            "Unincorporated foothill community of ~42,000 residents directly below "
            "the San Gabriel Mountains front. Diverse demographics: 27% Latino, "
            "18% Black, significant Asian population. Historically one of the "
            "largest Black homeownership communities in LA County (Black "
            "homeownership rate >80%, nearly double national average). Black "
            "population peaked at 43% in 1980, declined to 18% by 2020, with "
            "20% decline in BIPOC residents in west Altadena from 2015-2023 "
            "even before the fire. 57% of Black homeowners are over 65. "
            "\n\n"
            "EATON FIRE (Jan 7-31, 2025): 2nd most destructive fire in CA "
            "history. 9,418 structures destroyed, 1,073 damaged, 17 civilians "
            "killed, 14,021 acres. Fire ignited at 6:18 PM Jan 7 near SCE "
            "transmission towers in Eaton Canyon (coordinates N34.186, W118.094). "
            "Three SCE 220kV transmission structures in the preliminary origin "
            "area: M6T1 (Eagle Rock-Mesa line), M24T3 (Mesa-Vincent line), and "
            "M16T1 (decommissioned Mesa-Sylmar line). Surveillance video captured "
            "molten material falling from a tower onto dry brush in high winds. "
            "The US DOJ sued SCE in Sep 2025 alleging their equipment caused "
            "the fire. SCE disputes. "
            "\n\n"
            "FIRE BEHAVIOR: Hurricane-force Santa Ana winds (gusts to 90+ mph) "
            "drove fire out of Eaton Canyon and downslope into neighborhoods. "
            "From 400 acres at midnight to 10,000+ acres by 10:30 AM Jan 8. "
            "Embers carried well ahead of the fire front. Fire initially spread "
            "east and south, then a critical wind shift around 3 AM Jan 8 drove "
            "fire westward across Lake Avenue into west Altadena. Roof fires "
            "reported west of Lake Ave as early as 10:50 PM Jan 7 (embers), "
            "but the main fire front crossed Lake Ave between 1-3 AM. By 3:17 AM, "
            "fire was burning house-to-house in urban west Altadena. "
            "\n\n"
            "EVACUATION FAILURE: Lake Avenue became the dividing line between "
            "life and death. East Altadena received evacuation orders early "
            "(~9:20 PM Jan 7). West Altadena -- the historically Black "
            "neighborhood -- received first evacuation alert after 3:25 AM "
            "Jan 8, more than 8 hours after ignition and 4+ hours after "
            "authorities knew fire was spreading west. A second order at 5:42 AM. "
            "All but 1 of the 17 confirmed dead lived west of Lake Avenue. "
            "After-action reports cite 'outdated policies, inconsistent practices "
            "and communications vulnerabilities' in LA County's alert system. "
            "\n\n"
            "WATER SYSTEM: Three 1-million-gallon storage tanks serve Altadena's "
            "hilltop hydrants via gravity. All three ran dry overnight Jan 7-8 "
            "due to simultaneous demand from firefighters and residents. By "
            "midday Jan 8: 'We're up at Lake and Altadena, and all the hydrants "
            "up here are dead' (firefighter radio traffic). Power loss disabled "
            "some pump stations that refill the tanks. System was never designed "
            "for block-after-block simultaneous structure fire. "
            "\n\n"
            "TERRAIN: San Gabriel Mountains rise to 10,000+ ft directly above "
            "town. Three major canyons drain from the mountains directly into "
            "residential areas: Eaton Canyon (ignition zone), Rubio Canyon "
            "(parallel corridor ~1 mi NE), and Millard Canyon (~1.5 mi NW). "
            "Each canyon channels Santa Ana winds and provides zero fuel break "
            "between wildland and homes. The mountain front is steep chaparral "
            "transitioning to timber at higher elevations. Station Fire (2009) "
            "burned 160,577 acres in the range directly above Altadena."
        ),
        "danger_quadrants": ["north", "northeast", "northwest"],
        "safe_quadrants": ["south"],
        "key_features": [
            {
                "name": "Eaton Canyon",
                "bearing": "N",
                "distance_mi": 1,
                "type": "major_canyon",
                "notes": (
                    "Eaton Fire ignition zone. Deep canyon with SCE 220kV "
                    "transmission lines running through it (3 towers in "
                    "preliminary origin area). Canyon channels Santa Ana winds "
                    "directly into residential Altadena. Eaton Canyon Nature "
                    "Area (190 acres) provides no fuel break -- chaparral "
                    "is continuous from mountain to neighborhood. Fire ran "
                    "down-canyon at speeds exceeding 1 mile in 15 minutes."
                ),
            },
            {
                "name": "Rubio Canyon",
                "bearing": "NE",
                "distance_mi": 1,
                "type": "canyon",
                "notes": (
                    "Parallel fire corridor to Eaton Canyon. Steep-walled, "
                    "densely vegetated. Drains directly into east Altadena "
                    "residential areas. No fuel break. Site of historic "
                    "Rubio Canyon resort (destroyed by flood 1909)."
                ),
            },
            {
                "name": "Millard Canyon",
                "bearing": "NW",
                "distance_mi": 1.5,
                "type": "canyon",
                "notes": (
                    "Western fire corridor from San Gabriels into the Altadena/"
                    "La Canada border area. Steep, narrow, heavily vegetated."
                ),
            },
            {
                "name": "San Gabriel Mountains front",
                "bearing": "N",
                "distance_mi": 2,
                "type": "mountain",
                "notes": (
                    "10,064 ft (Mt Wilson) directly above town. Extremely steep "
                    "mountain front with chaparral/scrub transitioning to "
                    "conifer at ~5,000 ft. Station Fire (2009) burned 160,577 "
                    "acres in this range, threatening Altadena. Fuel loads "
                    "have largely recovered since 2009."
                ),
            },
            {
                "name": "SCE 220kV Transmission Corridor",
                "bearing": "N",
                "distance_mi": 1,
                "type": "ignition_source",
                "notes": (
                    "Multiple 220kV lines traverse Eaton Canyon: Eagle Rock-Mesa, "
                    "Mesa-Vincent No. 1 and 2, Goodrich-Gould, and decommissioned "
                    "Mesa-Sylmar. DOJ alleges SCE equipment caused Eaton Fire. "
                    "Surveillance video shows molten material falling from tower "
                    "onto brush. SCE began removing towers near origin point "
                    "in 2025."
                ),
            },
            {
                "name": "Lake Avenue corridor",
                "bearing": "N-S",
                "type": "access_route",
                "notes": (
                    "Major N-S arterial that divided the Eaton Fire's impact zone. "
                    "East of Lake: evacuated early, lower fatalities. West of Lake: "
                    "alerts delayed 4+ hours, 16 of 17 fatalities. Also a key "
                    "evacuation and fire apparatus access route. 4 lanes."
                ),
            },
            {
                "name": "Fair Oaks Avenue",
                "bearing": "N-S",
                "type": "access_route",
                "notes": (
                    "Western N-S evacuation route. Entry/exit point at Fair Oaks "
                    "and Harriet St. Closed from E Montana St to Loma Alta Dr "
                    "during fire. 2 lanes in residential sections."
                ),
            },
            {
                "name": "Lincoln Avenue",
                "bearing": "N-S",
                "type": "access_route",
                "notes": (
                    "N-S route through west Altadena. Closed from Woodbury Rd to "
                    "Loma Alta Dr during fire. Entry/exit at W Altadena Dr and "
                    "Lincoln Ave. Critical for west Altadena evacuation but "
                    "alerts to use it came hours too late."
                ),
            },
            {
                "name": "Altadena Water System (3x 1M-gallon tanks)",
                "bearing": "N/A",
                "type": "infrastructure",
                "notes": (
                    "Three 1-million-gallon gravity tanks serve hilltop hydrants. "
                    "All three ran dry overnight Jan 7-8. Power loss disabled "
                    "pumps that refill tanks. Firefighter radio: 'all the hydrants "
                    "up here are dead.' System not designed for neighborhood-scale "
                    "simultaneous structure fire."
                ),
            },
        ],
        "historical_fires": [
            "Eaton Fire 2025 (17 killed, 9,418 structures destroyed, 14,021 acres, 2nd most destructive in CA)",
            "Station Fire 2009 (160,577 acres, 2 firefighter deaths, threatened Altadena)",
            "Altadena Fire 1993 (threatened community)",
        ],
        "wui_class": "extreme",
        "population": 42000,
        "demographics_notes": (
            "61% of Black households were in the Eaton Fire perimeter vs 50% of "
            "non-Black households. 48% of Black households destroyed/major damage "
            "vs 37% non-Black. ~2,800 Black households evacuated on Day 1. "
            "Post-fire: corporate land acquisition surged -- nearly half of 94 "
            "post-fire sales (Feb-Apr 2025) went to corporate entities vs 5 of "
            "95 sales in same period prior year. Displacement crisis for elderly "
            "Black homeowners with insufficient insurance."
        ),
        "post_2025_status": (
            "Fewer than 20% of destroyed homes had rebuild permits issued as of "
            "late 2025. State fire maps only cover a fraction of the burn area "
            "as VHFHSZ -- meaning >3,500 homes CAN be rebuilt without wildfire "
            "building code compliance. Starting 2026, 'high' hazard zones will "
            "require wildfire codes, adding ~1,000 properties. Lumber tariffs "
            "and immigration enforcement reducing construction labor pool are "
            "raising rebuild costs. Insurance crisis: many carriers pulling out "
            "of foothill zip codes."
        ),
    },

    "la_canada_flintridge_ca": {
        "center": (34.1992, -118.1879),
        "elevation_ft": 1188,
        "terrain_notes": (
            "City of ~20,100 residents in the western San Gabriel foothills, "
            "adjacent to and immediately west of Altadena. Median household "
            "income $221,451. Demographics: 53.5% White, 31% Asian, median age "
            "45.2. Home to NASA's Jet Propulsion Laboratory (eastern end of city). "
            "Elevation ranges from 970 ft at Devil's Gate Dam (Arroyo Seco) to "
            "2,400 ft at the mountain front east of Pickens Canyon, with city "
            "limits extending to 3,440 ft along Mt Lukens Road. Entire northern "
            "boundary is Angeles National Forest (657,000 acres). Designated "
            "Very High Fire Hazard Severity Zone due to topography and abundance "
            "of California Live Oak. "
            "\n\n"
            "STATION FIRE (Aug 26 - Oct 16, 2009): Largest modern LA County "
            "wildfire. Ignited near Angeles Crest Highway Ranger Station, burned "
            "160,577 acres in the San Gabriel Mountains directly above the city. "
            "2 firefighter deaths. Threatened 12,000 structures across the "
            "foothill communities. Fire burned in both SE and NW directions "
            "simultaneously from Angeles Crest Hwy. Some growth areas hadn't "
            "burned in 50 years -- deep fuel loads. Mandatory evacuation of "
            "parts of La Canada Flintridge; fire threatened 500 homes. "
            "\n\n"
            "EATON FIRE (Jan 2025): Entire city of La Canada Flintridge placed "
            "under mandatory evacuation at ~5 AM Jan 8, 2025, about 11 hours "
            "after ignition. All ~20,000 residents ordered out. JPL was closed "
            "through Jan 13; LACoFD conducted fire-retardant drops to protect "
            "the facility. However, the fire did NOT enter La Canada Flintridge -- "
            "no structures were damaged. The city's aggressive fuel modification "
            "program and the wind pattern (primarily eastward into Altadena) "
            "spared it. Residents returned Jan 11. But the evacuation exposed "
            "the city's vulnerability: 20,000 people on a handful of E-W routes "
            "(Foothill Blvd, Angeles Crest Hwy) with the mountains cutting off "
            "northern escape. "
            "\n\n"
            "TERRAIN: Three key canyons drain from the San Gabriels through "
            "or near the city: Pickens Canyon (NE, fire corridor into upper "
            "residential areas at Ocean View Blvd), Gould Canyon (N, parallel "
            "corridor), and the Arroyo Seco (W boundary, major drainage from "
            "San Gabriels through Pasadena to LA River). Devil's Gate Dam at "
            "the Arroyo Seco is a critical debris basin -- post-fire debris "
            "flows from the Station Fire (2009) deposited massive sediment loads "
            "here. The mountain front is extremely steep, with chaparral and "
            "Live Oak grading to conifer above ~5,000 ft. Fuel loads above "
            "La Canada have regrown significantly since the 2009 Station Fire "
            "(16 years of growth). "
            "\n\n"
            "Angeles Crest Highway (SR-2) runs north from the city into the "
            "Angeles National Forest -- this is both an ignition corridor "
            "(Station Fire started along it) and the only route to mountain "
            "communities. The highway also brings recreational traffic into "
            "the forest, creating ignition risk from vehicles and humans. "
            "La Canada maintains an aggressive fire safety program including "
            "mandatory brush clearance, fire-resistant landscaping requirements, "
            "and community-wide evacuation planning."
        ),
        "danger_quadrants": ["north", "northeast", "east"],
        "safe_quadrants": ["south", "southwest"],
        "key_features": [
            {
                "name": "Angeles National Forest",
                "bearing": "N",
                "distance_mi": 0.5,
                "type": "wildland",
                "notes": (
                    "657,000-acre National Forest directly above city. Station "
                    "Fire (2009) burned 160,577 acres in this forest. Fuel loads "
                    "have regrown for 16 years since. No prescribed burns in "
                    "most areas due to air quality restrictions and terrain. "
                    "The interface is abrupt -- homes meet forest with minimal "
                    "transition zone."
                ),
            },
            {
                "name": "Pickens Canyon",
                "bearing": "NE",
                "distance_mi": 0.5,
                "type": "canyon",
                "notes": (
                    "Fire corridor from San Gabriels into upper La Canada "
                    "neighborhoods at Ocean View Blvd (2,400 ft elevation). "
                    "Steep-walled, densely vegetated. Drains directly into "
                    "residential areas. City's highest and most exposed homes "
                    "are at the mouth of this canyon."
                ),
            },
            {
                "name": "Gould Canyon",
                "bearing": "N",
                "distance_mi": 0.5,
                "type": "canyon",
                "notes": (
                    "Parallel fire corridor to Pickens Canyon. Narrow, steep, "
                    "with dense chaparral. Both canyons channel Santa Ana winds "
                    "into the city's northern residential tier."
                ),
            },
            {
                "name": "Arroyo Seco",
                "bearing": "W",
                "distance_mi": 1,
                "type": "major_canyon",
                "notes": (
                    "Major drainage from San Gabriels through Pasadena to LA "
                    "River. Devil's Gate Dam at the mouth is a critical debris "
                    "basin. Post-fire debris flows are a secondary hazard -- "
                    "Station Fire deposited massive sediment here. Western "
                    "boundary of the city. Fire in the Arroyo could cut off "
                    "Foothill Blvd access to Pasadena."
                ),
            },
            {
                "name": "Angeles Crest Highway (SR-2)",
                "bearing": "N",
                "type": "access_route",
                "notes": (
                    "Main route into Angeles NF and ignition corridor. Station "
                    "Fire (2009) started along this highway. Brings heavy "
                    "recreational traffic creating ignition risk. Also the only "
                    "route to mountain communities -- during Station Fire, "
                    "it was the primary fire approach vector."
                ),
            },
            {
                "name": "Foothill Blvd (SR-210 corridor)",
                "bearing": "E-W",
                "type": "access_route",
                "notes": (
                    "Primary E-W evacuation route along the base of the foothills. "
                    "Connects to I-210 freeway. During Eaton Fire evacuation, "
                    "20,000 residents funneled onto this corridor. Only viable "
                    "route -- mountains block northern escape."
                ),
            },
            {
                "name": "NASA Jet Propulsion Laboratory",
                "bearing": "E",
                "distance_mi": 1,
                "type": "critical_facility",
                "notes": (
                    "Major federal research facility at eastern end of city "
                    "(near Altadena border). Closed and evacuated during Eaton "
                    "Fire Jan 8-13, 2025. LACoFD conducted retardant drops to "
                    "protect it. Irreplaceable space exploration assets on site."
                ),
            },
            {
                "name": "Mt Lukens / Mt Wilson ridgeline",
                "bearing": "N/NE",
                "distance_mi": 3,
                "type": "ridgeline",
                "notes": (
                    "High ridgeline (5,074 ft Lukens, 5,710 ft Wilson) above "
                    "city. Mt Wilson hosts critical communications towers serving "
                    "all of LA -- loss would disable TV/radio/cell for millions. "
                    "Towers survived both Station Fire (2009) and Eaton Fire "
                    "(2025) but remain at extreme risk."
                ),
            },
            {
                "name": "Devil's Gate Dam / Debris Basin",
                "bearing": "W",
                "distance_mi": 1,
                "type": "infrastructure",
                "notes": (
                    "Critical debris basin at Arroyo Seco mouth. Post-fire "
                    "debris flows are a major secondary hazard. After Station "
                    "Fire (2009), massive sediment deposition. After any future "
                    "mountain fire, debris flows in the first rainy season could "
                    "be catastrophic for downstream Pasadena."
                ),
            },
        ],
        "historical_fires": [
            "Eaton Fire 2025 (entire city evacuated, no structures damaged, JPL protected by retardant drops)",
            "Station Fire 2009 (160,577 acres, 2 firefighter deaths, threatened 500 homes in LCF)",
        ],
        "wui_class": "extreme",
        "population": 20100,
        "post_2025_status": (
            "City escaped structural damage from Eaton Fire due to wind direction "
            "and fuel modification programs. After-action report commissioned from "
            "outside consultants. JPL reviewing fire resilience. City maintains "
            "aggressive brush clearance and fire-resistant landscaping mandates. "
            "However, 16 years of fuel regrowth since Station Fire means the "
            "Angeles NF above LCF has significant fuel loads. A fire starting "
            "in the forest above the city during a Santa Ana event remains "
            "the primary catastrophic scenario."
        ),
    },

    # =========================================================================
    # VENTURA / SANTA BARBARA COAST
    # =========================================================================

    # =========================================================================
    # OJAI — Thomas Fire corridor, Sundowner wind trap, single-exit valley
    # =========================================================================
    "ojai_ca": {
        "center": (34.4480, -119.2429),
        "elevation_ft": 746,
        "population": 7637,
        "population_year": 2020,
        "median_age": 49.7,
        "demographic_notes": (
            "Population 7,637 (2020 Census). Median age 49.7 years — one of the "
            "oldest communities in Ventura County. 27.2% of residents are 65+, "
            "and the city has 19 senior living/nursing facilities for a town of "
            "under 8,000. This elderly-heavy demographic critically slows "
            "evacuation response times. Artist/retirement community character "
            "with many residents who have limited mobility or no personal vehicle. "
            "Chain stores prohibited by city ordinance — small-town character "
            "but also means limited commercial infrastructure for shelter/staging."
        ),
        "terrain_notes": (
            "Small city (pop ~7,600) in the Ojai Valley, a bowl-shaped depression "
            "surrounded by mountains on three sides: Topatopa Mountains (6,300+ ft) "
            "to the north, Sulphur Mountain to the south, and Black Mountain/"
            "Nordhoff Ridge to the east. The valley is essentially a terrain trap — "
            "mountains funnel hot, dry air from the interior during both Santa Ana "
            "and Sundowner wind events. Thomas Fire (2017) nearly encircled the "
            "city, burning through Matilija Canyon from the north and wrapping "
            "around both flanks. By December 13, 2017 the fire had completely "
            "surrounded the Ojai Valley including Lake Casitas. Only SR-33 (north "
            "through canyon) and SR-150 (east toward Santa Paula / west toward "
            "Carpinteria) provide access — effectively TWO roads for 7,600+ people "
            "plus tourists. During Thomas Fire, SR-150 to Santa Paula was closed "
            "by CHP and the evacuation queue on remaining routes stretched for "
            "miles. The valley floor sits at 746 ft but is immediately bounded by "
            "terrain rising to 4,000-6,000+ ft, creating extreme fire behavior "
            "amplification through slope-driven convection. Los Padres National "
            "Forest borders the city on N/NE/E with hundreds of thousands of "
            "acres of unmanaged wildland fuel."
        ),
        "evacuation_analysis": {
            "routes": [
                {
                    "name": "SR-33 (Maricopa Highway)",
                    "direction": "N/S through valley",
                    "lanes": 2,
                    "constraints": (
                        "Primary route. Runs through narrow canyon north of Ojai — "
                        "both sides were on fire during Thomas Fire with flames and "
                        "embers crossing the highway in the Wheeler Canyon area. "
                        "Single two-lane road with no shoulder in canyon sections. "
                        "Closed during Thomas Fire for firefighter access."
                    ),
                },
                {
                    "name": "SR-150 (east toward Santa Paula)",
                    "direction": "E",
                    "lanes": 2,
                    "constraints": (
                        "CHP closed this route during Thomas Fire as fire "
                        "burned along both sides. Thomas Fire ignition point at "
                        "Anlauf Canyon was directly adjacent to this road near "
                        "Santa Paula. When closed, Ojai is effectively cut off "
                        "from the east."
                    ),
                },
                {
                    "name": "SR-150 (west toward Carpinteria/US-101)",
                    "direction": "W",
                    "lanes": 2,
                    "constraints": (
                        "Winding mountain road over Casitas Pass. Narrow, "
                        "two-lane, steep grades. Viable escape if fire approaches "
                        "from N/E but extremely slow under heavy traffic. Single "
                        "accident blocks entire route."
                    ),
                },
            ],
            "estimated_evacuation_time_hours": 3.0,
            "worst_case_scenario": (
                "Fire approaching from N (Matilija Canyon) and E (Santa Paula) "
                "simultaneously — exactly what happened during Thomas Fire. "
                "SR-33 closed by fire in Wheeler Gorge, SR-150 east closed by "
                "fire near Santa Paula. Only exit is SR-150 west over Casitas "
                "Pass: single two-lane mountain road for 7,600+ residents plus "
                "tourists. With 27% elderly population, evacuation compliance "
                "and speed are severely degraded. Thomas Fire demonstrated this "
                "exact scenario is not hypothetical."
            ),
        },
        "wind_regimes": {
            "sundowner": (
                "Sundowner winds are the most dangerous fire weather for Ojai. "
                "Unlike Santa Anas (NE downslope from Great Basin), Sundowners "
                "are northerly downslope winds off the Santa Ynez Mountains that "
                "intensify around sunset — hence the name. Air descends rapidly, "
                "compresses, heats, and dries. Gale force (40-60 mph) hot dry "
                "winds funnel through canyons into the Ojai Valley. Sundowners "
                "have driven every major Ojai-area fire. Critical layer formation "
                "with height in the lower troposphere reflects gravity wave "
                "energy to the surface, amplifying downslope wind speed."
            ),
            "santa_ana": (
                "Classic NE foehn winds also funnel through Ojai Valley. "
                "Thomas Fire was driven by Santa Anas gusting to 70 mph on "
                "ridgelines, 35-45 mph sustained in the valleys."
            ),
        },
        "danger_quadrants": ["north", "east", "west", "northwest"],
        "safe_quadrants": [],
        "key_features": [
            {
                "name": "Matilija Canyon",
                "bearing": "N",
                "distance_mi": 5,
                "type": "major_canyon",
                "notes": (
                    "Deep, steep-walled canyon extending into Los Padres NF. "
                    "Thomas Fire devastated this entire canyon — the lower "
                    "section was burned out overnight. Extremely remote and "
                    "rugged terrain with rock outcrops, crumbling slopes, and "
                    "steep side-canyons filled with dense brush. North Fork "
                    "Matilija Creek provides fuel-laden drainage directly toward "
                    "Ojai Valley. Matilija Wilderness area is 29,600 acres of "
                    "unmanaged fuel. Wheeler Fire (1985) also burned through "
                    "this canyon with winds pushing fire through Matilija and "
                    "over the Santa Ynez Mountains."
                ),
            },
            {
                "name": "Wheeler Gorge / Wheeler Canyon",
                "bearing": "NW",
                "distance_mi": 8,
                "type": "canyon",
                "notes": (
                    "Deep gorge along SR-33 north of Ojai. Wheeler Fire (1985) "
                    "ignited here by arsonist — burned 119,361 acres. Thomas "
                    "Fire burned through upper Wheeler Canyon with flames and "
                    "embers crossing SR-33 on both sides. Wheeler Gorge "
                    "Campground damaged. Canyon channeling accelerates winds "
                    "and firebrands directly toward Ojai Valley."
                ),
            },
            {
                "name": "Topatopa Mountains",
                "bearing": "N/NE",
                "distance_mi": 3,
                "type": "mountain",
                "notes": (
                    "6,300+ ft mountains directly above Ojai Valley. "
                    "4,500+ ft elevation gain from valley floor creates "
                    "extreme slope-driven fire runs. Topatopa Bluff (6,367 ft) "
                    "is the dominant terrain feature."
                ),
            },
            {
                "name": "Los Padres National Forest",
                "bearing": "N/E",
                "distance_mi": 2,
                "type": "wildland",
                "notes": (
                    "Massive undeveloped wildland — 1.75 million acres total. "
                    "Thomas Fire burned 150,000+ acres of LPNF lands. Fuel "
                    "loads include heavy chaparral, coastal sage scrub, and "
                    "mixed oak-conifer at higher elevations. DOJ recovered "
                    "$80M from SCE for LPNF damage alone."
                ),
            },
            {
                "name": "Sulphur Mountain",
                "bearing": "S",
                "distance_mi": 2,
                "type": "mountain",
                "notes": (
                    "Forms southern wall of Ojai Valley. Sulphur Mountain Road "
                    "is a narrow canyon road and fire corridor. Chaparral-covered "
                    "slopes face north into valley."
                ),
            },
            {
                "name": "Lake Casitas",
                "bearing": "SW",
                "distance_mi": 4,
                "type": "water_feature",
                "notes": (
                    "Primary water supply for Ojai via Casitas Municipal Water "
                    "District. Thomas Fire forced evacuation of Casitas MWD "
                    "water treatment facility staff, resulting in boil-water "
                    "advisory for Ojai and Ventura. Fire completely surrounded "
                    "Lake Casitas by Dec 13. Critical single-point water "
                    "infrastructure vulnerability."
                ),
            },
            {
                "name": "SR-33 / Maricopa Highway",
                "bearing": "N/S",
                "type": "access_route",
                "notes": (
                    "Primary route through canyon north of Ojai. Two-lane, "
                    "no shoulder in canyon sections. Both sides on fire during "
                    "Thomas Fire. Only viable north-south corridor."
                ),
            },
            {
                "name": "SR-150 / Ojai-Santa Paula Road",
                "bearing": "E",
                "type": "access_route",
                "notes": (
                    "Eastern access to Santa Paula and US-101. Thomas Fire "
                    "ignition point (Anlauf Canyon, SCE power lines) was "
                    "adjacent to this road. Closed by CHP during Thomas Fire. "
                    "Two-lane road through agricultural/foothill terrain."
                ),
            },
        ],
        "infrastructure_vulnerabilities": [
            {
                "type": "power_lines",
                "operator": "Southern California Edison (SCE)",
                "detail": (
                    "Thomas Fire had TWO ignition points, both caused by SCE "
                    "equipment: (1) Anlauf Canyon north of Santa Paula — power "
                    "lines contacted each other in high winds, dropping heated "
                    "material onto dry vegetation; (2) Koenigstein Road in "
                    "Upper Ojai — transformer failure caused energized line to "
                    "fall to ground. SCE paid $80M to US government (2024) and "
                    "$550M in CPUC penalties for Thomas, Woolsey, and other fires. "
                    "SCE infrastructure runs throughout canyon terrain surrounding "
                    "Ojai with lines exposed to Sundowner and Santa Ana winds."
                ),
            },
            {
                "type": "water_supply",
                "operator": "Casitas Municipal Water District",
                "detail": (
                    "Single water treatment facility serving Ojai, Upper Ojai, "
                    "Casitas Springs, and parts of Ventura. Thomas Fire forced "
                    "staff evacuation from treatment plant, causing system "
                    "depressurization and boil-water advisory. Lake Casitas is "
                    "fed by Ventura River diversions and surrounding drainages — "
                    "all within Thomas Fire burn area. Post-fire debris flows "
                    "threaten water quality for years."
                ),
            },
        ],
        "historical_fires": [
            {
                "name": "Thomas Fire",
                "year": 2017,
                "acres": 281893,
                "structures_destroyed": 1063,
                "deaths": 2,
                "detail": (
                    "Nearly encircled Ojai. Two SCE-caused ignition points on "
                    "Dec 4. Spread at rate of one football field per second on "
                    "Dec 5 morning. Fire traveled 12 miles from ignition to "
                    "Ventura coast in hours. Burned 150,000+ acres of Los Padres "
                    "NF. Lower Matilija Canyon burned out overnight. Completely "
                    "surrounded Ojai Valley and Lake Casitas by Dec 13. Largest "
                    "fire in California recorded history at the time. Santa Ana "
                    "winds gusted to 70 mph on ridgelines. SCE settled for $80M. "
                    "$2.2 billion total damages."
                ),
            },
            {
                "name": "Wheeler Fire",
                "year": 1985,
                "acres": 119361,
                "structures_destroyed": 19,
                "deaths": 0,
                "detail": (
                    "Arson ignition in Wheeler Gorge, 15 mi NW of Ojai. "
                    "Expanded to 45,000 acres in just two days. Winds pushed "
                    "fire through Matilija Canyon and over Santa Ynez Mountains "
                    "into Santa Barbara watershed. 119,361 acres, 19 homes, "
                    "37 buildings, 32 vehicles, $3M in orchards. Largest fire "
                    "ever handled by a single incident management team at that "
                    "time. Required 30,000-acre backfire to control."
                ),
            },
            {
                "name": "Matilija Fire",
                "year": 1932,
                "acres": 220000,
                "structures_destroyed": None,
                "deaths": 0,
                "detail": (
                    "Massive wildfire in Matilija Canyon/Los Padres NF area. "
                    "Demonstrated the canyon's potential for extreme fire runs "
                    "decades before modern development increased exposure."
                ),
            },
        ],
        "fire_behavior_notes": (
            "The Ojai Valley is one of California's most dangerous terrain traps "
            "for wildfire. The bowl-shaped valley channels both Sundowner and "
            "Santa Ana winds, creating extreme fire weather amplification. Thomas "
            "Fire demonstrated the worst case: fire approaching from multiple "
            "quadrants simultaneously, cutting evacuation routes, threatening "
            "water supply, and nearly encircling 7,600+ residents (27% elderly) "
            "with only narrow two-lane mountain roads for escape. The Matilija "
            "Canyon-to-Ojai axis is a proven fire run corridor — fire races "
            "down-canyon driven by gravity winds and channeled by steep canyon "
            "walls, emerging into the populated valley at high speed."
        ),
        "wui_class": "extreme",
    },

    # =========================================================================
    # VENTURA — Thomas Fire coastal terminus, Santa Clara River corridor
    # =========================================================================
    "ventura_ca": {
        "center": (34.2746, -119.2290),
        "elevation_ft": 115,
        "population": 110763,
        "population_year": 2020,
        "median_age": 36.0,
        "demographic_notes": (
            "Population 110,763 (2020 Census). Major coastal city and Ventura "
            "County seat. Density 5,061/sq mi. 35.1% Hispanic/Latino. Unlike "
            "Ojai, Ventura has a younger, more diverse population with better "
            "transportation infrastructure. However, the eastern hillside "
            "neighborhoods (Clearpoint, Ondulando, Skyline, Foothill Heights) "
            "that face the highest fire risk are among the older, more affluent "
            "residential areas with narrow winding streets on steep terrain."
        ),
        "terrain_notes": (
            "Coastal city (pop ~111,000) where Thomas Fire (2017) first struck "
            "urban areas. Fire raced from the mountains NE of Santa Paula to "
            "the coast in hours, driven by 60-70 mph Santa Ana winds. Eastern "
            "hillside neighborhoods along Foothill Road — Clearpoint, Ondulando, "
            "Skyline, Foothill Heights — suffered the heaviest damage with 538 "
            "structures destroyed in the city of Ventura alone (half the Thomas "
            "Fire's total structure loss). City is bounded by mountains to N/NE "
            "with multiple canyon drainages that act as fire funnels into the "
            "urban interface. The Santa Clara River corridor (Hwy 126) provides "
            "a broad fire approach vector from the east. The Ventura River "
            "corridor channels fire from the mountains directly to the coast. "
            "Coastal plain elevation ~50-150 ft but terrain rises steeply to "
            "N and NE."
        ),
        "evacuation_analysis": {
            "routes": [
                {
                    "name": "US-101 Freeway",
                    "direction": "E-W (coastal)",
                    "lanes": 6,
                    "constraints": (
                        "Primary evacuation route. Thomas Fire came within "
                        "striking distance of 101 corridor. During Woolsey Fire "
                        "(2018), the 101 was jumped by fire in neighboring "
                        "Ventura County communities. High-capacity but also "
                        "serves as primary route for all of coastal Ventura "
                        "County — gridlock during regional evacuations."
                    ),
                },
                {
                    "name": "SR-126 (toward Santa Clarita/I-5)",
                    "direction": "E",
                    "lanes": 4,
                    "constraints": (
                        "Runs through Santa Clara River valley. Thomas Fire "
                        "approached along this corridor from Santa Paula. "
                        "Provides access to I-5 but is also a fire approach "
                        "vector — fire and evacuation route conflict."
                    ),
                },
                {
                    "name": "SR-33 (toward Ojai)",
                    "direction": "N",
                    "lanes": 2,
                    "constraints": (
                        "Two-lane road into mountains. Not viable evacuation "
                        "route during most fire scenarios — leads toward fire "
                        "source terrain."
                    ),
                },
            ],
            "estimated_evacuation_time_hours": 2.0,
            "worst_case_scenario": (
                "Fire from NE cuts SR-126, limiting eastern evacuation. 101 "
                "becomes sole corridor for 110,000+ residents and surrounding "
                "communities (Oxnard, Camarillo also evacuating). Thomas Fire "
                "demonstrated that fire can reach Ventura's urban core from "
                "Santa Paula in under 6 hours with strong Santa Ana winds."
            ),
        },
        "danger_quadrants": ["north", "northeast", "east"],
        "safe_quadrants": ["south", "southwest"],
        "key_features": [
            {
                "name": "Santa Clara River corridor / Hwy 126",
                "bearing": "E",
                "distance_mi": 0,
                "type": "river_valley",
                "notes": (
                    "Broad valley running E-W from Santa Clarita to coast. "
                    "Thomas Fire approached along this corridor from Santa "
                    "Paula ignition point. River bottom vegetation provides "
                    "continuous fuel. Santa Ana winds align with valley "
                    "orientation, accelerating fire westward toward Ventura. "
                    "Additional fires have ignited in river bottom vegetation "
                    "within city limits."
                ),
            },
            {
                "name": "Ventura River corridor",
                "bearing": "N",
                "distance_mi": 0,
                "type": "river_valley",
                "notes": (
                    "Drainage from Ojai Valley to coast, passing through "
                    "Ventura's western neighborhoods. Fire corridor from "
                    "mountains to coast. Riparian vegetation along river."
                ),
            },
            {
                "name": "Foothill Road hillside neighborhoods",
                "bearing": "N/NE",
                "distance_mi": 2,
                "type": "wui_interface",
                "notes": (
                    "Clearpoint, Ondulando, Skyline, Foothill Heights — "
                    "residential neighborhoods built on steep hillsides at "
                    "the urban-wildland boundary. Thomas Fire destroyed homes "
                    "here as fire descended from mountains. Narrow winding "
                    "streets, heavy ornamental vegetation, difficult access "
                    "for fire apparatus. 538 structures destroyed in Ventura "
                    "during Thomas Fire — concentrated in these neighborhoods."
                ),
            },
            {
                "name": "Two Trees / hills above downtown",
                "bearing": "N",
                "distance_mi": 1,
                "type": "escarpment",
                "notes": (
                    "Steep hills immediately above downtown Ventura. Thomas "
                    "Fire reached these hills, destroying apartment buildings "
                    "and homes above the downtown core. Fire reached the "
                    "interface between foothill rangeland and developed areas."
                ),
            },
            {
                "name": "Anlauf Canyon (Thomas Fire ignition)",
                "bearing": "NE",
                "distance_mi": 12,
                "type": "canyon",
                "notes": (
                    "Canyon north of Santa Paula where Thomas Fire first "
                    "ignited at 6:30 PM on Dec 4, 2017. SCE power lines "
                    "contacted each other in high winds. Fire ran 12 miles "
                    "from this point to Ventura coast in hours."
                ),
            },
            {
                "name": "US-101 Freeway",
                "bearing": "E-W",
                "type": "access_route",
                "notes": (
                    "Major coastal evacuation route. 6-lane freeway but "
                    "serves as primary corridor for all of coastal Ventura "
                    "County. Thomas Fire burned to within 1 mile of 101 in "
                    "several locations."
                ),
            },
        ],
        "infrastructure_vulnerabilities": [
            {
                "type": "power_lines",
                "operator": "Southern California Edison (SCE)",
                "detail": (
                    "Thomas Fire was caused by two SCE equipment failures. "
                    "Anlauf Canyon: lines contacted in wind, dropped heated "
                    "material. Koenigstein Road: transformer failure, energized "
                    "line fell. $80M DOJ settlement, $550M CPUC penalties. "
                    "SCE distribution and transmission lines serve all Ventura "
                    "hillside neighborhoods."
                ),
            },
            {
                "type": "water_supply",
                "operator": "Ventura Water / Casitas MWD",
                "detail": (
                    "Thomas Fire forced Casitas MWD treatment facility "
                    "evacuation, causing boil-water advisory for entire city "
                    "of Ventura. Foster Park pump station lost pressure. Water "
                    "system depressurization meant fire hydrants in hillside "
                    "neighborhoods had reduced or zero pressure during active "
                    "structure defense."
                ),
            },
        ],
        "historical_fires": [
            {
                "name": "Thomas Fire",
                "year": 2017,
                "acres": 281893,
                "structures_destroyed": 1063,
                "structures_in_ventura": 538,
                "deaths": 2,
                "detail": (
                    "Ignited Dec 4 near Santa Paula from SCE equipment. "
                    "Reached Ventura coast within hours. Spread at one football "
                    "field per second on morning of Dec 5. 104,607 residents "
                    "evacuated. Santa Ana gusts to 70 mph on ridgelines. "
                    "Destroyed Clearpoint, Ondulando, Skyline neighborhoods. "
                    "$2.2 billion total damages. Largest CA fire at that time."
                ),
            },
            {
                "name": "Woolsey Fire",
                "year": 2018,
                "acres": 96949,
                "structures_destroyed": 1643,
                "deaths": 3,
                "detail": (
                    "Burned in SE Ventura County / LA County. Demonstrated "
                    "that fire can jump US-101 freeway — the primary Ventura "
                    "evacuation route. 295,000 people evacuated across the "
                    "region."
                ),
            },
        ],
        "fire_behavior_notes": (
            "Thomas Fire demonstrated the extreme fire run potential from "
            "interior mountains to the Ventura coast. The fire traveled 12 "
            "miles in hours under Santa Ana conditions, reaching Ventura's "
            "hillside neighborhoods before most residents could evacuate. The "
            "spread rate of one football field per second (approximately 36 mph "
            "linear advance) illustrates the futility of late evacuation in "
            "Santa Ana conditions. The Santa Clara River and Ventura River "
            "corridors provide broad, fuel-laden approach vectors from the "
            "interior. Hillside neighborhoods on the WUI boundary absorbed "
            "half the fire's total structure loss."
        ),
        "wui_class": "high",
    },

    # =========================================================================
    # THOUSAND OAKS — Woolsey Fire corridor, Conejo Valley, 101 vulnerability
    # =========================================================================
    "thousand_oaks_ca": {
        "center": (34.1706, -118.8376),
        "elevation_ft": 900,
        "population": 126966,
        "population_year": 2020,
        "median_age": 44.5,
        "demographic_notes": (
            "Population 126,966 (2020 Census). Affluent suburban city forming "
            "the central core of the Conejo Valley. Median age 44.5. "
            "68.3% White, 19.9% Hispanic. City is characterized by 50,000-60,000 "
            "oak trees within city limits. Major employment center with numerous "
            "corporate offices that evacuated during Woolsey Fire. Large "
            "commuter population — many residents away during daytime fires but "
            "creating return-traffic conflicts during evacuation."
        ),
        "terrain_notes": (
            "City of 127,000 in the Conejo Valley, a broad basin bounded by "
            "the Santa Monica Mountains (chaparral-covered, 2,000-3,000 ft) "
            "to the south, Simi Hills to the east/northeast, Conejo Mountains "
            "and Mount Clef Ridge to the north. Woolsey Fire (2018) demonstrated "
            "the city's extreme vulnerability: fire raced from Santa Susana "
            "Field Laboratory in the Simi Hills through Oak Park, jumped the "
            "101 Freeway at multiple points near Liberty Canyon with a 14-mile-"
            "long fireline, and continued through the Santa Monica Mountains "
            "to the coast, burning 80% of the Santa Monica Mountains National "
            "Recreation Area. The fire was driven by 50-70 mph Santa Ana winds "
            "and jumped the 101 Freeway — a presumed firebreak — at several "
            "points. Conejo Grade (US-101) between Thousand Oaks and Camarillo "
            "is a key wind acceleration point where terrain compression "
            "increases wind velocity. The Santa Monica Mountains chaparral has "
            "a natural fire return interval of 30-100 years, but fires now "
            "occur every 5-20 years due to human ignition, preventing full "
            "ecosystem recovery and creating type-converted grass/annual fuels "
            "that burn even more frequently."
        ),
        "evacuation_analysis": {
            "routes": [
                {
                    "name": "US-101 Freeway (westbound toward Camarillo/Ventura)",
                    "direction": "W",
                    "lanes": 6,
                    "constraints": (
                        "Primary evacuation route. Woolsey Fire CLOSED a "
                        "4-mile stretch from Las Virgenes Road to Kanan Road. "
                        "All lanes shut from Las Virgenes Canyon Rd (Calabasas) "
                        "to Adobe Rd (Agoura Hills). Also closed southbound "
                        "from Hwy 23 in Thousand Oaks to Hwy 34 in Camarillo. "
                        "When fire jumps 101, the presumed primary escape route "
                        "becomes impassable."
                    ),
                },
                {
                    "name": "US-101 Freeway (eastbound toward LA)",
                    "direction": "E",
                    "lanes": 6,
                    "constraints": (
                        "Woolsey Fire jumped 101 at Liberty Canyon, cutting "
                        "eastbound evacuation. Fire crossed at multiple points "
                        "along a 14-mile front."
                    ),
                },
                {
                    "name": "SR-23 (northbound toward Moorpark/Simi Valley)",
                    "direction": "N",
                    "lanes": 4,
                    "constraints": (
                        "Viable evacuation north through Conejo Grade if fire "
                        "is approaching from S/SE (Santa Monica Mountains). "
                        "However, Woolsey Fire originated from Simi Hills to "
                        "the NE — this route led TOWARD fire origin."
                    ),
                },
                {
                    "name": "Westlake Blvd / Kanan Rd / other surface streets",
                    "direction": "various",
                    "lanes": 2,
                    "constraints": (
                        "Surface streets through suburban neighborhoods. "
                        "Gridlocked during Woolsey Fire evacuations. Many lead "
                        "into Santa Monica Mountains — toward fire."
                    ),
                },
            ],
            "estimated_evacuation_time_hours": 2.5,
            "worst_case_scenario": (
                "Woolsey Fire demonstrated the worst case: fire approached "
                "from NE (Simi Hills), jumped 101 at multiple points cutting "
                "both east and west freeway evacuation, and burned south through "
                "Santa Monica Mountains. 295,000 people evacuated across the "
                "region. Bell Canyon, Oak Park, Agoura Hills, Malibu — all "
                "required total evacuation. Corporate offices in Thousand Oaks "
                "added to daytime evacuation traffic. For a city of 127,000, "
                "the freeway-dependent evacuation model fails when fire crosses "
                "the freeway."
            ),
        },
        "danger_quadrants": ["east", "northeast", "south", "southeast"],
        "safe_quadrants": ["west", "northwest"],
        "key_features": [
            {
                "name": "Santa Monica Mountains",
                "bearing": "S/SE",
                "distance_mi": 3,
                "type": "mountain",
                "notes": (
                    "Woolsey Fire burned 80% of the 156,000-acre Santa Monica "
                    "Mountains National Recreation Area. Dense chaparral, steep "
                    "canyons. Natural fire return interval 30-100 years but now "
                    "burning every 5-20 years. When chaparral burns too frequently "
                    "(< 10 years), seed banks are consumed and non-native grasses "
                    "colonize, creating grass-fire type conversion that burns "
                    "even more often."
                ),
            },
            {
                "name": "Simi Hills / Santa Susana Field Laboratory",
                "bearing": "E/NE",
                "distance_mi": 5,
                "type": "mountain",
                "notes": (
                    "Woolsey Fire ignited at Santa Susana Field Laboratory "
                    "(SSFL) — a former rocket testing and nuclear research "
                    "facility with known soil contamination. Fire burned 80% "
                    "of the 2,850-acre site. SSFL contains residual radioactive "
                    "and chemical contamination from a 1959 partial nuclear "
                    "meltdown. Studies detected radioactive microparticles "
                    "(thorium) in ash deposited up to 15 km from SSFL during "
                    "Woolsey Fire. Oak Park, Bell Canyon communities are "
                    "directly downwind."
                ),
            },
            {
                "name": "Liberty Canyon (101 Freeway crossing)",
                "bearing": "SE",
                "distance_mi": 5,
                "type": "canyon",
                "notes": (
                    "Location where Woolsey Fire jumped the 101 Freeway. "
                    "14-mile-long fireline crossed the freeway at multiple "
                    "points near Liberty Canyon, driven by 50-60 mph winds. "
                    "Liberty Canyon is also a key wildlife corridor connecting "
                    "Santa Monica Mountains to Simi Hills."
                ),
            },
            {
                "name": "Conejo Grade (US-101 between TO and Camarillo)",
                "bearing": "W/SW",
                "distance_mi": 3,
                "type": "mountain_pass",
                "notes": (
                    "Steep grade on US-101. Terrain compression accelerates "
                    "wind through this gap. Hill Fire (same day as Woolsey) "
                    "jumped 101 at Conejo Grade, burning thousands of acres. "
                    "Wind funneling effect creates extreme fire weather."
                ),
            },
            {
                "name": "Oak Park",
                "bearing": "E",
                "distance_mi": 3,
                "type": "community",
                "notes": (
                    "Residential community hit first by Woolsey Fire as it "
                    "moved from Simi Hills south. Total evacuation ordered. "
                    "Homes destroyed on Churchwood Dr, Wembly Ave, Symphony "
                    "Lane. Community sits directly below SSFL contaminated site."
                ),
            },
            {
                "name": "Bell Canyon",
                "bearing": "E",
                "distance_mi": 8,
                "type": "community",
                "notes": (
                    "Gated community in narrow canyon — total evacuation during "
                    "Woolsey Fire. Single access road. Directly in fire path "
                    "from SSFL."
                ),
            },
            {
                "name": "US-101 / SR-23 intersection",
                "bearing": "center",
                "type": "access_route",
                "notes": (
                    "Major evacuation hub. Both routes were impacted during "
                    "Woolsey Fire. 101 closed in multiple sections, SR-23 "
                    "led toward fire origin."
                ),
            },
        ],
        "infrastructure_vulnerabilities": [
            {
                "type": "power_lines",
                "operator": "Southern California Edison (SCE)",
                "detail": (
                    "SCE infrastructure throughout Simi Hills and Santa Monica "
                    "Mountains. CPUC investigation found SCE equipment "
                    "associated with Woolsey Fire ignition at SSFL. Part of "
                    "$550M CPUC penalty package."
                ),
            },
            {
                "type": "contaminated_site",
                "operator": "Boeing / DOE / NASA",
                "detail": (
                    "Santa Susana Field Laboratory contains radioactive and "
                    "chemical contamination from decades of rocket testing and "
                    "a 1959 partial nuclear meltdown. Woolsey Fire burned 80% "
                    "of the site, potentially mobilizing contaminants in smoke "
                    "and ash. Radioactive microparticles detected in ash up to "
                    "15 km away. This adds a hazmat dimension to any fire "
                    "originating from or burning through SSFL."
                ),
            },
        ],
        "historical_fires": [
            {
                "name": "Woolsey Fire",
                "year": 2018,
                "acres": 96949,
                "structures_destroyed": 1643,
                "deaths": 3,
                "detail": (
                    "Ignited Nov 8 at Santa Susana Field Laboratory. Driven by "
                    "50-70 mph Santa Ana winds. Jumped 101 Freeway at Liberty "
                    "Canyon with 14-mile fireline. Burned 80% of Santa Monica "
                    "Mountains NRA. 295,000 evacuated from 105,000 residences. "
                    "Total evacuation of Bell Canyon, Oak Park, Malibu, Agoura "
                    "Hills. Radioactive microparticles from SSFL detected in "
                    "ash deposits."
                ),
            },
            {
                "name": "Hill Fire",
                "year": 2018,
                "acres": 4531,
                "structures_destroyed": 4,
                "deaths": 0,
                "detail": (
                    "Ignited same day as Woolsey Fire. Jumped 101 at Conejo "
                    "Grade. Demonstrated that the 101 freeway is NOT a reliable "
                    "firebreak in Santa Ana conditions."
                ),
            },
            {
                "name": "Easy Fire",
                "year": 2019,
                "acres": 1860,
                "structures_destroyed": 0,
                "deaths": 0,
                "detail": (
                    "Burned in Simi Valley/Moorpark area, forcing evacuations. "
                    "Demonstrated continued fire threat from Simi Hills corridor."
                ),
            },
            {
                "name": "Springs Fire",
                "year": 2013,
                "acres": 24251,
                "structures_destroyed": 15,
                "deaths": 0,
                "detail": (
                    "Burned in Santa Monica Mountains near Camarillo. "
                    "Demonstrated regional fire potential."
                ),
            },
        ],
        "fire_behavior_notes": (
            "The Woolsey Fire fundamentally changed the risk assessment for "
            "Thousand Oaks and the Conejo Valley. Before 2018, the 101 Freeway "
            "was considered a de facto firebreak separating the chaparral-covered "
            "Santa Monica Mountains from suburban development. Woolsey Fire "
            "proved this assumption catastrophically wrong: driven by 50-70 mph "
            "Santa Ana winds, a 14-mile-long fireline jumped the 101 at multiple "
            "points near Liberty Canyon, continuing south through the Santa "
            "Monica Mountains to the Pacific Ocean. The fire destroyed 1,643 "
            "structures and required evacuation of 295,000 people. The "
            "contaminated origin site (SSFL) adds a unique hazmat dimension — "
            "radioactive and chemical contaminants were mobilized in smoke and "
            "ash. Santa Monica Mountains chaparral fire cycle has shortened from "
            "30-100 years to 5-20 years, meaning Thousand Oaks will face this "
            "threat repeatedly within a single generation."
        ),
        "wui_class": "extreme",
    },

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
    # SAN BERNARDINO MOUNTAINS
    # =========================================================================

    # =========================================================================
    # LAKE ARROWHEAD — Mountain island, limited escape, population surge
    # =========================================================================
    "lake_arrowhead_ca": {
        "center": (34.2580, -117.1890),
        "elevation_ft": 5174,
        "population": 12401,
        "population_year": 2020,
        "seasonal_population_peak": 40000,
        "seasonal_population_notes": (
            "Permanent population 12,401 (2020 Census). Approximately 4,000 "
            "homes occupied full-time by ~10,000 permanent residents. An "
            "additional 6,000 second/vacation homes are used on weekends, "
            "holidays, and summer. On a summer holiday weekend, population "
            "swells to 40,000 — quadrupling the permanent count. The area "
            "hosts 2.4 million visitors per year. Tourism contributes $78M "
            "annually. This seasonal population surge is an evacuation "
            "nightmare: 40,000 people, many unfamiliar with mountain roads, "
            "trying to descend via two-lane highways with hairpin turns."
        ),
        "median_age": None,
        "demographic_notes": (
            "Mountain resort community with extreme seasonal population "
            "variation. Mix of retirees, vacation homeowners, and service "
            "workers. Many seasonal visitors are unfamiliar with evacuation "
            "routes and mountain driving. Second-home owners may not receive "
            "or monitor local emergency alerts. 90% weekend/holiday occupancy "
            "vs 45% weekday occupancy means fire risk peaks correlate with "
            "maximum population exposure."
        ),
        "terrain_notes": (
            "Mountain resort community in the San Bernardino Mountains at "
            "5,174 ft elevation. Sits on a forested plateau atop the steep "
            "southern escarpment of the San Bernardino Mountains — a 4,000+ ft "
            "near-vertical drop to the San Bernardino Valley floor. The community "
            "is effectively a populated island on top of a mountain, accessible "
            "only by narrow, winding mountain roads. Dense conifer forest "
            "(ponderosa pine, sugar pine, incense cedar, white fir) with extreme "
            "fuel loading from decades of fire suppression and bark beetle "
            "mortality. The 2003 Old Fire climbed the southern escarpment from "
            "Waterman Canyon, forcing evacuation of 80,000+ from all mountain "
            "communities. The 2007 Grass Valley Fire destroyed 176 structures "
            "in a 'domino effect' where burning homes ignited adjacent homes "
            "without the wildfire as a factor. The 2024 Line Fire again forced "
            "evacuations, with Highway 18 closed northbound (inbound) while "
            "only southbound (outbound) traffic allowed. Lake Arrowhead "
            "reservoir provides a limited fire break at the community's center "
            "but is privately owned (Arrowhead Lake Association) and not "
            "accessible to the general public."
        ),
        "evacuation_analysis": {
            "routes": [
                {
                    "name": "SR-18 / Rim of the World Drive (south toward SB)",
                    "direction": "S/SW",
                    "lanes": 2,
                    "constraints": (
                        "Primary escape route. Two-lane road with hairpin turns "
                        "clinging to the rim of a 4,000 ft escarpment. No "
                        "shoulder in many sections. Single accident or downed "
                        "tree blocks entire route. Old Fire breached fire lines "
                        "along Rim of the World Hwy near Skyforest and burned "
                        "into Cedar Glen. During Line Fire (2024), SR-18 was "
                        "closed northbound — only outbound (downhill) traffic "
                        "allowed. Descent takes 30-45 min under normal "
                        "conditions; hours during mass evacuation."
                    ),
                },
                {
                    "name": "SR-18 east (toward Big Bear via Running Springs)",
                    "direction": "E",
                    "lanes": 2,
                    "constraints": (
                        "Connects to Running Springs, then Big Bear. During "
                        "Line Fire (2024), SR-18 was closed from Kuffel Canyon "
                        "to Big Bear Dam. Running Springs was under mandatory "
                        "evacuation. This route leads to ANOTHER mountain "
                        "community, not to safety at the valley floor. Only "
                        "useful if descending via SR-38 to Redlands (east side), "
                        "adding 60+ minutes."
                    ),
                },
                {
                    "name": "SR-138 (north toward Hesperia/I-15)",
                    "direction": "N",
                    "lanes": 2,
                    "constraints": (
                        "Northern escape route descending to high desert. "
                        "Connects to Crestline and then descends to I-15 via "
                        "Cajon Pass area. Two-lane, winding. During Old Fire, "
                        "SR-138 was slow-going but the best route to I-15 — "
                        "until the fire burned the east side below Cedarpines "
                        "Park and closed I-15. Back route through Silverwood "
                        "Lake area."
                    ),
                },
                {
                    "name": "SR-330 (south via Highland/Running Springs)",
                    "direction": "S",
                    "lanes": 2,
                    "constraints": (
                        "Alternative southern descent via Highland. During "
                        "Line Fire (2024), SR-330 was closed from Highland Ave "
                        "to SR-18 in Running Springs — completely severed. "
                        "Steep, narrow, winding. Known for accidents and "
                        "closures in winter (ice/snow)."
                    ),
                },
            ],
            "estimated_evacuation_time_hours": 5.0,
            "worst_case_scenario": (
                "Fire approaching from south (San Bernardino Valley floor) "
                "climbs the 4,000 ft escarpment — exactly as Old Fire (2003) "
                "did. SR-18 south and SR-330 are cut by fire on the southern "
                "face. SR-138 north is the only remaining route but passes "
                "through Crestline (also evacuating 11,650+ people). On a "
                "summer holiday weekend, 40,000 people are attempting to "
                "descend on a single two-lane mountain road (SR-138) through "
                "Crestline to I-15. An Arrowbear Lake resident during the "
                "2024 Line Fire reported it took nearly 7 HOURS to reach the "
                "evacuation center in Highland after turning back for a camera. "
                "This is a mass-casualty evacuation scenario for a mountain-"
                "top community with no helicopter pad capacity for 40,000."
            ),
        },
        "danger_quadrants": ["south", "southwest", "west"],
        "safe_quadrants": [],
        "key_features": [
            {
                "name": "San Bernardino Mountain southern escarpment",
                "bearing": "S/SW",
                "distance_mi": 1,
                "type": "escarpment",
                "notes": (
                    "Near-vertical 4,000+ ft drop from mountain communities "
                    "to San Bernardino Valley floor (elevation ~1,000 ft). "
                    "Old Fire (2003) climbed this face from Waterman Canyon "
                    "at over 1,000 acres/hour. Extreme slope-driven convection "
                    "creates flame lengths exceeding 100 ft. Santa Ana winds "
                    "compress against the mountain face, creating turbulent "
                    "upslope winds with long-range spotting capability — "
                    "embers launched miles ahead of the fire front."
                ),
            },
            {
                "name": "Grass Valley drainage",
                "bearing": "W",
                "distance_mi": 1,
                "type": "canyon",
                "notes": (
                    "Drainage one mile west of Lake Arrowhead where the 2007 "
                    "Grass Valley Fire started. Fire moved south through "
                    "drainage, then showered residential development with "
                    "firebrands at 0930. The USFS post-fire study documented "
                    "the 'domino effect': burning homes ignited adjacent homes "
                    "through radiant heat and ember showers, destroying 176 "
                    "structures independent of the wildfire's direct flame "
                    "front. Homes with wood shake roofs, pine litter in gutters, "
                    "and ornamental vegetation touching siding were the primary "
                    "ignition vectors."
                ),
            },
            {
                "name": "Rim of the World Drive (SR-18)",
                "bearing": "E-W",
                "type": "access_route",
                "notes": (
                    "Primary mountain road running along the rim of the "
                    "southern escarpment. Two-lane, hairpin turns, no shoulder. "
                    "Only route connecting Lake Arrowhead to Running Springs "
                    "and west to Crestline. Old Fire breached fire lines along "
                    "this road near Skyforest, allowing fire into Cedar Glen. "
                    "Road was designed for scenic tourism, not mass evacuation."
                ),
            },
            {
                "name": "SR-138 (toward Crestline / I-15)",
                "bearing": "W/N",
                "type": "access_route",
                "notes": (
                    "Connects Lake Arrowhead to Crestline and descends to "
                    "high desert. Two-lane, winding. Serves as backup "
                    "evacuation route when southern routes are cut."
                ),
            },
            {
                "name": "Cedar Glen",
                "bearing": "S",
                "distance_mi": 2,
                "type": "community",
                "notes": (
                    "Small mountain community on a single access road. Old "
                    "Fire (2003) destroyed 324 homes in Cedar Glen when fire "
                    "breached Rim of the World Hwy fire lines near Skyforest. "
                    "Community still recovering 20+ years later."
                ),
            },
            {
                "name": "Lake Arrowhead reservoir",
                "bearing": "center",
                "type": "water_feature",
                "notes": (
                    "184-acre private lake owned by Arrowhead Lake Association. "
                    "Provides limited fire break at community center and "
                    "emergency water supply for firefighting. However, lake "
                    "is not accessible to general public — gated access limits "
                    "its utility as a shelter-in-place refuge."
                ),
            },
            {
                "name": "Waterman Canyon / Old Waterman Canyon Rd",
                "bearing": "SW",
                "distance_mi": 5,
                "type": "canyon",
                "notes": (
                    "Canyon on southern face where Old Fire (2003) ignited "
                    "via arson. Steep terrain, dense chaparral. Fire ran "
                    "upslope from canyon through Arrowhead Springs and Del Rosa "
                    "neighborhoods before climbing to mountain communities."
                ),
            },
        ],
        "infrastructure_vulnerabilities": [
            {
                "type": "water_supply",
                "operator": "Lake Arrowhead CSD / CLAWA",
                "detail": (
                    "Water imported via Crestline-Lake Arrowhead Water Agency "
                    "(CLAWA) from Lake Silverwood via State Water Project — "
                    "pipeline runs through fire-prone terrain. Local "
                    "distribution system has aging steel mains with documented "
                    "leak problems (30,000-gallon leak in steel main, 216,000-"
                    "gallon leak on two-inch steel line). 420 fire hydrants "
                    "maintained by LACSD but flow rates vary — some hydrants "
                    "color-coded for GPM rating. Mountain terrain means gravity-"
                    "fed pressure is limited and pumping stations are vulnerable "
                    "to power loss during fire events."
                ),
            },
            {
                "type": "roads",
                "detail": (
                    "All access roads are two-lane mountain highways designed "
                    "for scenic tourism, not mass evacuation. SR-18 clings to "
                    "the rim of a 4,000 ft escarpment. No alternative routes. "
                    "Tree-fall from dead/beetle-killed conifers can block "
                    "roads with no detour options. Winter ice/snow closures "
                    "demonstrate the roads' vulnerability to any obstruction."
                ),
            },
            {
                "type": "power",
                "operator": "SCE / Bear Valley Electric",
                "detail": (
                    "Power lines run through dense forest on mountain roads. "
                    "Tree-fall onto lines is a constant ignition risk. Power "
                    "shutoffs (PSPS) during fire weather leave mountain "
                    "communities without power for pumping water, communications, "
                    "and medical equipment."
                ),
            },
        ],
        "historical_fires": [
            {
                "name": "Old Fire",
                "year": 2003,
                "acres": 91281,
                "structures_destroyed": 993,
                "deaths": 6,
                "detail": (
                    "Arson ignition in Waterman Canyon (Old Waterman Canyon Rd "
                    "at SR-18) on Oct 25, 2003. Driven by 50+ mph Santa Ana "
                    "winds. Spread exceeded 1,000 acres/hour initially. "
                    "Long-range spotting several miles ahead of flame front. "
                    "Forced evacuation of 80,000+ from ALL mountain communities "
                    "(Lake Arrowhead, Crestline, Running Springs, Cedar Glen). "
                    "Destroyed 324 homes in Cedar Glen alone when fire breached "
                    "Rim of the World Hwy fire lines. Part of 2003 Fire Siege "
                    "(15 simultaneous fires across SoCal). Arsonist Rickie Lee "
                    "Fowler convicted of murder, sentenced to death. Six deaths — "
                    "all from heart attacks caused by physical/emotional strain."
                ),
            },
            {
                "name": "Grass Valley Fire",
                "year": 2007,
                "acres": 1247,
                "structures_destroyed": 176,
                "deaths": 0,
                "detail": (
                    "Ignited Oct 22, 2007, one mile west of Lake Arrowhead. "
                    "Human-caused. Only 1,247 acres but destroyed 176 structures "
                    "and damaged 25 more. USFS study documented the 'domino "
                    "effect': firebrands ignited a few homes, then burning homes "
                    "ignited adjacent homes via radiant heat without the "
                    "wildfire front as a factor. Homes with wood shake roofs "
                    "and pine litter in gutters were primary ignition points. "
                    "Demonstrates that even a small fire in mountain community "
                    "dense housing can cause catastrophic structure loss."
                ),
            },
            {
                "name": "Slide Fire",
                "year": 2007,
                "acres": 12759,
                "structures_destroyed": 272,
                "deaths": 0,
                "detail": (
                    "Same day as Grass Valley Fire (Oct 22, 2007). Ignited "
                    "near Green Valley Lake/Running Springs. Destroyed 272 "
                    "homes and 3 outbuildings. Combined with Grass Valley Fire: "
                    "~450 structures destroyed in San Bernardino Mountains in "
                    "a single day."
                ),
            },
            {
                "name": "Line Fire",
                "year": 2024,
                "acres": 36539,
                "structures_destroyed": 35,
                "deaths": 0,
                "detail": (
                    "Ignited Sep 5, 2024 along Baseline Rd in Highland. "
                    "Grew to 36,000+ acres in San Bernardino National Forest. "
                    "Mandatory evacuation for Running Springs and Arrowbear "
                    "Lake; warnings for Lake Arrowhead, Crestline, Cedar Glen, "
                    "Valley of Enchantment. SR-18 closed northbound (inbound), "
                    "SR-330 closed entirely from Highland to Running Springs. "
                    "38,002 structures threatened (8,800 under evacuation "
                    "orders, 29,200 under warnings). One evacuee reported 7-hour "
                    "trip to reach evacuation center due to road congestion."
                ),
            },
        ],
        "fire_behavior_notes": (
            "Lake Arrowhead represents one of California's most dangerous "
            "evacuation scenarios: a mountain-top community of 12,000-40,000 "
            "(depending on season) accessible only by narrow two-lane mountain "
            "roads with hairpin turns, perched atop a 4,000 ft escarpment that "
            "amplifies fire behavior. The Old Fire (2003) demonstrated that "
            "fire can climb this escarpment at over 1,000 acres/hour with "
            "spotting miles ahead of the flame front. The Grass Valley Fire "
            "(2007) demonstrated that even a small fire can destroy hundreds "
            "of structures through the domino effect in dense mountain housing. "
            "The Line Fire (2024) demonstrated that evacuation takes HOURS — "
            "one resident reported 7 hours to descend. On a summer holiday "
            "weekend with 40,000 people on the mountain, mass evacuation via "
            "two-lane roads is functionally impossible in the time available "
            "when a wind-driven fire climbs the escarpment."
        ),
        "wui_class": "extreme",
    },

    # =========================================================================
    # CRESTLINE — Western rim, first in line, evacuation bottleneck
    # =========================================================================
    "crestline_ca": {
        "center": (34.2420, -117.2856),
        "elevation_ft": 4642,
        "population": 11650,
        "population_year": 2020,
        "seasonal_population_peak": 25000,
        "seasonal_population_notes": (
            "Permanent population 11,650 (2020 Census). Like Lake Arrowhead, "
            "significant vacation home and weekend visitor population. Centered "
            "around man-made Lake Gregory. Combined with adjacent communities "
            "(Cedarpines Park ~1,000, Valley of Enchantment, Twin Peaks), the "
            "western mountain rim communities total approximately 20,000+ "
            "permanent residents, swelling to 25,000+ on summer weekends. "
            "All share the same limited road network for evacuation."
        ),
        "median_age": None,
        "demographic_notes": (
            "Year-round mountain community — less seasonal than Lake Arrowhead "
            "but still significant visitor influx. Mix of retirees, families, "
            "and service workers. Many homes date to 1920s-1960s subdivisions "
            "(Cedarpines Park, Valley of Enchantment developed in 1920s) with "
            "construction that predates modern fire codes — wood frame, wood "
            "shake roofs, no defensible space. Lower-income demographic than "
            "Lake Arrowhead, with older housing stock more vulnerable to "
            "ember ignition."
        ),
        "terrain_notes": (
            "Mountain community (pop 11,650) on the WESTERN rim of the San "
            "Bernardino Mountains at 4,642 ft elevation. Sits on the very edge "
            "of the Rim of the World — dramatic 3,500+ ft escarpment dropping "
            "to San Bernardino Valley directly to the south. This is the FIRST "
            "mountain community that fire encounters when climbing the southern "
            "face from the San Bernardino Valley — it was hit before Lake "
            "Arrowhead during the Old Fire (2003). Dense pine/cedar forest with "
            "decades of fuel accumulation and extensive bark beetle mortality "
            "creating standing dead fuel. Crestline is also the critical "
            "evacuation BOTTLENECK for all mountain communities to the east — "
            "Lake Arrowhead, Running Springs, and Big Bear evacuees using "
            "SR-138 must pass THROUGH Crestline to reach I-15. If Crestline's "
            "roads are blocked, communities to the east are trapped."
        ),
        "evacuation_analysis": {
            "routes": [
                {
                    "name": "SR-138 (west/south toward I-15 / Cajon Pass)",
                    "direction": "W/S",
                    "lanes": 2,
                    "constraints": (
                        "Primary escape route descending to I-15 and the "
                        "high desert. Two-lane, winding mountain road. During "
                        "Old Fire (2003), the fire burned the east side below "
                        "Cedarpines Park and threatened to close I-15 at Cajon "
                        "Pass, leaving evacuees stranded on the north side of "
                        "the mountains. This is THE bottleneck for all western "
                        "mountain community evacuation."
                    ),
                },
                {
                    "name": "SR-18 (east toward Lake Arrowhead)",
                    "direction": "E",
                    "lanes": 2,
                    "constraints": (
                        "Rim of the World Drive connecting to Lake Arrowhead "
                        "and Running Springs. Two-lane. Goes DEEPER into "
                        "mountain communities, not toward safety. Only useful "
                        "if fire is approaching from west and eastern routes "
                        "(SR-18 east to Big Bear, SR-38 south to Redlands) are "
                        "still open — adding 60+ minutes to evacuation."
                    ),
                },
                {
                    "name": "Lake Drive / local surface streets",
                    "direction": "various",
                    "lanes": 2,
                    "constraints": (
                        "Narrow residential streets, many unpaved or poorly "
                        "maintained. Single-lane in some sections. Dead-end "
                        "streets throughout. Not viable for mass evacuation."
                    ),
                },
            ],
            "estimated_evacuation_time_hours": 4.0,
            "worst_case_scenario": (
                "Fire climbing southern escarpment from San Bernardino Valley "
                "(as in Old Fire 2003). Crestline, sitting on the western rim, "
                "is hit first. SR-138 down to I-15 is the only escape. But "
                "simultaneously, ALL mountain communities to the east — Lake "
                "Arrowhead (12,000-40,000), Running Springs, Cedar Glen, Twin "
                "Peaks — are also evacuating westward through Crestline. "
                "Combined evacuation demand: 30,000-60,000 people on a single "
                "two-lane mountain road. Old Fire forced evacuation of 80,000+ "
                "from all mountain communities. During Line Fire (2024), "
                "Crestline was under evacuation warning while Running Springs "
                "and Arrowbear Lake were under mandatory orders — creating "
                "bidirectional traffic conflicts on SR-18/SR-138."
            ),
        },
        "danger_quadrants": ["south", "southwest", "west"],
        "safe_quadrants": [],
        "key_features": [
            {
                "name": "San Bernardino Mountain western rim / escarpment",
                "bearing": "S",
                "distance_mi": 0.5,
                "type": "escarpment",
                "notes": (
                    "Extreme southern escarpment — 3,500+ ft vertical relief "
                    "from San Bernardino Valley floor to Crestline. Fire climbs "
                    "this face rapidly via slope-driven convection. Crestline "
                    "is literally on the rim — some properties sit within "
                    "hundreds of feet of the escarpment edge. Old Fire (2003) "
                    "climbed this face from Waterman Canyon at 1,000+ acres/hr. "
                    "The escarpment acts as a natural chimney, accelerating "
                    "fire upslope and launching embers onto the mountain-top "
                    "communities."
                ),
            },
            {
                "name": "Cedarpines Park",
                "bearing": "SW",
                "distance_mi": 1,
                "type": "community",
                "notes": (
                    "Adjacent community (~1,000 residents) on SR-138 below "
                    "Crestline. 1920s subdivision development predating fire "
                    "codes. Dense pine forest, narrow lots. Old Fire burned "
                    "the east side below Cedarpines Park. Community sits on "
                    "the evacuation route — if fire reaches Cedarpines Park, "
                    "the escape route (SR-138) is compromised."
                ),
            },
            {
                "name": "Valley of Enchantment",
                "bearing": "W",
                "distance_mi": 2,
                "type": "community",
                "notes": (
                    "Small community reached via SR-138 / Knapps Cut Off. "
                    "1920s subdivision development. Under evacuation warning "
                    "during Line Fire (2024). Limited access via narrow "
                    "mountain roads."
                ),
            },
            {
                "name": "Lake Gregory",
                "bearing": "center",
                "type": "water_feature",
                "notes": (
                    "Man-made lake (reservoir) at center of Crestline. Created "
                    "in late 1930s by damming Houston Creek. Provides a limited "
                    "fire break and emergency water source. County park "
                    "surrounds it — potential evacuation assembly point but "
                    "limited capacity. Not large enough to serve as meaningful "
                    "shelter-in-place buffer for the community."
                ),
            },
            {
                "name": "SR-138 / SR-18 junction",
                "bearing": "center",
                "type": "access_route",
                "notes": (
                    "Critical intersection connecting western mountain "
                    "evacuation route (SR-138 to I-15) with Rim of the World "
                    "Drive (SR-18 east to Lake Arrowhead). Bottleneck point "
                    "where traffic from multiple communities converges. Single "
                    "point of failure for entire western mountain evacuation."
                ),
            },
            {
                "name": "I-15 / Cajon Pass (destination)",
                "bearing": "W",
                "distance_mi": 12,
                "type": "freeway",
                "notes": (
                    "Destination freeway for evacuees descending SR-138. "
                    "Cajon Pass itself is a fire corridor — the Cajon Fire "
                    "has historically burned in this wind gap. If I-15 is "
                    "closed by fire at Cajon Pass (as nearly happened during "
                    "Old Fire), mountain evacuees have nowhere to go."
                ),
            },
        ],
        "infrastructure_vulnerabilities": [
            {
                "type": "water_supply",
                "operator": "Crestline-Lake Arrowhead Water Agency (CLAWA)",
                "detail": (
                    "Water imported from Lake Silverwood via State Water "
                    "Project pipeline running through fire-prone terrain. "
                    "Crestline Sanitation District manages local distribution. "
                    "Mountain terrain limits gravity-fed pressure. Power loss "
                    "during fire events (or PSPS shutoffs) disables pumping "
                    "stations, reducing hydrant pressure when it's needed most."
                ),
            },
            {
                "type": "roads",
                "detail": (
                    "SR-138 is the primary evacuation route and the critical "
                    "bottleneck for the entire western mountain zone. Two-lane, "
                    "winding, steep grades. No alternative routes. Many "
                    "residential streets are single-lane, unpaved, or dead-end. "
                    "1920s-era subdivisions (Cedarpines Park, Valley of "
                    "Enchantment) were platted without fire evacuation in mind."
                ),
            },
            {
                "type": "housing_stock",
                "detail": (
                    "Many homes built in 1920s-1960s before modern fire codes. "
                    "Wood frame construction, wood shake roofs, no ember-"
                    "resistant vents. Pine litter accumulation in gutters and "
                    "on roofs creates ignition pathways. USFS Grass Valley Fire "
                    "study (2007) documented the 'domino effect' in similar "
                    "mountain housing — burning homes ignite adjacent homes "
                    "through radiant heat. This building stock vulnerability "
                    "applies directly to Crestline's housing."
                ),
            },
        ],
        "historical_fires": [
            {
                "name": "Old Fire",
                "year": 2003,
                "acres": 91281,
                "structures_destroyed": 993,
                "deaths": 6,
                "detail": (
                    "Arson ignition in Waterman Canyon Oct 25, 2003. 50+ mph "
                    "Santa Ana winds. Forced evacuation of 80,000+ from ALL "
                    "mountain communities. One victim (Chad Leo Williams, 70) "
                    "died in Crestline from heart attack during evacuation. "
                    "Fire burned below Cedarpines Park, threatening SR-138 "
                    "evacuation route. Breached Rim of the World Hwy fire "
                    "lines near Skyforest, destroying 324 homes in Cedar Glen. "
                    "Part of 2003 Fire Siege. $1.2 billion damages."
                ),
            },
            {
                "name": "Slide Fire",
                "year": 2007,
                "acres": 12759,
                "structures_destroyed": 272,
                "deaths": 0,
                "detail": (
                    "Ignited Oct 22, 2007 near Green Valley Lake / Running "
                    "Springs area — adjacent to Crestline. Destroyed 272 homes. "
                    "Same day as Grass Valley Fire near Lake Arrowhead — "
                    "mountain communities hit by two fires simultaneously."
                ),
            },
            {
                "name": "Line Fire",
                "year": 2024,
                "acres": 36539,
                "structures_destroyed": 35,
                "deaths": 0,
                "detail": (
                    "Sep 2024. Crestline under evacuation WARNING while Running "
                    "Springs and Arrowbear Lake under mandatory orders. "
                    "Demonstrated that mountain evacuation creates cascading "
                    "traffic on SR-138 through Crestline even when Crestline "
                    "itself is not directly threatened."
                ),
            },
        ],
        "fire_behavior_notes": (
            "Crestline's fire vulnerability is defined by two compounding "
            "factors: (1) its position on the western rim of the escarpment "
            "makes it the FIRST community fire reaches when climbing from the "
            "San Bernardino Valley, and (2) its position on SR-138 makes it "
            "the evacuation BOTTLENECK for all communities to the east. A fire "
            "climbing the southern escarpment threatens Crestline directly "
            "while simultaneously forcing 20,000-40,000 people from Lake "
            "Arrowhead, Running Springs, and other eastern communities to "
            "evacuate THROUGH Crestline. The Old Fire (2003) demonstrated "
            "this exact scenario: fire on the escarpment below Crestline while "
            "80,000 mountain residents fled via limited routes. The 1920s-era "
            "housing stock, dense forest, bark beetle mortality, and decades "
            "of fuel accumulation create extreme structure ignition risk. A "
            "summer weekend fire during Santa Ana conditions represents a "
            "mass-casualty scenario with no adequate evacuation solution."
        ),
        "wui_class": "extreme",
    },

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

    "wrightwood_ca": {
        "center": (34.3608, -117.6334),
        "elevation_ft": 5935,
        "terrain_notes": (
            "Mountain community (pop 4,720 at 2020 census, up from 4,525 in "
            "2010) in the San Gabriel Mountains at 5,935-6,208 ft elevation, "
            "situated in Swarthout Valley — a pine-forested valley on the "
            "north slope of the San Gabriel Mountains. Wrightwood sits "
            "directly on the San Andreas Fault — the USGS Wrightwood "
            "paleoseismic site (at Swarthout Creek, 3 km NW of town) has "
            "documented 14 large earthquakes in the past 1,500 years with "
            "a mean recurrence interval of 105 years and mean slip of 3.2 m "
            "per event. The 1812 Wrightwood earthquake produced up to 170 km "
            "of surface rupture along the Mojave segment. This creates a "
            "compound hazard virtually unique in California: a community "
            "simultaneously at extreme risk from wildfire AND a major "
            "earthquake, where one event could trigger or compound the other "
            "(earthquake rupturing gas lines during fire season, or fire "
            "destroying infrastructure before earthquake strikes). "
            "\n\n"
            "The community is surrounded by Angeles National Forest on the "
            "south and west with extremely steep terrain on all sides — fire "
            "agencies describe it as 'some of the most extreme terrain crews "
            "have fought fire in the state.' Mt. Baldy (10,064 ft) rises to "
            "the west/southwest. Cajon Pass (east, 8 mi) funnels Santa Ana "
            "winds through the I-15 corridor, creating extreme fire weather. "
            "The mountains have been uplifted so rapidly along the San Andreas "
            "that erosion hasn't fully reduced slopes to stable geometries — "
            "bridges and drainages are built to contain rocky debris flows. "
            "\n\n"
            "Bridge Fire (Sep 2024) demonstrated the vulnerability: the fire "
            "'exploded' from ~4,000 to 34,000+ acres in hours on Sep 10, "
            "growing another 13,000 acres overnight. Evacuation order issued "
            "4:44 PM Sep 10 for all of Wrightwood. SR-2 fully closed from "
            "SR-138 to west of Big Pines. The fire destroyed 81 buildings "
            "and damaged 19 more (20 homes in Mt Baldy Village, 3 in "
            "Wrightwood, 6 wilderness cabins). Wrightwood's strong community "
            "preparedness proved critical: out of 2,000+ residences, only "
            "13 were destroyed (99%+ survival rate). The Wrightwood Fire "
            "Safe Council attributed this to years of defensible space "
            "advocacy — most homes had pruned grasses, saplings, and lower "
            "limbs. Mountain High Ski Resort structures all survived. "
            "\n\n"
            "Blue Cut Fire (Aug 2016) was even larger: 36,274 acres, 105 "
            "structures destroyed, 82,000 people evacuated across the region "
            "including Wrightwood, Swarthout Canyon, Lone Pine Canyon, West "
            "Cajon Valley, and Lytle Creek. I-15 (the main route between "
            "LA and Las Vegas) was fully closed through Cajon Pass. "
            "Wrightwood is a popular ski community with Mountain High Resort "
            "immediately west in Big Pines, creating significant seasonal "
            "population swings — winter ski weekends can flood the roads with "
            "LA visitors."
        ),
        "population": {
            "total_2020_census": 4720,
            "seasonal_note": (
                "Winter ski season (Mountain High Resort) brings thousands of "
                "LA-area visitors on weekends. Summer hikers and campers. "
                "Effective population can surge well beyond 4,700 residents "
                "during peak recreation periods."
            ),
        },
        "danger_quadrants": ["south", "southwest", "southeast", "west", "east"],
        "safe_quadrants": [],
        "key_features": [
            {
                "name": "San Andreas Fault",
                "bearing": "through town",
                "type": "seismic_hazard",
                "notes": (
                    "Wrightwood sits directly on the San Andreas Fault. "
                    "USGS paleoseismic site at Swarthout Creek (3 km NW) "
                    "documents 14 large earthquakes in 1,500 years (mean "
                    "recurrence 105 yrs, mean slip 3.2 m). 1812 earthquake: "
                    "up to 170 km surface rupture. Compound hazard: earthquake "
                    "could rupture gas lines during fire season, or fire could "
                    "destroy infrastructure before earthquake. Mountains "
                    "uplifted along fault so rapidly that slopes are inherently "
                    "unstable — debris flows, rockslides, and mudslides are "
                    "chronic. Post-Bridge Fire, rain caused debris/mud flows "
                    "on Hwy 2 requiring shelter-in-place orders."
                ),
            },
            {
                "name": "San Gabriel Mountains / Mt Baldy",
                "bearing": "W/SW",
                "distance_mi": 10,
                "type": "mountain",
                "notes": (
                    "Mt Baldy (10,064 ft) — highest peak in San Gabriel "
                    "Mountains. Extremely steep terrain. Bridge Fire burned "
                    "through this area Sep 2024, destroying 20 homes in "
                    "Mt Baldy Village. Fire travels upslope toward Wrightwood "
                    "from the south/southwest on extremely steep, heavily "
                    "forested slopes."
                ),
            },
            {
                "name": "Cajon Pass",
                "bearing": "E",
                "distance_mi": 8,
                "type": "wind_gap",
                "notes": (
                    "Major pass funneling Santa Ana winds from the Mojave "
                    "Desert through the I-15 corridor. Wind acceleration "
                    "through the pass creates extreme fire weather — gusts "
                    "frequently exceed 60 kt during Santa Ana events. Blue "
                    "Cut Fire (2016) burned 36,274 acres through the pass, "
                    "forcing closure of I-15 in both directions (main LA-"
                    "Vegas route). Lone Pine Canyon connects Cajon Pass to "
                    "Wrightwood — fire road gate at canyon crest."
                ),
            },
            {
                "name": "Swarthout Valley / Canyon",
                "bearing": "NW",
                "distance_mi": 1,
                "type": "valley",
                "notes": (
                    "Pine-forested valley where Wrightwood is situated. "
                    "Swarthout Creek crosses the San Andreas Fault (USGS "
                    "paleoseismic trench site). Valley is bounded by steep "
                    "mountain slopes on all sides. Early ski enthusiasts "
                    "discovered the north-facing slopes above Swarthout "
                    "Valley; Mountain High Resort developed here. Blue Cut "
                    "Fire evacuation orders included Swarthout Canyon."
                ),
            },
            {
                "name": "Angeles National Forest",
                "bearing": "S/W",
                "type": "wildland",
                "notes": (
                    "Surrounds community on south and west. Bridge Fire "
                    "(2024, 56,030 acres), Bobcat Fire (2020, 115,796 acres), "
                    "and Sheep Fire (2022) all burned in ANF near Wrightwood. "
                    "Station Fire (2009, 160,577 acres) burned farther west "
                    "in ANF. The forest has an extensive fire history with "
                    "major fires every few years."
                ),
            },
            {
                "name": "SR-2 (Angeles Crest Highway)",
                "bearing": "W",
                "type": "access_route",
                "notes": (
                    "Primary westbound route connecting Wrightwood to LA via "
                    "mountain highway. Fully closed during Bridge Fire 2024 "
                    "(from SR-138 to west of Big Pines). Frequently closed "
                    "by fire, snow, rockslides, and debris flows. Narrow "
                    "mountain road — not designed for mass evacuation. After "
                    "Bridge Fire, rain caused debris/mud flows that again "
                    "closed SR-2 and triggered shelter-in-place for Wrightwood."
                ),
            },
            {
                "name": "Big Pines Highway / Lone Pine Canyon Road",
                "bearing": "S/E",
                "type": "access_route",
                "notes": (
                    "Secondary routes. Big Pines Hwy runs south toward Big "
                    "Pines and Mountain High Resort. Lone Pine Canyon Road "
                    "connects to I-15 via Cajon Pass — goes through some of "
                    "the worst burn areas from previous fires, with scarred "
                    "hills on both sides. Both are narrow mountain roads with "
                    "limited capacity."
                ),
            },
        ],
        "evacuation": {
            "primary_routes": [
                "SR-2 west toward La Canada Flintridge / LA",
                "Lone Pine Canyon Road east to I-15 at Cajon Pass",
            ],
            "secondary_routes": [
                "Big Pines Highway south",
                "SR-2 east toward SR-138 / Palmdale",
            ],
            "bottlenecks": [
                "SR-2 is a single narrow mountain road (closed by fire, snow, debris)",
                "Lone Pine Canyon Road goes through burn scars, narrow",
                "All routes are mountain roads with no 4-lane alternatives",
            ],
            "critical_vulnerability": (
                "During Bridge Fire 2024, SR-2 was fully closed — the primary "
                "westbound route. With 4,700+ residents plus ski/recreation "
                "visitors, all routes are narrow mountain roads. Community is "
                "effectively surrounded by terrain that has burned repeatedly "
                "(Bridge 2024, Blue Cut 2016, Bobcat 2020, Sheep 2022). "
                "Post-fire debris flows add compound risk — rain after the "
                "Bridge Fire closed roads again with mud/debris. Winter "
                "ski traffic on weekends coincides with potential late-season "
                "fires and avalanche/debris risk."
            ),
        },
        "infrastructure": {
            "utility": "SCE (Southern California Edison)",
            "psps_notes": (
                "SCE implements PSPS shutoffs in the San Gabriel Mountains. "
                "Mountain community vulnerable to extended outages. Community "
                "Services District provides local governance."
            ),
            "water_system": "Wrightwood Community Services District",
            "debris_flow_infrastructure": (
                "Bridges and drainages throughout area built to contain "
                "rocky floods and debris flows from unstable slopes along "
                "San Andreas Fault zone. Post-fire hydrophobic soils "
                "dramatically increase debris flow risk — demonstrated "
                "after Bridge Fire when rain triggered shelter-in-place."
            ),
        },
        "community_preparedness": {
            "fire_safe_council": (
                "Wrightwood Fire Safe Council (501(c)(3), founded 2003). "
                "Monthly meetings third Tuesday at Community Building, "
                "1275 Hwy 2. Advocated defensible space, evacuation planning. "
                "Bridge Fire 2024 validated their work: out of 2,000+ "
                "residences, only 13 destroyed (99%+ survival rate). Most "
                "homes had defensible space per FSC recommendations. All "
                "Mountain High Resort structures survived."
            ),
            "regional_coordination": (
                "Mountain Rim Fire Safe Council Regional Project covers "
                "Wrightwood, Mt. Baldy, and Lytle Creek communities. "
                "Wildfire & Disaster Awareness Day events held at community "
                "building for education."
            ),
            "success_story": (
                "The Wrightwood Fire Safe Council is a national model for "
                "community fire preparedness. Their 20-year effort (2003-2024) "
                "to promote defensible space directly saved the community "
                "during the Bridge Fire. Media coverage (Yahoo News, local "
                "outlets) highlighted how community action prevented "
                "catastrophic losses."
            ),
        },
        "historical_fires": [
            "Bridge Fire 2024 (56,030 acres. Exploded from ~4,000 to 34,000+ acres "
            "in hours Sep 10. Evacuation order 4:44 PM. SR-2 fully closed. "
            "81 buildings destroyed, 19 damaged. Wrightwood: only 13 of 2,000+ "
            "residences destroyed thanks to defensible space program.)",
            "Blue Cut Fire 2016 (36,274 acres, 105 structures, 82,000 evacuated "
            "incl. Wrightwood/Swarthout/Lone Pine Canyons. I-15 closed through "
            "Cajon Pass. Started on Blue Cut hiking trail in San Bernardino NF.)",
            "Bobcat Fire 2020 (115,796 acres in ANF, evacuation warnings for Wrightwood)",
            "Sheep Fire 2022 (nearby in ANF, evacuation warnings)",
            "Station Fire 2009 (160,577 acres, largest in modern LA County ANF history)",
        ],
        "wui_class": "extreme",
        "compound_hazards": [
            "San Andreas Fault: 14 major earthquakes in 1,500 years at this site; "
            "mean recurrence 105 years. Community sits ON the fault. Earthquake "
            "could rupture gas lines and water mains during fire season.",
            "Post-fire debris flows: Bridge Fire burn scar + rain = mud/debris on SR-2, "
            "shelter-in-place orders. Repeat of this pattern likely after any future fire.",
            "Winter storm/fire overlap: ski community with heavy snow can have late-season "
            "fires. Snow-blocked roads + fire = no evacuation route.",
            "Cajon Pass wind acceleration: 60+ kt gusts during Santa Ana events funnel "
            "through pass directly toward community.",
            "SR-2 closure dependency: primary route frequently closed by fire, snow, "
            "rockslides, debris flows. No redundant 4-lane evacuation route exists.",
            "Seasonal population surge: Mountain High ski resort brings thousands of "
            "LA visitors on winter weekends, overwhelming mountain road capacity.",
            "Terrain instability: San Andreas uplift faster than erosion = unstable "
            "slopes, chronic rockslide and debris flow risk independent of fire.",
        ],
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

    "julian_ca": {
        "center": (33.0787, -116.6020),
        "elevation_ft": 4235,
        "terrain_notes": (
            "Small mountain town (pop 1,768 at 2020 census; ~1,490 estimated "
            "2023; median age 55.6) in San Diego backcountry at 4,235 ft in "
            "the Cuyamaca/Volcan Mountains within the Peninsular Ranges. Julian "
            "is a Gold Rush-era town (gold discovered 1869) now famous for "
            "apple orchards and tourism — during October apple season, the town "
            "bakes 10,000 apple pies per week and thousands of Southern "
            "California tourists flood the narrow mountain roads, potentially "
            "tripling or quadrupling the effective population on any given "
            "fall weekend. This creates a catastrophic evacuation scenario: "
            "1,500 residents plus thousands of tourists on 2-lane mountain "
            "highways during peak Santa Ana fire season. "
            "\n\n"
            "The town is surrounded by Cleveland National Forest with heavy "
            "chaparral and mixed-conifer fuels across diverse ecosystems from "
            "4,000 to 6,500 ft elevation (oak woodlands, conifer forests, "
            "meadows). Cedar Fire (2003) — the worst wildfire disaster in "
            "San Diego County history — burned 273,246 acres, destroyed 2,820 "
            "structures, killed 15 people (including 1 firefighter in Julian "
            "on Orchard Lane overrun by a flaming front on Oct 29), and moved "
            "at 3,600 acres/hour at peak, reaching 6,000 acres/hour during "
            "the most extreme conditions. The fire spread 2 acres per second "
            "and traveled 30+ miles southwest in under 10 hours, reaching "
            "Lakeside at 15 mph. On October 28, firefighters fired out along "
            "Hwy 78/79 from Pine Hills Road to Santa Ysabel (~7 miles) to "
            "keep the fire south of the highway. Julian itself narrowly "
            "survived. Witch Creek Fire (2007) forced full evacuation of "
            "Julian; the fire started in the Santa Ysabel area NW of town "
            "and burned 197,990 acres. "
            "\n\n"
            "Banner Grade (SR-78 east of Julian descending into the desert "
            "toward Shelter Valley and Earthquake Valley) is a critical "
            "terrain feature: extremely steep, winding descent with no "
            "shoulder, dropping from 4,200 ft to below 2,000 ft in just a "
            "few miles. This route provides the only eastbound escape but is "
            "also a potential fire corridor where desert winds funnel upslope."
        ),
        "population": {
            "total_2020_census": 1768,
            "estimated_2023": 1490,
            "median_age": 55.6,
            "tourist_peak": (
                "October apple season: 10,000 pies/week baked. Thousands of "
                "tourists from San Diego and LA flood SR-78/SR-79 on weekends. "
                "Effective daytime population may reach 5,000-8,000+ during "
                "peak apple festival weekends — during peak Santa Ana season."
            ),
        },
        "danger_quadrants": ["east", "southeast", "south", "northwest"],
        "safe_quadrants": [],
        "key_features": [
            {
                "name": "Cuyamaca Mountains",
                "bearing": "S/SE",
                "distance_mi": 5,
                "type": "mountain",
                "notes": (
                    "Cedar Fire (2003) destroyed entire community of Cuyamaca. "
                    "Heavy conifer forest with chronic drought stress. Cuyamaca "
                    "Peak (6,512 ft) creates terrain-driven fire acceleration. "
                    "Post-Cedar Fire landscape has regenerated significant "
                    "chaparral, creating new fuel loads."
                ),
            },
            {
                "name": "Cleveland National Forest",
                "bearing": "all",
                "type": "wildland",
                "notes": (
                    "Completely surrounds Julian. Both Cedar Fire and Witch "
                    "Creek Fire burned through CNF. Heavy recreational use "
                    "(camping, hiking, equestrian) creates ignition risk. "
                    "Cedar Fire was started by a lost hunter lighting a "
                    "signal fire in the CNF south of Ramona."
                ),
            },
            {
                "name": "Santa Ysabel Valley",
                "bearing": "NW",
                "distance_mi": 5,
                "type": "valley",
                "notes": (
                    "Witch Creek Fire (2007) started in the Santa Ysabel area. "
                    "Open grassland/chaparral valley that connects Julian to "
                    "Ramona via SR-78/79. Santa Ana winds accelerate through "
                    "this corridor."
                ),
            },
            {
                "name": "Banner Grade (SR-78 east)",
                "bearing": "E",
                "distance_mi": 3,
                "type": "terrain_trap",
                "notes": (
                    "Extremely steep, winding descent from Julian (4,200 ft) "
                    "into the Anza-Borrego desert toward Shelter Valley and "
                    "Earthquake Valley (below 2,000 ft). Only eastbound escape "
                    "route but also a fire corridor — desert Santa Ana winds "
                    "funnel upslope through this grade. Narrow, no shoulder, "
                    "dangerous at speed. A fire on Banner Grade would "
                    "eliminate the only eastbound evacuation option."
                ),
            },
            {
                "name": "Volcan Mountain",
                "bearing": "N",
                "distance_mi": 3,
                "type": "mountain",
                "notes": (
                    "Volcan Mountain (5,353 ft) north of Julian. Brush fire "
                    "incidents documented in steep, inaccessible terrain on "
                    "its slopes. Fires can approach Julian from the north "
                    "through this corridor."
                ),
            },
            {
                "name": "SR-78/SR-79 junction (center of town)",
                "bearing": "center",
                "type": "access_route",
                "notes": (
                    "Only major roads through town — both 2-lane mountain "
                    "highways. During Cedar Fire, sheriff's deputies and CHP "
                    "blocked traffic on Hwy 78 in Santa Ysabel and Hwy 79 "
                    "south of Cuyamaca for fire operations. The highways "
                    "served as both firebreaks and evacuation routes — "
                    "conflicting uses during a major fire. Cedar Fire jumped "
                    "the intersection of Hwys 78/79, creating a dire situation."
                ),
            },
        ],
        "evacuation": {
            "primary_routes": [
                "SR-79 south toward Cuyamaca/Descanso/I-8",
                "SR-78/79 west toward Santa Ysabel/Ramona",
            ],
            "secondary_routes": [
                "SR-78 east down Banner Grade toward Scissors Crossing/S2",
                "SR-79 north toward Warner Springs",
            ],
            "bottlenecks": [
                "SR-78/79 junction in center of town (single intersection)",
                "Banner Grade (steep, narrow, no shoulder)",
                "Santa Ysabel corridor (Witch Creek Fire origin zone)",
            ],
            "critical_vulnerability": (
                "During peak apple season (October = peak Santa Ana season), "
                "thousands of tourists are on narrow mountain roads. A fire "
                "blocking SR-78/79 to the west and SR-79 to the south would "
                "leave Banner Grade (steep, dangerous descent) as the only "
                "escape route for potentially 5,000+ people. All routes are "
                "2-lane mountain highways with no widening planned."
            ),
        },
        "infrastructure": {
            "utility": "SDG&E",
            "fire_hardening": (
                "SDG&E replaced wood poles with fire-resistant steel poles "
                "rated to 85 mph winds (some to 111 mph) in the Julian area. "
                "Strategic undergrounding project along Banner Road (SR-78) "
                "and Cape Horn Avenue east of downtown Julian to reduce "
                "wildfire risk and keep critical facilities powered during "
                "PSPS shutoffs. Facilities benefiting: post office, county "
                "library, Julian Union High School, Julian Charter School, "
                "Julian Elementary School, CAL FIRE Station."
            ),
            "water_system": (
                "Small community water system. During Witch Creek Fire 2007, "
                "power lines connecting water pumps burned, leaving residents "
                "without water for a week even after returning home."
            ),
            "cell_coverage": (
                "Mountain terrain creates coverage gaps. Remote location "
                "means limited tower density. Emergency communication "
                "reliability is a concern during fire events."
            ),
        },
        "community_preparedness": {
            "cwpp": (
                "Julian 2023 Community Wildfire Protection Plan published "
                "by San Diego County Fire Safe Council. Identifies specific "
                "fuel treatment priorities and evacuation improvements."
            ),
            "fire_safe_council": (
                "Julian Fire Safe Council (part of Backcountry Communities "
                "Thriving initiative) cooperates with CAL FIRE and SD County "
                "Fire. Promotes Firewise activities, structural hardening "
                "to meet/exceed County Building and Fire Code requirements."
            ),
        },
        "historical_fires": [
            "Cedar Fire 2003 (273,246 acres, 2,820 structures, 15 killed incl. 1 "
            "firefighter on Orchard Lane in Julian. Spread rate: 3,600-6,000 "
            "acres/hr, 2 acres/sec at peak. 30+ mi in <10 hrs. Started by "
            "lost hunter signaling with fire in CNF.)",
            "Witch Creek Fire 2007 (197,990 acres, 1,650 structures, 2 killed. "
            "Full evacuation of Julian. Started in Santa Ysabel area.)",
        ],
        "wui_class": "extreme",
        "compound_hazards": [
            "Tourist/resident evacuation conflict: peak apple season = peak fire season",
            "Banner Grade terrain trap: only eastbound escape is steep/dangerous",
            "Water system depends on power lines through fire zone",
            "Winter ice storms close SR-78/SR-79 (snow closures documented Feb 2019, "
            "2023) — compound hazard if ice precedes late-season fire",
            "5.2 magnitude earthquake struck near Julian April 2025 — seismic risk",
            "Remote location: fire response times measured in tens of minutes",
            "All evacuation routes are also potential fire corridors",
        ],
    },

    "ramona_ca": {
        "center": (33.0422, -116.8681),
        "elevation_ft": 1394,
        "terrain_notes": (
            "Large unincorporated community (pop 21,468 at 2020 census; ~22,800 "
            "estimated 2023; planning area 84,000+ acres / 130+ sq mi) in San "
            "Diego County backcountry at 1,394 ft elevation. Population has "
            "nearly doubled over the past 35 years, with continued development "
            "pushing into chaparral-covered hillsides. Ramona sits in a valley "
            "surrounded by chaparral hills with the Cuyamaca Mountains and "
            "Cleveland National Forest to the east. The entire area outside "
            "the Town Center is classified as fire-vulnerable, and all "
            "adjacent undeveloped areas are similarly at risk. California "
            "has proposed raising fire severity ratings from medium/high to "
            "'very high' for much of the Ramona planning area. "
            "\n\n"
            "Ramona's fire history is among the worst in California: the "
            "Cedar Fire (2003) burned ~50 sq mi on the south side of the "
            "community and killed 12 people in the Wildcat Canyon area "
            "southeast of town. Eight of those 12 died on Strange Way — a "
            "remote road off Wildcat Canyon Road that doesn't appear on "
            "official maps — with little or no warning that the fire was "
            "approaching. Victims included a mechanic and his wife fleeing "
            "in their car, a Walmart cashier with her 17-year-old daughter "
            "and relative at home, and a 77-year-old retired gardener. "
            "Firefighters were stymied by the difficult canyon terrain. "
            "\n\n"
            "The Witch Creek Fire (2007) was even more devastating locally: "
            "it swept over the east, north, and west sides of Ramona, "
            "burning nearly 70 sq mi. Combined with the simultaneous "
            "Guejito Fire, 1,141 homes and 509 outbuildings were destroyed "
            "in Ramona, Poway, Rancho Bernardo, Escondido, Del Dios, and "
            "Rancho Santa Fe. Ramona was ordered evacuated the first night, "
            "causing gridlock on SR-67 and SR-78 — evacuees spent hours on "
            "the two main routes with some drivers running out of gas en "
            "route. Power lines connecting water pumps burned, leaving "
            "residents without drinking water for a week after returning."
        ),
        "population": {
            "total_2020_census": 21468,
            "combined_area_2010": 30301,
            "estimated_2023": 22800,
            "growth_note": (
                "Population nearly doubled in 35 years. Continued rural "
                "residential development pushes WUI boundary deeper into "
                "chaparral. Many outlying residents not served by Ramona "
                "Municipal Water District, depend on wells."
            ),
        },
        "danger_quadrants": ["east", "northeast", "southeast", "north"],
        "safe_quadrants": ["west"],
        "key_features": [
            {
                "name": "Wildcat Canyon",
                "bearing": "SE",
                "distance_mi": 3,
                "type": "canyon",
                "notes": (
                    "Cedar Fire death zone: 12 of 15 total Cedar Fire "
                    "fatalities occurred in Wildcat Canyon/Muth Valley area. "
                    "8 died on Strange Way, a remote road off Wildcat Canyon "
                    "Road not shown on official maps. Serpentine road from "
                    "Ramona through Indian reservation into Lakeside. Extreme "
                    "fire behavior in canyon terrain — firefighters could not "
                    "reach victims due to terrain and fire intensity."
                ),
            },
            {
                "name": "Cleveland National Forest",
                "bearing": "E/NE",
                "distance_mi": 5,
                "type": "wildland",
                "notes": (
                    "Fire source zone during Santa Ana events. Both Cedar "
                    "and Witch Creek fires originated east of Ramona and "
                    "burned through CNF. Continuous wildland fuel from "
                    "mountains to town with no fire break."
                ),
            },
            {
                "name": "San Vicente Reservoir / San Diego River headwaters",
                "bearing": "S/SW",
                "distance_mi": 5,
                "type": "water_feature",
                "notes": (
                    "San Diego River headwaters originate in the chaparral-"
                    "filled valleys east of Ramona. Reservoir area provides "
                    "some break in fuels to the south but surrounding terrain "
                    "is heavily vegetated chaparral."
                ),
            },
            {
                "name": "Ramona Airport (KRNM)",
                "bearing": "E",
                "distance_mi": 2,
                "type": "infrastructure",
                "notes": (
                    "CAL FIRE air tanker base, critical for aerial fire "
                    "suppression in San Diego backcountry. Ramona Air Attack "
                    "Base supports initial attack on fires throughout the "
                    "region. Airport itself surrounded by chaparral."
                ),
            },
            {
                "name": "SR-67 corridor",
                "bearing": "SW",
                "type": "access_route",
                "notes": (
                    "Primary route to San Diego metro (Lakeside, El Cajon). "
                    "Currently 2 lanes through most of Ramona area. During "
                    "Witch Creek Fire 2007, evacuees spent hours gridlocked "
                    "on SR-67, some running out of gas. SANDAG budgeted $21M "
                    "for design/EIR to widen SR-67 to 4 lanes from Highland "
                    "Valley Road to Mapleview Street in Lakeside. Project "
                    "not yet constructed as of 2026."
                ),
            },
            {
                "name": "SR-78 corridor",
                "bearing": "E-W",
                "type": "access_route",
                "notes": (
                    "East-west route connecting Ramona to Julian (east) and "
                    "Escondido/I-15 (west). Also gridlocked during Witch "
                    "Creek Fire evacuation. Combined SR-67/SR-78 traffic "
                    "during mass evacuation overwhelms road capacity."
                ),
            },
        ],
        "evacuation": {
            "primary_routes": [
                "SR-67 south toward Lakeside/El Cajon/San Diego",
                "SR-78 west toward Escondido/I-15",
            ],
            "secondary_routes": [
                "SR-78 east toward Julian (uphill, into fire zone during Santa Ana events)",
                "Highland Valley Road, Mussey Grade Road (narrow rural roads)",
            ],
            "bottlenecks": [
                "SR-67 through Lakeside (2-lane, winding)",
                "SR-67/SR-78 junction in Ramona",
                "All routes funnel through limited chokepoints",
            ],
            "critical_vulnerability": (
                "21,000+ residents (30,000+ with San Diego Country Estates) "
                "on two 2-lane highways. Witch Creek Fire 2007 proved this "
                "is insufficient: hours of gridlock, drivers running out of "
                "gas. SR-67 widening ($21M SANDAG design study) not yet "
                "constructed. Community leaders describe evacuation routes "
                "as 'limited' and widening as 'urgent' for emergency safety."
            ),
            "sr67_widening": (
                "SANDAG budgeted $21M toward design and EIR for SR-67 "
                "widening to 4 lanes between Highland Valley Road (Ramona) "
                "and Mapleview Street (Lakeside). Ramona community leaders "
                "advocate urgently but project remains in planning phase."
            ),
        },
        "infrastructure": {
            "utility": "SDG&E",
            "fire_hardening": (
                "SDG&E replaced 34,000 wood poles with fire-resistant steel "
                "poles in backcountry since 2007 (Ramona, Julian, Descanso). "
                "SDG&E Fire Science & Climate Adaptation Dept employs 6 "
                "full-time meteorologists monitoring fire weather. Technosylva "
                "fire behavior modeling integrated into grid management."
            ),
            "water_system": (
                "Ramona Municipal Water District serves core area. Many "
                "outlying/rural residents depend on wells. Highland Valley "
                "area has separate agricultural water system for avocado "
                "groves. During Witch Creek Fire 2007, power lines connecting "
                "water pumps burned — residents without water for a week "
                "after returning home. Well-dependent households especially "
                "vulnerable (electric pumps fail during PSPS or fire-caused "
                "power outage)."
            ),
        },
        "community_preparedness": {
            "fire_safe_council": (
                "Ramona West End Fire Safe Council active in community "
                "education and fuel management. Focus on defensible space "
                "and structural hardening in the expanding WUI."
            ),
            "lessons_learned": (
                "2003 and 2007 fires transformed community awareness. "
                "San Diego Union-Tribune 'Searing Lessons' retrospective "
                "(2017) documented how the fires changed building codes, "
                "evacuation planning, and utility practices. SDG&E's "
                "post-2007 steel pole replacement program was a direct "
                "response to Witch Creek Fire infrastructure failures."
            ),
        },
        "historical_fires": [
            "Cedar Fire 2003 (273,246 total acres, 15 killed — 12 in Wildcat Canyon "
            "near Ramona. ~50 sq mi burned on south side of community. Fire moved "
            "at 3,600-6,000 acres/hr, 2 acres/sec at peak. 30+ mi in <10 hrs.)",
            "Witch Creek Fire 2007 (197,990 acres, 1,650 structures, 2 killed. "
            "Swept over east/north/west sides of Ramona, ~70 sq mi. Combined with "
            "Guejito Fire: 1,141 homes + 509 outbuildings destroyed across region. "
            "Ramona evacuees gridlocked on SR-67/SR-78 for hours.)",
        ],
        "wui_class": "extreme",
        "compound_hazards": [
            "Rapid population growth into fire-prone chaparral (doubled in 35 yrs)",
            "Evacuation routes proven inadequate in 2007 (gridlock, fuel exhaustion)",
            "SR-67 widening still not constructed despite SANDAG $21M allocation",
            "Well-dependent rural households lose water during power outages",
            "Power line/water pump interdependency (both failed in 2007)",
            "Wildcat Canyon terrain trap (12 Cedar Fire deaths in canyon with no escape)",
            "All surrounding areas are fire-vulnerable (no defensible buffer zone)",
            "Upwind of San Diego metro: fires starting here threaten 3+ million people",
        ],
    },

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
    # TEHACHAPI / KERN MOUNTAINS
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




# =============================================================================
# IGNITION SOURCES
# =============================================================================

CA_IGNITION_SOURCES = {

    "paradise_ca": {
        "primary": [
            {
                "source": "PG&E power lines",
                "risk": "EXTREME",
                "detail": (
                    "Camp Fire was started by PG&E Caribou-Palermo "
                    "transmission line failure in Feather River Canyon. "
                    "A worn C-hook on a 115 kV tower snapped, dropping "
                    "an energized line onto the tower. PG&E infrastructure "
                    "runs throughout canyon terrain. PG&E was convicted of "
                    "84 counts of involuntary manslaughter."
                ),
            },
            {
                "source": "Vegetation / fuel loads",
                "risk": "HIGH",
                "detail": (
                    "Dense pine, cedar, and oak forest with accumulated "
                    "fuel loads from decades of fire suppression. Long "
                    "summer drought cures fuels to extreme levels."
                ),
            },
        ],
        "corridors": [
            {
                "name": "PG&E Caribou-Palermo transmission line",
                "direction": "NE-SW",
                "risk": "Exact ignition source of Camp Fire — runs through Feather River Canyon",
            },
            {
                "name": "Hwy 70 through Feather River Canyon",
                "direction": "E-W",
                "risk": "Power line and vehicle ignition corridor",
            },
        ],
    },

    "magalia_ca": {
        "primary": [
            {
                "source": "PG&E power lines",
                "risk": "EXTREME",
                "detail": "Same PG&E infrastructure as Paradise. Transmission and distribution lines through forested terrain.",
            },
            {
                "source": "Vegetation / fuel loads",
                "risk": "HIGH",
                "detail": "Denser forest than Paradise at higher elevation. Heavy pine/cedar canopy.",
            },
        ],
        "corridors": [
            {
                "name": "PG&E distribution lines through forest",
                "direction": "multiple",
                "risk": "Overhead lines through dense canopy, tree strike risk",
            },
        ],
    },

    "santa_rosa_ca": {
        "primary": [
            {
                "source": "PG&E power lines",
                "risk": "EXTREME",
                "detail": (
                    "Tubbs Fire (2017) — while CAL FIRE attributed ignition "
                    "to a private electrical system, PG&E settled for $13.5B "
                    "across 2017 fires. Nuns Fire started when wind knocked "
                    "alder tree into powerline. Glass Fire (2020) cause "
                    "under investigation."
                ),
            },
            {
                "source": "Diablo wind events",
                "risk": "HIGH",
                "detail": (
                    "Offshore foehn winds (NE) create extreme fire weather. "
                    "Low humidity, high winds, warm temperatures. Wind can "
                    "turn small ignitions into urban conflagrations."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Mark West Springs Road corridor",
                "direction": "NE-SW",
                "risk": "Tubbs Fire corridor — power lines, vegetation, WUI",
            },
            {
                "name": "Calistoga / Knights Valley powerline corridor",
                "direction": "NE",
                "risk": "Source area for multiple Diablo wind-driven fires",
            },
        ],
    },

    "sonoma_ca": {
        "primary": [
            {
                "source": "Power lines during wind events",
                "risk": "HIGH",
                "detail": (
                    "Nuns Fire (2017) started when wind knocked tree into "
                    "powerline near Glen Ellen. Power infrastructure through "
                    "rural forested terrain."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Hwy 12 corridor through Sonoma Valley",
                "direction": "NW-SE",
                "risk": "Power lines, rural ignition sources",
            },
        ],
    },

    "malibu_ca": {
        "primary": [
            {
                "source": "Santa Ana wind events",
                "risk": "EXTREME",
                "detail": (
                    "Every major Malibu fire has been driven by Santa Anas. "
                    "60-80+ mph gusts push fire through mountain terrain to "
                    "coast. RH drops to single digits."
                ),
            },
            {
                "source": "Southern California Edison power lines",
                "risk": "HIGH",
                "detail": (
                    "Thomas Fire (2017) caused by SCE power lines. "
                    "Woolsey Fire (2018) started at SCE equipment near "
                    "Santa Susana Field Lab. Power infrastructure through "
                    "rugged mountain terrain."
                ),
            },
            {
                "source": "Arson / human causes",
                "risk": "HIGH",
                "detail": (
                    "High recreational use of Santa Monica Mountains NRA "
                    "and beaches. Numerous small fires from campfires, "
                    "fireworks, and arson."
                ),
            },
        ],
        "corridors": [
            {
                "name": "PCH / Malibu Canyon Road junction",
                "direction": "N-S",
                "risk": "Major access point, fire funnels down canyons",
            },
            {
                "name": "Kanan Dume Road corridor",
                "direction": "N-S",
                "risk": "Fire corridor through Santa Monica Mtns",
            },
        ],
    },

    "pacific_palisades_ca": {
        "primary": [
            {
                "source": "Undetermined (Palisades Fire 2025)",
                "risk": "EXTREME",
                "detail": (
                    "Palisades Fire (Jan 7, 2025) cause under investigation. "
                    "Started in brush along Temescal Ridge during extreme "
                    "Santa Ana wind event with gusts 60-80+ mph. Destroyed "
                    "6,837 structures."
                ),
            },
            {
                "source": "Santa Ana winds",
                "risk": "EXTREME",
                "detail": (
                    "NWS predicted 'life-threatening' windstorm prior to "
                    "Palisades Fire. Gusts to 90+ mph in mountain areas. "
                    "Any ignition becomes catastrophic in these conditions."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Temescal Ridge / Canyon",
                "direction": "N-S",
                "risk": "Palisades Fire ignition area, fire corridor into community",
            },
            {
                "name": "Topanga State Park interface",
                "direction": "NW",
                "risk": "16,000 acres of chaparral wildland directly adjacent",
            },
        ],
    },

    "topanga_ca": {
        "primary": [
            {
                "source": "Chaparral fire cycle",
                "risk": "EXTREME",
                "detail": (
                    "Chaparral in Santa Monica Mountains burns on roughly "
                    "20-year cycle. Dense, oil-rich fuels (chamise, "
                    "manzanita, ceanothus) are explosive when cured. "
                    "Community sits in middle of this fuel bed."
                ),
            },
            {
                "source": "Human ignition",
                "risk": "HIGH",
                "detail": (
                    "Heavy recreational use. Topanga State Park visitors. "
                    "Vehicle-related ignitions on canyon road."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Topanga Canyon Blvd",
                "direction": "N-S",
                "risk": "Only road through community, vehicle ignition risk",
            },
        ],
    },

    "altadena_ca": {
        "primary": [
            {
                "source": "Electrical distribution lines",
                "risk": "EXTREME",
                "detail": (
                    "NPR/CAL FIRE investigation found SCE distribution "
                    "lines failed hours before the Eaton Fire started in "
                    "Altadena. Power infrastructure in foothill terrain "
                    "subject to extreme Santa Ana wind loading."
                ),
            },
            {
                "source": "Santa Ana wind events",
                "risk": "EXTREME",
                "detail": (
                    "Eaton Fire burned during strongest Santa Ana winds in "
                    "over a decade. Hurricane-force gusts at foothills of "
                    "San Gabriels pushed fire downhill into community."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Eaton Canyon drainage",
                "direction": "N-S",
                "risk": "Eaton Fire ignition and spread corridor",
            },
            {
                "name": "Mountain front from La Canada to Sierra Madre",
                "direction": "W-E",
                "risk": "Continuous WUI interface along San Gabriel front",
            },
        ],
    },

    "la_canada_flintridge_ca": {
        "primary": [
            {
                "source": "Angeles National Forest fires",
                "risk": "EXTREME",
                "detail": (
                    "Station Fire (2009) started along Angeles Crest Hwy, "
                    "suspected arson. Burned 160,577 acres of Angeles NF "
                    "directly above the city. 657,000 acres of wildland "
                    "borders the city."
                ),
            },
            {
                "source": "Angeles Crest Highway traffic",
                "risk": "HIGH",
                "detail": (
                    "Heavy recreational traffic on SR-2 creates ignition "
                    "risk from vehicles, campfires. Station Fire started "
                    "near a ranger station along this road."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Angeles Crest Highway (SR-2)",
                "direction": "N",
                "risk": "Primary ignition corridor — Station Fire origin area",
            },
            {
                "name": "Arroyo Seco drainage",
                "direction": "NW-SE",
                "risk": "Canyon fire corridor from mountains through Pasadena",
            },
        ],
    },

    "redding_ca": {
        "primary": [
            {
                "source": "Vehicle / mechanical",
                "risk": "EXTREME",
                "detail": (
                    "Carr Fire (2018) started from sparks when a trailer "
                    "tire blew out and its wheel rim scraped the road on "
                    "Hwy 299. Triple-digit heat and bone-dry fuels turned "
                    "road sparks into a 229,651-acre catastrophe with a "
                    "fire tornado."
                ),
            },
            {
                "source": "Power lines",
                "risk": "HIGH",
                "detail": (
                    "Zogg Fire (2020) caused by PG&E pine tree contacting "
                    "power line. Rural power infrastructure in heavy timber."
                ),
            },
            {
                "source": "Extreme heat / lightning",
                "risk": "HIGH",
                "detail": (
                    "Redding regularly exceeds 105-110F in summer. Dry "
                    "lightning from monsoonal moisture can ignite fires "
                    "in remote terrain."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Hwy 299 through Whiskeytown",
                "direction": "E-W",
                "risk": "Carr Fire origin corridor — vehicle ignition risk",
            },
            {
                "name": "I-5 / Sacramento River corridor",
                "direction": "N-S",
                "risk": "Vehicle ignition, power line corridor",
            },
        ],
    },

    "ojai_ca": {
        "primary": [
            {
                "source": "SCE power lines",
                "risk": "EXTREME",
                "detail": (
                    "Thomas Fire (2017) caused by SCE power lines making "
                    "contact in high winds near Santa Paula. Power "
                    "infrastructure through mountainous terrain."
                ),
            },
            {
                "source": "Sundowner wind events",
                "risk": "HIGH",
                "detail": (
                    "Ojai Valley experiences unique 'Sundowner' winds — "
                    "hot, dry downslope winds off the mountains that occur "
                    "in late afternoon/evening. Creates critical fire weather."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Hwy 150 (Santa Paula to Ojai)",
                "direction": "E-W",
                "risk": "Thomas Fire approach corridor — power lines, terrain",
            },
            {
                "name": "Matilija Canyon / Hwy 33",
                "direction": "N",
                "risk": "Fire corridor from Los Padres NF into Ojai Valley",
            },
        ],
    },

    "ventura_ca": {
        "primary": [
            {
                "source": "SCE power lines",
                "risk": "EXTREME",
                "detail": (
                    "Thomas Fire (2017) was SCE power line ignition. "
                    "Same utility infrastructure issues as Ojai area."
                ),
            },
            {
                "source": "Vegetation management gaps",
                "risk": "HIGH",
                "detail": (
                    "Urban-wildland interface along Foothill Rd has "
                    "inconsistent vegetation management."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Hwy 126 corridor from Santa Paula",
                "direction": "E-W",
                "risk": "Thomas Fire approach route, power line corridor",
            },
            {
                "name": "Ventura River drainage",
                "direction": "N-S",
                "risk": "Fire corridor from mountains to coast",
            },
        ],
    },

    "lake_arrowhead_ca": {
        "primary": [
            {
                "source": "Arson",
                "risk": "EXTREME",
                "detail": (
                    "Old Fire (2003) was arson-caused. Line Fire (2024) — "
                    "a man was arrested on suspicion of arson. Mountain "
                    "communities have elevated arson risk due to dense "
                    "forest and steep terrain."
                ),
            },
            {
                "source": "Power lines in timber",
                "risk": "HIGH",
                "detail": (
                    "Overhead power lines through dense conifer forest. "
                    "Wind and snow loading cause tree contacts."
                ),
            },
            {
                "source": "Recreational visitors",
                "risk": "HIGH",
                "detail": (
                    "Heavy tourism to mountain resort areas. Campfires, "
                    "vehicle exhaust, cigarettes in drought-stressed forest."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Hwy 18 (Rim of the World)",
                "direction": "E-W",
                "risk": "Vehicle ignition along mountain road",
            },
            {
                "name": "Hwy 330 (from Highland)",
                "direction": "S-N",
                "risk": "Old Fire climbed this corridor from valley floor",
            },
        ],
    },

    "crestline_ca": {
        "primary": [
            {
                "source": "Arson / human causes",
                "risk": "EXTREME",
                "detail": "Same arson risk as Lake Arrowhead. Old Fire was arson-caused.",
            },
            {
                "source": "Power lines",
                "risk": "HIGH",
                "detail": "Mountain power infrastructure in dense forest.",
            },
        ],
        "corridors": [
            {
                "name": "Hwy 138 corridor",
                "direction": "E-W",
                "risk": "Vehicle and power line ignition corridor along rim",
            },
        ],
    },

    "julian_ca": {
        "primary": [
            {
                "source": "Human-caused in wildland",
                "risk": "EXTREME",
                "detail": (
                    "Cedar Fire (2003) started by a lost hunter lighting "
                    "a signal fire. Cleveland National Forest surrounds "
                    "Julian with heavy recreational use."
                ),
            },
            {
                "source": "Santa Ana wind-driven spread",
                "risk": "EXTREME",
                "detail": (
                    "Once ignited, Santa Ana winds drive fires at extreme "
                    "rates. Cedar Fire moved 29 miles in 10 hours, "
                    "2 acres per second at peak."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Cleveland National Forest surrounding Julian",
                "direction": "all",
                "risk": "Continuous wildland fuel, any ignition can reach town",
            },
            {
                "name": "Hwy 78/79 through mountains",
                "direction": "multiple",
                "risk": "Vehicle ignition on mountain roads",
            },
        ],
    },

    "ramona_ca": {
        "primary": [
            {
                "source": "Wildland fire from east",
                "risk": "EXTREME",
                "detail": (
                    "Santa Ana winds push fires from mountains and "
                    "backcountry westward through Ramona toward coast. "
                    "Both Cedar and Witch Creek fires affected Ramona."
                ),
            },
            {
                "source": "Rural / agricultural ignition",
                "risk": "HIGH",
                "detail": (
                    "Ranch land, agricultural operations, rural power "
                    "lines create ignition sources."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Wildcat Canyon / San Vicente corridor",
                "direction": "E-W",
                "risk": "Cedar Fire death zone — 12 fatalities in canyon",
            },
        ],
    },

    "grass_valley_ca": {
        "primary": [
            {
                "source": "Power lines in forest",
                "risk": "EXTREME",
                "detail": (
                    "PG&E infrastructure throughout forested foothills. "
                    "Same type of aging infrastructure that caused "
                    "Camp Fire in nearby Butte County."
                ),
            },
            {
                "source": "Recreational / human activity",
                "risk": "HIGH",
                "detail": (
                    "South Yuba River Canyon is a popular recreation area. "
                    "Campfires, vehicles, equipment use in dry forest."
                ),
            },
            {
                "source": "Vegetation / fuel accumulation",
                "risk": "HIGH",
                "detail": (
                    "Decades of fire suppression have created extreme fuel "
                    "loads. Dense understory beneath pine/oak canopy."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Hwy 49 corridor through foothills",
                "direction": "N-S",
                "risk": "Power lines, vehicle traffic through dense WUI",
            },
            {
                "name": "South Yuba River Canyon",
                "direction": "NE",
                "risk": "Recreational ignition sources, steep terrain",
            },
        ],
    },

    "nevada_city_ca": {
        "primary": [
            {
                "source": "PG&E power lines",
                "risk": "EXTREME",
                "detail": "Same PG&E aging infrastructure concerns as Grass Valley.",
            },
            {
                "source": "Forest fuel loading",
                "risk": "HIGH",
                "detail": (
                    "Historic town surrounded by forest. Decades of "
                    "suppression have created ladder fuels throughout."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Hwy 49 / Deer Creek corridor",
                "direction": "through town",
                "risk": "Power lines, dense vegetation, limited access",
            },
        ],
    },

    "wrightwood_ca": {
        "primary": [
            {
                "source": "Fire from Angeles National Forest",
                "risk": "EXTREME",
                "detail": (
                    "Bridge Fire (2024) burned 56,030 acres of ANF and "
                    "threatened Wrightwood. Community surrounded by "
                    "National Forest on south and west."
                ),
            },
            {
                "source": "Cajon Pass wind acceleration",
                "risk": "HIGH",
                "detail": (
                    "Santa Ana winds accelerate through Cajon Pass. "
                    "Blue Cut Fire (2016) burned 36,274 acres through pass."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Cajon Pass / I-15",
                "direction": "E",
                "risk": "Wind gap, vehicle ignition, power lines",
            },
            {
                "name": "Angeles Crest Highway (SR-2)",
                "direction": "W",
                "risk": "Fire corridor from Angeles NF",
            },
        ],
    },

    "thousand_oaks_ca": {
        "primary": [
            {
                "source": "SCE power equipment",
                "risk": "EXTREME",
                "detail": (
                    "Woolsey Fire (2018) started at or near SCE equipment "
                    "at the Santa Susana Field Laboratory. CPUC investigation "
                    "documented the ignition source."
                ),
            },
            {
                "source": "Santa Ana / Sundowner winds",
                "risk": "HIGH",
                "detail": (
                    "Ventura County experiences both Santa Ana winds and "
                    "Sundowner winds. Either can drive rapid fire spread "
                    "through chaparral terrain."
                ),
            },
        ],
        "corridors": [
            {
                "name": "Santa Susana Pass / Simi Hills",
                "direction": "NE",
                "risk": "Woolsey Fire origin area, power infrastructure",
            },
            {
                "name": "Santa Monica Mountains canyons (S)",
                "direction": "S",
                "risk": "Fire corridors to Malibu coast",
            },
        ],
    },
}


# =============================================================================
# CLIMATOLOGY
#
# Nearest ASOS/AWOS stations with fire season monthly normals.
# Fire season for California: June-December (SoCal extends through Feb for
# Santa Ana season; NorCal peaks Oct-Nov for Diablo winds).
#
# Data sourced from NOAA ISD normals, WRCC summaries, and IEM ASOS archives.
# Temperatures in F, dewpoints in F, RH in %, wind gusts in kt.
#
# Mapping:
#   KOVE (Oroville) — Paradise, Magalia
#   KSTS (Santa Rosa / Sonoma County) — Santa Rosa, Sonoma
#   KCMA (Camarillo) — Malibu, Pacific Palisades, Topanga, Thousand Oaks
#   KBUR (Burbank) — Altadena, La Canada Flintridge
#   KRDD (Redding) — Redding
#   KOXR (Oxnard) — Ventura, Ojai
#   KSBD (San Bernardino Intl) — Lake Arrowhead, Crestline (valley station)
#   KRNM (Ramona) — Julian, Ramona
#   KAUN (Auburn) — Grass Valley, Nevada City
#   KWJF (Lancaster / Gen Wm J Fox) — Wrightwood (desert-side proxy)
# =============================================================================

CA_CLIMATOLOGY = {

    # -------------------------------------------------------------------------
    # KOVE — Oroville Municipal Airport (Paradise, Magalia area)
    # Lat 39.49N, Lon 121.62W, Elev 191 ft
    # -------------------------------------------------------------------------
    "KOVE": {
        "_station_info": {
            "name": "Oroville Municipal Airport",
            "lat": 39.49,
            "lon": -121.62,
            "elevation_ft": 191,
            "serves": ["paradise_ca", "magalia_ca"],
        },
        6: {  # June
            "normal_high_f": 96, "normal_low_f": 62,
            "rh_typical_min": 15, "rh_extreme_min": 7, "rh_low_days": 10,
            "dp_typical_low_f": 45, "dp_extreme_low_f": 30,
            "gust_typical_max_kt": 20, "gust_significant_kt": 30, "gust_extreme_kt": 40,
        },
        7: {  # July
            "normal_high_f": 103, "normal_low_f": 66,
            "rh_typical_min": 10, "rh_extreme_min": 5, "rh_low_days": 15,
            "dp_typical_low_f": 42, "dp_extreme_low_f": 25,
            "gust_typical_max_kt": 20, "gust_significant_kt": 28, "gust_extreme_kt": 38,
        },
        8: {  # August
            "normal_high_f": 101, "normal_low_f": 64,
            "rh_typical_min": 10, "rh_extreme_min": 5, "rh_low_days": 15,
            "dp_typical_low_f": 43, "dp_extreme_low_f": 25,
            "gust_typical_max_kt": 18, "gust_significant_kt": 28, "gust_extreme_kt": 38,
        },
        9: {  # September
            "normal_high_f": 96, "normal_low_f": 60,
            "rh_typical_min": 12, "rh_extreme_min": 6, "rh_low_days": 12,
            "dp_typical_low_f": 40, "dp_extreme_low_f": 20,
            "gust_typical_max_kt": 20, "gust_significant_kt": 30, "gust_extreme_kt": 45,
        },
        10: {  # October — peak Diablo wind season for NorCal
            "normal_high_f": 84, "normal_low_f": 52,
            "rh_typical_min": 15, "rh_extreme_min": 6, "rh_low_days": 8,
            "dp_typical_low_f": 32, "dp_extreme_low_f": 10,
            "gust_typical_max_kt": 25, "gust_significant_kt": 40, "gust_extreme_kt": 55,
            "notes": "Peak Diablo wind season. Jarbo winds can exceed 50+ kt through Feather River Canyon.",
        },
        11: {  # November — Camp Fire month
            "normal_high_f": 65, "normal_low_f": 43,
            "rh_typical_min": 20, "rh_extreme_min": 8, "rh_low_days": 5,
            "dp_typical_low_f": 28, "dp_extreme_low_f": 8,
            "gust_typical_max_kt": 25, "gust_significant_kt": 40, "gust_extreme_kt": 55,
            "notes": "Camp Fire occurred Nov 8, 2018. Jarbo winds 40+ mph with single-digit RH.",
        },
        12: {  # December
            "normal_high_f": 55, "normal_low_f": 37,
            "rh_typical_min": 30, "rh_extreme_min": 15, "rh_low_days": 3,
            "dp_typical_low_f": 28, "dp_extreme_low_f": 12,
            "gust_typical_max_kt": 20, "gust_significant_kt": 35, "gust_extreme_kt": 50,
        },
    },

    # -------------------------------------------------------------------------
    # KSTS — Charles M. Schulz / Sonoma County Airport (Santa Rosa, Sonoma)
    # Lat 38.51N, Lon 122.81W, Elev 129 ft
    # -------------------------------------------------------------------------
    "KSTS": {
        "_station_info": {
            "name": "Charles M. Schulz / Sonoma County Airport",
            "lat": 38.51,
            "lon": -122.81,
            "elevation_ft": 129,
            "serves": ["santa_rosa_ca", "sonoma_ca"],
        },
        6: {
            "normal_high_f": 83, "normal_low_f": 50,
            "rh_typical_min": 20, "rh_extreme_min": 10, "rh_low_days": 5,
            "dp_typical_low_f": 45, "dp_extreme_low_f": 32,
            "gust_typical_max_kt": 22, "gust_significant_kt": 30, "gust_extreme_kt": 40,
        },
        7: {
            "normal_high_f": 87, "normal_low_f": 52,
            "rh_typical_min": 18, "rh_extreme_min": 8, "rh_low_days": 8,
            "dp_typical_low_f": 48, "dp_extreme_low_f": 35,
            "gust_typical_max_kt": 22, "gust_significant_kt": 28, "gust_extreme_kt": 38,
        },
        8: {
            "normal_high_f": 87, "normal_low_f": 52,
            "rh_typical_min": 18, "rh_extreme_min": 8, "rh_low_days": 8,
            "dp_typical_low_f": 48, "dp_extreme_low_f": 35,
            "gust_typical_max_kt": 20, "gust_significant_kt": 28, "gust_extreme_kt": 38,
        },
        9: {
            "normal_high_f": 87, "normal_low_f": 52,
            "rh_typical_min": 15, "rh_extreme_min": 6, "rh_low_days": 6,
            "dp_typical_low_f": 42, "dp_extreme_low_f": 25,
            "gust_typical_max_kt": 22, "gust_significant_kt": 32, "gust_extreme_kt": 45,
        },
        10: {  # Peak Diablo wind month
            "normal_high_f": 79, "normal_low_f": 48,
            "rh_typical_min": 15, "rh_extreme_min": 5, "rh_low_days": 6,
            "dp_typical_low_f": 35, "dp_extreme_low_f": 10,
            "gust_typical_max_kt": 28, "gust_significant_kt": 45, "gust_extreme_kt": 65,
            "notes": "Peak Diablo wind season. Tubbs Fire: Oct 8, 2017. Winds 50+ mph through mountain gaps.",
        },
        11: {
            "normal_high_f": 63, "normal_low_f": 42,
            "rh_typical_min": 25, "rh_extreme_min": 10, "rh_low_days": 3,
            "dp_typical_low_f": 32, "dp_extreme_low_f": 15,
            "gust_typical_max_kt": 25, "gust_significant_kt": 40, "gust_extreme_kt": 55,
        },
        12: {
            "normal_high_f": 56, "normal_low_f": 37,
            "rh_typical_min": 35, "rh_extreme_min": 15, "rh_low_days": 2,
            "dp_typical_low_f": 30, "dp_extreme_low_f": 15,
            "gust_typical_max_kt": 22, "gust_significant_kt": 35, "gust_extreme_kt": 50,
        },
    },

    # -------------------------------------------------------------------------
    # KCMA — Camarillo Airport (Malibu, Pac Palisades, Topanga, Thousand Oaks)
    # Lat 34.21N, Lon 119.09W, Elev 75 ft
    # -------------------------------------------------------------------------
    "KCMA": {
        "_station_info": {
            "name": "Camarillo Airport",
            "lat": 34.21,
            "lon": -119.09,
            "elevation_ft": 75,
            "serves": ["malibu_ca", "pacific_palisades_ca", "topanga_ca", "thousand_oaks_ca"],
        },
        6: {
            "normal_high_f": 75, "normal_low_f": 55,
            "rh_typical_min": 30, "rh_extreme_min": 12, "rh_low_days": 3,
            "dp_typical_low_f": 52, "dp_extreme_low_f": 35,
            "gust_typical_max_kt": 20, "gust_significant_kt": 28, "gust_extreme_kt": 40,
        },
        7: {
            "normal_high_f": 79, "normal_low_f": 57,
            "rh_typical_min": 28, "rh_extreme_min": 10, "rh_low_days": 3,
            "dp_typical_low_f": 55, "dp_extreme_low_f": 38,
            "gust_typical_max_kt": 18, "gust_significant_kt": 25, "gust_extreme_kt": 35,
        },
        8: {
            "normal_high_f": 80, "normal_low_f": 58,
            "rh_typical_min": 28, "rh_extreme_min": 10, "rh_low_days": 3,
            "dp_typical_low_f": 55, "dp_extreme_low_f": 38,
            "gust_typical_max_kt": 18, "gust_significant_kt": 25, "gust_extreme_kt": 38,
        },
        9: {
            "normal_high_f": 82, "normal_low_f": 58,
            "rh_typical_min": 18, "rh_extreme_min": 5, "rh_low_days": 5,
            "dp_typical_low_f": 45, "dp_extreme_low_f": 15,
            "gust_typical_max_kt": 25, "gust_significant_kt": 40, "gust_extreme_kt": 60,
            "notes": "Santa Ana season begins. Extreme dry/hot events possible.",
        },
        10: {
            "normal_high_f": 80, "normal_low_f": 55,
            "rh_typical_min": 12, "rh_extreme_min": 3, "rh_low_days": 6,
            "dp_typical_low_f": 30, "dp_extreme_low_f": 5,
            "gust_typical_max_kt": 30, "gust_significant_kt": 50, "gust_extreme_kt": 75,
            "notes": "Peak Santa Ana season. RH can drop to single digits. Mountain gusts 60+ kt.",
        },
        11: {
            "normal_high_f": 72, "normal_low_f": 48,
            "rh_typical_min": 10, "rh_extreme_min": 3, "rh_low_days": 5,
            "dp_typical_low_f": 22, "dp_extreme_low_f": 0,
            "gust_typical_max_kt": 30, "gust_significant_kt": 50, "gust_extreme_kt": 75,
            "notes": "Woolsey Fire: Nov 8, 2018. Strong Santa Ana events continue.",
        },
        12: {
            "normal_high_f": 66, "normal_low_f": 43,
            "rh_typical_min": 12, "rh_extreme_min": 3, "rh_low_days": 4,
            "dp_typical_low_f": 22, "dp_extreme_low_f": 0,
            "gust_typical_max_kt": 28, "gust_significant_kt": 45, "gust_extreme_kt": 70,
            "notes": "Thomas Fire began Dec 4, 2017. Santa Ana events remain possible.",
        },
        1: {  # January — Palisades Fire month
            "normal_high_f": 66, "normal_low_f": 42,
            "rh_typical_min": 15, "rh_extreme_min": 3, "rh_low_days": 3,
            "dp_typical_low_f": 25, "dp_extreme_low_f": 0,
            "gust_typical_max_kt": 25, "gust_significant_kt": 45, "gust_extreme_kt": 70,
            "notes": "Palisades Fire & Eaton Fire: Jan 7, 2025. Late-season Santa Ana possible.",
        },
        2: {
            "normal_high_f": 66, "normal_low_f": 44,
            "rh_typical_min": 18, "rh_extreme_min": 5, "rh_low_days": 2,
            "dp_typical_low_f": 28, "dp_extreme_low_f": 5,
            "gust_typical_max_kt": 22, "gust_significant_kt": 38, "gust_extreme_kt": 55,
        },
    },

    # -------------------------------------------------------------------------
    # KBUR — Burbank / Bob Hope Airport (Altadena, La Canada Flintridge)
    # Lat 34.20N, Lon 118.36W, Elev 778 ft
    # -------------------------------------------------------------------------
    "KBUR": {
        "_station_info": {
            "name": "Burbank / Bob Hope Airport",
            "lat": 34.20,
            "lon": -118.36,
            "elevation_ft": 778,
            "serves": ["altadena_ca", "la_canada_flintridge_ca"],
        },
        6: {
            "normal_high_f": 87, "normal_low_f": 61,
            "rh_typical_min": 18, "rh_extreme_min": 8, "rh_low_days": 5,
            "dp_typical_low_f": 48, "dp_extreme_low_f": 30,
            "gust_typical_max_kt": 22, "gust_significant_kt": 30, "gust_extreme_kt": 45,
        },
        7: {
            "normal_high_f": 93, "normal_low_f": 65,
            "rh_typical_min": 15, "rh_extreme_min": 6, "rh_low_days": 8,
            "dp_typical_low_f": 50, "dp_extreme_low_f": 32,
            "gust_typical_max_kt": 20, "gust_significant_kt": 28, "gust_extreme_kt": 40,
        },
        8: {
            "normal_high_f": 94, "normal_low_f": 66,
            "rh_typical_min": 14, "rh_extreme_min": 5, "rh_low_days": 8,
            "dp_typical_low_f": 50, "dp_extreme_low_f": 30,
            "gust_typical_max_kt": 20, "gust_significant_kt": 28, "gust_extreme_kt": 42,
        },
        9: {
            "normal_high_f": 92, "normal_low_f": 64,
            "rh_typical_min": 12, "rh_extreme_min": 4, "rh_low_days": 7,
            "dp_typical_low_f": 40, "dp_extreme_low_f": 12,
            "gust_typical_max_kt": 28, "gust_significant_kt": 45, "gust_extreme_kt": 65,
            "notes": "Santa Ana season onset. Station Fire: Aug 26, 2009 (late summer).",
        },
        10: {
            "normal_high_f": 85, "normal_low_f": 59,
            "rh_typical_min": 10, "rh_extreme_min": 3, "rh_low_days": 7,
            "dp_typical_low_f": 28, "dp_extreme_low_f": 2,
            "gust_typical_max_kt": 32, "gust_significant_kt": 50, "gust_extreme_kt": 75,
            "notes": "Peak Santa Ana season. Extreme downslope gusts off San Gabriels.",
        },
        11: {
            "normal_high_f": 75, "normal_low_f": 51,
            "rh_typical_min": 10, "rh_extreme_min": 3, "rh_low_days": 5,
            "dp_typical_low_f": 22, "dp_extreme_low_f": 0,
            "gust_typical_max_kt": 30, "gust_significant_kt": 50, "gust_extreme_kt": 75,
        },
        12: {
            "normal_high_f": 68, "normal_low_f": 46,
            "rh_typical_min": 12, "rh_extreme_min": 3, "rh_low_days": 4,
            "dp_typical_low_f": 22, "dp_extreme_low_f": 0,
            "gust_typical_max_kt": 28, "gust_significant_kt": 45, "gust_extreme_kt": 70,
        },
        1: {  # Eaton Fire month
            "normal_high_f": 68, "normal_low_f": 45,
            "rh_typical_min": 15, "rh_extreme_min": 3, "rh_low_days": 3,
            "dp_typical_low_f": 25, "dp_extreme_low_f": 0,
            "gust_typical_max_kt": 28, "gust_significant_kt": 50, "gust_extreme_kt": 80,
            "notes": (
                "Eaton Fire: Jan 7, 2025. Hurricane-force Santa Ana gusts "
                "at San Gabriel foothills. Strongest Santa Anas in a decade."
            ),
        },
    },

    # -------------------------------------------------------------------------
    # KRDD — Redding Regional Airport
    # Lat 40.51N, Lon 122.29W, Elev 502 ft
    # -------------------------------------------------------------------------
    "KRDD": {
        "_station_info": {
            "name": "Redding Regional Airport",
            "lat": 40.51,
            "lon": -122.29,
            "elevation_ft": 502,
            "serves": ["redding_ca"],
        },
        6: {
            "normal_high_f": 95, "normal_low_f": 58,
            "rh_typical_min": 12, "rh_extreme_min": 5, "rh_low_days": 12,
            "dp_typical_low_f": 42, "dp_extreme_low_f": 25,
            "gust_typical_max_kt": 22, "gust_significant_kt": 32, "gust_extreme_kt": 45,
        },
        7: {  # Carr Fire month
            "normal_high_f": 104, "normal_low_f": 63,
            "rh_typical_min": 8, "rh_extreme_min": 4, "rh_low_days": 18,
            "dp_typical_low_f": 38, "dp_extreme_low_f": 20,
            "gust_typical_max_kt": 22, "gust_significant_kt": 32, "gust_extreme_kt": 50,
            "notes": "Carr Fire: Jul 23, 2018. Triple digit heat, bone dry fuels. Fire tornado Jul 26.",
        },
        8: {
            "normal_high_f": 101, "normal_low_f": 61,
            "rh_typical_min": 8, "rh_extreme_min": 4, "rh_low_days": 18,
            "dp_typical_low_f": 38, "dp_extreme_low_f": 20,
            "gust_typical_max_kt": 22, "gust_significant_kt": 30, "gust_extreme_kt": 45,
        },
        9: {
            "normal_high_f": 95, "normal_low_f": 56,
            "rh_typical_min": 10, "rh_extreme_min": 5, "rh_low_days": 12,
            "dp_typical_low_f": 35, "dp_extreme_low_f": 15,
            "gust_typical_max_kt": 22, "gust_significant_kt": 32, "gust_extreme_kt": 50,
        },
        10: {
            "normal_high_f": 80, "normal_low_f": 48,
            "rh_typical_min": 15, "rh_extreme_min": 6, "rh_low_days": 6,
            "dp_typical_low_f": 30, "dp_extreme_low_f": 10,
            "gust_typical_max_kt": 22, "gust_significant_kt": 35, "gust_extreme_kt": 50,
        },
        11: {
            "normal_high_f": 60, "normal_low_f": 39,
            "rh_typical_min": 25, "rh_extreme_min": 10, "rh_low_days": 3,
            "dp_typical_low_f": 28, "dp_extreme_low_f": 10,
            "gust_typical_max_kt": 22, "gust_significant_kt": 30, "gust_extreme_kt": 45,
        },
        12: {
            "normal_high_f": 50, "normal_low_f": 34,
            "rh_typical_min": 35, "rh_extreme_min": 15, "rh_low_days": 1,
            "dp_typical_low_f": 28, "dp_extreme_low_f": 15,
            "gust_typical_max_kt": 20, "gust_significant_kt": 28, "gust_extreme_kt": 40,
        },
    },

    # -------------------------------------------------------------------------
    # KOXR — Oxnard Airport (Ventura, Ojai)
    # Lat 34.20N, Lon 119.21W, Elev 44 ft
    # -------------------------------------------------------------------------
    "KOXR": {
        "_station_info": {
            "name": "Oxnard Airport",
            "lat": 34.20,
            "lon": -119.21,
            "elevation_ft": 44,
            "serves": ["ojai_ca", "ventura_ca"],
        },
        6: {
            "normal_high_f": 73, "normal_low_f": 55,
            "rh_typical_min": 32, "rh_extreme_min": 12, "rh_low_days": 2,
            "dp_typical_low_f": 52, "dp_extreme_low_f": 35,
            "gust_typical_max_kt": 20, "gust_significant_kt": 28, "gust_extreme_kt": 38,
        },
        7: {
            "normal_high_f": 76, "normal_low_f": 58,
            "rh_typical_min": 30, "rh_extreme_min": 12, "rh_low_days": 2,
            "dp_typical_low_f": 55, "dp_extreme_low_f": 40,
            "gust_typical_max_kt": 18, "gust_significant_kt": 25, "gust_extreme_kt": 35,
        },
        8: {
            "normal_high_f": 77, "normal_low_f": 58,
            "rh_typical_min": 30, "rh_extreme_min": 12, "rh_low_days": 2,
            "dp_typical_low_f": 55, "dp_extreme_low_f": 40,
            "gust_typical_max_kt": 18, "gust_significant_kt": 25, "gust_extreme_kt": 35,
        },
        9: {
            "normal_high_f": 79, "normal_low_f": 58,
            "rh_typical_min": 18, "rh_extreme_min": 5, "rh_low_days": 4,
            "dp_typical_low_f": 42, "dp_extreme_low_f": 15,
            "gust_typical_max_kt": 25, "gust_significant_kt": 40, "gust_extreme_kt": 55,
        },
        10: {
            "normal_high_f": 77, "normal_low_f": 55,
            "rh_typical_min": 12, "rh_extreme_min": 3, "rh_low_days": 5,
            "dp_typical_low_f": 28, "dp_extreme_low_f": 5,
            "gust_typical_max_kt": 28, "gust_significant_kt": 45, "gust_extreme_kt": 65,
            "notes": "Peak Santa Ana / Sundowner wind season. Extreme drying and wind acceleration.",
        },
        11: {
            "normal_high_f": 71, "normal_low_f": 48,
            "rh_typical_min": 10, "rh_extreme_min": 3, "rh_low_days": 4,
            "dp_typical_low_f": 22, "dp_extreme_low_f": 0,
            "gust_typical_max_kt": 28, "gust_significant_kt": 45, "gust_extreme_kt": 65,
        },
        12: {  # Thomas Fire month
            "normal_high_f": 65, "normal_low_f": 43,
            "rh_typical_min": 12, "rh_extreme_min": 3, "rh_low_days": 3,
            "dp_typical_low_f": 22, "dp_extreme_low_f": 0,
            "gust_typical_max_kt": 25, "gust_significant_kt": 45, "gust_extreme_kt": 65,
            "notes": "Thomas Fire: Dec 4, 2017. Strong Santa Ana event with SCE power line failure.",
        },
    },

    # -------------------------------------------------------------------------
    # KSBD — San Bernardino International Airport (Lake Arrowhead, Crestline)
    # Lat 34.10N, Lon 117.23W, Elev 1159 ft
    # Note: Valley station. Mountain communities are 3000-5000 ft higher.
    # Temperatures aloft will be 15-30F cooler; winds will be stronger.
    # -------------------------------------------------------------------------
    "KSBD": {
        "_station_info": {
            "name": "San Bernardino International Airport",
            "lat": 34.10,
            "lon": -117.23,
            "elevation_ft": 1159,
            "serves": ["lake_arrowhead_ca", "crestline_ca"],
            "note": (
                "Valley floor station. Mountain communities (4500-5500 ft) "
                "are significantly cooler but experience stronger wind gusts "
                "due to terrain acceleration. Add 10-20 kt to gust values "
                "for ridgeline/pass exposure."
            ),
        },
        6: {
            "normal_high_f": 95, "normal_low_f": 60,
            "rh_typical_min": 12, "rh_extreme_min": 5, "rh_low_days": 8,
            "dp_typical_low_f": 38, "dp_extreme_low_f": 18,
            "gust_typical_max_kt": 22, "gust_significant_kt": 32, "gust_extreme_kt": 50,
        },
        7: {
            "normal_high_f": 102, "normal_low_f": 65,
            "rh_typical_min": 10, "rh_extreme_min": 4, "rh_low_days": 12,
            "dp_typical_low_f": 40, "dp_extreme_low_f": 20,
            "gust_typical_max_kt": 22, "gust_significant_kt": 30, "gust_extreme_kt": 45,
        },
        8: {
            "normal_high_f": 101, "normal_low_f": 65,
            "rh_typical_min": 10, "rh_extreme_min": 4, "rh_low_days": 12,
            "dp_typical_low_f": 40, "dp_extreme_low_f": 20,
            "gust_typical_max_kt": 20, "gust_significant_kt": 30, "gust_extreme_kt": 45,
        },
        9: {
            "normal_high_f": 97, "normal_low_f": 62,
            "rh_typical_min": 10, "rh_extreme_min": 3, "rh_low_days": 8,
            "dp_typical_low_f": 32, "dp_extreme_low_f": 8,
            "gust_typical_max_kt": 25, "gust_significant_kt": 40, "gust_extreme_kt": 60,
            "notes": "Santa Ana season begins. Line Fire (2024): Sep 5, burned 36,000+ acres.",
        },
        10: {  # Old Fire month
            "normal_high_f": 86, "normal_low_f": 55,
            "rh_typical_min": 8, "rh_extreme_min": 3, "rh_low_days": 7,
            "dp_typical_low_f": 22, "dp_extreme_low_f": 0,
            "gust_typical_max_kt": 30, "gust_significant_kt": 50, "gust_extreme_kt": 75,
            "notes": "Old Fire: Oct 25, 2003. Peak Santa Ana. Mountain gusts can exceed 70 kt.",
        },
        11: {
            "normal_high_f": 74, "normal_low_f": 47,
            "rh_typical_min": 10, "rh_extreme_min": 3, "rh_low_days": 5,
            "dp_typical_low_f": 20, "dp_extreme_low_f": 0,
            "gust_typical_max_kt": 28, "gust_significant_kt": 48, "gust_extreme_kt": 70,
        },
        12: {
            "normal_high_f": 64, "normal_low_f": 41,
            "rh_typical_min": 12, "rh_extreme_min": 3, "rh_low_days": 3,
            "dp_typical_low_f": 20, "dp_extreme_low_f": 0,
            "gust_typical_max_kt": 25, "gust_significant_kt": 42, "gust_extreme_kt": 65,
        },
    },

    # -------------------------------------------------------------------------
    # KRNM — Ramona Airport (Julian, Ramona)
    # Lat 33.04N, Lon 116.92W, Elev 1394 ft
    # -------------------------------------------------------------------------
    "KRNM": {
        "_station_info": {
            "name": "Ramona Airport",
            "lat": 33.04,
            "lon": -116.92,
            "elevation_ft": 1394,
            "serves": ["julian_ca", "ramona_ca"],
            "note": "Julian is ~2800 ft higher than Ramona station.",
        },
        6: {
            "normal_high_f": 88, "normal_low_f": 55,
            "rh_typical_min": 15, "rh_extreme_min": 6, "rh_low_days": 6,
            "dp_typical_low_f": 40, "dp_extreme_low_f": 20,
            "gust_typical_max_kt": 20, "gust_significant_kt": 28, "gust_extreme_kt": 40,
        },
        7: {
            "normal_high_f": 95, "normal_low_f": 60,
            "rh_typical_min": 12, "rh_extreme_min": 5, "rh_low_days": 10,
            "dp_typical_low_f": 45, "dp_extreme_low_f": 25,
            "gust_typical_max_kt": 18, "gust_significant_kt": 25, "gust_extreme_kt": 38,
        },
        8: {
            "normal_high_f": 96, "normal_low_f": 61,
            "rh_typical_min": 12, "rh_extreme_min": 5, "rh_low_days": 10,
            "dp_typical_low_f": 45, "dp_extreme_low_f": 25,
            "gust_typical_max_kt": 18, "gust_significant_kt": 25, "gust_extreme_kt": 38,
        },
        9: {
            "normal_high_f": 92, "normal_low_f": 58,
            "rh_typical_min": 10, "rh_extreme_min": 3, "rh_low_days": 7,
            "dp_typical_low_f": 35, "dp_extreme_low_f": 10,
            "gust_typical_max_kt": 25, "gust_significant_kt": 40, "gust_extreme_kt": 60,
        },
        10: {  # Cedar Fire / Witch Creek Fire month
            "normal_high_f": 84, "normal_low_f": 52,
            "rh_typical_min": 8, "rh_extreme_min": 2, "rh_low_days": 6,
            "dp_typical_low_f": 22, "dp_extreme_low_f": 0,
            "gust_typical_max_kt": 30, "gust_significant_kt": 50, "gust_extreme_kt": 75,
            "notes": (
                "Cedar Fire: Oct 25, 2003. Witch Creek Fire: Oct 21, 2007. "
                "Peak Santa Ana season. Fire moved 29 mi in 10 hrs (Cedar). "
                "Single-digit RH with 60+ kt gusts."
            ),
        },
        11: {
            "normal_high_f": 73, "normal_low_f": 43,
            "rh_typical_min": 10, "rh_extreme_min": 3, "rh_low_days": 4,
            "dp_typical_low_f": 20, "dp_extreme_low_f": 0,
            "gust_typical_max_kt": 28, "gust_significant_kt": 45, "gust_extreme_kt": 65,
        },
        12: {
            "normal_high_f": 64, "normal_low_f": 38,
            "rh_typical_min": 15, "rh_extreme_min": 5, "rh_low_days": 3,
            "dp_typical_low_f": 22, "dp_extreme_low_f": 5,
            "gust_typical_max_kt": 25, "gust_significant_kt": 40, "gust_extreme_kt": 60,
        },
    },

    # -------------------------------------------------------------------------
    # KAUN — Auburn Municipal Airport (Grass Valley, Nevada City)
    # Lat 38.95N, Lon 121.08W, Elev 1520 ft
    # -------------------------------------------------------------------------
    "KAUN": {
        "_station_info": {
            "name": "Auburn Municipal Airport",
            "lat": 38.95,
            "lon": -121.08,
            "elevation_ft": 1520,
            "serves": ["grass_valley_ca", "nevada_city_ca"],
            "note": (
                "Grass Valley and Nevada City are 800-1000 ft higher. "
                "KGOO (Nevada County Airport at Grass Valley) has AWOS "
                "but limited historical data."
            ),
        },
        6: {
            "normal_high_f": 92, "normal_low_f": 58,
            "rh_typical_min": 15, "rh_extreme_min": 7, "rh_low_days": 8,
            "dp_typical_low_f": 42, "dp_extreme_low_f": 28,
            "gust_typical_max_kt": 20, "gust_significant_kt": 28, "gust_extreme_kt": 38,
        },
        7: {
            "normal_high_f": 99, "normal_low_f": 62,
            "rh_typical_min": 10, "rh_extreme_min": 5, "rh_low_days": 14,
            "dp_typical_low_f": 40, "dp_extreme_low_f": 22,
            "gust_typical_max_kt": 18, "gust_significant_kt": 26, "gust_extreme_kt": 35,
        },
        8: {
            "normal_high_f": 97, "normal_low_f": 61,
            "rh_typical_min": 10, "rh_extreme_min": 5, "rh_low_days": 14,
            "dp_typical_low_f": 40, "dp_extreme_low_f": 22,
            "gust_typical_max_kt": 18, "gust_significant_kt": 26, "gust_extreme_kt": 35,
        },
        9: {
            "normal_high_f": 92, "normal_low_f": 57,
            "rh_typical_min": 12, "rh_extreme_min": 5, "rh_low_days": 10,
            "dp_typical_low_f": 35, "dp_extreme_low_f": 15,
            "gust_typical_max_kt": 20, "gust_significant_kt": 30, "gust_extreme_kt": 42,
        },
        10: {
            "normal_high_f": 80, "normal_low_f": 50,
            "rh_typical_min": 15, "rh_extreme_min": 6, "rh_low_days": 6,
            "dp_typical_low_f": 30, "dp_extreme_low_f": 8,
            "gust_typical_max_kt": 22, "gust_significant_kt": 35, "gust_extreme_kt": 50,
            "notes": (
                "Diablo wind events possible. Same general wind pattern "
                "that drives fires in Butte County (Camp Fire corridor). "
                "49er Fire: Sep-Oct 1988."
            ),
        },
        11: {
            "normal_high_f": 62, "normal_low_f": 42,
            "rh_typical_min": 22, "rh_extreme_min": 8, "rh_low_days": 3,
            "dp_typical_low_f": 28, "dp_extreme_low_f": 8,
            "gust_typical_max_kt": 22, "gust_significant_kt": 35, "gust_extreme_kt": 50,
        },
        12: {
            "normal_high_f": 53, "normal_low_f": 37,
            "rh_typical_min": 30, "rh_extreme_min": 12, "rh_low_days": 2,
            "dp_typical_low_f": 28, "dp_extreme_low_f": 12,
            "gust_typical_max_kt": 20, "gust_significant_kt": 30, "gust_extreme_kt": 45,
        },
    },

    # -------------------------------------------------------------------------
    # KWJF — Gen William J Fox Airfield, Lancaster (Wrightwood proxy)
    # Lat 34.74N, Lon 118.22W, Elev 2351 ft
    # Note: Desert-side station. Wrightwood at 5935 ft in mountains.
    # Best available ASOS with historical data for the area.
    # -------------------------------------------------------------------------
    "KWJF": {
        "_station_info": {
            "name": "Gen William J Fox Airfield, Lancaster",
            "lat": 34.74,
            "lon": -118.22,
            "elevation_ft": 2351,
            "serves": ["wrightwood_ca"],
            "note": (
                "Desert-side station. Wrightwood is 3500 ft higher in the "
                "mountains. Temperature lapse rate ~3.5F/1000ft applies. "
                "Wind gusts at mountain passes (Cajon, etc) significantly "
                "stronger than at this station."
            ),
        },
        6: {
            "normal_high_f": 97, "normal_low_f": 62,
            "rh_typical_min": 8, "rh_extreme_min": 3, "rh_low_days": 15,
            "dp_typical_low_f": 25, "dp_extreme_low_f": 5,
            "gust_typical_max_kt": 25, "gust_significant_kt": 35, "gust_extreme_kt": 50,
        },
        7: {
            "normal_high_f": 103, "normal_low_f": 68,
            "rh_typical_min": 6, "rh_extreme_min": 2, "rh_low_days": 20,
            "dp_typical_low_f": 28, "dp_extreme_low_f": 8,
            "gust_typical_max_kt": 22, "gust_significant_kt": 32, "gust_extreme_kt": 48,
        },
        8: {
            "normal_high_f": 101, "normal_low_f": 66,
            "rh_typical_min": 7, "rh_extreme_min": 2, "rh_low_days": 18,
            "dp_typical_low_f": 30, "dp_extreme_low_f": 10,
            "gust_typical_max_kt": 22, "gust_significant_kt": 32, "gust_extreme_kt": 48,
            "notes": "Blue Cut Fire: Aug 16, 2016. 82,000 evacuated in San Bernardino County.",
        },
        9: {
            "normal_high_f": 96, "normal_low_f": 60,
            "rh_typical_min": 6, "rh_extreme_min": 2, "rh_low_days": 14,
            "dp_typical_low_f": 20, "dp_extreme_low_f": 0,
            "gust_typical_max_kt": 28, "gust_significant_kt": 42, "gust_extreme_kt": 60,
            "notes": "Bridge Fire: Sep 8, 2024 (56,030 acres). Santa Ana onset.",
        },
        10: {
            "normal_high_f": 83, "normal_low_f": 50,
            "rh_typical_min": 6, "rh_extreme_min": 2, "rh_low_days": 10,
            "dp_typical_low_f": 12, "dp_extreme_low_f": -5,
            "gust_typical_max_kt": 32, "gust_significant_kt": 48, "gust_extreme_kt": 70,
            "notes": "Peak Santa Ana season. Cajon Pass gusts frequently exceed 60 kt.",
        },
        11: {
            "normal_high_f": 69, "normal_low_f": 40,
            "rh_typical_min": 8, "rh_extreme_min": 2, "rh_low_days": 6,
            "dp_typical_low_f": 10, "dp_extreme_low_f": -10,
            "gust_typical_max_kt": 30, "gust_significant_kt": 48, "gust_extreme_kt": 70,
        },
        12: {
            "normal_high_f": 58, "normal_low_f": 34,
            "rh_typical_min": 12, "rh_extreme_min": 3, "rh_low_days": 4,
            "dp_typical_low_f": 12, "dp_extreme_low_f": -5,
            "gust_typical_max_kt": 28, "gust_significant_kt": 45, "gust_extreme_kt": 65,
        },
    },
}


# =============================================================================
# UTILITY — City-to-station mapping for quick lookup
# =============================================================================

CITY_STATION_MAP = {
    "alpine_ca": "KRNM",
    "alta_sierra_ca": "KAUN",
    "altadena_ca": "KBUR",
    "angwin_ca": "KAPC",
    "ben_lomond_ca": "KWVI",
    "big_bear_lake_ca": "KSBD",
    "bonny_doon_ca": "KWVI",
    "boulder_creek_ca": "KWVI",
    "calistoga_ca": "KAPC",
    "carpinteria_ca": "KSBA",
    "clearlake_ca": "KSTS",
    "cobb_ca": "KSTS",
    "colfax_ca": "KAUN",
    "crestline_ca": "KSBD",
    "diamond_springs_ca": "KPVF",
    "dunsmuir_ca": "KSIS",
    "fallbrook_ca": "KRNM",
    "felton_ca": "KWVI",
    "forest_falls_ca": "KSBD",
    "foresthill_ca": "KAUN",
    "frazier_park_ca": "KWJF",
    "georgetown_ca": "KPVF",
    "glen_ellen_ca": "KSTS",
    "grass_valley_ca": "KAUN",
    "groveland_ca": "KMCE",
    "hayfork_ca": "KRDD",
    "idyllwild_ca": "KPSP",
    "julian_ca": "KRNM",
    "kenwood_ca": "KSTS",
    "la_canada_flintridge_ca": "KBUR",
    "lake_arrowhead_ca": "KSBD",
    "lower_lake_ca": "KSTS",
    "magalia_ca": "KOVE",
    "malibu_ca": "KCMA",
    "mariposa_ca": "KMCE",
    "middletown_ca": "KSTS",
    "montecito_ca": "KSBA",
    "mountain_center_ca": "KPSP",
    "nevada_city_ca": "KAUN",
    "ojai_ca": "KOXR",
    "pacific_palisades_ca": "KCMA",
    "paradise_ca": "KOVE",
    "paradise_satellite_communities": "KOVE",
    "pine_mountain_club_ca": "KWJF",
    "pine_valley_ca": "KRNM",
    "pollock_pines_ca": "KPVF",
    "ramona_ca": "KRNM",
    "redding_ca": "KRDD",
    "running_springs_ca": "KSBD",
    "san_lorenzo_valley_communities": "KWVI",
    "santa_rosa_ca": "KSTS",
    "sonoma_ca": "KSTS",
    "thousand_oaks_ca": "KCMA",
    "three_rivers_ca": "KVIS",
    "topanga_ca": "KCMA",
    "ukiah_outskirts_ca": "KUKI",
    "valley_center_ca": "KRNM",
    "ventura_ca": "KOXR",
    "weaverville_ca": "KRDD",
    "weed_ca": "KSIS",
    "willits_ca": "KUKI",
    "wrightwood_ca": "KWJF",
}


def get_city_profile(city_key: str) -> dict:
    """Get the full profile (terrain + ignition + climatology) for a city.

    Args:
        city_key: City key like "paradise_ca", "malibu_ca", etc.

    Returns:
        Dict with keys: terrain, ignition, climatology, station_id
        Returns empty dict if city not found.
    """
    result = {}

    if city_key in CA_TERRAIN_PROFILES:
        result["terrain"] = CA_TERRAIN_PROFILES[city_key]

    if city_key in CA_IGNITION_SOURCES:
        result["ignition"] = CA_IGNITION_SOURCES[city_key]

    station_id = CITY_STATION_MAP.get(city_key)
    if station_id and station_id in CA_CLIMATOLOGY:
        result["station_id"] = station_id
        result["climatology"] = CA_CLIMATOLOGY[station_id]

    return result


def list_california_cities() -> list:
    """List all California cities with fire vulnerability profiles.

    Returns:
        List of dicts with key, center, elevation, wui_class, and station_id.
    """
    cities = []
    for key, profile in CA_TERRAIN_PROFILES.items():
        cities.append({
            "key": key,
            "center": profile["center"],
            "elevation_ft": profile.get("elevation_ft", 0),
            "wui_class": profile.get("wui_class", "unknown"),
            "station_id": CITY_STATION_MAP.get(key, ""),
            "historical_fires": profile.get("historical_fires", []),
        })
    return cities
