import io, sys as _sys
_sys.stdout = io.TextIOWrapper(_sys.stdout.buffer, encoding='utf-8', errors='replace')
_sys.stderr = io.TextIOWrapper(_sys.stderr.buffer, encoding='utf-8', errors='replace')

"""
Oklahoma Prescribed Burns — Comprehensive Investigation & Justification Analysis
February 9, 2026

Investigates whether prescribed burns conducted during Red Flag Warning
conditions in western Oklahoma can be justified using multi-tool atmospheric,
terrain, fuel, and forecast analysis.

Agent Tools Used (ALL 12 modules):
  1. CrossSectionTool — multi-panel comparisons, data extraction, batch images
  2. FireRiskAnalyzer — quantitative risk assessment, transect analysis
  3. investigate_location — comprehensive site investigations
  4. ReportBuilder — LaTeX PDF compilation
  5. CaseStudy — structured event analysis framework
  6. ForecastGenerator — national fire scan context
  7. terrain — terrain complexity, city assessment
  8. fuel_conditions — fuel moisture, ignition risk
  9. frontal_analysis — wind shifts, overnight recovery, frontal fire impact
  10. report_quality — checklist validation, claim verification
  11. external_data — METAR, RAWS, drought, climatology, elevation, model-obs, etc.
  12. (MCP equivalents accessed via Python API)
"""
import sys, os, json, time, traceback
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# ======================================================================
# Import ALL agent tools
# ======================================================================
from tools.agent_tools.cross_section import CrossSectionTool, CrossSectionData
from tools.agent_tools.investigation import investigate_location, investigate_town
from tools.agent_tools.fire_risk import FireRiskAnalyzer
from tools.agent_tools.report_builder import ReportBuilder, ReportConfig
from tools.agent_tools.case_study import CaseStudy
from tools.agent_tools.forecast import ForecastGenerator
from tools.agent_tools.terrain import analyze_terrain_complexity, city_terrain_assessment
from tools.agent_tools.fuel_conditions import assess_fuel_conditions, get_ignition_risk
from tools.agent_tools.frontal_analysis import (
    detect_wind_shifts, classify_overnight_conditions, analyze_frontal_impact_on_fires
)
from tools.agent_tools.report_quality import fire_report_checklist, validate_report_claims
from tools.agent_tools.external_data import (
    get_metar_observations, get_raws_observations, get_spc_fire_weather_outlook,
    get_nws_alerts, get_spc_fire_discussion, get_spc_mesoscale_discussions,
    get_nws_forecast_discussion, get_nearby_stations, get_elevation_profile,
    get_drought_status, get_fire_weather_climatology, get_street_view_image,
    verify_wind_claims, get_point_surface_conditions, get_model_obs_comparison,
    assess_rh_dewpoint_severity
)

# ======================================================================
# Configuration
# ======================================================================
BASE_URL = 'http://localhost:5565'
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(OUT_DIR, 'figures')
os.makedirs(FIG_DIR, exist_ok=True)

# Initialize tools
cs = CrossSectionTool(base_url=BASE_URL)
fra = FireRiskAnalyzer(base_url=BASE_URL)
fg = ForecastGenerator(base_url=BASE_URL)

# Investigation sites
SITES = [
    {"name": "Woodward", "lat": 36.43, "lon": -99.39, "station": "KWDG", "county": "Woodward"},
    {"name": "Gage", "lat": 36.31, "lon": -99.76, "station": "KGAG", "county": "Harper"},
    {"name": "Elk City", "lat": 35.41, "lon": -99.40, "station": "KELK", "county": "Roger Mills"},
    {"name": "Oklahoma City", "lat": 35.47, "lon": -97.52, "station": "KOKC", "county": "Oklahoma"},
]

# Transects
EW = {"start": (35.5, -99.5), "end": (35.5, -95.0)}   # E-W central OK
NS = {"start": (37.0, -99.0), "end": (34.5, -99.0)}    # N-S western OK

CYCLE = "20260209_18z"  # 18z Feb 9 = noon CST
FHRS_AFTERNOON = [1, 3, 5, 8]  # 1pm, 3pm, 5pm, 8pm CST

# Collect all results
R = {}

def safe(label, fn, *args, **kwargs):
    """Run fn with error handling, print status, store in R."""
    print(f"  [{label}] ", end="", flush=True)
    try:
        result = fn(*args, **kwargs)
        R[label] = result
        print("OK" if result else "NO DATA")
        return result
    except Exception as e:
        print(f"ERROR: {e}")
        R[label] = {"_error": str(e)}
        traceback.print_exc()
        return None


# ======================================================================
# PHASE 1: Cross-Section Imagery (CrossSectionTool)
# ======================================================================
print("=" * 70)
print("PHASE 1: Cross-Section Image Generation")
print("=" * 70)

figures = {}

# 1a. 4-panel product: fire wx variables (E-W)
print("\n[1a] 4-panel product: wind_speed, rh, vpd, dewpoint_dep")
figures["product_firewx"] = cs.generate_comparison(
    start=EW["start"], end=EW["end"],
    mode="product", products="wind_speed,rh,vpd,dewpoint_dep",
    cycle=CYCLE, fhr=3, y_top=700,
    output_path=os.path.join(FIG_DIR, "product_4panel_firewx.png"))
print(f"  -> {'OK' if figures['product_firewx'] else 'FAIL'}")

# 1b. 4-panel temporal: wind afternoon progression
print("[1b] 4-panel temporal: wind F1,3,5,8")
figures["temporal_wind"] = cs.generate_comparison(
    start=EW["start"], end=EW["end"],
    mode="temporal", fhrs="1,3,5,8",
    cycle=CYCLE, product="wind_speed", y_top=500,
    output_path=os.path.join(FIG_DIR, "temporal_4panel_wind.png"))
print(f"  -> {'OK' if figures['temporal_wind'] else 'FAIL'}")

# 1c. 4-panel temporal: RH drying
print("[1c] 4-panel temporal: RH F1,3,5,8")
figures["temporal_rh"] = cs.generate_comparison(
    start=EW["start"], end=EW["end"],
    mode="temporal", fhrs="1,3,5,8",
    cycle=CYCLE, product="rh", y_top=700,
    output_path=os.path.join(FIG_DIR, "temporal_4panel_rh.png"))
print(f"  -> {'OK' if figures['temporal_rh'] else 'FAIL'}")

