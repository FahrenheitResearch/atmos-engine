"""
ZoneSwarm — Orchestrates 22 agents across 5 tiers for one zone.

Manages the barrier-synchronized execution: each tier must complete
before the next begins. Within each tier, agents run concurrently.

Usage:
    from tools.agent_tools.wfo_swarm.swarm import ZoneSwarm

    swarm = ZoneSwarm("OR-CENTCAS")
    result = swarm.run_cycle("latest")
    print(result.summary())
"""
import json
import logging
import os
import time
import uuid
import urllib.request
from typing import Optional

from tools.agent_tools.wfo_swarm.config import SwarmConfig, TierResult
from tools.agent_tools.wfo_swarm.zone_state import ZoneState

logger = logging.getLogger(__name__)


class ZoneSwarm:
    """Orchestrates all 22 agents for a single zone."""

    def __init__(self, zone_id: str, config: Optional[SwarmConfig] = None):
        self.zone_id = zone_id
        self.config = config or SwarmConfig()
        self._zone_config = None

    @property
    def zone_config(self):
        if self._zone_config is None:
            from tools.agent_tools.data.oregon_zones import get_zone
            self._zone_config = get_zone(self.zone_id)
        return self._zone_config

    def resolve_cycle(self, cycle: str = "latest") -> str:
        """Resolve 'latest' to an actual cycle key."""
        if cycle != "latest":
            return cycle
        try:
            url = f"{self.config.api_base}/api/v1/cycles"
            req = urllib.request.Request(url, headers={"User-Agent": "wfo-swarm/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read())
            # Find latest HRRR cycle
            for entry in data if isinstance(data, list) else data.get("cycles", []):
                if isinstance(entry, dict):
                    key = entry.get("cycle_key", entry.get("key", ""))
                    if key:
                        return key
                elif isinstance(entry, str):
                    return entry
        except Exception as e:
            logger.warning(f"Could not resolve 'latest' cycle: {e}")
        return cycle

    def resolve_available_fhrs(self, cycle: str) -> list[int]:
        """Query dashboard for which FHRs are actually available in this cycle."""
        try:
            url = f"{self.config.api_base}/api/v1/cycles"
            req = urllib.request.Request(url, headers={"User-Agent": "wfo-swarm/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read())
            cycles_list = data if isinstance(data, list) else data.get("cycles", [])
            for entry in cycles_list:
                if isinstance(entry, dict):
                    key = entry.get("cycle_key", entry.get("key", ""))
                    if key == cycle:
                        return sorted(entry.get("forecast_hours", []))
        except Exception as e:
            logger.warning(f"Could not resolve available FHRs: {e}")
        return self.config.fhrs  # fallback to config default

    def run_cycle(self, cycle: str = "latest") -> ZoneState:
        """Run the full 22-agent pipeline for one HRRR cycle.

        Returns the completed ZoneState with all data populated.
        """
        resolved_cycle = self.resolve_cycle(cycle)

        # Auto-detect available FHRs — use a per-run copy to avoid mutating shared config
        import copy
        self.config = copy.copy(self.config)
        available_fhrs = self.resolve_available_fhrs(resolved_cycle)
        self.config.fhrs = [f for f in self.config.fhrs if f in available_fhrs]
        if not self.config.fhrs:
            self.config.fhrs = available_fhrs

        run_id = f"{self.zone_id}_{resolved_cycle}_{uuid.uuid4().hex[:8]}"

        state = ZoneState(
            zone_id=self.zone_id,
            cycle=resolved_cycle,
            run_id=run_id,
        )

        logger.info(f"Starting swarm: {run_id}")
        logger.info(f"Zone: {self.zone_id} ({self.zone_config.name})")
        logger.info(f"Cycle: {resolved_cycle} ({len(self.config.fhrs)} FHRs available)")
        logger.info(f"Towns: {self.zone_config.town_count}, Transects: {self.zone_config.transect_count}")

        tier_results = []

        # ── Tier 1: Data Acquisition ──────────────────────────────────────
        tier_results.append(self._run_tier(1, state))

        # ── Tier 2: Cross-Section Analysis ────────────────────────────────
        tier_results.append(self._run_tier(2, state))

        # ── Tier 3: Assessment ────────────────────────────────────────────
        tier_results.append(self._run_tier(3, state))

        # ── Tier 4: Synthesis ─────────────────────────────────────────────
        tier_results.append(self._run_tier(4, state))

        # ── Tier 5: Output ────────────────────────────────────────────────
        tier_results.append(self._run_tier(5, state))

        # Log summary
        logger.info(f"Swarm complete: {state.summary()}")
        for tr in tier_results:
            logger.info(f"  {tr.summary}")

        return state

    def _run_tier(self, tier_num: int, state: ZoneState) -> TierResult:
        """Run a single tier and record timing."""
        t0 = time.time()
        logger.info(f"=== Tier {tier_num} starting ===")

        try:
            if tier_num == 1:
                from tools.agent_tools.wfo_swarm.agents.data_acquisition import run_tier1
                agent_results = run_tier1(
                    state, self.zone_config,
                    max_workers=min(5, self.config.max_tier_workers),
                )
            elif tier_num == 2:
                from tools.agent_tools.wfo_swarm.agents.cross_section import run_tier2
                agent_results = run_tier2(
                    state, self.zone_config, self.config,
                    max_workers=min(6, self.config.max_tier_workers),
                )
            elif tier_num == 3:
                from tools.agent_tools.wfo_swarm.agents.assessment import run_tier3
                agent_results = run_tier3(
                    state, self.zone_config, self.config,
                    max_workers=min(5, self.config.max_tier_workers),
                )
            elif tier_num == 4:
                from tools.agent_tools.wfo_swarm.agents.synthesis import run_tier4
                agent_results = run_tier4(
                    state, self.zone_config, self.config,
                    max_workers=min(4, self.config.max_tier_workers),
                )
            elif tier_num == 5:
                from tools.agent_tools.wfo_swarm.agents.output import run_tier5
                agent_results = run_tier5(state, self.zone_config, self.config)
            else:
                agent_results = []

        except Exception as e:
            logger.error(f"Tier {tier_num} failed: {e}")
            state.add_error(f"tier_{tier_num}", tier_num, str(e))
            agent_results = []

        elapsed = time.time() - t0
        state.tier_timings[tier_num] = elapsed

        tier_result = TierResult(
            tier=tier_num,
            agent_results=agent_results,
            elapsed_seconds=elapsed,
        )

        # Log any failures
        failed = tier_result.failed_agents
        if failed:
            logger.warning(f"Tier {tier_num} failures: {failed}")
            for agent_name in failed:
                for ar in agent_results:
                    if ar.agent_name == agent_name and ar.errors:
                        for err in ar.errors[:3]:
                            state.add_error(agent_name, tier_num, err)

        logger.info(f"=== {tier_result.summary} ===")
        return tier_result

    def run_quick(self, cycle: str = "latest") -> dict:
        """Run the swarm and return just the bulletin dict."""
        state = self.run_cycle(cycle)
        return state.bulletin
