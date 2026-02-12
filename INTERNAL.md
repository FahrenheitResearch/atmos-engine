# Internal Technical Reference — wxsection.com

> This document is the AI agent codebase map. Read this first to know exactly where to look.
> Not for external collaborators — see CONTRIBUTING.md for the public overview.

## Vision

An agent swarm of thousands running every HRRR cycle, each forensically evaluating the full atmosphere for specific towns and terrain features. No town is too small — even if it's one person. Agents use all our MCP tools, verify model data against real-world observations, find anomalies, and proactively warn communities about risks they don't know they have.

The web UI and cross-section tool are the human interface. The API and MCP servers are the agent interface. Both are always at feature parity.

## File Map (Where Everything Lives)

### Core Engine (3 files, ~5,060 lines)

| File | Lines | What It Does |
|------|-------|-------------|
| `core/cross_section_interactive.py` | ~3,605 | **The heart.** GRIB extraction, mmap cache, KDTree interp, all 21 product renderers (including isentropic ascent), GFS CONUS subset, smoke lazy-load, comparison panels |
| `core/map_overlay.py` | ~1,133 | Map overlay rendering. Reprojection (KDTree for curvilinear, bilinear for GFS), composite assembly (fill + contours + barbs), PNG/binary output |
| `model_config.py` | ~320 | Model registry. 6 models (HRRR/GFS/RRFS/NAM/RAP/NAM-Nest) metadata, grid specs, download URLs, forecast hour lists |

### Server + UI (1 file, ~15,961 lines)

| File | Lines | What It Does |
|------|-------|-------------|
| `tools/unified_dashboard.py` | ~15,961 | **Everything else.** Flask server, Mapbox GL JS frontend (inline HTML/CSS/JS), all 58 API endpoints (34 v1 + 24 legacy), model managers, prerender cache, autoload/rescan thread, frame cache, progress tracking, events system, city/region profiles UI, comparison/GIF generation, quick-start transects, og:image preview, FHR hover thumbnails, hero cross-section, smart product suggestions, skeleton loading, draw-mode feedback, distance/bearing line label, mobile panel backdrop, event timeline (hover tooltips), comparison diff view (with badge labels + draggable divider), 3D terrain, measurement tool, wind barb legend, geocoder search, image zoom/pan, product search filter, slider tick marks, download export, model-colored HUD badges |

