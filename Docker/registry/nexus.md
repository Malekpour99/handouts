# Nexus

## Core Concepts

### Blob Store

A blob store is the **physical storage backend** where Nexus keeps the actual artifact files (JARs, Docker images, NPM packages, etc.).

Think of it as the "disk space" for Nexus.

A blob store can be:

- **File system based** → stored on local disk or mounted volume.
- **Cloud based** → e.g., AWS S3.

**Multiple repositories can share the same blob store**.

Admins create blob stores mainly to manage storage strategy (e.g., put large Docker images in S3, Maven artifacts on local SSD).

### Repository

A repository is a **logical component where users interact** (upload/download) with artifacts.

Types:

- **Hosted** → store your own artifacts (e.g., your company’s internal builds).
- **Proxy** → cache artifacts from external registries (e.g., Maven Central, Docker Hub).
- **Group** → virtual view that combines multiple repositories under one URL.

Each repository must be assigned to **one blob store** for its storage.

Users and build tools (Maven, npm, Docker, etc.) never talk directly to blob stores — they always interact with repositories.

## Running a local registry

### Nexus Docker Container

```sh
# creating volume for persisting nexus data
docker volume create --name nexus-data

# running a local nexus container
docker run -d -p <nexus-GUI-port>:8081 -p <repository-port>:5000 --name nexus -v nexus-data:/nexus-data sonatype/nexus3

# initial admin password
docker exec -it <nexus-container> sh

    cd /nexus-data/
    cat admin.password

# login and change your admin password!
# only enable 'anonymous access' for secure internal systems which you are certain about them!
# by enabling anonymous access, anyone can browse and pull images from nexus repository but for pushing images everyone must login!
```

### Storage & Repository

- Create a new **file**-base blob storage
- Create a **docker (hosted)** repository
  - add your port for HTTP/HTTPS connection requests
  - enable anonymous pulls (only in safe internal environments)
  - dedicate your recently created blob to this storage

### Security

`Settings` → `Security` → `Realms`

Move **Docker Bearer Token Realm** to the **Active** column.

### Push/Pull Images

- How tags work:
- `[registry-host]:[port]/[namespace]/[image-name]:[tag]`
  - **registry-host:port** → your Nexus registry (e.g., 127.0.0.1:5000)
  - **namespace** → logical grouping (like a _folder_)
  - **image-name** → the actual project/app
  - **tag** → version (e.g., 1.0.0, latest, dev)

```sh
# tag an image for nexus repository
docker tag <image>:<version> <registry-host>:<repository-port>/<image>:<version>

# login to nexus repository
docker login <registry-host>:<repository-port>
# provide nexus username and password

# push image to repository
docker push <registry-host>:<repository-port>/<image>:<version>

# pull image from repository
docker pull <registry-host>:<repository-port>/<image>:<version>
```
