# Docker

## Table of Contents

- [Docker](#docker)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Introduction](#introduction)
  - [DockerFile](#dockerfile)
  - [Images](#images)
  - [Containers](#containers)
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

# login to docker-hub
docker login

# logout from docker-hub
docker logout
```

## Introduction

![docker build - ship - run](<./images/Docker(build-ship-run).jpg>)

![docker containers and images](<./images/Docker(containers-images).webp>)

- **Entrypoint**: all containers have an entrypoint which run every time a container is started and applies the work-load. you can inspect container's entrypoint from the provided path by `.Config.Entrypoint`.

for handling containers, both their **name** and **ID** can be used!

## DockerFile

- `FROM`: **Sets the base image (scratch)** for subsequent instructions

- `LABEL`: Adds **metadata** to the image as key-value pairs (e.g. maintainer, version, etc.).
- `ENV`: Sets **environment variables**. These persist in subsequent layers and inside the running container.
- `ARG`: Defines a **build-time variable**. These are not available at runtime (use `ENV` for that).

---

- `WORKDIR`: Sets the **working directory** for the container (for RUN, CMD, ENTRYPOINT, etc.). Like `cd` in bash.
- `ADD`: Copies files/directories from source to the container. Supports **remote URLs and auto-extracting tar files**.
- `COPY`: Copies files/directories from the build context into the container. Like `ADD`, but simpler and more predictable.
- `RUN`: **Executes a command** in a new layer on top of the current image and commits the result. Used to install packages, etc.
- `EXPOSE`: **Documents the port(s)** the container will listen on at runtime. It does not actually publish them.
- `USER`: Specifies the **user** (UID/GID) to use when running the image.
- `CMD`: **Provides default arguments** for the container (overridden by `docker run` arguments). Only one CMD allowed (use shell or exec form).
- `ENTRYPOINT`: Configures a **container to run as an executable**. Can be used with `CMD` to pass default arguments.

---

- `VOLUME`: Creates a mount point and marks it as a **volume** to persist data or share between containers.
- `ONBUILD`: Adds a trigger instruction that is **executed when the image is used as a base** for another image.
- `STOPSIGNAL`: Sets the system call signal sent to the container to **gracefully stop** it (e.g., `SIGTERM`).
- `HEALTHCHECK`: a **command to check container health**. Docker uses it to determine if the container is healthy.
- `SHELL`: Allows changing the default shell used for `RUN` commands (default is `["/bin/sh", "-c"]` on Linux).

**Best Practices**:

- Use official images or minimal base images (Prefer _language-specific_ base images)
- Use multi-stage builds (reduce image size by separating build and runtime environments)
- Document exposed ports and metadata (e.g. maintainer, version, etc.)
- Set WORKDIR instead of cd (use WORKDIR to define working directory; it’s clearer and Docker-layer aware)
- Install only what's necessary and combine RUN commands to reduce layers
- Clean up temporary files (remove caches and temp files after installing packages)
- Use non-root user (improves security by preventing privilege escalation in case of a container exploit)
- Minimize COPY scope using docker ignore (only copy what’s needed, use `.dockerignore` to skip unnecessary files e.g. node_modules, .git, etc.)
- Use ENTRYPOINT + CMD properly (ENTRYPOINT defines the fixed command; CMD defines default args -can be overridden-)
- Add HEALTHCHECK (helps detect if the app inside the container is working correctly)

## Images

```sh
# list images
docker image ls

# download an image from registry
docker pull <image>:<version>
# if version tag is not mentioned 'latest' will be considered!

# tag an image which refers to the source image
docker tag <source-image>:<version> [registry]/<new-name>:<new-version>
# you can mention your docker-hub's account as registry if you want to push images there!

# upload an image to a registry
docker push [registry]/<image>:<version>

# list image history for its layers
docker history <image>

# removing image(s)
docker rmi <image(s)>
docker image rm <image(s)>

# save image to a tar archive (streamed to STDOUT by default)
docker save -o <file> <image>
# `-o`: output
# then you can use FTP to more your file $ ftp <file> ...

# Load an image from a tar archive or STDIN
docker load -i <file>

# building a custom image from DockerFile
docker build -t <image-name>:<version> -f <DockerFile>
# only use small-letters for image name
# by default docker looks for 'DockerFile' if file is not mentioned (pass . to specify current directory)
```

## Containers

```sh
# create container
docker run --name <container-name> -p <system-port>:<container-port> <image>:<image-version>
# `--name`: dedicate a name to container (when not provided a random name will be dedicated to container)
# `-p` `--publish`: publish container's port(s) to the host
# `-d` `--detach`: run container in background (print container ID as response)
# `-e`: setting environment variables for running container
# `--rm`: remove container after exiting
# `--restart=<condition>:<max-retry>`: restart container on the mentioned 'condition' and retry for 'max-retry' times

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

# kill container(s) forcefully
kill -9 <container-PIDs>
# failure exit code will be shown in container's exit status

# kill container(s)
docker kill <container(s)>
# If used, docker believes you know what you are doing and failure exit code (137) is not mentioned in container's exit status (0 is shown)

# remove stopped containers
docker container prune

# copy files/folders between a container and the local filesystem
docker cp <source-path> <container>:<container-path> # copy from local to container
docker cp <container>:<container-path> <source-path> # copy from container to local
```

## Inspecting

```sh
# fetch logs of a container
docker logs <container>
# `-f`: follow log output
# `-n <n>` `--tail <n>`: number of logs to show from the end of logs (default: all)

# display a live stream of container(s) resource usage statistics
docker stats <container>
# `--no-stream`: display a snapshot of resource usage instead of live stream

# list port mappings or a specific mapping for the container
docker port <container>

# Display container's running processes
docker top <container>

# Return low-level information on Docker objects
docker inspect <container/image/volume/network>
```

---

## Examples

```sh
# inspecting containers config related details
docker inspect -f '{{.Config}}' <container>
# using format string (-f) instead of grep since it works better on JSON objects!
# {{.Config.Env}} -> environment variables
# {{.Config.ExposedPorts}} -> exposed ports
# {{.NetworkSettings.Networks.bridge.IPAddress}} -> Running container's IP address

# inspecting all the containers' names and IP addresses
docker inspect -f '{{.Name}} ---> {{.NetworkSettings.Networks.bridge.IPAddress}}' $(docker container ls -aq)

# creating an ubuntu container which gets removed after exiting
docker run -exec -it --rm ubuntu /bin/bash
# if /bin/bash is not executed, ubuntu exits immediately after running since it doesn't have an entrypoint

# running a MySQL database
docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:8.0.21
# By using 'MYSQL_RANDOM_ROOT_PASSWORD' as environment variable, a random password is generated for root user;
# which can be found in the container logs (look for GENERATED ROOT PASSWORD)
```
