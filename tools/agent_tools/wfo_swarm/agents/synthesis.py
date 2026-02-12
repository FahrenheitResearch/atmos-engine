"""
Tier 4: Synthesis Agents (4 agents)

These agents combine all data from Tiers 1-3 to produce human-readable
forecasts, discussions, and rankings.

Agents:
    17. TownForecaster   — per-town forecast text from all tier 1-3 data
    18. ZoneMeteorologist — zone-level AFD-style discussion
    19. RiskRanker        — rank all towns by fire risk, identify top concerns
    20. TemporalAnalyst   — track risk evolution over 48h forecast window
"""
import logging
import time
import traceback
from datetime import datetime

from tools.agent_tools.wfo_swarm.zone_state import ZoneState
from tools.agent_tools.wfo_swarm.config import AgentResult

logger = logging.getLogger(__name__)


# =============================================================================
# Agent 17: Town Forecaster
# =============================================================================

class TownForecaster:
    """Generates per-town forecast text from all available data."""

    TIER = 4
    NAME = "town_forecaster"

    def run(self, state: ZoneState, zone_config, swarm_config) -> AgentResult:
        t0 = time.time()
        errors = []
        data = {"towns_forecast": 0}

        try:
            for town_name, (lat, lon) in zone_config.towns.items():
                try:
                    forecast = self._generate_town_forecast(
                        town_name, lat, lon, state, zone_config
                    )
                    state.town_forecasts[town_name] = forecast
                    data["towns_forecast"] += 1
                except Exception as e:
                    errors.append(f"Forecast {town_name}: {e}")
                    state.town_forecasts[town_name] = {
                        "headline": f"Forecast unavailable for {town_name}",
                        "text": f"Error generating forecast: {e}",
                        "risk_level": "UNKNOWN",
                    }

        except Exception as e:
            errors.append(f"TownForecaster: {traceback.format_exc()}")

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=data["towns_forecast"] > 0,
            data=data,
            errors=errors,
            elapsed_seconds=elapsed,
        )

    def _generate_town_forecast(self, town_name, lat, lon, state, zone_config):
        """Build a structured forecast for one town from all available data."""

        # Gather inputs from zone state
        metar_summary = self._summarize_metar(state.metar_obs, lat, lon)
        raws_summary = self._summarize_raws(state.raws_obs)
        fire_risk_summary = self._summarize_fire_risk(state.fire_risk, zone_config)
        fuel_info = state.fuel_conditions.get(town_name, {})
        terrain_info = state.terrain_assessments.get(town_name, {})
        wind_info = self._summarize_wind_shifts(state.wind_shifts)

        # Determine risk level — use METAR ground truth to override column-averaged transect scores
        transect_score = 0
        for tid, fhr_data in state.fire_risk.items():
            for fhr_key, assessment in fhr_data.items():
                if isinstance(assessment, dict):
                    score = assessment.get("score", 0)
                    if score > transect_score:
                        transect_score = score

        # Compute METAR-based score using RiskRanker's scoring
        metar_score = 0
        nearest_obs = RiskRanker._find_nearest_metar(state.metar_obs, lat, lon)
        if nearest_obs:
            metar_score, _ = RiskRanker._score_from_metar(nearest_obs)

        max_risk_score = max(metar_score, transect_score)
        if max_risk_score >= 75:
            max_risk_level = "CRITICAL"
        elif max_risk_score >= 50:
            max_risk_level = "ELEVATED"
        elif max_risk_score >= 25:
            max_risk_level = "MODERATE"
        else:
            max_risk_level = "LOW"

        # Build headline
        headline = self._build_headline(town_name, max_risk_level, state)

        # Build forecast text
        sections = []

        # Current conditions
        if metar_summary:
            sections.append(f"CURRENT CONDITIONS: {metar_summary}")

        # Fire weather
        if fire_risk_summary:
            sections.append(f"FIRE WEATHER: {fire_risk_summary}")

        # Fuel conditions
        if fuel_info and not fuel_info.get("error"):
            fuel_text = fuel_info.get("fuel_assessment", {})
            if isinstance(fuel_text, dict) and fuel_text.get("summary"):
                sections.append(f"FUELS: {fuel_text['summary']}")

        # Terrain
        if terrain_info and terrain_info.get("status") != "no_profile":
            terrain_notes = terrain_info.get("terrain_notes", "")
            if terrain_notes:
                sections.append(f"TERRAIN: {terrain_notes[:200]}")

        # Wind shifts
        if wind_info:
            sections.append(f"WIND OUTLOOK: {wind_info}")

        # NWS alerts
        alert_text = self._summarize_alerts(state.nws_alerts, lat, lon)
        if alert_text:
            sections.append(f"ALERTS: {alert_text}")

        # RAWS/fuel moisture
        if raws_summary:
            sections.append(f"FIRE WEATHER OBS: {raws_summary}")

        text = "\n\n".join(sections) if sections else "Insufficient data for detailed forecast."

        return {
            "headline": headline,
            "text": text,
            "risk_level": max_risk_level,
            "risk_score": max_risk_score,
            "lat": lat,
            "lon": lon,
            "data_sources": {
                "metar_stations": len(state.metar_obs),
                "raws_stations": len(state.raws_obs),
                "nws_alerts": len(state.nws_alerts),
                "transects_assessed": len(state.fire_risk),
            },
        }

    def _build_headline(self, town_name, risk_level, state):
        """Generate a concise headline for the town."""
        level_text = {
            "CRITICAL": "CRITICAL FIRE WEATHER",
            "ELEVATED": "ELEVATED FIRE RISK",
            "MODERATE": "MODERATE FIRE RISK",
            "LOW": "LOW FIRE RISK",
        }
        prefix = level_text.get(risk_level, risk_level)

        # Check for active alerts
        alert_types = set()
        for alert in state.nws_alerts:
            event = alert.get("properties", {}).get("event", "")
            if "fire" in event.lower() or "red flag" in event.lower():
                alert_types.add(event)

        if alert_types:
            alert_str = ", ".join(sorted(alert_types))
            return f"{town_name}: {prefix} — Active: {alert_str}"

        return f"{town_name}: {prefix}"

    def _summarize_metar(self, metar_obs, lat, lon):
        """Summarize nearest METAR observations."""
        if not metar_obs:
            return ""

        # Find nearest station (simple distance)
        nearest = None
        nearest_dist = float("inf")
        for sid, obs in metar_obs.items():
            olat = obs.get("lat", 0)
            olon = obs.get("lon", 0)
            if olat and olon:
                d = ((olat - lat) ** 2 + (olon - lon) ** 2) ** 0.5
                if d < nearest_dist:
                    nearest_dist = d
                    nearest = obs

        if not nearest:
            # Just use first available
            nearest = next(iter(metar_obs.values()))

        parts = []
        if nearest.get("tmpf") is not None:
            parts.append(f"Temp {nearest['tmpf']:.0f}F")
        if nearest.get("relh") is not None:
            parts.append(f"RH {nearest['relh']:.0f}%")
        if nearest.get("sknt") is not None:
            wind = f"Wind {nearest['sknt']:.0f}kt"
            if nearest.get("drct") is not None:
                wind += f" from {nearest['drct']:.0f}°"
            if nearest.get("gust_sknt"):
                wind += f" G{nearest['gust_sknt']:.0f}kt"
            parts.append(wind)

        station = nearest.get("station", "?")
        return f"({station}) " + ", ".join(parts) if parts else ""

    def _summarize_raws(self, raws_obs):
        """Summarize RAWS observations."""
        if not raws_obs:
            return ""
        parts = []
        for name, obs in list(raws_obs.items())[:3]:
            rh = obs.get("relative_humidity") or obs.get("rh")
            wind = obs.get("wind_speed_mph")
            fm10 = obs.get("fuel_moisture_10hr")
            sub = []
            if rh is not None:
                sub.append(f"RH {rh}%")
            if wind is not None:
                sub.append(f"Wind {wind} mph")
            if fm10 is not None:
                sub.append(f"10-hr FM {fm10}%")
            if sub:
                parts.append(f"{name}: {', '.join(sub)}")
        return "; ".join(parts)

    def _summarize_fire_risk(self, fire_risk, zone_config):
        """Summarize fire risk across transects."""
        if not fire_risk:
            return ""
        levels = []
        for tid, fhr_data in fire_risk.items():
            for fhr_key, assessment in fhr_data.items():
                if isinstance(assessment, dict) and "level" in assessment:
                    levels.append((tid, fhr_key, assessment["level"], assessment.get("score", 0)))

        if not levels:
            return ""

        # Find peak
        peak = max(levels, key=lambda x: x[3])
        return (
            f"Peak risk: {peak[2]} (score {peak[3]}) on transect {peak[0]} "
            f"at {peak[1]}. {len(levels)} assessments across "
            f"{len(fire_risk)} transects."
        )

    def _summarize_wind_shifts(self, wind_shifts):
        """Summarize detected wind shifts."""
        if not wind_shifts:
            return "No significant wind shifts detected in forecast period."

        summaries = []
        for tid, shifts in wind_shifts.items():
            if isinstance(shifts, dict) and shifts.get("shifts"):
                for s in shifts["shifts"][:2]:
                    summaries.append(
                        f"{tid}: {s.get('description', 'shift detected')}"
                    )
        return "; ".join(summaries) if summaries else "No significant wind shifts."

    def _summarize_alerts(self, alerts, lat, lon):
        """Summarize NWS alerts near this location."""
        if not alerts:
            return ""
        fire_alerts = [
            a for a in alerts
            if any(kw in a.get("properties", {}).get("event", "").lower()
                   for kw in ("fire", "red flag", "wind", "heat"))
        ]
        if not fire_alerts:
            return ""
        return "; ".join(
            a.get("properties", {}).get("headline", "Alert")
            for a in fire_alerts[:3]
        )


