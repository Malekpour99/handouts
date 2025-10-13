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
    - [Resource Limit Configuration](#resource-limit-configuration)
    - [Kernel Module Loading](#kernel-module-loading)
    - [Reducing Unused Services](#reducing-unused-services)
    - [Defining a Custom Banner](#defining-a-custom-banner)
    - [SSH Configuration](#ssh-configuration)
      - [Basic](#basic)
      - [Logging](#logging)
      - [Authentication / Login](#authentication--login)
      - [Forwarding / Tunneling](#forwarding--tunneling)
      - [Session / Terminal behavior](#session--terminal-behavior)
      - [Banner / Environment](#banner--environment)
      - [Access Restrictions](#access-restrictions)
    - [fail2ban Configuration](#fail2ban-configuration)
    - [iptables configuration](#iptables-configuration)
      - [iptables](#iptables)

## Core Concepts

- SSH configuration path: `/etc/ssh/sshd_config`
- SSH Authorized Keys Configuration path: `/home/<user>/.ssh/authorized_keys` or `/root/.ssh.authorized_keys` (for root user)

  - Add public keys to the end of `authorized_keys` file to provide access to server for users by SSH keys!

```sh
# Adding Public Key to authorized_key for PubKeyAuthentication
cat <<EOT >> /root/.ssh/authorized_keys
<user's name>
<ssh-rsa USER_SSH_PUBLIC_KEY>
EOT
```

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

### Resource Limit Configuration

```sh
echo "root soft nofile 65535" >  /etc/security/limits.conf
echo "root hard nofile 65535" >> /etc/security/limits.conf
```

- `nofile` -> maximum number of **open file descriptors** (files, sockets) a process can hold.
- **soft** -> default limit when a session starts (can be increased up to the hard limit).
- **hard** -> absolute max limit, cannot be exceeded.
- **Root** is allowed up to 65,535 open files/sockets, which is very high (useful for DBs, proxies, web servers).
- `65535` -> It’s the **maximum value often allowed by the kernel** for file descriptors and processes per user in older Linux kernels.

```sh
echo "root soft nproc 65535" >> /etc/security/limits.conf
echo "root hard nproc 65535" >> /etc/security/limits.conf
```

- `nproc` = maximum number of **processes/threads** a user can create.
- **Root** can create up to 65,535 processes, preventing process exhaustion limits from breaking critical services.

```sh
echo "* soft nofile 2048" >  /etc/security/limits.conf
echo "* hard nofile 2048" >> /etc/security/limits.conf
```

- For **all users**, limits the **number of open files** to 2,048.
- Prevents normal users from hogging file descriptors and causing DoS.

```sh
echo "* soft nproc  2048" >> /etc/security/limits.conf
echo "* hard nproc  2048" >> /etc/security/limits.conf
```

- For **all users**, limits the **number of processes** to 2,048.
- Prevents fork-bomb attacks or accidental resource exhaustion.

### Kernel Module Loading

```sh
modprobe br_netfilter
```

- Loads the `br_netfilter` kernel module.
- This makes bridged traffic visible to `iptables`/`netfilter`, which is critical for **Kubernetes**, **Docker**, and **virtual networking**.
- Without it, firewall rules might not apply to packets forwarded across bridges.

### Reducing Unused Services

- `systemctl stop <service>` -> Immediately stops the service if it is running.
- `systemctl disable <service>` -> Prevents the service from starting automatically at boot.
- `systemctl mask <service>` -> Completely prevents the service from being started manually or automatically, even if another service tries to start it. (Essentially links the service unit to `/dev/null`.)

- **`postfix`**

  - Postfix is a mail server.
  - Disabling it is common on servers that don’t need to send or receive mail (reduces attack surface).

- **`firewalld`**

  - Dynamic firewall daemon used on RHEL/CentOS systems.
  - Disabled if you plan to use another firewall (like iptables rules directly) or don’t want the daemon managing rules.

- **`ufw`**

  - Uncomplicated Firewall, common on Ubuntu/Debian.
  - Disabled for the same reason as `firewalld`.

### Defining a Custom Banner

- `/etc/issue.net` -> On most Linux systems, `/etc/issue.net` is **displayed by SSH before login** (if Banner `/etc/issue.net` is set in `/etc/ssh/sshd_config`).

### SSH Configuration

- Configuration file -> `/etc/ssh/sshd_config`
- Test Configuration -> `sshd -t`

#### Basic

- `Port $SSH_PORT` -> Sets the TCP port sshd listens on. (default `22`)
- `ListenAddress 0.0.0.0` -> Bind sshd to all IPv4 network interfaces.

#### Logging

- `LogLevel VERBOSE` -> Increase logging detail for SSH events (useful for auditing and troubleshooting, Produces more log output than the default)

#### Authentication / Login

- `PermitRootLogin yes` -> Allows the root account to log in directly over SSH. (Security risk) — often _disabled_ in hardened systems!
- `MaxAuthTries 3` -> **Maximum number of authentication** attempts per connection before the server disconnects the client. Limits brute-force attempts.
- `MaxSessions 2` -> **Maximum open sessions** permitted per network connection (useful to limit resource usage and abuse).
- `PasswordAuthentication yes` -> Allow password-based authentication. (Security risk) — **public-key auth** is stronger and preferred!
- `ChallengeResponseAuthentication no` -> Disables challenge/response auth (e.g., some OTP PAM modules). If you rely on PAM-based 2FA, this may need to be yes.
- `GSSAPIAuthentication no` -> Disable **GSSAPI (Generic Security Services Application Program Interface - Kerberos)** authentication mechanisms. Good to disable if unused.
- `UsePAM yes` -> Enables **Pluggable Authentication Modules (PAM)**. Allows use of system auth stacks (account, password, session modules).

#### Forwarding / Tunneling

- `AllowAgentForwarding no` -> Disables SSH agent forwarding (prevents leaking agent credentials to remote hosts).
- `AllowTcpForwarding no` -> Disables port forwarding over SSH (prevents tunnel abuse).
- `X11Forwarding no` -> Disables X11 forwarding (reduces attack surface if graphical forwarding is not needed).

#### Session / Terminal behavior

- `PrintMotd no` -> Do not print `/etc/motd` upon SSH login (avoids duplicate messages if PAM prints it).
- `TCPKeepAlive no` -> Disable low-level TCP keepalives. (You rely on higher-level keepalives instead — see `ClientAlive\*` below.)
- `ClientAliveInterval 10` -> Server sends a **keepalive (null packet)** to the client every `10` seconds to check the connection.
- `ClientAliveCountMax 10` -> If the server sends `ClientAliveInterval` probes and receives no response `ClientAliveCountMax` times, it disconnects the session. With these values the server will drop an unresponsive client after `~100 seconds (10 × 10s)`.
- `UseDNS no` -> Don’t perform DNS lookups on client IPs for reverse lookup before authentication (speeds up logins and prevents DNS-based delays/attacks).

#### Banner / Environment

`Banner /etc/issue.net` -> Display the pre-login banner from `/etc/issue.net` to connecting clients before authentication.

`AcceptEnv LANG LC_*` -> Allow the client to **pass locale environment variables** (useful if you want remote processes to inherit locale). Can be restricted for security!

#### Access Restrictions

`AllowUsers root` -> Only the root user is allowed to login via SSH. This overrides more permissive access; if root is allowed this effectively restricts SSH to the root account only.

`AllowGroups root` -> Only users in the root group may authenticate. Combined with AllowUsers root this is highly restrictive.

<!-- todo: add documentation for commented commands -->

### fail2ban Configuration

```sh
cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
```

- Copies the default `jail.conf` to `jail.local`; since `jail.local` is the recommended place to put overrides so package upgrades don’t overwrite your custom settings.

```sh
# ssh config
sed -i '/^\[sshd\]/a enabled = true' /etc/fail2ban/jail.local

# tries to replace an existing enabled line or insert it if missing
sed -i '/^\[sshd\]/{:a;n;/^enabled[[:space:]]*=/!{i enabled = true; b}; s/^enabled[[:space:]]*=.*/enabled = true/}' /etc/fail2ban/jail.local
```

- Finds the line that starts a `[sshd]` jail section and inserts a new line `enabled = true` immediately after it.
- Effect: enables the SSH jail so fail2ban will monitor SSH auth attempts.

```sh
sed -i 's/port    = ssh/port    = '$SSH_PORT'/g' /etc/fail2ban/jail.local
sed -i 's/port     = ssh/port    = '$SSH_PORT'/g' /etc/fail2ban/jail.local

sed -i -E "s/^[[:space:]]*port[[:space:]]*=[[:space:]]*ssh/port    = $SSH_PORT/" /etc/fail2ban/jail.local
# try to catch spacing variants
```

### iptables configuration

```sh
DEBIAN_FRONTEND=noninteractive apt install -y iptables-persistent
```

- Installs `iptables-persistent`, which automatically **saves and restores firewall rules** across reboots.
- The `DEBIAN_FRONTEND=noninteractive` flag avoids interactive prompts during install.

#### iptables

- iptables rules can be divided into tables (like `filter`, `mangle`, `nat`, etc.).
- Each table contains chains (like `INPUT`, `OUTPUT`, `FORWARD`, etc.).
- Each chain has rules that decide what to do with packets.

```sh
*mangle
:PREROUTING ACCEPT [0:0]
:INPUT ACCEPT [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
:POSTROUTING ACCEPT [0:0]
```

- `*mangle` — starts the mangle table section.
- The `:` lines define chains and set their default policy to `ACCEPT`. (Meaning: if no rule matches, the packet passes through.)
- These chains correspond to different stages in packet traversal:

  - `PREROUTING` – before routing decisions (first stop for incoming packets)
  - `INPUT` – packets destined for this host
  - `FORWARD` – packets being routed through this host
  - `OUTPUT` – packets created locally
  - `POSTROUTING` – after routing decisions

```sh
# Drop packets with no TCP flags set (null scans).
-A PREROUTING -p tcp -m tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG NONE -j DROP

# Drop packets with both FIN and SYN set — invalid in normal TCP usage.
-A PREROUTING -p tcp -m tcp --tcp-flags FIN,SYN FIN,SYN -j DROP

# Drop packets with SYN and RST set — also invalid.
-A PREROUTING -p tcp -m tcp --tcp-flags SYN,RST SYN,RST -j DROP

# Drop packets that only have the FIN flag set with ACK present — often used in stealth scans.
-A PREROUTING -p tcp -m tcp --tcp-flags FIN,ACK FIN -j DROP

# Drop packets with only PSH flag — suspicious or malformed.
-A PREROUTING -p tcp -m tcp --tcp-flags PSH,ACK PSH -j DROP

# ...

# Saves and finalizes the mangle table rules.
COMMIT
```

- All of the above lines start with `-A PREROUTING`, meaning they append a rule to the `PREROUTING` chain in the mangle table.
- The others are variations of invalid `TCP` flag combinations (`FIN+URG`, `FIN+PSH+URG`, etc.)
  Essentially, all of these lines **protect your host from TCP flag abuse, stealth scans, and malformed packets**.
- They **drop malformed TCP packets**, which are often used in **scans or DoS attacks**.
- Each uses `--tcp-flags` to match suspicious flag combinations.

```sh
*filter
:INPUT ACCEPT [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
:CHECK_INPUT - [0:0]
:CHECK_OUTPUT - [0:0]
```

- Starts the `filter` table.
- Sets default policy for `INPUT`, `FORWARD`, and `OUTPUT` to `ACCEPT`.
- Defines two custom chains: `CHECK_INPUT` and `CHECK_OUTPUT`.

```sh
-A INPUT -j CHECK_INPUT
-A INPUT -j DROP

-A OUTPUT -j CHECK_OUTPUT
-A OUTPUT -j DROP
```

- Send all incoming packets to the `CHECK_INPUT` chain.
- If they don’t match any rule in `CHECK_INPUT`, drop them.
- Same logic for outgoing packets: only packets matching `CHECK_OUTPUT` rules are allowed.

```sh
# CHECK_INPUT RULES ----------------------------------------------

# Allow responses to already established connections (e.g., replies from websites you contacted).
-A CHECK_INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

# Allow traffic on the loopback interface (localhost).
-A CHECK_INPUT -i lo -j ACCEPT

# Allow all traffic from Docker containers (bridge network).
-A CHECK_INPUT -i docker0 -j ACCEPT

# Allow SSH connections to your server.
-A CHECK_INPUT -p tcp -m tcp --dport $SSH_PORT -j ACCEPT

# Allow HTTPS and HTTP traffic.
-A CHECK_INPUT -p tcp -m tcp --dport 443 -j ACCEPT
-A CHECK_INPUT -p tcp -m tcp --dport 80 -j ACCEPT

# Allow private local network ranges.
-A CHECK_INPUT -s 192.168.0.0/16 -j ACCEPT
-A CHECK_INPUT -s 172.17.0.0/16 -j ACCEPT

# Allow traffic from the domain/IP DockerMe.ir. (In actual rules, iptables will resolve that domain to an IP address.)
-A CHECK_INPUT -s DockerMe.ir -j ACCEPT -m comment --comment "The DockerMe Server Ip is Trusted"

# CHECK_OUTPUT RULES ----------------------------------------------

# Allow responses to existing outgoing connections.
-A CHECK_OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

# Allow all other outbound traffic.
-A CHECK_OUTPUT -j ACCEPT

# Finalizes the filter table rules.
COMMIT
```

```sh
iptables -nL
```

- Lists the currently active firewall rules.
- The `-n` flag prevents DNS lookups (for faster output and fewer external lookups).
- The second listing helps confirm that `fail2ban` successfully re-added its jail rules to the firewall.
