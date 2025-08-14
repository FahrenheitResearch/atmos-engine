# Weather Model Processing System

A high-performance, extensible system for downloading, processing, and visualizing weather model data from NOAA's HRRR (High-Resolution Rapid Refresh), RRFS (Rapid Refresh Forecast System), and GFS (Global Forecast System) models. Generates publication-quality meteorological maps with support for 98+ weather parameters.

## 🚀 Key Features

- **Multi-Model Support**: HRRR, RRFS, and GFS models
- **98+ Weather Parameters**: Including severe weather indices, instability parameters, smoke/fire products
- **Pure NumPy Performance**: Optimized meteorological calculations without external dependencies
- **Parallel Processing**: 8x faster map generation using multiprocessing
- **Smart Caching**: Avoids reprocessing completed products
- **Continuous Monitoring**: Automatically process new model runs as they become available
- **Modular Architecture**: Clean, maintainable code organized in focused modules
- **Professional Visualizations**: SPC-style plots with customizable colormaps

## 📁 Project Structure

```
hrrr-manual-4/
├── processor_cli.py              # Main CLI (70 lines - thin wrapper)
├── processor_batch.py            # Batch processing (19 lines - thin wrapper)
├── processor_base.py             # Base processor (13 lines - thin wrapper)
├── smart_hrrr/                   # 🆕 NEW: Modular architecture package
│   ├── __init__.py               # Package exports
│   ├── utils.py                  # Utility functions (logging, memory, parsing)
│   ├── products.py               # Product management and availability
│   ├── io.py                     # I/O operations and directory structure
│   ├── availability.py           # Cycle detection and availability checks
│   ├── derived.py                # Derived parameter computation logic
│   ├── processor_core.py         # Slim HRRRProcessor core
│   ├── orchestrator.py           # Process orchestration and workflows
│   └── parallel_engine.py        # Parallel processing engine
├── monitor_continuous.py         # Continuous monitoring for new model runs
├── field_registry.py             # Dynamic field configuration system
├── field_templates.py            # Reusable parameter templates
├── model_config.py              # Model-specific configurations (URLs, patterns)
├── map_enhancer.py              # Modern map styling enhancements
├── config/
│   ├── colormaps.py             # Custom colormaps for weather parameters
├── core/
│   ├── downloader.py            # GRIB file download management
│   ├── grib_loader.py           # GRIB data extraction with cfgrib
│   ├── metadata.py              # Metadata generation for products
│   └── plotting.py              # Map generation with Cartopy
├── derived_params/              # 70+ derived parameter calculations
├── parameters/                  # JSON configuration files by category
│   ├── severe.json             # Severe weather parameters
│   ├── instability.json        # CAPE, CIN, stability indices
│   ├── smoke.json              # Fire and smoke products
│   └── ...                     # Additional categories
├── tools/
│   ├── process_all_products.py # Batch processing utilities
│   ├── process_single_hour.py  # Single forecast hour processing
│   ├── create_gifs.py          # 🎬 Automated GIF/animation generation
│   └── hrrr_gif_maker.py       # Core GIF creation engine
└── outputs/                     # Generated products (organized by date/model/hour)
```

### 🏗️ Architecture Improvements (Latest Refactor)

**Modular Design**: The codebase has been refactored from monolithic files (~2800 LOC) into a clean, modular `smart_hrrr/` package:

- **Maintainability**: Each module has a single responsibility
- **Testability**: Isolated functions are easier to test
- **Extensibility**: Add new features without touching existing code
- **Backward Compatibility**: All existing commands work unchanged

#### Smart HRRR Modules

| Module | Purpose | Key Functions |
|--------|---------|---------------|
| `utils.py` | Common utilities | Logging setup, memory checks, hour parsing |
| `products.py` | Product management | Check existing products, find missing items |
| `io.py` | File operations | Directory structure, GRIB staging, cleanup |
| `availability.py` | Data availability | Latest cycle detection, forecast hour checks |
| `derived.py` | Heavy computations | Derived parameter and composite calculations |
| `processor_core.py` | Core processor | Slim HRRRProcessor class (delegates to other modules) |
| `orchestrator.py` | Workflow control | Process orchestration, parallel coordination |
| `parallel_engine.py` | Performance | Optimized parallel map generation |

## 🛠️ Installation

