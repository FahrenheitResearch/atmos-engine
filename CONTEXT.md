# Cross-Section Dashboard Context

## Current State (Feb 6, 2026)

### Branch: `hrrr-maps-cross-section`

Live at **wxsection.com** via Cloudflare Tunnel. WSL2 on Windows, 32 cores, 118GB RAM.

### Startup

```bash
cd ~/hrrr-maps && ./start.sh
# Mounts VHD, starts auto_update, dashboard (port 5561), cloudflared tunnel
```

Or manually:
```bash
sudo mount /dev/sde /mnt/hrrr
nohup python tools/auto_update.py --interval 2 --models hrrr,gfs,rrfs > /tmp/auto_update.log 2>&1 &
XSECT_GRIB_BACKEND=cfgrib WXSECTION_KEY=ctwc nohup python3 tools/unified_dashboard.py --port 5561 --models hrrr,gfs,rrfs > /tmp/dashboard.log 2>&1 &
nohup cloudflared tunnel run wxsection > /tmp/cloudflared.log 2>&1 &
```

---

## COMPLETED: NVMe Cache Migration

### What Changed
- **Deleted stale 371GB cache** at `~/hrrr-maps/cache/dashboard/` (was unused, left over from old config)
- **Moved CACHE_BASE to NVMe**: `/home/drew/hrrr-maps/cache/xsect` (was `/mnt/hrrr/cache/xsect` on VHD)
- **Updated `start.sh`** to create NVMe cache dir instead of VHD cache dir
- **NVMe free after migration**: ~1.4TB (was 963GB before deleting stale cache)
- **Old VHD cache** at `/mnt/hrrr/cache/xsect/` (~348GB) is now orphaned and can be deleted to free VHD space

### Performance Impact
- GRIB-to-mmap conversion improved from ~50s/FHR (VHD) to ~23s/FHR (NVMe) — **2x faster**
- Cache writes no longer compete with GRIB reads for VHD I/O bandwidth
- Mmap page faults for cached data now served from NVMe instead of external VHD

---

## CRITICAL ISSUES & PERFORMANCE PROBLEMS

### 1. GRIB-to-mmap Conversion (~23s/FHR on NVMe, was ~50s on VHD)
- **cfgrib** does extensive Python-level work between eccodes C calls — dominated by GIL contention
- 20 threads = 0 completions in 3+ min (99/102 threads on `futex_wait_queue`)
- 4 ThreadPool workers is the only stable config
- **ProcessPoolExecutor fails on WSL2**: `folio_wait_bit_common` kernel-level contention when multiple processes do concurrent I/O through Hyper-V virtual block layer. All workers go D-state
- Full preload of 151 uncached FHRs takes ~58 min at current rate (was ~125 min on VHD)

### 2. WSL2 VHD Folio Contention
- Both `/dev/sdd` (2TB NVMe VHD) and `/dev/sde` (20TB external VHD) go through Hyper-V virtual block layer
- Multiple *processes* doing concurrent I/O trigger `folio_wait_bit_common` in WSL2 page cache locking
- This is NOT disk speed — it's WSL2-specific kernel contention
- ThreadPoolExecutor (single process) avoids folio; ProcessPoolExecutor triggers it
- NVMe has less folio pressure than external VHD but still goes through Hyper-V layer

---

## Architecture

### Preload Window (6 HRRR cycles, ~151-174 FHRs)
```
Priority order:
  1. Latest init (e.g. 08z) — 19 FHRs, always first
  2. Newest synoptic 48h (e.g. 06z) — 49 FHRs
  3. Previous synoptic handoff (e.g. 00z) — 49 FHRs (if newest not ready)
  4. 3 recent hourlies (e.g. 07z, 05z, 04z) — 19 FHRs each

HRRR_HOURLY_CYCLES = 3  (was 5, reduced to keep picker clean)
```

Only these cycles appear in the run picker dropdown. Archive-requested cycles appear when downloading/loaded.

