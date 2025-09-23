# Hardening

## Table of Contents

- [Hardening](#hardening)
  - [Table of Contents](#table-of-contents)
  - [Core Concepts](#core-concepts)

## Core Concepts

- SSH configuration path: `/etc/ssh/sshd_config`
- SSH Authorized Keys Configuration path: `/home/<user>/.ssh/authorized_keys` or `/root/.ssh.authorized_keys` (for root user)

- Finding all the available bash on system:`which -a bash`

```text
/usr/bin/bash
/bin/bash   -> default bash on must systems
```
