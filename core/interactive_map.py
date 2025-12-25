"""Interactive map generator for weather data visualization.

Creates Leaflet-based interactive maps where users can hover/click
to see data values at any point - similar to PivotalWeather.
"""

import json
import numpy as np
from pathlib import Path
from typing import Optional, Dict, Any, Tuple
import folium
from folium import plugins


def _regrid_curvilinear_to_regular(
    values2d: np.ndarray,
    lats2d: np.ndarray,
    lons2d: np.ndarray,
    dlat: float = 0.03,
    dlon: float = 0.03,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, Tuple[float, float, float, float]]:
    """Regrid curvilinear data to regular lat/lon grid using nearest-neighbor.

    This is necessary because Leaflet's ImageOverlay assumes a rectilinear
    lat/lon raster, but HRRR uses Lambert Conformal with curvilinear coords.

    Returns:
        (values_regular, lats_1d, lons_1d, (lat_min, lat_max, lon_min, lon_max))
    """
    from scipy.spatial import cKDTree

    # Get bounds from corners (better than global min/max for curvilinear)
    corners_lat = np.array([lats2d[0, 0], lats2d[0, -1], lats2d[-1, 0], lats2d[-1, -1]])
    corners_lon = np.array([lons2d[0, 0], lons2d[0, -1], lons2d[-1, 0], lons2d[-1, -1]])

    lat_min, lat_max = float(np.nanmin(corners_lat)), float(np.nanmax(corners_lat))
    lon_min, lon_max = float(np.nanmin(corners_lon)), float(np.nanmax(corners_lon))

    # Create regular target grid
    lat_t = np.arange(lat_max, lat_min - dlat, -dlat)  # North to south for image
    lon_t = np.arange(lon_min, lon_max + dlon, dlon)
    lon_grid, lat_grid = np.meshgrid(lon_t, lat_t)

    # Build KDTree over source points
    src_pts = np.column_stack([lats2d.ravel(), lons2d.ravel()])
    tree = cKDTree(src_pts)

    # Query nearest neighbors for target grid
    tgt_pts = np.column_stack([lat_grid.ravel(), lon_grid.ravel()])
    distances, idx = tree.query(tgt_pts, k=1)

    # Map values to regular grid
    vals_src = values2d.ravel()
    vals_reg = vals_src[idx].reshape(lat_grid.shape)

    # Mask points too far from any source point (outside data coverage)
    # Use ~2x the grid spacing as threshold
    max_dist = np.sqrt(dlat**2 + dlon**2) * 2
    vals_reg[distances.reshape(lat_grid.shape) > max_dist] = np.nan

    return vals_reg, lat_t, lon_t, (lat_min, lat_max, lon_min, lon_max)