# =============================================================================
# Agent 18: Zone Meteorologist
# =============================================================================

class ZoneMeteorologist:
    """Generates AFD-style zone-level discussion."""

    TIER = 4
    NAME = "zone_meteorologist"

    def run(self, state: ZoneState, zone_config, swarm_config) -> AgentResult:
        t0 = time.time()
        errors = []

        try:
            discussion = self._generate_discussion(state, zone_config)
            state.zone_discussion = discussion
        except Exception as e:
            errors.append(f"ZoneMeteorologist: {traceback.format_exc()}")
            state.zone_discussion = f"Discussion generation failed: {e}"

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=len(state.zone_discussion) > 100,
            data={"length": len(state.zone_discussion)},
            errors=errors,
            elapsed_seconds=elapsed,
        )

    def _generate_discussion(self, state, zone_config):
        """Build an AFD-style discussion from zone data."""
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
        cycle = state.cycle

        sections = []

        # Header
        sections.append(
            f"ZONE FIRE WEATHER DISCUSSION\n"
            f"Zone: {zone_config.zone_id} — {zone_config.name}\n"
            f"Cycle: {cycle}\n"
            f"Issued: {now}\n"
            f"{'=' * 60}"
        )

        # Situation
        situation_parts = []
        if state.spc_discussion:
            # Extract relevant portion
            spc_excerpt = state.spc_discussion[:500]
            situation_parts.append(f"SPC Discussion excerpt:\n{spc_excerpt}")

        if state.nws_discussion:
            nws_excerpt = state.nws_discussion[:500]
            situation_parts.append(f"WFO Discussion excerpt:\n{nws_excerpt}")

        if state.nws_alerts:
            alert_count = len(state.nws_alerts)
            situation_parts.append(f"Active NWS alerts: {alert_count}")

        sections.append(
            "SITUATION:\n" +
            ("\n".join(situation_parts) if situation_parts else "No significant weather features.")
        )

        # Fire weather
        fire_parts = []
        for tid, fhr_data in state.fire_risk.items():
            peak_level = "LOW"
            peak_score = 0
            for fhr_key, assessment in fhr_data.items():
                if isinstance(assessment, dict):
                    s = assessment.get("score", 0)
                    if s > peak_score:
                        peak_score = s
                        peak_level = assessment.get("level", "LOW")
            fire_parts.append(f"  {tid}: Peak {peak_level} (score {peak_score})")

        sections.append(
            "FIRE WEATHER ASSESSMENT:\n" +
            ("\n".join(fire_parts) if fire_parts else "  No transect assessments available.")
        )

        # Observations summary
        obs_parts = []
        for sid, obs in list(state.metar_obs.items())[:5]:
            t = obs.get("tmpf", "?")
            rh = obs.get("relh", "?")
            w = obs.get("sknt", "?")
            obs_parts.append(f"  {sid}: T={t}F RH={rh}% Wind={w}kt")

        sections.append(
            "SURFACE OBSERVATIONS:\n" +
            ("\n".join(obs_parts) if obs_parts else "  No METAR data available.")
        )

        # Wind shifts
        if state.wind_shifts:
            shift_parts = []
            for tid, shifts in state.wind_shifts.items():
                if isinstance(shifts, dict) and shifts.get("shifts"):
                    shift_parts.append(f"  {tid}: {len(shifts['shifts'])} shift(s) detected")
            if shift_parts:
                sections.append("WIND SHIFT ANALYSIS:\n" + "\n".join(shift_parts))

        # Model comparison
        if state.model_comparison:
            comp_parts = []
            for tid, comp in state.model_comparison.items():
                comp_parts.append(f"  {tid}: HRRR vs GFS comparison available")
            sections.append("MODEL COMPARISON:\n" + "\n".join(comp_parts))

        # Footer
        sections.append(
            f"{'=' * 60}\n"
            f"Generated by Oregon WFO Agent Swarm v1.0\n"
            f"Zone {zone_config.zone_id} | {zone_config.town_count} towns | "
            f"{zone_config.transect_count} transects\n"
            f"Processing time: {state.elapsed:.1f}s"
        )

        return "\n\n".join(sections)


