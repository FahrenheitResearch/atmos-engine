# wxsection.com Cross-Section API

> **Beta** — This API is functional and actively maintained, but still in beta.
> Endpoint URLs and parameter names are stable, but response details or default
> behavior may change. No uptime SLA. If you build something on this, reach out
> so we know not to break you.

Generate atmospheric cross-section images from 6 NWP models (HRRR, GFS, RRFS, NAM, RAP, NAM-Nest) between any two points. Returns publication-quality PNG images.

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
| `model` | string | `hrrr` | Weather model: `hrrr`, `gfs`, `rrfs`, `nam`, `rap`, or `nam_nest` |
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

### List Products

```
GET /api/v1/products
```

Returns the list of available atmospheric products.

**Response:**
```json
{
  "products": [
    {"id": "temperature", "name": "Temperature", "units": "\u00b0C"},
    {"id": "wind_speed", "name": "Wind Speed", "units": "knots"},
    {"id": "theta_e", "name": "Equivalent Potential Temperature", "units": "K"},
    {"id": "rh", "name": "Relative Humidity", "units": "%"},
    {"id": "omega", "name": "Vertical Velocity", "units": "hPa/hr"},
    {"id": "q", "name": "Specific Humidity", "units": "g/kg"},
    {"id": "vorticity", "name": "Absolute Vorticity", "units": "10\u207b\u2075 s\u207b\u00b9"},
    {"id": "shear", "name": "Wind Shear", "units": "10\u207b\u00b3 s\u207b\u00b9"},
    {"id": "lapse_rate", "name": "Lapse Rate", "units": "\u00b0C/km"},
    {"id": "cloud_total", "name": "Cloud Total Condensate", "units": "g/kg"},
    {"id": "wetbulb", "name": "Wet-Bulb Temperature", "units": "\u00b0C"},
    {"id": "icing", "name": "Icing Potential", "units": "g/kg"},
    {"id": "frontogenesis", "name": "Frontogenesis", "units": "K/100km/3hr"},
    {"id": "smoke", "name": "PM2.5 Smoke", "units": "\u03bcg/m\u00b3"},
    {"id": "vpd", "name": "Vapor Pressure Deficit", "units": "hPa"},
    {"id": "dewpoint_dep", "name": "Dewpoint Depression", "units": "\u00b0C"},
    {"id": "moisture_transport", "name": "Moisture Transport", "units": "g\u00b7m/kg/s"},
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

### Generate Cross-Section GIF

```
GET /api/v1/cross-section/gif
```

Returns an animated GIF cycling through forecast hours for a given transect and product.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `start_lat`, `start_lon`, `end_lat`, `end_lon` | float | — | Transect endpoints |
| `product` | string | `wind_speed` | Atmospheric product |
| `model` | string | `hrrr` | Weather model |
| `cycle` | string | `latest` | Model cycle |
| `fhr_min` | int | — | Optional: minimum FHR to include |
| `fhr_max` | int | — | Optional: maximum FHR to include |
| `speed` | string | `0.5` | Frame speed: `1`, `0.75`, `0.5`, `0.25` |

**Response:** `200` — GIF image (`image/gif`)

---

### Multi-Panel Comparison

```
GET /api/v1/comparison
```

Returns a multi-panel PNG comparing models, forecast hours, products, or cycles.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `mode` | string | — | `model`, `temporal`, `product`, or `cycle` |
| `start_lat`, `start_lon`, `end_lat`, `end_lon` | float | — | Transect endpoints |
| `product` | string | `temperature` | Atmospheric product |
| `fhr` | int | `0` | Forecast hour |
| `model` | string | `hrrr` | Primary model |
| `models` | string | — | Comma-separated models (for `model` mode, e.g. `hrrr,gfs,rrfs`) |
| `fhrs` | string | — | Comma-separated FHRs (for `temporal` mode, e.g. `0,6,12`) |
| `products` | string | — | Comma-separated products (for `product` mode) |
| `cycles` | string | — | Comma-separated cycles (for `cycle` mode) |

**Response:** `200` — PNG image (`image/png`)

---

### Browse Events

```
GET /api/v1/events
GET /api/v1/events?category=fire
GET /api/v1/events?limit=10
```

Browse the archive of 88 curated weather events.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `category` | string | — | Filter by category: `fire`, `hurricane`, `tornado`, `derecho`, `winter`, `ar` |
| `limit` | int | — | Limit number of results |
| `has_data` | bool | — | Only show events with archive data loaded |

**Response:** JSON with event metadata, coordinates, suggested cross-sections.

---

### Map Overlay Frame

```
GET /api/v1/map-overlay/frame
```

Returns a server-rendered PNG map overlay (plan-view composite or individual field).

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `model` | string | `hrrr` | Weather model |
| `product` | string | `surface_analysis` | Composite product preset |
| `fhr` | int | `0` | Forecast hour |
| `cycle` | string | `latest` | Model cycle |

**Response:** `200` — PNG image (`image/png`)

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
| **RRFS** | 3km | CONUS | 00-12z hourly, 15/18/21z | F00-F18 (F00-F60 hourly + F63-F84 3h for 00/06/12/18z) |
| **NAM** | 12km | CONUS | 4x/day (00/06/12/18z) | F00-F36 hourly, F39-F84 3-hourly |
| **RAP** | 13km | CONUS | Hourly (24/day) | F00-F21 (F00-F51 extended) |
| **NAM-Nest** | 3km | CONUS | 4x/day (00/06/12/18z) | F00-F60 hourly |

- **Vertical:** 40 pressure levels, 1000 hPa to 50 hPa
- Typically 12+ recent cycles available per model

## Rate Limits

- 240 requests per minute per IP
- Burst: 40 requests per second
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
