"""
Tier 2: Cross-Section Analysis Agents (6 agents)

These agents generate cross-section imagery and data for all zone transects.
They depend on Tier 1 completing (for cycle resolution) but run in parallel
with each other.

Agents:
    6-9.  XsGenerator (x4)  — generate cross-section PNGs for assigned transects
    10.   GifGenerator       — generate animated GIFs for priority transects
    11.   ModelComparator    — compare HRRR vs GFS on key transects
"""
import logging
import math
import os
import time
import traceback
from typing import Optional

from tools.agent_tools.wfo_swarm.zone_state import ZoneState
from tools.agent_tools.wfo_swarm.config import AgentResult

logger = logging.getLogger(__name__)


# =============================================================================
# Agent 6-9: Cross-Section Generator (parameterized by transect subset)
# =============================================================================

class XsGenerator:
    """Generates cross-section PNG images for assigned transects."""

    TIER = 2

    def __init__(self, worker_id: int, transect_ids: list[str]):
        self.worker_id = worker_id
        self.transect_ids = transect_ids
        self.NAME = f"xs_generator_{worker_id}"

    def run(self, state: ZoneState, zone_config, swarm_config) -> AgentResult:
        t0 = time.time()
        errors = []
        data = {"images_generated": 0, "transects_processed": []}

        try:
            from tools.agent_tools.cross_section import CrossSectionTool
            from tools.agent_tools.data.oregon_transects import get_transect

            xs_tool = CrossSectionTool(base_url=swarm_config.api_base)

            output_dir = os.path.join(
                swarm_config.output_dir, state.zone_id, state.cycle, "xs"
            )
            os.makedirs(output_dir, exist_ok=True)

            for tid in self.transect_ids:
                try:
                    transect = get_transect(tid)
                    start = tuple(transect["start"])
                    end = tuple(transect["end"])

                    # Generate images for each product x FHR combination
                    images = xs_tool.batch_images(
                        transects=[{"name": tid, "start": start, "end": end}],
                        cycle=state.cycle,
                        fhrs=swarm_config.fhrs,
                        products=swarm_config.products,
                        output_dir=output_dir,
                        prefix="",
                        y_top=swarm_config.y_top,
                    )

                    state.xs_images[tid] = images if images else []
                    data["images_generated"] += len(images) if images else 0
                    data["transects_processed"].append(tid)

                except Exception as e:
                    errors.append(f"XS {tid}: {e}")
                    state.xs_images[tid] = []

        except Exception as e:
            errors.append(f"XsGenerator-{self.worker_id}: {traceback.format_exc()}")

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=data["images_generated"] > 0 or len(errors) == 0,
            data=data,
            errors=errors,
            elapsed_seconds=elapsed,
        )


# =============================================================================
# Agent 10: GIF Generator
# =============================================================================

class GifGenerator:
    """Generates animated GIFs for priority transects (temporal evolution)."""

    TIER = 2
    NAME = "gif_generator"

    def run(self, state: ZoneState, zone_config, swarm_config) -> AgentResult:
        t0 = time.time()
        errors = []
        data = {"gifs_generated": 0}

        if not swarm_config.generate_gifs:
            elapsed = time.time() - t0
            return AgentResult(
                agent_name=self.NAME, tier=self.TIER, success=True,
                data={"gifs_generated": 0, "skipped": True},
                elapsed_seconds=elapsed,
            )

        try:
            from tools.agent_tools.cross_section import CrossSectionTool
            from tools.agent_tools.data.oregon_transects import get_transect

            xs_tool = CrossSectionTool(base_url=swarm_config.api_base)

            output_dir = os.path.join(
                swarm_config.output_dir, state.zone_id, state.cycle, "gifs"
            )
            os.makedirs(output_dir, exist_ok=True)

            # Only generate GIFs for priority transects
            for tid in zone_config.priority_transects:
                try:
                    transect = get_transect(tid)
                    start = tuple(transect["start"])
                    end = tuple(transect["end"])

                    # Use fire_wx product for GIFs (most useful for fire weather)
                    gif_path = os.path.join(output_dir, f"{tid}_fire_wx.gif")

                    # Generate via dashboard API
                    import urllib.request
                    import urllib.parse

                    params = {
                        "model": "hrrr",
                        "cycle": state.cycle,
                        "product": "fire_wx",
                        "start_lat": start[0],
                        "start_lon": start[1],
                        "end_lat": end[0],
                        "end_lon": end[1],
                        "y_top": swarm_config.y_top,
                        "fhr_min": swarm_config.gif_fhr_min,
                        "fhr_max": swarm_config.gif_fhr_max,
                    }
                    qs = urllib.parse.urlencode(params)
                    url = f"{swarm_config.api_base}/api/v1/cross-section/gif?{qs}"

                    req = urllib.request.Request(url)
                    with urllib.request.urlopen(req, timeout=180) as resp:
                        gif_data = resp.read()

                    with open(gif_path, "wb") as f:
                        f.write(gif_data)

                    state.gif_paths[tid] = gif_path
                    data["gifs_generated"] += 1

                except Exception as e:
                    errors.append(f"GIF {tid}: {e}")

        except Exception as e:
            errors.append(f"GifGenerator: {traceback.format_exc()}")

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=data["gifs_generated"] > 0 or len(errors) == 0,
            data=data,
            errors=errors,
            elapsed_seconds=elapsed,
        )


