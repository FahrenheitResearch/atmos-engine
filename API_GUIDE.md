# wxsection.com Cross-Section API

> **Beta** — This API is functional and actively maintained, but still in beta.
> Endpoint URLs and parameter names are stable, but response details or default
> behavior may change. No uptime SLA. If you build something on this, reach out
> so we know not to break you.

Generate atmospheric cross-section images from HRRR, GFS, and RRFS weather models between any two points. Returns publication-quality PNG images.

**Base URL:** `https://wxsection.com`

No API key required. No authentication. Free to use. CORS enabled for browser apps.

## Quick Start

Request a temperature cross-section from Denver to Chicago:

```
GET https://wxsection.com/api/v1/cross-section?start_lat=39.74&start_lon=-104.99&end_lat=41.88&end_lon=-87.63
```

Returns a PNG image. That's it.

## Endpoints

### Generate Cross-Section

```
GET /api/v1/cross-section
```

Returns a PNG image of a vertical atmospheric cross-section.

**Required Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `start_lat` | float | Start point latitude (-90 to 90) |
| `start_lon` | float | Start point longitude (-180 to 180) |
| `end_lat` | float | End point latitude |
| `end_lon` | float | End point longitude |

**Optional Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `product` | string | `temperature` | Atmospheric product to visualize (see [Products](#products)) |
| `model` | string | `hrrr` | Weather model: `hrrr`, `gfs`, or `rrfs` |
| `cycle` | string | `latest` | Model cycle key (e.g. `20260205_19z`) or `latest` |
| `fhr` | int | `0` | Forecast hour (0-48 for synoptic HRRR, 0-18 for others) |
| `y_axis` | string | `pressure` | Vertical axis: `pressure` (hPa) or `height` (km) |
| `y_top` | int | `100` | Top of plot in hPa: `100`, `200`, `300`, `500`, or `700` |
| `units` | string | `km` | Distance axis: `km` or `mi` |

**Response:**
- `200` — PNG image (`image/png`)
- `400` — Invalid parameters (JSON error with details)
- `404` — No data available for requested cycle/forecast hour
- `500` — Render or load failure
- `503` — Server busy (try again in a few seconds)

**Examples:**

```bash
# Temperature from Denver to Chicago (latest HRRR data, analysis hour)
curl -o xsect.png "https://wxsection.com/api/v1/cross-section?start_lat=39.74&start_lon=-104.99&end_lat=41.88&end_lon=-87.63"

# Wind speed, 6-hour forecast, lower atmosphere only
curl -o wind.png "https://wxsection.com/api/v1/cross-section?start_lat=33.45&start_lon=-112.07&end_lat=40.71&end_lon=-74.01&product=wind_speed&fhr=6&y_top=500"

# GFS model cross-section
curl -o gfs.png "https://wxsection.com/api/v1/cross-section?start_lat=30.0&start_lon=-95.0&end_lat=45.0&end_lon=-85.0&product=rh&model=gfs"

# RRFS model cross-section
curl -o rrfs.png "https://wxsection.com/api/v1/cross-section?start_lat=39.74&start_lon=-104.99&end_lat=41.88&end_lon=-87.63&model=rrfs&product=wind_speed"

# Specific model cycle
curl -o rh.png "https://wxsection.com/api/v1/cross-section?start_lat=30.0&start_lon=-95.0&end_lat=45.0&end_lon=-85.0&product=rh&cycle=20260205_12z"

# Height axis in miles
curl -o icing.png "https://wxsection.com/api/v1/cross-section?start_lat=42.36&start_lon=-71.06&end_lat=38.90&end_lon=-77.04&product=icing&y_axis=height&units=mi"
```

**HTML embed:**
```html
<img src="https://wxsection.com/api/v1/cross-section?start_lat=39.74&start_lon=-104.99&end_lat=41.88&end_lon=-87.63&product=temperature" alt="Cross-section">
```

---

### Generate Cross-Section GIF

```
GET /api/v1/cross-section/gif
```

Returns an animated GIF of a vertical atmospheric cross-section, cycling through a range of forecast hours. Same coordinate parameters as `/api/v1/cross-section`, plus `fhr_min` and `fhr_max` to control the animation range.

The `product` parameter maps to the visualization style internally (same values as the cross-section endpoint). If `cycle` is omitted or set to `latest`, the server auto-resolves the latest available cycle.

**Required Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `start_lat` | float | Start point latitude (-90 to 90) |
| `start_lon` | float | Start point longitude (-180 to 180) |
| `end_lat` | float | End point latitude |
| `end_lon` | float | End point longitude |

**Optional Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `product` | string | `temperature` | Atmospheric product to visualize (maps to style internally; see [Products](#products)) |
| `model` | string | `hrrr` | Weather model: `hrrr`, `gfs`, or `rrfs` |
| `cycle` | string | `latest` | Model cycle key (e.g. `20260205_19z`) or `latest` (auto-resolves) |
| `fhr_min` | int | `0` | First forecast hour in the animation |
| `fhr_max` | int | `18` | Last forecast hour in the animation |
| `y_axis` | string | `pressure` | Vertical axis: `pressure` (hPa) or `height` (km) |
| `y_top` | int | `100` | Top of plot in hPa: `100`, `200`, `300`, `500`, or `700` |
| `units` | string | `km` | Distance axis: `km` or `mi` |

**Response:**
- `200` — Animated GIF image (`image/gif`)
- `400` — Invalid parameters (JSON error with details)
- `404` — No data available for requested cycle/forecast hours
- `500` — Render or load failure
- `503` — Server busy (try again in a few seconds)

**Examples:**

```bash
# Fire weather composite GIF from OKC area, FHR 0-12
curl -o fire_wx.gif "https://wxsection.com/api/v1/cross-section/gif?product=fire_wx&model=hrrr&start_lat=35.36&start_lon=-97.6&end_lat=35.36&end_lon=-96.7&fhr_min=0&fhr_max=12"

# Temperature evolution over 24 hours (Denver to Chicago)
curl -o temp_evolution.gif "https://wxsection.com/api/v1/cross-section/gif?product=temperature&start_lat=39.74&start_lon=-104.99&end_lat=41.88&end_lon=-87.63&fhr_min=0&fhr_max=24"

# Wind speed GIF with specific cycle, lower atmosphere
curl -o wind.gif "https://wxsection.com/api/v1/cross-section/gif?product=wind_speed&start_lat=33.45&start_lon=-112.07&end_lat=40.71&end_lon=-74.01&cycle=20260205_12z&fhr_min=0&fhr_max=18&y_top=500"
```

**HTML embed:**
```html
<img src="https://wxsection.com/api/v1/cross-section/gif?product=fire_wx&start_lat=35.36&start_lon=-97.6&end_lat=35.36&end_lon=-96.7&fhr_min=0&fhr_max=12" alt="Fire weather GIF">
```

---

### Get Numerical Data

```
GET /api/v1/data
```

Returns raw numerical cross-section data as JSON arrays. Same coordinate parameters as `/api/v1/cross-section`. This is the research powerhouse — returns the actual interpolated values that make up a cross-section.

**Required Parameters:** Same as cross-section (`start_lat`, `start_lon`, `end_lat`, `end_lon`).

**Optional Parameters:** Same as cross-section (`product`, `model`, `cycle`, `fhr`, `y_axis`, `y_top`, `units`).

**Response:**
```json
{
  "distances_km": [0.0, 5.2, 10.4, ...],
  "pressure_levels_hpa": [1000, 975, 950, ...],
  "lats": [39.74, 39.76, ...],
  "lons": [-104.99, -104.85, ...],
  "temperature_c": [[15.2, 15.1, ...], ...],
  "surface_pressure_hpa": [840.5, 842.1, ...],
  "metadata": {
    "model": "hrrr",
    "cycle": "20260205_19z",
    "fhr": 0,
    "valid_time": "2026-02-05T19:00Z",
    "product": "temperature",
    "style": "temp",
    "distance_km": 1492.3,
    "n_points": 497,
    "n_levels": 40,
    "fields": [{"key": "temperature_c", "units": "°C"}]
  }
}
```

Data arrays are 2D `[n_levels × n_points]` (~40 × ~200 = 8,000 values per field, ~64KB JSON).

**Field names by product:**

| Product | JSON field(s) | Units |
|---------|--------------|-------|
| `temperature` | `temperature_c` | °C |
| `wind_speed` | `u_wind_ms`, `v_wind_ms` | m/s |
| `theta_e` | `theta_e_k` | K |
| `rh` | `rh_pct` | % |
| `omega` | `omega_hpa_hr` | hPa/hr |
| `q` | `specific_humidity_gkg` | g/kg |
| `vorticity` | `vorticity_1e5_s` | 10⁻⁵ s⁻¹ |
| `shear` | `shear_1e3_s` | 10⁻³ s⁻¹ |
| `lapse_rate` | `lapse_rate_c_km` | °C/km |
| `cloud_total` | `cloud_total_gkg` | g/kg |
| `wetbulb` | `wetbulb_c` | °C |
| `icing` | `icing_gkg` | g/kg |
| `smoke` | `smoke_hyb` | μg/m³ |
| `vpd` | `vpd_hpa` | hPa |
| `dewpoint_dep` | `dewpoint_dep_c` | °C |
| `moisture_transport` | `moisture_transport_gmkgs` | g·m/kg/s |
| `pv` | `pv_pvu` | PVU |
| `fire_wx` | `rh_pct` | % |

**Example:**
```bash
curl "https://wxsection.com/api/v1/data?start_lat=39.74&start_lon=-104.99&end_lat=41.88&end_lon=-87.63&product=temperature" | python -m json.tool
```

---

### List Events

```
GET /api/v1/events
GET /api/v1/events?category=hurricane
GET /api/v1/events?has_data=true
```

Browse 85+ curated historical weather events (fires, hurricanes, tornadoes, derechos, hail, atmospheric rivers, winter storms).

**Optional Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` | string | Filter by category: `fire-ca`, `fire-pnw`, `fire-co`, `fire-sw`, `hurricane`, `tornado`, `derecho`, `hail`, `ar`, `winter`, `other` |
| `has_data` | bool | If `true`, only events with data currently available on the server |

**Response:**
```json
{
  "events": [
    {
      "cycle_key": "20250107_00z",
      "name": "LA Santa Ana Outbreak (Palisades/Eaton)",
      "category": "fire-ca",
      "date_local": "2025-01-07",
      "notes": "Peak morning to daytime winds",
      "why": "LA-area Santa Ana outbreak (Palisades/Eaton etc. starting Jan 7-9)",
      "has_data": false,
      "coordinates": {
        "center": [34.10, -118.20],
        "suggested_sections": [
          {"label": "NE-SW Santa Ana wind corridor", "start": [34.60, -117.50], "end": [33.70, -118.80], "products": ["wind_speed", "fire_wx", "rh"]}
        ]
      }
    }
  ],
  "count": 88
}
```

---

### Get Event Detail

```
GET /api/v1/events/<cycle_key>
```

Get detailed information about a specific event, including available forecast hours and suggested cross-section paths.

**Response:**
```json
{
  "cycle_key": "20250107_00z",
  "name": "LA Santa Ana Outbreak (Palisades/Eaton)",
  "category": "fire-ca",
  "date_local": "2025-01-07",
  "notes": "Peak morning to daytime winds",
  "why": "LA-area Santa Ana outbreak (Palisades/Eaton etc. starting Jan 7-9)",
  "has_data": false,
  "available_fhrs": [],
  "coordinates": {
    "center": [34.10, -118.20],
    "suggested_sections": [...]
  },
  "available_products": [{"id": "temperature", "name": "Temperature", "units": "°C"}, ...]
}
```

---

### Event Categories

```
GET /api/v1/events/categories
```

**Response:**
```json
{
  "categories": [
    {"category": "ar", "count": 5},
    {"category": "derecho", "count": 10},
    {"category": "fire-ca", "count": 14},
    {"category": "hurricane", "count": 15},
    {"category": "tornado", "count": 20}
  ]
}
```

---

### Capabilities

```
GET /api/v1/capabilities
```

Machine-readable parameter constraints for agents. Returns models, products, valid parameter values, coordinate bounds, and rate limits.

**Response:**
```json
{
  "models": [
    {
      "id": "hrrr",
      "name": "HRRR (High-Resolution Rapid Refresh)",
      "resolution": "3km",
      "domain": "CONUS",
      "forecast_hours": {"base": [0,1,2,...,18], "synoptic_max": 48},
      "synoptic_hours": [0, 6, 12, 18],
      "excluded_products": [],
      "available_cycles": 12
    }
  ],
  "products": [{"id": "temperature", "name": "Temperature", "units": "°C"}, ...],
  "parameters": {
    "y_axis": {"values": ["pressure", "height"], "default": "pressure"},
    "y_top": {"values": [100, 200, 300, 500, 700], "default": 100, "units": "hPa"},
    "units": {"values": ["km", "mi"], "default": "km"}
  },
  "coordinate_bounds": {"south": 21.14, "north": 52.62, "west": -134.10, "east": -60.92},
  "rate_limits": {"requests_per_minute": 60, "burst_per_second": 10},
  "event_count": 88
}
```

---

### Tool Schemas (Anthropic Format)

```
GET /api/v1/tools
```

Export Anthropic `tool_use` compatible JSON schemas for all wxsection API operations. Copy these directly into agent configurations.

**Response:**
```json
{
  "tools": [
    {
      "name": "wxsection_cross_section",
      "description": "Generate a PNG atmospheric cross-section...",
      "input_schema": {
        "type": "object",
        "properties": {...},
        "required": ["start_lat", "start_lon", "end_lat", "end_lon"]
      }
    },
    {
      "name": "wxsection_data",
      "description": "Get raw numerical atmospheric data...",
      "input_schema": {...}
    }
  ],
  "format": "anthropic_tool_use"
}
```

---

### List Products

```
GET /api/v1/products
```

Returns the list of available atmospheric products.

**Response:**
```json
{
  "products": [
    {"id": "temperature", "name": "Temperature", "units": "°C"},
    {"id": "wind_speed", "name": "Wind Speed", "units": "knots"},
    {"id": "theta_e", "name": "Equivalent Potential Temperature", "units": "K"},
    {"id": "rh", "name": "Relative Humidity", "units": "%"},
    {"id": "omega", "name": "Vertical Velocity", "units": "hPa/hr"},
    {"id": "q", "name": "Specific Humidity", "units": "g/kg"},
    {"id": "vorticity", "name": "Absolute Vorticity", "units": "10⁻⁵ s⁻¹"},
    {"id": "shear", "name": "Wind Shear", "units": "10⁻³ s⁻¹"},
    {"id": "lapse_rate", "name": "Lapse Rate", "units": "°C/km"},
    {"id": "cloud_total", "name": "Cloud Total Condensate", "units": "g/kg"},
    {"id": "wetbulb", "name": "Wet-Bulb Temperature", "units": "°C"},
    {"id": "icing", "name": "Icing Potential", "units": "g/kg"},
    {"id": "frontogenesis", "name": "Frontogenesis", "units": "K/100km/3hr"},
    {"id": "smoke", "name": "PM2.5 Smoke", "units": "μg/m³"},
    {"id": "vpd", "name": "Vapor Pressure Deficit", "units": "hPa"},
    {"id": "dewpoint_dep", "name": "Dewpoint Depression", "units": "°C"},
    {"id": "moisture_transport", "name": "Moisture Transport", "units": "g·m/kg/s"},
    {"id": "pv", "name": "Potential Vorticity", "units": "PVU"},
    {"id": "fire_wx", "name": "Fire Weather", "units": "composite"}
  ]
}
```

---

### List Available Cycles

```
GET /api/v1/cycles
GET /api/v1/cycles?model=gfs
```

Returns available model cycles and their forecast hours. Use `model` parameter to query a specific model (default: hrrr).

**Response:**
```json
{
  "cycles": [
    {
      "key": "20260205_19z",
      "display": "HRRR - Feb 05 19Z",
      "forecast_hours": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
      "loaded": true
    }
  ],
  "latest": "20260205_19z"
}
```

- `key` — Use this as the `cycle` parameter in cross-section requests
- `forecast_hours` — Available forecast hours for this cycle
- `loaded` — Whether the data is already in memory (faster response if true)
- `latest` — The newest available cycle key

---

### Server Status

```
GET /api/v1/status
```

Health check and basic server info.

**Response:**
```json
{
  "ok": true,
  "loaded_count": 220,
  "memory_mb": 6400,
  "latest_cycle": "20260205_19z"
}
```

---

## MCP Server & AI Agent Platform

A full AI-agent research platform is available with 22 MCP tools, 6 Python API modules, fire weather assessment, external data ingestion, report generation, and more.

**Full documentation:** [AGENT_GUIDE.md](AGENT_GUIDE.md)

**MCP Configuration** (Claude Code `~/.claude/claude_code_config.json`):
```json
{
  "mcpServers": {
    "wxsection": {
      "command": "python",
      "args": ["C:/Users/drew/hrrr-maps/tools/mcp_server.py"],
      "env": {
        "WXSECTION_API_BASE": "http://localhost:5565",
        "GOOGLE_STREET_VIEW_KEY": "your-key-here"
      }
    }
  }
}
```

**28 MCP tools across 5 categories:**
- **Investigation (6):** `investigate_location`, `investigate_town`, `compare_model_obs`, `get_point_forecast`, `batch_investigate`, `generate_cross_section_gif`
- **Cross-Section (9):** `get_capabilities`, `list_events`, `get_event`, `list_cycles`, `list_products`, `generate_cross_section`, `generate_cross_section_gif`, `get_atmospheric_data`, `get_status`
- **External Data (9):** `get_metar`, `find_stations`, `get_raws`, `get_spc_fire_outlook`, `get_spc_discussion`, `get_nws_alerts`, `get_forecast_discussion`, `get_elevation`, `get_drought`
- **Fire Weather (4):** `assess_fire_risk`, `national_fire_scan`, `compute_fire_indices`, `sub_metro_fire_scan`
- **Street View (2):** `get_street_view`, `get_street_view_panorama`

---

## Products

| Product ID | Description |
|-----------|-------------|
| `temperature` | Temperature with theta contours and freezing level |
| `wind_speed` | Wind speed magnitude with wind barbs |
| `theta_e` | Equivalent potential temperature (instability analysis) |
| `rh` | Relative humidity (dry/moist air boundaries) |
| `omega` | Vertical velocity (rising/sinking motion) |
| `q` | Specific humidity (moisture content) |
| `vorticity` | Absolute vorticity (rotation) |
| `shear` | Wind shear (change in wind with height) |
| `lapse_rate` | Temperature lapse rate (stability) |
| `cloud_total` | Total condensate (cloud + rain + snow + graupel) |
| `wetbulb` | Wet-bulb temperature with critical 0C line |
| `icing` | Icing potential (supercooled liquid water) |
| `frontogenesis` | Frontogenesis (frontal zone strengthening) |
| `smoke` | PM2.5 smoke concentration (HRRR-Smoke) |
| `vpd` | Vapor pressure deficit |
| `dewpoint_dep` | Dewpoint depression (T minus Td) |
| `moisture_transport` | Moisture transport (q x wind speed) |
| `pv` | Potential vorticity |
| `fire_wx` | Fire weather composite (VPD + wind + RH) |

All products include terrain shading, wind barbs, theta contours, and the 0C freezing level.

## Coverage

| Model | Resolution | Domain | Cycles | Forecast Hours |
|-------|-----------|--------|--------|----------------|
| **HRRR** | 3km | CONUS | Hourly (24/day) | F00-F18 (F00-F48 for 00/06/12/18z) |
| **GFS** | 0.25deg | Global | 4x/day (00/06/12/18z) | F00-F48 |
| **RRFS** | 3km | CONUS | Hourly (24/day) | F00-F18 |

- **Vertical:** 40 pressure levels, 1000 hPa to 50 hPa
- Typically 12+ recent cycles available per model

## Rate Limits

- 60 requests per minute per IP
- Burst: 10 requests per second
- Max 4 concurrent renders server-wide
- If you get a `503`, wait a few seconds and retry

## Notes

- Cross-section renders take ~0.5 seconds when data is loaded (prerendered cache: ~20ms)
- First request for an unloaded cycle may take 10-30 seconds (one-time GRIB-to-mmap conversion)
- Subsequent requests for the same cycle are fast
- Images are 1700x1100 PNG, typically 300-500 KB
- The `cycle=latest` default is recommended for most use cases
- HRRR/RRFS: points must be within the CONUS domain. GFS: global coverage
- CORS is enabled on all `/api/v1/` endpoints — safe to call from browser JavaScript
- This API is in **beta** — core functionality is stable but minor details may evolve
