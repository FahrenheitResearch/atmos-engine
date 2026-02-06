# Cross-Section Dashboard Context

## Current State (Feb 5, 2026 — evening)

### Branch: `hrrr-maps-cross-section`

Focused repo for interactive HRRR cross-section visualization.
Live at **wxsection.com** via Cloudflare Tunnel (`cloudflared` running in WSL).

### What's New (uncommitted changes on branch)

#### Multi-Model Support
- `unified_dashboard.py` supports `--models hrrr,gfs,rrfs` (comma-separated)
- `ModelManagerRegistry` holds one `CrossSectionManager` per model
- `MODEL_MEM_BUDGETS`: hrrr=58GB, gfs=8GB, rrfs=8GB (total ~64GB target)
- `model_config.py` registry provides full_name, resolution, domain per model
- `MODEL_PRS_PATTERNS`, `MODEL_SFC_PATTERNS`, `MODEL_NEEDS_SEPARATE_SFC` handle per-model GRIB layout
- All API endpoints accept `?model=hrrr` query param (defaults to hrrr)
- UI model selector dropdown (hidden when only 1 model enabled)

#### Extended 48h HRRR Forecasts (Synoptic Cycles)
- `SYNOPTIC_HOURS = {0, 6, 12, 18}` — these HRRR cycles run to F48 (others F18)
- `get_max_fhr_for_cycle()` returns 48 for synoptic, 18 for hourly
- `scan_available_cycles()` includes `max_fhr` and `is_synoptic` in cycle metadata
- `auto_update.py`: `get_latest_synoptic_cycle()` finds most recent 00/06/12/18z; `run_update_cycle()` downloads F19-F48 for it after standard F00-F18
- `cleanup_old_extended()` keeps only 2 most recent synoptic runs with extended FHRs

#### Synoptic Cycle Handoff (always keep a 48h cycle loaded)
- `get_protected_cycles()` now also calls `_get_synoptic_protected()` for HRRR
- Protects the newest synoptic cycle that has F00-F18 "mostly loaded" (15+ of 19 FHRs)
- If newest synoptic isn't ready yet, ALSO protects the previous synoptic cycle
- Ensures users always have a 48h cycle available during the handoff window
- `_auto_load_latest_inner()` prioritizes synoptic cycles (up to 2 newest) in load queue
- Synoptic HRRR cycles get ALL available FHRs loaded (F00-F48), not just base F00-F18

#### Interleaved Cycle Loading
- `_preload_latest_cycles_inner()` now interleaves FHRs round-robin across all cycles
- Both hourly AND synoptic cycles load simultaneously (no waiting for one to finish)
- Also pulls in synoptic cycles beyond the top N if not already included
- `PRELOAD_WORKERS = 4` (up from 2) — ~2.3GB temp RAM each during GRIB-to-mmap conversion

#### Dynamic FHR Chips (UI)
- `renderFhrChips()` reads `max_fhr` from cycle metadata
- Synoptic cycles show F00-F18 then divider `|` then F19-F48 with dashed-border "extended" chips
- Hourly cycles unchanged (F00-F18)

#### Time Slider + Auto-Play
- Slider row appears when 2+ FHRs loaded
- Play/pause button with configurable speed (0.5x, 1x, 2x, 4x)
- Pre-render button batches all loaded frames for instant scrubbing
- Slider uses prerendered blob URLs when available, else live fetch
- `invalidatePrerender()` fires on marker drag and style/param changes

#### Frame Prerender Cache + API
- `FRAME_CACHE` dict with 500-entry limit (~75MB max)
- `POST /api/prerender` — batch renders frames in background thread with progress tracking
- `GET /api/frame` — cache-first frame retrieval, falls back to live render
- Cached frames serve in ~20ms vs ~4.5s live render

#### Cycle Comparison Mode
- "Compare" toggle button in control bar
- Second cycle dropdown and mode toggle (Same FHR vs Valid Time)
- Side-by-side flexbox layout with labeled panels
- Same FHR mode: both panels show identical FHR from different init cycles
- Valid Time mode: auto-calculates comparison FHR to match same valid time
- Comparison panel updates on primary FHR change, marker drag, or slider scrub