```bash
# Clone the repository
git clone <repository-url> hrrr-dr-4
cd hrrr-dr-4

# Create conda environment
conda create -n hrrr_maps python=3.11
conda activate hrrr_maps

# Install dependencies
conda install -c conda-forge cartopy cfgrib matplotlib xarray numpy pandas
pip install psutil requests

# Note: MetPy is no longer required - all calculations use optimized pure NumPy
```

## 📊 Available Weather Parameters

### Categories:
- **Severe Weather** (27 params): STP, SCP, SHIP, EHI, bulk shear, effective layer parameters
- **Instability** (9 params): CAPE/CIN (surface-based, mixed-layer, most-unstable), LCL, LI
- **Surface** (10 params): Temperature, dewpoint, pressure, winds, relative humidity
- **Upper Air** (10 params): Heights, temperatures, winds at standard levels
- **Precipitation** (2 params): Instantaneous rate, accumulated total
- **Reflectivity** (3 params): Composite, 1km AGL, 4km AGL
- **Smoke/Fire** (6 params): Near-surface smoke, visibility, fire weather indices
- **Composites** (9 params): Multi-parameter visualizations with overlays
- **Heat Stress** (5 params): Wet bulb temperature, WBGT, heat indices
- **Updraft Helicity** (5 params): Various layer calculations for tornado potential

## 🎯 Command Examples

### Basic Processing

```bash
# Process latest available HRRR run (all products)
python processor_cli.py --latest

# Process specific date/hour
python processor_cli.py 20250715 12

# Process only specific categories
python processor_cli.py 20250715 12 --categories severe,instability

# Process specific parameters
python processor_cli.py 20250715 12 --fields sbcape,sbcin,stp,reflectivity_comp

# Process specific forecast hours (default is F00-F18)
python processor_cli.py 20250715 12 --hours 0-6

# Process extended forecast (for 00z, 06z, 12z, 18z runs)
python processor_cli.py 20250715 12 --hours 0-48
```


### Model Selection

```bash
# Process RRFS model (experimental)
python processor_cli.py --latest --model rrfs

# Process GFS model
python processor_cli.py --latest --model gfs
```

### Parallel Processing Control

```bash
# Use 4 worker processes (default: auto-detect)
python processor_cli.py --latest --workers 4

# Force reprocess all products (ignore existing)
python processor_cli.py 20250715 12 --force

# Enable debug logging
python processor_cli.py --latest --debug

# Enable detailed meteorological debugging
HRRR_DEBUG=1 python processor_cli.py --latest
```

### Continuous Monitoring

```bash
# Monitor and process new HRRR runs as they arrive
python monitor_continuous.py

# The monitor will:
# - Check for new data every 10 seconds
# - Process only missing forecast hours
# - Show progress for each cycle
# - Continue from previous cycle if new data isn't ready
```

### Creating Animations (GIFs)

```bash
# Step 1: Generate images for multiple forecast hours
python processor_cli.py 20250813 21 --hours 0-12 --categories smoke

# Step 2: Create animated GIFs
cd tools
python create_gifs.py 20250813 21z --categories smoke --max-hours 12

# Create GIFs for all categories
python create_gifs.py 20250813 21z

# Create faster animations (300ms per frame instead of 250ms)
python create_gifs.py 20250813 21z --duration 300

# Create animations for specific categories only
python create_gifs.py 20250813 21z --categories severe,instability,smoke
```

**Output:** GIFs are saved to `outputs/hrrr/YYYYMMDD/HHz/animations/category/`

### Advanced Features

```bash
# Generate all products for a full model run (parallel processing)
python processor_cli.py 20250715 12 --workers 8

# Create custom filter for specific use case
# Edit custom_filters.json, then:
python processor_cli.py --latest --filter "Severe Weather Core"

# Process with specific output directory
python processor_cli.py --latest --output-dir /path/to/output
```

## 🔧 Configuration

### Adding New Parameters

1. **For base GRIB fields**, add to appropriate JSON in `parameters/`:
```json
{
  "my_new_field": {
    "var": "GRIB_VARIABLE_NAME",
    "level": "2 m above ground",
    "cmap": "viridis",
    "title": "My New Field",
    "units": "units"
  }
}
```

2. **For derived parameters**, create a file in `derived_params/`:
```python
# derived_params/my_calculation.py
from .common import _dbg
import numpy as np

def my_calculation(input1: np.ndarray, input2: np.ndarray) -> np.ndarray:
    """Calculate my custom parameter"""
    _dbg("Computing my_calculation with pure NumPy")
    return input1 + input2 * 2.5
```

