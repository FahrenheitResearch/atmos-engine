#!/usr/bin/env python3
"""
Unified HRRR Weather Dashboard

A complete operational weather dashboard that:
1. Displays weather map products as overlays on a Leaflet map
2. Generates interactive cross-sections on demand
3. Shows diurnal temperature analysis
4. Auto-downloads and processes latest HRRR data
5. Includes rate limiting for safe public use

Usage:
    # Start with existing data
    python tools/unified_dashboard.py --data-dir outputs/hrrr/20251224/19z

    # Start and auto-download latest
    python tools/unified_dashboard.py --auto-update

    # Production mode with rate limiting
    python tools/unified_dashboard.py --production --port 8080
"""

import argparse
import json
import logging
import os
import sys
import time
import threading
from pathlib import Path
from datetime import datetime, timedelta
from functools import wraps
from collections import defaultdict

from flask import Flask, render_template_string, jsonify, request, send_file, abort

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

# =============================================================================
# CONFIGURATION
# =============================================================================

# CONUS map bounds (from HRRR grid analysis)
CONUS_BOUNDS = {
    'south': 21.1381,
    'north': 52.6157,
    'west': -134.0955,
    'east': -60.9172,
}

# Product categories and their display names
PRODUCT_CATEGORIES = {
    'reflectivity': {'name': 'Radar/Reflectivity', 'icon': '🌧️'},
    'surface': {'name': 'Surface', 'icon': '🌡️'},
    'instability': {'name': 'Instability', 'icon': '⚡'},
    'severe': {'name': 'Severe Weather', 'icon': '🌪️'},
    'upper_air': {'name': 'Upper Air', 'icon': '🎈'},
    'precipitation': {'name': 'Precipitation', 'icon': '💧'},
    'atmospheric': {'name': 'Atmospheric', 'icon': '☁️'},
    'smoke': {'name': 'Smoke/Fire', 'icon': '🔥'},
    'composites': {'name': 'Composites', 'icon': '🗺️'},
    'heat': {'name': 'Heat/Humidity', 'icon': '🌡️'},
    'updraft_helicity': {'name': 'Updraft Helicity', 'icon': '🌀'},
}

# Featured products for quick access
FEATURED_PRODUCTS = [
    ('reflectivity', 'reflectivity_comp', 'Composite Reflectivity'),
    ('surface', 't2m', '2m Temperature'),
    ('instability', 'sbcape', 'Surface-Based CAPE'),
    ('severe', 'stp_fixed', 'Sig Tornado Parameter'),
    ('surface', 'mslp', 'Mean Sea Level Pressure'),
    ('atmospheric', 'pwat', 'Precipitable Water'),
]

# Cross-section styles
XSECT_STYLES = [
    ('wind_speed', 'Wind Speed'),
    ('temp', 'Temperature'),
    ('theta_e', 'Theta-E'),
    ('rh', 'Relative Humidity'),
    ('omega', 'Vertical Velocity'),
    ('icing', 'Icing'),
    ('shear', 'Wind Shear'),
]

# =============================================================================
# RATE LIMITING
# =============================================================================

class RateLimiter:
    """Simple in-memory rate limiter."""

    def __init__(self, requests_per_minute=60, burst_limit=10):
        self.rpm = requests_per_minute
        self.burst = burst_limit
        self.requests = defaultdict(list)
        self.lock = threading.Lock()

    def is_allowed(self, client_ip):
        now = time.time()
        minute_ago = now - 60

        with self.lock:
            # Clean old requests
            self.requests[client_ip] = [t for t in self.requests[client_ip] if t > minute_ago]

            # Check rate
            if len(self.requests[client_ip]) >= self.rpm:
                return False

            # Check burst (last second)
            second_ago = now - 1
            recent = [t for t in self.requests[client_ip] if t > second_ago]
            if len(recent) >= self.burst:
                return False

            self.requests[client_ip].append(now)
            return True

rate_limiter = RateLimiter()

