"""
SwarmConfig and ZoneConfig — Configuration for the Oregon WFO Agent Swarm.

Defines the operational parameters for swarm scheduling, zone-level
orchestration, and agent-level execution.
"""
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SwarmConfig:
    """Top-level configuration for the multi-zone swarm scheduler."""

    # Zones to run (empty = all Oregon zones)
    zones: list[str] = field(default_factory=list)

    # Stagger interval between zone launches (seconds)
    zone_stagger_seconds: float = 30.0

    # Maximum concurrent zone swarms
    max_concurrent_zones: int = 3

    # HRRR cycle to process ("latest" or "YYYYMMDD_HHz")
    cycle: str = "latest"

    # Forecast hours to analyze
    fhrs: list[int] = field(default_factory=lambda: list(range(0, 49)))

    # Products for cross-section generation
    products: list[str] = field(
        default_factory=lambda: ["wind_speed", "rh", "temperature", "fire_wx"]
    )

    # Output directory for all generated files
    output_dir: str = "output/oregon_wfo"

    # Dashboard API base URL
    api_base: str = "http://127.0.0.1:5565"

    # Timeouts (seconds)
    agent_timeout: float = 120.0
    tier_timeout: float = 300.0
    zone_timeout: float = 600.0

    # Max workers for parallel agent execution within a tier
    max_tier_workers: int = 6

    # Cross-section image settings
    y_top: int = 300  # Top of cross-section (hPa)

    # Whether to generate PDFs (requires pdflatex)
    generate_pdf: bool = True

    # Whether to generate GIFs
    generate_gifs: bool = True

    # GIF FHR range (subset of fhrs for GIF generation)
    gif_fhr_min: int = 0
    gif_fhr_max: int = 24

    def __post_init__(self):
        if not self.fhrs:
            self.fhrs = list(range(0, 49))


@dataclass
class ZoneConfig:
    """Configuration for a single Oregon coverage zone."""

    zone_id: str
    name: str
    description: str

    # Towns in this zone with coordinates
    towns: dict[str, tuple[float, float]] = field(default_factory=dict)

    # NWS WFO(s) responsible for this zone
    wfos: list[str] = field(default_factory=list)

    # METAR stations to monitor
    metar_stations: list[str] = field(default_factory=list)

    # RAWS station search points (lat, lon, radius_km)
    raws_search_points: list[tuple[float, float, float]] = field(
        default_factory=list
    )

    # Transect IDs from oregon_transects.py
    transect_ids: list[str] = field(default_factory=list)

    # Priority transect IDs (for GIF generation — subset of transect_ids)
    priority_transects: list[str] = field(default_factory=list)

    # Geographic bounds (for NWS alert filtering)
    bounds: dict[str, float] = field(default_factory=dict)  # n, s, e, w

    # State(s) for NWS alert queries
    alert_states: list[str] = field(default_factory=lambda: ["OR"])

    @property
    def center(self) -> tuple[float, float]:
        """Geographic center of zone based on bounds."""
        if self.bounds:
            lat = (self.bounds["n"] + self.bounds["s"]) / 2
            lon = (self.bounds["e"] + self.bounds["w"]) / 2
            return (lat, lon)
        # Fallback: average of town coordinates
        if self.towns:
            lats = [c[0] for c in self.towns.values()]
            lons = [c[1] for c in self.towns.values()]
            return (sum(lats) / len(lats), sum(lons) / len(lons))
        return (44.0, -121.0)  # Oregon center

    @property
    def town_count(self) -> int:
        return len(self.towns)

    @property
    def transect_count(self) -> int:
        return len(self.transect_ids)


@dataclass
class AgentResult:
    """Result from a single agent execution."""

    agent_name: str
    tier: int
    success: bool
    data: dict = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    elapsed_seconds: float = 0.0

    @property
    def summary(self) -> str:
        status = "OK" if self.success else "FAILED"
        return f"[T{self.tier}] {self.agent_name}: {status} ({self.elapsed_seconds:.1f}s)"


@dataclass
class TierResult:
    """Result from an entire tier of agents."""

    tier: int
    agent_results: list[AgentResult] = field(default_factory=list)
    elapsed_seconds: float = 0.0

    @property
    def success(self) -> bool:
        return all(r.success for r in self.agent_results)

    @property
    def failed_agents(self) -> list[str]:
        return [r.agent_name for r in self.agent_results if not r.success]

    @property
    def summary(self) -> str:
        ok = sum(1 for r in self.agent_results if r.success)
        total = len(self.agent_results)
        return f"Tier {self.tier}: {ok}/{total} agents OK ({self.elapsed_seconds:.1f}s)"