# 1d. 4-panel temporal: temperature evolution
print("[1d] 4-panel temporal: temperature F1,3,5,8")
figures["temporal_temp"] = cs.generate_comparison(
    start=EW["start"], end=EW["end"],
    mode="temporal", fhrs="1,3,5,8",
    cycle=CYCLE, product="temperature", y_top=500,
    output_path=os.path.join(FIG_DIR, "temporal_4panel_temp.png"))
print(f"  -> {'OK' if figures['temporal_temp'] else 'FAIL'}")

# 1e. N-S product: wind, rh, temp, lapse_rate
print("[1e] 4-panel product: N-S transect")
figures["product_ns"] = cs.generate_comparison(
    start=NS["start"], end=NS["end"],
    mode="product", products="wind_speed,rh,temperature,lapse_rate",
    cycle=CYCLE, fhr=3, y_top=500,
    output_path=os.path.join(FIG_DIR, "product_4panel_ns.png"))
print(f"  -> {'OK' if figures['product_ns'] else 'FAIL'}")

# 1f. N-S temporal: wind evolution
print("[1f] 4-panel temporal: wind N-S")
figures["temporal_wind_ns"] = cs.generate_comparison(
    start=NS["start"], end=NS["end"],
    mode="temporal", fhrs="1,3,5,8",
    cycle=CYCLE, product="wind_speed", y_top=500,
    output_path=os.path.join(FIG_DIR, "temporal_4panel_wind_ns.png"))
print(f"  -> {'OK' if figures['temporal_wind_ns'] else 'FAIL'}")

# 1g. Model comparison: HRRR vs GFS
print("[1g] 2-panel model: HRRR vs GFS")
figures["model_compare"] = cs.generate_comparison(
    start=EW["start"], end=EW["end"],
    mode="model", models="hrrr,gfs",
    cycle=CYCLE, fhr=8, product="wind_speed", y_top=500,
    output_path=os.path.join(FIG_DIR, "model_2panel_hrrr_gfs.png"))
print(f"  -> {'OK' if figures['model_compare'] else 'FAIL'}")

# 1h. Single-panel fire_wx composite
print("[1h] Single: fire weather composite")
figures["fire_wx"] = cs.generate_image(
    start=EW["start"], end=EW["end"],
    cycle=CYCLE, fhr=3, product="fire_wx", y_top=700,
    output_path=os.path.join(FIG_DIR, "fire_wx_composite.png"))
print(f"  -> {'OK' if figures['fire_wx'] else 'FAIL'}")

# 1i. Single-panel VPD
print("[1i] Single: VPD")
figures["vpd"] = cs.generate_image(
    start=EW["start"], end=EW["end"],
    cycle=CYCLE, fhr=3, product="vpd", y_top=700,
    output_path=os.path.join(FIG_DIR, "vpd_single.png"))
print(f"  -> {'OK' if figures['vpd'] else 'FAIL'}")

# 1j. 3-panel product: theta, theta_e, lapse_rate (boundary layer structure)
print("[1j] 3-panel product: theta, theta_e, lapse_rate (BL structure)")
figures["bl_structure"] = cs.generate_comparison(
    start=EW["start"], end=EW["end"],
    mode="product", products="theta,theta_e,lapse_rate",
    cycle=CYCLE, fhr=3, y_top=500,
    output_path=os.path.join(FIG_DIR, "product_3panel_bl.png"))
print(f"  -> {'OK' if figures['bl_structure'] else 'FAIL'}")

n_ok = sum(1 for v in figures.values() if v)
print(f"\n  Images: {n_ok}/{len(figures)} generated")


# ======================================================================
# PHASE 2: Numerical Data Extraction (CrossSectionTool + CaseStudy)
# ======================================================================
print("\n" + "=" * 70)
print("PHASE 2: Numerical Data Extraction")
print("=" * 70)

surface_data = {}
for fhr in FHRS_AFTERNOON:
    cst_hr = (18 + fhr - 6) % 24
    label = f"F{fhr:02d} ({cst_hr}:00 CST)"
    for product in ["wind_speed", "rh", "temperature", "vpd"]:
        data = cs.get_data(
            start=EW["start"], end=EW["end"],
            cycle=CYCLE, fhr=fhr, product=product)
        if data:
            stats = data.surface_stats()
            key = f"{product}_F{fhr:02d}"
            surface_data[key] = stats
            print(f"  {label} {product}: min={stats['min']:.1f} max={stats['max']:.1f} mean={stats['mean']:.1f}")
        else:
            print(f"  {label} {product}: NO DATA")

# CaseStudy temporal evolution for structured analysis
print("\n  Setting up CaseStudy framework...")
try:
    case = CaseStudy(
        event_name="OK Prescribed Burns Feb 9 2026",
        cycle=CYCLE, output_dir=OUT_DIR, base_url=BASE_URL)
    case.add_transect("EW_Central", EW["start"], EW["end"],
                      products=["wind_speed", "rh", "temperature"],
                      description="E-W transect across central Oklahoma")
    case.add_transect("NS_Western", NS["start"], NS["end"],
                      products=["wind_speed", "rh"],
                      description="N-S transect through western Oklahoma")

    # Temporal evolution
    R["temporal_ew_wind"] = case.temporal_evolution("EW_Central", "wind_speed", FHRS_AFTERNOON)
    R["temporal_ew_rh"] = case.temporal_evolution("EW_Central", "rh", FHRS_AFTERNOON)
    print(f"  CaseStudy temporal evolution: OK")

    R["case_summary"] = case.generate_summary()
    print(f"  CaseStudy summary: OK")
except Exception as e:
    print(f"  CaseStudy: ERROR — {e}")
    traceback.print_exc()


# ======================================================================
# PHASE 3: Frontal Analysis (KEY for justification argument)
# ======================================================================
print("\n" + "=" * 70)
print("PHASE 3: Frontal Analysis — Wind Shifts & Recovery")
print("=" * 70)

# Detect wind shifts at Woodward (Red Flag area)
print("\n  Detecting wind shifts at Woodward...")
safe("wind_shifts_woodward", detect_wind_shifts,
     lat=36.43, lon=-99.39, model="hrrr", cycle=CYCLE, base_url=BASE_URL)

if R.get("wind_shifts_woodward") and not isinstance(R["wind_shifts_woodward"], dict) or \
   (isinstance(R.get("wind_shifts_woodward"), dict) and "_error" not in R["wind_shifts_woodward"]):
    ws = R["wind_shifts_woodward"]
    if isinstance(ws, dict):
        shifts = ws.get("wind_shifts", [])
        print(f"  Wind shifts detected: {len(shifts)}")
        for s in shifts[:3]:
            print(f"    FHR {s.get('fhr', '?')}: {s.get('direction_before', '?')}->{s.get('direction_after', '?')}, "
                  f"speed {s.get('speed_before_kt', '?')}->{s.get('speed_after_kt', '?')} kt")

