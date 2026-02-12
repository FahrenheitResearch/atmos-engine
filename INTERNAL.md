# Internal Technical Reference — wxsection.com

> This document is the AI agent codebase map. Read this first to know exactly where to look.
> Not for external collaborators — see CONTRIBUTING.md for the public overview.

## Vision

An agent swarm of thousands running every HRRR cycle, each forensically evaluating the full atmosphere for specific towns and terrain features. No town is too small — even if it's one person. Agents use all our MCP tools, verify model data against real-world observations, find anomalies, and proactively warn communities about risks they don't know they have.

The web UI and cross-section tool are the human interface. The API and MCP servers are the agent interface. Both are always at feature parity.

## File Map (Where Everything Lives)

### Core Engine (3 files, ~4,970 lines)

| File | Lines | What It Does |
|------|-------|-------------|
| `core/cross_section_interactive.py` | ~3,515 | **The heart.** GRIB extraction, mmap cache, KDTree interp, all 20 product renderers, GFS CONUS subset, smoke lazy-load, comparison panels |
| `core/map_overlay.py` | ~1,133 | Map overlay rendering. Reprojection (KDTree for curvilinear, bilinear for GFS), composite assembly (fill + contours + barbs), PNG/binary output |
| `model_config.py` | ~320 | Model registry. 6 models (HRRR/GFS/RRFS/NAM/RAP/NAM-Nest) metadata, grid specs, download URLs, forecast hour lists |

### Server + UI (1 file, ~12,340 lines)

| File | Lines | What It Does |
|------|-------|-------------|
| `tools/unified_dashboard.py` | ~12,340 | **Everything else.** Flask server, Mapbox GL JS frontend (inline HTML/CSS/JS), all 57 API endpoints (34 v1 + 23 legacy), model managers, prerender cache, autoload/rescan thread, frame cache, progress tracking, events system, city/region profiles UI, comparison/GIF generation, quick-start transects |

**Key sections in unified_dashboard.py:**
- Lines 1-1018: Imports, constants, overlay cache, helper functions, model config dicts
- Lines 1019-1240: `CrossSectionManager` class — init, config, model management
- Lines 1241-1720: `scan_available_cycles()`, `preload_latest_cycles()`, loading logic
- Lines 1721-2464: `auto_load_latest()`, orchestration, prerender hooks
- Lines 2465-9015: HTML template (inline, ~6,550 lines) — the entire frontend
  - CSS (~1,100 lines): Inter font, model pills, workflow grid, map HUD, dark theme with cyan accents, loading spinners
  - HTML body (~950 lines): icon sidebar (48px) + expanded panel (400px) + map + bottom slide-up
  - Mapbox GL JS map init + overlay controller (~2,100 lines): starts ~line 4500, double-buffered swap with 8s timeout
  - Frontend JS (~2,300 lines): model pills, FHR slider, product selector, keyboard shortcuts (1-6 model switch, Home/End, o=overlay toggle), URL state, GIF, events, cities, transect presets, quick-start, guide modal
- Lines 9021: Flask route `/` — serves HTML with token injection
- Lines 9021-12189: All API route handlers (57 endpoints)
- Lines 12190-12338: Startup — argument parsing, preload, rescan thread, server launch

### Download System (2 files, ~1,240 lines)

| File | Lines | What It Does |
|------|-------|-------------|
| `tools/auto_update.py` | ~929 | Download daemon. Slot-based concurrency (per-model ThreadPoolExecutor), priority boost for early HRRR FHRs, fail-fast pruning, status file IPC, disk eviction |
| `smart_hrrr/orchestrator.py` | ~312 | Single-FHR download. Multi-source fallback (NOMADS → AWS → Pando), 4-layer validation (HTTP status, content-type, size >500KB, GRIB magic bytes), atomic `.partial` → final rename |

### Agent Research Platform (12 modules + 8 data files + WFO swarm, ~57,500 lines total)

