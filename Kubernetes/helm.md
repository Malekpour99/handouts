# HELM

In Kubernetes, Helm is the **package manager**. It helps you define, install, and upgrade even the most complex Kubernetes applications.
You can think of it as similar to `apt` for Ubuntu, `yum` for CentOS, or `brew` for macOS, but specifically designed for Kubernetes resources.

Here is a breakdown of what Helm does and why it is used:

1. **Manages "Charts"**

   Helm packages Kubernetes resources into a single unit called a **Chart**.

   A Chart is a collection of files that describe a related set of Kubernetes resources (e.g., `Deployments`, `Services`, `ConfigMaps`, `Ingress`).
   Instead of writing and managing 20 different `YAML` files for a complex application (like WordPress or Prometheus), you install one Chart.

2. **Templating Engine**

   One of Helm's most powerful features is its **templating** capability.

   **Dynamic Configuration**: Instead of hardcoding values in your YAML files, Helm uses a `values.yaml` file. You can change variables (like image tags, replica counts, or passwords) without editing the actual template files.
   **Reusability**: You can use the same Chart for multiple environments (`dev`, `staging`, `production`) by simply swapping out the values file.

3. **Release Lifecycle Management**

   Helm tracks the installation of Charts as Releases. It allows you to manage the lifecycle of your application easily:

   **Install**: Deploy a new application (`helm install`).
   **Upgrade**: Update an existing application to a new version (`helm upgrade`).
   **Rollback**: If an update fails, you can instantly revert to the previous working version (`helm rollback`).
   **Uninstall**: Remove the application and all associated resources cleanly (`helm uninstall`).

4. **Dependency Management**

   Charts can depend on other Charts. For example, if you are deploying an application that requires a database, you can declare the database Chart as a dependency. Helm will ensure both are installed together correctly.

5. **Community and Sharing**

   Helm allows users to share Charts via **Repositories** (such as Artifact Hub). This means you don't have to build everything from scratch; you can install popular software (like MySQL, Redis, or NGINX) using community-maintained Charts.