# =============================================================================
# Agent 11: Model Comparator
# =============================================================================

class ModelComparator:
    """Compares HRRR vs GFS cross-sections on key transects."""

    TIER = 2
    NAME = "model_comparator"

    def run(self, state: ZoneState, zone_config, swarm_config) -> AgentResult:
        t0 = time.time()
        errors = []
        data = {"comparisons": 0}

        try:
            from tools.agent_tools.cross_section import CrossSectionTool
            from tools.agent_tools.data.oregon_transects import get_transect

            xs_tool = CrossSectionTool(base_url=swarm_config.api_base)

            # Compare HRRR vs GFS on priority transects at key FHRs
            compare_fhrs = [6, 12, 18, 24]  # key forecast hours
            compare_fhrs = [f for f in compare_fhrs if f in swarm_config.fhrs]

            for tid in zone_config.priority_transects[:2]:  # limit to top 2
                try:
                    transect = get_transect(tid)
                    start = tuple(transect["start"])
                    end = tuple(transect["end"])

                    comparison = {}
                    for fhr in compare_fhrs:
                        fhr_comp = {}
                        for model in ("hrrr", "gfs"):
                            try:
                                xs_data = xs_tool.get_data(
                                    start=start, end=end,
                                    cycle=state.cycle, fhr=fhr,
                                    product="wind_speed",
                                )
                                if xs_data and hasattr(xs_data, "surface_stats"):
                                    fhr_comp[model] = xs_data.surface_stats()
                                elif isinstance(xs_data, dict):
                                    fhr_comp[model] = xs_data
                            except Exception as e:
                                fhr_comp[model] = {"error": str(e)}

                        comparison[f"F{fhr:02d}"] = fhr_comp

                    state.model_comparison[tid] = comparison
                    data["comparisons"] += 1

                except Exception as e:
                    errors.append(f"Comparison {tid}: {e}")

        except Exception as e:
            errors.append(f"ModelComparator: {traceback.format_exc()}")

        elapsed = time.time() - t0
        state.agent_timings[self.NAME] = elapsed
        return AgentResult(
            agent_name=self.NAME,
            tier=self.TIER,
            success=True,  # comparison is optional
            data=data,
            errors=errors,
            elapsed_seconds=elapsed,
        )


# =============================================================================
# Tier 2 runner
# =============================================================================

def run_tier2(state: ZoneState, zone_config, swarm_config, max_workers: int = 6) -> list[AgentResult]:
    """Run all Tier 2 agents concurrently."""
    from concurrent.futures import ThreadPoolExecutor, as_completed

    # Split transects across 2 XS generator workers (limited to avoid overwhelming dashboard)
    all_transects = zone_config.transect_ids
    n_workers = min(2, len(all_transects))
    chunks = [[] for _ in range(n_workers)]
    for i, tid in enumerate(all_transects):
        chunks[i % n_workers].append(tid)

    agents = []
    for i, chunk in enumerate(chunks):
        if chunk:
            agents.append(XsGenerator(worker_id=i + 1, transect_ids=chunk))

    agents.append(GifGenerator())
    agents.append(ModelComparator())

    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {}
        for agent in agents:
            future = pool.submit(agent.run, state, zone_config, swarm_config)
            futures[future] = agent.NAME

        for future in as_completed(futures):
            name = futures[future]
            try:
                result = future.result(timeout=300)
                results.append(result)
                logger.info(result.summary)
            except Exception as e:
                results.append(AgentResult(
                    agent_name=name, tier=2, success=False,
                    errors=[str(e)],
                ))

    return results
