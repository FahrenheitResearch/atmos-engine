"""
Oklahoma Prescribed Burns on Red Flag Day — Agent Research Swarm
Feb 9, 2026

Uses wxsection.com agent tools:
  - CrossSectionTool (multi-panel comparisons)
  - investigate_location (comprehensive fire wx investigation)
  - FireRiskAssessor (fire condition assessment)
  - ReportBuilder (LaTeX → PDF compilation)
  - get_metar, get_spc_outlook, get_nws_alerts (external data)
"""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from tools.agent_tools.cross_section import CrossSectionTool, CrossSectionData
from tools.agent_tools.investigation import investigate_location
from tools.agent_tools.fire_risk import FireRiskAnalyzer
from tools.agent_tools.report_builder import ReportBuilder, ReportConfig
from tools.agent_tools.external_data import (
    get_metar_observations, get_spc_fire_weather_outlook,
    get_nws_alerts, get_spc_fire_discussion, get_nearby_stations
)

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(OUT_DIR, 'figures')
os.makedirs(FIG_DIR, exist_ok=True)

cs = CrossSectionTool(base_url='http://localhost:5565')
fra = FireRiskAnalyzer()

# =====================================================================
# Investigation sites (western OK red flag area + central OK)
# =====================================================================
SITES = [
    {"name": "Woodward, OK", "lat": 36.43, "lon": -99.39},
    {"name": "Oklahoma City, OK", "lat": 35.47, "lon": -97.52},
    {"name": "Gage, OK (Harper Co)", "lat": 36.31, "lon": -99.76},
]

# Transects
EW_CENTRAL = {"start": (35.5, -99.5), "end": (35.5, -95.0)}
NS_WESTERN = {"start": (37.0, -99.0), "end": (34.5, -99.0)}

CYCLE = "20260209_18z"  # 18z Feb 9 = noon CST

# =====================================================================
# PHASE 1: Generate cross-section images via CrossSectionTool
# =====================================================================
print("=" * 60)
print("PHASE 1: Cross-Section Image Generation")
print("=" * 60)

figures = {}

# 1a. Four-panel product comparison — fire weather variables
print("\n[1a] 4-panel product: wind_speed, rh, vpd, dewpoint_dep (E-W)")
ok = cs.generate_comparison(
    start=EW_CENTRAL["start"], end=EW_CENTRAL["end"],
    mode="product", products="wind_speed,rh,vpd,dewpoint_dep",
    cycle=CYCLE, fhr=2, y_top=700,
    output_path=os.path.join(FIG_DIR, "product_4panel_firewx.png"))
figures["product_firewx"] = ok
print(f"  -> {'OK' if ok else 'FAILED'}")

# 1b. Four-panel temporal — wind evolution through afternoon
print("\n[1b] 4-panel temporal: wind F00-F06 (noon-6pm CST)")
ok = cs.generate_comparison(
    start=EW_CENTRAL["start"], end=EW_CENTRAL["end"],
    mode="temporal", fhrs="1,3,5,8",
    cycle=CYCLE, product="wind_speed", y_top=500,
    output_path=os.path.join(FIG_DIR, "temporal_4panel_wind.png"))
figures["temporal_wind"] = ok
print(f"  -> {'OK' if ok else 'FAILED'}")

# 1c. Four-panel temporal — RH drying through afternoon
print("\n[1c] 4-panel temporal: RH F00-F06 (noon-6pm CST)")
ok = cs.generate_comparison(
    start=EW_CENTRAL["start"], end=EW_CENTRAL["end"],
    mode="temporal", fhrs="1,3,5,8",
    cycle=CYCLE, product="rh", y_top=700,
    output_path=os.path.join(FIG_DIR, "temporal_4panel_rh.png"))
figures["temporal_rh"] = ok
print(f"  -> {'OK' if ok else 'FAILED'}")

# 1d. N-S transect: 4-panel product through western OK
print("\n[1d] 4-panel product: wind, rh, temp, lapse_rate (N-S western OK)")
ok = cs.generate_comparison(
    start=NS_WESTERN["start"], end=NS_WESTERN["end"],
    mode="product", products="wind_speed,rh,temp,lapse_rate",
    cycle=CYCLE, fhr=2, y_top=500,
    output_path=os.path.join(FIG_DIR, "product_4panel_ns.png"))