**Key sections in unified_dashboard.py:**
- Lines 1-1031: Imports, constants, overlay cache, helper functions, model config dicts
- Lines 1032-1253: `CrossSectionManager` class — init, config, model management
- Lines 1254-1720: `scan_available_cycles()`, `preload_latest_cycles()`, loading logic
- Lines 1721-2478: `auto_load_latest()`, orchestration, prerender hooks
- Lines 2479-11927: HTML template (inline, ~9,449 lines) — the entire frontend
  - CSS (~2,085 lines, lines 2513-4597): Inter font, model pills, workflow grid, product picker, full CSS design system (18 z-index layers, 5 operation colors, 6 region colors, 3 HUD colors, anomaly var), dark theme with CSS custom properties (--transition-fast/default/slow, --surface/surface-alt), skeleton loading, draw-mode cursor, toast with animated spinner + auto-dismiss progress bars, mobile backdrop, FHR chip horizontal scroll with fade indicators + loading spinner. **Extracted CSS classes**: .ctx-menu (context menu with fade animation), .overlay-tooltip, .pp-search-wrap/input, .pp-chip-row, .pp-cat-chip (product picker categories), .fhr-thumb, .xs-minimap, .xs-cursor, .event-cat-pill (with CSS opacity states + hover), .hero-preview (CSS :hover replacing JS), .hero-preview-img/label, .landing/.landing-title/subtitle/steps/stat (full landing page), .map-hud, .hud-badge/.hud-model/cycle/fhr/overlay, .map-legend/.map-legend-right/left/title/labels, .barb-legend-items, .map-attribution, .map-coords, .modal-form/.form-label/input/row/submit, .bottom-peek/.peek-img, .active-product-badge/chip, .loaded-count, .cycle-age, .playback-btn/.play-btn, .slider-label, .frame-counter, .context-hint, .settings-footer, .api-code/.api-copy-btn/.api-links, .kbd, .sr-only, .xs-marker/.poi-marker/.measure-marker, .xs-info-badge, .product-strip-pill (CSS hover states), .suggest-pill/.suggest-row, .shortcut-help/.shortcut-grid, .guide-tab, .detail-header/.detail-header-meta, .detail-section/.detail-section-title/body, .detail-item/.detail-item-bordered, .detail-action, .error-panel/.error-icon/.error-msg, .tt (custom tooltip with arrow), .btn-primary, Mapbox popup theming via CSS vars. **UI features**: collapsible sidebar sections (chevron indicator), custom tooltips (data-tip replacing browser title, 59 elements), modal fade+scale transitions (4 modals), product picker dropdown slide-fade animation, Escape to close modals
  - HTML body (~1,120 lines): icon sidebar (48px, custom tooltips via data-tip, cities count badge) + expanded panel (400px, collapsible sections) + map toast + mobile backdrop + preset library + map + barb legend (backdrop blur) + bottom slide-up (drag handle hover effect) + hero preview + 3D terrain controls + zoom/download actions + compare divider + overlay HUD badge
  - Mapbox GL JS map init + overlay controller (~2,400 lines): starts ~line 4560, double-buffered swap with fade transitions, 3D terrain (Mapbox DEM), measurement tool, distance/bearing label layer
  - Frontend JS (~4,000 lines): model pills (partial/loaded indicators), FHR slider with tick marks + progress fill, FHR hover thumbnails, hero cross-section loader, smart product suggestions, visual product picker with category filter chips + text search, keyboard shortcuts (22 bindings), URL state (y_axis + overlay deep-link), user prefs, local timezone, GIF, events with emoji category pills + timeline canvas (hover tooltips), cities, transect preset library (18 in 4 categories + 36 in presets dropdown), quick-start loading (glow animation), guide modal (icons + fade transitions), recent transects (localStorage), all-models compare (draggable divider), draw-mode feedback, distance/bearing label, XS hover readout + zoom/pan, playback prefetch (chip glow), comparison diff view with badge labels, context menu (fade-in animation), measurement tool, map coords readout, CONUS mini-map, geocoder search, image download export, overlay HUD badge, model-colored HUD, product strip hover states (with colormap chips), settings API section, copy-link button (clipboard API), custom tooltip system (data-tip), recently used products (localStorage)
- Lines 11933: Flask routes start — `/` serves HTML, `/og-preview.png` serves branded preview
- Lines 11933-15172: All API route handlers (58 endpoints + og-preview)
- Lines 15299-15435: Startup — argument parsing, preload, rescan thread, server launch

### Download System (2 files, ~1,240 lines)

| File | Lines | What It Does |
|------|-------|-------------|
| `tools/auto_update.py` | ~929 | Download daemon. Slot-based concurrency (per-model ThreadPoolExecutor), priority boost for early HRRR FHRs, fail-fast pruning, status file IPC, disk eviction |
| `smart_hrrr/orchestrator.py` | ~311 | Single-FHR download. Multi-source fallback (NOMADS → AWS → Pando), 4-layer validation (HTTP status, content-type, size >500KB, GRIB magic bytes), atomic `.partial` → final rename |

### Agent Research Platform (12 modules + 8 data files + WFO swarm, ~57,500 lines total)

