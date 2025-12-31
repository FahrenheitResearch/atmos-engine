#!/usr/bin/env python3
"""
HRRR Cross-Section Dashboard

Interactive cross-section visualization on a Leaflet map.
Draw a line on the map to generate vertical cross-sections.

Usage:
    python tools/unified_dashboard.py --data-dir outputs/hrrr/20251227/09z
    python tools/unified_dashboard.py --auto-update
"""

import argparse
import json
import logging
import sys
import time
import io
import threading
from pathlib import Path
from datetime import datetime
from functools import wraps
from collections import defaultdict

from flask import Flask, jsonify, request, send_file, abort

sys.path.insert(0, str(Path(__file__).parent.parent))

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

# =============================================================================
# CONFIGURATION
# =============================================================================

CONUS_BOUNDS = {
    'south': 21.14, 'north': 52.62,
    'west': -134.10, 'east': -60.92,
}

XSECT_STYLES = [
    ('wind_speed', 'Wind Speed'),
    ('temp', 'Temperature'),
    ('theta_e', 'Theta-E'),
    ('rh', 'Relative Humidity'),
    ('q', 'Specific Humidity'),
    ('omega', 'Vertical Velocity'),
    ('vorticity', 'Vorticity'),
    ('shear', 'Wind Shear'),
    ('lapse_rate', 'Lapse Rate'),
    ('cloud', 'Cloud Water'),
    ('cloud_total', 'Total Condensate'),
    ('wetbulb', 'Wet-Bulb Temp'),
    ('icing', 'Icing Potential'),
    ('frontogenesis', '❄ Frontogenesis'),  # Winter Bander mode
]

# =============================================================================
# RATE LIMITING
# =============================================================================

class RateLimiter:
    def __init__(self, rpm=60, burst=10):
        self.rpm, self.burst = rpm, burst
        self.requests = defaultdict(list)
        self.lock = threading.Lock()

    def is_allowed(self, ip):
        now = time.time()
        with self.lock:
            self.requests[ip] = [t for t in self.requests[ip] if t > now - 60]
            if len(self.requests[ip]) >= self.rpm:
                return False
            if len([t for t in self.requests[ip] if t > now - 1]) >= self.burst:
                return False
            self.requests[ip].append(now)
            return True

rate_limiter = RateLimiter()

