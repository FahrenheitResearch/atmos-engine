r"""
Assemble final PDF from 5 agent intel files + figures.
Run: cd C:/Users/drew/hrrr-maps && python research/ok_prescribed_burn_20260209/build_pdf.py
"""
import sys, os, glob
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from tools.agent_tools.report_builder import ReportBuilder, ReportConfig

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(OUT_DIR, "figures")
os.chdir(OUT_DIR)


def fig(name):
    p = os.path.join(FIG_DIR, name)
    return p if os.path.exists(p) else None


def load(fname):
    p = os.path.join(OUT_DIR, fname)
    if os.path.exists(p):
        with open(p, encoding='utf-8', errors='replace') as f:
            return f.read()
    return ""


def esc(text):
    return (text.replace('\\', '\\textbackslash{}')
                .replace('_', r'\_').replace('&', r'\&')
                .replace('%', r'\%').replace('#', r'\#')
                .replace('$', r'\$').replace('{', r'\{')
                .replace('}', r'\}').replace('~', r'\textasciitilde{}')
                .replace('^', r'\textasciicircum{}'))


# Load intel files
intel_atmos = load("intel_atmospheric.md")
intel_frontal = load("intel_frontal.md")
intel_terrain = load("intel_terrain_fuel.md")
intel_obs = load("intel_observations.md")
intel_risk = load("intel_risk_context.md")

print(f"Intel files loaded: atmos={len(intel_atmos)}c, frontal={len(intel_frontal)}c, "
      f"terrain={len(intel_terrain)}c, obs={len(intel_obs)}c, risk={len(intel_risk)}c")

# ======================================================================
# Report Configuration
# ======================================================================
config = ReportConfig(
    title="Oklahoma Prescribed Burns During Red Flag Conditions: A Multi-Agent Investigation",
    author="5-Agent AI Research Swarm (wxsection.com)",
    date="February 9--10, 2026",
    report_type="bulletin",
    institution="wxsection.com Atmospheric Research Platform",
)

rb = ReportBuilder(config, output_dir=OUT_DIR)

# ======================================================================
# Abstract
# ======================================================================
rb.set_abstract(
    "On February 9, 2026, prescribed burn activity was reported across portions of western "
    "Oklahoma while Red Flag Warnings were in effect for Harper, Ellis, Woodward, and Roger "
    "Mills counties. This investigation deployed five autonomous AI research agents --- each "
    "using a distinct analytical domain from the wxsection.com platform --- to determine "
    "whether a data-driven justification exists for conducting prescribed burns on this day. "
    "The agents analyzed HRRR cross-sections (22 multi-panel images), frontal passage timing "
    "and overnight recovery, terrain complexity and fuel conditions, 625 METAR observations "
    "with model verification, and national fire risk context including SPC/NWS products. "
    "All five agents independently concluded that conditions on February 9 did not support "
    "prescribed burning, though the terrain and seasonal context make western Oklahoma "
    "appropriate for prescribed burns under normal February conditions."
)

# ======================================================================
# Section 1: Synoptic Overview
# ======================================================================
rb.add_section("Synoptic Overview", content=(
    "A strong cold front advanced across the southern High Plains during the afternoon "
    "of February 9, 2026. Ahead of the front, west-southwesterly winds of 20--25 mph "
    "(gusting to 40 mph) combined with relative humidity values of 10--15\\% to produce "
    "critical fire weather conditions across the Oklahoma and Texas Panhandles.\n\n"
    "The SPC Day 1 Fire Weather Outlook designated \\textbf{CRITICAL} fire weather for "
    "NE New Mexico into the OK/TX Panhandles and \\textbf{ELEVATED} conditions across the "
    "broader western Oklahoma corridor. The NWS Norman office issued Red Flag Warnings for "
    "Harper, Ellis, Woodward, and Roger Mills counties through 7 PM CST. "
    "NWS forecaster Ungar explicitly stated: ``burning is discouraged in and near the "
    "warning area.''\n\n"
    "This investigation asks: despite these warnings, could prescribed burn operators have "
    "identified a defensible window based on temporal trends, frontal recovery, terrain "
    "advantages, or seasonal necessity?"
))

