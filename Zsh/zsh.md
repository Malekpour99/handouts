# oh-my-zsh

## Table of Contents

- [oh-my-zsh](#oh-my-zsh)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Shortcuts](#shortcuts)
  - [Plugins](#plugins)
    - [git](#git)
      - [**Aliases**](#aliases)
    - [zsh-syntax-highlighting](#zsh-syntax-highlighting)
    - [zsh-autosuggestions](#zsh-autosuggestions)
      - [**Shortcuts**](#shortcuts-1)

## Installation

```sh
# install zsh (if not installed)
sudo apt update
sudo apt install zsh -y

# install oh-my-zsh via curl
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# install oh-my-zsh via wget
sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
```

## Shortcuts

- `<C-a>`: Move to **start** of line
- `<C-e>`: Move to **end** of line
- `<A-b>`: Move **back** one word
- `<A-f>`: Move **forward** one word
- `<C-u>`: Delete from cursor to **start** of line
- `<C-k>`: Delete from cursor to **end** of line
- `<C-w>`: Delete the **previous word**
- `<C-y>`: **Paste** (yank) the last killed text
- `<C-r>`: **Search history** interactively
- `<C-d>`: Exit shell (if line is empty)
- `<C-l>`: Clear the screen (like `clear`)
- `<C-_>`: Undo last action
- `<Esc-.>` / `<A-.>`: Insert last argument from previous command (press repeatedly to cycle back through earlier arguments)

## Plugins

### git

GIT plugin is included when you instal oh-my-zsh

#### **Aliases**

| Alias  | Full Command                           | Description                               |
| ------ | -------------------------------------- | ----------------------------------------- |
| `gst`  | `git status`                           | Show working tree status                  |
| `gss`  | `git status -s`                        | Short format status                       |
| `gl`   | `git pull`                             | Fetch and merge from origin               |
| `gp`   | `git push`                             | Push current branch to origin             |
| `gco`  | `git checkout`                         | Switch branches or restore files          |
| `gcm`  | `git commit -m`                        | Commit with message                       |
| `gaa`  | `git add --all`                        | Stage all changes                         |
| `gcam` | `git commit -a -m`                     | Stage and commit all changes with message |
| `gb`   | `git branch`                           | List branches                             |
| `gcb`  | `git checkout -b`                      | Create and switch to new branch           |
| `glog` | `git log --oneline --graph --decorate` | Nice visual git log                       |
| `gcl`  | `git clone`                            | Clone a repo                              |
| `gsta` | `git stash`                            | Stash current changes                     |
| `gstp` | `git stash pop`                        | Pop the last stash                        |
| `grh`  | `git reset HEAD`                       | Unstage files                             |


### zsh-syntax-highlighting

```sh
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

vim ~/.zshrc

# add `zsh-syntax-highlighting` to plugins and include its source:
plugins=(... zsh-syntax-highlighting)

# ...
source ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
```

### zsh-autosuggestions

```sh
git clone https://github.com/zsh-users/zsh-autosuggestions \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

vim ~/.zshrc

# add `zsh-syntax-highlighting` to plugins and include its source:
plugins=(... zsh-autosuggestions)

# OPTIONAL (if suggestions are faint), add below line to `.zshrc`
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=#999999'
```

#### **Shortcuts**

| Key               | Action                                        |
| ----------------- | --------------------------------------------- |
| `→` (Right arrow) | Accept suggestion                             |
| `<C-F>`           | Accept full suggestion                        |
| `<A-→>`           | Accept next word of suggestion (customizable) |