| File | Lines | What It Does |
|------|-------|-------------|
| `tools/agent_tools/cross_section.py` | 362 | CrossSectionTool, CrossSectionData, batch_images |
| `tools/agent_tools/external_data.py` | ~2,400 | METAR, RAWS, SPC, NWS, elevation, drought, Street View, mesonet, wind verification, climatology |
| `tools/agent_tools/fire_risk.py` | ~1,700 | assess_conditions, investigation_checklist, data quality checks |
| `tools/agent_tools/case_study.py` | 931 | CaseStudy framework, TransectSpec, temporal evolution |
| `tools/agent_tools/report_builder.py` | 1,142 | ReportBuilder, LaTeX templates, PDF compilation |
| `tools/agent_tools/forecast.py` | 1,832 | ForecastGenerator, agent swarm orchestrator, national_fire_scan |
| `tools/agent_tools/investigation.py` | 900 | investigate_location, investigate_town, batch_investigate (44 OR towns) |
| `tools/agent_tools/terrain.py` | ~1,318 | analyze_terrain_complexity, city_terrain_assessment (232 city profiles) |
| `tools/agent_tools/fuel_conditions.py` | ~1,800 | assess_fuel_conditions (73 city ignition profiles), seasonal context |
| `tools/agent_tools/frontal_analysis.py` | 1,078 | detect_wind_shifts, classify_overnight_conditions |
| `tools/agent_tools/report_quality.py` | 803 | fire_report_checklist, validate_report_claims |

### Regional Profile Data (6 files, ~42,000 lines, 258 cities)

| File | Lines | Cities |
|------|-------|--------|
| `tools/agent_tools/data/california_profiles.py` | 14,102 | 62 |
| `tools/agent_tools/data/pnw_rockies_profiles.py` | 7,587 | 76 (43 OR, 12 WA, 10 ID, 11 MT) |
| `tools/agent_tools/data/colorado_basin_profiles.py` | 5,669 | 38 |
| `tools/agent_tools/data/southwest_profiles.py` | 4,624 | 29 |
| `tools/agent_tools/data/southern_plains_profiles.py` | 3,541 | 28 |
| `tools/agent_tools/data/southeast_misc_profiles.py` | 3,512 | 25 |
| `tools/agent_tools/data/oregon_zones.py` | 310 | 7 zones, 44 towns |
| `tools/agent_tools/data/oregon_transects.py` | 704 | 31 cross-section presets |

### Oregon WFO Swarm (11 files, ~3,120 lines)

| File | Lines | What It Does |
|------|-------|-------------|
| `tools/agent_tools/wfo_swarm/config.py` | 161 | Zone config, agent tier definitions |
| `tools/agent_tools/wfo_swarm/scheduler.py` | 384 | Tier-based scheduling, dependency tracking |
| `tools/agent_tools/wfo_swarm/swarm.py` | 199 | Main swarm orchestrator, zone runner |
| `tools/agent_tools/wfo_swarm/zone_state.py` | 143 | Per-zone state accumulator |
| `tools/agent_tools/wfo_swarm/agents/data_acquisition.py` | 414 | Tier 1: METAR/RAWS/NWS data fetch |
| `tools/agent_tools/wfo_swarm/agents/cross_section.py` | 300 | Tier 2: Batch cross-section generation |
| `tools/agent_tools/wfo_swarm/agents/assessment.py` | 390 | Tier 3: Fire risk, terrain, fuel assessment |
| `tools/agent_tools/wfo_swarm/agents/synthesis.py` | 801 | Tier 4: Zone-level risk synthesis |
| `tools/agent_tools/wfo_swarm/agents/output.py` | 299 | Tier 5: Bulletin/PDF/GIF output |

### MCP Servers (3 files)

| File | What It Does |
|------|-------------|
| `tools/mcp_server.py` | Private MCP (stdio, 52 tools, local only) |
| `tools/mcp_public.py` | Public MCP (SSE, 53 tools, port 5566, API key auth via SHA-256 hashes in `data/mcp_api_keys.json`) |
| `tools/mcp_helpers.py` | Shared helpers: `_api_get`, `_ext_fetch_json`, `_ext_fetch_text` |

## Supported Models

| Model | Resolution | Domain | Cycles | Max FHR | Notes |
|-------|-----------|--------|--------|---------|-------|
| **HRRR** | 3km | CONUS | Every hour | 18h (48h synoptic) | Primary model. Full field set (20 products). |
| **GFS** | 0.25deg | Global (CONUS subset) | 00/06/12/18z | 384h | Subset to CONUS+5deg at extraction. All products except smoke. |
| **RRFS** | 3km | North America | Every hour | 18h (60h synoptic) | Experimental HRRR successor. Rotated lat/lon grid. All products except smoke. |
| **NAM** | 12km | CONUS | 00/06/12/18z | 84h | awphys product. 39 levels. cfgrib extracts v-wind (eccodes misses it). Missing q/cloud/dew_point. |
| **RAP** | 13km | CONUS | Every hour | 21h (51h ext) | awp130pgrb product. 37 levels. Same cfgrib v-wind trick. Missing q/cloud/dew_point. |
| **NAM-Nest** | 3km | CONUS | 00/06/12/18z | 60h | High-res NAM nest. 42 levels, 926MB/FHR. Has most fields; dew_point/vorticity partial (7/42 levels). |