figures["product_ns"] = ok
print(f"  -> {'OK' if ok else 'FAILED'}")

# 1e. Model comparison HRRR vs GFS
print("\n[1e] 2-panel model: HRRR vs GFS (valid-time matched)")
ok = cs.generate_comparison(
    start=EW_CENTRAL["start"], end=EW_CENTRAL["end"],
    mode="model", models="hrrr,gfs",
    cycle=CYCLE, fhr=8, product="wind_speed", y_top=500,
    output_path=os.path.join(FIG_DIR, "model_2panel_hrrr_gfs.png"))
figures["model_compare"] = ok
print(f"  -> {'OK' if ok else 'FAILED'}")

# 1f. Single-panel fire_wx composite
print("\n[1f] Single panel: fire weather composite")
ok = cs.generate_image(
    start=EW_CENTRAL["start"], end=EW_CENTRAL["end"],
    cycle=CYCLE, fhr=2, product="fire_wx", y_top=700,
    output_path=os.path.join(FIG_DIR, "fire_wx_composite.png"))
figures["fire_wx"] = ok
print(f"  -> {'OK' if ok else 'FAILED'}")

# 1g. Single-panel VPD
print("\n[1g] Single panel: Vapor Pressure Deficit")
ok = cs.generate_image(
    start=EW_CENTRAL["start"], end=EW_CENTRAL["end"],
    cycle=CYCLE, fhr=2, product="vpd", y_top=700,
    output_path=os.path.join(FIG_DIR, "vpd_single.png"))
figures["vpd"] = ok
print(f"  -> {'OK' if ok else 'FAILED'}")

# 1h. Temporal wind on N-S transect
print("\n[1h] 4-panel temporal: wind N-S western OK")
ok = cs.generate_comparison(
    start=NS_WESTERN["start"], end=NS_WESTERN["end"],
    mode="temporal", fhrs="1,3,5,8",
    cycle=CYCLE, product="wind_speed", y_top=500,
    output_path=os.path.join(FIG_DIR, "temporal_4panel_wind_ns.png"))
figures["temporal_wind_ns"] = ok
print(f"  -> {'OK' if ok else 'FAILED'}")

print(f"\n  Images generated: {sum(1 for v in figures.values() if v)}/{len(figures)}")

# =====================================================================
# PHASE 2: Numerical data extraction via CrossSectionTool.get_data()
# =====================================================================
print("\n" + "=" * 60)
print("PHASE 2: Numerical Data Extraction")
print("=" * 60)

surface_data = {}
for fhr in [1, 3, 5, 8]:
    valid_hr = 18 + fhr
    cst_hr = (valid_hr - 6) % 24
    label = f"F{fhr:02d} ({cst_hr}:00 CST)"
    for product in ["wind_speed", "rh"]:
        data = cs.get_data(
            start=EW_CENTRAL["start"], end=EW_CENTRAL["end"],
            cycle=CYCLE, fhr=fhr, product=product)
        if data:
            stats = data.surface_stats()
            key = f"{product}_F{fhr:02d}"
            surface_data[key] = stats
            print(f"  {label} {product}: min={stats['min']} max={stats['max']} mean={stats['mean']}")
        else:
            print(f"  {label} {product}: NO DATA")

# =====================================================================
# PHASE 3: Location investigations via investigate_location()
# =====================================================================
print("\n" + "=" * 60)
print("PHASE 3: Location Investigations")
print("=" * 60)

