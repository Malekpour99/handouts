#!/bin/bash
# set-proxy.sh - Configure system-wide proxy settings

set -e

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <proxy_ip> <proxy_port>"
    echo "Example: $0 localhost 10808"
    exit 1
fi

PROXY_IP="$1"
PROXY_PORT="$2"
PROXY_URL="http://${PROXY_IP}:${PROXY_PORT}"

if [ "$EUID" -ne 0 ]; then 
    echo "Run as root or use sudo"
    exit 1
fi

echo "Setting proxy to ${PROXY_URL}"

# /etc/environment
if ! grep -q "^http_proxy=" /etc/environment 2>/dev/null; then
    echo "http_proxy=${PROXY_URL}" >> /etc/environment
    echo "https_proxy=${PROXY_URL}" >> /etc/environment
    echo "ftp_proxy=${PROXY_URL}" >> /etc/environment
else
    sed -i "s|^http_proxy=.*|http_proxy=${PROXY_URL}|" /etc/environment
    sed -i "s|^https_proxy=.*|https_proxy=${PROXY_URL}|" /etc/environment
    sed -i "s|^ftp_proxy=.*|ftp_proxy=${PROXY_URL}|" /etc/environment
fi

# /etc/profile.d/http_proxy.sh
cat > /etc/profile.d/http_proxy.sh <<EOF
export http_proxy=${PROXY_URL}
export https_proxy=${PROXY_URL}
export ftp_proxy=${PROXY_URL}
EOF
chmod +x /etc/profile.d/http_proxy.sh

# Current session
export http_proxy="${PROXY_URL}"
export https_proxy="${PROXY_URL}"
export ftp_proxy="${PROXY_URL}"

# apt config
if command -v apt &>/dev/null; then
    cat > /etc/apt/apt.conf.d/95proxies <<EOF
Acquire::http::Proxy "${PROXY_URL}";
Acquire::https::Proxy "${PROXY_URL}";
Acquire::ftp::Proxy "${PROXY_URL}";
EOF
fi

# yum config (note: your doc has wrong format - yum uses proxy=, not [main] section for proxy)
if command -v yum &>/dev/null && [ -f /etc/yum.conf ]; then
    if ! grep -q "^proxy=" /etc/yum.conf; then
        echo "proxy=${PROXY_URL}" >> /etc/yum.conf
    else
        sed -i "s|^proxy=.*|proxy=${PROXY_URL}|" /etc/yum.conf
    fi
fi

# wget config
if ! grep -q "^http_proxy" /etc/wgetrc 2>/dev/null; then
    cat >> /etc/wgetrc <<EOF

# Proxy settings
http_proxy = ${PROXY_URL}
https_proxy = ${PROXY_URL}
ftp_proxy = ${PROXY_URL}
EOF
else
    sed -i "s|^http_proxy.*|http_proxy = ${PROXY_URL}|" /etc/wgetrc
    sed -i "s|^https_proxy.*|https_proxy = ${PROXY_URL}|" /etc/wgetrc
    sed -i "s|^ftp_proxy.*|ftp_proxy = ${PROXY_URL}|" /etc/wgetrc
fi

echo "Proxy configured. Log out and back in for full effect, or run: source /etc/profile.d/http_proxy.sh"