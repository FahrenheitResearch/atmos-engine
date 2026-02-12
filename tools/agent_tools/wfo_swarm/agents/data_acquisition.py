"""
Tier 1: Data Acquisition Agents (5 agents)

These agents run first, in parallel, to gather all external data needed
by downstream tiers. Each agent writes to a specific section of ZoneState.

Agents:
    1. MetarObserver      — get_metar, find_stations for all zone stations
    2. RawsObserver       — get_raws for fire weather stations in zone
    3. NwsMonitor         — get_nws_alerts, get_forecast_discussion
    4. SpcMonitor         — get_spc_fire_outlook, get_spc_discussion
    5. ModelIngestor      — get_point_forecast for all zone towns (HRRR + GFS)
"""
import logging
import time
import traceback
import urllib.request
import urllib.error
import json
from typing import Optional

from tools.agent_tools.wfo_swarm.zone_state import ZoneState
from tools.agent_tools.wfo_swarm.config import AgentResult

logger = logging.getLogger(__name__)

API_BASE = "http://127.0.0.1:5565"


# =============================================================================
# Shared helpers
# =============================================================================

def _api_get(path: str, params: dict = None, timeout: int = 60) -> dict:
    """GET from dashboard API."""
    url = API_BASE + path
    if params:
        qs = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
        url += "?" + qs
    req = urllib.request.Request(url, headers={"User-Agent": "wfo-swarm/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read())
    except Exception as e:
        return {"error": str(e)}


# =============================================================================
# Agent 1: METAR Observer
# =============================================================================

class MetarObserver:
    """Fetches METAR observations for all stations in the zone."""

    TIER = 1
    NAME = "metar_observer"

    def run(self, state: ZoneState, zone_config) -> AgentResult:
        t0 = time.time()
        errors = []
        data = {}

        try:
            from tools.agent_tools.external_data import (
                get_metar_observations,
                get_nearby_stations,
            )

            # Fetch from listed METAR stations
            if zone_config.metar_stations:
                obs = get_metar_observations(
                    stations=zone_config.metar_stations,
                    hours_back=3,
                )
                if isinstance(obs, dict) and "data" in obs:
                    for ob in obs["data"]:
                        sid = ob.get("station", "unknown")
                        state.metar_obs[sid] = ob
                        data[sid] = {
                            "tmpf": ob.get("tmpf"),
                            "dwpf": ob.get("dwpf"),
                            "relh": ob.get("relh"),
                            "sknt": ob.get("sknt"),
                            "drct": ob.get("drct"),
                            "gust": ob.get("gust_sknt"),
                            "valid": ob.get("valid"),
                        }
                elif isinstance(obs, dict) and "error" in obs:
                    errors.append(f"METAR fetch: {obs['error']}")

            # Also search for nearby stations around zone center
            center = zone_config.center
            try:
                nearby = get_nearby_stations(center[0], center[1], radius_km=80)
                if isinstance(nearby, dict) and "stations" in nearby:
                    # Add any stations we don't already have
                    extra_ids = [
                        s["id"] for s in nearby["stations"]
                        if s["id"] not in zone_config.metar_stations
                    ][:5]  # limit to 5 extra
                    if extra_ids:
                        extra_obs = get_metar_observations(
                            stations=extra_ids, hours_back=3
                        )
                        if isinstance(extra_obs, dict) and "data" in extra_obs:
                            for ob in extra_obs["data"]:
                                sid = ob.get("station", "unknown")
                                state.metar_obs[sid] = ob
            except Exception as e:
                errors.append(f"Nearby station search: {e}")

        except Exception as e:
            errors.append(f"MetarObserver: {traceback.format_exc()}")

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=len(errors) == 0 or len(state.metar_obs) > 0,
            data=data,
            errors=errors,
            elapsed_seconds=elapsed,
        )


# =============================================================================
# Agent 2: RAWS Observer
# =============================================================================

class RawsObserver:
    """Fetches RAWS fire weather station observations for the zone."""

    TIER = 1
    NAME = "raws_observer"

    def run(self, state: ZoneState, zone_config) -> AgentResult:
        t0 = time.time()
        errors = []
        data = {}

        try:
            from tools.agent_tools.external_data import get_raws_observations

            for lat, lon, radius_km in zone_config.raws_search_points:
                try:
                    obs = get_raws_observations(lat=lat, lon=lon, radius_miles=round(radius_km * 0.621, 1), hours_back=6)
                    if isinstance(obs, dict) and "stations" in obs:
                        for stn in obs["stations"]:
                            name = stn.get("name", f"RAWS_{lat}_{lon}")
                            state.raws_obs[name] = stn
                            data[name] = {
                                "air_temp_f": stn.get("air_temp_f"),
                                "rh": stn.get("relative_humidity"),
                                "wind_speed_mph": stn.get("wind_speed_mph"),
                                "wind_dir": stn.get("wind_direction"),
                                "fuel_moisture_10hr": stn.get("fuel_moisture_10hr"),
                            }
                    elif isinstance(obs, dict) and "error" in obs:
                        errors.append(f"RAWS at ({lat},{lon}): {obs['error']}")
                except Exception as e:
                    errors.append(f"RAWS at ({lat},{lon}): {e}")

        except Exception as e:
            errors.append(f"RawsObserver: {traceback.format_exc()}")

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=len(errors) == 0 or len(state.raws_obs) > 0,
            data=data,
            errors=errors,
            elapsed_seconds=elapsed,
        )