# =============================================================================
# Agent 19: Risk Ranker
# =============================================================================

class RiskRanker:
    """Ranks all towns by fire risk and identifies top concerns.

    Uses METAR surface observations as ground truth to override column-averaged
    cross-section scores that systematically underestimate surface conditions.
    """

    TIER = 4
    NAME = "risk_ranker"

    def run(self, state: ZoneState, zone_config, swarm_config) -> AgentResult:
        t0 = time.time()
        errors = []

        try:
            rankings = []

            for town_name, (lat, lon) in zone_config.towns.items():
                factors = []

                # ── METAR-derived surface fire risk (ground truth) ────────
                metar_score = 0
                nearest_obs = self._find_nearest_metar(state.metar_obs, lat, lon)
                if nearest_obs:
                    metar_score, metar_factors = self._score_from_metar(nearest_obs)
                    factors.extend(metar_factors)

                # ── Transect-derived fire risk (column-averaged, may be low-biased) ──
                transect_score = 0
                for tid, fhr_data in state.fire_risk.items():
                    for fhr_key, assessment in fhr_data.items():
                        if isinstance(assessment, dict):
                            s = assessment.get("score", 0)
                            if s > transect_score:
                                transect_score = s

                # Take the MAXIMUM of METAR and transect scores as the fire wx component
                fire_wx_score = max(metar_score, transect_score)
                if transect_score > 50:
                    factors.append(f"High transect fire risk ({transect_score})")
                if metar_score > transect_score + 10:
                    factors.append(f"METAR override: surface conditions worse than model ({metar_score} vs {transect_score})")

                # ── Composite score: fire wx (50%) + fuel (15%) + alerts (15%) + wind shifts (10%) + obs validation (10%) ──
                score = fire_wx_score * 0.50

                # Fuel conditions (up to 15 pts)
                fuel = state.fuel_conditions.get(town_name, {})
                if isinstance(fuel, dict) and not fuel.get("error"):
                    fuel_assessment = fuel.get("fuel_assessment", {})
                    if isinstance(fuel_assessment, dict):
                        fuel_risk = str(fuel_assessment.get("risk_level", "")).lower()
                        if "high" in fuel_risk or "extreme" in fuel_risk:
                            score += 15
                            factors.append("High fuel risk")
                        elif "moderate" in fuel_risk:
                            score += 8
                            factors.append("Moderate fuel risk")

                # Active NWS fire-related alerts (up to 15 pts)
                fire_alerts = [
                    a for a in state.nws_alerts
                    if any(kw in a.get("properties", {}).get("event", "").lower()
                           for kw in ("fire", "red flag"))
                ]
                if fire_alerts:
                    score += 15
                    factors.append(f"{len(fire_alerts)} fire-related alerts active")
                else:
                    # Wind advisories still matter for fire spread
                    wind_alerts = [
                        a for a in state.nws_alerts
                        if "wind" in a.get("properties", {}).get("event", "").lower()
                    ]
                    if wind_alerts:
                        score += 5
                        factors.append(f"Wind advisory active")

                # Wind shifts detected (up to 10 pts)
                for tid, shifts in state.wind_shifts.items():
                    if isinstance(shifts, dict) and shifts.get("shifts"):
                        score += 10
                        factors.append("Wind shifts forecast")
                        break

                # Obs-model validation bias (up to 10 pts) — penalize if model is known-wrong
                if nearest_obs:
                    bias_penalty = self._compute_bias_penalty(nearest_obs, state)
                    if bias_penalty > 0:
                        score += bias_penalty
                        factors.append(f"Model bias detected (+{bias_penalty:.0f})")

                # Determine level
                if score >= 75:
                    level = "CRITICAL"
                elif score >= 50:
                    level = "ELEVATED"
                elif score >= 25:
                    level = "MODERATE"
                else:
                    level = "LOW"

                rankings.append({
                    "town": town_name,
                    "lat": lat,
                    "lon": lon,
                    "score": round(score, 1),
                    "level": level,
                    "factors": factors,
                    "metar_score": round(metar_score, 1),
                    "transect_score": round(transect_score, 1),
                })

            # Sort by score descending
            rankings.sort(key=lambda x: x["score"], reverse=True)
            state.risk_ranking = rankings

        except Exception as e:
            errors.append(f"RiskRanker: {traceback.format_exc()}")

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=len(state.risk_ranking) > 0,
            data={"towns_ranked": len(state.risk_ranking)},
            errors=errors,
            elapsed_seconds=elapsed,
        )

    @staticmethod
    def _find_nearest_metar(metar_obs: dict, lat: float, lon: float) -> dict | None:
        """Find the nearest METAR station to a lat/lon point."""
        if not metar_obs:
            return None
        nearest = None
        nearest_dist = float("inf")
        for sid, obs in metar_obs.items():
            olat = obs.get("lat")
            olon = obs.get("lon")
            if olat is not None and olon is not None:
                d = ((olat - lat) ** 2 + (olon - lon) ** 2) ** 0.5
                if d < nearest_dist:
                    nearest_dist = d
                    nearest = obs
        return nearest

    @staticmethod
    def _score_from_metar(obs: dict) -> tuple[float, list[str]]:
        """Compute a fire risk score directly from METAR surface observations.

        Uses the same thresholds as FireRiskAnalyzer.assess_conditions() but
        applied to actual surface obs instead of column-averaged model data.
        Returns (score 0-100, list of factor strings).
        """
        factors = []

        # ── RH component (40% weight) ──
        rh = obs.get("relh")
        rh_component = 0
        if rh is not None:
            if rh < 8:
                rh_component = 100
                factors.append(f"CRITICAL: Surface RH {rh:.0f}% (METAR)")
            elif rh < 15:
                rh_component = 50 + 50 * (15 - rh) / 7
                factors.append(f"Red flag RH: {rh:.0f}% (METAR)")
            elif rh < 25:
                rh_component = 50 * (25 - rh) / 10
                factors.append(f"Low RH: {rh:.0f}% (METAR)")
            elif rh < 35:
                rh_component = 15 * (35 - rh) / 10
                # Only add factor if notable
                if rh < 30:
                    factors.append(f"Below-average RH: {rh:.0f}% (METAR)")

        # ── Wind component (30% weight) ──
        wind_kt = obs.get("sknt") or 0
        gust_kt = obs.get("gust_sknt") or 0
        max_wind = max(wind_kt, gust_kt)
        wind_component = 0
        if max_wind >= 30:
            wind_component = 100
            factors.append(f"CRITICAL: Wind {max_wind:.0f}kt (METAR)")
        elif max_wind >= 25:
            wind_component = 50 + 50 * (max_wind - 25) / 5
            factors.append(f"Red flag wind: {max_wind:.0f}kt (METAR)")
        elif max_wind >= 15:
            wind_component = 50 * (max_wind - 15) / 10
            if max_wind >= 20:
                factors.append(f"Elevated wind: {max_wind:.0f}kt (METAR)")
        elif max_wind >= 10:
            wind_component = 10 * (max_wind - 10) / 5

        # ── VPD component (10% weight) ──
        temp_f = obs.get("tmpf")
        vpd_component = 0
        if temp_f is not None and rh is not None:
            temp_c = (temp_f - 32) * 5 / 9
            # Tetens formula for saturation vapor pressure
            es = 6.1078 * 10 ** (7.5 * temp_c / (temp_c + 237.3))
            ea = es * (rh / 100.0)
            vpd = es - ea
            if vpd >= 13:
                vpd_component = 100
            elif vpd >= 7.8:
                vpd_component = 100 * (vpd - 7.8) / (13 - 7.8)

        # ── Temperature component (20% weight) — hot+dry is worse ──
        temp_component = 0
        if temp_f is not None:
            if temp_f >= 100:
                temp_component = 100
                factors.append(f"Extreme heat: {temp_f:.0f}F (METAR)")
            elif temp_f >= 90:
                temp_component = 50 + 50 * (temp_f - 90) / 10
                factors.append(f"Hot: {temp_f:.0f}F (METAR)")
            elif temp_f >= 80:
                temp_component = 25 * (temp_f - 80) / 10
            # Cold temps suppress fire risk
            elif temp_f < 40:
                rh_component *= 0.3  # heavily suppress RH concern in cold weather
                wind_component *= 0.5  # somewhat suppress wind concern

        score = (
            0.40 * rh_component
            + 0.30 * wind_component
            + 0.20 * temp_component
            + 0.10 * vpd_component
        )
        return score, factors

    @staticmethod
    def _compute_bias_penalty(nearest_obs: dict, state: ZoneState) -> float:
        """Compute a penalty score when METAR diverges significantly from model.

        Large divergence means the model cross-section data is unreliable and
        conditions may be worse than the transect assessment suggests.
        """
        penalty = 0
        obs_rh = nearest_obs.get("relh")
        obs_wind = nearest_obs.get("sknt") or 0

        # Check if any obs_model_validation shows large biases
        for sid, val in state.obs_model_validation.items():
            # If METAR shows low RH but model thinks it's moderate, add penalty
            if obs_rh is not None and obs_rh < 25:
                penalty = max(penalty, 5)  # model may be overestimating moisture
            if obs_wind > 15:
                penalty = max(penalty, 5)  # model may be underestimating wind

        return min(penalty, 10)  # cap at 10