# ======================================================================
# Section 2: The Case for Prescribed Burns
# ======================================================================
rb.add_section("The Case for Prescribed Burns", content=(
    "Before examining the atmospheric data, it is essential to understand the operational "
    "constraints facing prescribed burn managers in the southern Great Plains.\n\n"
    "\\subsection*{Seasonal Imperative}\n"
    "February is the primary prescribed burn window for Oklahoma's grasslands. Native "
    "tallgrass and mixed-grass prairies must be burned during dormancy (December--March) "
    "before spring green-up renders burns ineffective. December and January often have "
    "snow cover or frozen ground; March can see early green-up in southern Oklahoma. "
    "February is frequently the only viable month.\n\n"
    "\\subsection*{Terrain Suitability}\n"
    "All three investigation sites (Woodward, Gage, Elk City) were classified as "
    "\\textbf{Rolling Hills} terrain with no canyon features, no steep segments, and "
    "maximum slopes under 5\\textdegree. Average slopes were under 1\\textdegree. "
    "This is textbook prescribed burn terrain --- flat, predictable, accessible to "
    "mechanized suppression equipment. The E-W transect showed only 0.10\\% average grade "
    "over 253 miles.\n\n"
    "\\subsection*{Fuel Management Urgency}\n"
    "Fuel assessments revealed \\textbf{critically low fuel moisture} (2--8\\%) across all "
    "sites, with zero precipitation for 8+ days at Gage. Paradoxically, the same drought "
    "conditions that make burns more dangerous also make them more necessary --- accumulated "
    "dead grass creates continuous fuel beds that increase wildfire risk. Prescribed burning "
    "is the primary tool for reducing this accumulated fuel load.\n\n"
    "\\subsection*{National Context}\n"
    "Western Oklahoma ranked \\textbf{7th of 8 regions} in the national fire weather scan "
    "(score 38/100, MODERATE). NE New Mexico was the worst area nationally (score 70, "
    "ELEVATED, RH as low as 6.4\\%). The OK/TX Panhandles scored 52--56. Oklahoma's burn "
    "area was on the lower end of the fire weather spectrum --- still under Red Flag "
    "conditions, but not the worst location in the country."
))

# ======================================================================
# Section 3: Atmospheric Analysis
# ======================================================================
rb.add_section("Atmospheric Cross-Section Analysis", content=(
    "The Atmospheric Agent generated 22 multi-panel cross-section images and extracted "
    "surface statistics at 135 points (E-W) and 92 points (N-S) per forecast hour. "
    "Two transects were analyzed: an E-W transect across central Oklahoma (35.5\\textdegree N, "
    "99.5\\textdegree W to 95.0\\textdegree W) and a N-S transect through the Red Flag Warning "
    "zone (37.0\\textdegree N to 34.5\\textdegree N at 99.0\\textdegree W).\n\n"
    "\\subsection*{Relative Humidity}\n"
    "RH bottomed at \\textbf{12.9\\%} on the E-W transect at 3 PM CST and \\textbf{13.0\\%} "
    "on the N-S transect at 5 PM. Mean RH across the entire RFW zone dropped to 16.6\\% by "
    "5 PM. At no point during the 1--6 PM window did any location along the western OK "
    "transect exceed 30\\% RH after 2 PM.\n\n"
    "\\subsection*{Dewpoint Depression}\n"
    "Dewpoint depressions of \\textbf{24--31\\textdegree C} confirmed extremely dry air through "
    "the full atmospheric column --- not a surface artifact but a deep, well-mixed boundary "
    "layer phenomenon extending to $\\sim$700 hPa ($\\sim$3 km AGL).\n\n"
    "\\subsection*{Temperature}\n"
    "Surface temperatures peaked at \\textbf{78.6\\textdegree F (25.9\\textdegree C)} on the "
    "N-S transect --- 15--20\\textdegree F above normal for early February. Combined with "
    "low RH, this produced extreme vapor pressure deficit (VPD) of 5.0+ kPa.\n\n"
    "\\subsection*{Boundary Layer Structure}\n"
    "Potential temperature cross-sections revealed a deep, well-mixed boundary layer "
    "extending from the surface to $\\sim$700 hPa by 3 PM. Steep (near-superadiabatic) "
    "lapse rates efficiently transported momentum from aloft to the surface and maintained "
    "extreme dryness through the full BL depth."
))

