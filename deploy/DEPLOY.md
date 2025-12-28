# Deploy HRRR Cross-Section Dashboard from Home PC

## Quick Start

### 1. Run the Server
```bash
chmod +x deploy/run_production.sh
./deploy/run_production.sh
```

This will:
- Download latest HRRR data
- Start the dashboard on port 5559
- Auto-update every hour with fresh data

### 2. Expose to Internet (Cloudflare Tunnel - Recommended)

Cloudflare Tunnel is free, secure, and handles SSL automatically. No port forwarding needed.

#### Install cloudflared
```bash
# Ubuntu/Debian
curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb -o cloudflared.deb
sudo dpkg -i cloudflared.deb

# Or with brew
brew install cloudflare/cloudflare/cloudflared
```

#### Quick Tunnel (for testing)
```bash
# This gives you a temporary public URL instantly
cloudflared tunnel --url http://localhost:5559
```
You'll get a URL like `https://random-words.trycloudflare.com`

#### Permanent Tunnel (for production)
```bash
# 1. Login to Cloudflare
cloudflared tunnel login

# 2. Create tunnel
cloudflared tunnel create hrrr-dashboard

# 3. Route your domain
cloudflared tunnel route dns hrrr-dashboard xsect.yourdomain.com

# 4. Create config file
cat > ~/.cloudflared/config.yml << EOF
tunnel: hrrr-dashboard
credentials-file: /home/$USER/.cloudflared/<tunnel-id>.json

ingress:
  - hostname: xsect.yourdomain.com
    service: http://localhost:5559
  - service: http_status:404
EOF

# 5. Run as service
sudo cloudflared service install
sudo systemctl start cloudflared
```

### 3. Run Everything at Boot

Create systemd service for the dashboard:
```bash
sudo tee /etc/systemd/system/hrrr-dashboard.service << EOF
[Unit]
Description=HRRR Cross-Section Dashboard
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=/home/$USER/hrrr-maps
ExecStart=/home/$USER/hrrr-maps/deploy/run_production.sh
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable hrrr-dashboard
sudo systemctl start hrrr-dashboard
```

## Alternative: ngrok (simpler but limited free tier)

```bash
# Install
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc
echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
sudo apt update && sudo apt install ngrok

# Run
ngrok http 5559
```

## Resource Requirements

- **RAM**: ~25GB for 7 hours, ~50GB for 12 hours, ~80GB for 18 hours
- **Disk**: ~15GB for cached data per run
- **CPU**: Minimal once loaded (cross-sections render in <1s)
- **Bandwidth**: ~500MB per data update

## Monitoring

Check status:
```bash
# Dashboard logs
journalctl -u hrrr-dashboard -f

# Tunnel logs
journalctl -u cloudflared -f

# Memory usage
free -h
```
