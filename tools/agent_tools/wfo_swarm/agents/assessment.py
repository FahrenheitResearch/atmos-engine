"""
Tier 3: Assessment Agents (5 agents)

These agents analyze the data gathered in Tiers 1-2 to produce structured
risk assessments. They run in parallel, each writing to different ZoneState
fields.

Agents:
    12. FireRiskAssessor    — fire risk assessment along each transect
    13. FuelAnalyst         — fuel conditions and ignition sources per town
    14. TerrainAnalyst      — terrain complexity assessment per town
    15. WindShiftDetector   — wind shift detection along transects
    16. ObsModelValidator   — compare model output against METAR observations
"""
import logging
import time
import traceback

from tools.agent_tools.wfo_swarm.zone_state import ZoneState
from tools.agent_tools.wfo_swarm.config import AgentResult

logger = logging.getLogger(__name__)


# =============================================================================
# Agent 12: Fire Risk Assessor
# =============================================================================

class FireRiskAssessor:
    """Runs fire risk assessment along each zone transect."""

    TIER = 3
    NAME = "fire_risk_assessor"

    def run(self, state: ZoneState, zone_config, swarm_config) -> AgentResult:
        t0 = time.time()
        errors = []
        data = {"transects_assessed": 0}

        try:
            from tools.agent_tools.fire_risk import FireRiskAnalyzer
            from tools.agent_tools.data.oregon_transects import get_transect

            analyzer = FireRiskAnalyzer(base_url=swarm_config.api_base)

            # Assess each transect at key forecast hours
            assess_fhrs = [0, 6, 12, 18, 24]
            assess_fhrs = [f for f in assess_fhrs if f in swarm_config.fhrs]

            for tid in zone_config.transect_ids:
                try:
                    transect = get_transect(tid)
                    start = tuple(transect["start"])
                    end = tuple(transect["end"])

                    tid_results = {}
                    for fhr in assess_fhrs:
                        try:
                            result = analyzer.analyze_transect(
                                start=start, end=end,
                                cycle=state.cycle, fhr=fhr,
                                label=transect["label"],
                            )
                            if result:
                                tid_results[f"F{fhr:02d}"] = {
                                    "score": result.score if hasattr(result, "score") else 0,
                                    "level": result.level if hasattr(result, "level") else "UNKNOWN",
                                    "summary": result.summary if hasattr(result, "summary") else "",
                                    "data_quality_warnings": (
                                        result.data_quality_warnings
                                        if hasattr(result, "data_quality_warnings") else []
                                    ),
                                    "investigation_flags": (
                                        result.investigation_flags
                                        if hasattr(result, "investigation_flags") else []
                                    ),
                                }
                        except Exception as e:
                            tid_results[f"F{fhr:02d}"] = {"error": str(e)}

                    state.fire_risk[tid] = tid_results
                    data["transects_assessed"] += 1

                except Exception as e:
                    errors.append(f"Fire risk {tid}: {e}")

        except Exception as e:
            errors.append(f"FireRiskAssessor: {traceback.format_exc()}")

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=data["transects_assessed"] > 0,
            data=data,
            errors=errors,
            elapsed_seconds=elapsed,
        )


# =============================================================================
# Agent 13: Fuel Analyst
# =============================================================================

