"""
SwarmScheduler — Multi-zone scheduler that watches for new HRRR cycles.

Launches staggered zone swarms when new HRRR data becomes available.
Manages concurrency across zones and tracks pipeline status.

Usage:
    from tools.agent_tools.wfo_swarm.scheduler import SwarmScheduler

    # Run all zones for a specific cycle
    scheduler = SwarmScheduler()
    results = scheduler.run_all_zones("20260211_12z")

    # Run continuously (watches for new cycles)
    scheduler.start()  # blocks, runs forever

    # Run a single zone
    result = scheduler.run_zone("OR-CENTCAS", "latest")
"""
import json
import logging
import os
import time
import threading
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Optional

from tools.agent_tools.wfo_swarm.config import SwarmConfig
from tools.agent_tools.wfo_swarm.swarm import ZoneSwarm

logger = logging.getLogger(__name__)


# =============================================================================
# Persistent output store for MCP/API access
# =============================================================================

class OutputStore:
    """Thread-safe store for zone bulletins and status."""

    def __init__(self):
        self._lock = threading.Lock()
        self._bulletins: dict[str, dict] = {}  # zone_id -> latest bulletin
        self._status: dict[str, dict] = {}     # zone_id -> run status
        self._last_cycle: str = ""

    def update_bulletin(self, zone_id: str, bulletin: dict):
        with self._lock:
            self._bulletins[zone_id] = bulletin

    def get_bulletin(self, zone_id: str) -> dict | None:
        with self._lock:
            return self._bulletins.get(zone_id)

    def update_status(self, zone_id: str, status: dict):
        with self._lock:
            self._status[zone_id] = status

    def get_status(self, zone_id: str = None) -> dict:
        with self._lock:
            if zone_id:
                return self._status.get(zone_id, {})
            return dict(self._status)

    def get_all_bulletins(self) -> dict[str, dict]:
        with self._lock:
            return dict(self._bulletins)

    @property
    def last_cycle(self) -> str:
        with self._lock:
            return self._last_cycle

    @last_cycle.setter
    def last_cycle(self, value: str):
        with self._lock:
            self._last_cycle = value

    def load_from_disk(self, output_dir: str = "output/oregon_wfo"):
        """Load latest bulletins from disk (for cold-start / cross-process access)."""
        from tools.agent_tools.data.oregon_zones import OREGON_ZONES

        if not os.path.isabs(output_dir):
            output_dir = os.path.join(
                os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
                output_dir,
            )

        loaded = 0
        latest_cycle = ""
        for zone_id in OREGON_ZONES:
            zone_dir = os.path.join(output_dir, zone_id)
            if not os.path.isdir(zone_dir):
                continue
            # Find the most recent cycle directory
            cycles = sorted(
                [d for d in os.listdir(zone_dir) if os.path.isdir(os.path.join(zone_dir, d))],
                reverse=True,
            )
            for cycle_dir in cycles:
                bulletin_path = os.path.join(zone_dir, cycle_dir, "bulletin.json")
                if os.path.isfile(bulletin_path):
                    try:
                        with open(bulletin_path, "r") as f:
                            bulletin = json.load(f)
                        self.update_bulletin(zone_id, bulletin)
                        self.update_status(zone_id, {
                            "status": "complete",
                            "cycle": cycle_dir,
                            "loaded_from_disk": True,
                        })
                        loaded += 1
                        if cycle_dir > latest_cycle:
                            latest_cycle = cycle_dir
                    except Exception as e:
                        logger.warning(f"Failed to load bulletin {bulletin_path}: {e}")
                    break  # only load the latest cycle per zone

        if latest_cycle:
            self.last_cycle = latest_cycle
        logger.info(f"OutputStore: loaded {loaded} bulletins from disk (cycle: {latest_cycle})")
        return loaded


# Global output store — accessible by MCP tools and API endpoints
output_store = OutputStore()
output_store.load_from_disk()  # Auto-load any existing bulletins on import


# =============================================================================
# SwarmScheduler
# =============================================================================

