# CLAUDE.md — Agent Context for wxsection.com

## Project Overview

Multi-model atmospheric cross-section generator. Users draw a line on a map, get an instant vertical cross-section from HRRR, GFS, or RRFS weather model data. Live at **wxsection.com**.

## Architecture Summary

```
tools/unified_dashboard.py    — Flask server + Leaflet UI + all API endpoints (~5000 lines)
core/cross_section_interactive.py  — Rendering engine (matplotlib + cartopy, 0.5s warm)
tools/auto_update.py          — GRIB download daemon (HRRR-priority batched)
model_config.py               — Model registry (HRRR/GFS/RRFS metadata, URLs, grids)
smart_hrrr/orchestrator.py    — Parallel GRIB download with callbacks
start.sh                      — Production startup (mount VHD, start services, cloudflared)
```

## Key Design Decisions

- **Mmap cache on NVMe**: GRIB files are converted to raw numpy arrays (2.3GB/FHR on disk, ~100MB resident RAM). This is what makes instant cross-sections possible.
- **Single-process, threaded**: WSL2 folio contention breaks ProcessPoolExecutor. Everything runs in one process with ThreadPoolExecutor.
- **HRRR-priority auto-update**: HRRR downloads in batches of 5, then yields to GFS/RRFS. Fail-fast when FHRs aren't published yet.
- **No handoff cycles**: Only one synoptic (48h) HRRR cycle, only one GFS/RRFS cycle. Previous cycles are evicted.
- **Two-tier NVMe eviction**: Rotated preload cycles always evicted. Archive request caches persist up to 670GB.

## Running Locally

```bash
cd ~/hrrr-maps && ./start.sh
# Or:
sudo mount /dev/sde /mnt/hrrr
python tools/auto_update.py --interval 2 --models hrrr,gfs,rrfs &
XSECT_GRIB_BACKEND=cfgrib WXSECTION_KEY=cwtc python3 tools/unified_dashboard.py --port 5561 --models hrrr,gfs,rrfs
```

Logs: `/tmp/dashboard.log`, `/tmp/auto_update.log`, `/tmp/cloudflared.log`

## Environment

- **WSL2** on Windows, 32 cores, 118GB RAM
- **NVMe** (2TB VHD at `/`): code + mmap cache (`~/hrrr-maps/cache/xsect/`)
- **External VHD** (20TB at `/mnt/hrrr`): GRIB source files
- **Cloudflare Tunnel**: `cloudflared tunnel run wxsection` routes wxsection.com to localhost:5561

## Performance Characteristics

| Operation | Time |
|-----------|------|
| Warm render (cached FHR) | ~0.5s |
| Cached prerender (from frame cache) | ~20ms |
| GRIB-to-mmap conversion | ~23s/FHR |
| Mmap load (cached on NVMe) | <0.1s |
| Parallel prerender (19 frames) | ~4s |
| Full preload (125 uncached FHRs) | ~48 min |

## Critical Constraints

1. **cfgrib is GIL-bound**: Can't parallelize GRIB conversion beyond 4 threads. Don't try ProcessPoolExecutor — folio contention on WSL2.
2. **matplotlib is not thread-safe**: The Agg backend works with ThreadPool but font cache can throw warnings under load. Non-fatal.
3. **Memory budget**: HRRR 48GB, GFS 8GB, RRFS 8GB. Mmap keeps resident small but monitor with `/api/status`.
4. **NVMe space**: 670GB cache limit enforced by `cache_evict_old_cycles()`. Monitor with `df -h /`.
5. **VHD must be mounted**: `/mnt/hrrr` needs `sudo mount /dev/sde /mnt/hrrr` after every WSL restart.

## Key Constants

```python
# unified_dashboard.py
RENDER_SEMAPHORE = 12      # Max concurrent matplotlib renders
PRERENDER_WORKERS = 8      # Parallel prerender threads
PRELOAD_WORKERS = 20       # Cached mmap load threads
GRIB_WORKERS = 4           # GRIB conversion threads
CACHE_LIMIT_GB = 670       # NVMe cache size limit
HRRR_HOURLY_CYCLES = 3     # Non-synoptic cycles in preload window

# auto_update.py
HRRR_BATCH_SIZE = 5        # HRRR FHRs per batch before yielding to GFS/RRFS
DISK_LIMIT_GB = 500        # GRIB source disk limit on VHD
```

## API Quick Reference

| Endpoint | Description |
|----------|-------------|
| `GET /api/v1/cross-section` | Generate cross-section PNG (agent-friendly) |
| `GET /api/v1/products` | List available visualization styles |
| `GET /api/v1/cycles` | List available model cycles |
| `GET /api/v1/status` | Server health check |
| `GET /api/xsect` | Generate cross-section PNG (internal) |
| `GET /api/cycles` | List cycles with load status |
| `GET /api/status` | Memory/load status |
| `POST /api/load` | Load specific cycle + FHR |
| `POST /api/prerender` | Batch pre-render frames |

See [API_GUIDE.md](API_GUIDE.md) for full documentation.

## Common Tasks

### Restart dashboard
```bash
pkill -f unified_dashboard; sleep 2
XSECT_GRIB_BACKEND=cfgrib WXSECTION_KEY=cwtc nohup python3 tools/unified_dashboard.py --port 5561 --models hrrr,gfs,rrfs > /tmp/dashboard.log 2>&1 &
```

### Restart auto-update
```bash
pkill -f auto_update; sleep 2
nohup python tools/auto_update.py --interval 2 --models hrrr,gfs,rrfs > /tmp/auto_update.log 2>&1 &
```

### Check what's loaded
```bash
curl -s localhost:5561/api/cycles | python3 -m json.tool
curl -s localhost:5561/api/status | python3 -m json.tool
```

### Check NVMe usage
```bash
df -h /
du -sh ~/hrrr-maps/cache/xsect/*/
```

## Known Performance Bottlenecks

1. **GRIB conversion (23s/FHR)**: cfgrib + xarray overhead. Could improve by using eccodes directly or a Rust/C GRIB reader.
2. **Matplotlib render (0.5s)**: CPU-bound. Agg backend releases GIL for some C work but font/text rendering is Python.
3. **WSL2 VHD I/O**: All disk goes through Hyper-V virtual block layer. Native Linux would be faster.
4. **GFS data volume**: 65 FHRs x 6h intervals = F00-F384. Full cycle download is large.