class FuelAnalyst:
    """Assesses fuel conditions and ignition risk per town."""

    TIER = 3
    NAME = "fuel_analyst"

    def run(self, state: ZoneState, zone_config, swarm_config) -> AgentResult:
        t0 = time.time()
        errors = []
        data = {"towns_assessed": 0}

        try:
            from tools.agent_tools.fuel_conditions import (
                assess_fuel_conditions,
                get_ignition_risk,
            )

            for town_name, (lat, lon) in zone_config.towns.items():
                try:
                    # Fuel conditions assessment
                    fuel = assess_fuel_conditions(lat, lon, base_url=swarm_config.api_base)
                    ignition = get_ignition_risk(lat, lon, city_name=town_name)

                    state.fuel_conditions[town_name] = {
                        "fuel_assessment": fuel if isinstance(fuel, dict) else {"raw": str(fuel)},
                        "ignition_risk": ignition if isinstance(ignition, dict) else {"raw": str(ignition)},
                    }
                    data["towns_assessed"] += 1

                except Exception as e:
                    errors.append(f"Fuel {town_name}: {e}")
                    state.fuel_conditions[town_name] = {"error": str(e)}

        except Exception as e:
            errors.append(f"FuelAnalyst: {traceback.format_exc()}")

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=data["towns_assessed"] > 0,
            data=data,
            errors=errors,
            elapsed_seconds=elapsed,
        )


# =============================================================================
# Agent 14: Terrain Analyst
# =============================================================================

class TerrainAnalyst:
    """Assesses terrain complexity for each zone town."""

    TIER = 3
    NAME = "terrain_analyst"

    def run(self, state: ZoneState, zone_config, swarm_config) -> AgentResult:
        t0 = time.time()
        errors = []
        data = {"towns_assessed": 0}

        try:
            from tools.agent_tools.terrain import city_terrain_assessment

            for town_name, (lat, lon) in zone_config.towns.items():
                try:
                    # Try to get pre-computed terrain profile
                    assessment = city_terrain_assessment(lat, lon, town_name)
                    if assessment:
                        state.terrain_assessments[town_name] = (
                            assessment if isinstance(assessment, dict)
                            else {"raw": str(assessment)}
                        )
                        data["towns_assessed"] += 1
                    else:
                        state.terrain_assessments[town_name] = {
                            "status": "no_profile",
                            "note": f"No terrain profile found for {town_name}, OR",
                        }

                except Exception as e:
                    errors.append(f"Terrain {town_name}: {e}")
                    state.terrain_assessments[town_name] = {"error": str(e)}

        except Exception as e:
            errors.append(f"TerrainAnalyst: {traceback.format_exc()}")

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=True,  # terrain data is supplementary
            data=data,
            errors=errors,
            elapsed_seconds=elapsed,
        )


# =============================================================================
# Agent 15: Wind Shift Detector
# =============================================================================

class WindShiftDetector:
    """Detects wind direction shifts along zone transects."""

    TIER = 3
    NAME = "wind_shift_detector"

    def run(self, state: ZoneState, zone_config, swarm_config) -> AgentResult:
        t0 = time.time()
        errors = []
        data = {"transects_analyzed": 0, "shifts_detected": 0}

        try:
            from tools.agent_tools.frontal_analysis import detect_wind_shifts
            from tools.agent_tools.data.oregon_transects import get_transect

            for tid in zone_config.priority_transects:
                try:
                    transect = get_transect(tid)
                    # Use midpoint of transect for wind shift detection
                    mid_lat = (transect["start"][0] + transect["end"][0]) / 2
                    mid_lon = (transect["start"][1] + transect["end"][1]) / 2

                    result = detect_wind_shifts(mid_lat, mid_lon, cycle=state.cycle, base_url=swarm_config.api_base)
                    if result:
                        state.wind_shifts[tid] = (
                            result if isinstance(result, dict)
                            else {"raw": str(result)}
                        )
                        data["transects_analyzed"] += 1
                        if isinstance(result, dict) and result.get("shifts"):
                            data["shifts_detected"] += len(result["shifts"])

                except Exception as e:
                    errors.append(f"Wind shift {tid}: {e}")

        except Exception as e:
            errors.append(f"WindShiftDetector: {traceback.format_exc()}")

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=True,  # wind shifts are optional
            data=data,
            errors=errors,
            elapsed_seconds=elapsed,
        )


# =============================================================================
# Agent 16: Obs-Model Validator
# =============================================================================