### Two-Phase Preload (cache-first)
```
Phase 1: ThreadPoolExecutor(20 workers) — cached mmap loads (<0.1s each)
Phase 2: ThreadPoolExecutor(4 workers)  — GRIB conversion (~23s each on NVMe)
```
Partitions FHRs by checking if mmap cache dir exists. Users see data immediately from Phase 1 instead of waiting for all GRIB conversions.

### Cache Eviction (RAM + NVMe disk)
```
RAM eviction:
  - _auto_load_latest_inner(): evicts loaded FHRs whose cycle is no longer in target window
  - _evict_if_needed(): memory-pressure backstop at 48GB HRRR / 8GB GFS,RRFS limits
  - Protected cycles (current target window) are never evicted from RAM

NVMe cache eviction — two-tier (cache_evict_old_cycles):
  Tier 1 (always, every ~10 min):
    - Rotated preload cycles: if a cycle falls out of target window and
      wasn't an archive request, its cache is deleted immediately
    - Example: 03z hourly rotates out when 09z appears → 03z cache deleted
  Tier 2 (size-based, CACHE_LIMIT_GB = 670):
    - Archive request caches persist on NVMe for fast re-loading
    - Only evicted when total cache exceeds 670GB, oldest archive first
    - Evicts down to 85% (~570GB) to avoid thrashing
  - ARCHIVE_CACHE_KEYS set tracks which cycles were archive-requested
  - Target/loaded cycles are never evicted at either tier
  - Budget: ~425GB preload window + ~245GB archive headroom
```

### HRRR-Priority Auto-Update (interleaved)
```
Old: for model in [hrrr, gfs, rrfs]: download_all_fhrs(model)  # RRFS blocks for 15+ min
New: Download one FHR at a time, HRRR always first:
  - If HRRR has work -> download HRRR FHR, continue
  - If HRRR empty -> download one GFS/RRFS FHR (round-robin)
  - Every 2 non-HRRR downloads -> re-check HRRR for new FHRs from NOMADS
  - When HRRR queue empties -> re-scan for newly published FHRs
```

### Memory Architecture
- **Mmap cache per FHR**: 2.3GB on disk (40 levels x 1059 x 1799 x 14 float16/32 fields)
- **Resident RAM per FHR**: ~100MB (mmap only pages in accessed slices)
- **174 FHRs loaded**: ~4-6GB RAM, ~400GB on disk
- **Heap per FHR**: ~29MB (lats+lons coordinate arrays)
- **Memory limits**: 48GB HRRR hard cap, 8GB each GFS/RRFS

### Disk Layout
```
/dev/sdd (2TB NVMe VHD) mounted at /  — 1.4TB free
  ~/hrrr-maps/                         — code
  ~/hrrr-maps/cache/xsect/hrrr/       — ACTIVE mmap cache (NVMe, building up)
  ~/hrrr-maps/cache/xsect/gfs/        — GFS cache (NVMe)
  ~/hrrr-maps/outputs/                 — symlinks to VHD

/dev/sde (20TB external VHD) mounted at /mnt/hrrr  — 17TB free
  /mnt/hrrr/hrrr-live/                 — live HRRR GRIBs (491GB)
  /mnt/hrrr/gfs/                       — live GFS GRIBs (113GB)
  /mnt/hrrr/rrfs/                      — live RRFS GRIBs (83GB)
  /mnt/hrrr/cache/xsect/              — OLD VHD cache (~348GB, orphaned, can delete)
  /mnt/hrrr/YYYYMMDD/                 — archived HRRR GRIBs
  /mnt/hrrr/climatology/              — monthly mean NPZ files

/dev/shm (59GB tmpfs, pure RAM)       — unused, too small for cache
```

### Per-FHR Sizes
```
HRRR GRIB source:  ~1.2GB (wrfprs + wrfsfc + wrfnat)
HRRR mmap cache:   ~2.3GB (14 fields x 40 levels x 1059x1799)
HRRR cycle (19 FHR): ~23GB GRIB, ~44GB cache
HRRR synoptic (49 FHR): ~61GB GRIB, ~113GB cache
```

