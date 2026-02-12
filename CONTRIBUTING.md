# Contributing to wxsection.com (atmos-engine)

## What This Is

wxsection.com is a near-instant atmospheric cross-section tool supporting 6 NWP models (HRRR, GFS, RRFS, NAM, RAP, NAM-Nest). Users draw a line on a map and get a vertical cross-section in ~0.5s. It also generates map overlays, animated GIFs, multi-panel comparisons, and serves as the foundation for an AI agent swarm system designed for hyper-local fire weather surveillance.

The platform is **agent-native**: everything the web UI can do is also available via a free REST API and MCP tool servers at feature parity. The long-term vision is thousands of AI agents running every HRRR cycle, each forensically evaluating atmospheric conditions for specific towns and terrain features — so no community is too small to get personalized severe weather surveillance.

## Architecture Overview

```
tools/unified_dashboard.py      Flask server + Mapbox GL JS frontend + 58 API endpoints (~15,168 lines)
core/cross_section_interactive.py   Rendering engine (matplotlib, 0.5s warm renders) (~3,605 lines)
core/map_overlay.py             Map overlay composites (fill + contours + wind barbs) (~1,133 lines)
tools/auto_update.py            GRIB download daemon (slot-based concurrent) (~913 lines)
smart_hrrr/orchestrator.py      Parallel download with multi-layer validation (~311 lines)
model_config.py                 Model registry (6 models: HRRR/GFS/RRFS/NAM/RAP/NAM-Nest) (~320 lines)
tools/agent_tools/              Agent research platform (12 modules + 8 data files, ~57,500 lines)
tools/agent_tools/wfo_swarm/    Oregon WFO agent swarm pilot (7 zones, 154 agents, ~3,900 lines)
tools/mcp_server.py             MCP server — private (52 tools, stdio)
tools/mcp_public.py             MCP server — public (53 tools, SSE, API key auth)
```

### What Makes It Fast

Cross-sections are instant because of a mmap-on-NVMe caching architecture:

1. GRIB files are downloaded from NOMADS and converted once to per-field float16 numpy mmap files on NVMe
2. Cross-section interpolation reads **only the ~500 bytes needed** (the path points) from each mmap'd level via cached KDTree + fancy indexing — not the full 3.8MB 2D array
3. Frame cache stores pre-rendered PNGs for instant replay

The result is ~15ms interpolation + ~400ms matplotlib render = **~0.5s total**, vs 10-60s for typical on-demand GRIB parsing tools.

### Data Flow

```
NOMADS/AWS → auto_update.py (slot-based download) → outputs/model/date/cycle/FHR/
    → GRIB-to-mmap conversion (eccodes, ProcessPoolExecutor) → cache/xsect/
    → Cross-section render on request (matplotlib, ProcessPoolExecutor) → PNG
    → Frame cache (prerendered) → instant API response (~20ms)
```

### Models

| Model | Resolution | FHRs | Update | Notes |
|-------|-----------|------|--------|-------|
| HRRR | 3km | F00-F48 (synoptic), F00-F18 (hourly) | Every hour | Primary model, full field set |
| GFS | 0.25deg | F00-F384 (6h intervals) | Every 6h | CONUS subset, ~50MB/FHR |
| RRFS | 3km | F00-F18 (F00-F60 synoptic) | Every hour | HRRR successor (experimental) |
| NAM | 12km | F00-F84 | 00/06/12/18z | Wind via cfgrib fallback; missing q/cloud/dew_point |
| RAP | 13km | F00-F21 (F00-F51 extended) | Every hour | Wind via cfgrib fallback; missing q/cloud/dew_point |
| NAM-Nest | 3km | F00-F60 | 00/06/12/18z | Full field set, 926MB/FHR |

### Products

21 cross-section styles: temperature, wind_speed, theta_e, rh, omega, specific_humidity, vorticity, shear, lapse_rate, cloud, cloud_total, wetbulb, icing, frontogenesis, smoke (HRRR only), vpd, dewpoint_dep, moisture_transport, potential_vorticity, fire_wx, isentropic_ascent.

8 map overlay composites: surface_analysis, radar_composite, severe_weather, upper_500, upper_250, moisture, fire_weather, precip.

### Fire Weather Focus

The product is primarily directed at fire weather — that's why it has VPD, fire_wx composite, HDW index, and fuel/terrain/ignition analysis but is intentionally lean on some severe weather parameters. We're meant to stay slim and fast.

## Environment

- **Native Windows**, 32 cores, 128GB RAM, NVMe SSDs
- Python 3.12+ via conda (`wxsection` environment)
- Key dependencies: numpy, matplotlib, scipy, cartopy, eccodes, flask, mapboxgl
- Archive SSDs: `E:\hrrr-archive`, `F:\hrrr-archive`, `H:\hrrr-archive`

### Running Locally

```bash
# Restart dashboard (handles env vars, port conflicts, archive dirs)
python restart_dashboard.py

# Or manually:
python tools/unified_dashboard.py --port 5565 --models hrrr,gfs,rrfs,nam,rap,nam_nest

# Start auto-update daemon (from hrrr-maps/ directory!)
python tools/auto_update.py --models hrrr,gfs,rrfs,nam,rap --hrrr-slots 6 --gfs-slots 2 --rrfs-slots 4
```

**Important:** Always launch auto_update.py from the `hrrr-maps/` project directory, or set `XSECT_OUTPUTS_DIR` to an absolute path. The outputs directory resolves relative to the project root via `Path(__file__).parent.parent`.

### API Quick Start

```bash
# List available cycles
curl localhost:5565/api/v1/cycles

# Generate a cross-section
curl "localhost:5565/api/v1/cross-section?model=hrrr&start_lat=34.0&start_lon=-118.5&end_lat=34.5&end_lon=-117.0&product=fire_wx" -o section.png

# List products
curl localhost:5565/api/v1/products

# Browse events
curl localhost:5565/api/v1/events?category=fire
```

Full API documentation: see [API_GUIDE.md](API_GUIDE.md) and [AGENT_GUIDE.md](AGENT_GUIDE.md).

## Agent Platform

The MCP servers and v1 API endpoints are the foundation for AI agent workflows. Agents can:

- Generate and analyze cross-sections across any transect
- Ingest real-world observations (METAR, RAWS) and compare against model forecasts
- Assess fire risk using terrain profiles, fuel conditions, and ignition corridors
- Investigate specific towns with full atmospheric forensics
- Run coordinated swarm operations across geographic zones

See [AGENT_GUIDE.md](AGENT_GUIDE.md) for the full agent platform reference.

## Code Conventions

- **matplotlib OO API only** — `Figure()` + `fig.add_subplot()`, never `plt.subplots()` (avoids pyplot global state races in multiprocess)
- **ProcessPoolExecutor for CPU-bound work** — GRIB conversion, matplotlib rendering, composites
- **ThreadPoolExecutor for I/O-bound work** — downloads, mmap loads
- **Atomic file operations** — `.partial` → final rename for downloads and cache writes
- **No secrets in source** — API keys via env vars, Mapbox token via `MAPBOX_TOKEN`

## Repository Structure

Two remotes:
- `origin` → FahrenheitResearch/hrrr-maps (legacy)
- `atmos-engine` → FahrenheitResearch/atmos-engine (primary, collaborator access)

Active branch: `windows`