**NAM/RAP cfgrib v-wind discovery**: eccodes one-pass scan misses v-component of wind in awphys/awp130pgrb GRIB products, but cfgrib (the `auto` backend fallback) successfully extracts it. Verified: NAM v_wind (39, 428, 614), RAP v_wind (37, 337, 451) — both with real wind values. Wind-dependent styles (wind_speed, shear, fire_wx) are now **enabled**. Still excluded: q, moisture_transport, cloud_total, icing, dewpoint_dep, vorticity, pv (missing fields or level count mismatch).

**NAM-Nest level mismatch**: dew_point and vorticity arrays have only 7 of 42 pressure levels. The `interp_3d()` function maps array indices to pressure level indices, so mismatched arrays get placed at WRONG pressure positions. These styles (dewpoint_dep, vorticity, pv) are excluded via `MODEL_EXCLUDED_STYLES`.

**Sub-hourly data**: No publicly available NWP model provides sub-hourly 3D pressure level data. HRRR wrfsubhf (15-min) is surface-only (2D) — useless for cross-sections. All 3D data (wrfprs, prslev, etc.) is hourly at best. Future possibility: 3D-RTMA (15-min 3D analysis) is in experimental/prototype stage at NCEP, not yet available.

## How the Speed Works (Technical Deep Dive)

### Mmap Cache Architecture

GRIB → per-field `.npy` files on NVMe:
```
cache/xsect/<date>_<cycle>_<fhr>_<filename>/
    temperature.npy     (float16, 50 levels × 1059 × 1799)
    u_wind.npy          (float16)
    v_wind.npy          (float16)
    geopotential_height.npy  (float32 — needs precision for shear/lapse)
    surface_pressure.npy
    pressure_levels.npy (float64, tiny)
    lats.npy            (float64, tiny)
    lons.npy            (float64, tiny)
    _complete           (marker file)
```

**Load** = open file handles with `mmap_mode='r'`. No data read yet. ~0.1s for entire FHR.

**Field sets** (cross_section_interactive.py lines 817-836):
- `_FLOAT16_FIELDS`: temperature, u/v wind, rh, omega, q, vorticity, cloud, dew_point, hydrometeors, smoke, surface_pressure, theta, temp_c (17 fields)
- `_SURFACE_OVERLAY_FIELDS`: refc, t2m, d2m, u10m, v10m, mslp, cape_sfc, cin_sfc, gust, vis, prate (11 fields) — **saved to cache but NOT loaded during preload**, lazy-loaded by map overlay
- `_FLOAT32_FIELDS`: geopotential_height only

### The Cross-Section Interpolation Trick

HRRR uses a Lambert conformal curvilinear grid (2D lat/lon arrays). Traditional approach: build RegularGridInterpolator or do scipy griddata — **slow** (100ms+).

Our approach (cross_section_interactive.py lines 2097-2119):

1. **Build KDTree once** from the 2D grid (~0.3s, cached forever):
   ```python
   tree = cKDTree(np.column_stack([lats.ravel(), lons.ravel()]))
   ```

2. **Query path points** (~0.5ms for 133 points):
   ```python
   _, indices = tree.query(target_points, k=1)
   ```

3. **Fancy-index into mmap** (~0.1ms per level):
   ```python
   vals = field_3d[lev].ravel()[indices]
   ```
   This reads ONLY the ~500 bytes containing the cross-section points from NVMe, not the full 3.8MB 2D level. For 50 levels × 8 fields = 400 reads of ~500 bytes = **200KB total I/O** vs **1.5GB** for full-level reads.

### GFS CONUS Subsetting

GFS global 0.25deg = 721×1440 pixels. We subset to CONUS+5deg padding = ~166×333 pixels (95% reduction). Done at GRIB extraction time (lines 140-227). Old global caches auto-invalidate.

### Map Overlay Reprojection

Same KDTree trick but for 2D→2D. Build projection map once (source grid → output grid indices), cache to disk. Then per-request is just `flat_field[indices].reshape(output_shape)` — ~10ms.

### Prerender Frame Cache

After a cycle loads, the dashboard auto-prerenders all FHR frames for the current style in parallel (8 ProcessPoolExecutor workers). Cached PNGs are served at ~20ms. The FHR slider scrubs through cached frames instantly.

