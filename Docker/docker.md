# Docker

## Table of Contents

- [Docker](#docker)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Containers](#containers)
      - [Docker Images \& Containers](#docker-images--containers)
      - [Managing Containers](#managing-containers)
      - [Inspecting](#inspecting)
    - [Examples](#examples)

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

#### Managing Containers

```sh
# create container
docker run --name <container-name> -p <system-port>:<container-port> <image>:<image-version>
# `--name`: dedicate a name to container (when not provided a random name will be dedicated to container)
# `-p` or `--publish`: publish container's port(s) to the host
# `-d` or `--detach`: run container in background (print container ID as response)
# `-e`: setting environment variables for running container

# list Up containers
docker ps
# `-l`: show latest created container with up status
# `-a`: show all container including both up and down (exited) containers
# `-q`: only returning containers' ID

# starting an interactive bash shell inside running container
docker exec -it <container> bash
# `-i` (interactive): Keeps STDIN open, so you can type input
# `-t` (TTY): Allocates a pseudo-terminal, so the output looks like a normal terminal session

# start container(s)
docker start <container(s)>

# stop container(s)
docker stop <container(s)>

# restart container(s)
docker restart <container(s)>

# rename container
docker rename <container> <new-name>

# remove container(s)
docker rm <container(s)>
# `-f` or `--force`: force the removal of a running container (uses SIGKILL)

# remove stopped containers
docker container prune
```

---

#### Inspecting

```sh
# fetch logs of a container
docker logs <container>
# `-f`: follow log output
# `-n <n>` or`--tail <n>`: number of logs to show from the end of logs (default: all)

# display a live stream of container(s) resource usage statistics
docker stats <container>

# list port mappings or a specific mapping for the container
docker port <container>

# Display container's running processes
docker top <container>

# Return low-level information on Docker objects
docker inspect <container/image/volume/network>
```

---

### Examples

```sh
# inspecting containers config related details
docker inspect -f '{{.Config}}' <container>
# using format string (-f) instead of grep since it works better on JSON objects!

# running a MySQL database
docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:8.0.21
# By using 'MYSQL_RANDOM_ROOT_PASSWORD' as environment variable, a random password is generated for root user;
# which can be found in the container logs (look for GENERATED ROOT PASSWORD)
```
