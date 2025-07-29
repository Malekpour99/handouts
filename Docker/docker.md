# Docker


## Table of Contents

- [Docker](#docker)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Containers](#containers)
      - [Docker Images \& Containers](#docker-images--containers)
      - [Creating](#creating)
      - [Listing](#listing)
      - [Removing](#removing)
      - [Stopping](#stopping)
      - [Starting](#starting)
      - [Logs](#logs)
      - [Renaming](#renaming)
      - [Port Mapping](#port-mapping)
      - [Inspecting](#inspecting)

## Installation

Official docker installation process: [docker-installation](https://docs.docker.com/engine/install/)

In order to manage docker as a non-root user; follow the post installation process: [docker-post-installation](https://docs.docker.com/engine/install/linux-postinstall/)

```sh
# check docker status
systemctl status docker

# start docker
systemctl start docker

# keep docker active after reboot
systemctl enable docker

# docker client & server version
docker version
# It's recommended to have same version for both client & server!

# Detailed docker service information
docker info

# docker commands help
docker --help

# simple hello-word app for checking docker installation and health
docker container run hello-world
```

---

### Containers

#### Docker Images & Containers

![docker containers and images](./images/docker%20containers%20and%20images.webp)

for handling containers, both their **name** and **ID** can be used!

---

#### Creating

```sh
docker run --name <container-name> -p <system-port>:<container-port> <image>:<image-version>
```

flags:
- `--name`: dedicate a name to container (when not provided a random name will be dedicated to container)
- `-p` or `--publish`: publish container's port(s) to the host
- `-d` or `--detach`: run container in background (print container ID as response)

---

#### Listing

```sh
# display the running processes of a container
docker top <container>

# list Up containers
docker ps
```

flags:
- `-l`: show latest created container with up status
- `-a`: show all container including both up and down (exited) containers

---

#### Removing

```sh
docker rm <container(s)>
```

flags:
- `-f` or `--force`: force the removal of a running container (uses SIGKILL)

---

#### Stopping

```sh
docker stop <container(s)>
```

---

#### Starting

```sh
docker start <container(s)>
```

---

#### Logs

```sh
# fetch logs of a container
docker logs <container>
```

flags:
- `-f`: follow log output
- `-n <n>` or`--tail <n>`: number of logs to show from the end of logs (default: all)


#### Renaming

```sh
docker rename <container> <new-name>
```

#### Port Mapping

```sh
# list port mappings or a specific mapping for the container
docker port <container>
```

#### Inspecting

```sh
# Return low-level information on Docker objects
docker inspect <container/image/volume/network>
```
