# TMUX (Terminal Multiplexer)

## Table of Contents

- [TMUX (Terminal Multiplexer)](#tmux-terminal-multiplexer)
  - [Table of Contents](#table-of-contents)
  - [Installation \& Terms](#installation--terms)
  - [Commands](#commands)

## Installation & Terms

```sh
sudo apt install tmux
```

- **Pane**: Contains a terminal and running program, appears in one window
- **Window**: Groups one or more panes together, linked to one or more sessions
- **Session**: Groups one or more windows together (By default, the first session will be called `0`, the second `1` and so on.)

By installing **_powerline_** you can manage your sessions and commands better!

## Commands

`<C-b> ?`: List key bindings

`<C-b> %`: Splits window vertically

`<C-b> "`: Splits window horizontally

`<C-b> ↑/↓/→/←`: Switch between panes

`<C-b> ;`: Switch to last used pane

`<C-b> o`: Switch to next pane

`<C-b> <C-↑/↓/→/←>`: Change pane size

`<C-b> z`: Zoom pane to fullscreen (press again to exit zoom)

`<C-b> t`: Show current time

`<C-b> c`: Create new session

`<C-b> <n>`: Switch to session _n_ (e.g. 0,1,2,...)

`<C-b> D`: Detach from current session (saves session)

`<C-b> PgUp/PgDn`: Viewing long content (`q`: Quit, `N`: Next, `P`: Previous, `<C-s>`: Search)

`<C-b> s`: List sessions (also you can switch between them)

- `t`: target session
- `:kill-session`: kill desired session

`<C-b> :`: Enter command mode

- `setw synchronize-panes on`: Sync all panes
- `setw synchronize-panes off`: Unsync all panes

`tmux new`: Create new session

`tmux new -s <session-name>`: Create new session with the provided name

`tmux ls`: List sessions

`tmux attach`: Attach to the most recent session

`tmux attach -t <session>`: Attach to the desired session

`tmux kill-session -t <session>`: Kill specific session

`tmux rename-session -t <old> <new>`: Rename session
