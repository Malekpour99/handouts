# GitLab

## Table of Contents

- [GitLab](#gitlab)
  - [Table of Contents](#table-of-contents)
  - [Installation \& Setup](#installation--setup)
  - [Runners](#runners)
  - [CI/CD Overview](#cicd-overview)
  - [CI/DC Configurations](#cidc-configurations)
    - [Executors](#executors)
    - [Manual Trigger](#manual-trigger)
    - [Tags](#tags)
    - [Environments](#environments)
    - [Variables](#variables)
    - [Rules](#rules)
    - [Releases](#releases)
    - [Cache \& Artifacts](#cache--artifacts)
    - [Parallel](#parallel)
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

- For creating a pipeline in your project you must create `.gitlab-ci.yml` file in your project base path and configure your pipeline in this file.

## CI/DC Configurations

### Executors

- [Executors](https://docs.gitlab.com/runner/executors/)
- An executor is the **environment type** that a GitLab Runner uses to **run your CI/CD jobs**.

| Executor           | Description                                                       | Typical Use Case                                         |
| ------------------ | ----------------------------------------------------------------- | -------------------------------------------------------- |
| **shell**          | Runs directly on the host’s shell (Bash, PowerShell, etc.)        | Simple builds, quick testing, local runners              |
| **docker**         | Runs each job inside a Docker container                           | Isolated builds, easy cleanup, reproducible environments |
| **docker+machine** | Dynamically creates Docker Machine instances (e.g., on cloud VMs) | Autoscaling CI infrastructure                            |
| **kubernetes**     | Runs each job in a Kubernetes pod                                 | Scalable CI/CD clusters                                  |
| **virtualbox**     | Runs jobs inside VirtualBox VMs                                   | Strong isolation (rarely used today)                     |
| **custom**         | Lets you define your own execution logic                          | Highly specialized setups                                |
| **ssh**            | Runs jobs remotely over SSH                                       | Deployments or remote build servers                      |
| **parallels**      | Runs jobs inside Parallels VMs                                    | macOS builds (e.g., for iOS apps)                        |

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

# This job is optional — the pipeline continues without waiting for manual trigger.
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

### Rules

- [Pipeline job rules](https://docs.gitlab.com/ci/jobs/job_rules/)
- define **conditions** that decide whether a job should run, be skipped, or run manually. Think of them as **if/else logic** for jobs.
- Rules replaced the older `only:` and `except:` keywords, offering much finer control.
- Each rule has three main parts:
  | Field | Description |
  | ---------------- | ------------------------------------------------------------- |
  | `if:` | A condition (uses GitLab predefined variables or custom ones) |
  | `when:` | Action to take if condition matches (`on_success` - default) |
  | `allow_failure:` | Whether failure of this job is allowed (`false` - default) |

```yaml
# Run this job if the branch is main. Otherwise, do not run (`when: never`)
job_name:
  script: echo "Hello"
  rules:
    - if: '$CI_COMMIT_BRANCH == "main"'
      when: always
    - when: never

# Runs only for tag pipelines (e.g., version releases).
publish:
  stage: deploy
  script: echo "Publishing release..."
  rules:
    - if: "$CI_COMMIT_TAG"
      when: on_success

# Deprecated - run this job only for merge requests
test:
  stage: test
  script: echo "Testing merge request"
  only:
    - merge_requests

# Deprecated - skip this job for tags
build:
  stage: build
  script: echo "Building..."
  except:
    - tags
```

### Releases

- [Release CI/CD](https://docs.gitlab.com/user/project/releases/)
- A GitLab Release is **a snapshot of your project at a specific point in time**, typically linked to a Git tag. (Think of it like GitHub Releases — a “tag + extra info” combo.)
- `GitLab Release CLI` tool was deprecated in GitLab 18.0 and is planned for removal in 20.0. Use the [`GitLab CLI`](https://docs.gitlab.com/editor_extensions/gitlab_cli/) instead; in order to manage releases and access other gitlab features as well.

```yaml
stages:
  - build
  - release

build:
  stage: build
  script:
    - echo "Building project..."
    - mkdir dist
    - echo "Hello Release" > dist/app.txt
  artifacts:
    paths:
      - dist/

release_job:
  stage: release
  script:
    - echo "Creating release $CI_COMMIT_TAG"
  release:
    tag_name: $CI_COMMIT_TAG
    name: "Release $CI_COMMIT_TAG"
    description: "Automatic release for $CI_COMMIT_TAG"
  only:
    - tags
```

- When you push a tag (e.g., `v1.0.0`), the pipeline runs.
- GitLab automatically creates a Release page under “`Deployments → Releases`”.
- The page shows:
  - Tag (`v1.0.0`)
  - Description
  - Artifacts (from the `build` job)

### Cache & Artifacts

- [Caching in CI/CD](https://docs.gitlab.com/ci/caching/)

| Feature       | Purpose                                                                                       | Lifetime                                  | Scope                  |
| ------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------- | ---------------------- |
| **Cache**     | Speed up builds by reusing dependencies between jobs or pipelines                             | Temporary; can be reused in next pipeline | Shared (if configured) |
| **Artifacts** | Store build results (e.g., compiled app, test reports) to pass between jobs or download later | Stored permanently (until expiration)     | Per pipeline / per job |

### Parallel

- [Parallel Job Execution](https://docs.gitlab.com/ci/jobs/job_control/#parallelize-large-jobs)
- The `parallel` keyword lets GitLab **create multiple copies of a job** that can run **simultaneously**.
- Each job runs in its own environment (runner instance) — this helps you:
  - Split workloads into smaller chunks
  - Reduce total pipeline execution time
  - Run tests or builds for different configurations or data sets
- GitLab also supports `matrix-style parallelism` — multiple jobs generated from combinations of variables.

## Fixing Common Issues

### How to solve `ERROR: Job failed (system failure): prepare environment: exit status 1. Check https://docs.gitlab.com/runner/shells/index.html#shell-profile-loading for more information`?

- Remove `.bash_logout` file: `sudo rm /home/gitlab-runner/.bash_logout` or comment all of its content.

### How to solve `permission denied while trying to connect to Docker daemon socket at ... ERROR: Job failed: exit status 1.`?

- Add `gitlab-runner` user to `docker` group: `usermod -aG docker gitlab-runner`
