# Kubernetes

## Table of Contents

- [Kubernetes](#kubernetes)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Components](#components)
    - [Control Plane (Master)](#control-plane-master)
    - [Data Plane (Worker)](#data-plane-worker)
    - [Kubernetes Terms](#kubernetes-terms)
  - [Learning Environments](#learning-environments)
  - [Configurations](#configurations)
    - [Context Management](#context-management)
    - [Cluster Setup Requirements (Production Environment)](#cluster-setup-requirements-production-environment)
    - [Installing `containerd` Container Runtime](#installing-containerd-container-runtime)
    - [Firewall Configuration](#firewall-configuration)
    - [Cluster Setup (Production)](#cluster-setup-production)
    - [Namespaces](#namespaces)
    - [Logs \& Port-Forwarding](#logs--port-forwarding)
    - [Labels](#labels)
    - [Annotation](#annotation)
    - [Liveness](#liveness)
    - [Replication Management](#replication-management)
    - [Useful Tricks](#useful-tricks)

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

### Kubernetes Terms

- **Resource**: Anything that you can manage/control using `kubectl`, e.g. Pod, Service, etc.
- **Pod**:
  - An **isolated wrapper** around containers which enables kubernetes to manage them.
  - The smallest unit of resources in kubernetes.
  - Generally consists of `1` container, sometimes more:
    - in case your containers need to interact with each other **isolated from outside** of the pod.
    - in case your containers need to **start/stop** together
    - in case your containers need to **scale** together
  - Each pod has a `VI - Virtual Interface` for connecting/interacting with other pods.
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

### Cluster Setup Requirements (Production Environment)

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

# kubernetes.repo (Directly connected to internet) -> kubernetes.repo.old for disabling repo, add a suffix to its name like .old or .backup
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

[appstream]
name=centos $releasever - AppStream
baseurl=http://<repository-IP>:<repository-port>/repository/yum-repo/AppStream/x86_64/os/
gpgcheck=0
enabled=1
# local repository is a proxy for https://mirror.stream.centos.org/9-stream/

[baseOs]
name=centos $releasever - BaseOs
baseurl=http://<repository-IP>:<repository-port>/repository/yum-repo/BaseOs/x86_64/os/
gpgcheck=0

[ha]
name=centos $releasever - HA
baseurl=http://<repository-IP>:<repository-port>/repository/yum-repo/HighAvailability/x86_64/os/
gpgcheck=0
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

### Firewall Configuration

```sh
# Checking firewall status
systemctl status firewalld.service

# Stop & Disable your firewall - Not Recommended!
systemctl stop firewalld.service
systemctl disable firewalld.service

# Instead of stopping & disabling your firewall manage kubernetes required ports!
```

- `Kubernetes` required ports:
  - `6443` -> Kubernetes API Server: Open to control-plane nodes and admins / CI. DO NOT EXPOSE PUBLICLY!
  - `2379` -> client traffic (API server → `etcd`)
  - `2380` -> peer traffic (`etcd` ↔ `etcd`)
  - `10250` -> `kubelet`
  - `10251` -> `kube-scheduler`
  - `10252` -> `kube-controller-manager`
  - `10255` -> `kubelet` read-only port
  - `5473`

### Cluster Setup (Production)

```sh
# Enable kubelet service
systemctl enable --now kubelet.service

# Check kubelet status
systemctl status kubelet.service

# if kubelet was experiencing FAILURE you can check its logs using
journalctl -r
# ignore not found error related to /var/lib/kubelet/config.yaml
# above file will be created after kubernetes installation
```

- Now install kubernetes

```sh
# List of required images for setting up kubernetes
kubeadm config images list

# Download kubernetes required images
kubeadm config images pull
# stored these images in your local repository for kubernetes setup in no-internet environments

# First, run this command on your master node
kubeadm init --pod-network-cidr=10.244.0.0/16
# --pod-network-cidr -> configuration of pods internal network
# -v6 -> by adding this flag you can run your kubernetes setup in debug mode to fix its errors

# Run after installation of kubernetes (prompted in logs!)
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# you will also be prompted with the command for joining worker nodes!

# Check your nodes
kubectl get nodes
```

- Now you need to manage kubernetes internal network by using a `CNI - Container Network Interface`
- `CNI` is a tool for container network and security management
- You can use different tools for fulfilling this purpose like:

  - [`Calico`](https://www.tigera.io/project-calico/)
  - `Flannel`
  - `Canal`
  - `Cilium`

- `Calico` [quickstart installation](https://docs.tigera.io/calico/latest/getting-started/kubernetes/quickstart)
- If your server is not connected to internet, you can save `tigera-operator.yaml` and `custom-resources.yaml` in your server.
- If you have multiple network interfaces - `NIC`, you must determine which one of them should be used for internal network under `Calico`:

```yaml
calicoNetwork:
  # ...
  nodeAddressAutodetectionV4:
    interface: <NIC-name(e.g. ens33)>
```

- update `cidr` address in `custom-resources.yaml` file based on the address you provided when using `kubeadm` init command (e.g. `10.244.0.0/16`) and the follow below instructions ([How to customize `Calico`](https://docs.tigera.io/calico/latest/getting-started/kubernetes/self-managed-onprem/config-options#how-to)):

```sh
kubectl create -f tigera-operator.yaml
kubectl create -f custom-resources.yaml
```

- Checking kubernetes pods:

```sh
# get pods in all namespaces
kubectl get pod -A
# After successful setup all of the pods should have 'Running' STATUS and '1/1` READY!
```

- Now your single-master kubernetes cluster is ready! (you can also setup a multi-master kubernetes cluster with a little bit more configuration!)
- Let's run some pods to test our cluster:

```sh
# Creating an nginx pod without any manifest
kubectl run nginx-pod --image=nginx --restart=Never --port=80 -n default

# check nginx status
kubectl get po
kubectl get pod

# check cluster services
kubectl get svc
kubectl get service
# you can find your cluster IP here!

# Exposing nginx-pod by creating nginx service
kubectl expose pod nginx-pod --type=NodePort --port=80 --name=nginx-service
# Now you can access your nginx service by using your public-IP on port 80!

# deleting nginx pod
kubectl delete po nginx-pod

# deleting nginx service
kubectl delete svc nginx-service
```

- Now let's create a manifest for nginx, called `nginx.yaml`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
    - name: nginx-container
      image: nginx:latest
      ports:
        - containerPort: 80
```

```sh
# creating nginx pod by its manifest
kubectl create -f nginx.yaml

# deleting manifest's pod
kubectl delete -f nginx.yaml
```

### Namespaces

- `Namespace`: is a high level wrapper for isolating different resources in kubernetes (similar to Linux namespaces)

```sh
# list available namespaces
kubectl get namespace
kubectl get ns
# kubernetes considers 'default' namespace when you are getting different resources

# Create namespace
kubectl create ns <namespace>

# Delete namespace
kubectl delete ns <namespace>
# Every corresponding resource of the desired namespace will be deleted!

# Delete all pods inside a namespace
kubectl delete po -n <namespace> --all

# Delete all resources inside a namespace (almost all resource)
kubectl delete all --all -n <namespace>

# Getting pods by using namespace filtering
kubectl get po --namespace <namespace>
kubectl get po -n <namespace>

# Getting all of the available pods in every namespace
kubectl get po -A

# Get a specific pod manifest (in different formats)
kubectl get po <pod> -n <namespace> -o yaml
kubectl get po <pod> -n <namespace> -o json
```

### Logs & Port-Forwarding

```sh
# Check pod logs
kubectl logs -n <namespace> <pod>

# Editing pod
kubectl po -n <namespace> <pod>
# Some properties are immutable and you can not edit them (e.g. container-name)
# After saving your changes, this pod will be restarted and your changes will apply!

# Check a container's logs in a specific pod
kubectl logs -n <namespace> <pod> -c <container>
# -f -> follow flag in order to follow generated logs

# Exposing your pod by port-forwarding
kubectl port-forward -n <namespace> <pod> <server-port>:<pod-port>
# Now your pod's internal port is accessible through server's port (from inside your server!)
# You can quickly test your pod by port-forwarding and curl command
# [C-c] will End your port-forwarding!
```

### Labels

- `Label` is a key-value pair used for **categorizing** your resources(e.g. pods, nodes) in the same namespace!

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels: # define labels here (key: value)
    app: nginx
    rel: beta
spec:
  nodeSelector: # Filter for node selection on deployment
    disk: ssd # label-key: label-value for filtering nodes
  containers:
    - name: nginx-container
      imagePullPolicy: Always
      image: nginx:latest
      ports:
        - containerPort: 80
          protocol: TCP
```

```sh
# Apply your changes
kubectl apply -f nginx.yaml

# List pods + labels
kubectl get po -n <namespace> --show-labels

# List pods + nodes (and complementary data)
kubectl get po -n <namespace> -o wide

# List pods + showing specific label(s) value
kubectl get po -n <namespace> -L <label-key>
kubectl get po -n <namespace> -L <label-key>,<label-key2>

# Filtering pods based on labels
kubectl get po -n <namespace> -l <label-key>
# pods without specified label will be excluded

kubectl get po -n <namespace> -l '!<label-key>'
# pods with specified label will be excluded

# Filtering pods/nodes based on label and its value
kubectl get po -n <namespace> -l <label-key>=<label-value>
kubectl get nodes -l <label-key>=<label-value>

# Filtering pods with combined label filters
kubectl get po -n <namespace> -l '!<label-key>',<label-key>=<label-value>

# Add label to pod
kubectl label po -n <namespace> <pod> key=value --overwrite
# If your label already exists you must use --overwrite flag (Caution: your previous label(s) will be overwritten!)
# If you label is new, you don't need overwrite flag

# Add label to node
kubectl label nodes <node> key=value

# Delete pods based on labels
kubectl delete po -n <namespace>  -l <label-key>=<label-value>
```

### Annotation

- `Annotation` is similar to label, but annotations are used for long-content key-value pairs.
- Used for:
  - Documenting project authors
  - Using `Beta` release features based on annotations

```sh
# Add annotation to pod
kubectl annotate po -n <namespace> key=value

# Get detailed information about pod
kubectl describe po -n <namespace> <pod>
# 'Events' section is very useful for debugging pods when using describe command
```

### Liveness

- Liveness is controlled by defining a health-check for your pod
- Consider defining liveness criteria based on the rule of thumb that a restart can resolve your liveness issue
- Types of liveness-probe:
  - HTTP: Sending a GET request to an endpoint and check its response
  - TCP: Establish a TCP connection to an address and check its connection
  - Exe-C: Check Exit status of a command after execution
- Best practices of health-check:
  - Keep health-check process light, do not include heavy processing for health-checks
  - Make health-check endpoint public, do not require authentication for health-check
  - Do not rely on external components and infra-structures for health-check (restarting your pod won't resolve external components failure)
  - Include some delay before restarting your pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
    app: nginx
spec:
  containers:
    - name: nginx-container
      imagePullPolicy: Always
      image: nginx:latest
      livenessProbe: # Defining liveness probe (immutable)
        httpGet: # liveness probe type
          path: / # where to call for health-check
          port: 80
        initialDelaySeconds: 15 # delay before restarting pod after liveness check failure
      ports:
        - containerPort: 80
          protocol: TCP
```

```sh
# watch for pods status change
watch kubectl get po
kubectl get po -w
# -w: is the watch flag to follow status changes

# check container events and health-check status
kubectl describe po <pod>

# when your pod restarts a new container is created; in order to check previous container logs, run
kubectl logs <pod> --previous
```

### Replication Management

- `Replica Controller`: Manages pod replication for high-availability by making sure there always a specified number of replicas are running simultaneously in cluster
- A `Replica Controller` consists of:

  - `Pod Selector`: criteria for selecting certain pods to be managed by this replica-controller
  - `Replicas`: Holds the number of replicas
  - `Pod Template`: A sample template for replication of pods, holding pod's specifications

- Now let's create a manifest for nginx replica controller, called `nginx-rc.yaml`:

```yaml
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx-rc
    app: nginx
spec:
  replicas: 2 # number of replicas
  selector:
    app: item # label criteria for selecting pods
  template: # signature for replicating pods
    metadata: # name will be created by replica-controller
      labels:
        app: item # must match the selector criteria
      spec:
        containers:
        - name: nginx
          image: nginx
          ports:
          - containerPort: 80
```

```sh
# Create replica controller
kubectl apply -f nginx-rc.yaml

# List replica-controllers
kubectl get rc
# if you change a pod labels, replica controller won't notice until a restart happens!

# Force deleting a pod
kubectl delete po <pod> --force
# This can be a bad-practice since it prevents graceful shutdown and resources might not get freed!

# Delete replica controller
kubectl delete rc <replica-controller>
```

- `ReplicaSet` is a more modern replication controller which provides more options for replication management, like:
  - Defining multiple labels for pod selection
  - Defining expressions which provide more advanced filtering for pod selection
- ReplicaSets focus on maintaining a defined number of pod replicas across the cluster. Their primary goal is to enhance availability and load balancing by ensuring multiple instances of an application run simultaneously.

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-rs
    app: nginx
spec:
  replicas: 2 # number of replicas
  selector:
    matchLabels: # you can define multiple labels
      app: item
  # ...
```

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-rs
    app: nginx
spec:
  replicas: 2 # number of replicas
  selector:
    matchExpressions: # Expressions provides more control on your selector criteria
    - key: app
      operator: In # you can use other operators like not-in, exist, etc.
      values:
        - item
  # ...
```

- `DaemonSet` ensures that **one instance** of a specific pod runs on **all or selected nodes** in a cluster. This is ideal for tasks like logging, monitoring, or other node-specific services.
- With DaemonSets, you can guarantee that critical services operate consistently across your entire infrastructure.

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: nginx-ds
    app: nginx
spec:
  selector:
    matchLabels: # you can define multiple labels
      app: item
  template:
    metadata:
      labels:
        app: item # must match the selector criteria
      spec:
        nodeSelector: # label criteria for selecting deployment nodes (if not mentioned all of the nodes are considered)
          disk: ssd
        containers:
        - name: nginx
          image: nginx
```

### Useful Tricks

- For ease of use you can utilize aliases and auto-completion for `kubectl` commands, by adding below configuration to your `~/.bashrc` file:

```sh
alias k='kubectl'

source <(kubectl completion bash)
complete -F __start_kubectl k
```

- When debugging your `NOT READY` nodes:
- First check for `kubelet` and `containerd` status:

```sh
# Check status
systemctl status containerd.service
systemctl status kubelet.service

# If services were in inactive(dead)/FAILURE status, restart them
systemctl restart containerd.service
systemctl restart kubelet.service

# Make sure to enable and activate your containerd and kubelet services to always keep them running!
```
