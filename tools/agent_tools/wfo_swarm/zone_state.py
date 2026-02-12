"""
ZoneState — Shared mutable state for a zone swarm run.

Each ZoneSwarm creates one ZoneState at the start of a cycle run.
All 22 agents read from and write to this state. Tier barriers ensure
that downstream agents only see data from completed upstream tiers.

Thread-safety: agents within a tier run concurrently but tiers are
sequential, so no locking is needed — each tier writes different keys.
"""
import time
from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class ZoneState:
    """Shared state accumulated by all agents during a zone swarm run."""

    zone_id: str
    cycle: str
    run_id: str = ""  # unique run identifier
    started_at: float = field(default_factory=time.time)

    # ── Tier 1: Data Acquisition ──────────────────────────────────────────
    metar_obs: dict[str, Any] = field(default_factory=dict)
    # station_id -> {tmpf, dwpf, sknt, drct, relh, ...}

    raws_obs: dict[str, Any] = field(default_factory=dict)
    # station_name -> {air_temp, rh, wind_speed, wind_dir, ...}

    nws_alerts: list[dict] = field(default_factory=list)
    # List of NWS alert features

    nws_discussion: str = ""
    # Area Forecast Discussion text from zone WFO(s)

    spc_fire_outlook: dict[str, Any] = field(default_factory=dict)
    # SPC Day 1 Fire Weather Outlook

    spc_discussion: str = ""
    # SPC Fire Weather Discussion text

    model_points: dict[str, dict] = field(default_factory=dict)
    # town_name -> {hrrr: {T, RH, wind, ...}, gfs: {...}}

    # ── Tier 2: Cross-Section Analysis ────────────────────────────────────
    xs_images: dict[str, list[str]] = field(default_factory=dict)
    # transect_id -> [path1.png, path2.png, ...]

    xs_data: dict[str, dict] = field(default_factory=dict)
    # transect_id -> {fhr -> CrossSectionData stats}

    gif_paths: dict[str, str] = field(default_factory=dict)
    # transect_id -> gif_path

    model_comparison: dict[str, dict] = field(default_factory=dict)
    # transect_id -> {hrrr: {...}, gfs: {...}, delta: {...}}

    # ── Tier 3: Assessment ────────────────────────────────────────────────
    fire_risk: dict[str, dict] = field(default_factory=dict)
    # transect_id -> FireRiskAssessment-like dict per FHR

    fuel_conditions: dict[str, dict] = field(default_factory=dict)
    # town_name -> fuel assessment dict

    terrain_assessments: dict[str, dict] = field(default_factory=dict)
    # town_name -> terrain assessment dict

    wind_shifts: dict[str, dict] = field(default_factory=dict)
    # transect_id -> wind shift detection results

    obs_model_validation: dict[str, dict] = field(default_factory=dict)
    # station_id -> {model_wind, obs_wind, bias, ...}

    # ── Tier 4: Synthesis ─────────────────────────────────────────────────
    town_forecasts: dict[str, dict] = field(default_factory=dict)
    # town_name -> {headline, text, risk_level, details}

    zone_discussion: str = ""
    # AFD-style zone-level meteorological discussion

    risk_ranking: list[dict] = field(default_factory=list)
    # [{town, score, level, factors}, ...] sorted by risk

    temporal_analysis: dict[str, dict] = field(default_factory=dict)
    # town_name -> {peak_fhr, trend, evolution}

    # ── Tier 5: Output ────────────────────────────────────────────────────
    bulletin: dict[str, Any] = field(default_factory=dict)
    # Structured JSON bulletin (the primary MCP output)

    report_path: str = ""
    # Path to compiled PDF report

    # ── Metadata ──────────────────────────────────────────────────────────
    tier_timings: dict[int, float] = field(default_factory=dict)
    # tier_number -> elapsed_seconds

    agent_timings: dict[str, float] = field(default_factory=dict)
    # agent_name -> elapsed_seconds

    errors: list[dict] = field(default_factory=list)
    # [{agent, tier, error, timestamp}, ...]

    @property
    def elapsed(self) -> float:
        return time.time() - self.started_at

    def add_error(self, agent: str, tier: int, error: str):
        self.errors.append({
            "agent": agent,
            "tier": tier,
            "error": error,
            "timestamp": time.time(),
            "elapsed": self.elapsed,
        })

    def to_bulletin_meta(self) -> dict:
        """Metadata section for the output bulletin."""
        return {
            "zone_id": self.zone_id,
            "cycle": self.cycle,
            "run_id": self.run_id,
            "elapsed_seconds": self.elapsed,
            "tier_timings": self.tier_timings,
            "error_count": len(self.errors),
            "town_count": len(self.town_forecasts),
            "transect_images": sum(
                len(v) for v in self.xs_images.values()
            ),
        }

    def summary(self) -> str:
        """One-line summary of the run state."""
        n_errors = len(self.errors)
        n_towns = len(self.town_forecasts)
        n_images = sum(len(v) for v in self.xs_images.values())
        return (
            f"Zone {self.zone_id} | cycle={self.cycle} | "
            f"{n_towns} town forecasts | {n_images} images | "
            f"{n_errors} errors | {self.elapsed:.1f}s"
        )
