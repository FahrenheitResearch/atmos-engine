"""
Tier 5: Output Agents (2 agents)

These agents compile all zone state into final deliverables:
the structured JSON bulletin and the PDF report.

Agents:
    21. BulletinWriter   — compile structured JSON bulletin (primary MCP output)
    22. ReportCompiler   — generate LaTeX/PDF report with all figures
"""
import json
import logging
import os
import time
import traceback
from datetime import datetime

from tools.agent_tools.wfo_swarm.zone_state import ZoneState
from tools.agent_tools.wfo_swarm.config import AgentResult

logger = logging.getLogger(__name__)


# =============================================================================
# Agent 21: Bulletin Writer
# =============================================================================

class BulletinWriter:
    """Compiles the structured JSON bulletin — the primary MCP/API output."""

    TIER = 5
    NAME = "bulletin_writer"

    def run(self, state: ZoneState, zone_config, swarm_config) -> AgentResult:
        t0 = time.time()
        errors = []

        try:
            bulletin = self._compile_bulletin(state, zone_config)
            state.bulletin = bulletin

            # Write to disk
            output_dir = os.path.join(
                swarm_config.output_dir, state.zone_id, state.cycle
            )
            os.makedirs(output_dir, exist_ok=True)

            bulletin_path = os.path.join(output_dir, "bulletin.json")
            with open(bulletin_path, "w") as f:
                json.dump(bulletin, f, indent=2, default=str)

            logger.info(f"Bulletin written: {bulletin_path} ({os.path.getsize(bulletin_path)} bytes)")

        except Exception as e:
            errors.append(f"BulletinWriter: {traceback.format_exc()}")

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=bool(state.bulletin),
            data={"bulletin_size": len(json.dumps(state.bulletin, default=str))},
            errors=errors,
            elapsed_seconds=elapsed,
        )

    def _compile_bulletin(self, state, zone_config):
        """Build the complete JSON bulletin."""
        now = datetime.utcnow().isoformat() + "Z"

        # Determine zone-level headline from risk ranking
        if state.risk_ranking:
            top_town = state.risk_ranking[0]
            top_level = top_town["level"]
            headline = (
                f"{zone_config.name}: {top_level} — "
                f"Highest risk at {top_town['town']} "
                f"(score {top_town['score']})"
            )
        else:
            top_level = "UNKNOWN"
            headline = f"{zone_config.name}: Assessment in progress"

        bulletin = {
            "version": "1.0",
            "type": "zone_fire_weather_bulletin",
            "zone_id": zone_config.zone_id,
            "zone_name": zone_config.name,
            "cycle": state.cycle,
            "issued": now,
            "headline": headline,
            "max_risk_level": top_level,

            # Risk summary
            "risk_summary": {
                "ranking": state.risk_ranking,
                "top_concern": state.risk_ranking[0] if state.risk_ranking else None,
                "elevated_towns": [
                    r for r in state.risk_ranking
                    if r["level"] in ("CRITICAL", "ELEVATED")
                ],
            },

            # Per-town forecasts
            "town_forecasts": state.town_forecasts,

            # Zone discussion
            "zone_discussion": state.zone_discussion,

            # Transect assessments
            "transect_assessments": {
                tid: {
                    "fire_risk": state.fire_risk.get(tid, {}),
                    "wind_shifts": state.wind_shifts.get(tid, {}),
                    "image_count": len(state.xs_images.get(tid, [])),
                    "gif_available": tid in state.gif_paths,
                }
                for tid in zone_config.transect_ids
            },

            # External data summary
            "external_data": {
                "metar_stations": len(state.metar_obs),
                "raws_stations": len(state.raws_obs),
                "nws_alerts": len(state.nws_alerts),
                "nws_alert_types": list(set(
                    a.get("properties", {}).get("event", "")
                    for a in state.nws_alerts
                )),
                "spc_fire_outlook_areas": len(
                    state.spc_fire_outlook.get("features", [])
                ) if isinstance(state.spc_fire_outlook, dict) else 0,
                "model_points": len(state.model_points),
                "obs_validations": len(state.obs_model_validation),
            },

            # Temporal analysis
            "temporal_analysis": state.temporal_analysis,

            # Model comparison
            "model_comparison": {
                tid: "available" for tid in state.model_comparison
            },

            # Metadata
            "metadata": state.to_bulletin_meta(),
        }

        return bulletin


# =============================================================================
# Agent 22: Report Compiler
# =============================================================================

