# Proxy Setup

- Find your system or proxy service IP (e.g. `localhost`)
- Find your v2ray client port (`LAN - HTTP`) (e.g. `10808`)

## Setting Up Proxy

- Setup a Network Proxy in GUI
  - choose `Manual` mode
  - set `HTTP Proxy`
  - set `HTTPS Proxy`

- Check `$http_proxy`
  - `echo $http_proxy`
  - `export http_proxy=http://localhost:10808`

- Add Proxy to environments
  - `vim /etc/environment`
  - `http_proxy=http://localhost:10808`

- Add Proxy to profile
  - `vim /etc/profile.d/http_proxy.sh`
  - `http_proxy=http://localhost:10808`

  - `vim /etc/profile`

  - ```
    export http_proxy=http://localhost:10808
    export https_proxy=http://localhost:10808
    export ftp_proxy=http://localhost:10808
    ```

- Add Proxy to package manager (e.g. `yum`, `apt`)
  - `vim /etc/yum.conf`

  - ```
    [main]
    proxy=localhost:10808
    gpgcheck=1
    installonly_limit=3
    clean_requirements_on_remove=True
    best=True
    skip_if_unavailable=False
    ```

- Add Proxy to Docker:
  - `mkdir /etc/systemd/system/docker.service.d`
  - `cd /etc/systemd/system/docker.service.d`
  - `vim http-proxy.conf`

  - ```
    [Service]
    Environment="HTTPS_PROXY=localhost:10808"
    ```

  - `sudo systemctl daemon-reload`
  - `sudo systemctl restart docker`

- Add Proxy to `wget` tool
  - `vim /etc/wgetrc`

  - ```
    http_proxy = http://localhost:10808
    https_proxy = http://localhost:10808
    ftp_proxy = http://localhost:10808
    ```

## Testing Proxy

- `curl google.com -v` (You should see `Connected to <Proxy Address>`)
- `wget google.com -v` (You should see `Connecting to <Proxy Address>... Connected`)
- `systemctl show docker --property Environment` (You should see `Environment="HTTPS_PROXY=localhost:10808"`)