#### Agent-Friendly v1 API
- All endpoints return JSON (cycles, status, progress, etc.)
- `/api/frame` returns PNG for a single frame
- `/api/prerender` batch renders
- `API_GUIDE.md` documents all endpoints

#### Standard Temperature Colormap
- New `standard` temp colormap added as default
- Auto-load priority favors newest cycle

### Memory Architecture (updated)
- **58GB HRRR hard cap** (soft trigger at 56GB), 8GB each for GFS/RRFS
- **Mmap cache**: Per-field float16 .npy files, memory-mapped with `mmap_mode='r'`
- **Heap per FHR**: ~29MB (just lats+lons coordinate arrays) — OS page cache manages data
- **GRIB-to-mmap conversion**: ~30-40s per FHR, ~2.3GB temp RAM during conversion, then garbage collected
- **Disk requirement**: ~2.3GB cache per FHR; ensure sufficient free disk or mmap saves fail and RAM stays high
- **Old-format cache cleanup**: Previously caches were at `cache/dashboard/xsect/CYCLE_FHR_FILE/`, now at `cache/dashboard/xsect/{model}/CYCLE_FHR_FILE/`. Old format must be manually cleaned: `rm -rf cache/dashboard/xsect/202*`

### What Works
- **Dashboard**: `tools/unified_dashboard.py` - Flask + Leaflet interactive map
- **Cross-section engine**: `core/cross_section_interactive.py` - Sub-second generation
- **Mmap caching**: `cache/dashboard/xsect/{model}/` — per-field .npy files in float16, memory-mapped (~12ms "load" vs 2s old NPZ, ~2.3GB/FHR disk, 400GB limit with eviction). OS page cache manages physical RAM automatically. Legacy .npz caches auto-migrate on first load
- **15 styles**: wind_speed, temp, theta_e, rh, q, omega, vorticity, shear, lapse_rate, cloud, cloud_total, wetbulb, icing, frontogenesis, smoke
- **Anomaly/departure mode**: "Raw / 5yr Dep" toggle subtracts 5-year HRRR climatological mean from current forecast. RdBu_r diverging colormap centered at 0. Works for 10 anomaly-eligible styles
- **Climatology pipeline**: `tools/build_climatology.py` builds monthly mean NPZ files from archived HRRR data
- **Color-coded chip UI**: Grey (on disk) / Green (in RAM) / Blue (viewing) / Yellow (loading) / Shift+click to unload
- **Plot annotations**: A/B labels, ~100+ city labels, lat/lon secondary axis, legend box, inset map with A/B badges
- **Distance units**: km/mi toggle at render time
- **Auto-load**: Background thread (every 60s) detects new FHRs, loads them, prioritizes synoptic cycles
- **Smart memory management**: LRU eviction with synoptic cycle protection
- **Render semaphore**: Limits concurrent matplotlib renders to 4, returns 503 if queue full
- **Disk management**: 500GB GRIB limit with space-based LRU eviction
- **Auto-update daemon**: `tools/auto_update.py` downloads latest cycles continuously + extended F19-F48 for synoptic
- **Custom date requests**: Calendar button downloads any date from NOMADS/AWS with live progress toast (admin key required)
- **Community favorites**: Save/load cross-section configs, 12h expiry
- **Cloudflare Tunnel**: Named tunnel `wxsection` -> wxsection.com + www.wxsection.com
- **GIF animation**: `/api/xsect_gif` animated GIF with Pillow, 4 speed options
- **Terrain masking**: Theta contours, freezing level, isotherms masked below terrain
- **Temperature colormaps**: 4 options (standard, green_purple, white_zero, nws_ndfd)
- **Admin key system**: `WXSECTION_KEY` env var only gates downloading. Loading/unloading open to all
- **Smoke loading**: eccodes-based MASSDEN from wrfnat on native hybrid levels
- **Atomic downloads**: `.partial` temp files, renamed on completion

