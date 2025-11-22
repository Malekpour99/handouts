#!/bin/bash
# unset-proxy.sh - Remove all proxy settings

set -e

if [ "$EUID" -ne 0 ]; then 
    echo "Run as root or use sudo"
    exit 1
fi

echo "Removing proxy settings"

# /etc/environment
sed -i '/^http_proxy=/d' /etc/environment 2>/dev/null || true
sed -i '/^https_proxy=/d' /etc/environment 2>/dev/null || true
sed -i '/^ftp_proxy=/d' /etc/environment 2>/dev/null || true

# /etc/profile.d/http_proxy.sh
rm -f /etc/profile.d/http_proxy.sh

# Current session
unset http_proxy
unset https_proxy
unset ftp_proxy

# apt config
rm -f /etc/apt/apt.conf.d/95proxies
[ -f /etc/apt.conf ] && sed -i '/Acquire::/d' /etc/apt.conf 2>/dev/null || true

# yum config
if [ -f /etc/yum.conf ]; then
    sed -i '/^proxy=/d' /etc/yum.conf
fi

# wget config
sed -i '/^http_proxy/d' /etc/wgetrc 2>/dev/null || true
sed -i '/^https_proxy/d' /etc/wgetrc 2>/dev/null || true
sed -i '/^ftp_proxy/d' /etc/wgetrc 2>/dev/null || true
sed -i '/^# Proxy settings/d' /etc/wgetrc 2>/dev/null || true

echo "Proxy removed. Log out and back in for full effect."