# Add key atmospheric figures
for fname, cap in [
    ("ew_temporal_rh.png",
     "E-W transect: RH evolution from 1 PM to 8 PM CST (FHR 1/3/5/8). "
     "RH collapses to 12.9% minimum at 3 PM with partial recovery after 7 PM."),
    ("ns_temporal_rh.png",
     "N-S transect through Red Flag Warning zone: RH evolution. Mean RH drops to 16.6% "
     "by 5 PM -- the entire western OK corridor was below critical thresholds."),
    ("ew_temporal_wind_speed.png",
     "E-W transect: wind speed evolution showing sustained boundary layer winds "
     "through the afternoon heating cycle."),
    ("ew_products_fhr3.png",
     "Three-panel comparison at 3 PM CST (peak conditions): wind speed, RH, and VPD "
     "along the E-W transect. Note co-location of strong winds and extreme dryness."),
    ("ew_temporal_dewpoint_dep.png",
     "E-W dewpoint depression evolution. Values of 24-31 deg C confirm extreme "
     "dryness through the full atmospheric column, not just at the surface."),
    ("ew_temporal_theta.png",
     "Potential temperature (theta) evolution showing the deep, well-mixed boundary "
     "layer extending to approximately 700 hPa. This mixing transports dry, windy air to the surface."),
]:
    if fig(fname):
        rb.add_figure("Atmospheric Cross-Section Analysis",
            os.path.join(FIG_DIR, fname), cap, width="1.0\\textwidth")

# ======================================================================
# Section 4: Temporal Window Analysis (Frontal Agent)
# ======================================================================
rb.add_section("Temporal Window Analysis", content=(
    "The Frontal \\& Temporal Agent investigated whether the approaching cold front could "
    "have provided a justifiable burn window --- the strongest potential argument for "
    "prescribed burning on this day.\n\n"
    "\\subsection*{Cold Front Timing}\n"
    "The cold front passed Woodward/Gage at approximately \\textbf{5:00 AM CST on February 10} "
    "(FHR 17) --- a full \\textbf{16--18 hours} after any plausible morning burn ignition on "
    "February 9. This eliminates any argument that ``the front would bring relief by evening.''\n\n"
    "\\subsection*{Post-Frontal Conditions}\n"
    "Critically, the front did NOT suppress fire weather. Post-frontal conditions:\n"
    "\\begin{itemize}\n"
    "  \\item \\textbf{Woodward:} Wind reversal WSW$\\rightarrow$N (97\\textdegree\\ shift), "
    "sustained \\textbf{30.7 kt}, gusts \\textbf{43 kt}. RH rose to only 33\\%.\n"
    "  \\item \\textbf{Gage:} Two-phase shift, sustained \\textbf{32.8 kt}, gusts "
    "\\textbf{46 kt}. RH rose to 38\\%.\n"
    "  \\item \\textbf{Elk City:} Sustained \\textbf{31.0 kt}, gusts \\textbf{43 kt}. "
    "RH \\textbf{dropped to 16\\%} at frontal passage --- zero humidity relief.\n"
    "\\end{itemize}\n\n"
    "\\subsection*{Overnight Recovery Classification}\n"
    "\\begin{itemize}\n"
    "  \\item \\textbf{Woodward:} \\texttt{frontal\\_shift} --- NOT recovery. Winds 16--31 kt "
    "overnight. All firelines change direction.\n"
    "  \\item \\textbf{Gage:} \\texttt{partial\\_recovery} --- RH improved to 53\\% but winds "
    "remained 15+ kt. Fires moderate but don't go out.\n"
    "  \\item \\textbf{Elk City:} \\texttt{no\\_recovery} --- Winds 30--34 kt, RH 16--24\\% "
    "all night. Fires continue to run.\n"
    "\\end{itemize}\n\n"
    "\\subsection*{The ``Morning Burn'' Argument}\n"
    "Could burns have been safely conducted in the morning before peak heating? The HRRR data "
    "shows conditions were already deteriorating by noon CST (model initialization). At 1 PM "
    "(F01), RH was 22--30\\% across western OK --- already below the 25--30\\% threshold used "
    "by most prescribed burn guidelines. Any fire ignited in the morning would still be active "
    "during the 3--5 PM peak. The \\textbf{17 consecutive hours} of critically low humidity "
    "(noon Feb 9 through 5 AM Feb 10) left no safe temporal window."
))