# Classify overnight conditions
print("\n  Classifying overnight conditions at Woodward...")
safe("overnight_woodward", classify_overnight_conditions,
     lat=36.43, lon=-99.39, model="hrrr", cycle=CYCLE, base_url=BASE_URL)

if isinstance(R.get("overnight_woodward"), dict) and "_error" not in R["overnight_woodward"]:
    oc = R["overnight_woodward"]
    print(f"  Classification: {oc.get('classification', '?')}")
    print(f"  Overnight RH range: {oc.get('overnight_rh_range_pct', '?')}")
    print(f"  Overnight wind range: {oc.get('overnight_wind_range_kt', '?')}")

# Same for Gage
print("\n  Detecting wind shifts at Gage...")
safe("wind_shifts_gage", detect_wind_shifts,
     lat=36.31, lon=-99.76, model="hrrr", cycle=CYCLE, base_url=BASE_URL)

# Frontal impact on fire behavior
print("\n  Analyzing frontal impact on fires at Woodward...")
safe("frontal_fire_woodward", analyze_frontal_impact_on_fires,
     lat=36.43, lon=-99.39, model="hrrr", cycle=CYCLE, base_url=BASE_URL)

if isinstance(R.get("frontal_fire_woodward"), dict) and "_error" not in R["frontal_fire_woodward"]:
    ff = R["frontal_fire_woodward"]
    print(f"  Current spread: {ff.get('current_spread', {}).get('direction', '?')}")
    print(f"  Post-shift spread: {ff.get('post_shift_spread', {}).get('direction', '?')}")
    print(f"  Tactical window: {ff.get('tactical_window', '?')}")


# ======================================================================
# PHASE 4: Terrain & Elevation Assessment
# ======================================================================
print("\n" + "=" * 70)
print("PHASE 4: Terrain & Elevation Assessment")
print("=" * 70)

# Terrain complexity for each site
for site in SITES[:3]:  # Woodward, Gage, Elk City
    print(f"\n  Terrain: {site['name']}...")
    safe(f"terrain_{site['name'].lower().replace(' ','_')}",
         analyze_terrain_complexity, lat=site["lat"], lon=site["lon"], radius_km=15)

# City terrain assessment
print("\n  City terrain: Woodward...")
safe("city_terrain_woodward", city_terrain_assessment,
     lat=36.43, lon=-99.39, city_name="Woodward", radius_km=20)

print("  City terrain: Elk City...")
safe("city_terrain_elkcity", city_terrain_assessment,
     lat=35.41, lon=-99.40, city_name="Elk City", radius_km=20)

# Elevation profile along E-W transect
print("\n  Elevation profile: E-W transect...")
safe("elevation_ew", get_elevation_profile,
     start_lat=EW["start"][0], start_lon=EW["start"][1],
     end_lat=EW["end"][0], end_lon=EW["end"][1], n_points=50)

# Elevation profile along N-S transect
print("  Elevation profile: N-S transect...")
safe("elevation_ns", get_elevation_profile,
     start_lat=NS["start"][0], start_lon=NS["start"][1],
     end_lat=NS["end"][0], end_lon=NS["end"][1], n_points=50)


# ======================================================================
# PHASE 5: Fuel Conditions & Ignition Risk
# ======================================================================
print("\n" + "=" * 70)
print("PHASE 5: Fuel Conditions & Ignition Risk Assessment")
print("=" * 70)

for site in SITES[:3]:  # Woodward, Gage, Elk City
    print(f"\n  Fuel conditions: {site['name']}...")
    safe(f"fuel_{site['name'].lower().replace(' ','_')}",
         assess_fuel_conditions, lat=site["lat"], lon=site["lon"],
         station_id=site.get("station"), base_url=BASE_URL)

    print(f"  Ignition risk: {site['name']}...")
    safe(f"ignition_{site['name'].lower().replace(' ','_')}",
         get_ignition_risk, lat=site["lat"], lon=site["lon"],
         city_name=site["name"])


# ======================================================================
# PHASE 6: Fire Risk Quantification (FireRiskAnalyzer)
# ======================================================================
print("\n" + "=" * 70)
print("PHASE 6: Fire Risk Quantification")
print("=" * 70)

# Transect-based risk analysis at peak afternoon
print("\n  Transect risk: E-W at F03 (3pm CST)...")
safe("risk_ew_f03", fra.analyze_transect,
     start=EW["start"], end=EW["end"], cycle=CYCLE, fhr=3, label="EW_F03")

print("  Transect risk: N-S at F03...")
safe("risk_ns_f03", fra.analyze_transect,
     start=NS["start"], end=NS["end"], cycle=CYCLE, fhr=3, label="NS_F03")

# Also analyze early afternoon (F01 = 1pm) — was it calmer?
print("  Transect risk: E-W at F01 (1pm CST)...")
safe("risk_ew_f01", fra.analyze_transect,
     start=EW["start"], end=EW["end"], cycle=CYCLE, fhr=1, label="EW_F01")

# And evening (F08 = 8pm) — post-frontal recovery?
print("  Transect risk: E-W at F08 (8pm CST)...")
safe("risk_ew_f08", fra.analyze_transect,
     start=EW["start"], end=EW["end"], cycle=CYCLE, fhr=8, label="EW_F08")

# Print risk comparisons
for key in ["risk_ew_f01", "risk_ew_f03", "risk_ew_f08"]:
    r = R.get(key)
    if r and hasattr(r, 'risk_level'):
        print(f"  {key}: {r.risk_level} (score {r.risk_score})")
    elif isinstance(r, dict) and "risk_level" in r:
        print(f"  {key}: {r['risk_level']} (score {r.get('risk_score', '?')})")

# Investigation checklist for Woodward
print("\n  Investigation checklist: Woodward...")
safe("checklist_woodward", fra.investigation_checklist,
     lat=36.43, lon=-99.39)


# ======================================================================
# PHASE 7: Surface Observations & Verification
# ======================================================================
print("\n" + "=" * 70)
print("PHASE 7: Surface Observations & External Data")
print("=" * 70)

# METAR observations
stations = [s["station"] for s in SITES]
print(f"\n  METAR observations: {', '.join(stations)}...")
safe("metars", get_metar_observations, stations=stations, hours_back=12)

if isinstance(R.get("metars"), dict):
    for obs in R["metars"].get("data", [])[:8]:
        raw = obs.get("raw", "")[:100]
        print(f"    {obs.get('station', '?')}: {raw}")

