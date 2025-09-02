# Interview Questions

## Table of Contents

- [Interview Questions](#interview-questions)
  - [Table of Contents](#table-of-contents)
  - [Docker \& Containerization](#docker--containerization)
    - [Image Vs. Container](#image-vs-container)
    - [Custom Image (Dockerfile) Best Practices](#custom-image-dockerfile-best-practices)
    - [Multi-Staging](#multi-staging)
    - [CMD Vs. RUN](#cmd-vs-run)
    - [Entrypoint](#entrypoint)
    - [Docker Vs. VM](#docker-vs-vm)
    - [How Docker Containers Are Isolated from Each Other?](#how-docker-containers-are-isolated-from-each-other)

## Docker & Containerization

### Image Vs. Container

- **Docker Image**

  - Think of it as a blueprint (or template).
  - It’s a read-only snapshot that contains everything needed to run an application: code, dependencies, libraries, environment variables, and configs.
  - Images are built in layers (each instruction in a Dockerfile creates a new layer).
  - They are immutable — once built, they don’t change.

- **Docker Container**

  - A running instance of an image.
  - Containers are mutable at runtime: they can write to their filesystem (a writable layer is added on top of the image).
  - Multiple containers can be created from the same image, each isolated with its own process space, networking, and storage.
  - Containers can be started, stopped, restarted, or destroyed without affecting the original image.

---

### Custom Image (Dockerfile) Best Practices

- Use official images or minimal base images (Prefer _language-specific_ base images)
- Use multi-stage builds (reduce image size by separating build and runtime environments)
- Document exposed ports and metadata (e.g. maintainer, version, etc.)
- Use Environment Variables (`ENV`) instead of hardcoding paths or other variables.
- Set WORKDIR instead of cd (use WORKDIR to define working directory; it’s clearer and Docker-layer aware)
- Install only what's necessary and combine RUN commands to reduce layers
- Clean up temporary files (remove caches and temp files after installing packages)
- Use non-root user (improves security by preventing privilege escalation in case of a container exploit)
- Minimize COPY scope using docker ignore (only copy what’s needed, use `.dockerignore` to skip unnecessary files e.g. node_modules, .git, etc.)
- Use ENTRYPOINT + CMD properly (ENTRYPOINT defines the fixed command; CMD defines default args -can be overridden-)
- Use specific tag for each image which shows file-version (e.g. _jenkins:2.1.4_)
- Use Linters for assessing Dockerfiles ([`hadolint`](https://github.com/hadolint/hadolint))
- Add HEALTHCHECK (helps detect if the app inside the container is working correctly)
- Limit containers processes during creation (use constraints like _CPU_ and _memory_ limits and _control group (cgroup)_ configurations)
- Analyze docker image layers ([`dive`](https://github.com/wagoodman/dive))

---

### Multi-Staging

Multi-staging allows you to separate the build environment (where you compile or bundle your app) from the runtime environment (where you actually run it).

- Compile/build in one stage (with all the heavy tooling).
- Copy only the final artifacts into a minimal base image.
- Keep the final runtime image lean and secure.

- **Benefits**

  - Smaller images → Faster pulls, less attack surface.
  - Cleaner Dockerfiles → You don’t need separate build scripts.
  - Security → No leftover compilers or secrets in the runtime image.
  - Flexibility → You can have multiple build stages for testing, linting, or packaging.

---

### CMD Vs. RUN

- `RUN`

  - Purpose: Executes a command at build time.
  - Used for: Installing software, modifying the image filesystem, etc.
  - Effect: The result becomes part of the final image layer.

- `CMD`

  - Purpose: Specifies the default command to run when a container starts (runtime).
  - Used for: Defining what the container should do by default.
  - Effect: Does not affect the image during build.

---

### Entrypoint

`ENTRYPOINT` defines the main command that will always run when a container starts.
It makes the container behave like an executable.
Unlike `CMD`, which is more of a “default argument”, `ENTRYPOINT` is the fixed command — arguments from `docker run` are passed to it.

- `ENTRYPOINT` -> fixed program.
- `CMD` -> default arguments to that program (but can be _overridden_ at runtime).

---

### Docker Vs. VM

1. Architecture

- VMs

  - Run a full operating system (guest OS) on top of a **hypervisor** (like VMware, VirtualBox, KVM).
  - Each VM includes its own kernel + system libraries + application.
  - Heavyweight: more resource overhead.

- Docker (containers)

  - Run on the **host OS kernel** (no guest OS).
  - Containers share the host kernel but isolate processes, filesystems, and networking using Linux namespaces & cgroups.
  - Lightweight: no need to boot a full OS.

2. Startup Time

- VMs: Minutes (booting an OS).
- Containers: Seconds or less (just starting processes).

3. Resource Usage

- VMs: Require dedicated CPU, memory, and disk. Duplicates OS overhead. (dedicated resources are not shared, even if they are not used!)
- Containers: Share resources dynamically; many more containers can run on the same host.

4. Portability

- VMs: Images are big (GBs), less portable.
- Containers: Images are layered and small (MBs), easy to move and deploy.

5. Isolation & Security

- VMs: Strong isolation — each VM has its own kernel. Good for untrusted workloads.
- Containers: Weaker isolation — all containers share the host kernel. Security depends on kernel hardening, namespaces, SELinux/AppArmor.

6. Use Cases

- VMs: Best for running multiple OS types on the same host (e.g., Linux + Windows). Good when strong isolation is needed.
- Containers (Docker): Best for microservices, CI/CD pipelines, cloud-native apps, fast scaling.

---

### How Docker Containers Are Isolated from Each Other?

1. Namespaces (provide isolation of resources)

Namespaces create the illusion that each container has its own dedicated system.

- **PID namespace** → Each container has its own process tree (can’t see or affect host/other containers’ processes).
- **NET namespace** → Each container has its own network stack (interfaces, IPs, routing tables, ports).
- **MNT namespace** → Separate filesystem view (different root FS, mounts).
- **UTS namespace** → Each container can have its own hostname & domain name.
- **IPC namespace** → Isolates inter-process communication (shared memory, semaphores, message queues).
- **User namespace** → Maps container users to different host users (can make root inside container map to unprivileged UID on host).

2. Control Groups (cgroups) (provide resource limits)

- Limit and monitor resources: CPU, memory, I/O, network bandwidth.
- Prevents one container from starving others.
- Example: You can cap a container to 512MB RAM and 1 CPU core.

3. Union File Systems (OverlayFS, AUFS, etc.)

- Each container gets its own **filesystem layer**.
- **Copy-on-write** ensures containers can modify files without affecting the base image or other containers.

4. Capabilities & Seccomp

- By default, containers drop many Linux capabilities (like loading kernel modules).
- `Seccomp` (secure computing mode) filters syscalls to restrict what a containerized process can do.

5. Security Modules

- Tools like `AppArmor` and `SELinux` add mandatory access control policies to restrict container actions beyond namespaces/cgroups.

---