# =============================================================================
# Agent 20: Temporal Analyst
# =============================================================================

class TemporalAnalyst:
    """Tracks risk evolution over the 48h forecast window."""

    TIER = 4
    NAME = "temporal_analyst"

    def run(self, state: ZoneState, zone_config, swarm_config) -> AgentResult:
        t0 = time.time()
        errors = []
        data = {"towns_analyzed": 0}

        try:
            for town_name in zone_config.towns:
                try:
                    # Build temporal evolution from fire risk data
                    evolution = {}
                    peak_fhr = None
                    peak_score = 0

                    for tid, fhr_data in state.fire_risk.items():
                        for fhr_key, assessment in fhr_data.items():
                            if isinstance(assessment, dict) and "score" in assessment:
                                fhr_num = int(fhr_key.replace("F", ""))
                                score = assessment["score"]
                                level = assessment.get("level", "LOW")

                                if fhr_num not in evolution or score > evolution[fhr_num]["score"]:
                                    evolution[fhr_num] = {
                                        "score": score,
                                        "level": level,
                                        "transect": tid,
                                    }

                                if score > peak_score:
                                    peak_score = score
                                    peak_fhr = fhr_num

                    # Determine trend
                    sorted_fhrs = sorted(evolution.keys())
                    if len(sorted_fhrs) >= 2:
                        first_half = [evolution[f]["score"] for f in sorted_fhrs[:len(sorted_fhrs)//2]]
                        second_half = [evolution[f]["score"] for f in sorted_fhrs[len(sorted_fhrs)//2:]]
                        avg_first = sum(first_half) / len(first_half) if first_half else 0
                        avg_second = sum(second_half) / len(second_half) if second_half else 0

                        if avg_second > avg_first + 10:
                            trend = "INCREASING"
                        elif avg_first > avg_second + 10:
                            trend = "DECREASING"
                        else:
                            trend = "STEADY"
                    else:
                        trend = "INSUFFICIENT_DATA"

                    state.temporal_analysis[town_name] = {
                        "peak_fhr": peak_fhr,
                        "peak_score": peak_score,
                        "trend": trend,
                        "evolution": {
                            f"F{fhr:02d}": ev for fhr, ev in sorted(evolution.items())
                        },
                    }
                    data["towns_analyzed"] += 1

                except Exception as e:
                    errors.append(f"Temporal {town_name}: {e}")

        except Exception as e:
            errors.append(f"TemporalAnalyst: {traceback.format_exc()}")

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=data["towns_analyzed"] > 0,
            data=data,
            errors=errors,
            elapsed_seconds=elapsed,
        )


# =============================================================================
# Tier 4 runner
# =============================================================================

ALL_TIER4_AGENTS = [
    TownForecaster,
    ZoneMeteorologist,
    RiskRanker,
    TemporalAnalyst,
]


def run_tier4(state: ZoneState, zone_config, swarm_config, max_workers: int = 4) -> list[AgentResult]:
    """Run all Tier 4 agents concurrently."""
    from concurrent.futures import ThreadPoolExecutor, as_completed

    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {}
        for agent_cls in ALL_TIER4_AGENTS:
            agent = agent_cls()
            future = pool.submit(agent.run, state, zone_config, swarm_config)
            futures[future] = agent.NAME

        for future in as_completed(futures):
            name = futures[future]
            try:
                result = future.result(timeout=120)
                results.append(result)
                logger.info(result.summary)
            except Exception as e:
                results.append(AgentResult(
                    agent_name=name, tier=4, success=False,
                    errors=[str(e)],
                ))

    return results