# =============================================================================
# Agent 3: NWS Monitor
# =============================================================================

class NwsMonitor:
    """Fetches NWS alerts and forecast discussion for the zone."""

    TIER = 1
    NAME = "nws_monitor"

    def run(self, state: ZoneState, zone_config) -> AgentResult:
        t0 = time.time()
        errors = []
        data = {}

        try:
            from tools.agent_tools.external_data import get_nws_alerts

            # Get alerts for each state in zone
            all_alerts = []
            for alert_state in zone_config.alert_states:
                try:
                    alerts = get_nws_alerts(state=alert_state)
                    if isinstance(alerts, dict) and "features" in alerts:
                        # Filter to alerts relevant to zone bounds
                        for feat in alerts["features"]:
                            all_alerts.append(feat)
                    elif isinstance(alerts, dict) and "error" in alerts:
                        errors.append(f"NWS alerts ({alert_state}): {alerts['error']}")
                except Exception as e:
                    errors.append(f"NWS alerts ({alert_state}): {e}")

            state.nws_alerts = all_alerts
            data["alert_count"] = len(all_alerts)
            data["alert_types"] = list(set(
                a.get("properties", {}).get("event", "unknown")
                for a in all_alerts
            ))

            # Get forecast discussion from each WFO
            discussions = []
            for wfo in zone_config.wfos:
                try:
                    url = f"https://api.weather.gov/products/types/AFD/locations/{wfo}"
                    req = urllib.request.Request(url, headers={
                        "User-Agent": "wxsection-wfo-swarm/1.0",
                        "Accept": "application/geo+json",
                    })
                    with urllib.request.urlopen(req, timeout=30) as resp:
                        products = json.loads(resp.read())
                    if products.get("@graph"):
                        latest_url = products["@graph"][0].get("@id", "")
                        if latest_url:
                            req2 = urllib.request.Request(latest_url, headers={
                                "User-Agent": "wxsection-wfo-swarm/1.0",
                            })
                            with urllib.request.urlopen(req2, timeout=30) as resp2:
                                product_data = json.loads(resp2.read())
                            discussions.append(
                                product_data.get("productText", "")
                            )
                except Exception as e:
                    errors.append(f"AFD from {wfo}: {e}")

            state.nws_discussion = "\n\n---\n\n".join(discussions)
            data["discussion_wfos"] = zone_config.wfos
            data["discussion_length"] = len(state.nws_discussion)

        except Exception as e:
            errors.append(f"NwsMonitor: {traceback.format_exc()}")

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=True,  # alerts may legitimately be empty
            data=data,
            errors=errors,
            elapsed_seconds=elapsed,
        )


