"""Arizona & New Mexico Fire-Vulnerable City Profiles
====================================================

Comprehensive terrain, evacuation, fire behavior, infrastructure, and demographic
data for 29 fire-vulnerable cities across Arizona and New Mexico.
Profiles derived from NWCG after-action reports, NIFC historical records,
state forestry data, CWPPs, InciWeb, and peer-reviewed literature.

Usage:
    from tools.agent_tools.data.southwest_profiles import (
        SW_TERRAIN_PROFILES,
        SW_IGNITION_SOURCES,
        SW_CLIMATOLOGY,
    )

Cities covered (29 entries across 2 states):
    ARIZONA (15 cities):
        Alpine Greer
        Carefree Cave Creek
        Crown King
        Flagstaff
        Kearny Winkelman
        Oracle
        Paradise Valley
        Payson
        Prescott
        Sedona
        Show Low
        Sierra Vista
        Strawberry Pine
        Tucson Foothills
        Yarnell
    NEW MEXICO (14 cities):
        Angel Fire
        Cloudcroft
        Jemez Springs
        Las Vegas
        Los Alamos
        Pecos
        Red River
        Reserve
        Ruidoso Downs
        Ruidoso
        Santa Fe
        Silver City
        Taos
        Tres Piedras

Sources:
    - NWCG after-action reports (Yarnell Hill, Dude Fire)
    - InciWeb, NIFC incident data
    - Arizona Dept of Forestry: At Risk Communities
    - New Mexico State Forestry fire records
    - USFS: Coconino NF, Prescott NF, Lincoln NF, Gila NF, Carson NF, Santa Fe NF
    - WRCC / IEM / ASOS climatology archives
"""

# =============================================================================
# TERRAIN PROFILES -- 29 entries organized by state
# =============================================================================

SW_TERRAIN_PROFILES = {

    # =========================================================================
    # ARIZONA (15 cities)
    # =========================================================================

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
    # NEW MEXICO (14 cities)
    # =========================================================================

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

}




# ---------------------------------------------------------------------------
# 2. IGNITION SOURCES
# ---------------------------------------------------------------------------

SW_IGNITION_SOURCES = {
    "lightning": {
        "description": (
            "Lightning is the dominant natural ignition source across the "
            "Southwest. The monsoon season (July-September) brings dry "
            "thunderstorms in June and early July before moisture fully "
            "arrives. These produce lightning with little or no rain — the "
            "most dangerous ignition scenario. Post-monsoon lightning in "
            "October can also start fires in drying fuels. The Wallow Fire "
            "(2011, 538K ac), Whitewater-Baldy (2012, 298K ac), and Bighorn "
            "Fire (2020, 120K ac) were all lightning-caused."
        ),
        "peak_months": "June, early July (pre-monsoon dry lightning)",
        "secondary_months": "October (post-monsoon drying)",
        "risk_level": "extreme",
        "affected_cities": [
            "flagstaff_az", "show_low_az", "alpine_greer_az", "payson_az",
            "silver_city_nm", "cloudcroft_nm", "ruidoso_nm", "taos_nm",
        ],
    },

    "prescribed_burn_escapes": {
        "description": (
            "Prescribed burn escapes have caused the most devastating fires "
            "in NM history. Cerro Grande Fire (2000): NPS prescribed burn "
            "escaped, destroyed 400+ homes in Los Alamos, forced evacuation "
            "of nuclear weapons lab, $1B damage. Understaffed crew, "
            "inadequate planning for wind. Hermits Peak/Calf Canyon (2022): "
            "TWO separate USFS management failures — a prescribed burn "
            "escaped April 6, and pile burns from January rekindled April 9. "
            "341,471 ac burned, 903 structures, water supply contaminated. "
            "Federal government accepted liability, Congress authorized "
            "$3.95B in claims. These failures have made prescribed fire "
            "politically controversial despite its ecological necessity."
        ),
        "risk_level": "extreme (historically)",
        "affected_cities": [
            "los_alamos_nm", "las_vegas_nm", "santa_fe_nm",
        ],
    },

    "power_lines": {
        "description": (
            "Power line failures are a significant ignition source, "
            "especially during spring wind events. Las Conchas Fire (2011) "
            "started when a tree fell on a power line — burned 44,000 ac "
            "in the first 13 hours. Tunnel Fire (2022) near Flagstaff "
            "likely from a holdover ignition reignited by wind. Utility "
            "infrastructure in forested mountain terrain is vulnerable to "
            "tree strikes and wind damage."
        ),
        "risk_level": "high",
        "affected_cities": [
            "santa_fe_nm", "flagstaff_az", "prescott_az", "ruidoso_nm",
            "los_alamos_nm",
        ],
    },

    "human_caused": {
        "description": (
            "Human-caused ignitions include arson, campfires, equipment, "
            "vehicles, and target shooting. Rodeo Fire (2002) was ARSON — "
            "set by a seasonal tribal firefighter near Cibecue, led to "
            "468,638 ac burned, 491 homes, 30,000 evacuated. Arsonist "
            "received 10 years. Recreational use of national forests "
            "around Flagstaff, Prescott, Sedona, Payson, and Ruidoso "
            "creates constant human ignition risk during dry periods. "
            "Target shooting sparks fires in dry grass/brush."
        ),
        "risk_level": "high",
        "affected_cities": [
            "flagstaff_az", "prescott_az", "sedona_az", "payson_az",
            "show_low_az", "ruidoso_nm", "santa_fe_nm",
        ],
    },

    "military_operations": {
        "description": (
            "Fort Huachuca near Sierra Vista conducts training operations "
            "that can ignite fires. Brown Fire (2014) started from a "
            "bulldozer on fort property. The fort has a dedicated wildfire "
            "management plan but equipment and training exercises remain "
            "ignition sources."
        ),
        "risk_level": "moderate",
        "affected_cities": ["sierra_vista_az"],
    },

    "transportation_corridors": {
        "description": (
            "Major highway corridors through forest and grassland create "
            "ignition risk from vehicle fires, catalytic converters, "
            "tire blowouts, and dragging equipment. I-40 across northern "
            "AZ (Flagstaff corridor), I-17 (Phoenix to Flagstaff through "
            "high-fire terrain), I-10 (Tucson to Phoenix), and I-25 "
            "(Santa Fe corridor) are key routes."
        ),
        "corridors": {
            "I-40": {
                "route": "E-W across northern AZ and NM",
                "cities_affected": ["flagstaff_az", "santa_fe_nm"],
                "risk_level": "moderate",
            },
            "I-17": {
                "route": "N-S Phoenix to Flagstaff",
                "cities_affected": ["flagstaff_az", "sedona_az"],
                "notes": (
                    "Climbs 5,000 ft through chaparral and pine forest. "
                    "Vehicle fires along steep grades."
                ),
                "risk_level": "moderate",
            },
            "I-25": {
                "route": "N-S Albuquerque to Colorado",
                "cities_affected": ["santa_fe_nm", "las_vegas_nm"],
                "risk_level": "moderate",
            },
        },
    },
}


