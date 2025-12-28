# Cross-Section Dashboard Context

## Current State (Dec 27, 2025)

### Branch: `focused/cross-section-dashboard`

Stripped-down repo focused on interactive cross-sections only.

### What Works
- Dashboard at `tools/unified_dashboard.py` (475 lines)
- Cross-section generation via `core/cross_section_interactive.py`
- NPZ caching in `cache/dashboard/xsect/` (~3s per hour from cache)
- 7 styles: wind_speed, temp, theta_e, rh, omega, vorticity, cloud
- GRIB downloads via `smart_hrrr/orchestrator.py`

### Files (14 Python files)
```
config/colormaps.py
core/cross_section_interactive.py  # Main engine - get_cross_section()
core/cross_section_production.py
core/downloader.py
core/grib_loader.py
model_config.py
smart_hrrr/availability.py
smart_hrrr/io.py
smart_hrrr/orchestrator.py
smart_hrrr/utils.py
tools/auto_update.py
tools/unified_dashboard.py
```

### Key APIs
- `InteractiveCrossSection.get_cross_section(start_point, end_point, style, forecast_hour)` returns PNG bytes
- `download_gribs_parallel(model, date_str, cycle_hour, forecast_hours)` downloads GRIBs

### TODO
1. ~~Fix UI - make cross-section bigger, map smaller~~ DONE - sidebar now 55% width
2. ~~Add draggable markers~~ DONE - markers are now draggable, line updates on drag
3. Test and refine as needed

### Previous Branches
- `experimental/unified-dashboard` - full dashboard with map overlays
- `feature/interactive-maps` - earlier work
- `master` - main branch

### Data Location
- GRIB files: `outputs/hrrr/YYYYMMDD/HHz/F##/`
- NPZ cache: `cache/dashboard/xsect/`

### Running Dashboard
```bash
python tools/unified_dashboard.py --data-dir outputs/hrrr/20251227/09z --port 5559 --max-hours 4
```