| File | Lines | What It Does |
|------|-------|-------------|
| `tools/agent_tools/cross_section.py` | 362 | CrossSectionTool, CrossSectionData, batch_images |
| `tools/agent_tools/external_data.py` | ~2,415 | METAR, RAWS, SPC, NWS, elevation, drought, Street View, mesonet, wind verification, climatology |
| `tools/agent_tools/fire_risk.py` | ~1,681 | assess_conditions, investigation_checklist, data quality checks |
| `tools/agent_tools/case_study.py` | 931 | CaseStudy framework, TransectSpec, temporal evolution |
| `tools/agent_tools/report_builder.py` | 1,142 | ReportBuilder, LaTeX templates, PDF compilation |
| `tools/agent_tools/forecast.py` | ~1,841 | ForecastGenerator, agent swarm orchestrator, national_fire_scan |
| `tools/agent_tools/investigation.py` | 900 | investigate_location, investigate_town, batch_investigate (44 OR towns) |
| `tools/agent_tools/terrain.py` | ~1,318 | analyze_terrain_complexity, city_terrain_assessment (261 city profiles) |
| `tools/agent_tools/fuel_conditions.py` | ~1,831 | assess_fuel_conditions (73 city ignition profiles), seasonal context |
| `tools/agent_tools/frontal_analysis.py` | ~1,077 | detect_wind_shifts, classify_overnight_conditions |
| `tools/agent_tools/report_quality.py` | ~802 | fire_report_checklist, validate_report_claims |

### Regional Profile Data (6 files, ~42,000 lines, 258 cities + 3 hardcoded = 261 total)

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
| **HRRR** | 3km | CONUS | Every hour | 18h (48h synoptic) | Primary model. Full field set (21 products). |
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

### Map Overlay Prerender

Mirrors the cross-section prerender pattern for map overlays. `OVERLAY_CACHE` (500 frames, LRU eviction, ~75MB) stores PNG→WebP converted overlay frames (~70-80% size reduction). Auto-prerenders `surface_analysis` and `fire_weather` products on every cycle load via `auto_prerender_overlay_all_products()`. Endpoints: `/api/v1/map-overlay/frame` (cache-first single frame), `/api/v1/map-overlay/prerender` (batch prerender). Frontend uses double-buffered Mapbox image sources (weather-overlay-a/b) with sequence-gated swaps for flash-free animation. `prefetchAllFrames()` fetches all FHR frames as blob URLs for instant slider scrubbing.

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
- **Comparison prerender**: `/api/prerender` accepts `comparison: {mode, products, models, cycles, cycle_match}` to batch-render multi-panel composites per FHR. Cached frames served via `/api/v1/comparison` (cache hit). Frontend detects `multiPanelMode` and sends comparison params automatically.
- **Comparison GIF export**: GIF button routes to `/api/v1/comparison/gif` when in multi-panel mode (product, model, or cycle). Each frame is a full multi-panel composite at a different FHR.
- **Comparison caching**: `/api/v1/comparison` now checks FRAME_CACHE before rendering and stores results after. Cache key includes mode, model, cycle, FHR, and mode-specific params.

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

### Visual Product Picker
Custom dropdown panel replaces flat `<select>` for the 21 cross-section products. Shows products organized by category (Core, Thermodynamics, Moisture, Dynamics, Cloud & Precip, Fire & Smoke) with colormap gradient chips and descriptions. Supports keyboard navigation (arrow keys, Enter, Escape). Hidden `<select>` stays in sync for all existing code references.

### Colormap Preview Bar
A 4px gradient bar below the product picker shows the color scheme of the currently selected product. Updates on style change. Defined in `cmapGradients` object (21 products). Value range labels below the bar show min/max values (e.g., "0 kt → 80 kt" for wind speed). Defined in `cmapRanges` object.

### Transect Metadata Overlay
Floating pill on the cross-section image showing: model name, transect distance (km/mi), bearing, valid time, and render time (e.g., "1.4s").

### Bottom Status Bar
Shows model name, active product badge (with colormap chip), comparison mode badge, and FHR with valid time. Updates on each cross-section generation. Loading spinner shows product name (e.g., "Rendering Fire Weather..."). For events, shows event name with star icon. Comparison badge shows active mode (Multi-Product, Multi-Model, Cycle Compare, Temporal) with accent-tinted pill styling.