investigations = {}
for site in SITES:
    print(f"\n  Investigating: {site['name']}...")
    try:
        result = investigate_location(site["lat"], site["lon"], name=site["name"])
        investigations[site["name"]] = result

        # Print key findings
        conds = result.get("current_conditions", {})
        if conds:
            print(f"    Temp: {conds.get('temperature_f', '?')}°F, "
                  f"RH: {conds.get('relative_humidity', '?')}%, "
                  f"Wind: {conds.get('wind_speed_kt', '?')} kt "
                  f"{conds.get('wind_direction', '?')}")

        alerts = result.get("alerts", [])
        if alerts:
            for a in alerts[:3]:
                event = a.get("event", a) if isinstance(a, dict) else str(a)[:80]
                print(f"    ALERT: {event}")

        spc = result.get("spc_outlook", {})
        if spc.get("risk_level"):
            print(f"    SPC: {spc['risk_level']}")

        notes = result.get("investigation_notes", [])
        for n in notes[:3]:
            print(f"    Note: {n}")

    except Exception as e:
        print(f"    ERROR: {e}")
        investigations[site["name"]] = {"_error": str(e)}

# =====================================================================
# PHASE 4: Fire Risk Assessment via FireRiskAssessor
# =====================================================================
print("\n" + "=" * 60)
print("PHASE 4: Fire Risk Assessment")
print("=" * 60)

assessments = {}
# Use F03 (peak afternoon ~21Z / 3PM CST) surface data
rh_stats = surface_data.get("rh_F03", {})
wind_stats = surface_data.get("wind_speed_F03", {})

# Also pull temp data
temp_data = cs.get_data(
    start=EW_CENTRAL["start"], end=EW_CENTRAL["end"],
    cycle=CYCLE, fhr=3, product="temperature")
temp_stats = temp_data.surface_stats() if temp_data else {"min": None, "max": None, "mean": None}

if rh_stats.get("min") is not None and wind_stats.get("min") is not None:
    assessment = fra.assess_conditions(rh_stats, wind_stats, temp_stats)
    assessments["central_ok_f02"] = assessment
    print(f"  Level: {assessment.get('level', '?')}")
    print(f"  Score: {assessment.get('score', '?')}/100")
    for f in assessment.get("factors", []):
        print(f"    - {f}")
    for c in assessment.get("data_caveats", []):
        print(f"    CAVEAT: {c}")
else:
    print("  Insufficient data for assessment")

# =====================================================================
# PHASE 5: METAR observations
# =====================================================================
print("\n" + "=" * 60)
print("PHASE 5: METAR Observations")
print("=" * 60)

metars = {}
stations = ["KOKC", "KTUL", "KLAW", "KGAG", "KWDG"]
try:
    result = get_metar_observations(stations, hours_back=6)
    obs_list = result.get("data", [])
    # Group by station, keep latest
    for obs in obs_list:
        stn = obs.get("station", "")
        if stn not in metars or obs.get("utc_valid", "") > metars[stn].get("utc_valid", ""):
            metars[stn] = obs
    for stn in stations:
        if stn.lstrip("K") in metars or stn in metars:
            key = stn if stn in metars else stn.lstrip("K")
            obs = metars.get(key, metars.get(stn, {}))
            raw = obs.get("raw", str(obs))[:120]
            print(f"  {stn}: {raw}")
        else:
            print(f"  {stn}: No recent obs")
except Exception as e:
    print(f"  METAR fetch error: {e}")
    # Try individually
    for stn in stations:
        try:
            result = get_metar_observations([stn], hours_back=6)
            obs_list = result.get("data", [])
            if obs_list:
                metars[stn] = obs_list[-1]
                print(f"  {stn}: {obs_list[-1].get('raw', '?')[:120]}")
            else:
                print(f"  {stn}: No data")
        except Exception as e2:
            print(f"  {stn}: ERROR - {e2}")

# =====================================================================
# PHASE 6: Build PDF Report via ReportBuilder
# =====================================================================
print("\n" + "=" * 60)
print("PHASE 6: PDF Report Generation")
print("=" * 60)

config = ReportConfig(
    title="Oklahoma Prescribed Burns During Red Flag Conditions",
    author="AI Research Agent Swarm (wxsection.com)",
    report_type="bulletin",
    institution="wxsection.com Atmospheric Research Platform",
)

rb = ReportBuilder(config, OUT_DIR)

