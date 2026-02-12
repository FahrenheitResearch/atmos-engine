"""
Enhanced LA Basin Fire-Vulnerable City Terrain Profiles
========================================================

Deep research-backed profiles for 5 cities in the LA Basin WUI.
Every sentence is operational intelligence -- no filler.

Cities: Malibu, Pacific Palisades, Topanga, Altadena, La Canada Flintridge

Sources:
    - Palisades Fire (Jan 7-31, 2025): CAL FIRE final report; LAPD after-action;
      LADWP water system preliminary report (Jul 2025); NASA SVS fire spread viz
    - Eaton Fire (Jan 7-31, 2025): CAL FIRE final report; LA County AAR;
      Washington Post evacuation investigation; UCLA Bunche Center demographics
    - Franklin Fire (Dec 9-12, 2024): CAL FIRE incident report
    - Woolsey Fire (Nov 8-21, 2018): CPUC investigation; NPS SAMO; CAL FIRE
    - Station Fire (Aug 26 - Oct 16, 2009): USFS Angeles NF; CAL FIRE
    - Old Topanga Fire (Nov 2-11, 1993): LAFD official report; CAL FIRE
    - SCE Eaton Fire investigation: CPUC filings; federal DOJ lawsuit (Sep 2025)
    - LADWP Palisades water analysis: CalEPA memo (Nov 2025)
    - Altadena demographics: UCLA Center for Neighborhood Knowledge (Jan 2025);
      SAJE displacement report (May 2025)
    - La Canada Flintridge: City after-action report; State Fire Marshal VHFHSZ map
"""

LA_BASIN_TERRAIN_PROFILES = {

    # =========================================================================
    # SANTA MONICA MOUNTAINS CORRIDOR -- Palisades / Woolsey / Franklin Fires
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

    # =========================================================================
    # SAN GABRIEL FOOTHILLS -- Eaton Fire / Station Fire
    # =========================================================================

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
}
