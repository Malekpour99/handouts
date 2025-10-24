# Traefik

## Table of Contents

- [Traefik](#traefik)
  - [Table of Contents](#table-of-contents)
  - [Configuration](#configuration)
    - [Static](#static)
    - [Dynamic](#dynamic)
  - [Request Flow](#request-flow)
  - [YAML Configuration File](#yaml-configuration-file)
  - [CLI Configuration (`docker-compose.yaml` file)](#cli-configuration-docker-composeyaml-file)
    - [Volumes](#volumes)
  - [Labels Configuration](#labels-configuration)

## Configuration

### Static

- Defines how Traefik itself runs. The static configuration **controls Traefik’s core behavior** — the `entrypoints`, `providers`, `logs`, `certificates`, and `dashboard`.
- It’s called **“static”** because you must **restart** Traefik whenever you change it.

- Commonly set in:
  - `traefik.yml`
  - CLI arguments (--entrypoints.web.address=:80)
  - Environment variables
  - Docker labels (for providers, minimally)

| Section                 | Description                                                                             |
| ----------------------- | --------------------------------------------------------------------------------------- |
| `entryPoints`           | Defines ports and protocols Traefik listens on (e.g., HTTP :80, HTTPS :443).            |
| `providers`             | Tells Traefik **where to find dynamic configuration** (Docker, Kubernetes, file, etc.). |
| `api`                   | Enables Traefik’s dashboard and REST API.                                               |
| `log` / `accessLog`     | Controls Traefik’s internal logs and access logs.                                       |
| `certificatesResolvers` | Configures Let’s Encrypt/ACME automatic certificate generation.                         |
| `metrics` / `tracing`   | Enables Prometheus, Datadog, etc. for observability.                                    |

### Dynamic

- Defines how traffic is handled and routed. This controls the **runtime routing behavior** — what to do with requests, how to forward them, what headers to apply, etc.
- Dynamic config can be **reloaded live without restarting** Traefik.

- Commonly set in:
  - A file provider (`dynamic.yml` or multiple files)
  - Docker labels
  - Kubernetes ingress annotations
  - Consul / etcd (key-value stores)

| Section       | Description                                                                         |
| ------------- | ----------------------------------------------------------------------------------- |
| `routers`     | Define **routing rules**: which requests go where (by domain, path, headers, etc.). |
| `services`    | Define **backends**: the actual servers or containers handling the requests.        |
| `middlewares` | Define **filters or modifiers**: security headers, redirects, rate limits, etc.     |
| `tls`         | Define **certificates and cipher options** for HTTPS routing.                       |

## Request Flow

**`entrypoint → router → middleware → service`**

---

## YAML Configuration File

```yaml
http:
  middlewares:
    security:
      headers:
        frameDeny: true
        contentTypeNosniff: true
        browserXssFilter: true
    hsts:
      headers:
        stsSeconds: 31536000
        stsIncludeSubdomains: true
        stsPreload: true
        forceSTSHeader: true
```

- `http`: → Root section for HTTP-related configuration (`middlewares`, `routers`, `services`).
  - `middlewares`: → Defines named middlewares — reusable components that can modify requests/responses (e.g., add `headers`).
    - `security`: → A middleware named `security`.
      - `headers`: → Configures HTTP security headers.
        - `frameDeny`: true → Adds `X-Frame-Options: DENY` which Prevents your site from being embedded in an `<iframe>`, mitigating click-jacking attacks.
        - `contentTypeNosniff`: true → Adds `X-Content-Type-Options: nosniff` which Stops browsers from MIME-sniffing content types. Helps prevent content-type confusion attacks.
        - `browserXssFilter`: true → Adds `X-XSS-Protection: 1; mode=block` which Enables legacy browser XSS filters (helpful for older browsers; modern browsers ignore it).
    - `hsts`: → Another middleware, typically used to enforce **HTTP Strict Transport Security (HSTS)**.
      - `headers`: → Adds Strict-Transport-Security header.
        - `stsSeconds: 31536000` → Adds `max-age=31536000 → 31,536,000 seconds = 1 year`. Tells browsers to only use HTTPS for future requests for one year.
        - `stsIncludeSubdomains: true` → Adds `includeSubDomains`. Extends HTTPS enforcement to all subdomains.
        - `stsPreload: true` → Adds preload flag. Allows your domain to be included in Chrome’s HSTS preload list
        - `forceSTSHeader: true` → Forces Traefik to send the header even if the connection is not HTTPS (useful when Traefik terminates TLS).

```yaml
tls:
  options:
    default:
      minVersion: VersionTLS12
      maxVersion: VersionTLS13
      cipherSuites:
        - TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
        - TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
        - TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305
        - TLS_AES_256_GCM_SHA384
        - TLS_CHACHA20_POLY1305_SHA256
  certificates:
    - certFile: /traefik/certs/fullchain.pem
      keyFile: /traefik/certs/privkey.pem
```

- `tls`: → Top-level TLS configuration.
  - `options`: → Defines TLS policy sets that can be referenced by routers.
    - `default`: → The default TLS option used if no specific one is assigned.
      - `minVersion` → Enforces a minimum TLS protocol version (here: `TLS 1.2`).
      - `maxVersion` → Maximum TLS version allowed (`TLS 1.3`).
      - Together, this ensures only secure versions of TLS are used (no `TLS 1.0/1.1`).
      - `cipherSuites` → Specifies which cipher suites are allowed for `TLS 1.2` connections (`TLS 1.3` uses its own built-in list).
        - `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256` → Secure cipher using ECDHE (Perfect Forward Secrecy) + AES-128 + SHA256.
        - `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384` → AES-256 variant.
        - `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305` → Uses ChaCha20 for faster encryption on low-power devices.
        - `TLS_AES_256_GCM_SHA384`, `TLS_CHACHA20_POLY1305_SHA256` → Native TLS 1.3 ciphers.
        - Together, these are modern, strong ciphers ensuring robust encryption.
  - `certificates` → Defines the SSL certificate Traefik should use. List of certificate/key pairs.
    - `certFile`: → Path to the public certificate chain (fullchain.pem), including your certificate + intermediates.
    - `keyFile`: → Path to the private key corresponding to the certificate.
    - These files are typically mounted from your host or obtained from `Let’s Encrypt`.

## CLI Configuration (`docker-compose.yaml` file)

```yaml
- "--log.level=INFO"
- "--log.filepath=/traefik.log"
- "--log.format=json"
```

- Sets the Traefik **internal log level**. Valid levels: `DEBUG`, `INFO`, `WARN`, `ERROR`, `FATAL`, `PANIC`.
- Writes Traefik’s **internal logs** (not access logs) to `/traefik.log` inside the container. If omitted, logs go to `stdout`.
- Changes the log format from plain text to `JSON`. Useful for structured log aggregation (e.g., in `ELK`, `Loki`, or `Datadog`).

```yaml
- "--api=true"
- "--ping=true"
- "--accesslog=true"
- "--accesslog.bufferingsize=100"
- "--api.insecure=true"
```

- Enables the **Traefik API**. This API allows Traefik to expose info about its `routers`, `services`, `middlewares`, etc. (You can access it via `/api/http/routers`, `/api/http/services`, etc.)
- Enables a **health check endpoint** (`/ping`). Used to verify that Traefik is alive and responding — great for monitoring or readiness probes.
- Enables **access logs** — logs every HTTP request handled by Traefik. These logs are separate from the internal system logs (`--log.filepath`).
- Buffers access logs before writing to disk/output for performance. Here, Traefik stores up to `100` log lines in memory before flushing to disk.
- Enables the insecure Traefik dashboard on port `:8080` without authentication. This exposes a web UI at `http://<traefik_host>:8080/dashboard/`. (⚠️ Security warning: This should never be enabled in production without protection (e.g., `firewall`, `auth middleware`).)

```yaml
- "--providers.docker.endpoint=unix:///var/run/docker.sock"
- "--providers.docker.exposedbydefault=false"
- "--providers.docker.network=<network-name>"
```

- Tells Traefik where to find the **Docker API socket** to discover containers and their labels. `unix:///var/run/docker.sock` is the Unix socket where Docker listens by default.
- By default, Traefik routes to all Docker containers. Setting `exposedbydefault` to `false` means containers are not exposed unless explicitly labeled with: `- "traefik.enable=true"` (Best practice for security.)
- Defines which **Docker network** Traefik should use to connect to containers. All backend containers (services) that you want Traefik to route to must be attached to the same network.

```yaml
- "--entrypoints.http.address=:80"
- "--entrypoints.https.address=:443"
```

- Defines an entrypoint named **`http`** that listens on port `80 (HTTP)`. This is where unencrypted requests arrive.
- Defines an entrypoint named **`https`** that listens on port `443 (HTTPS)`. Used for encrypted traffic (TLS/SSL).

```yaml
- "--certificatesresolvers.mycert.acme.email=<email-address>"
- "--certificatesresolvers.mycert.acme.storage=/acme/acme.json"
- "--certificatesresolvers.mycert.acme.tlschallenge=true"
```

- Configures the **ACME (Let’s Encrypt)** account email. Let’s Encrypt uses this address for renewal notifications and registration.
- Tells Traefik where to **store issued certificates** and account info. File `/acme/acme.json` contains the certificates and keys (must be persisted via a Docker volume).
- Enables the **TLS-ALPN challenge** method for Let’s Encrypt. This means Traefik proves domain ownership by responding to a TLS challenge on port `443`

```yaml
- "--providers.file.filename=/traefik/config.yml"
```

- Tells Traefik to load **dynamic configuration** from `/traefik/config.yml`. This file can define middlewares, routers, services, or TLS options that update live (without restart).

### Volumes

| Mount                                          | Purpose                                                | Required?                                          | What happens if missing         |
| ---------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------- | ------------------------------- |
| `/etc/localtime:/etc/localtime:ro`             | Sync container timezone with host                      | ❌ Optional                                        | Logs use UTC time               |
| `/var/run/docker.sock:/var/run/docker.sock:ro` | Allow Traefik to discover Docker containers and labels | ✅ Required for Docker provider                    | No container-based routing      |
| `traefik-acme:/acme`                           | Persist Let’s Encrypt certs and keys                   | ✅ Required for ACME                               | HTTPS certs lost on restart     |
| `./traefik:/traefik`                           | Load config and manual certs from local folder         | ✅ Required if using file provider or manual certs | Config and cert files not found |

## Labels Configuration

```yaml
- "traefik.enable=true"
- "traefik.docker.network=<network-name>"
```

- Enables Traefik routing for this container.
- Tells Traefik which Docker network to use to communicate with this container. (Traefik must be connected to the same network to route traffic properly.)

```yaml
- "traefik.http.routers.<router-name>.entrypoints=http"
- "traefik.http.routers.<router-name>.rule=Host(`<host-route>`)"
```

- Defines the entrypoint this router listens on (router names must be unique to prevent clashing!) — here it’s `http` (port `80`). Entry points are defined in your Traefik service config (`--entrypoints.http.address=:80`).
- Defines the routing rule: This router matches requests with the **Host header**: `<host-route>`

```yaml
- "traefik.http.routers.<router-name>.middlewares=https-redirect"
- "traefik.http.middlewares.https-redirect.redirectscheme.scheme=https"
```

- Attaches the middleware called `https-redirect` to this router. This middleware will redirect HTTP traffic to HTTPS (we’ll define it below).
- Defines a middleware named `https-redirect` that performs a redirect from `HTTP` to `HTTPS`. It tells browsers: “If you came over port 80, go to the same URL but with HTTPS.”

```yaml
- "traefik.http.middlewares.web-auth.basicauth.users=user:$$apr1$$QpkypDvQ$$FjJgBGyX/By8agkOCUvDo."
```

- Defines a middleware named `web-auth` that enables **HTTP Basic Authentication**.
  - `user` is the username.
  - The long hash (`$$apr1$$...`) is an **Apache MD5-hashed** password.
  - The double `$` (`$$`) is necessary in Docker Compose to escape `$` from YAML interpolation.
  - You can generate your password, using:

```sh
echo $(htpasswd -nb user password) | sed -e s/\\$/\\$\\$/g
```

```yaml
- "traefik.http.routers.<router-name-secure>.middlewares=web-auth"
- "traefik.http.routers.<router-name-secure>.entrypoints=https"
- "traefik.http.routers.<router-name-secure>.rule=Host(`<host-route>`)"
- "traefik.http.routers.<router-name-secure>.tls=true"
- "traefik.http.routers.<router-name-secure>.tls.options=default"
- "traefik.http.routers.<router-name-secure>.tls.certresolver=mycert"
- "traefik.http.services.<service-name>.loadbalancer.server.port=<port>"
```

- Applies the previously defined middleware (`web-auth`) to this new router, enforcing Basic Auth for HTTPS access.
- Specifies the `https` entrypoint (port `443`).
- The routing rule for HTTPS requests — same host as the HTTP router.
- Enables TLS for this router, meaning Traefik will serve it over HTTPS.
- Specifies which TLS options to use — in this case, `default`, This configuration was defined in the `yaml` file for traefik.
- Tells Traefik to use the ACME certificate resolver named `mycert` (defined in Traefik CLI command flags) to automatically obtain and renew Let’s Encrypt certificates for this domain.
- Defines the internal port Traefik should connect to inside the container; so this tells Traefik where to send traffic once routing is matched.

```yaml
- "traefik.http.routers.<router-name>.service=<service-name>"
- "traefik.http.routers.<router-name-secure>.service=<service-name>"
```

- This tells Traefik that the HTTP router (listening on port 80) should forward its traffic to the defined service. Basically, before redirecting or upgrading, it associates this router with that backend definition. Even though this router is mainly used for HTTP (and will redirect to HTTPS via middleware), this explicit link ensures Traefik knows what service the router corresponds to.
- Defines that the HTTPS router also forwards traffic to the same backend service defined here. This is what will actually handle requests once the TLS handshake is done. It’s common to use the same service name for both routers (HTTP + HTTPS), but the HTTPS one is the one that truly matters since HTTP just redirects.
