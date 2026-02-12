"""
wxsection.com Agent Research Toolkit

AI-agent-native atmospheric research platform. Tools for conducting
atmospheric research, case studies, fire weather forecasting, report
generation, and ground-truth analysis.

All tools connect to the wxsection.com dashboard API (localhost:5565)
and are also exposed via MCP server (tools/mcp_server.py).

Modules:
    cross_section    - Generate and analyze HRRR/GFS/RRFS/NAM/RAP/NAM-Nest cross-sections
    external_data    - METAR, RAWS, SPC, NWS, elevation, drought, Street View
    fire_risk        - Fire weather risk assessment, indices, threshold analysis
    fuel_conditions  - Fuel condition assessment, seasonal context, ignition sources
    terrain          - Topographic complexity analysis, canyon/valley detection
    case_study       - Historical event case study framework
    report_builder   - LaTeX report generation and PDF compilation
    forecast         - Forecast generator and agent swarm orchestrator
    frontal_analysis - Wind shift / frontal passage detection for fire weather

Quick Start:
    from tools.agent_tools.cross_section import CrossSectionTool
    from tools.agent_tools.fire_risk import FireRiskAnalyzer
    from tools.agent_tools.fuel_conditions import assess_fuel_conditions, get_ignition_risk
    from tools.agent_tools.terrain import analyze_terrain_complexity, city_terrain_assessment
    from tools.agent_tools.case_study import CaseStudy
    from tools.agent_tools.report_builder import ReportBuilder
    from tools.agent_tools.forecast import ForecastGenerator, ForecastConfig
    from tools.agent_tools.frontal_analysis import (
        detect_wind_shifts,
        analyze_frontal_impact_on_fires,
        classify_overnight_conditions,
    )
"""
