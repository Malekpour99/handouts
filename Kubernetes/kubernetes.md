# Kubernetes

## Table of Contents

- [Kubernetes](#kubernetes)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Components](#components)
    - [Control Plane (Master)](#control-plane-master)
    - [Data Plane (Worker)](#data-plane-worker)

## Introduction

Kubernetes is a **container orchestration platform**. Its only job is to:

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
  - Everything — `kubectl`, `controllers`, `nodes` — talks to the API server.
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

  - **Manages networking rules**.
  - It ensures:
    - Services get virtual IPs
    - Load balancing to pods works
    - Cluster networking rules are correct
  - If this breaks → traffic routing breaks internally.