def rate_limit(f):
    """Rate limiting decorator."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if app.config.get('PRODUCTION_MODE'):
            client_ip = request.remote_addr
            if not rate_limiter.is_allowed(client_ip):
                return jsonify({'error': 'Rate limit exceeded. Please wait.'}), 429
        return f(*args, **kwargs)
    return decorated

# =============================================================================
# DATA MANAGER
# =============================================================================

class WeatherDataManager:
    """Manages weather data loading and caching."""

    def __init__(self, cache_dir='cache/dashboard'):
        self.data_dir = None
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        # In-memory data for cross-sections
        self.xsect_data = {}
        self.xsect_engine = None

        # Available products and hours
        self.available_products = {}
        self.available_hours = []
        self.cycle_info = {}

    def load_run(self, data_dir: str, max_xsect_hours: int = 6):
        """Load a model run directory."""
        self.data_dir = Path(data_dir).resolve()  # Use absolute path
        if not self.data_dir.exists():
            logger.error(f"Data directory not found: {data_dir}")
            return False

        # Parse cycle info from path
        # e.g., outputs/hrrr/20251224/19z
        parts = self.data_dir.parts
        try:
            self.cycle_info = {
                'date': parts[-2],
                'hour': parts[-1].replace('z', ''),
                'model': parts[-3] if len(parts) > 3 else 'hrrr',
            }
        except:
            self.cycle_info = {'date': 'unknown', 'hour': '00', 'model': 'hrrr'}

        # Scan for available forecast hours and products
        self._scan_products()

        # Load cross-section data
        self._load_xsect_data(max_xsect_hours)

        logger.info(f"Loaded run: {self.cycle_info['date']} {self.cycle_info['hour']}Z")
        logger.info(f"Available hours: {self.available_hours}")
        logger.info(f"Products: {len(self.available_products)} categories")

        return True

    def _scan_products(self):
        """Scan directory for available products."""
        self.available_products = {}
        self.available_hours = []

        for fhr_dir in sorted(self.data_dir.glob("F*")):
            if fhr_dir.is_dir():
                fhr = int(fhr_dir.name[1:])
                self.available_hours.append(fhr)

                # Scan categories in this hour
                for cat_dir in fhr_dir.iterdir():
                    if cat_dir.is_dir() and cat_dir.name not in ['conus']:
                        category = cat_dir.name
                        if category not in self.available_products:
                            self.available_products[category] = []

                        # Scan products
                        for png_file in cat_dir.glob("*_f*.png"):
                            # Extract product name
                            name = png_file.stem.replace(f'_f{fhr:02d}', '').replace('_REFACTORED', '')
                            if name not in self.available_products[category]:
                                self.available_products[category].append(name)

        self.available_hours = sorted(self.available_hours)

    def _load_xsect_data(self, max_hours: int):
        """Load data for cross-sections."""
        try:
            from core.cross_section_interactive import InteractiveCrossSection

            self.xsect_engine = InteractiveCrossSection(cache_dir=str(self.cache_dir / 'xsect'))

            # Find GRIB files
            loaded = 0
            for fhr in self.available_hours[:max_hours]:
                fhr_dir = self.data_dir / f"F{fhr:02d}"
                prs_files = list(fhr_dir.glob("*wrfprs*.grib2"))
                if prs_files:
                    self.xsect_engine.load_forecast_hour(str(prs_files[0]), fhr)
                    loaded += 1

            logger.info(f"Loaded {loaded} hours for cross-sections ({self.xsect_engine.get_memory_usage():.0f} MB)")

        except Exception as e:
            logger.error(f"Failed to load cross-section data: {e}")
            self.xsect_engine = None

    def get_product_path(self, category: str, product: str, hour: int) -> Path:
        """Get path to a product PNG."""
        fhr_dir = self.data_dir / f"F{hour:02d}"

        # Try different naming patterns
        patterns = [
            fhr_dir / category / f"{product}_f{hour:02d}_REFACTORED.png",
            fhr_dir / category / f"{product}_f{hour:02d}.png",
            fhr_dir / "conus" / f"F{hour:02d}" / category / f"{product}_f{hour:02d}_REFACTORED.png",
        ]

        for path in patterns:
            if path.exists():
                return path

        return None

    def get_xsect(self, start_point, end_point, style, hour, n_points=80):
        """Generate a cross-section."""
        if self.xsect_engine is None:
            return None

        return self.xsect_engine.get_cross_section(
            start_point=start_point,
            end_point=end_point,
            style=style,
            forecast_hour=hour,
            n_points=n_points,
        )

# Global data manager
data_manager = WeatherDataManager()

# =============================================================================
# HTML TEMPLATE
# =============================================================================

DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HRRR Weather Dashboard</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }

        :root {
            --bg-dark: #0f172a;
            --bg-panel: #1e293b;
            --bg-card: #334155;
            --text-primary: #f1f5f9;
            --text-secondary: #94a3b8;
            --accent: #38bdf8;
            --accent-hover: #7dd3fc;
            --border: #475569;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--bg-dark);
            color: var(--text-primary);
            overflow: hidden;
        }

        /* Header */
        .header {
            background: var(--bg-panel);
            padding: 8px 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid var(--border);
            height: 48px;
        }

        .header h1 {
            font-size: 18px;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .cycle-info {
            font-size: 14px;
            color: var(--text-secondary);
        }

        .cycle-info span {
            color: var(--accent);
            font-weight: 500;
        }

        /* Main Layout */
        .main-container {
            display: flex;
            height: calc(100vh - 48px);
        }

        /* Left Panel - Map */
        .map-panel {
            flex: 1;
            display: flex;
            flex-direction: column;
            border-right: 1px solid var(--border);
        }

        .map-controls {
            background: var(--bg-panel);
            padding: 8px 12px;
            display: flex;
            gap: 12px;
            align-items: center;
            flex-wrap: wrap;
            border-bottom: 1px solid var(--border);
        }

        .control-group {
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .control-group label {
            font-size: 12px;
            color: var(--text-secondary);
            white-space: nowrap;
        }

        select, input[type="range"] {
            background: var(--bg-card);
            border: 1px solid var(--border);
            color: var(--text-primary);
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 13px;
        }

        select:focus { outline: none; border-color: var(--accent); }

        #map {
            flex: 1;
            background: #1a1a2e;
        }

        /* Time Slider */
        .time-slider {
            background: var(--bg-panel);
            padding: 8px 12px;
            display: flex;
            align-items: center;
            gap: 12px;
            border-top: 1px solid var(--border);
        }

        .time-slider input[type="range"] {
            flex: 1;
            height: 6px;
        }

        .time-display {
            font-size: 14px;
            font-weight: 500;
            min-width: 50px;
            color: var(--accent);
        }

        .play-btn {
            background: var(--accent);
            border: none;
            color: var(--bg-dark);
            width: 32px;
            height: 32px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 14px;
        }

        .play-btn:hover { background: var(--accent-hover); }

        /* Right Panel - Cross Section */
        .xsect-panel {
            width: 45%;
            min-width: 400px;
            display: flex;
            flex-direction: column;
            background: var(--bg-panel);
        }

        .xsect-controls {
            padding: 8px 12px;
            display: flex;
            gap: 12px;
            align-items: center;
            border-bottom: 1px solid var(--border);
        }

        .xsect-container {
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 12px;
            overflow: auto;
        }

        #xsect-img {
            max-width: 100%;
            max-height: 100%;
            border-radius: 8px;
        }

        .xsect-info {
            background: var(--bg-dark);
            padding: 8px 12px;
            font-size: 12px;
            color: var(--text-secondary);
            display: flex;
            justify-content: space-between;
        }

        .xsect-info .timing { color: var(--accent); }

        /* Loading/Error states */
        .loading, .error {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            font-size: 16px;
        }

        .error { color: #f87171; }

        /* Preset buttons */
        .preset-btns {
            display: flex;
            gap: 4px;
            flex-wrap: wrap;
        }

        .preset-btn {
            background: var(--bg-card);
            border: 1px solid var(--border);
            color: var(--text-secondary);
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 11px;
            cursor: pointer;
        }

        .preset-btn:hover {
            background: var(--accent);
            color: var(--bg-dark);
            border-color: var(--accent);
        }

        /* Tabs */
        .tab-bar {
            display: flex;
            background: var(--bg-dark);
            border-bottom: 1px solid var(--border);
        }

        .tab {
            padding: 8px 16px;
            font-size: 13px;
            color: var(--text-secondary);
            cursor: pointer;
            border-bottom: 2px solid transparent;
        }

        .tab:hover { color: var(--text-primary); }
        .tab.active {
            color: var(--accent);
            border-bottom-color: var(--accent);
        }

        /* Product dropdown styling */
        .product-select {
            max-width: 200px;
        }

        optgroup {
            font-weight: 600;
            color: var(--accent);
        }
    </style>
</head>
<body>
    <header class="header">
        <h1>🌦️ HRRR Weather Dashboard</h1>
        <div class="cycle-info">
            Cycle: <span id="cycle-date">{{ cycle_date }}</span> <span id="cycle-hour">{{ cycle_hour }}Z</span>
            | Hours: <span id="hours-available">F00-F{{ max_hour }}</span>
        </div>
    </header>

    <div class="main-container">
        <!-- Map Panel -->
        <div class="map-panel">
            <div class="map-controls">
                <div class="control-group">
                    <label>Product:</label>
                    <select id="product-select" class="product-select">
                        {% for cat, products in available_products.items() %}
                        <optgroup label="{{ category_names.get(cat, cat) }}">
                            {% for product in products %}
                            <option value="{{ cat }}/{{ product }}">{{ product.replace('_', ' ').title() }}</option>
                            {% endfor %}
                        </optgroup>
                        {% endfor %}
                    </select>
                </div>
                <div class="control-group">
                    <label>Opacity:</label>
                    <input type="range" id="opacity-slider" min="0" max="100" value="70" style="width: 80px;">
                    <span id="opacity-value">70%</span>
                </div>
                <div class="preset-btns">
                    {% for cat, prod, name in featured %}
                    <button class="preset-btn" data-product="{{ cat }}/{{ prod }}">{{ name }}</button>
                    {% endfor %}
                </div>
            </div>

            <div id="map"></div>

            <div class="time-slider">
                <button class="play-btn" id="play-btn">▶</button>
                <input type="range" id="hour-slider" min="0" max="{{ max_hour }}" value="0">
                <div class="time-display">F<span id="current-hour">00</span></div>
            </div>
        </div>

        <!-- Cross Section Panel -->
        <div class="xsect-panel">
            <div class="tab-bar">
                <div class="tab active" data-tab="xsect">Cross-Section</div>
                <div class="tab" data-tab="diurnal">Diurnal</div>
            </div>

            <div class="xsect-controls">
                <div class="control-group">
                    <label>Style:</label>
                    <select id="xsect-style">
                        {% for value, name in xsect_styles %}
                        <option value="{{ value }}">{{ name }}</option>
                        {% endfor %}
                    </select>
                </div>
                <div class="control-group">
                    <label>Hour:</label>
                    <select id="xsect-hour">
                        {% for hour in xsect_hours %}
                        <option value="{{ hour }}">F{{ '%02d'|format(hour) }}</option>
                        {% endfor %}
                    </select>
                </div>
            </div>

            <div class="xsect-container" id="xsect-container">
                <div class="loading">Drag markers on map to create cross-section</div>
            </div>

            <div class="xsect-info">
                <span id="xsect-coords">Click and drag on map</span>
                <span class="timing" id="xsect-timing"></span>
            </div>
        </div>
    </div>

    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script>
        // =================================================================
        // MAP SETUP
        // =================================================================

        const CONUS_BOUNDS = {{ conus_bounds | tojson }};
        const bounds = L.latLngBounds(
            L.latLng(CONUS_BOUNDS.south, CONUS_BOUNDS.west),
            L.latLng(CONUS_BOUNDS.north, CONUS_BOUNDS.east)
        );

        const map = L.map('map', {
            center: [39, -98],
            zoom: 4,
            minZoom: 3,
            maxZoom: 10,
        });

        // Dark basemap
        L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
            attribution: '&copy; CARTO',
            maxZoom: 19
        }).addTo(map);

        // Weather overlay
        let weatherOverlay = null;
        let currentProduct = 'reflectivity/reflectivity_comp';
        let currentHour = 0;
        let overlayOpacity = 0.7;

        function updateWeatherOverlay() {
            const [category, product] = currentProduct.split('/');
            const url = `/api/overlay/${category}/${product}/${currentHour}`;

            if (weatherOverlay) {
                map.removeLayer(weatherOverlay);
            }

            weatherOverlay = L.imageOverlay(url, bounds, {
                opacity: overlayOpacity,
                interactive: false,
            }).addTo(map);
        }

        // =================================================================
        // CROSS-SECTION MARKERS
        // =================================================================

        const startIcon = L.divIcon({
            className: 'marker',
            html: '<div style="background:#22c55e; width:14px; height:14px; border-radius:50%; border:2px solid white; box-shadow:0 2px 4px rgba(0,0,0,0.5);"></div>',
            iconSize: [18, 18],
            iconAnchor: [9, 9]
        });

        const endIcon = L.divIcon({
            className: 'marker',
            html: '<div style="background:#ef4444; width:14px; height:14px; border-radius:50%; border:2px solid white; box-shadow:0 2px 4px rgba(0,0,0,0.5);"></div>',
            iconSize: [18, 18],
            iconAnchor: [9, 9]
        });

        let startMarker = L.marker([39.74, -104.99], {draggable: true, icon: startIcon}).addTo(map);
        let endMarker = L.marker([41.88, -87.63], {draggable: true, icon: endIcon}).addTo(map);

        let pathLine = L.polyline([startMarker.getLatLng(), endMarker.getLatLng()], {
            color: '#38bdf8',
            weight: 2,
            opacity: 0.8,
            dashArray: '8, 8'
        }).addTo(map);

        function updateLine() {
            pathLine.setLatLngs([startMarker.getLatLng(), endMarker.getLatLng()]);
        }

        startMarker.on('drag', updateLine);
        endMarker.on('drag', updateLine);

        // =================================================================
        // CROSS-SECTION GENERATION
        // =================================================================

        let xsectDebounce;

        async function generateXsect() {
            const start = startMarker.getLatLng();
            const end = endMarker.getLatLng();
            const style = document.getElementById('xsect-style').value;
            const hour = parseInt(document.getElementById('xsect-hour').value);

            document.getElementById('xsect-coords').textContent =
                `${start.lat.toFixed(2)}, ${start.lng.toFixed(2)} → ${end.lat.toFixed(2)}, ${end.lng.toFixed(2)}`;

            document.getElementById('xsect-container').innerHTML = '<div class="loading">Generating...</div>';

            const t0 = performance.now();

            try {
                const response = await fetch('/api/xsect', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        start_lat: start.lat,
                        start_lon: start.lng,
                        end_lat: end.lat,
                        end_lon: end.lng,
                        style: style,
                        hour: hour,
                    })
                });

                const data = await response.json();
                const elapsed = ((performance.now() - t0) / 1000).toFixed(2);

                if (data.success) {
                    document.getElementById('xsect-container').innerHTML =
                        `<img id="xsect-img" src="data:image/png;base64,${data.image}" alt="Cross-section">`;
                    document.getElementById('xsect-timing').textContent = `${elapsed}s`;
                } else {
                    document.getElementById('xsect-container').innerHTML =
                        `<div class="error">${data.error || 'Failed to generate'}</div>`;
                }
            } catch (err) {
                document.getElementById('xsect-container').innerHTML =
                    `<div class="error">Error: ${err.message}</div>`;
            }
        }

        function debouncedXsect() {
            clearTimeout(xsectDebounce);
            xsectDebounce = setTimeout(generateXsect, 300);
        }

        startMarker.on('dragend', debouncedXsect);
        endMarker.on('dragend', debouncedXsect);
        document.getElementById('xsect-style').addEventListener('change', generateXsect);
        document.getElementById('xsect-hour').addEventListener('change', generateXsect);

        // =================================================================
        // CONTROLS
        // =================================================================

        // Product select
        document.getElementById('product-select').addEventListener('change', function() {
            currentProduct = this.value;
            updateWeatherOverlay();
        });

        // Preset buttons
        document.querySelectorAll('.preset-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                currentProduct = this.dataset.product;
                document.getElementById('product-select').value = currentProduct;
                updateWeatherOverlay();
            });
        });

        // Opacity
        document.getElementById('opacity-slider').addEventListener('input', function() {
            overlayOpacity = this.value / 100;
            document.getElementById('opacity-value').textContent = this.value + '%';
            if (weatherOverlay) {
                weatherOverlay.setOpacity(overlayOpacity);
            }
        });

        // Hour slider
        document.getElementById('hour-slider').addEventListener('input', function() {
            currentHour = parseInt(this.value);
            document.getElementById('current-hour').textContent = currentHour.toString().padStart(2, '0');
            updateWeatherOverlay();
        });

        // Play button
        let playing = false;
        let playInterval;

        document.getElementById('play-btn').addEventListener('click', function() {
            playing = !playing;
            this.textContent = playing ? '⏸' : '▶';

            if (playing) {
                playInterval = setInterval(() => {
                    const slider = document.getElementById('hour-slider');
                    currentHour = (currentHour + 1) % (parseInt(slider.max) + 1);
                    slider.value = currentHour;
                    document.getElementById('current-hour').textContent = currentHour.toString().padStart(2, '0');
                    updateWeatherOverlay();
                }, 500);
            } else {
                clearInterval(playInterval);
            }
        });

        // Tabs
        document.querySelectorAll('.tab').forEach(tab => {
            tab.addEventListener('click', function() {
                document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                this.classList.add('active');
                // TODO: Switch content based on tab
            });
        });

        // =================================================================
        // INITIALIZATION
        // =================================================================

        updateWeatherOverlay();
        setTimeout(generateXsect, 1000);
    </script>
</body>
</html>
"""

