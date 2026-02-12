"""
Oregon WFO Agent Swarm System — AI-Native Weather Forecasting

Pilot implementation for Oregon: 7 coverage zones, 22 agents per zone,
running every HRRR cycle (hourly) to produce personalized fire weather
forecasts for every vulnerable town.

Architecture:
    SwarmScheduler → ZoneSwarm (x7) → 22 agents per zone (5 tiers)

    Tier 1: Data Acquisition (5 agents)  — METAR, RAWS, NWS, SPC, Model
    Tier 2: Cross-Section (6 agents)     — XS images, GIFs, model comparison
    Tier 3: Assessment (5 agents)        — Fire risk, fuel, terrain, wind, validation
    Tier 4: Synthesis (4 agents)         — Town forecasts, zone discussion, ranking
    Tier 5: Output (2 agents)            — Bulletin JSON, PDF report

Usage:
    from tools.agent_tools.wfo_swarm import SwarmScheduler, ZoneSwarm
    from tools.agent_tools.wfo_swarm.config import SwarmConfig, OREGON_ZONES

    # Run single zone
    swarm = ZoneSwarm("OR-CENTCAS")
    bulletin = await swarm.run_cycle("20260211_12z")

    # Run all zones
    scheduler = SwarmScheduler()
    scheduler.start()
"""
