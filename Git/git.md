# Git

## Table of Contents
- [Git](#git)
  - [Table of Contents](#table-of-contents)
  - [Configuration](#configuration)
  - [Initializing and Cloning](#initializing-and-cloning)
  - [Staging and Committing](#staging-and-committing)
  - [Branching](#branching)
  - [Merging](#merging)
  - [Rebasing](#rebasing)
  - [Cherry-picking](#cherry-picking)
  - [Pushing and Pulling](#pushing-and-pulling)
  - [Undoing Changes](#undoing-changes)
  - [Stashing Changes](#stashing-changes)
  - [Working with Remotes](#working-with-remotes)
  - [Viewing History](#viewing-history)
  - [Tagging](#tagging)
  - [Deleting and Cleaning](#deleting-and-cleaning)
  - [Signing Commits and Tags](#signing-commits-and-tags)
  - [Blaming](#blaming)
  - [Bisect](#bisect)
  - [Help](#help)
  - [Others](#others)

## Configuration
```bash
# Set global username
git config --global user.name "Your Name"

# Set global email
git config --global user.email "your.email@example.com"

# Check global configuration
git config --global --list
```

## Initializing and Cloning
```bash
# Initialize a new Git repository
git init

# Clone an existing repository
git clone <repository_url>

# Clone desired number (n) of the latest commits from a branch of an existing repository
git clone --branch=<branch_name> --depth=<n> <repository_url>
```

## Staging and Committing
```bash
# Check the status of the repository
git status

# Add a file to the staging area
git add <file>

# Add all files to the staging area
git add .
git add *
git add -A

# Add matching names to the staging area
git add *.py

# Add a specific file to the staging area
git add <file>

# Add patches from a specific file to the staging area
git add -p <file>
# y - stage the hunk
# n - skip staging the hunk
# s - split the hunk into smaller parts
# e - manually edit the hunk (use this to select specific lines)
# q - quit

# Unstage file (Keeping its changes)
git restore --staged <file>

# Commit changes with a message
git commit -m "Commit message"

# Commit changes
git commit
# Then your default terminal editor opens and you can write your commit title and description

# Edit the latest submitted commit
git commit --amend
# To add new changes, stage them before running above code!

# Show details of a specific commit
git show <commit_hash>

# Show details of the latest commit
git show HEAD

# Show a commit in a specific format
git show --pretty=short <commit_hash>
```

## Branching
```bash
# List all branches
git branch

# List all branches and their HEAD commit
git branch -v

# Lists branches that are fully merged into the current branch
git branch --merged

# Lists branches that still have unmerged commits with the current branch
git branch --no-merged

# Create a new branch
git branch <branch_name>

# Switch to a branch
git checkout <branch_name>

# Create and switch to a new branch
git checkout -b <branch_name>

# Delete a branch locally
git branch -d <branch_name>

# Delete a branch remotely
git push origin --delete <branch_name>

# Rename current branch
git branch -m <new-branch-name>

# Rename another branch
git branch -m <old-branch-name> <new-branch-name>
```

## Merging
```bash
# Merge 'branch_name' branch into the current branch (fast-forward)
git merge <branch_name>
git merge --ff <branch_name>

# Merge specified branch into the current branch, also Preserves the history by creating a merge commit (no-fast-forward)
git merge --no-ff feature-branch

# Merge changes from a specific commit
git merge <commit-hash>

# Stops the merge and restores the previous state
git merge --abort

# Ignores the conflicting commit and continues merging
git merge --skip

# Continue merge after resolving conflicts
git merge --continue

# The recursive strategy for merging branches (default)
git merge -s recursive feature-branch

# merging more than two branches (octopus strategy for merging multiple branches at once)
git merge -s octopus feature1 feature2 feature3

# merge two branches and resolves trivial conflicts (resolve strategy for simple merges)
git merge -s resolve feature-branch

# Merge but prefer the current branch's status and ignores incoming changes (ours strategy for conflicts)
git merge -s ours feature-branch
git merge -X ours feature-branch

# Merge but prefer the incoming changes (theirs strategy for conflicts)
git merge -X theirs feature-branch
```

## Rebasing
```bash
# Rebase the current branch onto the 'branch_name' branch
git rebase <branch_name>

# Moves the current branch to start from a specific commit
git rebase <commit-hash>

# Moves feature-branch commits on top of main
git rebase main feature-branch

# Moves the last 'n' commits onto main, skipping older commits in the current branch
git rebase --onto main HEAD~n

# Opens an interactive editor to modify the last 'n' commits in the current branch
git rebase -i HEAD~n

# Stops the rebase and restores the previous state
git rebase --abort

# Ignores the conflicting commit and continues rebasing
git rebase --skip

# Continue rebase after resolving conflicts
git rebase --continue
```
- During interactive rebase:
  - ***pick*** a commit: add a commit.
  - ***Reword*** a commit message: modify a commit message.
  - ***Squash*** multiple commits into one: merge commits.
  - ***Drop*** a commit: removes a commit.
  - *Reorder* commits: Simply move commit lines up/down in the rebase editor.

## Cherry-picking
```bash
# Copies a commit from another branch to the current branch
git cherry-pick <commit-hash>

# Picks and copies multiple commits.
git cherry-pick <commit-hash1> <commit-hash2>

# Copies all commits from <commit-hash1> (exclusive) to <commit-hash2> (inclusive).
git cherry-pick <commit-hash1>^..<commit-hash2>

# Copies changes and takes them to staging but doesn’t create a commit (lets you edit before committing)
git cherry-pick -n <commit-hash>

# Opens the commit message editor so you can modify the commit message.
git cherry-pick -e <commit-hash>

# Stops the cherry-pick and restores the previous state
git cherry-pick --abort

# Continue cherry-pick after resolving conflicts
git cherry-pick --continue
```

## Pushing and Pulling
```bash
# Push changes to a remote repository
git push origin <branch_name>

# Pull latest changes from a remote repository
git pull origin <branch_name>

# Fetch updates from a remote repository without merging
git fetch origin

# Set upstream branch for push (git push)
git push --set-upstream origin <branch_name>
git push -u origin <branch_name>

# Push changes based on the upstream
git push

# Set upstream branch for pull (git pull)
git pull --set-upstream origin <branch_name>
git pull -u origin <branch_name>

# Pull changes based on the upstream
git pull
```

## Undoing Changes
```bash
# Discards local changes in a tracked file and restores it to the last committed state
git checkout -- <file>

# Unstages a file but keeps its changes in the working directory
git reset <file>
git reset HEAD <file>

# Reset to a previous commit (soft reset, keeps changes staged)
git reset --soft <commit_hash>

# Reset to a previous commit (mixed reset, unstages changes but keeps them in the working directory)
git reset --mixed <commit_hash>

# Reset to a previous commit (hard reset, discards changes)
git reset --hard <commit_hash>

# Revert a commit
git revert <commit_hash>
```

## Stashing Changes
```bash
# Stash current changes
git stash

# Stash current changes with a message (helps to identify stash)
git stash push -m "My stash message"

# Stash current changes + untracked files
git stash -u
git stash --include-untracked

# Stash everything (even ignored files)
git stash -a
git stash --all

# List stashes
git stash list

# shows file changes in the latest stash
git stash show

# shows file changes in the latest stash (like a git diff output)
git stash show -p

# shows the changes in the second-most recent stash
git stash show stash@{1}
# 0 is the most recent stash!

# Apply the last stashed changes and deletes it from stash list
git stash pop

# Apply the last stashed changes without deleting it from stash list
git stash apply

# Apply a specific stash
git stash apply stash@{n}

# Removes the last stashed changes from stash list
git stash drop

# Removes a specific stash from stash list
git stash drop stash@{n}

# Removes all stashed changes
git stash clear
```

## Working with Remotes
```bash
# Add a remote repository
git remote add origin <repository_url>

# List remote repositories
git remote -v

# Change the remote URL
git remote set-url origin <new_repository_url>

# Remove a remote repository
git remote rm <remote_name>
```

## Viewing History
```bash
# Show commit history
git log

# Show commit history including all branches
git log --all

# Show commit history with one-line summaries
git log --oneline

# Show commit history with a graph of their branches
git log --graph

# Shows a history of all movements of HEAD, including commits, resets, checkouts, cherry-picks, and reverts.
git reflog
# useful for recovering lost commits

# Show current unstaged changes
git diff
git diff HEAD
git diff -u

# Show only which files changed (without details)
git diff --name-only

# Shows currents changes in the specified file
git diff <path/to/file>
# you can mention your desired file at the each diff command!

# Show changes in staged files
git diff --staged

# Compares changes to the previous commit before HEAD
git diff HEAD^

# Compares changes to the 'n'th previous commit before HEAD
git diff HEAD~n

# Compares two different commits
git diff <commit_hash_1> <commit_hash_2>

# Shows changes between current branch and 'main'
git diff main

# Compares two specific branches
git diff <branch_1> <branch_2>

# Compares local 'main' branch to its remote
git diff origin/main
```

## Tagging
```bash
# Create a new tag
git tag <tag_name>

# List all tags
git tag

# List all tags starting with "v"
git tag -l "v*"

# Show details and changes made by an annotated tag
git show <tag_name>

# Create an annotated tag with a message
git tag -a <tag_name> -m "Tag message"

# Create a tag for a specific commit
git tag -a <tag_name> <commit>
# Then your default terminal editor opens and you can write your tag title and description or message

# Push tags to remote repository
git push origin --tags

# Push a specific tag to remote
git push origin <tag_name>

# Delete a local tag
git tag -d <tag_name>

# Delete a remote tag
git push --delete origin <tag_name>
```

## Deleting and Cleaning
```bash
# Remove a file from local working directory and git history
git rm <file>

# Show what would be deleted (Dry Run)
git clean -n

# Interactively choose files to delete
git clean -i

# Remove untracked files (forced)
git clean -f

# Remove untracked files and directories (forced)
git clean -fd

# Remove untracked and ignored files (forced)
git clean -fx

# Removes all untracked files EXCEPT *.log files
git clean -f -e "*.log"

# Removes only untracked files that MATCH .log
git clean -f -X "*.log"
```

## Signing Commits and Tags
```bash
# Configure Git to use GPG for signing
git config --global user.signingkey <gpg_key_id>

git config --global commit.gpgsign true

# Sign a commit
git commit -S -m "Signed commit message"

# Verify a signed commit
git log --show-signature

# Create a signed tag
git tag -s <tag_name> -m "Signed tag message"

# Verify a signed tag
git tag -v <tag_name>
```

## Blaming
```bash
# Shows who last modified each line in a file
git blame <file>

# Shows the blame for a specific line in a file
git blame <file> -L <line-number>

# Shows the blame for a specific range of lines in a file
git blame <file> -L <start>,<end>

# Provides a more detailed, machine-readable format for the blame information, (useful for scripting or automation)
git blame --line-porcelain <file>

# Displays the author, timestamp, and the full file path for each line of code
git blame --show-name <file>

# Blames the lines of a file based on a specific commit hash
git blame <file> <commit-hash>

# Limits the blame to a specific date range. (use dates like `2025-01-01` or `last week`)
git blame --since=<date> --until=<date> <file>

# Ignores changes in whitespace when performing the blame. (useful whitespace changes aren’t relevant)
git blame -w <file>

# Performs blame analysis on a file from a specific branch.
git blame <branch> <file>
```

## Bisect
```bash
# Start a binary search to find a faulty commit
git bisect start

# Mark the current commit as bad
git bisect bad

# Mark a known bad commit
git bisect bad <commit_hash>

# Mark a known good commit
git bisect good <commit_hash>

# Let Git pick the next commit to test
git bisect next

# Reset bisect state after finishing
git bisect reset

# Run a script to automate bisecting
git bisect run <script>
```

## Help
```bash
# Show help for a specific command
git help <command>

# Show the manual page for a command
git <command> --help

# Show all available Git commands
git help -a

# Show guides and tutorials
git help -g
```

## Others
- ***api.github.com/users/<user_name>*** provides user information in a JSON format
- Create a Github repository named after your **username** to provide a special representation of your profile in Github!
- Create a Github repository named **username**.github.io to provide a web-page with this address for showing your resume or any other purpose!