## Key Constants

```python
# unified_dashboard.py
RENDER_SEMAPHORE = 12       # Max concurrent matplotlib renders
PRERENDER_WORKERS = 8       # Parallel prerender processes
PRELOAD_WORKERS = 20        # Cached mmap load threads
GRIB_POOL_WORKERS = 6       # GRIB conversion processes
HRRR_HOURLY_CYCLES = 3      # Non-synoptic hourly cycles to keep loaded

# auto_update.py
HRRR_SLOTS = 4-6            # Concurrent HRRR downloads (boosted to ~12 during priority)
GFS_SLOTS = 2               # Concurrent GFS downloads
RRFS_SLOTS = 4-8            # Concurrent RRFS downloads
MIN_GRIB_SIZE = 500_000     # Download validation minimum (500KB)
```

## Known Issues / Underbaked Areas

### Multi-Panel / Comparison
- Plot labeling now uses `panel_label` metadata to clearly identify each panel's model/cycle/FHR/product
- Inlay display (small overview map showing transect location) is basic
- Multi-product panels (e.g., temp + wind + rh side-by-side) need better visual hierarchy
- `render_multi_panel()` uses PIL compositing: render each panel individually, paste into grid

### Events System
- 88 events in events.json, 22 with curated coordinates and suggested_sections
- Events need reliability pass once all archive data is loaded on SSDs
- Interactive event display presets are very underbaked — should have agent-curated "best view" configs (4-panel time series, multi-product, etc.)
- Agent should be creative with display format based on what the event best shows

### Oregon WFO Swarm
- RAWS 403 errors (MesoWest API rate limiting)
- Dashboard crashes if >1 zone runs concurrent cross-sections
- "Verify METAR" warnings in FireRiskAnalyzer are redundant (swarm already has METAR in state)
- First pilot went "so-so" — agent swarm design still evolving

### GIF / Render Worker
- **FIXED 2026-02-12**: `render_worker.py render_frame()` was passing `marker`, `marker_label`, `markers` kwargs to `get_cross_section()` which doesn't accept them. This caused ALL GIF frames to silently return None. Fix: removed unsupported kwargs.
- Added diagnostic logging: render_frame errors now printed to stderr, GIF error responses include diagnostic counts (loaded/cached/rendered/no_render_info)

### Legacy Code
- Switched from WSL2 to native Windows — some legacy code may still assume Linux paths or lack ProcessPoolExecutor parallelism
- CLAUDE.md has been corrected but other docs may have stale WSL2 references
- Some `.pyc` files have newer bytecode than committed `.py` sources (minor wfo_swarm edits never committed)

### Performance
- Cold FHR interp ~350ms (NVMe page faults when scrubbing through different FHRs for the first time)
- Could add background prefetching of mmap pages for likely-next FHRs
- matplotlib is the bottleneck at ~400ms — rendering is CPU-bound, Agg backend

### Missing Severe Weather Params
- Intentionally lean — fire weather focused
- Missing: STP, SCP, SHERBS, hodograph tools, sounding/skew-T
- Could add if demand exists but want to stay slim

## UI Features (unified_dashboard.py Frontend)

### Valid Time Display
FHR labels throughout the UI show UTC valid time (e.g., "F06 — 18Z Wed 12"). Computed from cycle init time + FHR hours. Appears in:
- Slider label (bottom panel)
- Active FHR display (bottom status bar)
- FHR chip tooltips (hover to see valid time)
- Map HUD overlay (top-left corner)
Functions: `getValidTime(fhr)`, `formatValidTime(fhr)`, `fhrLabel(fhr)`, `fhrWithTime(fhr)`

### Cycle Age Indicator
Shows how old the current model run is (e.g., "3h ago", "2d ago") next to the cycle dropdown. Updates every 10 seconds. Color-coded: green (<1h), muted (<4h), amber (4-48h), red (>48h).

### Right-Click Context Menu
Right-clicking the map shows a context menu with:
- Set start point (A)
- Set end point (B)
- Add POI marker
- Copy coordinates to clipboard
Includes coordinate display at bottom. Auto-positions to stay on screen.

### Product Description Toasts
Selecting a new product style shows a brief info toast with the product's description (e.g., "Equivalent potential temperature — instability analysis"). Auto-dismisses after 3 seconds.

### Colormap Preview Bar
A 4px gradient bar below the style dropdown shows the color scheme of the currently selected product. Updates on style change. Defined in `cmapGradients` object (20 products).

