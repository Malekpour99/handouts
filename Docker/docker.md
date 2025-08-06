# Docker

## Table of Contents

- [Docker](#docker)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Introduction](#introduction)
  - [Network](#network)
  - [Volume-Mount \& Bind-Mount](#volume-mount--bind-mount)
  - [DockerFile](#dockerfile)
  - [Images](#images)
  - [Containers](#containers)
  - [Inspecting](#inspecting)
  - [Examples](#examples)
  - [Docker Compose](#docker-compose)
  - [Docker Swarm](#docker-swarm)
    - [Nodes (servers)](#nodes-servers)
      - [Manager Nodes (Master)](#manager-nodes-master)
      - [Worker Nodes (Slave)](#worker-nodes-slave)
    - [Setup Docker Swarm](#setup-docker-swarm)
      - [Swarm Cluster Network Configuration](#swarm-cluster-network-configuration)
      - [Routing Mesh](#routing-mesh)
    - [Commands](#commands)
      - [Nodes](#nodes)
      - [Services](#services)
    - [Rolling Update](#rolling-update)
      - [Configuration \& Commands](#configuration--commands)
    - [Stack Deploy](#stack-deploy)

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

## Network

**Default Networks and drivers**
| Network Name | Driver | Description |
| ------------ | -------- | -------------------------------------------------------------------------------------------------------------------- |
| `bridge` | `bridge` | The default network for containers on a single host if none is specified. Suitable for container-to-container communication on the same host. |
| `host` | `host` | Shares the host’s network stack directly. Container uses the host’s IP address and ports. Only available on Linux. |
| `none` | `null` | Disables networking entirely. The container has no network access. Useful for security or testing. |

- Networks are isolated in docker.
- Container's IP address is not static, so it's better to use it's name or define an alias for it, when you need communication in the same network.

```sh
# list networks
docker network ls

# remove unused networks
docker network prune

# create a new network
docker network create <name>

# add container to network
docker network connect <network> <container>

# remove container from network
docker network disconnect <network> <container>
```

## Volume-Mount & Bind-Mount

| Volume                           | Bind-Mount                          |
| -------------------------------- | ----------------------------------- |
| Managed by Docker daemon         | Managed by non-Docker processes     |
| Path: `/var/lib/docker/volumes/` | Path: Any where on the host system  |
| Can be used in `Dockerfile`      | Can **not** be used in `Dockerfile` |

```sh
# list volumes
docker volume ls

# remove unused volumes
docker volume prune

# remove volume(s)
docker volume rm <volume(s)>

# remove all volumes
docker volume rm $(docker volumes ls -q)

# volume mount
docker run -v <volume>:<app-data-path> <image>
docker run --mount type=volume,source=<volume>,target=<app-data-path> <image>
# volume gets created if it doesn't exist!

# bind mount
docker run -v <host-path>:<app-data-path> <image>
docker run --mount type=bind,source=<host-path>,target=<app-data-path> <image>
# use absolute paths!
```

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

# remove unused images
docker image prune

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
docker run --name <container-name> -p <system-port>:<container-port> -v <volume>:<data-path> <image>:<image-version>
# General configuration
# `--name`: dedicate a name to container (when not provided a random name will be dedicated to container)
# `-e`: set environment variables for running container

# Life-cycle configuration
# `-d` `--detach`: run container in background (print container ID as response)
# `--rm`: remove container after exiting
# `--restart=<condition>:<max-retry>`: restart container on the mentioned 'condition' and retry for 'max-retry' times

# Network configuration
# `-p` `--publish`: publish container's port(s) to the host
# `--network <network>`: add container to the desired network (if network doesn't exist, it will be created!)

# Persisting data configuration
# `-v <volume>:<data-path>`: volume mount (volume gets created if it doesn't exist)
# `-v <host-path>:<data-path>`: bind-mount (no volume gets created)
# `--mount type=volume,source=<volume>,target=<data-path>`: volume mount (volume gets created if it doesn't exist) -new syntax-
# `--mount type=bind,source=<host-path>,target=<data-path>`: bind mount (volume gets created if it doesn't exist) -new syntax-


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

## Examples

```sh
# inspecting containers config related details
docker inspect -f '{{.Config}}' <container>
# using format string (-f --format) instead of grep since it works better on JSON objects!
# {{.Mounts}} -> Data Mounting configuration
# {{.Config.Env}} -> environment variables
# {{.Config.ExposedPorts}} -> exposed ports
# {{.NetworkSettings.Networks.bridge.IPAddress}} -> Running container's IP address

# inspecting all the containers' names and IP addresses
docker inspect -f '{{.Name}} ---> {{.NetworkSettings.Networks.bridge.IPAddress}}' $(docker container ls -aq)

# creating an ubuntu container which gets removed after exiting
docker run -exec -it --rm ubuntu /bin/bash
# if /bin/bash is not executed, ubuntu exits immediately after running since it doesn't have an entrypoint

# ping another container in the same network
docker exec -it <container> ping <target-container>
# if you saw 'executable file not found in $PATH', it means 'ping' command is not available; you can install it by following below process.

# installing ping command on a container
docker exec -if <container> /bin/bash
apt-get update
apt-get install iputils-ping

# running a MySQL database
docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:8.0.21
# By using 'MYSQL_RANDOM_ROOT_PASSWORD' as environment variable, a random password is generated for root user;
# which can be found in the container logs (look for GENERATED ROOT PASSWORD)
```

## Docker Compose

Best option for managing multiple dependent services with just one file, and creating dependency for order of running containers, also you can specify condition checks for your dependencies.

By default Docker Compose will look for `docker-compose.yaml` file, in order to use different files, you must use `-f` flag for passing your file

```sh
# Parse, resolve and render compose file in canonical format
docker compose -f <docker-compose-file> config

# download service image(s)
docker compose -f <docker-compose-file> pull

# build/rebuild service image(s)
docker compose -f <docker-compose-file> build
# `--no-cache`: Do not use cache when building the image

# create and run service containers
docker compose -f <docker-compose-file> up
# `--build`: build images before starting containers
# `-d`: run containers in detached mode

# stop and remove service containers, networks (keeps volumes)
docker compose -f <docker-compose-file> down
# `-v`: removing volumes as well!

# stop service containers (doesn't remove them)
docker compose -f <docker-compose-file> stop

# start service containers
docker compose -f <docker-compose-file> start

# snapshot of service containers logs
docker compose -f <docker-compose-file> logs
# `-f`: follow logs
# `-t`: add timestamp to logs

# running an interactive bash shell on desired service
docker compose -f <docker-compose-file> exec -it <service> /bin/bash

# running a command inside your container's shell
docker compose -f <docker-compose-file> exec <service> sh -c "<command>"

# list service containers status
docker compose -f <docker-compose-file> ps

# list service containers images
docker compose -f <docker-compose-file> images

# list service containers processes
docker compose -f <docker-compose-file> top

# scaling docker compose services
docker compose -f <docker-compose-file> scale <service-1>=<n> <service2>=<m> ...
```

- you can also run docker compose commands explicitly on your desired services if you provide the **service's name** after you command!

## Docker Swarm

**Benefits**

- Automation
- Load balancing
- Scaling
- Fail-over
- Rolling update (zero downtime)

### Nodes (servers)

![docker swarm](./images/swarm-diagram.webp)

#### Manager Nodes (Master)

- Manager are aware of the cluster status and configuration
- Manager have a **RAFT consensus group** (consider RAFT as some kind of database which holds cluster and services configuration)
- There must be more than one manager nodes in order to work with RAFT consensus group (usually an _odd_ number is chosen to have tie-breakers in consensus)
- usually there is only **one _Leader_** between manager nodes (leader-follower design)

#### Worker Nodes (Slave)

- Workers are responsible for running service's containers
- Workers are **not connected to the RAFT consensus group**, so they are not aware of the cluster configuration
- Workers can not work without managers

![swarm service life-cycle](./images/swarm-service-lifecycle.webp)

### Setup Docker Swarm

- **docker-machine**: can be used for creating virtual nodes and simulating a cluster.

```sh
# change node's name
hostnamectl set-hostname <name> && bash

# check swarm status
docker info

# initializing swarm & making this node manager(leader)
docker swarm init
# `--advertise-addr <IP>`: specify which IP address should be used for swarm services communication, from your NIC IPs

# remove current node from swarm cluster
docker swarm leave
# NOTE: if this is the last manager node you must use `--force` flag for leaving!

# shows join-token based on the provided role
docker swarm join-token <manager/worker>
# Run the provided join command on the node your want to join this swarm cluster based on its role

# joining swarm cluster
docker swarm join --token <token>
# based on the provided token, this node's role is specified (master/worker)
```

#### Swarm Cluster Network Configuration

- **TCP/port 2377**: Cluster management communications
- **TCP & UDP/port 7946**: Communication among nodes (for container network discovery)
- **UDP/port 4789**: _Overlay_ network traffic (for container ingress network)

- **Overlay Network**: Default network driver for swarm cluster

```sh
# Network configuration on Manger nodes
firewall-cmd --add-port=2377/tcp --permanent
firewall-cmd --add-port=7946/tcp --permanent
firewall-cmd --add-port=7946/udp --permanent
firewall-cmd --add-port=4789/udp --permanent

# Network configuration on Worker nodes
firewall-cmd --add-port=7946/tcp --permanent
firewall-cmd --add-port=7946/udp --permanent
firewall-cmd --add-port=4789/udp --permanent

# restarting firewall and docker to apply configurations
firewall-cmd --reload
systemctl restart docker

# check docker firewall status
systemctl status firewalld
```

```sh
# creating an overlay network
docker network create --driver overlay <name>

# creating a service in overlay network
docker service create --name webhost -p 8085:80 -d --network <overlay-network> nginx
# Now because of routing mesh, Nginx service is accessible via every node on 8085 published port in the swarm cluster specified network!

# add a service to a network
docker service update --network-add <network> <service>

# remove a service from a network
docker service update --network-rm <network> <service>

# updating a service published port
docker service update --publish-rm published=8080,target=80 --publish-add published=8083,target=80 <service>
```

#### Routing Mesh

**Routing Mesh** is a mechanism in Docker Swarm that allows you to **expose a service on every node in the swarm**, regardless of where the service tasks (containers) are actually running.
Even if a container of that service is running on only a single node, any node in the swarm can accept incoming traffic and route it to the appropriate container.

**Key Purpose of Routing Mesh**:

- Global Accessibility: You can publish a service on a specific port, and any node in the swarm will listen on that port.
- Load Distribution: It automatically routes traffic to the appropriate container instance (task), wherever it's running.
- Simplified Networking: Clients don't need to know which node actually runs the container.

**How Routing Mesh Works**:

1. **Published Ports & IPVS**

- When you run a service with a published port, Docker sets up a listener on that port on all nodes.
- Docker uses IPVS (IP Virtual Server) inside the Linux kernel for load balancing incoming requests.

2. **Ingress Network (Overlay Network)**

- Docker Swarm uses a special "ingress" overlay network.
- This network allows incoming requests to be forwarded from any node to a node where the service task is running.
- Nodes in the swarm use an **encrypted VXLAN tunnel for cross-node communication**.

3. **Connection Flow**

- Here’s what happens when a request comes in:
  - A client sends a request to a swarm node on a published port.
  - The node checks if it has a local task (container) for that service.
  - If Yes: It sends traffic to the container directly.
  - If No: It routes the traffic over the ingress overlay network to a node that has a running task.
  - **IPVS ensures even load distribution across tasks**.

**When to Use or Avoid Routing Mesh**:

- Use Routing Mesh:

  - When you want to expose a service externally without worrying about which node it runs on.
  - When you need a simple external Load Balancer.

- Avoid Routing Mesh (Use DNS Round-Robin Instead):
  - For internal microservice communication.
  - When you want more direct control over which node handles the traffic.

### Commands

#### Nodes

```sh
# list cluster nodes (only works on manager nodes!)
docker node ls

# promote a worker not to manager (only works on manager nodes!)
docker node promote <note-hostname>

# demote a manager to worker (only works on manager nodes!)
docker node demote <note-hostname>

# list current running services (tasks) on current node
docker node ps

# inspecting node information and status
docker node inspect --pretty <node>
# `--pretty`: prettifies the output

# list current running services (tasks) on desired noe
docker node ps <node-hostname>

# deactivating (draining) a node
docker node update --availability drain <node>
# by draining a node, its tasks will be distributed among other active nodes

# activating a node
docker node update --availability active <node>
# node will be activated, but tasks won't be distributed again

# adding label
docker node update --label-add <key>=<value> <node>
# label sample: region=iran

# removing label
docker node update --label-rm <key>=<value> <node>
```

- you manage task assignment more by using **constraint** and **labeling**!

#### Services

```sh
# running a sample ping service in swarm cluster
docker service create --name pingGoogle --replicas 4 alpine:latest ping 8.8.4.4
# 'verify: service converged' --means--> deployment was successful!

# creating a service and distribute it between nodes which have the given label's key-value
docker service create --name webhost -p 8080:80 --replicas 3 --constraint node.labels.<key>==<value> nginx:alpine

# limiting max number of replicas per node
docker service create --name ... --replicas 3 --replicas-max-per-node 1 <service>
# you can also update this property after creating your service
# `--restart-delay`: adding a delay before restarting services

# list running services
docker service ls

# check service status and see in which node it's running
docker service ps <service>

# inspecting service information and status
docker service inspect --pretty <service>
# `--pretty`: prettifies the output

# checking for swarm cluster containers
docker container ls
# Swarm container names: <TaskName>.<RandomString>

# show service logs
docker service logs <service>

# removing a service
docker service rm <service>
# In Docker Swarm, you can not stop a service!

# updating service replicas
docker service update <service> --replicas 5

# forcing service task distribution (used after activating nodes in the cluster)
docker service update --force <service>
```

### Rolling Update

**Process Flow**

1. You update the service definition (new image version, new env vars, etc.)

2. Swarm orchestrator plans an update:

- It checks the update configuration (parallelism, delay, failure action).
- It determines which tasks need to be replaced.

3. Update happens in steps (batches):

- Stops an existing task.
- Starts a new task with the updated specification (new image, env vars, etc.).
- Waits for the new task to become healthy.
- Proceeds to update the next task(s).

4. Monitors for failures:

- If a task fails to update, Docker can pause, continue, or roll back the update based on your settings.

#### Configuration & Commands

- **Parallelism**: `1` -> Number of containers which simultaneously will be updated (default)
- **delay**: 5m -> Delay duration between starting updates
- **On Failure**: `pause`(/`continue`/`rollback`) -> Pauses update if failure happens (default)
- **Update order**: `stop-first`(/`start-first`) -> First stops the task and then start updated task
- **Monitoring Period**: 5s -> Monitors process every 5 seconds
- **Max Failure Ratio**: 0 -> Max number of retries if failure happens

```sh
# update rolling update delay duration
docker service update --update-delay 1h1m1s <service>

# update rolling update parallelism
docker service update --update-parallelism 2 <service>

# update rolling update failure action to rollback
docker service update --update-failure-action rollback <service>

# update rollback failure action to continue
docker service update --rollback-failure-action continue <service>
# Now, rollback continues even if failure occurs during rollback process!

# performing rolling update on service(s) (updating services' image)
docker service update --image <new-image:new-version> <service>

# rollback update
docker service rollback <service>
docker service update --rollback <service>
# you can only revert last change, not further!!
```

### Stack Deploy

- **Docker Compose**: used for test/integration/development on a single Docker engine
- **Docker Stack**: used for production on Docker Swarm

you can create a docker compose file for both deployments; any configuration which is not supported by either Docker Compose or Docker Swarm will be ignored by them. similar to Docker Compose, specified volumes and overlay networks will be created by Docker Swarm; since stack is used for production it doesn't have _build_ command!

```sh
# deploying a stack compose file
docker stack deploy -c <stack-compose-file> <stack-name>

# list deployed stacks
docker stack ls

# list stack deployed services
docker stack services <stack-name>

# remove deployed stack
docker stack rm <stack-name>
```