# ======================================================================
# Section 5: Terrain & Fuel Assessment
# ======================================================================
rb.add_section("Terrain and Fuel Assessment", content=(
    "\\subsection*{Terrain Complexity}\n"
    "All three sites were classified as \\textbf{Rolling Hills} with no canyons, no steep "
    "segments, and maximum slopes of 3--5\\textdegree:\n\n"
    "\\begin{tabular}{lrrrl}\n"
    "\\hline\n"
    "\\textbf{Site} & \\textbf{Elevation (ft)} & \\textbf{Relief (ft)} & "
    "\\textbf{Max Slope} & \\textbf{Canyons} \\\\\n"
    "\\hline\n"
    "Woodward & 1,942 & 502 & 3.6\\textdegree & None \\\\\n"
    "Gage & 2,172 & 390 & 3.2\\textdegree & None \\\\\n"
    "Elk City & 1,929 & 512 & 5.0\\textdegree & None \\\\\n"
    "\\hline\n"
    "\\end{tabular}\n\n"
    "Fire behavior is entirely wind-dominated with no topographic acceleration effects. "
    "However, the flat terrain also means \\textbf{no natural firebreaks} --- no rivers, "
    "canyons, or ridgelines to stop an escaped burn.\n\n"
    "\\subsection*{Fuel Conditions}\n"
    "\\begin{tabular}{lrrl}\n"
    "\\hline\n"
    "\\textbf{Site} & \\textbf{Fuel Moisture} & \\textbf{7-Day Precip} & "
    "\\textbf{Min RH (Feb 9)} \\\\\n"
    "\\hline\n"
    "Woodward & 5--8\\% (Very Low) & 0.02 in (trace) & 22.6\\% \\\\\n"
    "Gage & 2--5\\% (Critical) & 0.00 in (zero) & 10.2\\% \\\\\n"
    "Elk City & 2--5\\% (Critical) & 0.00 in (zero) & 16.0\\% \\\\\n"
    "\\hline\n"
    "\\end{tabular}\n\n"
    "Fuel moisture was \\textbf{well below the 8\\% threshold for extreme fire behavior}. "
    "At 2--5\\%, flame lengths in cured grass could exceed 10 feet with rate of spread "
    "exceeding 300 chains/hour (3.4 mph) under the observed winds.\n\n"
    "\\subsection*{The Central Paradox}\n"
    "The terrain supports prescribed burning as a general management practice --- flat, "
    "predictable, accessible. But the conditions on February 9 were the \\textit{most "
    "dangerous possible} within an otherwise valid burn season. The terrain's lack of "
    "natural firebreaks means containment failure is catastrophic rather than merely "
    "problematic."
))

# ======================================================================
# Section 6: Surface Observations
# ======================================================================
rb.add_section("Surface Observations and Verification", content=(
    "The Observations Agent parsed \\textbf{625 METAR observations} across 7 Oklahoma stations "
    "and verified wind claims, model accuracy, and fire weather climatology.\n\n"
    "\\subsection*{Peak Observed Conditions}\n"
    "\\begin{itemize}\n"
    "  \\item \\textbf{KGAG (Gage):} Peak gust \\textbf{37 kt (43 mph)} at 15:58 CST. "
    "Sustained \\textbf{27 kt (31 mph)} at 14:20 CST. RFW criteria met for "
    "\\textbf{3 continuous hours} (14:20--17:20 CST) with 24 individual METAR observations "
    "meeting the threshold.\n"
    "  \\item \\textbf{KWDG (Woodward):} Sustained 13 kt. Moderate but under RFW.\n"
    "  \\item \\textbf{KOKC (OKC):} 21\\% RH, 20 mph winds --- marginal, well below criteria.\n"
    "  \\item \\textbf{KTUL (Tulsa):} 24\\% RH, 16 mph --- below criteria.\n"
    "\\end{itemize}\n\n"
    "\\subsection*{Model Verification}\n"
    "HRRR 18Z F03 was \\textbf{remarkably accurate} at 21Z validation: temperature within "
    "1\\textdegree F, winds within 1 kt, RH within 2\\%. The event was NOT overforecast --- "
    "actual conditions matched model predictions.\n\n"
    "\\subsection*{Spatial Gradient}\n"
    "A sharp west-to-east gradient existed: KGAG had 10.2\\% RH and 43 mph gusts while OKC "
    "had 21\\% RH and 20 mph winds. The worst conditions were focused precisely on the "
    "Gage-Woodward corridor where burns were conducted.\n\n"
    "\\subsection*{Fire Weather Climatology}\n"
    "February climatology for KGAG shows the observed conditions were a ``once-or-twice "
    "per year'' event. KOKC's observed 80.6\\textdegree F was \\textbf{27.6\\textdegree F "
    "above the February normal} of 53\\textdegree F."
))

