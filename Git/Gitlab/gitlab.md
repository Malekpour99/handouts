# GitLab

## Table of Contents

- [GitLab](#gitlab)
  - [Table of Contents](#table-of-contents)
  - [Installation \& Setup](#installation--setup)
  - [Runners](#runners)

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
