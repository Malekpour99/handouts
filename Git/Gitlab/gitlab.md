# GitLab

## Table of Contents

- [GitLab](#gitlab)
  - [Table of Contents](#table-of-contents)
  - [Installation \& Setup](#installation--setup)
  - [Runners](#runners)
  - [CI/CD Overview](#cicd-overview)
  - [CI/DC Configurations](#cidc-configurations)
    - [Manual Trigger](#manual-trigger)
    - [Tags](#tags)
    - [Environments](#environments)
    - [Variables](#variables)
  - [Fixing Common Issues](#fixing-common-issues)
    - [How to solve `ERROR: Job failed (system failure): prepare environment: exit status 1. Check https://docs.gitlab.com/runner/shells/index.html#shell-profile-loading for more information`?](#how-to-solve-error-job-failed-system-failure-prepare-environment-exit-status-1-check-httpsdocsgitlabcomrunnershellsindexhtmlshell-profile-loading-for-more-information)
    - [How to solve `permission denied while trying to connect to Docker daemon socket at ... ERROR: Job failed: exit status 1.`?](#how-to-solve-permission-denied-while-trying-to-connect-to-docker-daemon-socket-at--error-job-failed-exit-status-1)

## Installation & Setup

- First get a VPS and define an `A` record for your desired domain to your server. (e.g. `gitlab.example.com`)
  - Resource Recommendations:
  - CPU: `4 core`
  - Memory: `8 GiB`
- Update and Upgrade your server packages:

  ```sh
  sudo apt update
  sudo apt upgrade -y
  ```

- Follow official documentation for installing GitLab: [Install Self-Managed GitLab](https://about.gitlab.com/install/#install-self-managed-gitlab)

  - Find your desired installation method and matching operating system and architecture
  - make sure to install `Community Edition`! (`Enterprise Edition` support and features are not supported in Iran due to sanctions)

- After installation you can change your configurations in this path: `/etc/gitlab/gitlab.rb`

  - e.g. changing your GitLab domain (`external_url`)

- Now after following these steps your GitLab should be available at your defined domain and SSL is also activated, now it's recommended to follow these steps:
  - Deactivating Sign-up (Uncheck `Sign-up enabled` option)
  - To access Admin panel search for `Admin Area` in the search bar

## Runners

| Scope Type                | Visibility     | Use Case Example                       |
| ------------------------- | -------------- | -------------------------------------- |
| Shared Runner             | All projects   | GitLab.com default runners             |
| Group Runner              | A GitLab group | Multiple microservices in one team     |
| Specific (Project) Runner | One project    | Sensitive or custom build environments |

- [Install GitLab Runner](https://docs.gitlab.com/runner/install/)
- Yon can setup runners on the self-hosted GitLab server or other servers and add them to the GitLab; in order to do so just follow its official documentation.
- For security and performance reasons, **install GitLab Runner on a machine separate from the machine that hosts your GitLab instance**.

## CI/CD Overview

- A **pipeline** is the entire process that runs when you push code or trigger automation. ([Pipelines](https://docs.gitlab.com/ci/pipelines/))
- A **stage** is a group of related jobs that run at the same point in that process.
- A **job** is a specific task that GitLab Runner executes (like running tests or building code).

```yaml
Pipeline
 ├── Stage 1: build
 │    ├── Job: compile_code
 │    └── Job: install_dependencies
 ├── Stage 2: test
 │    ├── Job: run_unit_tests
 │    └── Job: run_lint
 └── Stage 3: deploy
      ├── Job: deploy_staging
      └── Job: deploy_production
```

```yaml
stages:
  - build
  - test
  - deploy

build_app: # jog
  stage: build
  script:
    - echo "Building app..."

run_tests: # job
  stage: test
  script:
    - echo "Running tests..."

deploy_app: # job
  stage: deploy
  script:
    - echo "Deploying..."
```

- For creating a pipeline in your project you must create `gitlab-ci.yml` file in your project base path and configure your pipeline in this file.

## CI/DC Configurations

### Manual Trigger

Adding a manual trigger for a stage (or job) in GitLab CI/CD is a very common and useful technique — especially for things like production deployments, approvals, or controlled rollouts.

```yaml
when: manual
```

- GitLab won’t start that job automatically.
- Instead, it will show a “Play” button in the UI so a developer or maintainer can trigger it manually.

By default, a **manual job does not block the next stages**.
If you want it to pause the pipeline until you trigger it, you can add:

```yaml
allow_failure: false
```

```yaml
# This will pause the pipeline and wait for your manual confirmation.
deploy_staging:
  stage: deploy
  script: ./deploy_staging.sh
  when: manual
  allow_failure: false

# This job is optional — the pipeline continues without waiting if you skip it.
deploy_preview:
  stage: deploy
  script: ./deploy_preview.sh
  when: manual
  allow_failure: true
```

### Tags

You assign tags to a job to tell GitLab which runners are allowed to pick it up.

Best Practices:

- **Use tags to separate environments**: Example: `staging`, `production`, `aws`, `gcp`
- **Use tags to define runtime types**: Example: `docker`, `shell`, `kubernetes`, `windows`
- **Avoid too many tags per runner**: Only use relevant tags — they act like filters, not categories.
- **Match all tags**: A job’s runner must have **all listed tags** (not just one).
- **Fallback for untagged jobs**: By default, only **shared runners** can pick up **untagged jobs**.

```yaml
build_backend:
  stage: build
  tags:
    - shell
    - staging
  script:
    - echo "Building backend..."
```

- This job will **only run on runners that have both tags**: `shell` and `staging`.
- You can allow a runner to run untagged jobs by setting (in Runner Configuration):

```toml
run_untagged = true
```

### Environments

- A GitLab Environment represents a **deployment target** — a real-world place where your application is running or can be deployed.
- Environments provide **visibility and control** over deployments.
- GitLab automatically **tracks deployments**, **records history**, and **visualizes** environments in your project
- You can protect environments (like `production`) so that only specific users or roles can deploy to them.

```yaml
deploy_staging:
  stage: deploy
  script:
    - echo "Deploying app to staging server..."
  environment:
    name: staging
    url: https://staging.example.com
```

- GitLab creates an environment named staging (if it doesn’t exist).
- Links the deployment to that environment.
- Shows it in the GitLab Environments tab with:
  - Name (staging)
  - URL (https://staging.example.com)
  - Deployed commit info

Real-world sample

| Environment     | Purpose                | Typical Setup             | Trigger                     |
| --------------- | ---------------------- | ------------------------- | --------------------------- |
| **Development** | Developer sandbox      | Local/test server         | Auto on each push           |
| **Staging**     | Pre-production testing | QA environment            | Auto on `main` or `develop` |
| **Production**  | Live system for users  | Public or customer server | Manual or approval required |

### Variables

- [Predefined CI/CD Variables](https://docs.gitlab.com/ci/variables/predefined_variables/)
- Custom Variables

  - Global variables in `.gitlab-ci.yml`
    ```yaml
    variables:
      DOCKER_IMAGE: myapp
      DOCKER_TAG: latest
      APP_ENV: production
    ```
    - These are global — available to all jobs in the pipeline.
  - Job specific variables
    ```yaml
    deploy_staging:
      stage: deploy
      variables:
        APP_ENV: staging
      script:
        - echo "Deploying $APP_ENV"
    ```
  - GitLab UI variables (Best Practice)
    - `Project → Settings → CI/CD → Variables → Add Variable`
    - These are **secure**, **encrypted**, and injected into the CI job runtime automatically.

- Using environment substitution inside `docker-compose.yml`

```yaml
services:
  web:
    image: "${DOCKER_IMAGE}:${DOCKER_TAG}"
    environment:
      - APP_ENV=${APP_ENV}
      - DATABASE_URL=${DATABASE_URL}
    ports:
      - "${WEB_PORT}:80"
```

- GitLab CI/CD variables are injected into the environment, and docker compose replaces them at runtime.

## Fixing Common Issues

### How to solve `ERROR: Job failed (system failure): prepare environment: exit status 1. Check https://docs.gitlab.com/runner/shells/index.html#shell-profile-loading for more information`?

- Remove `.bash_logout` file: `sudo rm /home/gitlab-runner/.bash_logout` or comment all of its content.

### How to solve `permission denied while trying to connect to Docker daemon socket at ... ERROR: Job failed: exit status 1.`?

- Add `gitlab-runner` user to `docker` group: `usermod -aG docker gitlab-runner`