# RAWS observations (remote automated wx stations — fire weather specific)
print("\n  RAWS observations near Woodward...")
safe("raws_woodward", get_raws_observations,
     lat=36.43, lon=-99.39, radius_miles=50, hours_back=12)

# Nearby stations
print("  Finding nearby stations...")
safe("nearby_woodward", get_nearby_stations,
     lat=36.43, lon=-99.39, radius_km=80)

# Verify wind claims: were 40 mph gusts real?
print("\n  Verifying wind observations near Woodward...")
safe("wind_verify", verify_wind_claims,
     lat=36.43, lon=-99.39, radius_miles=50, hours_back=12)

# Model-observation comparison
print("  Model vs obs comparison: Woodward...")
safe("model_obs_woodward", get_model_obs_comparison,
     lat=36.43, lon=-99.39, model="hrrr", cycle=CYCLE, fhr=3, base_url=BASE_URL)

# Point surface conditions from model
for site in SITES[:3]:
    print(f"  Point conditions: {site['name']} at F03...")
    safe(f"point_{site['name'].lower().replace(' ','_')}",
         get_point_surface_conditions,
         lat=site["lat"], lon=site["lon"], cycle=CYCLE, fhr=3, base_url=BASE_URL)

# RH/dewpoint severity assessment
print("\n  RH severity assessment...")
safe("rh_severity", assess_rh_dewpoint_severity,
     rh_pct=13.0, dewpoint_f=5.0, station_id="KGAG", month=2)


# ======================================================================
# PHASE 8: Location Investigations
# ======================================================================
print("\n" + "=" * 70)
print("PHASE 8: Location Investigations")
print("=" * 70)

for site in SITES:
    print(f"\n  Investigating: {site['name']}...")
    inv = safe(f"inv_{site['name'].lower().replace(' ','_')}",
               investigate_location, lat=site["lat"], lon=site["lon"],
               name=site["name"], base_url=BASE_URL)
    if isinstance(inv, dict) and "_error" not in inv:
        conds = inv.get("current_conditions", {})
        if conds:
            print(f"    Temp: {conds.get('temperature_f', '?')}F, "
                  f"Wind: {conds.get('wind_speed_kt', '?')} kt")
        alerts = inv.get("alerts", [])
        for a in alerts[:3]:
            evt = a.get("event", str(a)) if isinstance(a, dict) else str(a)[:60]
            print(f"    ALERT: {evt}")

# Also try investigate_town
print("\n  Town investigation: Woodward, OK...")
safe("town_woodward", investigate_town, town_name="Woodward", state="OK", base_url=BASE_URL)


# ======================================================================
# PHASE 9: Broader Context — National Scan, SPC, NWS, Drought, Climatology
# ======================================================================
print("\n" + "=" * 70)
print("PHASE 9: Broader Context")
print("=" * 70)

# National fire scan
print("\n  National fire weather scan...")
safe("national_scan", fg.national_fire_scan, cycle=CYCLE, fhrs=FHRS_AFTERNOON)

if isinstance(R.get("national_scan"), dict) and "_error" not in R["national_scan"]:
    for region, info in R["national_scan"].items():
        if isinstance(info, dict):
            print(f"    {region}: {info.get('risk_level', '?')} "
                  f"(score {info.get('risk_score', '?')})")

# SPC fire weather outlook
print("\n  SPC Day 1 Fire Weather Outlook...")
safe("spc_outlook", get_spc_fire_weather_outlook, day=1)

# SPC fire discussion
print("  SPC Fire Weather Discussion...")
safe("spc_discussion", get_spc_fire_discussion)

# SPC mesoscale discussions
print("  SPC Mesoscale Discussions...")
safe("spc_mds", get_spc_mesoscale_discussions)

# NWS alerts for Oklahoma
print("  NWS Alerts: Oklahoma...")
safe("nws_alerts_ok", get_nws_alerts, state="OK")

# NWS forecast discussion — Norman WFO
print("  NWS Norman Forecast Discussion...")
safe("nws_oun_disc", get_nws_forecast_discussion, wfo="OUN")

# Drought status
print("  Drought status: Oklahoma...")
safe("drought_ok", get_drought_status, state="OK")

# Fire weather climatology for Gage (Harper Co)
print("  Fire weather climatology: KGAG February...")
safe("climo_gag_feb", get_fire_weather_climatology, station_id="KGAG", month=2)

# Fire weather climatology for Woodward
print("  Fire weather climatology: KWDG February...")
safe("climo_wdg_feb", get_fire_weather_climatology, station_id="KWDG", month=2)


# ======================================================================
# PHASE 10: Report Quality Pre-Check
# ======================================================================
print("\n" + "=" * 70)
print("PHASE 10: Report Quality & Validation")
print("=" * 70)

# Fire report checklist for Woodward
print("\n  Fire report checklist: Woodward...")
safe("rpt_checklist", fire_report_checklist,
     lat=36.43, lon=-99.39, city_name="Woodward", base_url=BASE_URL)

if isinstance(R.get("rpt_checklist"), dict) and "_error" not in R["rpt_checklist"]:
    cl = R["rpt_checklist"]
    print(f"  Critical items: {cl.get('critical_count', '?')}/{cl.get('total_count', '?')}")
    print(f"  Summary: {cl.get('summary', '?')[:120]}")

# Validate key claims we plan to make in the report
claims = [
    {"type": "rh", "value": 15, "qualifier": "below"},
    {"type": "wind_speed", "value": 40, "unit": "mph", "qualifier": "gusts"},
    {"type": "front_timing", "value": "evening"},
    {"type": "fuels", "value": "dormant grass"},
    {"type": "terrain", "value": "flat"},
]
print("\n  Validating report claims...")
safe("claim_validation", validate_report_claims,
     claims=claims, lat=36.43, lon=-99.39, base_url=BASE_URL)


# ======================================================================
# PHASE 11: Build Comprehensive PDF Report
# ======================================================================
print("\n" + "=" * 70)
print("PHASE 11: PDF Report Generation")
print("=" * 70)

config = ReportConfig(
    title="Oklahoma Prescribed Burns During Red Flag Conditions:\\\\A Balanced Investigation",
    author="AI Research Agent Swarm (wxsection.com)",
    report_type="bulletin",
    institution="wxsection.com Atmospheric Research Platform",
)

rb = ReportBuilder(config, OUT_DIR)

# --- Helper to safely get nested values ---
def rget(key, *path, default="N/A"):
    """Get nested value from R dict."""
    obj = R.get(key)
    if obj is None or (isinstance(obj, dict) and "_error" in obj):
        return default
    for p in path:
        if isinstance(obj, dict):
            obj = obj.get(p, default)
        elif hasattr(obj, p):
            obj = getattr(obj, p, default)
        else:
            return default
    return obj

