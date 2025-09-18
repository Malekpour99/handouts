# HAProxy

## Installation

```sh
# update repositories
sudo apt update

# install HA-Proxy
sudo apt install haproxy
```

### Configuration

You can configure HAProxy in this path: `/etc/haproxy/haproxy.cfg`

```sh
vim /etc/haproxy/haproxy.cfg
```

- Sample Configuration for zipkin services

```text
frontend lb
  bind *:80
  stats uri /haproxy?stats
  default_backend zipkin
backend zipkin
  balance roundrobin
  server worker1 192.168.230.133:9411 check
  server worker1 192.168.230.134:9411 check
```

- `frontend` -> Receivers of requests
- `bind` -> Port of frontend where requests are received
- `backend` -> processors of requests
- `balance` -> load balancing algorithm used between backend servers

Add this to the end of your configuration file.