### Files (16 Python files)
```
config/colormaps.py
core/__init__.py
core/cross_section_interactive.py   # Main engine - get_cross_section() + anomaly subtraction
core/cross_section_production.py    # Batch generation
core/downloader.py
core/grib_loader.py
model_config.py                     # Model registry (HRRR/GFS/RRFS metadata)
smart_hrrr/__init__.py
smart_hrrr/availability.py
smart_hrrr/io.py
smart_hrrr/orchestrator.py          # Parallel GRIB downloads (on_complete callback)
smart_hrrr/utils.py
tools/auto_update.py                # Progressive download daemon + extended 48h synoptic
tools/build_climatology.py          # Build monthly climatology NPZ from archived HRRR
tools/bulk_download.py              # Bulk HRRR archive downloader for VHD/external drives
tools/unified_dashboard.py          # Flask dashboard + multi-model + comparison + slider
```

### Key Architecture Details
- **Engine key system**: `_engine_key_map` maps `(cycle_key, fhr)` to auto-incrementing int for `self.forecast_hours` dict
- **Metadata passthrough**: Dashboard builds metadata dict (model, init_date, init_hour, real FHR) and passes directly to `get_cross_section(metadata=...)` — thread-safe, no shared state
- **Colorbar positioning**: Manual `fig.add_axes([0.90, 0.12, 0.012, 0.68])` with `cax=cbar_ax` (15 instances)
- **City labels**: `ax.secondary_xaxis(-0.08)` for aligned secondary axis, 120km search radius
- **Unit conversion**: `dist_scale = KM_TO_MI if use_miles else 1.0` applied at render time
- **Figure size**: `figsize=(17, 11)`, axes at `[0.06, 0.12, 0.82, 0.68]`
- **Terrain masking**: `terrain_mask` built from `pressure_levels > surface_pressure[i]`, applied to theta/temperature contours via `np.ma.masked_where`
- **Temperature colormaps**: `_build_temp_colormap(name)` static method returns colormap. All defined as F anchor arrays, converted to C internally. 512-bin `LinearSegmentedColormap`
- **GIF frame lock**: Terrain + pressure levels from first FHR, locked across all subsequent frames
- **Render semaphore**: `threading.Semaphore(4)` wraps all matplotlib render calls
- **Admin key**: `WXSECTION_KEY` env var, only gates `/api/request_cycle` downloads
- **Protected cycles**: `get_protected_cycles()` returns newest 2 + synoptic-protected cycles. Eviction skips these
- **Synoptic protection**: `_get_synoptic_protected()` keeps newest ready synoptic + previous synoptic during handoff
- **Interleaved loading**: `_preload_latest_cycles_inner()` round-robins FHRs across all cycles so users get usable data from multiple cycles quickly
- **Auto-load priority**: Newest cycle first, then synoptic cycles (up to 2), then remaining. Synoptic cycles load all FHRs (F00-F48)
- **Mmap cache format**: Per-FHR directory under `cache/dashboard/xsect/{model}/`. Individual `.npy` files. 3D fields as float16, geopotential_height as float32. `_complete` marker for atomic creation. `np.load(path, mmap_mode='r')` for zero-copy access
- **Smoke loading**: eccodes-based, native hybrid levels (50 levels), not interpolated to isobaric
- **Anomaly engine**: `ClimatologyData` dataclass, coarsened climo arrays, `RegularGridInterpolator` for cross-section path interpolation
- **Atomic downloads**: `.partial` temp files throughout all download paths
- **FHR availability gating**: Requires wrfprs AND wrfnat (HRRR) or wrfprs (GFS/RRFS) to exist
- **Stale cache validation**: Checks pressure levels count and surface pressure on load
- **Duplicate prevention**: All `loaded_items.append()` sites check before appending
- **Loading mutex**: `self._loading` prevents overlapping bulk loads

### VHD Archive Infrastructure
- **VHDX file**: `D:\hrrr-archive.vhdx` (20TB dynamic)
- **WSL mount**: `wsl --mount --vhd "D:\hrrr-archive.vhdx" --bare` from PowerShell (admin), then `sudo mount /dev/sde /mnt/hrrr` in WSL
- **Why VHD**: WSL2 9p bottleneck — 19.7 MB/s through 9p vs 183 MB/s direct VHD
- **Remount after WSL restart**: Required every time