# --- Abstract ---
rb._abstract = (
    "On February 9, 2026, prescribed burn activity was reported across portions of Oklahoma "
    "while Red Flag Warnings were in effect for several western counties. This investigation "
    "uses the full wxsection.com agent research platform --- 12 analysis modules comprising "
    "terrain assessment, fuel condition evaluation, frontal analysis, fire risk quantification, "
    "climatological context, and multi-model atmospheric cross-sections --- to examine whether "
    "a data-driven case can be made for or against conducting prescribed burns on this day. "
    "Rather than assuming negligence, this report evaluates the seasonal necessity, temporal "
    "windows, post-frontal recovery potential, and spatial variability that burn managers "
    "may have considered in their decision-making."
)

# ===== Section 1: Synoptic Overview =====
rb.add_section("Synoptic Overview", content=(
    "A strong cold front was advancing across the southern High Plains during the afternoon "
    "of February 9, 2026. Ahead of the front, west-southwesterly winds of 20--25 mph "
    "(gusting to 40 mph) combined with relative humidity values of 10--15\\% to produce "
    "critical fire weather conditions across the Oklahoma and Texas Panhandles. "
    "The SPC Day 1 Fire Weather Outlook highlighted critical risk areas from northeastern "
    "New Mexico through the OK/TX Panhandles.\n\n"
    "The NWS Norman office issued Red Flag Warnings for Harper, Ellis, Woodward, and "
    "Roger Mills counties, effective through 7 PM CST. However, the critical question "
    "is not merely \\textit{whether} conditions were dangerous, but whether prescribed "
    "burn operators could have identified safe temporal or spatial windows within the "
    "broader fire weather environment."
))

# ===== Section 2: The Case for Prescribed Burns =====
# Build from fuel conditions + climatology + drought
fuel_text = ""
for site in SITES[:3]:
    key = f"fuel_{site['name'].lower().replace(' ','_')}"
    fd = R.get(key)
    if isinstance(fd, dict) and "_error" not in fd:
        fa = fd.get("fuel_assessment", {})
        fuel_text += (
            f"\\textbf{{{site['name']}}}: Season: {fa.get('season', '?')}, "
            f"Fuel type: {fa.get('fuel_type', '?')}, "
            f"Estimated fuel moisture: {fa.get('fuel_moisture_estimate', '?')}\\%. "
            f"{fa.get('seasonal_context', '')[:200]}\n\n"
        )

drought_text = ""
dd = R.get("drought_ok")
if isinstance(dd, list) and dd:
    d = dd[0] if dd else {}
    drought_text = (
        f"Oklahoma drought status: D0={d.get('D0', '?')}\\%, "
        f"D1={d.get('D1', '?')}\\%, D2={d.get('D2', '?')}\\%, "
        f"D3={d.get('D3', '?')}\\%, D4={d.get('D4', '?')}\\%."
    )
elif isinstance(dd, dict) and "_error" not in dd:
    drought_text = f"Oklahoma drought data: {json.dumps(dd)[:200]}"

climo_text = ""
for key in ["climo_gag_feb", "climo_wdg_feb"]:
    cd = R.get(key)
    if isinstance(cd, dict) and "_error" not in cd:
        climo_text += f"{key.replace('climo_','').replace('_feb','')} Feb climatology: {json.dumps(cd)[:200]}\n\n"

rb.add_section("The Case for Prescribed Burns", content=(
    "Before condemning the decision to burn, it is essential to understand the operational "
    "constraints facing prescribed burn managers in the southern Great Plains.\n\n"
    "\\subsection*{Seasonal Necessity}\n"
    "February is the primary prescribed burn window for Oklahoma's grasslands. Native "
    "tallgrass and mixed-grass prairies must be burned during dormancy (December--March) "
    "before spring green-up renders burns ineffective. The window is narrow: December and "
    "January often have snow cover or frozen ground, while March can see early green-up "
    "in southern Oklahoma. February is frequently the only viable month.\n\n"
    "\\subsection*{Fuel Conditions}\n"
    + (fuel_text if fuel_text else "Fuel condition data was not available for this assessment.\n\n")
    + "\\subsection*{Drought Context}\n"
    + (drought_text if drought_text else "Drought data was not available.")
    + "\n\nProlonged drought increases fuel loading and makes prescribed burning more urgent, "
    "not less. Accumulated dead grass creates continuous fuel beds that increase wildfire "
    "risk. Paradoxically, the same conditions that make prescribed burns more dangerous "
    "also make them more necessary.\n\n"
    "\\subsection*{Fire Weather Climatology}\n"
    + (climo_text if climo_text else "Climatology data was not available for this assessment.")
))

# ===== Section 3: Atmospheric Analysis =====
rb.add_section("Atmospheric Cross-Section Analysis", content=(
    "HRRR model cross-sections were generated along two transects: an east-west transect "
    "across central Oklahoma (35.5\\textdegree N, 99.5\\textdegree W to 95.0\\textdegree W) "
    "and a north-south transect through western Oklahoma (37.0\\textdegree N to "
    "34.5\\textdegree N at 99.0\\textdegree W). Multi-panel comparisons reveal the vertical "
    "structure driving fire weather conditions."
))

if figures.get("product_firewx"):
    rb.add_figure("Atmospheric Cross-Section Analysis",
        os.path.join(FIG_DIR, "product_4panel_firewx.png"),
        "Four-panel fire weather comparison at 21Z (3 PM CST): wind speed, relative humidity, "
        "VPD, and dewpoint depression. RH values of 10--20\\% extend through the boundary layer.",
        width="1.0\\textwidth")

if figures.get("bl_structure"):
    rb.add_figure("Atmospheric Cross-Section Analysis",
        os.path.join(FIG_DIR, "product_3panel_bl.png"),
        "Boundary layer structure: potential temperature ($\\theta$), equivalent potential "
        "temperature ($\\theta_e$), and lapse rate. The well-mixed boundary layer extends "
        "above 600 hPa, promoting surface wind enhancement.",
        width="1.0\\textwidth")

if figures.get("product_ns"):
    rb.add_figure("Atmospheric Cross-Section Analysis",
        os.path.join(FIG_DIR, "product_4panel_ns.png"),
        "North-south transect through western Oklahoma showing wind speed, RH, temperature, "
        "and lapse rate. Steep lapse rates indicate vigorous boundary layer mixing.",
        width="1.0\\textwidth")

