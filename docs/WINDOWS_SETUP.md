# Windows Native Setup

Run wxsection.com on native Windows (no WSL2 required).

## Prerequisites

1. **Python 3.10+** (Anaconda/Miniconda recommended)
2. **eccodes** - GRIB decoding library

## Install

```powershell
# Clone
git clone https://github.com/<your-org>/hrrr-maps.git
cd hrrr-maps
git checkout windows

# Create conda env (recommended for eccodes)
conda create -n wxsection python=3.11 eccodes -c conda-forge -y
conda activate wxsection

# Install Python deps
pip install flask numpy matplotlib cartopy xarray cfgrib scipy pillow imageio
```

## Environment Variables

All paths that were previously hardcoded to Linux locations are now configurable via env vars. On Windows, set these before running:

| Variable | Purpose | Default |
|---|---|---|
| `XSECT_CACHE_DIR` | NVMe mmap cache directory | `<repo>/cache/xsect` |
| `XSECT_STATUS_FILE` | auto_update IPC status file | `%TEMP%\auto_update_status.json` |
| `XSECT_CLIMATOLOGY_DIR` | Climatology data (optional) | `/mnt/hrrr/climatology` |
| `XSECT_ARCHIVE_DIR` | Archive GRIB storage (optional) | `/mnt/hrrr/hrrr-archive-events` |
| `XSECT_LIVE_DIR` | Live GRIB symlink dir (optional) | `/mnt/hrrr/hrrr-live` |
| `XSECT_OUTPUTS_DIR` | GRIB download output dir | `outputs` (relative) |
| `XSECT_GRIB_BACKEND` | GRIB backend: `auto`, `eccodes`, `cfgrib` | `auto` |
| `WXSECTION_KEY` | Admin API key | (required) |

For basic operational use, only `WXSECTION_KEY` and `XSECT_GRIB_BACKEND` are needed - the rest default to sensible locations relative to the repo root.

## Run

```powershell
# Quick start
.\start_windows.ps1

# Or manually:
$env:XSECT_GRIB_BACKEND = "auto"
$env:WXSECTION_KEY = "cwtc"
python tools/unified_dashboard.py --port 5561 --models hrrr,gfs,rrfs
```

## Verify

```powershell
# Check dashboard is running
Invoke-RestMethod http://localhost:5561/api/v1/status

# List available models
Invoke-RestMethod http://localhost:5561/api/v1/products

# List cycles
Invoke-RestMethod http://localhost:5561/api/v1/cycles
```

## What Works on Windows

- Dashboard (Flask server + all API endpoints)
- GRIB loading via eccodes/cfgrib (no wgrib2 needed - it's auto-detected)
- Mmap cache (numpy mmap works identically on Windows)
- All 20 visualization styles
- Auto-update daemon (downloads from NOMADS/AWS)
- Prerender pipeline
- Archive event browsing (from cached data)

## What Doesn't Work (Yet)

- **wgrib2 strategies**: wgrib2 is Linux-only. The code auto-detects this and falls back to eccodes/cfgrib. Only affects the `smoke` style's COLMD field (column-integrated smoke).
- **Symlinks for archive events**: `os.symlink()` requires elevated privileges on Windows. Archive download scripts skip symlinking if it fails.
- **Cloudflare tunnel**: Use your own tunneling solution or access via `localhost:5561`.

## Troubleshooting

**"No module named 'eccodes'"**: Install via conda, not pip:
```powershell
conda install eccodes -c conda-forge
```

**Dashboard won't start**: Check that port 5561 isn't in use:
```powershell
netstat -ano | findstr :5561
```

**Empty cycles list**: auto_update.py needs to download at least one FHR first. Check:
```powershell
python tools/auto_update.py --once --models hrrr
```
