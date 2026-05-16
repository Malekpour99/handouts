# UV

## Table of Contents

- [UV](#uv)
  - [Table of Contents](#table-of-contents)
  - [Installation/Upgrade](#installationupgrade)
  - [Python Configuration](#python-configuration)
  - [Project Initial Environment Setup](#project-initial-environment-setup)
  - [Dependency Configuration \& Management](#dependency-configuration--management)

## Installation/Upgrade

- [UV official website](https://docs.astral.sh/uv/)

```sh
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Check uv version
uv --version

# Upgrade uv version
uv self update

# Show help
uv --help
```

## Python Configuration

```sh
# Show Python interpreters detected by uv
uv python list

# Show available Python versions for installation
uv python list --all-versions

# Install a Python version or multiple versions
uv python install 3.12
uv python install 3.11 3.12

# Pin/change project default Python version
uv python pin 3.12

# Use system-installed Python interpreter
uv venv --python /usr/bin/python3.12

# Show currently pinned Python version
cat .python-version
```

## Project Initial Environment Setup

```sh
# Create a new Python project
uv init <project>

# Create a virtual environment
uv venv
uv venv --python 3.12  # environment with a specific python version

# Remove and recreate environment (useful in CI/debugging)
uv venv --clear
rm -rf .venv # more aggressive

# Activate virtual environment (you don't actually need to run these, uv handles execution commands!)
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate.bat  # Windows CMD
.venv\Scripts\Activate.ps1  # Windows PowerShell
```

## Dependency Configuration & Management

```sh
# Install dependencies from pyproject.toml and uv.lock
uv sync
# uv sync uses uv.lock if present.
# If uv.lock is missing, dependencies are resolved from pyproject.toml and a lock file is generated.

# Sync/Install environment from requirements.txt
uv pip sync requirements.txt
uv pip install -r requirements.txt

# Add a dependency or multiple dependencies
uv add requests
uv add django djangorestframework psycopg2-binary

# Add a development dependency
uv add --dev pytest

# Remove a dependency
uv remove requests

# Upgrade a package
uv add requests --upgrade-package requests
uv add requests --upgrade

# Generate/update lock file
uv lock
# after modification of pyproject.toml file make sure to sync your uv.lock file with pyproject.toml!

# Upgrade all dependencies
uv lock --upgrade

# Install a package without modifying pyproject.toml
uv pip install requests

# Export dependencies to requirements.txt
uv export -o requirements.txt

# Create requirements.txt from current environment
uv pip freeze > requirements.txt

# Compile dependencies from requirements.in
uv pip compile requirements.in -o requirements.txt

# Show dependency tree
uv tree

# Run a Python script inside the project environment
uv run main.py

# Run a module
uv run -m http.server

# Run pytest
uv run pytest

# Run Django development server
uv run python manage.py runserver

# Run a command with a temporary dependency
uvx cowsay "hello"
uvx black .

# Run a specific tool temporarily
uv tool run black .

# Install a CLI tool globally
uv tool install ruff

# Upgrade an installed tool
uv tool upgrade ruff

# List installed tools
uv tool list

# Uninstall a global tool
uv tool uninstall ruff

# Clean unused packages from environment
uv pip prune
```