def create_interactive_map(
    data,  # xarray.DataArray
    field_name: str,
    field_config: Dict[str, Any],
    cycle: str,
    forecast_hour: int,
    output_dir: Path,
    colormap: str = "viridis",
) -> Optional[Path]:
    """Create an interactive HTML map with hover values.

    Args:
        data: xarray DataArray with lat/lon coordinates
        field_name: Name of the field
        field_config: Field configuration dict
        cycle: Model cycle string
        forecast_hour: Forecast hour
        output_dir: Output directory
        colormap: Matplotlib colormap name

    Returns:
        Path to generated HTML file, or None on failure
    """
    try:
        import matplotlib.pyplot as plt
        import matplotlib.colors as mcolors

        # Get data values and coordinates
        values = data.values
        lats = data.latitude.values if 'latitude' in data.coords else data.lat.values
        lons = data.longitude.values if 'longitude' in data.coords else data.lon.values

        # Convert longitudes to -180 to 180 range if needed
        if lons.max() > 180:
            lons = np.where(lons > 180, lons - 360, lons)

        # Get value range for colormap
        # Use levels if available, otherwise vmin/vmax, otherwise data range
        levels = field_config.get('levels')
        if levels and len(levels) >= 2:
            vmin = float(min(levels))
            vmax = float(max(levels))
        else:
            vmin = field_config.get('vmin', float(np.nanmin(values)))
            vmax = field_config.get('vmax', float(np.nanmax(values)))

        # Handle curvilinear vs regular grids differently
        # Curvilinear grids (like HRRR Lambert Conformal) must be regridded
        # to regular lat/lon for ImageOverlay to work correctly
        is_curvilinear = lats.ndim == 2

        if is_curvilinear:
            # Regrid to regular lat/lon - this makes overlay and hover consistent
            # Use ~0.03 degree resolution (~3km, similar to HRRR native)
            values_reg, lats_1d, lons_1d, bounds = _regrid_curvilinear_to_regular(
                values, lats, lons, dlat=0.03, dlon=0.03
            )
            lat_min, lat_max, lon_min, lon_max = bounds

            # For regular grid, image rows are already north-to-south from regrid
            values_for_image = values_reg
            values_for_hover = values_reg
            lats_for_hover = lats_1d
            lons_for_hover = lons_1d
        else:
            # Regular 1D grid - subsample for performance
            step = 2
            values_sub = values[::step, ::step]
            lats_sub = lats[::step]
            lons_sub = lons[::step]

            lat_min, lat_max = float(lats.min()), float(lats.max())
            lon_min, lon_max = float(lons.min()), float(lons.max())

            # Check if we need to flip for north-up display
            if lats_sub[0] < lats_sub[-1]:  # South to north
                values_for_image = np.flipud(values_sub)
                values_for_hover = np.flipud(values_sub)
                lats_for_hover = lats_sub[::-1]
            else:
                values_for_image = values_sub
                values_for_hover = values_sub
                lats_for_hover = lats_sub
            lons_for_hover = lons_sub

        # Calculate center
        center_lat = (lat_min + lat_max) / 2
        center_lon = (lon_min + lon_max) / 2

        # Create color-mapped image
        # Handle custom colormaps - fall back to standard ones
        try:
            cmap = plt.get_cmap(colormap)
        except ValueError:
            # Custom colormap not available, use appropriate fallback
            if 'reflectivity' in field_name.lower() or 'refl' in colormap.lower():
                cmap = plt.get_cmap('turbo')  # Good for radar
            else:
                cmap = plt.get_cmap('viridis')
        norm = mcolors.Normalize(vmin=vmin, vmax=vmax)

        # Normalize values and apply colormap
        values_norm = norm(values_for_image)
        rgba = cmap(values_norm)

        # Mask values below vmin or NaN (make transparent)
        mask = (values_for_image < vmin) | np.isnan(values_for_image)
        rgba[mask, 3] = 0  # Set alpha to 0 for masked values

        # Convert to uint8 for PNG
        rgba_uint8 = (rgba * 255).astype(np.uint8)

        # Create base map
        m = folium.Map(
            location=[center_lat, center_lon],
            zoom_start=4,
            tiles='CartoDB positron',
        )

        # Add image overlay
        from PIL import Image
        import io
        import base64

        img = Image.fromarray(rgba_uint8, 'RGBA')

        # Save to bytes
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        img_base64 = base64.b64encode(img_bytes.read()).decode()

        # Add as image overlay
        bounds = [[lat_min, lon_min], [lat_max, lon_max]]
        folium.raster_layers.ImageOverlay(
            image=f"data:image/png;base64,{img_base64}",
            bounds=bounds,
            opacity=0.7,
            name=field_name,
        ).add_to(m)

        # Prepare data for JavaScript hover lookup
        # After regridding, we always have regular 1D lat/lon arrays
        # Subsample hover data for smaller file size (values_for_hover matches image)
        hover_step = 2
        values_js = values_for_hover[::hover_step, ::hover_step]
        lats_js = lats_for_hover[::hover_step]
        lons_js = lons_for_hover[::hover_step]

        # Convert to nested list for 2D array access in JS
        values_list = []
        for row in values_js:
            row_list = []
            for val in row:
                if np.isnan(val):
                    row_list.append(None)
                else:
                    row_list.append(round(float(val), 1))
            values_list.append(row_list)

        lats_list = lats_js.tolist()
        lons_list = lons_js.tolist()

        # Get units
        units = field_config.get('units', '')
        title = field_config.get('title', field_name)

        # Get Folium's map variable name for reliable JS access
        map_var = m.get_name()

        # JavaScript for hover display - uses binary search on regular grid
        hover_js = f"""
        <script>
        var weatherData = {{
            lats: {json.dumps(lats_list)},
            lons: {json.dumps(lons_list)},
            values: {json.dumps(values_list)},
            units: "{units}",
            title: "{title}"
        }};

        function binarySearchNearest(arr, val, descending) {{
            var lo = 0, hi = arr.length - 1;
            while (lo < hi - 1) {{
                var mid = (lo + hi) >> 1;
                if (descending) {{
                    if (arr[mid] > val) lo = mid;
                    else hi = mid;
                }} else {{
                    if (arr[mid] < val) lo = mid;
                    else hi = mid;
                }}
            }}
            return Math.abs(arr[lo] - val) < Math.abs(arr[hi] - val) ? lo : hi;
        }}

        function findNearestValue(lat, lon) {{
            var lats = weatherData.lats;
            var lons = weatherData.lons;
            var values = weatherData.values;

            // Lats are north-to-south (descending), lons are west-to-east (ascending)
            var latIdx = binarySearchNearest(lats, lat, true);
            var lonIdx = binarySearchNearest(lons, lon, false);

            if (latIdx >= 0 && latIdx < values.length &&
                lonIdx >= 0 && lonIdx < values[0].length) {{
                return values[latIdx][lonIdx];
            }}
            return null;
        }}"""

        hover_js += f"""

        document.addEventListener('DOMContentLoaded', function() {{
            var map = document.querySelector('.folium-map');
            if (!map) return;

            // Create info display
            var info = document.createElement('div');
            info.id = 'weather-info';
            info.style.cssText = 'position:absolute;top:10px;right:10px;z-index:1000;background:white;padding:10px;border-radius:5px;box-shadow:0 2px 5px rgba(0,0,0,0.3);font-family:monospace;min-width:200px;';
            info.innerHTML = '<b>{title}</b><br>Hover over map for values';
            document.body.appendChild(info);

            // Create opacity slider
            var sliderDiv = document.createElement('div');
            sliderDiv.style.cssText = 'position:fixed;bottom:80px;left:10px;z-index:1000;background:white;padding:10px;border-radius:5px;box-shadow:0 2px 5px rgba(0,0,0,0.3);';
            sliderDiv.innerHTML = '<label style="font-weight:bold;">Opacity: <span id="opacity-val">70%</span></label><br>' +
                '<input type="range" id="opacity-slider" min="0" max="100" value="70" style="width:150px;">';
            document.body.appendChild(sliderDiv);

            // Add mousemove with throttling and opacity control
            setTimeout(function() {{
                var leafletMap = {map_var};
                if (leafletMap && leafletMap.on) {{
                    // Throttle mousemove to ~20 FPS for performance
                    var lastT = 0;
                    leafletMap.on('mousemove', function(e) {{
                        var now = performance.now();
                        if (now - lastT < 50) return;
                        lastT = now;

                        var lat = e.latlng.lat;
                        var lon = e.latlng.lng;
                        var val = findNearestValue(lat, lon);
                        var valStr = (val === null) ? 'No data' : val + ' {units}';
                        info.innerHTML = '<b>{title}</b><br>' +
                            'Lat: ' + lat.toFixed(2) + '°<br>' +
                            'Lon: ' + lon.toFixed(2) + '°<br>' +
                            '<b>Value: ' + valStr + '</b>';
                    }});

                    // Connect opacity slider to image overlay
                    var slider = document.getElementById('opacity-slider');
                    var opacityVal = document.getElementById('opacity-val');
                    slider.addEventListener('input', function() {{
                        var opacity = this.value / 100;
                        opacityVal.textContent = this.value + '%';
                        var overlays = document.querySelectorAll('.leaflet-image-layer');
                        overlays.forEach(function(overlay) {{
                            overlay.style.opacity = opacity;
                        }});
                    }});
                }}
            }}, 500);
        }});
        </script>
        """

        # Add the JavaScript
        m.get_root().html.add_child(folium.Element(hover_js))

        # Add layer control
        folium.LayerControl().add_to(m)

        # Add colorbar legend
        colorbar_html = f"""
        <div style="position:fixed;bottom:30px;left:10px;z-index:1000;background:white;padding:10px;border-radius:5px;box-shadow:0 2px 5px rgba(0,0,0,0.3);">
            <div style="font-weight:bold;margin-bottom:5px;">{title}</div>
            <div style="display:flex;align-items:center;">
                <span>{vmin:.1f}</span>
                <div style="width:150px;height:15px;margin:0 5px;background:linear-gradient(to right,
                    {mcolors.to_hex(cmap(0.0))},
                    {mcolors.to_hex(cmap(0.25))},
                    {mcolors.to_hex(cmap(0.5))},
                    {mcolors.to_hex(cmap(0.75))},
                    {mcolors.to_hex(cmap(1.0))});"></div>
                <span>{vmax:.1f}</span>
                <span style="margin-left:5px;">{units}</span>
            </div>
        </div>
        """
        m.get_root().html.add_child(folium.Element(colorbar_html))

        # Add title
        title_html = f"""
        <div style="position:fixed;top:10px;left:50%;transform:translateX(-50%);z-index:1000;background:white;padding:10px 20px;border-radius:5px;box-shadow:0 2px 5px rgba(0,0,0,0.3);font-size:16px;font-weight:bold;">
            {title} - {cycle} F{forecast_hour:02d}
        </div>
        """
        m.get_root().html.add_child(folium.Element(title_html))

        # Save
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"{field_name}_f{forecast_hour:02d}_interactive.html"
        m.save(str(output_path))

        return output_path

    except Exception as e:
        print(f"Error creating interactive map: {e}")
        import traceback
        traceback.print_exc()
        return None


def batch_create_interactive_maps(
    data_dict: Dict[str, Any],  # field_name -> (data, field_config)
    cycle: str,
    forecast_hour: int,
    output_dir: Path,
) -> Dict[str, Path]:
    """Create interactive maps for multiple fields.

    Returns dict mapping field_name -> output_path
    """
    results = {}
    for field_name, (data, field_config) in data_dict.items():
        colormap = field_config.get('colormap', 'viridis')
        path = create_interactive_map(
            data, field_name, field_config,
            cycle, forecast_hour, output_dir, colormap
        )
        if path:
            results[field_name] = path
    return results
