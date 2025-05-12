# VIM
Vim is a powerful text editor often used in command-line environments.
Here I will provide and update a simple handout for VIM editor key bindings and modes, along side its robust features and plugins.

## Table of Contents
- [VIM](#vim)
  - [Table of Contents](#table-of-contents)
  - [Installation \& configuration](#installation--configuration)
    - [Plugin configuration](#plugin-configuration)
  - [Vim Modes](#vim-modes)
  - [Basic Operations](#basic-operations)
  - [Configurations](#configurations)
  - [Movements \& Navigation](#movements--navigation)
  - [Editing](#editing)
    - [Deleting \& Cutting](#deleting--cutting)
    - [Copying (Yanking)](#copying-yanking)
    - [Pasting](#pasting)
    - [Changing](#changing)
    - [Undo and Redo](#undo-and-redo)
  - [Searching \& Navigation](#searching--navigation)
  - [Indentation](#indentation)
  - [Substitution](#substitution)
  - [Marking \& Jumping](#marking--jumping)
  - [Registers](#registers)
  - [Macros](#macros)
  - [Plugins](#plugins)
    - [Vim Move - vim-move](#vim-move---vim-move)
    - [Surround - vim-surround](#surround---vim-surround)
    - [Comment - vim-commentary](#comment---vim-commentary)
    - [NERD Tree - nerdtree](#nerd-tree---nerdtree)
      - [Basic Navigation](#basic-navigation)
      - [Managing Tabs](#managing-tabs)
      - [File \& Directory Management](#file--directory-management)
      - [Bookmarking](#bookmarking)
      - [Miscellaneous](#miscellaneous)


## Installation & configuration
To install VIM on linux:
```
sudo apt install vim
```
modifying and customizing vim's configuration file
```
vim ~/.vimrc
```
by modifying vim's configuration file, you can make your customized changes and configuration persist; and you can also temporarily apply and use them directly from the vim's normal mode!

---

It's recommended to use **neo vim** instead of vim since it's better and supports using multiple plugins which provides numerous features and functionality alongside vim
To install Neo VIM on linux:
```
sudo apt install neovim
```
modifying and customizing neo-vim's configuration file
```
nvim ~/.config/nvim/init.vim
```
> A Sample for Neo-Vim configuration file: [NeuralNine / config-files](https://github.com/NeuralNine/config-files/blob/master/.config/nvim/old/init.vim)

### Plugin configuration
> [junegunn / vim-plug](https://github.com/junegunn/vim-plug) for managing and installing plugins:
```
call plug#begin()
Plug '<link-to-plugin-Github-repository>'
call plug#end()
```
After listing your required plugins in the neo-vim's configuration file, then open it with ```nvim``` like above, and:
- ```:PlugInstall``` Installs plugins from plug-links list
- ```:PlugUpdate```: Installs or updates the plugins
- ```:PlugDiff```: Reviews the changes from the last update
- ```:PlugClean```: Removes plugins no longer in the list


## Vim Modes
- **NORMAL mode**: Default mode for navigation and executing commands
  - VIM opens files in the normal mode
  - ```esc``` for returning to normal mode from insert mode
  - ```esc esc``` for returning to normal mode from visual mode
- **INSERT mode**: Where you can type and edit text
  - ```i``` for inserting before the cursor
  - ```<S-i>``` or ```I``` for inserting at the beginning of the current line
  - ```a``` for inserting after the cursor
  - ```<S-a>``` or ```A``` for inserting at the end of the current line
  - ```o``` for inserting in a new line below the current line
  - ```<S-o>``` or ```O``` for inserting in a new line above the current line
- **VISUAL mode**: Allows you to select and manipulate text visually
  - ```v``` for activating visual mode
  - ```<S-v>``` or ```V``` for activating visual line mode which allows to select lines(rows) by navigating
  - ```<C-v>``` for activating visual block mode which allows you to select columns by navigating
- **Replace mode**: Gets activate by pressing ```r``` and allows you to replace only one character then returns to normal mode after replacement


## Basic Operations
- Open a file: ```vim <file_name>```
  - note that if the file does not exist, vim creates it if you save your changes when exiting the vim editor!
- To save (write) changes: ```:w```
- To exit (quit): ```q```
- To save and exit: ```:wq```
- To exit without saving changes: ```:q!```
  - note that by exiting without saving your changes, any changes made will be discarded!


## Configurations
- ```:! <command>```: Runs your command in the terminal without closing the vim editor
- ```:set number```: Shows line numbers
- ```:set relativenumber```: Shows relative line numbers based on the current selected line (numbers change by moving through lines)
- ```:set mouse=a```: Activates the mouse cursor for selection and scrolling through lines
- ```:set tabstop=4```: Sets tab stop indentation to 4 spaces
- ```:set shiftwidth=4```: Sets shift width to 4 spaces (this option works with ```>>``` and ```<<``` for indenting and dedenting lines)
- ```:set autoindent```: Activates automatic indentation when pressing enter to enter next lines
- ```:colorscheme <color>```: Changes vim theme colors


## Movements & Navigation
- Use ```h```, ```j```, ```k```, ```l``` for left, down, up, and right movements respectively; you can also navigate your movements by using arrow keys, but using the first method is much faster!!
  - you can combine navigation keys with numbers which enables you to multiply navigation direction by that number, e.g. ```20j``` will move the cursor down by 20 lines from its current position.
- ```w```: Moves forward by a word
- ```b```: Moves backward by a word
- ```e```: Jumps to the end of a word
- ```<S-e>``` or ```E```: Jumps to the end of a word (ignores any ```-``` in the words when jumping to the end of the word)
- ```0```: Jumps to the beginning of the current line
- ```^```: Jumps to first (non-blank) character at the beginning of the current line
- ```$```: Jumps to the end of the current line
- ```gg```: Jumps to the beginning of the file
- ```<S-g>``` or ```G```: Jumps to the end of the file


## Editing
any action in the editing section **can be combined with numbers** which multiplies the number of execution times for that action!!

### Deleting & Cutting
- ```x```: Deletes the character under the cursor
- ```d```: Deletes selection in **visual** mode
- ```dw```: Deletes from the cursor until the start of the next word
- ```d2w or 2dw```: Deletes 2 words from the current cursor position
- ```diw```: Deletes the word under the cursor (inner word)
- ```di)``` or ```di(```: Deletes everything inside the parenthesis ()
- ```di"```: Deletes everything inside the quotation mark ""
- ```de```: Deletes to the end of the word
- ```dd```: Deletes the current line
- ```d0```: Deletes from the cursor to the beginning of the current line
- ```:[start],[end]d```: Deletes lines *start* through *end*
- ```<S-d>``` or ```d$```: Deletes from the cursor to the end of the current line
- note that **deleting is the same as cutting** and you can paste any deleted text where you want it!

### Copying (Yanking)
- ```y```: Yanks selection in the **visual** mode
- ```yy```: Yanks () the current line
- ```5yy```: Yanks 5 lines from the current position of the cursor
- ```yiw```: Yanks the current word under the cursor (inner word)
- ```ye```: Yanks to the end of the word
- ```yi(``` or ```yi)```: Yanks inside the parentheses ()
- ```y0```: Yanks from the cursor to the beginning of the line
- ```y$```: Yanks from the cursor to the end of the line

### Pasting
- ```p```: Pastes below the cursor
- ```<S-p>``` or ```P```: Pastes above the cursor

### Changing
- ```c```: Changes selection in the **visual** mode
- ```cc```: Changes the current line
- ```cw```: Changes the current word
- ```ci(``` or ```ci)```: Changes inside the parentheses ()
- ```cw```: Changes the current word
- ```c0```: Changes from the cursor to the beginning of the line
- ```c$```: Changes from the cursor to the end of the line
- ```cb```: Changes to the beginning of the previous word
- Note that when you want change something its position and dedicated space is preserved and only the contents are removed whereas when you want to delete something everything relevant to the context is removed!

### Undo and Redo
- ```u```: Undo changes individually (step by step)
- ```<S-u>``` or ```U```: Undo changes made to the current line (resets the current line to its original state)
- ```ctrl + r```: Redo changes
- ```.```: Repeat the last command

## Searching & Navigation
> All of this search and navigations can be combined with yank, change or delete actions!
- ```%```: Jumps between matching parentheses or brackets 
- ```t<character>```: Searches for the character's next occurrence on the current line and jumps <u>right before</u> that character
- ```<S-t><character>```: Searches for the character's previous occurrence on the current line and jumps <u>right after</u> that character
- ```f<character>```: Searches for the character's next occurrence on the current line and jumps <u>right on that</u> character
- ```<S-f><character>```: Searches for the character's previous occurrence on the current line and jumps <u>right on that</u> character
- ```nG``` or ```:n```: Jumps to the n-th line of the current file
- ```zz```: Centers the current line in the screen (for better content view)

---
> Searching in the Normal mode
- ```/<characters> + Enter```: Searches for the next occurrence of the characters
- ```?<characters> + Enter```: Searches for the previous occurrence of the characters
- ```n```: Jumps to the next search result
- ```<S-n>``` or ```N```: Jumps to the previous search result
---
> Searching in the Visual mode
  >> After selecting your token in this mode:
- ```*```: Jumps to the next occurrence of the selected token
- ```#```: Jumps to the previous occurrence of the selected token

## Indentation
- ```>>```: Indents the current line (or selected lines)
- ```<<```: Dedents the current line (or selected lines)
- ```==```: Auto-indents the current line (or selected lines)
- ```gg=G```: Auto-indents the entire file

## Substitution
- ```:%s/<search term>/<replacement term>/g```: Substitute all occurrences of the search term with the replacement term in the entire file
- ```:s/<search term>/<replacement term>/g```: Substitute all occurrences of the search term with the replacement term in the current line or selected lines

## Marking & Jumping
- ```m<letter>```: Sets a mark at the current position
- ```'<letter>```: Jumps to the mark position, set with the specified letter
> You can use letters like a, b, c, etc. to set a mark!

## Registers
- ```:reg```: Lists all registers and their contents
- ```"0p```: Pastes the contents of the unnamed register (last registered content)
- ```"7p```: Pastes the contents of register 7
- ```"7yy```: Yanks the current line into register 7
- ```"+```: Uses the system clipboard
- ```"+yy```: Copies the current line to the system clipboard

## Macros
- ```q<letter>```: Starts recording a macro into the specified register letter
- ```q```: Stops recording the macro
- ```@<letter>```: Executes the macro stored in the specified register letter
> You can also combine macro actions in another macro!

## Plugins

### Vim Move - [vim-move](https://github.com/matze/vim-move)
- ```<A-k>```: Move current line/selection up
- ```<A-j>```: Move current line/selection down
- ```<A-h>```: Move current character/selection left
- ```<A-l>```: Move current character/selection right

### Surround - [vim-surround](https://github.com/tpope/vim-surround)
- ```ysiw)```: Surrounds inner-word with parenthesis()
- ```cs("```: Changes surrounding parenthesis with double-quotations
- ```ds"```: Removes surrounding double-quotations

### Comment - [vim-commentary](https://github.com/tpope/vim-commentary)
- ```gcc```: Comments/Uncomments a line
- ```gc```: Comments/Uncomments selection in visual mode
- ```:7,10Commentary```: Comments/Uncomments lines from '7' to '10'

### NERD Tree - [nerdtree](https://github.com/preservim/nerdtree)

#### Basic Navigation
- ```:NERDTreeToggle```: Toggles NERD tree
- ```:NERDTreeFind```: Open NERDTree and locate the current file
- ```<C-w>w```: Cycle between open windows (NERDTree and main editor).
- ```<C-w>h```: Move focus to the window on the left (usually NERDTree)
- ```<C-w>l```: Move focus to the window on the right (usually the main editor)
- ```o```: Open file/directory (expand/collapse)
- ```i```: Open file in a split window (horizontally)
- ```s```: Open file in a split window (vertically)
- ```go```: Open file but keep focus in NERDTree
- ```p```: Jump to parent directory
- ```P```: Jump to root directory
- ```K```: Go to the first child node
- ```J```: Go to the last child node

#### Managing Tabs
- ```t```: Open file in a new tab
- ```T```: Open file in a new tab but stay in NERDTree
- ```gt```: Go to the next tab
- ```gT```: Go to the previous tab
- ```{number}gt```: Jump to a specific tab (e.g., 2gt for the second tab)
- ```:tabnew```: Open a new empty tab
- ```:tabclose```: Close the current tab
- ```:tabonly```: Close all tabs except the current one
- ```:tabs```: List all open tabs

#### File & Directory Management
- ```m```: Show menu for file operations (create, delete, rename, etc.)
- ```a```: Add a new file/directory (append / for directories)
- ```d```: Delete file/directory
- ```r```: Rename file/directory
- ```c```: Copy file/directory
- ```x```: Cut file/directory
- ```p```: Paste file/directory

#### Bookmarking
- ```B```: Toggle bookmarks
- ```b```: Add/remove a bookmark
- ```qb```: List all bookmarks

#### Miscellaneous
- ```u```: Move up a directory level (collapse parent)
- ```R```: Refresh the NERDTree
- ```q```: Close NERDTree