class ReportCompiler:
    """Generates LaTeX/PDF report with all figures."""

    TIER = 5
    NAME = "report_compiler"

    def run(self, state: ZoneState, zone_config, swarm_config) -> AgentResult:
        t0 = time.time()
        errors = []
        data = {}

        if not swarm_config.generate_pdf:
            elapsed = time.time() - t0
            return AgentResult(
                agent_name=self.NAME, tier=self.TIER, success=True,
                data={"skipped": True, "reason": "PDF generation disabled"},
                elapsed_seconds=elapsed,
            )

        try:
            from tools.agent_tools.report_builder import ReportBuilder, ReportConfig

            output_dir = os.path.join(
                swarm_config.output_dir, state.zone_id, state.cycle
            )
            os.makedirs(output_dir, exist_ok=True)

            # Create report
            config = ReportConfig(
                title=f"Fire Weather Assessment: {zone_config.name}",
                report_type="fire_weather",
                author="Oregon WFO Agent Swarm",
                date=datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
                abstract=(
                    f"Automated fire weather assessment for {zone_config.name} "
                    f"({zone_config.zone_id}), cycle {state.cycle}. "
                    f"Analysis covers {zone_config.town_count} towns and "
                    f"{zone_config.transect_count} cross-section transects."
                ),
            )

            builder = ReportBuilder(config, output_dir=output_dir)

            # Section 1: Zone Discussion
            s1 = builder.add_section(
                "Zone Meteorological Discussion",
                state.zone_discussion or "No discussion generated.",
            )

            # Section 2: Risk Ranking
            if state.risk_ranking:
                ranking_text = "\\begin{enumerate}\n"
                for r in state.risk_ranking:
                    ranking_text += (
                        f"\\item \\textbf{{{r['town']}}} — "
                        f"{r['level']} (score {r['score']}). "
                        f"Factors: {', '.join(r['factors']) if r['factors'] else 'None identified'}\n"
                    )
                ranking_text += "\\end{enumerate}"
                s2 = builder.add_section("Risk Ranking", ranking_text)

            # Section 3: Town Forecasts
            for town_name, forecast in state.town_forecasts.items():
                from tools.agent_tools.report_builder import escape_latex
                town_text = escape_latex(
                    f"{forecast.get('headline', town_name)}\n\n"
                    f"{forecast.get('text', 'No forecast text.')}"
                )
                builder.add_section(
                    f"Town Forecast: {town_name}", town_text
                )

            # Section 4: Cross-Section Figures
            fig_section = builder.add_section(
                "Cross-Section Analysis", "Selected cross-section imagery:"
            )
            for tid, images in state.xs_images.items():
                for img_path in images[:4]:  # limit to 4 per transect
                    if os.path.exists(img_path):
                        builder.add_figure(
                            fig_section, img_path,
                            caption=f"Transect: {tid}",
                        )

            # Section 5: Observation Summary
            if state.metar_obs:
                from tools.agent_tools.report_builder import escape_latex
                obs_lines = []
                for sid, obs in list(state.metar_obs.items())[:10]:
                    t = obs.get("tmpf", "?")
                    rh = obs.get("relh", "?")
                    w = obs.get("sknt", "?")
                    obs_lines.append(f"{sid}: T={t}F, RH={rh}\\%, Wind={w}kt")
                builder.add_section(
                    "Surface Observations",
                    "\\begin{verbatim}\n" + "\n".join(obs_lines) + "\n\\end{verbatim}"
                )

            # Compile
            builder.save_latex()
            pdf_path = builder.compile_pdf()
            if pdf_path and os.path.exists(pdf_path):
                state.report_path = pdf_path
                data["pdf_path"] = pdf_path
                data["pdf_size_kb"] = os.path.getsize(pdf_path) // 1024
                logger.info(f"PDF report: {pdf_path} ({data['pdf_size_kb']} KB)")
            else:
                errors.append("PDF compilation returned no path")

        except Exception as e:
            errors.append(f"ReportCompiler: {traceback.format_exc()}")

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=bool(state.report_path) or not swarm_config.generate_pdf,
            data=data,
            errors=errors,
            elapsed_seconds=elapsed,
        )


# =============================================================================
# Tier 5 runner
# =============================================================================

def run_tier5(state: ZoneState, zone_config, swarm_config) -> list[AgentResult]:
    """Run Tier 5 agents. Bulletin first (fast), then report (slow)."""
    results = []

    # Bulletin is fast and critical — run synchronously first
    bulletin_agent = BulletinWriter()
    result = bulletin_agent.run(state, zone_config, swarm_config)
    results.append(result)

    # Report can run after bulletin
    report_agent = ReportCompiler()
    result = report_agent.run(state, zone_config, swarm_config)
    results.append(result)

    return results