### Key APIs
```python
# Interactive cross-section
from core.cross_section_interactive import InteractiveCrossSection
ixs = InteractiveCrossSection(cache_dir="cache/dashboard/xsect")
ixs.set_climatology_dir("/mnt/hrrr/climatology")
ixs.load_forecast_hour(data_dir, forecast_hour)
img_bytes = ixs.get_cross_section(start_point, end_point, style, forecast_hour, units='km', metadata={...}, anomaly=True)

# Parallel downloads
from smart_hrrr.orchestrator import download_gribs_parallel
download_gribs_parallel(model, date_str, cycle_hour, forecast_hours)

# Build climatology
# python tools/build_climatology.py --archive /mnt/hrrr --output /mnt/hrrr/climatology --month 2 --min-samples 3
```

### Running Dashboard
```bash
# Production (all 3 services)
export WXSECTION_KEY=your_secret
./deploy/run_production.sh        # start dashboard + auto-update + tunnel
./deploy/run_production.sh stop   # stop all

# Manual
WXSECTION_KEY=secret python tools/unified_dashboard.py --port 5559 --preload 2 --production --models hrrr
python tools/auto_update.py --interval 2 --max-hours 18
cloudflared tunnel run wxsection

# Test server (different port, same code)
python tools/unified_dashboard.py --port 5560 --models hrrr,gfs,rrfs

# Remount VHD after WSL restart (PowerShell admin first)
# wsl --mount --vhd "D:\hrrr-archive.vhdx" --bare
sudo mount /dev/sde /mnt/hrrr
```

### Process Management
Startup order matters — dashboard must bind port 5559 before cloudflared starts forwarding:
1. Remount VHD if WSL restarted
2. Start dashboard (binds :5559)
3. Start cloudflared tunnel (forwards wxsection.com -> localhost:5559)
4. Start auto_update daemon

Common issue: stale port after crash. Fix: `kill -9 $(lsof -ti:5559)`, wait 3s, then restart dashboard.

Cloudflare tunnel config at `~/.cloudflared/config.yml`:
```yaml
tunnel: 13c6556c-b8bb-4a81-8730-f57005819544
credentials-file: /home/drew/.cloudflared/13c6556c-...json
ingress:
  - hostname: wxsection.com
    service: http://localhost:5559
  - hostname: www.wxsection.com
    service: http://localhost:5559
  - service: http_status:404
```

### Data Locations
- **Live GRIB files**: `outputs/hrrr/YYYYMMDD/HHz/F##/` (auto-update writes here, 500GB limit)
- **Mmap cache**: `cache/dashboard/xsect/{model}/` (per-field .npy dirs, auto-created on load)
- **OLD mmap cache**: `cache/dashboard/xsect/YYYYMMDD_*` (pre-model-subdirectory format — delete these: `rm -rf cache/dashboard/xsect/202*`)
- **Archive GRIBs**: `/mnt/hrrr/YYYYMMDD/HHz/F##/` (VHD, bulk_download.py writes here)
- **Climatology NPZ**: `/mnt/hrrr/climatology/climo_MM_HHz_FNN.npz` (~30MB each)
- **Favorites**: `data/favorites.json`
- **Votes**: `data/votes.json`
- **Feature requests**: `data/requests.json`
- **Disk metadata**: `data/disk_meta.json`

### Known Issues / TODO
- **Disk space**: 2TB WSL disk fills up fast. Old-format mmap caches under `cache/dashboard/xsect/202*` must be manually cleaned. GRIB outputs at 500GB limit. Monitor with `df -h /home/drew/`
- **AWS bulk downloads**: Paused while nailing down 48h cycle + multi-model. Resume when ready
- **GFS/RRFS verification**: Multi-model code is in place but needs verification on test server before production push
- **48h cycle verification**: Synoptic handoff logic implemented, needs extended testing
- **Test-then-prod workflow**: Changes should go to test server (:5560) first, verify, then push to production (:5559). Current session pushed directly to prod
