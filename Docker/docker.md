# Docker


## Table of Contents

- [Docker](#docker)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Commands](#commands)
    - [Docker Commands Structure](#docker-commands-structure)

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

## Commands

### Docker Commands Structure

```sh
# new structure
docker <management command> <sub-commands> <options>

# old structure
docker <command> <options>
```
