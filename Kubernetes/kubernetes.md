# Kubernetes

## Table of Contents

- [Kubernetes](#kubernetes)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Components](#components)
    - [Control Plane (Master)](#control-plane-master)
    - [Data Plane (Worker)](#data-plane-worker)
    - [Objects (The Things You Deploy)](#objects-the-things-you-deploy)
  - [Learning Environments](#learning-environments)
  - [Configurations](#configurations)
    - [Context Management](#context-management)
    - [Cluster Setup (Production Environment)](#cluster-setup-production-environment)
    - [Installing `containerd` Container Runtime](#installing-containerd-container-runtime)

## Introduction

[Kubernetes](https://kubernetes.io/docs/setup/) is a **container orchestration platform**. Its only job is to:

- Keep your containers running.
- Restart them when they fail.
- Scale them.
- Network them.
- Update them without downtime.

## Components

![Kubernetes Components](./images/kubernetes-components.png)

### Control Plane (Master)

- **API Server**

  - The **entry point**.
  - Everything — `kubectl`, `controllers`, `nodes` — talks to the API server. (`kubectl` converts your commands to REST HTTP requests for interacting with API Server!)
  - You don’t talk to anything else.
  - If this is down, you won’t “feel” the cluster immediately die, but you cannot manage it.

- **etcd**

  - A distributed key-value store.
  - Kubernetes **stores EVERYTHING here**:
    - Pod definitions
    - Secrets
    - ConfigMaps
    - Cluster state
  - If etcd is corrupted, the cluster is dead. This is **the most critical component**.

- **Controller Manager**

  - This is where Kubernetes **enforces the desired state**.
  - Example:
    - You want 3 replicas of a pod. 1 crashes -> Controller notices -> Controller creates a new one
  - It constantly reconciles **“what should be” vs “what is”**.

- **Scheduler**

  - Decides **where a pod should run**.
  - Example questions it answers:
    - Is there enough CPU?
    - Enough memory?
    - Correct node selector?
    - Tolerations/Taints OK?
  - If the scheduler stops working, existing pods continue running, but no new pods get scheduled.

- **Cloud Controller Manager** (optional)

  - Integrates with cloud providers (`AWS`, `GCP`, etc.).
  - Manages:
    - Load balancers
    - Persistent volumes
    - Routes
  - If you’re on bare-metal, this might not exist.

### Data Plane (Worker)

- **Kubelet**

  - The **agent running on every node**.
  - It **receives instructions from the API server**:
    - “Run this pod. Here is the definition.”
  - The kubelet talks to the container runtime to launch containers.
  - If kubelet dies → the node becomes “NotReady”.

- **Container Runtime**

  - `Docker`, `containerd`, `CRI-O` — doesn’t matter.
  - Its job is simple:
    - Pull the image
    - Start the container
    - Report status to kubelet
  - **Kubernetes does NOT run containers itself**.

- **Kube-Proxy**

  - **Manages networking rules** - received from the API server.
  - It ensures:
    - Services get virtual IPs
    - Load balancing to pods works
    - Cluster networking rules are correct
  - If this breaks → traffic routing breaks internally.

### Objects (The Things You Deploy)

- **Pod**: The smallest unit. Generally 1 container, sometimes more.
- **ReplicaSet**: Keeps a number of pods running.
- **Deployment**: Manages ReplicaSets + rolling updates.
- **StatefulSet**: Manages ordered, persistent workloads (databases).
- **DaemonSet**: Runs one pod per node (logging agents, node exporters).
- **Job / CronJob**: One-time or scheduled workloads.
- **Service**: Network abstraction for pods.
- **Ingress**: Routing from outside → inside cluster (HTTP/HTTPS).
- **ConfigMap / Secret**: Configuration and sensitive data.
- **PersistentVolume / PersistentVolumeClaim**: Storage.

## Learning Environments

- [Kind](https://kind.sigs.k8s.io/docs/user/quick-start/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)

## Configurations

### Context Management

- Kubectl configuration file: **`~/.kube/config`** or **`/root/.kube/config`**

```yaml
apiVersion: v1 # using version 1 of APIs for interacting with API Server
clusters: # List of current configured clusters and each ones name
  - cluster: # cluster configuration info
      certificate-authority: /home/malekpour/.minikube/ca.crt # This key is used for connecting to cluster using TLS
      extensions:
        - extension:
            last-update: Tue, 09 Dec 2025 20:16:34 +0330
            provider: minikube.sigs.k8s.io
            version: v1.37.0
          name: cluster_info
      server: https://192.168.49.2:8443 # Cluster's server address
    name: minikube # cluster's name
contexts: # context informs kubectl how to connect to a cluster (in which namespace and by using which user)
  - context:
      cluster: minikube
      extensions:
        - extension:
            last-update: Tue, 09 Dec 2025 20:16:34 +0330
            provider: minikube.sigs.k8s.io
            version: v1.37.0
          name: context_info
      namespace: default
      user: minikube
    name: minikube # context's name
current-context: minikube # Current active context of kubectl (by changing this to another context, you can update the default context of kubectl!)
kind: Config
preferences: {}
users: # List of users
  - name: minikube # user's name
    user:
      client-certificate: /home/malekpour/.minikube/profiles/minikube/client.crt # certificate for connecting to cluster
      client-key: /home/malekpour/.minikube/profiles/minikube/client.key # key for connecting to cluster
```

- If you have other clusters in other servers, you can add their configuration (IP & Port, public key - certificate) and define a context for connecting to them in your configured namespace and by using the valid user

### Cluster Setup (Production Environment)

- `kubeadm`: the command to bootstrap the cluster. (You need [`kubeadm`](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/) on both master and worker nodes for setting up your cluster.)
- `kubelet`: the component that runs on all of the machines in your cluster and does things like starting pods and containers. (You need `kubelet` on both master and worker nodes)
- `kubectl`: the command line util to talk to your cluster. (You only need `kubectl` on your master nodes.)
- Choose your `kubeadm`, `kubectl` and `kubelet` based on your `kubernetes` version!

- Now you can update your nodes' name using `hostnamectl set-hostname <desired-name>` command.
- Then your should define corresponding DNS records for your nodes in order to let them communicate with each other
- You can setup a DNS service like `bind` and connect it to your kubernetes or you can directly define your DNS records in each node:

```sh
vim /etc/hosts

# defined your desired node IP and host name
<node-IP-address> <node-hostname>
```

- below commands are required to be run on both master and worker nodes!
- Install required kernel headers (Since kubernetes does not use `iptables`, instead it uses Linux `IP-route` directly and adds some rules to the `iptables`)

```sh
# Debian kernel
sudo apt install kernel-devel-$(uname -r)

# Red-Hat kernel
sudo dnf install kernel-devel-$(uname -r)
```

- Now load kubernetes required kernel modules at runtime, like `bridge` and `port-forwarding` tools which are used mostly by `kube-proxy`

```sh
# Enable netfilter (iptables/nftables) on Linux bridge traffic.
sudo modprobe br_netfilter

# Enable IP Virtual Server (IPVS): Kernel-level Layer-4 load balancing, Faster and more scalable than iptables
sudo modprobe ip_vs

# Add Round-Robin scheduling to IPVS.
sudo modprobe ip_vs_rr

# Add Weighted Round-Robin scheduling.
sudo modprobe ip_vs_wrr

# Add Source Hashing (Same client IP → same backend pod): sticky sessions (session affinity)
sudo modprobe ip_vs_sh

# Enable OverlayFS, a union filesystem. (Container runtimes use OverlayFS to: Mount image layers efficiently, Avoid copying entire filesystems per container, Reduce disk usage and startup time)
sudo modprobe overlay
```

- Persist loaded kernel modules in kubernetes configuration

```sh
cat > /etc/modules-load.d/kubernetes.conf << EOF
br_netfilter
ip_vs
ip_vs_rr
ip_vs_wrr
ip_vs_sh
overlay
EOF
```

- Enable IP-forwarding in kubernetes configuration

```sh
cat > /etc/sysctl.d/kubernetes.conf << EOF
net.ipv4.ip_forward = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
```

- Now Refresh your configurations in order to apply them

```sh
sysctl --system
```

- Disable `swap-memory` (it can cause unexpected behavior and errors while using kubernetes)

```sh
# Disable swap-memory
sudo swapoff -a

# Comment out all swap entries in /etc/fstab, effectively disabling swap on system boot
sed -e '/swap/s/^/#/g' -i /etc/fstab

# check swap memory status
free -h
# swap-memory dedicated storage should be 0 now!
```

### Installing `containerd` Container Runtime

- Container Runtime is responsible for pushing/pulling images, managing repository, network and storage.
- `containerd` [releases](https://containerd.io/releases/), choose a stable and compatible version based on your kubernetes version
- Add docker repository to your OS package manager:

```sh
# Red-Hat - Docker
vim /etc/yum.repos.d/yum-docker.repo

# yum-docker.repo
[docker-ce]
name=centos $releasever - Docker-CE
baseurl=http://<repository-IP>:<repository-port>/repository/yum-docker/
gpgcheck=0
enabled=1
# local repository is a proxy for https://download.docker.com/linux/centos/9/x86_64/stable

# Debian
vim /etc/apt/sources.list.d/docker-ce.list

# docker-ce.list
deb [trusted=yes] http://<repository-IP>:<repository-port>/repository/apt-docker/ /
# updated this local repository according to your debian-based OS

# ------------------------------------------------------------------------------------------

# Red-Hat - Kubernetes
vim /etc/yum.repos.d/kubernetes.repo

# kubernetes.repo (Directly connected to internet)
[kubernetes]
name=kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v1.32/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v1.32/rpm/repodata/repomd.xml.key
exclude=kubelet kubeadm kubectl cri-tools kubernetes-cni
# update kubernetes version based on your installed kubernetes

# kubernetes.repo (Connected to local repository)
[kubernetes]
name=centos $releasever - Docker-CE
baseurl=http://<repository-IP>:<repository-port>/repository/yum-kubernetes/
gpgcheck=0
enabled=1
# local repository is a proxy for https://pkgs.k8s.io/core:/stable:/v1.32/rpm/

# ------------------------------------------------------------------------------------------

# Red-Hat - Packages
vim /etc/yum.repos.d/yum-repo.repo

# Configure it same as other repos proxying required CentOS package providers
```

- Now install `containerd`

```sh
# Red-Hat
yum install containerd.io

# Check Installation
crictl
# outputs available commands for interacting with containerd
```

- Default `containerd` configuration file: `/etc/containerd/config.toml`
- Advanced configuration of containerd: `sudo sh -c "containerd config default > /etc/containerd/config.toml"`
- Now update this advanced configuration for using local registry and interacting with kubernetes:

```sh
vim /etc/containerd/config.toml
```

```toml
<!-- Enable runc SystemCgroup -->
[Plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
  ...
  SystemdCgroup = true

<!-- Update Registry Mirrors -->
[Plugins."io.containerd.grpc.v1.cri".registry.mirrors]
  [Plugins."io.containerd.grpc.v1.cri".registry.mirrors."quay.io"]
    endpoint = ["http://<repository-IP>:<repository-port>"]
  [Plugins."io.containerd.grpc.v1.cri".registry.mirrors."docker.io"]
    endpoint = ["http://<repository-IP>:<repository-port>"]
  [Plugins."io.containerd.grpc.v1.cri".registry.mirrors."k8s.gcr.io"]
    endpoint = ["http://<repository-IP>:<repository-port>"]
  [Plugins."io.containerd.grpc.v1.cri".registry.mirrors."*"]
    endpoint = ["http://<repository-IP>:<repository-port>"]
  [Plugins."io.containerd.grpc.v1.cri".registry.mirrors."gcr.io"]
    endpoint = ["http://<repository-IP>:<repository-port>"]
  [Plugins."io.containerd.grpc.v1.cri".registry.mirrors."docker.elastic.io"]
    endpoint = ["http://<repository-IP>:<repository-port>"]

<!-- You should define a proxy repository for each one of these registries and them include them inside a group repository -->
```

```sh
# restart containerd for applying changes
systemctl restart containerd.service

# if containerd default service was not created, you should enable it
systemctl enable --now containerd.service
```