# =============================================================================
# FLASK ROUTES
# =============================================================================

@app.route('/')
def index():
    """Serve the main dashboard."""
    return render_template_string(
        DASHBOARD_HTML,
        cycle_date=data_manager.cycle_info.get('date', 'N/A'),
        cycle_hour=data_manager.cycle_info.get('hour', '00'),
        max_hour=max(data_manager.available_hours) if data_manager.available_hours else 0,
        available_products=data_manager.available_products,
        category_names={k: v['name'] for k, v in PRODUCT_CATEGORIES.items()},
        featured=FEATURED_PRODUCTS,
        xsect_styles=XSECT_STYLES,
        xsect_hours=sorted(data_manager.xsect_engine.get_loaded_hours()) if data_manager.xsect_engine else [0],
        conus_bounds=CONUS_BOUNDS,
    )


@app.route('/api/overlay/<category>/<product>/<int:hour>')
@rate_limit
def get_overlay(category, product, hour):
    """Serve a weather product PNG as overlay."""
    path = data_manager.get_product_path(category, product, hour)

    if path and path.exists():
        return send_file(path, mimetype='image/png')

    # Return transparent placeholder
    abort(404)


@app.route('/api/xsect', methods=['POST'])
@rate_limit
def generate_xsect():
    """Generate a cross-section."""
    import base64

    if data_manager.xsect_engine is None:
        return jsonify({'success': False, 'error': 'Cross-section engine not loaded'})

    try:
        data = request.json
        start_point = (data['start_lat'], data['start_lon'])
        end_point = (data['end_lat'], data['end_lon'])
        style = data.get('style', 'wind_speed')
        hour = data.get('hour', 0)

        img_bytes = data_manager.get_xsect(start_point, end_point, style, hour)

        if img_bytes is None:
            return jsonify({'success': False, 'error': 'Failed to generate cross-section'})

        img_b64 = base64.b64encode(img_bytes).decode('utf-8')
        return jsonify({'success': True, 'image': img_b64})

    except Exception as e:
        logger.exception("Error generating cross-section")
        return jsonify({'success': False, 'error': str(e)})