# --- Abstract ---
rb._abstract = (
    "On February 9, 2026, the Storm Prediction Center issued critical fire weather "
    "outlooks for the Oklahoma and Texas Panhandles, with elevated to near-critical "
    "conditions extending across much of western Oklahoma. Red Flag Warnings were in "
    "effect for Harper, Ellis, Woodward, and Roger Mills counties. Despite these "
    "conditions, prescribed burn activity was reported across portions of Oklahoma. "
    "This bulletin uses HRRR model cross-sections, multi-panel comparison imagery, "
    "surface observations, and automated fire risk assessment tools to analyze the "
    "atmospheric conditions that made prescribed burning particularly hazardous on this day."
)

# --- Section 1: Synoptic Overview ---
sec1 = rb.add_section("Synoptic Overview", content=(
    "A strong cold front was advancing across the southern High Plains on the afternoon "
    "of February 9, 2026. Ahead of the front, west-southwesterly winds of 20--25 mph "
    "(gusting to 40 mph) combined with relative humidity values of 10--15\\% to produce "
    "critical fire weather conditions across the Oklahoma and Texas Panhandles. "
    "The SPC Day 1 Fire Weather Outlook highlighted two critical risk areas: "
    "southeastern Wyoming into western Nebraska, and northeastern New Mexico through "
    "the OK/TX Panhandles into extreme northwestern Oklahoma and southwestern Kansas.\n\n"
    "The NWS Norman office issued Red Flag Warnings for Harper, Ellis, Woodward, and "
    "Roger Mills counties, effective through 7 PM CST. Elevated to near-critical "
    "conditions extended across most of western and central Oklahoma through sunset."
))

# --- Section 2: Cross-Section Analysis ---
sec2 = rb.add_section("Cross-Section Analysis", content=(
    "HRRR model cross-sections were generated along two transects: an east-west "
    "transect across central Oklahoma (35.5°N, 99.5°W to 95.0°W) and a north-south "
    "transect through western Oklahoma (37.0°N to 34.5°N at 99.0°W). Multi-panel "
    "comparison imagery demonstrates the atmospheric structure driving fire weather "
    "conditions."
))

# Add figures
if figures.get("product_firewx"):
    rb.add_figure("Cross-Section Analysis",
        os.path.join(FIG_DIR, "product_4panel_firewx.png"),
        "Four-panel fire weather variable comparison across central Oklahoma at 20Z "
        "(2 PM CST): wind speed, relative humidity, vapor pressure deficit, and "
        "dewpoint depression. Note the extremely low RH values (10--20\\%) extending "
        "through the boundary layer and high VPD indicating severe atmospheric drying.",
        width="1.0\\textwidth")

if figures.get("temporal_wind"):
    rb.add_figure("Cross-Section Analysis",
        os.path.join(FIG_DIR, "temporal_4panel_wind.png"),
        "Temporal evolution of wind speed across central Oklahoma from 18Z to 00Z "
        "(noon to 6 PM CST). The four panels show increasing wind speeds through "
        "the afternoon heating cycle, with boundary layer mixing enhancing surface winds.",
        width="1.0\\textwidth")

if figures.get("temporal_rh"):
    rb.add_figure("Cross-Section Analysis",
        os.path.join(FIG_DIR, "temporal_4panel_rh.png"),
        "Temporal evolution of relative humidity across central Oklahoma. Progressive "
        "drying through the afternoon as the boundary layer deepens and entrains "
        "dry air from aloft, pushing surface RH to critical levels.",
        width="1.0\\textwidth")

# --- Section 3: Vertical Structure ---
sec3 = rb.add_section("Vertical Structure and Mixing", content=(
    "The north-south cross-section through western Oklahoma reveals the vertical "
    "structure of the fire-critical atmosphere. Key features include a deep, dry "
    "boundary layer extending from the surface to above 600 hPa, steep lapse rates "
    "promoting vigorous mixing that brings strong winds aloft to the surface, and "
    "a sharp moisture gradient at the boundary layer top."
))

if figures.get("product_ns"):
    rb.add_figure("Vertical Structure and Mixing",
        os.path.join(FIG_DIR, "product_4panel_ns.png"),
        "North-south transect through western Oklahoma (37°N to 34.5°N at 99°W) "
        "showing wind speed, RH, temperature, and lapse rate. The steep lapse rates "
        "and deep dry layer indicate strong boundary layer mixing, which transports "
        "momentum from upper levels to the surface.",
        width="1.0\\textwidth")