### Transect Metadata Overlay
Floating pill on the cross-section image showing: model name, transect distance (km/mi), bearing, valid time, and render time (e.g., "1.4s").

### Bottom Status Bar
Shows product name + FHR with valid time. Updates on each cross-section generation. For events, shows event name with star icon.

### Playback Frame Counter
During animation playback, shows frame position (e.g., "3/48") next to the slider. Play button toggles between play and pause icons with matching tooltip text.

### Keyboard Shortcuts
- Left/Right arrow (J/K): step FHR
- Space: play/pause
- 1-6: switch models (HRRR, GFS, RRFS, NAM, RAP, NAM-Nest)
- O: toggle map overlay
- C: compare mode
- S: swap A/B endpoints
- Home/End: first/last FHR
- Esc: clear cross-section line
- ?: show shortcuts help
All action buttons include keyboard shortcut hints in their tooltips.

### Onboarding Landing Panel
Visual 1-2-3 step guide ("Click A → Click B → Explore") with numbered circles. Includes 6 quick-start transect buttons and live cycle info.

### Quick-Start Transects
6 preloaded transects on the landing page: Denver Front Range, Columbia Gorge, Sierra Nevada, Great Plains Dryline, Oregon Cascades, LA Basin.

### Tabbed Guide Modal
Help button opens a 3-tab modal:
- **Getting Started**: visual steps, key features overview, quick shortcuts
- **Products (20)**: clickable product reference cards (click to switch and close modal)
- **Shortcuts**: comprehensive keyboard shortcut grid organized by category

### New Cycle Notifications
Auto-refresh checks for new model cycles every 3 minutes. Shows toast with model name and cycle label (e.g., "New HRRR cycle: 20260212 12Z").

### Quick Analysis Workflows
7 one-click workflow presets (sidebar buttons): Fire Weather, Severe, Upper Air, Moisture, Jet Stream, Surface, Model Compare, Time Series. Each sets style + overlay product + y_top.

### Share & Save Buttons
- Share: copies current URL (with all state) to clipboard
- Save: downloads current cross-section PNG with descriptive filename

## API Endpoint Count

- **57 total endpoints** (34 v1 agent-friendly + 23 legacy/internal)
- **52 MCP tools** (private stdio server)
- **53 MCP tools** (public SSE server, +3 city browsing tools)
- **20 cross-section products** (13 with anomaly support)
- **8 map overlay composites** + 21 individual overlay fields

## Events & Archive

- 88 events in `data/events.json` (fires, hurricanes, tornadoes, derechos, hail, winter, AR)
- Archive HRRR data on SSDs: E:\, F:\, H:\ drives
- Events have agent-swarm-curated init times, FHR ranges, coordinates, suggested cross-sections
- Each event can have a "hero" configuration — the single best view that tells the story
- Interactive events: agent-generated presets for how to display (time series, multi-product, multi-panel)

## Operational Rhythm

Every hour:
1. auto_update detects new HRRR cycle (~50min after init)
2. Downloads wrfprs + wrfsfc for F00-F18 (6 slots, ~80s/FHR)
3. Dashboard rescan thread (2s interval) detects new GRIBs
4. GRIB → mmap conversion (eccodes, 6 ProcessPoolExecutor workers, ~15s/FHR)
5. Auto-prerender all frames for loaded styles (8 workers, ~4s for 19 frames)
6. User requests served from frame cache (~20ms) or live render (~500ms)

Every 6 hours (synoptic):
- Same flow but extended HRRR to F48 + new GFS cycle (F00-F384)

## Restart Procedures

```bash
# Dashboard (handles everything)
python restart_dashboard.py

# Auto-update (MUST run from hrrr-maps/ directory)
cd C:\Users\drew\hrrr-maps
python tools/auto_update.py --models hrrr,gfs,rrfs --hrrr-slots 6 --gfs-slots 2 --rrfs-slots 4

# MCP public server
python tools/mcp_public.py  # port 5566
```

## Agent Swarm Design (Evolving)

Current Oregon pilot: 7 zones × 22 agents = 154 agents per HRRR cycle
5 tiers: Data Acquisition → Cross-Section → Assessment → Synthesis → Output

Future vision:
- Scale to all CONUS with 258 city profiles as seeds
- Each city gets a team of agents every cycle
- Agents compare model vs observations, detect anomalies
- Towns that are "the main risk but don't know it" get proactive alerts
- Creative display: agents decide best visualization format per-event
- Not just warnings — full atmospheric forensics with cross-sections, terrain analysis, fuel assessment, observation verification
