# VIM
Vim is a powerful text editor often used in command-line environments.
Here I will provide and update a simple handout for VIM editor key bindings and modes, along side its robust features and plugins.

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

It's recommended to use neo vim instead of vim since it's better and supports using multiple plugins which provides numerous features and functionality alongside vim
To install Neo VIM on linux:
```
sudo apt install neovim
```
modifying and customizing neo-vim's configuration file
```
vim ~/.config/nvim/init.vim
```

## Vim Modes
- **NORMAL mode**: Default mode for navigation and executing commands
  - VIM opens files in the normal mode
  - ```esc``` for returning to normal mode from insert mode
  - ```esc esc``` for returning to normal mode from visual mode
- **INSERT mode**: Where you can type and edit text
  - ```i``` for inserting before the cursor
  - ```(Shift + i)``` or ```I``` for inserting at the beginning of the current line
  - ```a``` for inserting after the cursor
  - ```(Shift + a)``` or ```A``` for inserting at the end of the current line
  - ```o``` for inserting in a new line below the current line
  - ```(Shift + o)``` or ```O``` for inserting in a new line above the current line
- **VISUAL mode**: Allows you to select and manipulate text visually
  - ```v``` for activating visual mode
  - ```(Shift + v)``` or ```V``` for activating visual line mode which allows to select lines(rows) by navigating
  - ```ctrl + v``` for activating visual block mode which allows you to select columns by navigating


## Basic Operations
- Open a file: ```vim <file_name>```
  - note that if the file does not exist, vim creates it if you save your changes when exiting the vim editor!
- To save (write) changes: ```:w```
- To exit (quit): ```q```
- To save and exit: ```:wq```
- To exit without saving changes: ```:q!```
  - note that by exiting without saving your changes, any changes made will be discarded!

## Movements & Navigation
- Use ```h```, ```j```, ```k```, ```l``` for left, down, up, and right movements respectively; you can also navigate your movements by using arrow keys, but using the first method is much faster!!
  - you can combine navigation keys with numbers which enables you to multiply navigation direction by that number, e.g. ```20j``` will move the cursor down by 20 lines from its current position.
- ```w```: Moves forward by a word
- ```b```: Moves backward by a word
- ```e```: Jumps to the end of a word
- ```(Shift + e)``` or ```E```: Jumps to the end of a word (ignores any ```-``` in the words when jumping to the end of the word)
- ```0```: Jumps to the beginning of the current line
- ```^```: Jumps to first (non-blank) character at the beginning of the current line
- ```$```: Jumps to the end of the current line
- ```gg```: Jumps to the beginning of the file
- ```(Shift + g)``` or ```G```: Jumps to the end of the file

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
- ```(Shift + d)``` or ```d$```: Deletes from the cursor to the end of the current line
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
- ```P```: Pastes above the cursor

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
- ```Shift + u``` or ```U```: Undo changes made to the current line (resets the current line to its original state)
- ```ctrl + r```: Redo changes