# ---------------------------------------------------------------------------
# 3. CLIMATOLOGY
# ---------------------------------------------------------------------------

SW_CLIMATOLOGY = {
    "region_overview": {
        "primary_fire_season": "May through July (peak: June, pre-monsoon)",
        "secondary_fire_season": "October-November (post-monsoon drying), March-April (spring wind)",
        "why_pre_monsoon": (
            "May-June is the driest period in the Southwest. Winter snowpack "
            "has melted, spring rains have ended, and the monsoon has not yet "
            "arrived. Relative humidity drops to single digits, 1000-hour "
            "fuel moisture bottoms out, and afternoon winds of 25-40 mph are "
            "common. Live fuel moisture in conifers drops below critical "
            "thresholds. This 4-6 week window produces the largest fires. "
            "When the monsoon arrives (typically early-mid July), fire "
            "activity drops dramatically."
        ),
        "monsoon_effect": (
            "The North American Monsoon (July-September) brings afternoon "
            "thunderstorms and dramatically increases humidity, dampening "
            "fire spread. However, early monsoon storms produce lightning "
            "without rain (dry thunderstorms), creating new ignitions. "
            "Late monsoon failures (years when moisture is weak or late) "
            "extend fire season into August-September."
        ),
        "worst_months_by_acres": ["June", "May", "July", "April"],
        "key_weather_drivers": [
            "Upper-level ridge building — hot, dry subsidence over the region",
            "Pre-monsoon wind events — southwest flow aloft mixes to surface",
            "Dry thunderstorms — lightning ignitions before monsoon moisture arrives",
            "Spring cold fronts — March-April wind events with 40-60 mph gusts",
            "Foehn/downslope winds — localized drying on lee sides of mountain ranges",
            "Monsoon failure — weak or late monsoon extends fire season by weeks",
        ],
    },

    "city_climatology": {
        "prescott_az": {
            "annual_avg_wind_mph": 7.5,
            "peak_gust_recorded_mph": 65,
            "summer_avg_rh_min_pct": 10,
            "critical_rh_threshold_pct": 12,
            "days_below_15pct_rh_fire_season": 40,
            "annual_precip_in": 19.2,
            "monsoon_precip_in": 7.5,
            "avg_monsoon_onset": "Jul 7",
            "fire_season_precip_in": 1.5,
            "fire_weather_notes": (
                "Central highlands location creates complex wind patterns "
                "from terrain channeling. Chaparral fires produce extreme "
                "heat and spread rates. Yarnell Hill Fire (2013) had 10-12 "
                "mph spread rate in chaparral with erratic wind shifts "
                "from thunderstorm outflow. Granite dells terrain creates "
                "box canyons that trap fire crews."
            ),
        },
        "flagstaff_az": {
            "annual_avg_wind_mph": 7.2,
            "peak_gust_recorded_mph": 76,
            "summer_avg_rh_min_pct": 8,
            "critical_rh_threshold_pct": 12,
            "days_below_15pct_rh_fire_season": 35,
            "annual_precip_in": 22.8,
            "monsoon_precip_in": 8.0,
            "avg_monsoon_onset": "Jul 5",
            "fire_season_precip_in": 1.2,
            "fire_weather_notes": (
                "At 7,000 ft, Flagstaff has a unique fire climatology. "
                "Snow covers the forest Nov-Mar but the transition from "
                "snowmelt to monsoon onset (May-early Jul) is extremely "
                "dry. NWS Flagstaff Museum Fire analysis noted the 2019 "
                "monsoon was late and dry, leading to elevated ERCs. "
                "Ponderosa pine needles on the forest floor create a "
                "continuous fuel bed. April wind events can produce gusts "
                "to 60-70 mph — the Tunnel Fire (2022) went from 100 ac "
                "to 6,000 ac in one day from wind."
            ),
        },
        "sedona_az": {
            "annual_avg_wind_mph": 5.8,
            "peak_gust_recorded_mph": 55,
            "summer_avg_rh_min_pct": 12,
            "critical_rh_threshold_pct": 15,
            "days_below_15pct_rh_fire_season": 25,
            "annual_precip_in": 17.6,
            "monsoon_precip_in": 5.5,
            "avg_monsoon_onset": "Jul 10",
            "fire_season_precip_in": 1.0,
            "fire_weather_notes": (
                "Canyon terrain creates complex wind patterns. Afternoon "
                "upcanyon winds can shift to downcanyon at night. Oak Creek "
                "Canyon acts as a chimney — fire at the bottom races upward. "
                "Single-road evacuation through canyon is a critical "
                "vulnerability. Higher than average temps due to lower "
                "elevation (4,350 ft) compared to Flagstaff (6,910 ft)."
            ),
        },
        "payson_az": {
            "annual_avg_wind_mph": 6.5,
            "peak_gust_recorded_mph": 65,
            "summer_avg_rh_min_pct": 9,
            "critical_rh_threshold_pct": 12,
            "days_below_15pct_rh_fire_season": 35,
            "annual_precip_in": 22.0,
            "monsoon_precip_in": 8.5,
            "avg_monsoon_onset": "Jul 8",
            "fire_season_precip_in": 1.5,
            "fire_weather_notes": (
                "Mogollon Rim creates extreme fire weather dynamics. "
                "Afternoon upslope winds push fire up the 2,000-ft Rim "
                "face. Dude Fire (1990) occurred during record heat — 122 F "
                "in Phoenix, 106 F in Payson — combined with 3-year drought. "
                "The Rim acts as a convection driver, pulling air upward "
                "from the hot desert below. Spring wind events are "
                "particularly dangerous when the Rim amplifies wind speed."
            ),
        },
        "show_low_az": {
            "annual_avg_wind_mph": 7.8,
            "peak_gust_recorded_mph": 70,
            "summer_avg_rh_min_pct": 10,
            "critical_rh_threshold_pct": 12,
            "days_below_15pct_rh_fire_season": 30,
            "annual_precip_in": 21.5,
            "monsoon_precip_in": 9.0,
            "avg_monsoon_onset": "Jul 5",
            "fire_season_precip_in": 1.8,
            "fire_weather_notes": (
                "White Mountains plateau at 6,345 ft. Rodeo-Chediski Fire "
                "(2002) occurred in severe drought with unseasonably hot "
                "temps and low humidity. The fire made multiple 20+ mile "
                "runs. This area receives some of the best monsoon moisture "
                "in AZ, which shortens fire season — but pre-monsoon drought "
                "years are exceptionally dangerous."
            ),
        },
        "alpine_greer_az": {
            "annual_avg_wind_mph": 6.0,
            "peak_gust_recorded_mph": 60,
            "summer_avg_rh_min_pct": 8,
            "critical_rh_threshold_pct": 12,
            "days_below_15pct_rh_fire_season": 25,
            "annual_precip_in": 23.0,
            "monsoon_precip_in": 10.0,
            "avg_monsoon_onset": "Jul 3",
            "fire_season_precip_in": 2.0,
            "fire_weather_notes": (
                "High-elevation (8,050 ft) location with longer snow season "
                "but intense pre-monsoon drying. Wallow Fire (2011) burned "
                "538,049 ac with sustained 40+ mph winds. Remote location "
                "means fire can burn for days before reaching communities, "
                "building to extreme size. Wilderness areas prohibit "
                "mechanical suppression."
            ),
        },
        "tucson_foothills_az": {
            "annual_avg_wind_mph": 8.3,
            "peak_gust_recorded_mph": 58,
            "summer_avg_rh_min_pct": 8,
            "critical_rh_threshold_pct": 10,
            "days_below_15pct_rh_fire_season": 50,
            "annual_precip_in": 11.6,
            "monsoon_precip_in": 5.5,
            "avg_monsoon_onset": "Jul 3",
            "fire_season_precip_in": 0.5,
            "fire_weather_notes": (
                "Driest major city on this list. The Catalina Mountains "
                "create a dramatic elevation gradient — 2,700 ft at the "
                "foothills to 9,157 ft at Mt. Lemmon. This drives extreme "
                "diurnal wind patterns: upslope afternoon winds push fire "
                "into mountain forest, downslope evening winds push fire "
                "and embers toward homes below. Bighorn Fire (2020) burned "
                "48 days because terrain was too rugged for direct attack. "
                "Monsoon is the primary containment mechanism."
            ),
        },
        "sierra_vista_az": {
            "annual_avg_wind_mph": 9.5,
            "peak_gust_recorded_mph": 62,
            "summer_avg_rh_min_pct": 10,
            "critical_rh_threshold_pct": 12,
            "days_below_15pct_rh_fire_season": 40,
            "annual_precip_in": 15.5,
            "monsoon_precip_in": 8.0,
            "avg_monsoon_onset": "Jul 1",
            "fire_season_precip_in": 0.8,
            "fire_weather_notes": (
                "Windiest city on this list due to open desert exposure. "
                "Strong afternoon winds are funneled by the San Pedro "
                "Valley. Historical fire interval in Huachuca Mountains "
                "was 4-10 years, now disrupted. Madrean sky island "
                "vegetation includes species adapted to fire but current "
                "overgrowth creates dangerous fuel loads."
            ),
        },
        "santa_fe_nm": {
            "annual_avg_wind_mph": 7.5,
            "peak_gust_recorded_mph": 65,
            "summer_avg_rh_min_pct": 10,
            "critical_rh_threshold_pct": 12,
            "days_below_15pct_rh_fire_season": 35,
            "annual_precip_in": 14.2,
            "monsoon_precip_in": 5.5,
            "avg_monsoon_onset": "Jul 5",
            "fire_season_precip_in": 1.5,
            "fire_weather_notes": (
                "Spring wind events (March-May) are the primary fire "
                "weather driver. Southwest flow aloft mixes strong winds "
                "to the surface. Las Conchas Fire (2011) burned 44,000 ac "
                "in 13 hours — among the fastest-moving fires in US "
                "history. The Jemez Mountains NW of Santa Fe are the "
                "primary fire threat vector. Municipal watershed at risk."
            ),
        },
        "los_alamos_nm": {
            "annual_avg_wind_mph": 7.0,
            "peak_gust_recorded_mph": 67,
            "summer_avg_rh_min_pct": 8,
            "critical_rh_threshold_pct": 10,
            "days_below_15pct_rh_fire_season": 40,
            "annual_precip_in": 18.5,
            "monsoon_precip_in": 7.0,
            "avg_monsoon_onset": "Jul 5",
            "fire_season_precip_in": 1.0,
            "fire_weather_notes": (
                "Springtime Jemez Mountains are prone to high winds and "
                "low humidity creating extreme fire danger. Forest density "
                "of 400-1,300 trees per acre (vs. natural 50-150) means "
                "crown fire potential is extreme. Two major fires in 11 "
                "years (Cerro Grande 2000, Las Conchas 2011) demonstrate "
                "recurring threat. National security dimension: nuclear "
                "weapons research and materials on site. LANL has invested "
                "heavily in fuel reduction on lab property since 2000."
            ),
        },
        "ruidoso_nm": {
            "annual_avg_wind_mph": 6.0,
            "peak_gust_recorded_mph": 60,
            "summer_avg_rh_min_pct": 10,
            "critical_rh_threshold_pct": 12,
            "days_below_15pct_rh_fire_season": 30,
            "annual_precip_in": 23.5,
            "monsoon_precip_in": 10.0,
            "avg_monsoon_onset": "Jul 1",
            "fire_season_precip_in": 1.5,
            "fire_weather_notes": (
                "Mountain resort at 6,920 ft with good monsoon moisture "
                "but devastating pre-monsoon fire potential. South Fork "
                "Fire (June 2024) destroyed ~1,400 structures — the canyon "
                "terrain funneled fire directly through town. Two people "
                "died, one burned in their vehicle. Little Bear Fire "
                "(2012) also caused major destruction (254 structures). "
                "Pattern of recurring destructive fires in the same area."
            ),
        },
        "las_vegas_nm": {
            "annual_avg_wind_mph": 8.8,
            "peak_gust_recorded_mph": 67,
            "summer_avg_rh_min_pct": 12,
            "critical_rh_threshold_pct": 15,
            "days_below_15pct_rh_fire_season": 25,
            "annual_precip_in": 16.0,
            "monsoon_precip_in": 6.5,
            "avg_monsoon_onset": "Jul 5",
            "fire_season_precip_in": 1.2,
            "fire_weather_notes": (
                "Mountain-to-plains transition at 6,424 ft. Spring wind "
                "events are extreme — Hermits Peak/Calf Canyon merger day "
                "(April 22, 2022) had 40-50 mph sustained winds, 67 mph "
                "gusts, 6% RH. These conditions are not uncommon in April "
                "along the eastern Sangre de Cristos. The Gallinas River "
                "watershed (city water supply) is in the burn zone, making "
                "post-fire flooding a compounding disaster."
            ),
        },
        "silver_city_nm": {
            "annual_avg_wind_mph": 7.0,
            "peak_gust_recorded_mph": 60,
            "summer_avg_rh_min_pct": 8,
            "critical_rh_threshold_pct": 10,
            "days_below_15pct_rh_fire_season": 35,
            "annual_precip_in": 16.5,
            "monsoon_precip_in": 8.0,
            "avg_monsoon_onset": "Jul 1",
            "fire_season_precip_in": 0.8,
            "fire_weather_notes": (
                "Gateway to the Gila Wilderness — fires in the wilderness "
                "can burn freely for weeks before threatening communities. "
                "Whitewater-Baldy (2012) had 40-50 mph sustained winds. "
                "The Gila NF is among the most active lightning fire areas "
                "in the US. Extremely rugged terrain means fires are often "
                "uncontainable until weather (monsoon) or terrain stops them."
            ),
        },
        "taos_nm": {
            "annual_avg_wind_mph": 7.2,
            "peak_gust_recorded_mph": 60,
            "summer_avg_rh_min_pct": 10,
            "critical_rh_threshold_pct": 12,
            "days_below_15pct_rh_fire_season": 30,
            "annual_precip_in": 12.8,
            "monsoon_precip_in": 4.5,
            "avg_monsoon_onset": "Jul 8",
            "fire_season_precip_in": 1.5,
            "fire_weather_notes": (
                "Taos receives less monsoon moisture than southern NM "
                "cities, extending effective fire season. Spring wind "
                "events drive through the Sangre de Cristos. Taos Canyon "
                "is a high-risk WUI corridor. The 2022 Hermits Peak/Calf "
                "Canyon Fire burned into Taos County (Mora County border). "
                "Taos Pueblo (1,000-year-old World Heritage Site) adds "
                "irreplaceable cultural risk."
            ),
        },
        "cloudcroft_nm": {
            "annual_avg_wind_mph": 8.0,
            "peak_gust_recorded_mph": 65,
            "summer_avg_rh_min_pct": 8,
            "critical_rh_threshold_pct": 10,
            "days_below_15pct_rh_fire_season": 35,
            "annual_precip_in": 24.5,
            "monsoon_precip_in": 11.0,
            "avg_monsoon_onset": "Jul 1",
            "fire_season_precip_in": 1.0,
            "fire_weather_notes": (
                "Highest elevation city on this list (8,663 ft). Gets good "
                "monsoon moisture but the pre-monsoon window (May-early Jul) "
                "is extremely dangerous. Strong diurnal upslope winds from "
                "the Tularosa Basin push fire from desert scrub into "
                "mountain forest. Mean fire interval of 6-18 years means "
                "fire is not if but when. South Fork/Salt fires (2024) in "
                "Ruidoso 40 mi SE demonstrated the vulnerability of "
                "Sacramento Mountain communities."
            ),
        },
    },
}