---

## Features

### What Works
- **Dashboard**: `tools/unified_dashboard.py` — Flask + Leaflet, live at wxsection.com:5561
- **Cross-section engine**: `core/cross_section_interactive.py` — 0.5s warm renders
- **Multi-model**: HRRR, GFS, RRFS support everywhere
- **15 styles**: wind_speed, temp, theta_e, rh, q, omega, vorticity, shear, lapse_rate, cloud, cloud_total, wetbulb, icing, frontogenesis, smoke
- **Run picker**: Filtered to preload window + loaded archive cycles only
- **Archive requests**: Modal with date picker, hour selector, FHR range (admin-gated)
- **Download progress**: Shows in-flight FHRs in real-time (`Downloading F00, F01, F02, F03 from AWS archive...`)
- **Cancel jobs**: Admin can cancel pre-render and download operations via X button in progress panel
- **Auto-update**: HRRR-priority interleaved downloads, re-checks HRRR every 2 non-HRRR downloads
- **Cache-first preload**: Cached FHRs load in <1s total, GRIB conversions run in background
- **Time slider + auto-play**: 0.5x-4x speed, pre-render for instant scrubbing
- **Frame prerender cache**: 500-entry server-side cache
- **Cycle comparison mode**: Side-by-side Same FHR or Valid Time matching
- **Community favorites**: Save/load cross-section configs
- **GIF animation**: `/api/xsect_gif`
- **Admin key**: `WXSECTION_KEY=ctwc` env var gates archive downloads, cancel ops

### Controls UI
- **Primary row**: Model, Run, Style, Favorites, Swap, Clear, "More" toggle
- **Secondary row** (hidden by default): Y-Axis, V-Scale, Top, Units, Help, Request Run, GIF, Load All, Compare, Admin, Memory

---

## Files

```
start.sh                           # Startup script (mount VHD, start services)
model_config.py                     # Model registry (HRRR/GFS/RRFS metadata)
core/cross_section_interactive.py   # Main engine — mmap cache, cartopy cache, KDTree cache
smart_hrrr/orchestrator.py          # Parallel GRIB downloads (on_complete, on_start, should_cancel)
tools/auto_update.py                # HRRR-priority interleaved download daemon
tools/unified_dashboard.py          # Flask dashboard — everything UI + API
```

### Key Constants (unified_dashboard.py)
```python
PRELOAD_WORKERS = 20   # Thread workers for cached mmap loads
GRIB_WORKERS = 4       # Thread workers for GRIB-to-mmap conversion
CACHE_BASE = '/home/drew/hrrr-maps/cache/xsect'  # NVMe — fast local storage
CACHE_LIMIT_GB = 670   # ~425GB preload + ~245GB archive headroom
HRRR_HOURLY_CYCLES = 3
```

---

## Known Issues / TODO

1. **Delete orphaned VHD cache**: `rm -rf /mnt/hrrr/cache/xsect/` frees ~348GB on VHD (no longer used after NVMe migration)
2. **cfgrib is the bottleneck**: No WSL2-compatible parallelism solution found. 4 threads = ~23s/FHR on NVMe
3. **ProcessPoolExecutor broken on WSL2**: folio contention, all workers D-state. Would need native Linux or different GRIB library
4. **GRIB alternatives**: eccodes Python bindings directly (skip cfgrib/xarray overhead), or cfgrib with `indexpath=''` to skip index
5. **GFS/RRFS rendering**: Works but needs more testing at extended FHRs
6. **VHD remount required**: After every WSL/PC restart, run `start.sh` or mount manually
7. **Background rescan frequency**: HRRR every 30s, others every 60s — could be tunable
8. **Monitor NVMe space**: Full preload cache = ~400GB, eviction keeps it bounded. Monitor with `df -h /`
