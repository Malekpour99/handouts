# Hardening

## Table of Contents

- [Hardening](#hardening)
  - [Table of Contents](#table-of-contents)
  - [Core Concepts](#core-concepts)
  - [Hardening Commands \& Actions](#hardening-commands--actions)
    - [Removing snapd](#removing-snapd)
    - [Installing Useful Tools](#installing-useful-tools)
    - [Timeout Configuration](#timeout-configuration)
    - [Systemctl Configuration](#systemctl-configuration)
      - [TCP/Networking Performance](#tcpnetworking-performance)
      - [File Descriptors \& Memory Maps](#file-descriptors--memory-maps)

## Core Concepts

- SSH configuration path: `/etc/ssh/sshd_config`
- SSH Authorized Keys Configuration path: `/home/<user>/.ssh/authorized_keys` or `/root/.ssh.authorized_keys` (for root user)

  - Add public keys to the end of `authorized_keys` file to provide access to server for users by SSH keys!

- Finding all the available bash on system:`which -a bash`

```text
/usr/bin/bash
/bin/bash   -> default bash on must systems
```

## Hardening Commands & Actions

### Removing snapd

`snapd` is the **background service (daemon)** that runs on Linux systems to support Snaps, which are Canonical’s (Ubuntu’s) package format for distributing software.

removing snapd helps:

- **Reduces attack surface** → one less daemon and one less socket listening.
- **Eliminates uncontrolled software sources** → all packages must then come from your distribution’s package manager (e.g., `apt`, `yum`, etc.), where you can mirror or restrict repositories.
- **Prevents unexpected updates** → you regain full control of when and how updates happen.
- **Simplifies system footprint** → fewer processes, fewer binaries to patch or monitor.

### Installing Useful Tools

- `wget` → Command-line tool to download files from the web (HTTP, HTTPS, FTP).
- `git` → Version control system for managing source code and configurations.
- `vim` → Powerful text editor, often used for editing configs or code.
- `nano` → Simple, user-friendly text editor for quick edits.
- `bash`-completion → Provides tab-completion for commands, options, and paths in Bash.
- `curl` → Transfers data from/to URLs, useful for APIs, testing endpoints.
- `htop` → Interactive process viewer (like `top`, but more user-friendly).
- `iftop` → Real-time display of network bandwidth usage by connection.
- `jq` → Command-line JSON processor (filter, transform, parse JSON).
- `ncdu` → Disk usage analyzer, shows space consumption interactively.
- `unzip` → Extracts `.zip` archives.
- `net-tools` → Legacy networking tools (`ifconfig`, `netstat`, etc.).
- `dnsutils` → DNS query tools (`dig`, `nslookup`) for troubleshooting DNS.
- `atop` → Advanced system and process monitor (CPU, memory, disk, network).
- `sudo` → Allows running commands with elevated (root) privileges.
- `ntp` → Synchronizes system time with network time servers.
- `fail2ban` → Intrusion prevention: bans IPs with repeated failed logins.
- `software`-properties-common → Adds `add-apt-repository` and related tools for managing PPAs (Personal Package Archives)/repos.
- `apache2`-utils → Contains `htpasswd`, `ab` (ApacheBench) for benchmarking and auth.
- `tcpdump` → Captures and analyzes network packets.
- `telnet` → Simple TCP client, useful for debugging connectivity.
- `axel` → Lightweight download accelerator (multi-threaded downloader).

### Timeout Configuration

Below configuration overwrites or creates `/etc/profile.d/timout-settings.sh`:

```sh
#!/bin/bash
### 300 seconds == 5 minutes ##
TMOUT=300
readonly TMOUT
export TMOUT
```

- `TMOUT=300` → sets the shell timeout to **300 seconds (5 minutes)**.
- `readonly TMOUT` → makes the variable **immutable** so users cannot change it.
- `export TMOUT` → makes the variable available to all _sub-shells_.

This means: if a user is idle in the shell for more than 5 minutes, they are automatically logged out.

### Systemctl Configuration

#### TCP/Networking Performance

```sh
# Decrease TIME_WAIT seconds
net.ipv4.tcp_fin_timeout = 30
```

- Reduces the time (`default ~60s`) a socket stays in **FIN-WAIT-2** after closing. Helps free sockets faster.
- In Linux, **FIN_WAIT_2** isn't a state with a mandatory timeout; instead, it's **the `TCP` state where a local socket waits for the remote end to close a connection**, which typically occurs after the application initiating the close has already sent its FIN. The system's `tcp_fin_timeout` applies to **"orphaned"** sockets, meaning connections no longer associated with an active process.

```sh
# Recycle and Reuse TIME_WAIT sockets faster
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_tw_reuse = 1
```

- `tcp_tw_reuse` → allows reuse of TIME_WAIT sockets for new connections (safe-ish).
- `tcp_tw_recycle` → enables fast recycling of TIME_WAIT sockets (⚠️ deprecated/unsafe if `NAT` or `load balancers` are used; can break clients - the "problems when using load balancers" is about `public-facing servers`. With recycle is enabled, the server cant distinguish new incoming connections from different clients behind the same NAT device).

```sh
# Decrease ESTABLISHED seconds
net.netfilter.nf_conntrack_tcp_timeout_established=3600
```

- Reduces timeout for **established TCP connections** in the connection tracking table (default often `5` days). Helps **save memory** in busy servers/firewalls.

#### File Descriptors & Memory Maps

```sh
# Maximum Number Of Open Files
fs.file-max = 500000
```

- Increases the maximum number of open file descriptors system-wide (default is usually much lower). Useful for **high-load** servers.
- A **file descriptor** is an **integer** that **uniquely identifies an `open file`, `socket`, or other `I/O resource` within a process**. It abstracts the underlying file system, providing a consistent interface for reading from and writing to resources.

```sh
vm.max_map_count=262144
```

- Sets the maximum number of memory map areas a process can have. Required by apps like `Elasticsearch`.
