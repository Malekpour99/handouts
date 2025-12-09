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