def rate_limit(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if app.config.get('PRODUCTION'):
            if not rate_limiter.is_allowed(request.remote_addr):
                return jsonify({'error': 'Rate limit exceeded'}), 429
        return f(*args, **kwargs)
    return decorated

# =============================================================================
# DATA MANAGER - On-Demand Loading for Memory Efficiency
# =============================================================================

class CrossSectionManager:
    """Manages cross-section data with smart pre-loading.

    Pre-loads latest N cycles at startup for instant access.
    Older cycles are available on-demand with loading indicator.
    """

    FORECAST_HOURS = [0, 6, 12, 18]
    PRELOAD_CYCLES = 2  # Number of cycles to pre-load at startup

    def __init__(self):
        self.xsect = None
        self.base_dir = Path("outputs/hrrr")
        self.available_cycles = []  # List of available cycles (metadata only)
        self.loaded_cycles = set()  # Cycle keys that are fully loaded
        self.loaded_items = []  # List of (cycle_key, fhr) currently in memory
        self.current_cycle = None  # Currently selected cycle
        self._loading = False  # Lock to prevent concurrent loads

    def init_engine(self):
        """Initialize the cross-section engine if needed."""
        if self.xsect is None:
            from core.cross_section_interactive import InteractiveCrossSection
            self.xsect = InteractiveCrossSection(cache_dir='cache/dashboard/xsect')

    def scan_available_cycles(self, n_cycles: int = 5):
        """Scan for available cycles WITHOUT loading data."""
        from datetime import datetime

        self.available_cycles = []

        if not self.base_dir.exists():
            return self.available_cycles

        # Scan for date directories
        for date_dir in sorted(self.base_dir.iterdir(), reverse=True):
            if not date_dir.is_dir() or not date_dir.name.isdigit():
                continue
            if len(date_dir.name) != 8:
                continue

            # Scan for hour directories within date
            for hour_dir in sorted(date_dir.iterdir(), reverse=True):
                if not hour_dir.is_dir() or not hour_dir.name.endswith('z'):
                    continue

                hour = hour_dir.name.replace('z', '')
                if not hour.isdigit():
                    continue

                # Check what forecast hours are available on disk
                available_fhrs = []
                for fhr in self.FORECAST_HOURS:
                    fhr_dir = hour_dir / f"F{fhr:02d}"
                    if fhr_dir.exists() and list(fhr_dir.glob("*wrfprs*.grib2")):
                        available_fhrs.append(fhr)

                if available_fhrs:
                    cycle_key = f"{date_dir.name}_{hour}z"
                    init_dt = datetime.strptime(f"{date_dir.name}{hour}", "%Y%m%d%H")

                    self.available_cycles.append({
                        'cycle_key': cycle_key,
                        'date': date_dir.name,
                        'hour': hour,
                        'path': str(hour_dir),
                        'available_fhrs': available_fhrs,
                        'init_dt': init_dt,
                        'display': f"HRRR - {init_dt.strftime('%b %d %HZ')}",
                    })

                if len(self.available_cycles) >= n_cycles:
                    return self.available_cycles

        return self.available_cycles

    def get_cycles_for_ui(self):
        """Return cycles formatted for UI dropdown."""
        return [
            {
                'key': c['cycle_key'],
                'display': c['display'],
                'fhrs': c['available_fhrs'],
                'loaded': c['cycle_key'] in self.loaded_cycles,
            }
            for c in self.available_cycles
        ]

    def preload_latest_cycles(self, n_cycles: int = None):
        """Pre-load the latest N cycles that have all 4 forecast hours."""
        if n_cycles is None:
            n_cycles = self.PRELOAD_CYCLES

        self.init_engine()

        # Prefer cycles with all 4 FHRs (F00, F06, F12, F18)
        complete_cycles = [c for c in self.available_cycles
                          if all(fhr in c['available_fhrs'] for fhr in self.FORECAST_HOURS)]

        if len(complete_cycles) >= n_cycles:
            cycles_to_load = complete_cycles[:n_cycles]
            logger.info(f"Found {len(complete_cycles)} complete cycles (all 4 FHRs)")
        else:
            # Fall back to newest cycles if not enough complete ones
            cycles_to_load = self.available_cycles[:n_cycles]
            logger.info(f"Only {len(complete_cycles)} complete cycles, using newest {n_cycles}")

        for cycle in cycles_to_load:
            cycle_key = cycle['cycle_key']
            logger.info(f"Pre-loading {cycle['display']}...")

            for fhr in cycle['available_fhrs']:
                if (cycle_key, fhr) in self.loaded_items:
                    continue

                run_path = Path(cycle['path'])
                fhr_dir = run_path / f"F{fhr:02d}"
                prs_files = list(fhr_dir.glob("*wrfprs*.grib2"))

                if prs_files:
                    self.xsect.init_date = cycle['date']
                    self.xsect.init_hour = cycle['hour']

                    if self.xsect.load_forecast_hour(str(prs_files[0]), fhr):
                        self.loaded_items.append((cycle_key, fhr))

            # Mark this cycle as fully loaded
            self.loaded_cycles.add(cycle_key)
            mem_mb = self.xsect.get_memory_usage()
            logger.info(f"  {cycle['display']} loaded ({mem_mb:.0f} MB total)")

    def get_loaded_status(self):
        """Return current memory status."""
        mem_mb = self.xsect.get_memory_usage() if self.xsect else 0
        return {
            'loaded': self.loaded_items.copy(),
            'loaded_cycles': list(self.loaded_cycles),
            'memory_mb': round(mem_mb, 0),
            'loading': self._loading,
        }

    def load_cycle(self, cycle_key: str) -> dict:
        """Load an entire cycle (all available FHRs) into memory."""
        if self._loading:
            return {'success': False, 'error': 'Another load in progress'}

        if cycle_key in self.loaded_cycles:
            return {'success': True, 'already_loaded': True}

        cycle = next((c for c in self.available_cycles if c['cycle_key'] == cycle_key), None)
        if not cycle:
            return {'success': False, 'error': f'Cycle {cycle_key} not found'}

        self._loading = True
        try:
            self.init_engine()
            loaded_count = 0

            for fhr in cycle['available_fhrs']:
                if (cycle_key, fhr) in self.loaded_items:
                    loaded_count += 1
                    continue

                run_path = Path(cycle['path'])
                fhr_dir = run_path / f"F{fhr:02d}"
                prs_files = list(fhr_dir.glob("*wrfprs*.grib2"))

                if prs_files:
                    self.xsect.init_date = cycle['date']
                    self.xsect.init_hour = cycle['hour']

                    logger.info(f"Loading {cycle_key} F{fhr:02d}...")
                    if self.xsect.load_forecast_hour(str(prs_files[0]), fhr):
                        self.loaded_items.append((cycle_key, fhr))
                        loaded_count += 1

            self.loaded_cycles.add(cycle_key)
            mem_mb = self.xsect.get_memory_usage()
            logger.info(f"Loaded {cycle['display']} ({loaded_count} FHRs, {mem_mb:.0f} MB total)")

            return {
                'success': True,
                'cycle': cycle_key,
                'loaded_fhrs': loaded_count,
                'memory_mb': round(mem_mb, 0),
            }

        finally:
            self._loading = False

    def load_forecast_hour(self, cycle_key: str, fhr: int) -> dict:
        """Load a specific forecast hour into memory."""
        from datetime import datetime, timedelta

        if self._loading:
            return {'success': False, 'error': 'Another load in progress'}

        # Check if already loaded
        if (cycle_key, fhr) in self.loaded_items:
            return {'success': True, 'already_loaded': True}

        # Find cycle info
        cycle = next((c for c in self.available_cycles if c['cycle_key'] == cycle_key), None)
        if not cycle:
            return {'success': False, 'error': f'Cycle {cycle_key} not found'}

        if fhr not in cycle['available_fhrs']:
            return {'success': False, 'error': f'F{fhr:02d} not available for {cycle_key}'}

        self._loading = True
        try:
            self.init_engine()

            # Set metadata
            self.xsect.init_date = cycle['date']
            self.xsect.init_hour = cycle['hour']

            # Find and load the GRIB file
            run_path = Path(cycle['path'])
            fhr_dir = run_path / f"F{fhr:02d}"
            prs_files = list(fhr_dir.glob("*wrfprs*.grib2"))

            if not prs_files:
                return {'success': False, 'error': f'No GRIB file found for F{fhr:02d}'}

            logger.info(f"Loading {cycle_key} F{fhr:02d}...")
            if self.xsect.load_forecast_hour(str(prs_files[0]), fhr):
                self.loaded_items.append((cycle_key, fhr))
                self.current_cycle = cycle_key
                mem_mb = self.xsect.get_memory_usage()
                logger.info(f"Loaded {cycle_key} F{fhr:02d} (Total: {mem_mb:.0f} MB)")
                return {
                    'success': True,
                    'loaded': (cycle_key, fhr),
                    'memory_mb': round(mem_mb, 0),
                }
            else:
                return {'success': False, 'error': 'Failed to load data'}

        finally:
            self._loading = False

    def _unload_item(self, cycle_key: str, fhr: int):
        """Unload a forecast hour from memory."""
        if self.xsect and fhr in self.xsect.forecast_hours:
            self.xsect.unload_hour(fhr)
            logger.info(f"Unloaded F{fhr:02d}")

    def unload_forecast_hour(self, cycle_key: str, fhr: int) -> dict:
        """Explicitly unload a forecast hour."""
        if (cycle_key, fhr) not in self.loaded_items:
            return {'success': True, 'not_loaded': True}

        self._unload_item(cycle_key, fhr)
        self.loaded_items.remove((cycle_key, fhr))

        mem_mb = self.xsect.get_memory_usage() if self.xsect else 0
        return {
            'success': True,
            'unloaded': (cycle_key, fhr),
            'memory_mb': round(mem_mb, 0),
        }

    def generate_cross_section(self, start, end, cycle_key, fhr, style):
        """Generate a cross-section for a loaded forecast hour."""
        if not self.xsect:
            return None

        if (cycle_key, fhr) not in self.loaded_items:
            return None

        # Set correct metadata for this cycle
        cycle = next((c for c in self.available_cycles if c['cycle_key'] == cycle_key), None)
        if cycle:
            self.xsect.init_date = cycle['date']
            self.xsect.init_hour = cycle['hour']

        try:
            png_bytes = self.xsect.get_cross_section(
                start_point=start,
                end_point=end,
                forecast_hour=fhr,
                style=style,
                return_image=True,
                dpi=100
            )
            if png_bytes is None:
                return None
            return io.BytesIO(png_bytes)
        except Exception as e:
            logger.error(f"Cross-section error: {e}")
            return None

    # Legacy compatibility methods
    def get_available_times(self):
        """Legacy: Return loaded times for old API."""
        from datetime import timedelta
        times = []
        for cycle_key, fhr in self.loaded_items:
            cycle = next((c for c in self.available_cycles if c['cycle_key'] == cycle_key), None)
            if cycle:
                valid_dt = cycle['init_dt'] + timedelta(hours=fhr)
                times.append({
                    'valid': valid_dt.strftime("%Y-%m-%d %HZ"),
                    'init': cycle['init_dt'].strftime("%Y-%m-%d %HZ"),
                    'fhr': fhr,
                    'cycle_key': cycle_key,
                })
        return times


data_manager = CrossSectionManager()

# =============================================================================
# HTML TEMPLATE
# =============================================================================

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HRRR Cross-Section Dashboard</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        :root {
            --bg: #0f172a;
            --panel: #1e293b;
            --card: #334155;
            --text: #f1f5f9;
            --muted: #94a3b8;
            --accent: #38bdf8;
            --border: #475569;
            --success: #22c55e;
            --warning: #f59e0b;
        }
        body {
            font-family: system-ui, sans-serif;
            background: var(--bg);
            color: var(--text);
            height: 100vh;
            display: flex;
        }
        #map-container {
            flex: 1;
            display: flex;
            flex-direction: column;
        }
        #map { flex: 1; }
        #controls {
            background: var(--panel);
            padding: 12px 16px;
            display: flex;
            flex-direction: column;
            gap: 12px;
            border-bottom: 1px solid var(--border);
        }
        .control-row {
            display: flex;
            gap: 16px;
            align-items: center;
            flex-wrap: wrap;
        }
        .control-group { display: flex; align-items: center; gap: 8px; }
        label { color: var(--muted); font-size: 13px; font-weight: 500; }
        select {
            background: var(--card);
            color: var(--text);
            border: 1px solid var(--border);
            padding: 8px 12px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 14px;
            min-width: 180px;
        }
        select:focus { outline: 2px solid var(--accent); outline-offset: 1px; }

        /* Forecast Hour Chips */
        .chip-group {
            display: flex;
            gap: 6px;
            align-items: center;
        }
        .chip {
            background: var(--card);
            color: var(--muted);
            border: 1px solid var(--border);
            padding: 6px 14px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 13px;
            font-weight: 500;
            transition: all 0.15s ease;
            user-select: none;
        }
        .chip:hover { border-color: var(--accent); color: var(--text); }
        .chip.selected {
            background: var(--accent);
            color: #000;
            border-color: var(--accent);
        }
        .chip.loading {
            background: var(--warning);
            color: #000;
            border-color: var(--warning);
            animation: pulse 1s infinite;
        }
        .chip:disabled, .chip.unavailable {
            opacity: 0.4;
            cursor: not-allowed;
        }

        /* Memory indicator */
        #memory-status {
            margin-left: auto;
            display: flex;
            align-items: center;
            gap: 8px;
            color: var(--muted);
            font-size: 12px;
        }
        .mem-bar {
            width: 60px;
            height: 6px;
            background: var(--card);
            border-radius: 3px;
            overflow: hidden;
        }
        .mem-fill {
            height: 100%;
            background: var(--accent);
            transition: width 0.3s ease;
        }

        /* Toast notifications */
        #toast-container {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 10000;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .toast {
            background: var(--panel);
            border: 1px solid var(--border);
            padding: 12px 20px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            display: flex;
            align-items: center;
            gap: 10px;
            animation: slideUp 0.3s ease;
        }
        .toast.loading { border-left: 3px solid var(--warning); }
        .toast.success { border-left: 3px solid var(--success); }
        .toast.error { border-left: 3px solid #ef4444; }
        @keyframes slideUp {
            from { transform: translateY(20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        @keyframes pulse { 50% { opacity: 0.6; } }

        button {
            background: var(--card);
            color: var(--text);
            border: 1px solid var(--border);
            padding: 6px 12px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 13px;
        }
        button:hover { background: var(--accent); color: #000; }

        #sidebar {
            width: 55%;
            min-width: 500px;
            background: var(--panel);
            border-left: 1px solid var(--border);
            display: flex;
            flex-direction: column;
        }
        #xsect-header {
            padding: 12px 16px;
            border-bottom: 1px solid var(--border);
            font-weight: 600;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        #active-fhr { color: var(--accent); font-size: 13px; }
        #xsect-container {
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 12px;
            overflow: hidden;
        }
        #xsect-img {
            max-width: 100%;
            max-height: 100%;
            border-radius: 4px;
        }
        #instructions {
            color: var(--muted);
            text-align: center;
            padding: 20px;
        }
        .loading-text {
            color: var(--accent);
            animation: pulse 1.5s infinite;
        }
    </style>
</head>
<body>
    <div id="map-container">
        <div id="controls">
            <div class="control-row">
                <div class="control-group">
                    <label>Model Run:</label>
                    <select id="cycle-select"></select>
                </div>
                <div class="control-group">
                    <label>Style:</label>
                    <select id="style-select"></select>
                </div>
                <button id="clear-btn">Clear Line</button>
                <div id="memory-status">
                    <span id="mem-text">0 MB</span>
                    <div class="mem-bar"><div class="mem-fill" id="mem-fill" style="width:0%"></div></div>
                </div>
            </div>
            <div class="control-row">
                <label>Forecast Hours:</label>
                <div class="chip-group" id="fhr-chips"></div>
            </div>
        </div>
        <div id="map"></div>
    </div>
    <div id="sidebar">
        <div id="xsect-header">
            <span>Cross-Section</span>
            <span id="active-fhr"></span>
        </div>
        <div id="xsect-container">
            <div id="instructions">
                Click two points on the map to draw a cross-section line.<br>
                Then select forecast hours to load.
            </div>
        </div>
    </div>
    <div id="toast-container"></div>

    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script>
        const styles = ''' + json.dumps(XSECT_STYLES) + ''';
        const MAX_SELECTED = 2;  // Maximum forecast hours that can be loaded

        // State
        let startMarker = null, endMarker = null, line = null;
        let cycles = [];           // Available cycles from server
        let currentCycle = null;   // Currently selected cycle key
        let selectedFhrs = [];     // Currently selected/loaded forecast hours
        let activeFhr = null;      // Which FHR is currently displayed in cross-section

        // Initialize map
        const map = L.map('map', {
            center: [39, -98],
            zoom: 5,
            minZoom: 4,
            maxZoom: 10
        });
        L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
            attribution: '&copy; OpenStreetMap, &copy; CARTO'
        }).addTo(map);

        // =========================================================================
        // Toast Notification System
        // =========================================================================
        function showToast(message, type = 'loading', duration = null) {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            toast.className = `toast ${type}`;
            const icon = type === 'loading' ? '⏳' : (type === 'success' ? '✓' : '✗');
            toast.innerHTML = `<span>${icon} ${message}</span>`;
            container.appendChild(toast);

            if (duration || type !== 'loading') {
                setTimeout(() => toast.remove(), duration || 3000);
            }
            return toast;
        }

        function updateMemoryDisplay(memMb) {
            const maxMem = 8000;  // Approximate max for 2 forecast hours
            const pct = Math.min(100, (memMb / maxMem) * 100);
            document.getElementById('mem-text').textContent = `${Math.round(memMb)} MB`;
            document.getElementById('mem-fill').style.width = `${pct}%`;
        }

        // =========================================================================
        // Style Selector
        // =========================================================================
        const styleSelect = document.getElementById('style-select');
        styles.forEach(([val, label]) => {
            const opt = document.createElement('option');
            opt.value = val;
            opt.textContent = label;
            styleSelect.appendChild(opt);
        });
        styleSelect.onchange = generateCrossSection;

        // =========================================================================
        // Cycle (Model Run) Selector
        // =========================================================================
        const cycleSelect = document.getElementById('cycle-select');

        async function loadCycles() {
            try {
                const res = await fetch('/api/cycles');
                const data = await res.json();
                cycles = data.cycles || [];

                cycleSelect.innerHTML = '';
                if (cycles.length === 0) {
                    const opt = document.createElement('option');
                    opt.textContent = 'No data available';
                    cycleSelect.appendChild(opt);
                    return;
                }

                cycles.forEach(c => {
                    const opt = document.createElement('option');
                    opt.value = c.key;
                    // Mark unloaded cycles
                    opt.textContent = c.loaded ? c.display : `${c.display} ⏳`;
                    opt.dataset.fhrs = JSON.stringify(c.fhrs);
                    opt.dataset.loaded = c.loaded ? 'true' : 'false';
                    cycleSelect.appendChild(opt);
                });

                // Select first cycle and render chips
                currentCycle = cycles[0].key;
                renderFhrChips(cycles[0].fhrs, cycles[0].loaded);

                // Check what's already loaded
                await refreshLoadedStatus();

                // If first cycle is loaded, auto-select first available FHR
                if (cycles[0].loaded && cycles[0].fhrs.length > 0) {
                    activeFhr = cycles[0].fhrs[0];
                    selectedFhrs = cycles[0].fhrs.slice();  // All FHRs are "selected" for loaded cycles
                    document.getElementById('active-fhr').textContent = `F${String(activeFhr).padStart(2,'0')}`;
                    renderFhrChips(cycles[0].fhrs, true);
                }
            } catch (err) {
                console.error('Failed to load cycles:', err);
            }
        }

        cycleSelect.onchange = async () => {
            const selected = cycleSelect.options[cycleSelect.selectedIndex];
            currentCycle = selected.value;
            const fhrs = JSON.parse(selected.dataset.fhrs || '[]');
            const isLoaded = selected.dataset.loaded === 'true';

            if (!isLoaded) {
                // Need to load this cycle first
                const toast = showToast(`Loading cycle (this may take a minute)...`);
                try {
                    const res = await fetch(`/api/load_cycle?cycle=${currentCycle}`, {method: 'POST'});
                    const data = await res.json();
                    toast.remove();

                    if (data.success) {
                        showToast(`Loaded ${data.loaded_fhrs} forecast hours`, 'success');
                        selected.textContent = selected.textContent.replace(' ⏳', '');
                        selected.dataset.loaded = 'true';
                        updateMemoryDisplay(data.memory_mb || 0);

                        // Refresh cycles list to update loaded status
                        const cyclesRes = await fetch('/api/cycles');
                        const cyclesData = await cyclesRes.json();
                        cycles = cyclesData.cycles || [];
                    } else {
                        showToast(data.error || 'Failed to load cycle', 'error');
                        return;
                    }
                } catch (err) {
                    toast.remove();
                    showToast('Failed to load cycle', 'error');
                    return;
                }
            }

            // Render chips for loaded cycle
            renderFhrChips(fhrs, true);
            selectedFhrs = fhrs.slice();

            // Auto-select first FHR
            if (fhrs.length > 0) {
                activeFhr = fhrs[0];
                document.getElementById('active-fhr').textContent = `F${String(activeFhr).padStart(2,'0')}`;
                generateCrossSection();
            }
        };

        // =========================================================================
        // Forecast Hour Chips (Split & Chip Pattern)
        // =========================================================================
        function renderFhrChips(availableFhrs, cycleLoaded = false) {
            const container = document.getElementById('fhr-chips');
            container.innerHTML = '';

            // Standard forecast hours to show
            const allFhrs = [0, 6, 12, 18];

            allFhrs.forEach(fhr => {
                const chip = document.createElement('div');
                chip.className = 'chip';
                chip.textContent = `F${String(fhr).padStart(2, '0')}`;
                chip.dataset.fhr = fhr;

                // Mark unavailable
                if (!availableFhrs.includes(fhr)) {
                    chip.classList.add('unavailable');
                    chip.title = 'Data not available';
                } else if (cycleLoaded) {
                    // Cycle is loaded - all available FHRs are ready
                    // Highlight the active one
                    if (fhr === activeFhr) {
                        chip.classList.add('selected');
                    }
                    chip.onclick = () => selectFhr(fhr, chip);
                } else {
                    // Cycle not loaded - chips trigger loading
                    if (selectedFhrs.includes(fhr)) {
                        chip.classList.add('selected');
                    }
                    chip.onclick = () => toggleFhr(fhr, chip);
                }

                container.appendChild(chip);
            });
        }

        // For loaded cycles: just switch which FHR we're viewing
        function selectFhr(fhr, chipEl) {
            // Update active FHR
            activeFhr = fhr;
            document.getElementById('active-fhr').textContent = `F${String(fhr).padStart(2,'0')}`;

            // Update chip visual state
            document.querySelectorAll('#fhr-chips .chip').forEach(c => {
                c.classList.remove('selected');
            });
            chipEl.classList.add('selected');

            // Generate cross-section
            generateCrossSection();
        }

        // For unloaded cycles: load/unload individual FHRs
        async function toggleFhr(fhr, chipEl) {
            if (chipEl.classList.contains('loading') || chipEl.classList.contains('unavailable')) {
                return;  // Ignore clicks while loading or unavailable
            }

            const isSelected = selectedFhrs.includes(fhr);

            if (isSelected) {
                // === UNLOAD this forecast hour ===
                chipEl.classList.add('loading');
                chipEl.classList.remove('selected');
                const toast = showToast(`Unloading F${String(fhr).padStart(2,'0')}...`);

                try {
                    const res = await fetch(`/api/unload?cycle=${currentCycle}&fhr=${fhr}`, {method: 'POST'});
                    const data = await res.json();

                    if (data.success) {
                        selectedFhrs = selectedFhrs.filter(f => f !== fhr);
                        toast.remove();
                        showToast(`Unloaded F${String(fhr).padStart(2,'0')}`, 'success');
                        updateMemoryDisplay(data.memory_mb || 0);

                        // If this was the active FHR, switch to another
                        if (activeFhr === fhr) {
                            activeFhr = selectedFhrs.length > 0 ? selectedFhrs[selectedFhrs.length - 1] : null;
                            if (activeFhr !== null) {
                                generateCrossSection();
                            } else {
                                document.getElementById('xsect-container').innerHTML =
                                    '<div id="instructions">Select a forecast hour to view</div>';
                                document.getElementById('active-fhr').textContent = '';
                            }
                        }
                    } else {
                        toast.remove();
                        showToast(data.error || 'Unload failed', 'error');
                        chipEl.classList.add('selected');
                    }
                } catch (err) {
                    toast.remove();
                    showToast('Unload failed', 'error');
                    chipEl.classList.add('selected');
                }
                chipEl.classList.remove('loading');

            } else {
                // === LOAD this forecast hour ===
                chipEl.classList.add('loading');
                const toast = showToast(`Loading F${String(fhr).padStart(2,'0')}...`);

                try {
                    const res = await fetch(`/api/load?cycle=${currentCycle}&fhr=${fhr}`, {method: 'POST'});
                    const data = await res.json();

                    if (data.success) {
                        toast.remove();
                        showToast(`Loaded F${String(fhr).padStart(2,'0')}`, 'success');

                        // Update selected state based on what server says is loaded
                        await refreshLoadedStatus();

                        // Set this as active and generate cross-section
                        activeFhr = fhr;
                        document.getElementById('active-fhr').textContent = `F${String(fhr).padStart(2,'0')}`;
                        generateCrossSection();
                    } else {
                        toast.remove();
                        showToast(data.error || 'Load failed', 'error');
                    }
                } catch (err) {
                    toast.remove();
                    showToast('Load failed', 'error');
                }
                chipEl.classList.remove('loading');
            }
        }

        async function refreshLoadedStatus() {
            try {
                const res = await fetch('/api/status');
                const data = await res.json();

                // Update selected FHRs based on what's actually loaded
                selectedFhrs = [];
                (data.loaded || []).forEach(item => {
                    if (item[0] === currentCycle) {
                        selectedFhrs.push(item[1]);
                    }
                });

                // Update chip UI
                document.querySelectorAll('#fhr-chips .chip').forEach(chip => {
                    const fhr = parseInt(chip.dataset.fhr);
                    if (selectedFhrs.includes(fhr)) {
                        chip.classList.add('selected');
                    } else {
                        chip.classList.remove('selected');
                    }
                });

                updateMemoryDisplay(data.memory_mb || 0);
            } catch (err) {
                console.error('Failed to refresh status:', err);
            }
        }

        // =========================================================================
        // Map Interaction
        // =========================================================================
        map.on('click', e => {
            const {lat, lng} = e.latlng;

            if (!startMarker) {
                startMarker = L.marker([lat, lng], {
                    draggable: true,
                    icon: L.divIcon({
                        className: 'marker-start',
                        html: '<div style="width:16px;height:16px;background:#38bdf8;border-radius:50%;border:2px solid white;"></div>',
                        iconSize: [16, 16],
                        iconAnchor: [8, 8]
                    })
                }).addTo(map);
                startMarker.on('drag', updateLine);
                startMarker.on('dragend', generateCrossSection);
            } else if (!endMarker) {
                endMarker = L.marker([lat, lng], {
                    draggable: true,
                    icon: L.divIcon({
                        className: 'marker-end',
                        html: '<div style="width:16px;height:16px;background:#f87171;border-radius:50%;border:2px solid white;"></div>',
                        iconSize: [16, 16],
                        iconAnchor: [8, 8]
                    })
                }).addTo(map);
                endMarker.on('drag', updateLine);
                endMarker.on('dragend', generateCrossSection);

                line = L.polyline([startMarker.getLatLng(), endMarker.getLatLng()], {
                    color: '#fbbf24', weight: 3, dashArray: '10, 5'
                }).addTo(map);

                generateCrossSection();
            }
        });

        function updateLine() {
            if (startMarker && endMarker && line) {
                line.setLatLngs([startMarker.getLatLng(), endMarker.getLatLng()]);
            }
        }

        // =========================================================================
        // Cross-Section Generation
        // =========================================================================
        async function generateCrossSection() {
            if (!startMarker || !endMarker) return;
            if (activeFhr === null) {
                document.getElementById('xsect-container').innerHTML =
                    '<div id="instructions">Select a forecast hour chip to load data first</div>';
                return;
            }

            const container = document.getElementById('xsect-container');
            container.innerHTML = '<div class="loading-text">Generating cross-section...</div>';

            const start = startMarker.getLatLng();
            const end = endMarker.getLatLng();
            const style = document.getElementById('style-select').value;

            const url = `/api/xsect?start_lat=${start.lat}&start_lon=${start.lng}` +
                `&end_lat=${end.lat}&end_lon=${end.lng}&cycle=${currentCycle}&fhr=${activeFhr}&style=${style}`;

            try {
                const res = await fetch(url);
                if (!res.ok) throw new Error('Failed to generate');
                const blob = await res.blob();
                const img = document.createElement('img');
                img.id = 'xsect-img';
                img.src = URL.createObjectURL(blob);
                container.innerHTML = '';
                container.appendChild(img);
            } catch (err) {
                container.innerHTML = `<div style="color:#f87171">${err.message}</div>`;
            }
        }

        // Clear button
        document.getElementById('clear-btn').onclick = () => {
            if (startMarker) { map.removeLayer(startMarker); startMarker = null; }
            if (endMarker) { map.removeLayer(endMarker); endMarker = null; }
            if (line) { map.removeLayer(line); line = null; }
            document.getElementById('xsect-container').innerHTML =
                '<div id="instructions">Click two points on the map to draw a cross-section line</div>';
        };

        // =========================================================================
        // Auto-refresh for new cycles
        // =========================================================================
        setInterval(async () => {
            const oldCount = cycles.length;
            await loadCycles();
            if (cycles.length > oldCount) {
                showToast('New model run available!', 'success');
            }
        }, 5 * 60 * 1000);  // Every 5 minutes

        // =========================================================================
        // Initialize
        // =========================================================================
        loadCycles();
    </script>
