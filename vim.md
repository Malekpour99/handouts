# VIM
Vim is a powerful text editor often used in command-line environments.
Here I will provide and update a simple handout for VIM editor key bindings and modes, along side its robust features and plugins.

## Installation & configuration
To install VIM on linux:
```
sudo apt install vim
```
To install Neo VIM on linux:
```
sudo apt install neovim
```

## Vim Modes
- **NORMAL mode**: Default mode for navigation and executing commands
  - VIM opens files in the normal mode
  - ```esc``` for returning to normal mode from any other mode
- **INSERT mode**: Where you can type and edit text
  - ```i``` for inserting before the cursor
  - ```(Shift + i) or I``` for inserting at the beginning of the current line
  - ```a``` for inserting after the cursor
  - ```(Shift + a) or A``` for inserting at the end of the current line
  - ```o``` for inserting in a new line below the current line
  - ```(Shift + o) or O``` for inserting in a new line above the current line
- **VISUAL mode**: Allows you to select and manipulate text visually
  - ```v``` for activating visual mode
  - ```(Shift + v) or V``` for activating visual line mode which allows to select lines(rows) by navigating
  - ```ctrl + v``` for activating visual block mode which allows you to select columns by navigating