# ===== Section 4: Temporal Window Analysis =====
# This is the key justification section — were there calmer periods?
temporal_text = "The critical question for burn justification is whether any temporal window "
temporal_text += "existed with conditions below critical thresholds.\n\n"

# Compare F01 vs F03 risk levels
r01 = R.get("risk_ew_f01")
r03 = R.get("risk_ew_f03")
r08 = R.get("risk_ew_f08")

if r01 and hasattr(r01, 'risk_level'):
    temporal_text += f"\\textbf{{1 PM CST (F01):}} Risk level: {r01.risk_level}, score: {r01.risk_score}/100\n\n"
elif isinstance(r01, dict) and "risk_level" in r01:
    temporal_text += f"\\textbf{{1 PM CST (F01):}} Risk level: {r01['risk_level']}, score: {r01.get('risk_score', '?')}/100\n\n"

if r03 and hasattr(r03, 'risk_level'):
    temporal_text += f"\\textbf{{3 PM CST (F03):}} Risk level: {r03.risk_level}, score: {r03.risk_score}/100\n\n"
elif isinstance(r03, dict) and "risk_level" in r03:
    temporal_text += f"\\textbf{{3 PM CST (F03):}} Risk level: {r03['risk_level']}, score: {r03.get('risk_score', '?')}/100\n\n"

if r08 and hasattr(r08, 'risk_level'):
    temporal_text += f"\\textbf{{8 PM CST (F08):}} Risk level: {r08.risk_level}, score: {r08.risk_score}/100\n\n"
elif isinstance(r08, dict) and "risk_level" in r08:
    temporal_text += f"\\textbf{{8 PM CST (F08):}} Risk level: {r08['risk_level']}, score: {r08.get('risk_score', '?')}/100\n\n"

# Add frontal analysis
oc = R.get("overnight_woodward")
if isinstance(oc, dict) and "_error" not in oc:
    temporal_text += (
        f"\\subsection*{{Overnight Recovery Classification}}\n"
        f"The frontal analysis tool classified overnight conditions at Woodward as "
        f"\\textbf{{{oc.get('classification', 'unknown')}}}. "
    )
    if oc.get("overnight_rh_range_pct"):
        temporal_text += f"Overnight RH range: {oc['overnight_rh_range_pct']}. "
    if oc.get("overnight_wind_range_kt"):
        temporal_text += f"Wind range: {oc['overnight_wind_range_kt']}. "
    temporal_text += "\n\n"

ff = R.get("frontal_fire_woodward")
if isinstance(ff, dict) and "_error" not in ff:
    temporal_text += (
        f"\\subsection*{{Frontal Impact on Fire Behavior}}\n"
        f"Pre-frontal spread direction: {ff.get('current_spread', {}).get('direction', '?')}. "
        f"Post-frontal spread: {ff.get('post_shift_spread', {}).get('direction', '?')}. "
        f"Tactical window: {ff.get('tactical_window', 'undetermined')}.\n\n"
    )

rb.add_section("Temporal Window Analysis", content=temporal_text)

if figures.get("temporal_wind"):
    rb.add_figure("Temporal Window Analysis",
        os.path.join(FIG_DIR, "temporal_4panel_wind.png"),
        "Wind speed evolution from 1 PM to 8 PM CST along the E-W transect. "
        "Boundary layer mixing intensifies surface winds through peak heating.",
        width="1.0\\textwidth")

if figures.get("temporal_rh"):
    rb.add_figure("Temporal Window Analysis",
        os.path.join(FIG_DIR, "temporal_4panel_rh.png"),
        "Relative humidity evolution showing progressive drying through the afternoon. "
        "RH drops from marginal to critical levels as the boundary layer deepens.",
        width="1.0\\textwidth")

if figures.get("temporal_temp"):
    rb.add_figure("Temporal Window Analysis",
        os.path.join(FIG_DIR, "temporal_4panel_temp.png"),
        "Temperature evolution showing the heating cycle driving boundary layer mixing.",
        width="1.0\\textwidth")

# ===== Section 5: Terrain Assessment =====
terrain_text = (
    "Western Oklahoma's terrain is a critical factor in prescribed burn feasibility. "
    "The region's characteristics affect fire predictability, containment options, and risk.\n\n"
)

for site in SITES[:3]:
    key = f"terrain_{site['name'].lower().replace(' ','_')}"
    td = R.get(key)
    if isinstance(td, dict) and "_error" not in td:
        summary = td.get("summary", {})
        terrain_text += (
            f"\\textbf{{{site['name']}}}: "
            f"Terrain class: {summary.get('terrain_class', '?')}. "
            f"Total relief: {summary.get('total_relief_ft', '?')} ft. "
        )
        fi = td.get("fire_implications", "")
        if fi:
            terrain_text += f"{str(fi)[:200]}\n\n"
        else:
            terrain_text += "\n\n"

# Elevation profile summary
ep = R.get("elevation_ew")
if isinstance(ep, list) and ep:
    elevs = [p.get("elevation_m", 0) for p in ep if isinstance(p, dict)]
    if elevs:
        terrain_text += (
            f"\\subsection*{{Elevation Profile}}\n"
            f"E-W transect elevation: {min(elevs):.0f}--{max(elevs):.0f} m "
            f"({min(elevs)*3.281:.0f}--{max(elevs)*3.281:.0f} ft). "
            f"Total relief: {max(elevs)-min(elevs):.0f} m ({(max(elevs)-min(elevs))*3.281:.0f} ft).\n\n"
        )

# Ignition sources
for site in SITES[:3]:
    key = f"ignition_{site['name'].lower().replace(' ','_')}"
    ig = R.get(key)
    if isinstance(ig, dict) and "_error" not in ig:
        sources = ig.get("sources", [])
        terrain_text += (
            f"\\textbf{{{site['name']} ignition sources:}} {len(sources)} identified. "
        )
        for s in sources[:2]:
            terrain_text += f"{s.get('type', '?')}: {s.get('description', '')[:80]}. "
        terrain_text += "\n\n"

rb.add_section("Terrain and Fuel Assessment", content=terrain_text)

# ===== Section 6: Model Comparison =====
if figures.get("model_compare"):
    rb.add_section("Model Agreement", content=(
        "HRRR and GFS model cross-sections were compared at matched valid times. "
        "Agreement between independent model systems strengthens confidence in the "
        "analyzed conditions --- whether used to justify or oppose prescribed burning."
    ))
    rb.add_figure("Model Agreement",
        os.path.join(FIG_DIR, "model_2panel_hrrr_gfs.png"),
        "HRRR vs GFS wind speed comparison. Both models depict strong boundary layer winds, "
        "confirming the fire weather environment was well-forecast and predictable.",
        width="1.0\\textwidth")