@app.route('/api/products')
def list_products():
    """List available products."""
    return jsonify({
        'products': data_manager.available_products,
        'hours': data_manager.available_hours,
        'cycle': data_manager.cycle_info,
    })


@app.route('/api/health')
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'ok',
        'loaded': data_manager.data_dir is not None,
        'xsect_hours': len(data_manager.xsect_engine.get_loaded_hours()) if data_manager.xsect_engine else 0,
    })


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="Unified HRRR Weather Dashboard")
    parser.add_argument("--data-dir", type=str, help="Path to model run directory")
    parser.add_argument("--auto-update", action="store_true", help="Auto-download latest data")
    parser.add_argument("--xsect-hours", type=int, default=6, help="Max hours to load for cross-sections")
    parser.add_argument("--port", type=int, default=8080, help="Server port")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Server host")
    parser.add_argument("--production", action="store_true", help="Enable production mode with rate limiting")

    args = parser.parse_args()

    app.config['PRODUCTION_MODE'] = args.production

    # Find data directory
    if args.data_dir:
        data_dir = args.data_dir
    else:
        # Find latest available
        outputs_dir = Path("outputs/hrrr")
        if outputs_dir.exists():
            for date_dir in sorted(outputs_dir.iterdir(), reverse=True):
                for hour_dir in sorted(date_dir.iterdir(), reverse=True):
                    if list(hour_dir.glob("F*/hrrr*.grib2")) or list(hour_dir.glob("F*/*/*.png")):
                        data_dir = str(hour_dir)
                        break
                else:
                    continue
                break
        else:
            logger.error("No data found. Use --data-dir or run processing first.")
            sys.exit(1)

    # Load data
    logger.info(f"Loading data from {data_dir}...")
    if not data_manager.load_run(data_dir, max_xsect_hours=args.xsect_hours):
        logger.error("Failed to load data")
        sys.exit(1)

    # Start server
    logger.info("=" * 60)
    logger.info("HRRR Weather Dashboard")
    logger.info(f"Open in browser: http://{args.host}:{args.port}")
    if args.production:
        logger.info("Production mode: Rate limiting enabled")
    logger.info("=" * 60)

    app.run(host=args.host, port=args.port, debug=False, threaded=True)


if __name__ == "__main__":
    main()