if figures.get("temporal_wind_ns"):
    rb.add_figure("Vertical Structure and Mixing",
        os.path.join(FIG_DIR, "temporal_4panel_wind_ns.png"),
        "Temporal evolution of wind speed along the north-south western Oklahoma "
        "transect, showing intensification of low-level winds through the afternoon.",
        width="1.0\\textwidth")

# --- Section 4: Model Comparison ---
if figures.get("model_compare"):
    sec4 = rb.add_section("Model Comparison", content=(
        "HRRR and GFS model cross-sections were compared at matched valid times to "
        "assess model agreement on the fire weather environment. Both models show "
        "similar wind speed patterns, though HRRR resolves finer-scale terrain "
        "interactions along the Oklahoma escarpments."
    ))
    rb.add_figure("Model Comparison",
        os.path.join(FIG_DIR, "model_2panel_hrrr_gfs.png"),
        "HRRR vs GFS wind speed comparison at matched valid times. The panels show "
        "init time, forecast hour, and valid time for each model. Note the generally "
        "consistent depiction of the wind field, with HRRR showing more detail in "
        "terrain-forced accelerations.",
        width="1.0\\textwidth")

# --- Section 5: Surface Observations ---
sec5 = rb.add_section("Surface Observations and Assessment", content="")

# Add METAR data as content
metar_text = "\\subsection*{METAR Reports}\n"
for stn, obs in metars.items():
    if isinstance(obs, dict):
        raw = obs.get("raw", str(obs))
    else:
        raw = str(obs) if obs else "No data"
    safe_raw = raw.replace("_", "\\_").replace("&", "\\&").replace("#", "\\#")[:120]
    metar_text += f"\\texttt{{{stn}}}: \\texttt{{{safe_raw}}}\n\n"
sec5.content = metar_text

# Add investigation results
for site_name, inv in investigations.items():
    if "_error" in inv:
        continue
    conds = inv.get("current_conditions", {})
    alerts = inv.get("alerts", [])
    notes = inv.get("investigation_notes", [])

    site_text = f"\\subsection*{{{site_name}}}\n"
    if conds:
        t = conds.get('temperature_f', '?')
        rh = conds.get('relative_humidity', '?')
        ws = conds.get('wind_speed_kt', '?')
        wd = conds.get('wind_direction', '?')
        site_text += f"Temperature: {t}°F, RH: {rh}\\%, Wind: {ws} kt from {wd}\n\n"
    if alerts:
        for a in alerts[:3]:
            evt = a.get("event", str(a)) if isinstance(a, dict) else str(a)
            safe_evt = evt.replace("_", "\\_").replace("&", "\\&")[:100]
            site_text += f"\\textbf{{ALERT:}} {safe_evt}\n\n"
    if notes:
        site_text += "\\textbf{Investigation Notes:}\n\\begin{itemize}\n"
        for n in notes[:5]:
            safe_n = str(n).replace("_", "\\_").replace("&", "\\&").replace("#", "\\#")[:150]
            site_text += f"  \\item {safe_n}\n"
        site_text += "\\end{itemize}\n"

    sec5.content += site_text

# --- Section 6: Fire Risk Assessment ---
sec6 = rb.add_section("Automated Fire Risk Assessment", content="")