# ======================================================================
# Section 7: Fire Risk Quantification
# ======================================================================
rb.add_section("Fire Risk Quantification", content=(
    "The Risk Agent ran quantitative fire risk analysis along both transects at four "
    "forecast hours.\n\n"
    "\\subsection*{Risk Score Evolution (E-W Transect)}\n"
    "\\begin{tabular}{llrrl}\n"
    "\\hline\n"
    "\\textbf{FHR} & \\textbf{Time} & \\textbf{Score} & \\textbf{Level} & "
    "\\textbf{RH Min} \\\\\n"
    "\\hline\n"
    "F01 & 1 PM & 14 & LOW & 21.7\\% \\\\\n"
    "F03 & 3 PM & \\textbf{40} & \\textbf{MODERATE} & \\textbf{12.9\\%} \\\\\n"
    "F05 & 5 PM & 17 & LOW & 17.0\\% \\\\\n"
    "F08 & 8 PM & 13 & LOW & 16.7\\% \\\\\n"
    "\\hline\n"
    "\\end{tabular}\n\n"
    "Risk peaked sharply at 3 PM (score 40, MODERATE) then declined. At 1 PM, the "
    "transect-averaged score was only 14 (LOW). \\textbf{Important caveat:} these scores "
    "use column-averaged cross-section wind data, which dilutes surface wind speeds. "
    "NWS-reported surface gusts of 35--43 mph are not fully captured. The actual surface "
    "fire risk was likely \\textbf{higher than these scores indicate}.\n\n"
    "\\subsection*{NWS Products}\n"
    "\\begin{itemize}\n"
    "  \\item SPC designated \\textbf{CRITICAL} fire weather for NE NM into the OK/TX Panhandles\n"
    "  \\item \\textbf{15 active NWS alerts} for Oklahoma including multiple Red Flag Warnings\n"
    "  \\item NWS Norman explicitly stated: ``\\textit{Outdoor burning is not recommended}''\n"
    "  \\item NWS Norman forecaster: ``\\textit{burning is discouraged in and near the warning area}''\n"
    "  \\item SPC Day 2 outlook: ``NO CRITICAL AREAS'' --- confirming this was a single-day event\n"
    "\\end{itemize}"
))

# ======================================================================
# Section 8: Balanced Assessment
# ======================================================================
rb.add_section("Balanced Assessment", content=(
    "\\subsection*{Arguments Supporting Burn Operations}\n"
    "\\begin{enumerate}\n"
    "  \\item \\textbf{Seasonal imperative:} February is genuinely the narrowest prescribed burn "
    "window for Oklahoma's dormant grasslands. Missing it risks no burns until next year.\n"
    "  \\item \\textbf{Terrain suitability:} Western OK's flat terrain (max slope 5\\textdegree, "
    "no canyons) is ideal prescribed burn landscape under normal conditions.\n"
    "  \\item \\textbf{Fuel management urgency:} Critically low fuel moisture (2--8\\%) and "
    "zero recent precipitation indicate dangerous fuel accumulation. Prescribed burning "
    "reduces wildfire risk for the upcoming fire season.\n"
    "  \\item \\textbf{Not the worst nationally:} Oklahoma ranked 7th of 8 regions in the "
    "national fire scan. NE New Mexico, the TX/OK Panhandles, and SE Wyoming all had "
    "worse conditions.\n"
    "  \\item \\textbf{Morning conditions less severe:} At 1 PM, risk scores were LOW (14/100) "
    "and RH was still 22--30\\%. Earlier morning hours would have been more favorable.\n"
    "\\end{enumerate}\n\n"
    "\\subsection*{Arguments Against Burn Operations}\n"
    "\\begin{enumerate}\n"
    "  \\item \\textbf{Red Flag Warnings active:} NWS explicitly recommended against outdoor "
    "burning. These warnings represent the meteorological community's consensus assessment.\n"
    "  \\item \\textbf{No safe temporal window:} RH was below 25\\% across western OK by 1 PM "
    "and below 15\\% by 3 PM. Any morning burn would still be active during peak conditions. "
    "17 consecutive hours of critically low humidity left no window.\n"
    "  \\item \\textbf{Front brings no relief:} The cold front arrived 16--18 hours after any "
    "morning ignition and brought \\textit{increased} winds (30--46 kt gusts) with a violent "
    "wind reversal. At Elk City, RH actually \\textit{dropped} at frontal passage.\n"
    "  \\item \\textbf{No natural firebreaks:} Zero canyons, rivers, or ridgelines to stop "
    "an escaped burn. Miles of continuous dormant grass in every direction.\n"
    "  \\item \\textbf{Model was accurate:} HRRR verification within 1\\textdegree F / 1 kt / 2\\% "
    "RH. The dangerous conditions were well-forecast and predictable.\n"
    "  \\item \\textbf{Escape consequences catastrophic:} With 2--5\\% fuel moisture and 43 mph "
    "gusts, an escaped burn would face rate of spread exceeding 300 chains/hour.\n"
    "\\end{enumerate}"
))