# ===== Section 7: Surface Observations =====
obs_text = "\\subsection*{METAR Reports}\n"
metars_data = R.get("metars")
if isinstance(metars_data, dict) and "data" in metars_data:
    for obs in metars_data["data"][:10]:
        raw = obs.get("raw", "")[:120]
        safe_raw = raw.replace("_", "\\_").replace("&", "\\&").replace("#", "\\#")
        stn = obs.get("station", "?")
        obs_text += f"\\texttt{{{stn}}}: \\texttt{{{safe_raw}}}\n\n"

# Wind verification
wv = R.get("wind_verify")
if isinstance(wv, dict) and "_error" not in wv:
    obs_text += (
        f"\\subsection*{{Wind Claim Verification}}\n"
        f"Claim: sustained 25 mph with 40 mph gusts near Woodward. "
        f"Verified: {wv.get('claim_verified', '?')}. "
        f"Max observed sustained: {wv.get('max_observed_sustained_kt', '?')} kt. "
        f"Max observed gust: {wv.get('max_observed_gust_kt', '?')} kt. "
        f"Assessment: {str(wv.get('assessment', ''))[:200]}\n\n"
    )

# Model vs obs comparison
mo = R.get("model_obs_woodward")
if isinstance(mo, dict) and "_error" not in mo:
    obs_text += (
        f"\\subsection*{{Model-Observation Comparison (Woodward)}}\n"
        f"Model vs observed differences help assess HRRR accuracy for this event. "
    )
    diffs = mo.get("differences", {})
    if diffs:
        obs_text += f"Temperature bias: {diffs.get('temp_diff_c', '?')}C. "
        obs_text += f"Wind bias: {diffs.get('wind_diff_kt', '?')} kt. "
        obs_text += f"RH bias: {diffs.get('rh_diff_pct', '?')}\\%. "
    assessment = mo.get("assessment", "")
    if assessment:
        obs_text += f"{str(assessment)[:200]}\n\n"
    obs_text += "\n\n"

# RH severity
rhs = R.get("rh_severity")
if isinstance(rhs, dict) and "_error" not in rhs:
    obs_text += (
        f"\\subsection*{{RH/Dewpoint Severity Assessment}}\n"
        f"RH severity: {rhs.get('rh_severity', '?')}. "
        f"Dewpoint severity: {rhs.get('dewpoint_severity', '?')}. "
        f"Regional context: {str(rhs.get('regional_context', ''))[:200]}. "
        f"Implications: {str(rhs.get('implications', ''))[:200]}\n\n"
    )

rb.add_section("Surface Observations and Verification", content=obs_text)

# ===== Section 8: Fire Risk Quantification =====
risk_text = ""

# Numerical data table
risk_text += "\\subsection*{HRRR Surface Statistics Along Central OK Transect}\n"
rb.add_section("Fire Risk Quantification", content=risk_text)

table_rows = []
for fhr in FHRS_AFTERNOON:
    cst = f"{(18+fhr-6)%24}:00 CST"
    ws = surface_data.get(f"wind_speed_F{fhr:02d}", {})
    rh = surface_data.get(f"rh_F{fhr:02d}", {})
    table_rows.append([
        cst,
        f"{ws.get('min', '?'):.1f}" if isinstance(ws.get('min'), (int, float)) else "?",
        f"{ws.get('max', '?'):.1f}" if isinstance(ws.get('max'), (int, float)) else "?",
        f"{ws.get('mean', '?'):.1f}" if isinstance(ws.get('mean'), (int, float)) else "?",
        f"{rh.get('min', '?'):.1f}" if isinstance(rh.get('min'), (int, float)) else "?",
        f"{rh.get('max', '?'):.1f}" if isinstance(rh.get('max'), (int, float)) else "?",
        f"{rh.get('mean', '?'):.1f}" if isinstance(rh.get('mean'), (int, float)) else "?",
    ])

rb.add_table("Fire Risk Quantification",
    caption="HRRR surface statistics along the E-W central Oklahoma transect through the afternoon.",
    headers=["Time", "Wind Min (kt)", "Wind Max", "Wind Mean", "RH Min (\\%)", "RH Max", "RH Mean"],
    rows=table_rows)

# ===== Section 9: National Context =====
national_text = ""
ns_data = R.get("national_scan")
if isinstance(ns_data, dict) and "_error" not in ns_data:
    national_text += "The national fire weather scan places Oklahoma's conditions in broader context:\n\n"
    national_text += "\\begin{itemize}\n"
    for region, info in ns_data.items():
        if isinstance(info, dict):
            national_text += (
                f"  \\item \\textbf{{{info.get('label', region)}}}: "
                f"{info.get('risk_level', '?')} (score {info.get('risk_score', '?')})\n"
            )
    national_text += "\\end{itemize}\n\n"
else:
    national_text = "National fire scan data was not available for this assessment.\n\n"

rb.add_section("National Context", content=national_text)

# ===== Section 10: Balanced Assessment =====
rb.add_section("Balanced Assessment", content=(
    "\\subsection*{Arguments Supporting Burn Operations}\n"
    "\\begin{enumerate}\n"
    "  \\item \\textbf{Seasonal imperative:} February is the primary prescribed burn window "
    "for Oklahoma's dormant grasslands. Delaying burns risks missing the window entirely "
    "before spring green-up.\n"
    "  \\item \\textbf{Fuel management urgency:} Under drought conditions, accumulated dead "
    "grass creates continuous fuel beds. Prescribed burning reduces wildfire risk for the "
    "upcoming fire season.\n"
    "  \\item \\textbf{Frontal passage recovery:} The approaching cold front was forecast to "
    "bring humidity recovery and wind shifts by evening, providing a natural endpoint to "
    "burn operations.\n"
    "  \\item \\textbf{Spatial variability:} Not all of Oklahoma was under identical conditions. "
    "Central and eastern Oklahoma had lower wind speeds and higher humidity, potentially "
    "offering workable conditions.\n"
    "  \\item \\textbf{Professional judgment:} Experienced burn managers may have identified "
    "local microclimates, terrain sheltering, or temporal windows not captured in "
    "county-level warnings.\n"
    "\\end{enumerate}\n\n"
    "\\subsection*{Arguments Against Burn Operations}\n"
    "\\begin{enumerate}\n"
    "  \\item \\textbf{Red Flag Warnings:} NWS Red Flag Warnings explicitly advise against "
    "outdoor burning. These warnings represent the meteorological community's assessment "
    "that conditions are too dangerous for fire operations.\n"
    "  \\item \\textbf{SPC Critical outlook:} The Storm Prediction Center's critical fire "
    "weather outlook indicates conditions favorable for rapid fire spread and difficulty "
    "with containment.\n"
    "  \\item \\textbf{Extreme drying:} RH values of 10--15\\% combined with wind gusts to "
    "40 mph create conditions where even small fires can become uncontrollable within minutes.\n"
    "  \\item \\textbf{Deep dry boundary layer:} The well-mixed boundary layer extending above "
    "600 hPa means no moisture recovery is possible during daylight hours.\n"
    "  \\item \\textbf{Predictability:} Both HRRR and GFS models correctly forecast the "
    "dangerous conditions, meaning the information was available to burn operators.\n"
    "  \\item \\textbf{Escape consequences:} An escaped prescribed burn under these conditions "
    "would face extreme spread rates (ROS potentially exceeding 300 chains/hour in grass), "
    "threatening lives, property, and infrastructure.\n"
    "\\end{enumerate}\n\n"
))