### Playback Frame Counter
During animation playback, shows frame position (e.g., "3/48") next to the slider. Play button toggles between play and pause icons with matching tooltip text. Active play button has pulsing blue glow animation (`play-glow` keyframes).

### Keyboard Shortcuts (28 key bindings, 20 actions)
- Left/Right arrow (J/K): step FHR
- Space: play/pause
- Home/End: first/last FHR
- [ / ]: previous/next product
- 1-6: switch models (HRRR, GFS, RRFS, NAM, RAP, NAM-Nest)
- Y: cycle y-axis (pressure/height/isentropic)
- A: toggle anomaly mode
- O: toggle map overlay
- Shift+O: toggle overlay loop
- { / }: cycle overlay product
- C: compare mode
- S: swap A/B endpoints
- F: fullscreen cross-section
- T: toggle 3D terrain
- M: measure distance on map
- Esc: clear cross-section line / exit mode
- ?: show shortcuts help modal
All action buttons include `.kbd-hint` shortcut badge indicators.

### FHR Hover Thumbnails
When hovering over a loaded (green) FHR chip for 300ms, a thumbnail preview of the cross-section at that forecast hour appears above the chip. Uses the existing frame cache for instant response. Thumbnails are cached as blob URLs client-side to avoid redundant fetches. Only triggers for loaded FHRs with an active cross-section line.

### Onboarding Landing Panel
Visual 1-2-3 step guide ("Click A → Click B → Explore") with numbered circles. Includes 6 quick-start transect buttons, hero cross-section preview, and live cycle info.

### Hero Cross-Section Preview
Auto-loads a sample cross-section (randomly: Denver Front Range, Oregon Cascades, or Sierra Nevada) 2s after page load. Displayed as a clickable thumbnail in the landing panel — click to load the full transect. Fades in smoothly; disappears when user draws their own line or clicks a quick-start button.

### Quick-Start Transects
6 preloaded transects on the landing page: Denver Front Range, Columbia Gorge, Sierra Nevada, Great Plains Dryline, Oregon Cascades, LA Basin.

### Tabbed Guide Modal
Help button opens a 3-tab modal:
- **Getting Started**: visual steps, key features overview, quick shortcuts
- **Products (21)**: clickable product reference cards (click to switch and close modal)
- **Shortcuts**: comprehensive keyboard shortcut grid organized by category

### New Cycle Notifications
Auto-refresh checks for new model cycles every 3 minutes. Shows toast with model name and cycle label (e.g., "New HRRR cycle: 20260212 12Z").

### Quick Analysis Workflows
8 one-click workflow presets in a 4-column grid (sidebar buttons): Fire Weather, Severe, Upper Air, Moisture, Jet Stream, Surface, Model Compare, Time Series. Each sets style + overlay product + y_top.

