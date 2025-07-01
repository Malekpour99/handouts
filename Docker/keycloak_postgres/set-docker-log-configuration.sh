#!/bin/bash

set -e

CONFIG_FILE="/etc/docker/daemon.json"

# Backup existing Docker config
if [ -f "$CONFIG_FILE" ]; then
  echo "Backing up existing Docker daemon.json to daemon.json.bak"
  cp "$CONFIG_FILE" "$CONFIG_FILE.bak"
fi

# Write log config with local driver and daily rotation
cat >"$CONFIG_FILE" <<EOF
{
  "log-driver": "local",
  "log-opts": {
    "max-size": "10m",
    "max-file": "20",
    "max-age": "1d"
  }
}
EOF

echo "Docker log configuration updated:"
cat "$CONFIG_FILE"

# Restart Docker
echo "Restarting Docker service..."
systemctl restart docker

echo "Docker log configuration applied successfully."
