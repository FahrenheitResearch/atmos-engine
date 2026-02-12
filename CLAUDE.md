# CLAUDE.md — Agent Context for wxsection.com

## Project Overview

Multi-model atmospheric cross-section generator. Users draw a line on a map, get an instant vertical cross-section from HRRR, GFS, RRFS, NAM, RAP, or NAM-Nest weather model data. Live at **wxsection.com**. 21 visualization styles, all derived from cached fields. Agent-native platform: everything the web UI can do is also available via a free REST API and MCP tool servers at feature parity.

## Architecture Summary

```
tools/unified_dashboard.py         — Flask server + Mapbox GL JS frontend + 58 API endpoints (~14,508 lines)
core/cross_section_interactive.py  — Rendering engine (matplotlib, 0.5s warm renders) (~3,605 lines)
core/map_overlay.py                — Map overlay composites (fill + contours + wind barbs) (~1,133 lines)
tools/auto_update.py               — GRIB download daemon (slot-based concurrent) (~929 lines)
model_config.py                    — Model registry (6 models: HRRR/GFS/RRFS/NAM/RAP/NAM-Nest) (~320 lines)
smart_hrrr/orchestrator.py         — Parallel GRIB download with multi-layer validation (~311 lines)
tools/agent_tools/                 — Agent research platform (12 modules + 8 data files, ~57,500 lines)
tools/agent_tools/wfo_swarm/       — Oregon WFO agent swarm pilot (7 zones, 154 agents, ~3,120 lines)
tools/mcp_server.py                — MCP server — private (52 tools, stdio)
tools/mcp_public.py                — MCP server — public (53 tools, SSE, API key auth)
restart_dashboard.py               — Production startup (handles env vars, port conflicts, archive dirs)
```

## Key Design Decisions

- **Mmap cache on NVMe**: GRIB files are converted to raw numpy arrays (~2.8GB/FHR HRRR, ~50MB/FHR GFS on disk, ~100MB resident RAM). This is what makes instant cross-sections possible.
- **GFS CONUS subset**: GFS global 0.25deg grid (721x1440) is subset to CONUS+5deg padding (~166x333) at extraction time. Cuts GFS cache from ~500MB to ~50MB/FHR on disk.
- **eccodes `auto` backend**: Default GRIB backend tries eccodes direct (one-pass scan, ~35% faster), falls back to cfgrib. Configurable via `XSECT_GRIB_BACKEND` env var. Critical for NAM/RAP: eccodes misses v-wind in awphys/awp130pgrb, but cfgrib fallback extracts it — enabling wind_speed, shear, fire_wx for those models.
- **Lazy smoke loading**: wrfnat files (652MB, 50 hybrid levels) loaded on-demand on first `smoke` style request, not during preload.
- **Multiprocess + threaded**: Native Windows. CPU-bound work (rendering, GRIB conversion) uses ProcessPoolExecutor. I/O-bound work (downloads, mmap loads) uses ThreadPoolExecutor.
- **Slot-based concurrent auto-update**: 4 HRRR + 2 GFS + 8 RRFS download slots via per-model ThreadPoolExecutor. Each model has its own lane. HRRR fail-fast prunes unavailable FHRs. Priority boost steals slots from RRFS/GFS for early HRRR FHRs.
- **Status file IPC**: auto_update.py writes status JSON to `tempfile.gettempdir()` atomically; dashboard reads it. No shared memory or sockets.
- **No handoff cycles**: Only one synoptic (48h) HRRR cycle, only one GFS/RRFS cycle. Previous cycles are evicted.
- **Two-tier NVMe eviction**: Rotated preload cycles always evicted. Archive request caches persist up to 1TB.
- **Project-relative paths**: All output/cache paths resolve via `Path(__file__).resolve().parent.parent`, never CWD-relative. Env var `XSECT_OUTPUTS_DIR` overrides.

## Environment