class SwarmScheduler:
    """Manages multi-zone swarm execution."""

    def __init__(self, config: Optional[SwarmConfig] = None):
        self.config = config or SwarmConfig()
        self._running = False
        self._last_cycle = ""

    def run_zone(self, zone_id: str, cycle: str = "latest") -> dict:
        """Run a single zone swarm and return the bulletin."""
        logger.info(f"Running zone {zone_id} for cycle {cycle}")

        output_store.update_status(zone_id, {
            "status": "running",
            "started_at": time.time(),
            "cycle": cycle,
        })

        try:
            swarm = ZoneSwarm(zone_id, config=self.config)
            state = swarm.run_cycle(cycle)

            # Store results
            output_store.update_bulletin(zone_id, state.bulletin)
            output_store.update_status(zone_id, {
                "status": "complete",
                "cycle": state.cycle,
                "elapsed": state.elapsed,
                "error_count": len(state.errors),
                "town_count": len(state.town_forecasts),
                "completed_at": time.time(),
            })

            return state.bulletin

        except Exception as e:
            logger.error(f"Zone {zone_id} failed: {e}")
            output_store.update_status(zone_id, {
                "status": "failed",
                "error": str(e),
                "cycle": cycle,
            })
            return {"error": str(e), "zone_id": zone_id}

    def run_all_zones(self, cycle: str = "latest") -> dict[str, dict]:
        """Run all Oregon zones with staggered launches."""
        from tools.agent_tools.data.oregon_zones import OREGON_ZONES

        zone_ids = self.config.zones or list(OREGON_ZONES.keys())
        logger.info(f"Running {len(zone_ids)} zones for cycle {cycle}")

        results = {}
        stagger = self.config.zone_stagger_seconds

        with ThreadPoolExecutor(max_workers=self.config.max_concurrent_zones) as pool:
            futures = {}
            for i, zone_id in enumerate(zone_ids):
                # Stagger launches
                if i > 0 and stagger > 0:
                    time.sleep(stagger)

                future = pool.submit(self.run_zone, zone_id, cycle)
                futures[future] = zone_id

            for future in as_completed(futures):
                zone_id = futures[future]
                try:
                    results[zone_id] = future.result(timeout=self.config.zone_timeout)
                except Exception as e:
                    results[zone_id] = {"error": str(e), "zone_id": zone_id}

        output_store.last_cycle = cycle
        logger.info(f"All zones complete for cycle {cycle}")
        return results

    def get_latest_hrrr_cycle(self) -> str | None:
        """Check dashboard for latest available HRRR cycle."""
        try:
            url = f"{self.config.api_base}/api/v1/cycles"
            req = urllib.request.Request(url, headers={"User-Agent": "wfo-swarm/1.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read())

            cycles = data if isinstance(data, list) else data.get("cycles", [])
            for entry in cycles:
                if isinstance(entry, dict):
                    key = entry.get("cycle_key", entry.get("key", ""))
                    model = entry.get("model", "")
                    if "hrrr" in model.lower() or "hrrr" in key.lower():
                        return key
                elif isinstance(entry, str) and "hrrr" in entry.lower():
                    return entry

            # Return first available cycle
            if cycles:
                entry = cycles[0]
                if isinstance(entry, dict):
                    return entry.get("cycle_key", entry.get("key", ""))
                return entry

        except Exception as e:
            logger.debug(f"Could not check cycles: {e}")

        return None

    def start(self, poll_interval: int = 300):
        """Start continuous cycle monitoring. Blocks forever.

        Checks for new HRRR cycles every poll_interval seconds (default 5 min).
        When a new cycle is detected, runs all zones.
        """
        self._running = True
        logger.info("SwarmScheduler starting continuous mode")
        logger.info(f"Poll interval: {poll_interval}s")

        while self._running:
            try:
                latest = self.get_latest_hrrr_cycle()
                if latest and latest != self._last_cycle:
                    logger.info(f"New cycle detected: {latest}")
                    self.run_all_zones(latest)
                    self._last_cycle = latest
                else:
                    logger.debug(f"No new cycle (current: {self._last_cycle})")
            except Exception as e:
                logger.error(f"Scheduler loop error: {e}")

            time.sleep(poll_interval)

    def stop(self):
        """Stop the scheduler loop."""
        self._running = False
        logger.info("SwarmScheduler stopping")


# =============================================================================
# Convenience functions for MCP/API access
# =============================================================================

def get_zone_bulletin(zone_id: str) -> dict | None:
    """Get the latest bulletin for a zone (from output store)."""
    return output_store.get_bulletin(zone_id)


def get_zone_town_forecast(zone_id: str, town: str) -> dict | None:
    """Get a specific town's forecast from the latest bulletin."""
    bulletin = output_store.get_bulletin(zone_id)
    if not bulletin:
        return None
    forecasts = bulletin.get("town_forecasts", {})
    # Case-insensitive match
    for t, f in forecasts.items():
        if t.lower() == town.lower():
            return f
    return None


def get_zone_risk_ranking(zone_id: str) -> list | None:
    """Get the risk ranking for a zone."""
    bulletin = output_store.get_bulletin(zone_id)
    if not bulletin:
        return None
    return bulletin.get("risk_summary", {}).get("ranking")


def get_zone_discussion(zone_id: str) -> str | None:
    """Get the zone discussion text."""
    bulletin = output_store.get_bulletin(zone_id)
    if not bulletin:
        return None
    return bulletin.get("zone_discussion")


def oregon_fire_scan() -> dict:
    """Quick scan across all 7 zones — returns highest risk per zone."""
    from tools.agent_tools.data.oregon_zones import OREGON_ZONES

    scan = {}
    for zone_id in OREGON_ZONES:
        bulletin = output_store.get_bulletin(zone_id)
        if bulletin:
            scan[zone_id] = {
                "headline": bulletin.get("headline", ""),
                "max_risk_level": bulletin.get("max_risk_level", "UNKNOWN"),
                "cycle": bulletin.get("cycle", ""),
                "top_concern": bulletin.get("risk_summary", {}).get("top_concern"),
            }
        else:
            status = output_store.get_status(zone_id)
            scan[zone_id] = {
                "headline": "No data available",
                "max_risk_level": "UNKNOWN",
                "status": status.get("status", "not_run"),
            }
    return scan


def oregon_state_bulletin() -> dict:
    """State-level aggregated bulletin across all zones."""
    from tools.agent_tools.data.oregon_zones import OREGON_ZONES

    zones_data = {}
    all_rankings = []
    max_level = "LOW"
    level_order = {"CRITICAL": 4, "ELEVATED": 3, "MODERATE": 2, "LOW": 1, "UNKNOWN": 0}

    for zone_id in OREGON_ZONES:
        bulletin = output_store.get_bulletin(zone_id)
        if bulletin:
            zones_data[zone_id] = {
                "headline": bulletin.get("headline", ""),
                "max_risk_level": bulletin.get("max_risk_level", "UNKNOWN"),
                "town_count": len(bulletin.get("town_forecasts", {})),
            }
            ranking = bulletin.get("risk_summary", {}).get("ranking", [])
            for r in ranking:
                r["zone_id"] = zone_id
                all_rankings.append(r)

            zone_level = bulletin.get("max_risk_level", "LOW")
            if level_order.get(zone_level, 0) > level_order.get(max_level, 0):
                max_level = zone_level

    # Sort all towns by risk
    all_rankings.sort(key=lambda x: x.get("score", 0), reverse=True)

    return {
        "type": "oregon_state_bulletin",
        "issued": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "cycle": output_store.last_cycle,
        "max_risk_level": max_level,
        "zones": zones_data,
        "statewide_ranking": all_rankings[:20],  # top 20 towns
        "zone_count": len(zones_data),
        "total_towns": sum(z.get("town_count", 0) for z in zones_data.values()),
    }


def get_swarm_status() -> dict:
    """Get pipeline status for all zones."""
    from tools.agent_tools.data.oregon_zones import OREGON_ZONES

    return {
        "zones": {
            zone_id: output_store.get_status(zone_id) or {"status": "not_run"}
            for zone_id in OREGON_ZONES
        },
        "last_cycle": output_store.last_cycle,
        "zone_count": len(OREGON_ZONES),
    }