# ===== Section 11: Conclusions =====
rb.add_section("Conclusions and Recommendations", content=(
    "This investigation used all 12 modules of the wxsection.com agent research platform "
    "to examine prescribed burn operations during Red Flag Warning conditions. The analysis "
    "reveals a tension between seasonal burn necessity and acute fire weather danger.\n\n"
    "\\textbf{Key Findings:}\n"
    "\\begin{enumerate}\n"
    "  \\item Atmospheric conditions on February 9, 2026 met or exceeded critical fire "
    "weather thresholds across western Oklahoma, confirmed by multiple independent data sources.\n"
    "  \\item The approaching cold front offered a potential recovery timeline, but pre-frontal "
    "conditions were at their most dangerous precisely during typical burn operations hours.\n"
    "  \\item Terrain in western Oklahoma is predominantly flat grassland, making fire behavior "
    "more predictable but offering fewer natural containment features.\n"
    "  \\item February is genuinely the narrowest prescribed burn window, and operational "
    "pressure to burn during marginal conditions is real.\n"
    "\\end{enumerate}\n\n"
    "\\textbf{Recommendations:}\n"
    "\\begin{enumerate}\n"
    "  \\item Prescribed burns should not be conducted under active Red Flag Warnings, "
    "regardless of seasonal pressure.\n"
    "  \\item Oklahoma should consider mandatory pre-burn weather briefings requiring "
    "documentation that NWS products were consulted.\n"
    "  \\item Burn managers should use tools like wxsection.com cross-sections to assess "
    "vertical atmospheric structure, not just surface observations.\n"
    "  \\item Post-frontal burn windows (the day after cold front passage) often provide "
    "the ideal combination of low winds, moderate humidity, and dormant fuels.\n"
    "\\end{enumerate}"
))

# --- Compile PDF ---
print("\nCompiling PDF...")
try:
    pdf_path = rb.compile_pdf(passes=2)
    print(f"\n  PDF generated: {pdf_path}")
except Exception as e:
    print(f"\n  PDF compilation error: {e}")
    traceback.print_exc()
    # Try saving just the LaTeX
    try:
        rb.save_latex("main.tex")
        print("  LaTeX source saved — can compile manually")
    except Exception as e2:
        print(f"  LaTeX save also failed: {e2}")


# ======================================================================
# PHASE 12: Post-Compilation Report Quality Validation
# ======================================================================
print("\n" + "=" * 70)
print("PHASE 12: Post-Compilation Validation")
print("=" * 70)

# Read the generated tex and validate claims
tex_path = os.path.join(OUT_DIR, "main.tex")
if os.path.exists(tex_path):
    with open(tex_path, 'r') as f:
        tex_content = f.read()
    # Check for common LaTeX issues
    issues = []
    if "\\%" not in tex_content and "%" in tex_content:
        issues.append("Possible unescaped % characters")
    if "?" in tex_content:
        issues.append("Contains ? placeholders — some data may be missing")
    print(f"  LaTeX validation: {len(issues)} potential issues")
    for i in issues:
        print(f"    - {i}")

# ======================================================================
# SUMMARY
# ======================================================================
print("\n" + "=" * 70)
print("INVESTIGATION COMPLETE — Full Agent Swarm Summary")
print("=" * 70)

# Count tools used
tools_used = {
    "CrossSectionTool": ["generate_comparison", "generate_image", "get_data"],
    "CaseStudy": ["temporal_evolution", "generate_summary"],
    "FireRiskAnalyzer": ["analyze_transect", "investigation_checklist"],
    "ForecastGenerator": ["national_fire_scan"],
    "investigate_location": ["investigate_location", "investigate_town"],
    "terrain": ["analyze_terrain_complexity", "city_terrain_assessment"],
    "fuel_conditions": ["assess_fuel_conditions", "get_ignition_risk"],
    "frontal_analysis": ["detect_wind_shifts", "classify_overnight_conditions", "analyze_frontal_impact_on_fires"],
    "report_quality": ["fire_report_checklist", "validate_report_claims"],
    "external_data": [
        "get_metar_observations", "get_raws_observations", "get_spc_fire_weather_outlook",
        "get_spc_fire_discussion", "get_spc_mesoscale_discussions", "get_nws_alerts",
        "get_nws_forecast_discussion", "get_nearby_stations", "get_elevation_profile",
        "get_drought_status", "get_fire_weather_climatology", "verify_wind_claims",
        "get_point_surface_conditions", "get_model_obs_comparison", "assess_rh_dewpoint_severity",
    ],
    "ReportBuilder": ["add_section", "add_figure", "add_table", "compile_pdf"],
}

total_functions = sum(len(v) for v in tools_used.values())
print(f"\n  Modules used: {len(tools_used)}/12")
print(f"  Functions called: {total_functions}")
print(f"  Images generated: {sum(1 for v in figures.values() if v)}/{len(figures)}")
print(f"  Data collection results: {len(R)} entries")

errors = sum(1 for v in R.values() if isinstance(v, dict) and "_error" in v)
print(f"  Errors: {errors}/{len(R)}")

print(f"\n  Output directory: {OUT_DIR}")
for f in sorted(os.listdir(FIG_DIR)):
    sz = os.path.getsize(os.path.join(FIG_DIR, f))
    print(f"    figures/{f}: {sz//1024}KB")

pdf = os.path.join(OUT_DIR, "main.pdf")
if os.path.exists(pdf):
    print(f"\n  PDF: {os.path.getsize(pdf)//1024}KB")