</body>
</html>'''

# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def index():
    return HTML_TEMPLATE

@app.route('/api/cycles')
def api_cycles():
    """Return available cycles for the dropdown."""
    return jsonify({
        'cycles': data_manager.get_cycles_for_ui(),
    })

@app.route('/api/status')
def api_status():
    """Return current memory/loading status."""
    return jsonify(data_manager.get_loaded_status())

@app.route('/api/load', methods=['POST'])
@rate_limit
def api_load():
    """Load a forecast hour into memory."""
    cycle_key = request.args.get('cycle')
    fhr = request.args.get('fhr')

    if not cycle_key or fhr is None:
        return jsonify({'success': False, 'error': 'Missing cycle or fhr parameter'}), 400

    try:
        fhr = int(fhr)
    except ValueError:
        return jsonify({'success': False, 'error': 'Invalid fhr'}), 400

    result = data_manager.load_forecast_hour(cycle_key, fhr)
    return jsonify(result)

@app.route('/api/load_cycle', methods=['POST'])
@rate_limit
def api_load_cycle():
    """Load an entire cycle (all FHRs) into memory."""
    cycle_key = request.args.get('cycle')

    if not cycle_key:
        return jsonify({'success': False, 'error': 'Missing cycle parameter'}), 400

    result = data_manager.load_cycle(cycle_key)
    return jsonify(result)

@app.route('/api/unload', methods=['POST'])
@rate_limit
def api_unload():
    """Unload a forecast hour from memory."""
    cycle_key = request.args.get('cycle')
    fhr = request.args.get('fhr')

    if not cycle_key or fhr is None:
        return jsonify({'success': False, 'error': 'Missing cycle or fhr parameter'}), 400

    try:
        fhr = int(fhr)
    except ValueError:
        return jsonify({'success': False, 'error': 'Invalid fhr'}), 400

    result = data_manager.unload_forecast_hour(cycle_key, fhr)
    return jsonify(result)

@app.route('/api/xsect')
@rate_limit
def api_xsect():
    """Generate a cross-section image."""
    try:
        start = (float(request.args['start_lat']), float(request.args['start_lon']))
        end = (float(request.args['end_lat']), float(request.args['end_lon']))
        cycle_key = request.args.get('cycle')
        fhr = int(request.args.get('fhr', 0))
        style = request.args.get('style', 'wind_speed')
    except (KeyError, ValueError) as e:
        return jsonify({'error': f'Invalid parameters: {e}'}), 400

    if not cycle_key:
        return jsonify({'error': 'Missing cycle parameter'}), 400

    buf = data_manager.generate_cross_section(start, end, cycle_key, fhr, style)
    if buf is None:
        return jsonify({'error': 'Failed to generate cross-section. Data may not be loaded.'}), 500

    return send_file(buf, mimetype='image/png')

# Legacy endpoint for compatibility
@app.route('/api/info')
def api_info():
    """Legacy endpoint - returns available times."""
    times = data_manager.get_available_times()
    return jsonify({
        'times': times,
        'hours': [t['fhr'] for t in times],
        'styles': XSECT_STYLES,
    })

# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description='HRRR Cross-Section Dashboard')
    parser.add_argument('--auto-update', action='store_true', help='Download latest data before starting')
    parser.add_argument('--n-cycles', type=int, default=5, help='Number of cycles to scan for')
    parser.add_argument('--preload', type=int, default=2, help='Number of latest cycles to pre-load')
    parser.add_argument('--max-hours', type=int, default=18, help='Max forecast hour to download')
    parser.add_argument('--port', type=int, default=5000, help='Server port')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Server host')
    parser.add_argument('--production', action='store_true', help='Enable rate limiting')

    args = parser.parse_args()
    app.config['PRODUCTION'] = args.production

    # Optionally download fresh data
    if args.auto_update:
        from smart_hrrr.orchestrator import download_latest_cycle

        logger.info("Downloading latest HRRR data...")
        fhrs_to_download = [0, 6, 12, 18]
        fhrs_to_download = [f for f in fhrs_to_download if f <= args.max_hours]

        date_str, hour, results = download_latest_cycle(
            max_hours=max(fhrs_to_download),
            forecast_hours=fhrs_to_download
        )
        if not date_str:
            logger.error("Failed to download data")
            sys.exit(1)
        logger.info(f"Downloaded {sum(results.values())}/{len(fhrs_to_download)} forecast hours")

    # Scan for available cycles
    logger.info(f"Scanning for available cycles...")
    cycles = data_manager.scan_available_cycles(n_cycles=args.n_cycles)

    if not cycles:
        logger.error("No data found. Run with --auto-update to download.")
        sys.exit(1)

    logger.info(f"Found {len(cycles)} cycles:")
    for c in cycles:
        fhrs_str = ', '.join(f'F{f:02d}' for f in c['available_fhrs'])
        logger.info(f"  {c['display']}: [{fhrs_str}]")

    # Pre-load latest cycles
    logger.info("")
    logger.info(f"Pre-loading latest {args.preload} cycles...")
    data_manager.preload_latest_cycles(n_cycles=args.preload)

    mem_mb = data_manager.xsect.get_memory_usage() if data_manager.xsect else 0
    logger.info("")
    logger.info("=" * 60)
    logger.info("HRRR Cross-Section Dashboard")
    logger.info(f"Pre-loaded: {len(data_manager.loaded_cycles)} cycles ({mem_mb:.0f} MB)")
    logger.info(f"Older cycles available on-demand")
    logger.info(f"Open: http://{args.host}:{args.port}")
    logger.info("=" * 60)

    app.run(host=args.host, port=args.port, threaded=True)

if __name__ == '__main__':
    main()
