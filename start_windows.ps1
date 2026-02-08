# start_windows.ps1 - Start wxsection dashboard on native Windows
#
# Usage:
#   .\start_windows.ps1                    # Dashboard only (default)
#   .\start_windows.ps1 -WithAutoUpdate    # Dashboard + auto-update

param(
    [switch]$WithAutoUpdate
)

# --- Environment ---
$env:XSECT_GRIB_BACKEND = "auto"
$env:WXSECTION_KEY = "cwtc"

# Cache dir defaults to ./cache/xsect (relative to repo root)
# Override with $env:XSECT_CACHE_DIR if you want a different location
if (-not $env:XSECT_CACHE_DIR) {
    $env:XSECT_CACHE_DIR = Join-Path $PSScriptRoot "cache" "xsect"
}

# Status file defaults to %TEMP%\auto_update_status.json
# (auto_update.py and dashboard agree on this automatically via tempfile)

Write-Host "=== wxsection.com - Windows Startup ===" -ForegroundColor Cyan
Write-Host "Cache dir:    $env:XSECT_CACHE_DIR"
Write-Host "GRIB backend: $env:XSECT_GRIB_BACKEND"

# --- Auto-update (optional) ---
if ($WithAutoUpdate) {
    Write-Host "`nStarting auto-update in background..." -ForegroundColor Yellow
    Start-Process python -ArgumentList "tools/auto_update.py", "--interval", "2", "--models", "hrrr,gfs,rrfs" -NoNewWindow
    Start-Sleep -Seconds 2
}

# --- Dashboard ---
Write-Host "`nStarting dashboard on port 5561..." -ForegroundColor Green
python tools/unified_dashboard.py --port 5561 --models hrrr,gfs,rrfs
