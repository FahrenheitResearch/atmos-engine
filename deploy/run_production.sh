#!/bin/bash
# HRRR Cross-Section Dashboard - Production Runner
# Run this on your home PC to serve the dashboard

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_DIR"

# Configuration
PORT=${PORT:-5559}
MAX_HOURS=${MAX_HOURS:-12}
UPDATE_INTERVAL=${UPDATE_INTERVAL:-3600}  # 1 hour in seconds

echo "=============================================="
echo "HRRR Cross-Section Dashboard - Production Mode"
echo "=============================================="
echo "Port: $PORT"
echo "Max forecast hours: $MAX_HOURS"
echo "Update interval: ${UPDATE_INTERVAL}s"
echo ""

# Function to update data and restart server
update_and_serve() {
    echo "[$(date)] Downloading latest HRRR data..."

    # Kill existing server if running
    pkill -f "unified_dashboard.py" 2>/dev/null || true
    sleep 2

    # Start server with auto-update (downloads latest, then serves)
    python tools/unified_dashboard.py \
        --auto-update \
        --port "$PORT" \
        --max-hours "$MAX_HOURS" \
        --production &

    SERVER_PID=$!
    echo "[$(date)] Server started (PID: $SERVER_PID)"
}

# Initial start
update_and_serve

# Keep running and update periodically
while true; do
    sleep "$UPDATE_INTERVAL"
    echo ""
    echo "[$(date)] Scheduled update..."
    update_and_serve
done