- **Native Windows** (NOT WSL2), 32 cores, 128GB RAM
- **NVMe**: code + mmap cache (`C:\Users\drew\hrrr-maps\cache\xsect\`)
- **Archive SSDs**: `E:\hrrr-archive`, `F:\hrrr-archive`, `H:\hrrr-archive`
- **Cloudflare Tunnel**: routes wxsection.com to localhost:5565
- **Conda env**: `wxsection`, Python 3.12+
- **Restart**: `python C:\Users\drew\hrrr-maps\restart_dashboard.py`

## Running Locally

```bash
# Restart dashboard (handles env vars, port conflicts, archive dirs)
python restart_dashboard.py

# Or manually:
python tools/unified_dashboard.py --port 5565 --models hrrr,gfs,rrfs,nam,rap,nam_nest

# Start auto-update daemon (MUST run from hrrr-maps/ directory, or set XSECT_OUTPUTS_DIR)
python tools/auto_update.py --models hrrr,gfs,rrfs,nam,rap --hrrr-slots 6 --gfs-slots 2 --rrfs-slots 4
```

## Performance Characteristics

| Operation | Time |
|-----------|------|
| Warm render (cached FHR) | ~0.5s |
| Cached prerender (from frame cache) | ~20ms |
| Cross-section interpolation (KDTree + mmap) | ~7ms |
| GRIB-to-mmap conversion (eccodes) | ~15s/FHR HRRR, ~11s GFS, ~28s RRFS |
| Mmap load (cached on NVMe) | <0.1s |
| Cached preload (176 FHRs) | ~4s total |
| Parallel prerender (19 frames) | ~4s |
| HRRR FHR download (519MB, wrfprs+wrfsfc) | ~80s |
| GFS FHR download (516MB) | ~83s |
| RRFS FHR download (795MB) | ~124s |

## Critical Constraints

1. **Multiprocess parallelism**: Native Windows — all CPU-bound work uses ProcessPoolExecutor with persistent pools. Each worker has its own GIL + eccodes instance.
2. **matplotlib OO API required**: Uses `Figure()` + `fig.add_subplot()` (not `plt.subplots()`) to avoid pyplot global state races. All colorbar/savefig calls go through `fig.` not `plt.`.
3. **Memory budget**: HRRR 48GB, GFS 1.5GB (CONUS subset), RRFS 8GB. Mmap keeps resident small.
4. **NVMe space**: Cache limit enforced by `cache_evict_old_cycles()`.
5. **Smoke loading is lazy**: wrfnat only loaded on first `style=smoke` request.
6. **Project-relative paths**: Never use `Path('outputs')` — always `Path(__file__).resolve().parent.parent / 'outputs'`.

## Key Constants

```python
# unified_dashboard.py
RENDER_SEMAPHORE = 12       # Max concurrent matplotlib renders
PRERENDER_WORKERS = 8       # Parallel prerender processes
PRELOAD_WORKERS = 20        # Cached mmap load threads
GRIB_POOL_WORKERS = 6       # GRIB conversion processes
CACHE_LIMIT_GB = 2000       # NVMe cache size limit
HRRR_HOURLY_CYCLES = 3      # Non-synoptic cycles in preload window

# auto_update.py (slot-based concurrent)
HRRR_SLOTS = 4              # --hrrr-slots (boosted to ~12 during priority)
GFS_SLOTS = 2               # --gfs-slots
RRFS_SLOTS = 8              # --rrfs-slots
MIN_GRIB_SIZE = 500_000     # Download validation minimum (500KB)
# STATUS_FILE = tempfile.gettempdir() / "auto_update_status.json"
```

## API Counts

- **58 total endpoints** (34 v1 agent-friendly + 24 legacy/internal)
- **52 MCP tools** (private stdio server)
- **53 MCP tools** (public SSE server, +3 city browsing tools)
- **21 cross-section products** (13 with anomaly support)
- **8 map overlay composites** + 21 individual overlay fields

## API Quick Reference

| Endpoint | Description |
|----------|-------------|
| `GET /api/v1/cross-section` | Generate cross-section PNG (agent-friendly) |
| `GET /api/v1/products` | List available visualization styles |
| `GET /api/v1/cycles` | List available model cycles |
| `GET /api/v1/status` | Server health check |
| `GET /api/v1/overlay` | Map overlay PNG |
| `GET /api/v1/events` | Browse archive events |
| `GET /api/xsect` | Generate cross-section PNG (legacy) |
| `GET /api/cycles` | List cycles with load status |
| `GET /api/status` | Memory/load status |
| `POST /api/load` | Load specific cycle + FHR |
| `POST /api/prerender` | Batch pre-render frames |

See [API_GUIDE.md](API_GUIDE.md) for full documentation.

## Common Tasks

### Restart dashboard
```bash
python C:\Users\drew\hrrr-maps\restart_dashboard.py
```

### Restart auto-update
```bash
python tools/auto_update.py --models hrrr,gfs,rrfs,nam,rap --hrrr-slots 6 --gfs-slots 2 --rrfs-slots 4
```

### Check what's loaded
```bash
curl -s localhost:5565/api/cycles | python -m json.tool
curl -s localhost:5565/api/status | python -m json.tool
```

## Download Architecture

Auto-update uses slot-based concurrency (`run_download_pass_concurrent`):
- Each model gets dedicated ThreadPoolExecutor slots (4 HRRR + 2 GFS + 8 RRFS defaults)
- **HRRR-first priority boost**: When new HRRR cycle detected, temporarily steals slots from RRFS/GFS until early FHRs (F00-F05) are done
- Models download in parallel — slow RRFS can't block HRRR
- HRRR fail-fast: if an FHR isn't published, prunes higher FHRs from same cycle
- Downloads full wrfprs (~383MB) + wrfsfc (~136MB) per HRRR FHR. Skips wrfnat (~663MB) — lazy-downloaded on smoke request.
- **Download validation**: HTTP status, content-type, file size >500KB, GRIB magic bytes. Atomic .partial → final rename.
- Self-restart wrapper with exponential backoff on crashes (2s → 30s max)

**Availability lag**: HRRR 50min, GFS 180min (3h), RRFS 0min. Set in `MODEL_AVAILABILITY_LAG`.

## Activity Panel (Progress Tracking)

Dashboard tracks operations via `PROGRESS` dict + `/api/progress` endpoint. Frontend polls every 1.5s.

| Op Type | Icon | Color | Source |
|---------|------|-------|--------|
| `preload` | > | indigo | Startup preload of target cycles |
| `autoload` | > | light-indigo | Background rescan auto-load (every 30-60s) |
| `load` | up | default | Manual FHR load |
| `download` | down | amber | Archive cycle download |
| `prerender` | dot | purple | Batch frame rendering |
| `autoupdate` | cycle | cyan | auto_update download progress (from status file) |

## Repository

Two remotes (same local directory):
- `origin` -> FahrenheitResearch/hrrr-maps (legacy, do NOT push here)
- `atmos-engine` -> FahrenheitResearch/atmos-engine (primary)

Active branch: `windows`

## Known Performance Bottlenecks

1. **GRIB-to-mmap conversion (~15s/FHR)**: eccodes `auto` backend is ~35% faster than cfgrib but still GIL-bound. 3-4 workers optimal.
2. **NOMADS per-connection speed (~6-7 MB/s)**: Main download bottleneck. More slots help linearly up to ~8 connections.
3. **Matplotlib render (~400ms)**: CPU-bound. Agg backend.
4. **GFS data volume**: 65 FHRs x 6h intervals = F00-F384. Full cycle download is large.