# =============================================================================
# Agent 4: SPC Monitor
# =============================================================================

class SpcMonitor:
    """Fetches SPC fire weather outlook and discussion."""

    TIER = 1
    NAME = "spc_monitor"

    def run(self, state: ZoneState, zone_config) -> AgentResult:
        t0 = time.time()
        errors = []
        data = {}

        try:
            from tools.agent_tools.external_data import (
                get_spc_fire_weather_outlook,
                get_spc_fire_discussion,
            )

            # Day 1 fire outlook
            try:
                outlook = get_spc_fire_weather_outlook(day=1)
                if isinstance(outlook, dict):
                    state.spc_fire_outlook = outlook
                    data["fire_outlook_areas"] = len(
                        outlook.get("features", [])
                    )
            except Exception as e:
                errors.append(f"SPC outlook: {e}")

            # Fire weather discussion
            try:
                discussion = get_spc_fire_discussion()
                if isinstance(discussion, str):
                    state.spc_discussion = discussion
                    data["discussion_length"] = len(discussion)
                elif isinstance(discussion, dict) and "text" in discussion:
                    state.spc_discussion = discussion["text"]
                    data["discussion_length"] = len(discussion["text"])
            except Exception as e:
                errors.append(f"SPC discussion: {e}")

        except Exception as e:
            errors.append(f"SpcMonitor: {traceback.format_exc()}")

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=True,  # SPC products may not be available
            data=data,
            errors=errors,
            elapsed_seconds=elapsed,
        )


# =============================================================================
# Agent 5: Model Ingestor
# =============================================================================

class ModelIngestor:
    """Fetches point forecast data (HRRR + GFS) for all zone towns."""

    TIER = 1
    NAME = "model_ingestor"

    def run(self, state: ZoneState, zone_config) -> AgentResult:
        t0 = time.time()
        errors = []
        data = {}

        try:
            for town_name, (lat, lon) in zone_config.towns.items():
                town_data = {}
                for model in ("hrrr", "gfs"):
                    try:
                        result = _api_get("/api/v1/data", {
                            "model": model,
                            "cycle": state.cycle,
                            "fhr": 0,
                            "product": "temperature",
                            "start_lat": lat,
                            "start_lon": lon,
                            "end_lat": lat + 0.01,
                            "end_lon": lon + 0.01,
                        })
                        if isinstance(result, dict) and "error" not in result:
                            town_data[model] = result
                        else:
                            err = result.get("error", "unknown") if isinstance(result, dict) else "bad response"
                            errors.append(f"{town_name}/{model}: {err}")
                    except Exception as e:
                        errors.append(f"{town_name}/{model}: {e}")

                state.model_points[town_name] = town_data
                data[town_name] = list(town_data.keys())

        except Exception as e:
            errors.append(f"ModelIngestor: {traceback.format_exc()}")

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=len(state.model_points) > 0,
            data=data,
            errors=errors,
            elapsed_seconds=elapsed,
        )


# =============================================================================
# Tier 1 runner
# =============================================================================

ALL_TIER1_AGENTS = [
    MetarObserver,
    RawsObserver,
    NwsMonitor,
    SpcMonitor,
    ModelIngestor,
]


def run_tier1(state: ZoneState, zone_config, max_workers: int = 5) -> list[AgentResult]:
    """Run all Tier 1 agents concurrently."""
    from concurrent.futures import ThreadPoolExecutor, as_completed

    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {}
        for agent_cls in ALL_TIER1_AGENTS:
            agent = agent_cls()
            future = pool.submit(agent.run, state, zone_config)
            futures[future] = agent.NAME

        for future in as_completed(futures):
            name = futures[future]
            try:
                result = future.result(timeout=120)
                results.append(result)
                logger.info(result.summary)
            except Exception as e:
                results.append(AgentResult(
                    agent_name=name, tier=1, success=False,
                    errors=[str(e)],
                ))

    return results