class ObsModelValidator:
    """Compares model forecast against actual METAR observations."""

    TIER = 3
    NAME = "obs_model_validator"

    def run(self, state: ZoneState, zone_config, swarm_config) -> AgentResult:
        t0 = time.time()
        errors = []
        data = {"stations_validated": 0}

        try:
            # Compare most recent METAR obs against model F00/F01
            for station_id, obs in state.metar_obs.items():
                try:
                    obs_wind = obs.get("sknt")
                    obs_temp = obs.get("tmpf")
                    obs_rh = obs.get("relh")
                    obs_dir = obs.get("drct")

                    if obs_wind is None and obs_temp is None:
                        continue

                    validation = {
                        "station": station_id,
                        "obs_wind_kt": obs_wind,
                        "obs_temp_f": obs_temp,
                        "obs_rh_pct": obs_rh,
                        "obs_wind_dir": obs_dir,
                        "obs_time": obs.get("valid"),
                    }

                    # Find nearest town's model data for comparison
                    best_town = None
                    best_dist = float("inf")
                    obs_lat = obs.get("lat")
                    obs_lon = obs.get("lon")

                    if obs_lat and obs_lon:
                        for town_name, (tlat, tlon) in zone_config.towns.items():
                            dist = ((obs_lat - tlat) ** 2 + (obs_lon - tlon) ** 2) ** 0.5
                            if dist < best_dist:
                                best_dist = dist
                                best_town = town_name

                    if best_town and best_town in state.model_points:
                        model_data = state.model_points[best_town]
                        validation["nearest_town"] = best_town

                        # Compute actual biases where model point data is available
                        model_temp = model_data.get("temperature_f") or model_data.get("tmp_f")
                        model_wind = model_data.get("wind_speed_kt") or model_data.get("wspd_kt")
                        model_rh = model_data.get("relative_humidity") or model_data.get("rh")

                        if obs_temp is not None and model_temp is not None:
                            validation["temp_bias_f"] = round(obs_temp - model_temp, 1)
                        if obs_wind is not None and model_wind is not None:
                            validation["wind_bias_kt"] = round(obs_wind - model_wind, 1)
                        if obs_rh is not None and model_rh is not None:
                            validation["rh_bias_pct"] = round(obs_rh - model_rh, 1)

                    # Flag if METAR shows fire-critical conditions
                    if obs_rh is not None and obs_rh < 25:
                        validation["fire_flag"] = f"METAR RH {obs_rh:.0f}% — fire weather threshold"
                    if obs_wind is not None and obs_wind >= 20:
                        validation["wind_flag"] = f"METAR wind {obs_wind:.0f}kt — elevated fire spread risk"

                    state.obs_model_validation[station_id] = validation
                    data["stations_validated"] += 1

                except Exception as e:
                    errors.append(f"Validation {station_id}: {e}")

        except Exception as e:
            errors.append(f"ObsModelValidator: {traceback.format_exc()}")

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=True,
            data=data,
            errors=errors,
            elapsed_seconds=elapsed,
        )


# =============================================================================
# Tier 3 runner
# =============================================================================

ALL_TIER3_AGENTS = [
    FireRiskAssessor,
    FuelAnalyst,
    TerrainAnalyst,
    WindShiftDetector,
    ObsModelValidator,
]


def run_tier3(state: ZoneState, zone_config, swarm_config, max_workers: int = 5) -> list[AgentResult]:
    """Run all Tier 3 agents concurrently."""
    from concurrent.futures import ThreadPoolExecutor, as_completed

    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {}
        for agent_cls in ALL_TIER3_AGENTS:
            agent = agent_cls()
            future = pool.submit(agent.run, state, zone_config, swarm_config)
            futures[future] = agent.NAME

        for future in as_completed(futures):
            name = futures[future]
            try:
                result = future.result(timeout=180)
                results.append(result)
                logger.info(result.summary)
            except Exception as e:
                results.append(AgentResult(
                    agent_name=name, tier=3, success=False,
                    errors=[str(e)],
                ))

    return results
