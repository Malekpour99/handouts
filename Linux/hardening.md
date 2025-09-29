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
      - [Network Options](#network-options)
      - [Kernel Hardening](#kernel-hardening)
      - [Network Hardening (`IPv4`)](#network-hardening-ipv4)
      - [`IPv6` Disabling](#ipv6-disabling)

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

#### Network Options

```sh
net.ipv4.ip_nonlocal_bind = 1
```

- Allows binding sockets to non-local IP addresses. Useful for **load balancers**, **HA setups**.

```sh
net.bridge.bridge-nf-call-iptables = 1
net.bridge.bridge-nf-call-ip6tables = 1
```

- Ensures bridged traffic goes through iptables/ip6tables for filtering. Needed for **Kubernetes/containers networking**.

```sh
net.ipv4.ip_forward = 1
```

- Enables IP forwarding (router behavior). Required for **NAT**, **VPNs**, **Docker/Kubernetes**.

#### Kernel Hardening

```sh
fs.suid_dumpable = 0
```

- Prevents `setuid` programs from writing core dumps (avoids leaking sensitive data).
- A **`setuid program`** is an executable file with the `setuid` bit set (e.g., `/usr/bin/passwd`). When run, it executes with the file owner’s privileges instead of the user’s. Typically, this means running with **root privileges** even if a normal user launched it.
- A **`core dump`** is a file the kernel writes when a process crashes. It contains the process’s memory (`variables`, `stack`, `heap`, etc.) at the time of the crash — useful for debugging, but potentially very sensitive.

```sh
kernel.core_uses_pid = 1
```

- Appends `PID` to core dump filenames (avoids overwriting).

```sh
kernel.dmesg_restrict = 1
```

- Restricts access to kernel logs (`dmesg`) to **root** only. Prevents info leaks.

```sh
kernel.kptr_restrict = 2
```

- Restricts exposure of kernel addresses in `/proc` and logs. Mitigates kernel exploit attacks.

```sh
kernel.sysrq = 0
```

- Disables `SysRq key combos` (used for debugging/crash dumps). Prevents abuse.
- The **`SysRq` (System Request) key** is a special key combo built into the Linux kernel. It lets you send **low-level commands** directly to the kernel using: `Alt + SysRq + <command key>`
  - `Alt+SysRq+S` → sync disks (flush all data to disk)
  - `Alt+SysRq+U` → remount all filesystems read-only
  - `Alt+SysRq+B` → immediately reboot the machine (bypassing normal shutdown!)
  - `Alt+SysRq+K` → kill all processes on the current console

```sh
kernel.yama.ptrace_scope=1
```

- Restricts `ptrace` debugging: _only a process’s children_ can be traced. Prevents privilege escalation via `ptrace`.
- `ptrace` is a Linux system call that lets one process **observe and control another process**.
- By default (_historically_), any process owned by the same user could `ptrace` another.
  - This means: if you have two processes running under the same user, one can inject code into the other.
  - If the target process has higher privileges (e.g., `setuid` binary that temporarily runs as root), this could lead to **privilege escalation**.

#### Network Hardening (`IPv4`)

```sh
net.ipv4.conf.all.forwarding = 1
```

- Same as `ip_forward`, enables forwarding globally.

```sh
net.ipv4.conf.all.send_redirects = 0
```

- Prevents sending `ICMP` redirects (protects from **routing manipulation**). This prevents your host from accidentally or maliciously influencing the routing decisions of other devices on the network.

```sh
net.ipv4.conf.default.accept_redirects = 0
net.ipv4.conf.default.accept_source_route = 0
```

- Disables **IP redirects** and **source routing** by default. Hardens networking.

```sh
net.ipv4.conf.all.log_martians = 1
net.ipv4.conf.default.log_martians = 1
net.ipv4.conf.all.accept_redirects = 0
```

- Logs suspicious/malicious `IPv4` packets (**"martians"** = bad source/dest addresses).
- Disables `IPv4` packets redirects globally.

```sh
net.ipv4.conf.all.rp_filter=1
```

- Enables **reverse path filtering**. Drops packets with spoofed (fake) source addresses.
- **Reverse Path Filtering (RPF)** checks whether the source address of a received packet is reachable via the interface it came in on. If not → the packet is likely spoofed → **drop it**.

#### `IPv6` Disabling

```sh
net.ipv6.conf.all.accept_redirects = 0
net.ipv6.conf.default.accept_redirects = 0
```

- Disables `ICMPv6` redirect acceptance. Prevents **MITM (Man-in-the-Middle) attacks & routing-based attacks**.
- **`ICMPv6` (Internet Control Message Protocol for IPv6)** is used by routers and hosts to exchange control messages. One feature is the **Redirect message**: You connect to a router → the router notices a shorter path → it sends you an ICMPv6 Redirect so your host updates its routing table.
- Without this configuration, a malicious host can send **fake redirect messages**, tricking your machine into:
  - Sending traffic through the attacker (Man-in-the-Middle attack)
  - Dropping traffic (Denial of Service)

```sh
# Disable Ipv6
net.ipv6.conf.all.disable_ipv6=1
net.ipv6.conf.default.disable_ipv6=1
net.ipv6.conf.lo.disable_ipv6=1
```

- Completely disables `IPv6` support (all interfaces including loopback). Useful if not needed (reduces attack surface).