Then add to `parameters/derived.json`:
```json
{
  "my_derived_field": {
    "derived": true,
    "function": "my_calculation",
    "inputs": ["base_field1", "base_field2"],
    "title": "My Derived Field",
    "units": "custom units",
    "cmap": "RdBu_r"
  }
}
```


### Custom Colormaps

Add new colormaps in `config/colormaps.py` for specialized visualizations.

## 📈 Performance Optimization

- **Pure NumPy Operations**: Vectorized meteorological calculations (10x+ faster than MetPy)
- **Parallel Processing**: Automatically uses N-1 CPU cores (max 8)
- **Smart Caching**: Skips already-processed products
- **Batch Loading**: Loads all GRIB fields once, then generates all products
- **Memory Efficient**: Processes one forecast hour at a time
- **Optimized Algorithms**: Mixed-phase psychrometrics, vectorized lapse-rate interpolation

### Recent Performance Improvements (v2.1)

| Parameter | Before (MetPy) | After (Pure NumPy) | Speedup |
|-----------|---------------|-------------------|---------|
| `wet_bulb_temperature` | ~80ms/52k pts | ~35ms/52k pts | **2.3x faster** |
| `lapse_rate_03km` | ~150ms/52k pts | ~17ms/52k pts | **8.8x faster** |
| `mixing_ratio_2m` | ~45ms/52k pts | ~12ms/52k pts | **3.8x faster** |

**Accuracy**: All calculations maintain scientific accuracy with residuals < 1e-6

## 🗄️ Output Structure

```
outputs/
└── hrrr/
    └── 20250715/           # Date
        └── 12z/            # Model run hour
            ├── F00/        # Forecast hour directories
            ├── F01/
            ├── F02/
            │   └── conus/  # Fixed output region
            │       └── F02/
            │           ├── severe/       # Category folders
            │           ├── instability/
            │           ├── surface/
            │           └── metadata/     # JSON metadata for each product
            ├── animations/ # 🎬 Animated GIFs (created with tools/create_gifs.py)
            │   ├── severe/
            │   │   ├── stp_20250715_12z_animation.gif
            │   │   └── scp_20250715_12z_animation.gif
            │   ├── smoke/
            │   │   ├── near_surface_smoke_20250715_12z_animation.gif
            │   │   └── visibility_smoke_20250715_12z_animation.gif
            │   └── instability/
            └── logs/       # Processing logs
```

## 🔄 Migration Notes

### Deprecated Functions (v2.1)

If you're using the old MetPy-dependent functions, update your code:

```python
# OLD (deprecated, but still works with warning)
from derived_params import wet_bulb_temperature_metpy
wb = wet_bulb_temperature_metpy(temp_2m, dewpoint_2m, pressure)

# NEW (recommended)
from derived_params import wet_bulb_temperature
wb = wet_bulb_temperature(temp_2m, dewpoint_2m, pressure)
```

See [MIGRATION.md](MIGRATION.md) for detailed migration guide.

## 🔍 Troubleshooting

```bash
# Check if data is available for a specific cycle
python processor_cli.py 20250715 12 --check-availability

# View all available parameters
python processor_cli.py --list-fields

# View parameters by category
python processor_cli.py --list-fields --category severe

# Test single parameter processing
python processor_cli.py --latest --fields sbcape --debug

# Run verification tests
PYTHONPATH=. python tests/test_metpy_free_refactor.py

# Check what GIFs exist for a model run
ls outputs/hrrr/20250813/21z/animations/*/

# Test GIF creation for a single category
cd tools && python create_gifs.py 20250813 21z --categories smoke --max-hours 2
```

## 📝 Notes

- HRRR data is typically available 45-75 minutes after the model run time
- NOMADS (primary source) keeps ~2 days of data
- AWS S3 (backup source) has historical data
- GFS and RRFS have different schedules and forecast lengths
- All derived parameters use optimized pure NumPy (no external meteorological libraries required)

## 🚦 Environment Variables

```bash
# Disable parallel processing
export HRRR_USE_PARALLEL=false

# Set custom number of workers
export HRRR_MAX_WORKERS=4

# Change default model
export HRRR_DEFAULT_MODEL=rrfs

# Enable detailed meteorological calculation logging
export HRRR_DEBUG=1  # or true/yes/on
```

## 📜 License

[Your license here]

## 🤝 Contributing

Contributions welcome! Please ensure new parameters include:
- Proper metadata in JSON configuration
- Documentation of calculations
- Appropriate colormaps and units
- Test coverage for derived parameters