### Product Quick-Switch Strip
After generating a cross-section, a row of small product pills appears below the image. Active product highlighted in cyan; click any pill to instantly switch products. Pills are grouped by category with colored dot separators (matching the product picker's group colors). Excluded products for the current model are hidden.

### Recent Transects
Last 5 cross-section transects saved to localStorage with dedup. Shows clickable "Recent transects" section on landing page for quick re-access. Functions: `getRecentTransects()`, `saveRecentTransect()`, `renderRecentTransects()`.

### Share & Save Buttons
- Share: copies current URL (with all state) to clipboard
- Save: downloads current cross-section PNG with descriptive filename

### Social Sharing / OG Preview
Full Open Graph + Twitter Card meta tags. Server-generated 1200x630 OG preview image at `/og-preview.png` (matplotlib-rendered, cached in memory after first request). Shows branded atmospheric contour background with cross-section line motif, site name, tagline, and model list.

### User Preference Persistence
Saves user choices to `localStorage` under `wxs-prefs` key: style, model, basemap, y_axis, y_top, units. Restored on next visit, but URL state always takes priority. Implemented via function patching on `switchModel()` and `setYAxis()` plus change listeners on select elements.

### Smart Product Suggestions
After rendering a cross-section, a "Try:" row suggests 2-3 relevant products based on transect geography. Rules: mountains → wind/lapse_rate/isentropic_ascent, fire regions → fire_wx/VPD/RH, Great Plains → theta_e/shear/omega, coastal → moisture_transport/RH, winter months → icing/wetbulb. Implemented in `getSmartSuggestions()`.

### Skeleton Loading Animation
Cross-section render shows a dark card with shimmer effect and terrain silhouette instead of a plain spinner. CSS `.xsect-skeleton` with `clip-path` mountain shape and gradient shimmer animation.

### All Models Compare Button
One-click "All Models" button in toolbar triggers multi-panel model comparison across all 6 models for the current transect and FHR. Activates multi-panel mode and selects all model chips automatically.

### Event Category Filter Pills
Color-coded category pills (fire-ca, hurricane, tornado, derecho, hail, ar, winter) with counts replace the dropdown filter for instant visual category scanning. Active pill highlighted, click to filter. `selectEventCatPill()` syncs pills with hidden select.

### Accessibility
All interactive controls have `aria-label` attributes: playback buttons, FHR slider, overlay toggles/selects, search inputs, GIF controls, event filter, toolbar buttons. Product picker has `role="listbox"` with `role="option"` items and full keyboard navigation.

### Cross-Section Image Zoom & Pan
Mouse wheel zoom (up to 8x) centered on cursor position. Drag to pan when zoomed. Controls: +/- buttons and 1:1 reset in top-right corner. Auto-resets zoom on new image load. Download button in top-left action bar.

### FHR Slider Enhancements
- **Tick marks**: Major interval labels (F06/F12/F18/F24/F36/F48) below slider, auto-adjusting interval (6h for <24h range, 12h for >24h)
- **Progress fill**: Gradient fill from accent to gray tracks playback position
- **FHR chip tooltips**: All chips show valid time on hover (e.g., "F12 — 00Z Thu 13 (viewing · Shift+click to unload)")

### Toast Notification System
- Type-specific auto-dismiss: success 3s, info 5s, error 8s, loading stays until removed
- Animated progress bar at bottom shows time remaining
- Click any toast to dismiss immediately
- Smooth fade-out animation on dismiss

### Product Picker Search
Text search input at top of product dropdown. Filters products by name, description, or key as you type. Combined with existing category filter chips. Auto-focuses when dropdown opens. Escape clears search and closes dropdown.

### Overlay Fade Transitions
Smooth 400ms raster-opacity fade in/out when toggling map overlay on/off (instead of instant show/hide). Uses Mapbox `raster-opacity-transition` property.

### Overlay URL State Persistence
Overlay state (on/off, product, opacity) saved to URL parameters for link sharing. Parameters: `overlay=1`, `overlay_product=surface_analysis`, `overlay_opacity=70`. Restored from URL on page load alongside other state (transect, model, style).

### Comparison Panel Badge Labels
Rich labels in compare mode show model, product, cycle, and FHR as color-coded badges. Differences between panels highlighted in amber (e.g., different cycle or FHR gets amber badge vs standard gray/blue).

### Model Load State Indicators
Model pills show data load state via colored dot: green = 10+ FHRs loaded, amber = partial (<10 FHRs), gray = empty. Updated every few seconds via `/api/models` polling.

### 3D Terrain
Mapbox DEM tiles (`mapbox-terrain-dem-v1`) with configurable exaggeration (1-3x slider). Auto-tilts map to 45° pitch when enabled. Keyboard shortcut [T]. Re-enables terrain after basemap style change.

### Map Measurement Tool
Multi-point click measurement. GeoJSON line + symbol layers show segment distances and total (km + mi). Toggle with Measure button or [M] key. Escape clears measurement. Haversine distance calculation.

### Wind Barb Legend
SVG-based legend showing 5kt (half barb), 10kt (full barb), 50kt (flag) symbols. Auto-shows for composite overlay products (surface_analysis, fire_weather, etc.). Hidden for single-field overlays and when overlay is off.

### Geocoder Search
Mapbox GL Geocoder plugin in top-left map corner (collapsed icon mode). Dark theme CSS. Bounded to CONUS (bbox: -170,15 to -50,75). No custom marker — just navigates to location.

### Event Timeline Canvas
HTML5 canvas timeline visualization showing all 88 events as color-coded dots by category. Year gridlines. Click a dot to show event details. DPR-aware rendering. Part of the Events tab.

### Context Menu Enhancements
Right-click context menu includes: Set start A, Set end B, Add POI, Copy coords, Center map here, Zoom in here. Custom positioning avoids screen edge overflow. Fade-in scale animation, rounded hover rows.

### Tab Content Animations
Sidebar panel tab switching uses CSS fade + translateY transition. Content fades in with a 4px upward slide. Guide modal tab content also uses the same pattern.

### Compare Mode Draggable Divider
Draggable vertical divider between comparison panels. Drag left/right to resize panels (15-85% range). Resets to 50/50 when exiting compare mode. Blue accent color with ↕ icon indicator.

### Event Category Emoji Icons
Event category pills show emoji icons: fire (🔥), hurricane (🌀), tornado (🌪), derecho (⚡), hail/winter (❄), AR (🌊). Icons appear in both filter pills and event list chips.

### Model-Colored Map HUD
The map HUD model badge uses per-model colors: HRRR=cyan (#0ea5e9), GFS=purple (#8b5cf6), RRFS=green (#22c55e), NAM=orange (#f97316), RAP=yellow (#eab308), NAM-Nest=pink (#ec4899). Updates dynamically on model switch.

### CSS Design System Variables
Custom properties for consistent design:
- **Transitions**: `--transition-fast: 0.12s`, `--transition-default: 0.2s`, `--transition-slow: 0.35s`
- **Surfaces**: `--surface: #253347`, `--surface-alt: #2d3f56` (mid-tone panel backgrounds)
- **Border radius**: `--radius-sm/md/lg/pill` (4/6/8/12px)
- **Box shadow**: `--shadow-sm/md/lg/xl` (4 elevation levels)
- **Z-index layers**: 18 named layers (`--z-base` through `--z-modal-top`) replacing scattered magic numbers
- **Operation colors**: `--op-preload/autoload/download/prerender/autoupdate` for progress bars
- **Region colors**: `--region-california/pnw/colorado/southwest/plains/southeast` for city chips
- **HUD colors**: `--hud-model/--hud-dark/--hud-overlay` for map HUD badge backgrounds
- **Status colors**: `--danger`, `--danger-light`, `--anomaly: #FF6D00`
- **Button sizes**: `.btn-sm` (3px 8px, 12px), `.btn-xs` (2px 6px, 11px), `.input-xs` (50px, 11px, dark bg)
- Shared `MODEL_COLORS` JS constant for per-model coloring
- All CSS class definitions use CSS variables for transitions, colors, and z-indices (no hardcoded values)

### Settings Panel API Section
Settings tab includes an API quick-reference section with copyable endpoint URL and links to products/status endpoints. Section titles have emoji icons (🌎 Map Style, 📍 Map Markers, ⚡ API).

### Bottom Panel Drag Handle
Handle pill widens (40→56px) and turns accent-colored on hover. Double-click cycles through all three states: collapsed → half → full → collapsed.

### Slider Thumb Hover Effects
FHR slider thumb scales up 1.2x on hover with enhanced glow. Active (dragging) state: 1.1x scale with brighter glow.

### Product Strip Hover States
Inactive product pills in the quick-switch strip highlight on hover (background darkens, text brightens). Active product shown in bold with accent background.

### Control Section Hover Accent
Control sections (.ctrl-section) get a subtle left border accent in translucent cyan on hover, providing visual feedback for which section the user is interacting with.

### CSS Utility Classes
Extracted from inline `style=` attributes for consistency:
- **Selects**: `.select--flex`, `.select--compact-flex`, `.select--min50/60/70/80/120`, `.select--min120-sm`, `.select--speed`, `.select--gif-speed`, `.select--mp-mode`
- **Buttons**: `.btn--tight`, `.btn--diff`, `.btn--feature`, `.btn-primary--sm`, `.zoom-btn--sm`
- **Layout**: `.ctrl-row--mt`, `.ctrl-row--mb`, `.ctrl-row--wrap`, `.input-range--flex`, `.input--fhrs`, `.playback-group`
- **Labels**: `.label--muted-sm`, `.label--vs`, `.label--xs`
- **Badges**: `.badge--success`, `.comparison-badge`
- **Elements**: `.canvas--colorbar`, `.xsect-actions`, `.xsect-action-download`, `.xsect-action-link`, `.diff-canvas`, `.diff-panel-label`, `.colorbar-units`, `.event-list`, `.memory-status`
- **Modals**: `.guide-tabs`, `.modal-content--sm`, `.modal-header--compact`, `.shortcut-title`, `.shortcut-footer`
- **Legend**: `.legend-title--bold`

### Sidebar Tab Active Indicator
Active sidebar icon tab has a left accent bar (`::after` pseudo-element, 3px wide, 18px tall) plus inner box-shadow for depth. Creates a visual "selected" indicator extending outside the tab.

### Prerender Indicator
FHR chips with prerendered frames show a glowing blue dot (6px, accent color, 4px box-shadow) in the top-right corner instead of a lightning bolt emoji. Consistent with the design language.

### Dynamic Page Title
Browser tab title updates to show current state: "HRRR 20260212_06z F03 | wxsection.com". Updated every 500ms via `updateHUD()`.

### Accessibility Features
- `:focus-visible` outline (cyan accent ring) for keyboard navigation
- `aria-live` region announces toast messages to screen readers
- Playback controls wrapped in `role="group"` with `aria-label`
- `prefers-reduced-motion` media query disables all animations
- Print stylesheet hides UI chrome and formats cross-section for paper

### Model Pill Per-Color Coding
Active model pill uses the model's unique color (from `MODEL_COLORS`) instead of generic accent blue. HRRR=cyan, GFS=purple, RRFS=green, NAM=orange, RAP=yellow, NAM-Nest=pink. Includes a pop animation on activation.

### FHR Chip Valid Time Tooltips
Loaded FHR chips show valid time on hover via `title` attribute (e.g. "Forecast Hour 3 (09:00 UTC Wed)").

### Overlay Keyboard Shortcuts
`Shift+O` toggles overlay loop, `{` and `}` cycle overlay products. Documented in shortcut help overlay.

### Share URL Full State
Share URL now includes `vscale`, `ytop`, `units` parameters in addition to model, style, FHR, cycle, y_axis, overlay state. Fully reproducible cross-sections when shared.

### Error Recovery (Retry Buttons)
Error states in city profile, multi-panel comparison, and all showcase features (quad-plot, temporal evolution, playback) now include a Retry button.

### Showcase Notes Dismiss
The analysis notes bar in showcase mode has a dismiss X button, allowing users to close it without exiting showcase mode.

### Activity Panel Auto-Open
Submitting an archive download request auto-expands the progress/activity panel so users see download progress immediately.

### Tablet Breakpoint
Intermediate breakpoint at 769-1024px (tablet landscape): narrower sidebar panel (340px), smaller chips and toggle buttons.

### Scroll-Snap for FHR Chips
`.chip-group` uses `scroll-snap-type: x proximity` and `.chip` uses `scroll-snap-align: start` for smoother mobile FHR scrolling.

### GIF Progress Feedback
GIF button shows frame count during generation ("GIF 18f..."). Success toast includes frame count: "GIF saved (18 frames, 2.1 MB, 8.3s)".

### Modal Backdrop Blur
All modals (explainer, archive request, run request) use `backdrop-filter: blur(8px)` for depth-of-field effect behind the modal overlay.

### Mapbox Controls Dark Theme
Zoom/compass controls restyled with dark translucent background, blur backdrop, accent-hover, and inverted icons to match the dark UI theme. Focus-visible ring on keyboard navigation.

### Button Disabled States
Global `button:disabled` and `.toggle-btn:disabled` styles: 50% opacity, not-allowed cursor, pointer-events disabled. Applied consistently across all UI buttons.

### FHR Chip Loading Spinner
FHR chips in `.loading` state show a spinning border `::after` pseudo-element (8px circle, 0.6s rotation). Provides visual feedback during the ~15s load operation.

### Error Panel Helper
Reusable `showErrorPanel(container, message, retryAction)` function renders consistent error displays with optional retry button. Replaces 7 identical inline error patterns.

### Empty State Guidance
Empty search/filter results show secondary hint text: "Try a different term or clear the region filter" (cities), "Try removing category or date filters" (events).

### List Item Hover Elevation
City-item and event-item rows gain subtle `box-shadow: var(--shadow-sm)` on hover for depth affordance alongside existing background/border-color changes.

### Colorbar Fade Transition
Overlay colorbar fades out with 200ms opacity transition instead of instant `display:none`. Uses CSS transition property on the inline style.

### Global Scrollbar Styling
All scrollable containers use `scrollbar-width: thin; scrollbar-color: var(--border) transparent` (Firefox) and `::-webkit-scrollbar` styles (6px width, dark thumb with hover brightening).

### Model Dot Load Animation
When a model's status dot transitions to `.loaded` state, a pulse animation (`dot-pulse` keyframe) briefly scales the dot to 1.6x with a green glow halo. Uses `animationend` listener for clean class removal.

### Memory Counter Animation
Memory display (`updateMemoryDisplay`) uses `requestAnimationFrame`-based counting animation with cubic ease-out. Smoothly interpolates between old and new MB values over 200-400ms. Skips animation for changes <2 MB.

### Toast Loading Spinner
Loading-type toasts now show an animated CSS border-spinner (`.toast-spinner`) instead of the hourglass emoji. Other toast types (success, info, error) retain their emoji icons.

### Focus-Visible Ring
All buttons, selects, and toggle-btns have `:focus-visible` outline (2px solid accent, 2px offset) for keyboard accessibility. No visible ring on mouse click.

### HUD Badge CSS Variables
Map HUD badges use CSS custom properties: `--hud-model` (cyan translucent), `--hud-dark` (dark translucent), `--hud-overlay` (purple translucent). Centralizes the 3 HUD background colors.

### Compare Button CSS Transitions
Compare and diff toggle buttons use CSS class-based active states (`.active`) instead of inline JS style assignments. `#compare-btn.active` gets accent background, `#compare-diff-btn.active` gets warning/amber background. Both have `transition: background/color var(--transition-fast)`.

### Button Size Classes
Reusable `.btn-sm` (3px 8px, 12px font) and `.btn-xs` (2px 6px, 11px font) CSS classes replace 13 identical inline `style="padding:3px 8px;font-size:12px;"` attributes on action buttons.

### Map Toast Slide-In
Map toast notification slides in from above with translateY(-8px→0) combined with opacity fade, creating a subtle entrance animation instead of simple fade-in.

### Anomaly Status Variable
Anomaly toggle button color centralized to CSS variable `--anomaly: #FF6D00` instead of hardcoded hex. Used by `.toggle-btn.anomaly-active`.

## API Endpoint Count

- **58 total endpoints** (34 v1 agent-friendly + 24 legacy/internal)
- **52 MCP tools** (private stdio server)
- **53 MCP tools** (public SSE server, +3 city browsing tools)
- **21 cross-section products** (13 with anomaly support)
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
- Scale to all CONUS with 261 city profiles as seeds
- Each city gets a team of agents every cycle
- Agents compare model vs observations, detect anomalies
- Towns that are "the main risk but don't know it" get proactive alerts
- Creative display: agents decide best visualization format per-event
- Not just warnings — full atmospheric forensics with cross-sections, terrain analysis, fuel assessment, observation verification