# ======================================================================
# Section 9: Conclusions
# ======================================================================
rb.add_section("Conclusions and Recommendations", content=(
    "Five autonomous AI research agents independently analyzed this event using 12 analytical "
    "modules, 40+ tool functions, 22 cross-section images, 625 surface observations, "
    "and national context data. \\textbf{All five agents concluded that prescribed burns "
    "were not justifiable on February 9, 2026.}\n\n"
    "\\textbf{Key Findings:}\n"
    "\\begin{enumerate}\n"
    "  \\item Atmospheric conditions met or exceeded critical fire weather thresholds across "
    "western Oklahoma for 17 consecutive hours, confirmed by HRRR model, GFS model, METARs, "
    "SPC outlooks, and NWS warnings.\n"
    "  \\item The approaching cold front --- the strongest potential justification for ``burn "
    "now, recovery later'' --- provided no meaningful relief. Post-frontal winds actually "
    "\\textit{increased} to 30--46 kt with a dangerous direction reversal.\n"
    "  \\item While terrain and seasonal context genuinely support prescribed burning in western "
    "Oklahoma during the January--March window, the specific conditions on February 9 were "
    "the most dangerous possible within that window.\n"
    "  \\item Oklahoma ranked 7th of 8 nationally --- not the worst, but still firmly within "
    "Red Flag Warning criteria with explicit NWS guidance against burning.\n"
    "\\end{enumerate}\n\n"
    "\\textbf{Recommendations:}\n"
    "\\begin{enumerate}\n"
    "  \\item Prescribed burns should not be conducted under active Red Flag Warnings, "
    "regardless of seasonal pressure.\n"
    "  \\item Oklahoma should require mandatory pre-burn weather briefings with documented "
    "NWS product review.\n"
    "  \\item Post-frontal windows (February 10 had ``NO CRITICAL AREAS'' per SPC) often "
    "provide the ideal burn conditions that February 9 lacked.\n"
    "  \\item Burn managers should evaluate frontal recovery quality, not just timing --- "
    "a front that maintains 30+ kt winds is not ``recovery.''\n"
    "  \\item Tools like wxsection.com cross-sections can help burn managers assess vertical "
    "atmospheric structure (boundary layer depth, momentum transport) beyond surface obs.\n"
    "\\end{enumerate}\n\n"
    "\\vspace{1em}\n"
    "\\begin{center}\n"
    "\\small\\textit{Generated by 5 parallel AI agents using all 12 wxsection.com analytical "
    "modules. Total agent compute: 270K tokens across 122 tool invocations.}\n"
    "\\end{center}"
))

# Add N-S figures to Terrain section
for fname, cap in [
    ("ns_products_fhr3.png",
     "N-S transect through Red Flag Warning zone at 3 PM CST: wind speed, RH, and VPD. "
     "The entire transect is below 30% RH with minimum 13.8%."),
    ("ns_temporal_wind_speed.png",
     "N-S transect wind speed temporal evolution showing increasing boundary layer winds "
     "through peak afternoon heating in the Red Flag Warning counties."),
]:
    if fig(fname):
        rb.add_figure("Terrain and Fuel Assessment",
            os.path.join(FIG_DIR, fname), cap, width="1.0\\textwidth")

# ======================================================================
# Compile
# ======================================================================
print("\nCompiling PDF...")
try:
    pdf_path = rb.compile_pdf(passes=2)
    print(f"\nPDF generated: {pdf_path}")
    print(f"Size: {os.path.getsize(pdf_path) // 1024} KB")
except Exception as e:
    print(f"\nPDF compilation error: {e}")
    import traceback; traceback.print_exc()
    try:
        rb.save_latex("main.tex")
        print("LaTeX source saved — compile manually with pdflatex")
    except Exception as e2:
        print(f"LaTeX save failed: {e2}")