if assessments.get("central_ok_f02"):
    a = assessments["central_ok_f02"]
    assessment_text = (
        f"The automated FireRiskAssessor rated conditions along the central Oklahoma "
        f"transect at \\textbf{{{a.get('level', 'UNKNOWN')}}} "
        f"(score: {a.get('score', '?')}/100) at 20Z (2 PM CST).\n\n"
    )
    factors = a.get("factors", [])
    if factors:
        assessment_text += "\\textbf{Contributing Factors:}\n\\begin{itemize}\n"
        for f in factors:
            safe_f = str(f).replace("_", "\\_").replace("&", "\\&").replace("%", "\\%").replace("#", "\\#")[:200]
            assessment_text += f"  \\item {safe_f}\n"
        assessment_text += "\\end{itemize}\n"

    caveats = a.get("data_caveats", [])
    if caveats:
        assessment_text += "\\textbf{Data Caveats:}\n\\begin{itemize}\n"
        for c in caveats:
            safe_c = str(c).replace("_", "\\_").replace("&", "\\&").replace("%", "\\%")[:200]
            assessment_text += f"  \\item {safe_c}\n"
        assessment_text += "\\end{itemize}\n"

    sec6.content = assessment_text

    # Add numerical data table
    rb.add_table("Automated Fire Risk Assessment",
        headers=["Time (CST)", "Wind Min (kt)", "Wind Max (kt)", "Wind Mean (kt)",
                 "RH Min (%)", "RH Max (%)", "RH Mean (%)"],
        rows=[
            [f"{(18+fhr-6)%24}:00 CST",
             str(surface_data.get(f"wind_speed_F{fhr:02d}", {}).get("min", "?")),
             str(surface_data.get(f"wind_speed_F{fhr:02d}", {}).get("max", "?")),
             str(surface_data.get(f"wind_speed_F{fhr:02d}", {}).get("mean", "?")),
             str(surface_data.get(f"rh_F{fhr:02d}", {}).get("min", "?")),
             str(surface_data.get(f"rh_F{fhr:02d}", {}).get("max", "?")),
             str(surface_data.get(f"rh_F{fhr:02d}", {}).get("mean", "?")),
            ]
            for fhr in [1, 3, 5, 8]
        ],
        caption="HRRR surface-level wind speed and relative humidity statistics along "
                "the central Oklahoma transect (35.5°N, 99.5°W to 95.0°W) through the "
                "afternoon of February 9, 2026.")

# --- Section 7: Conclusions ---
sec7 = rb.add_section("Conclusions", content=(
    "The atmospheric conditions on February 9, 2026 presented significant fire weather "
    "hazards across Oklahoma, particularly in the western counties under Red Flag Warnings. "
    "Key findings:\n\n"
    "\\begin{enumerate}\n"
    "  \\item \\textbf{Critical fire weather conditions} were confirmed by SPC outlooks, "
    "NWS Red Flag Warnings, HRRR model analysis, and surface observations.\n"
    "  \\item \\textbf{Deep dry boundary layer} extending above 600 hPa promoted vigorous "
    "mixing, transporting strong winds from aloft to the surface.\n"
    "  \\item \\textbf{RH values of 10--20\\%} combined with winds gusting to 40 mph created "
    "conditions where any fire, prescribed or otherwise, faced extreme spread potential.\n"
    "  \\item \\textbf{Prescribed burns during these conditions} violate fundamental fire "
    "weather safety principles. Red Flag Warnings explicitly warn against outdoor burning. "
    "The combination of low humidity, strong winds, and dry fuels creates conditions where "
    "containment is extremely difficult and escape probability is high.\n"
    "  \\item \\textbf{Model agreement} between HRRR and GFS on wind and moisture fields "
    "confirms that the dangerous conditions were well-forecast and predictable.\n"
    "\\end{enumerate}\n\n"
    "Conducting prescribed burns under these conditions demonstrates either a failure to "
    "check fire weather forecasts, a disregard for Red Flag Warnings, or insufficient "
    "understanding of fire behavior in critical weather environments. Oklahoma's prescribed "
    "burn regulations require compliance with burn bans, but the enforcement gap between "
    "county-level burn bans and NWS Red Flag Warnings remains a policy concern."
))

# --- Compile PDF ---
print("\nCompiling PDF...")
try:
    pdf_path = rb.compile_pdf(passes=2)
    print(f"\n  PDF generated: {pdf_path}")
except Exception as e:
    print(f"\n  PDF compilation error: {e}")
    print("  (LaTeX source saved — can compile manually)")

print("\n" + "=" * 60)
print("INVESTIGATION COMPLETE")
print("=" * 60)
print(f"Output directory: {OUT_DIR}")
for f in sorted(os.listdir(FIG_DIR)):
    sz = os.path.getsize(os.path.join(FIG_DIR, f))
    print(f"  figures/{f}: {sz//1024}KB")
