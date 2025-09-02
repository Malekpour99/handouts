# Interview Questions

## Table of Contents

- [Interview Questions](#interview-questions)
  - [Table of Contents](#table-of-contents)
  - [Git](#git)
    - [What does actually a git commit stores in itself?](#what-does-actually-a-git-commit-stores-in-itself)
    - [Merge Vs. Rebase](#merge-vs-rebase)
    - [Cherry-Pick](#cherry-pick)

## Git

### What does actually a git commit stores in itself?

A Git commit **_stores a snapshot of the entire working tree_**, not just the changes.

However, Git optimizes storage by:

- Storing the full snapshot only for the first commit.
- For subsequent commits, Git stores the snapshot as a set of differences (deltas) internally to save space — but conceptually, **each commit represents a full snapshot** of your project at that point in time.

1. Tree Object (Snapshot)

   Points to a tree object, which represents the directory structure and content (blobs) of the project at the time of the commit.
   This tree is what contains the actual files and folders (via SHA-1/SHA-256 hashes).

2. Parent Commits

   Points to one (or more) parent commits:

   - A normal commit has 1 parent.
   - The first commit has no parent.
   - A merge commit has 2 or more parents.

3. Author Information

   Includes the name and email of the person who originally wrote the changes.
   Also includes a timestamp (with timezone).

4. Committer Information

   Includes the name and email of the person who made the commit.
   Usually the same as the author, but can differ (e.g., if someone else applies your patch).
   Also includes a timestamp.

5. Commit Message

   A human-readable message describing what the commit does.
   Often includes details on what changed and why.

6. Commit Hash

   A SHA-1 or SHA-256 hash of the commit content (including metadata and tree).
   This hash uniquely identifies the commit and changes if any part of the commit changes.

7. Optional: GPG Signature

   A commit may be signed with a GPG key to verify its authenticity.

---

### Merge Vs. Rebase

`git merge`

- Combines changes from one branch into another by creating a new merge commit (unless _fast-forward_ is possible).
- Preserves the exact history of both branches.
- **Fast-forward merge**
  - Happens when the target branch has not diverged.
  - Git just moves the pointer forward — no new commit is created.
- **No fast-forward merge**
  - Happens when both branches have diverged.
  - Git creates a merge commit to tie them together.

`git rebase`

- Moves (or "replays") the commits from one branch on top of another branch, rewriting history.
- Commits are recreated with new hashes.

---

### Cherry-Pick

`git cherry-pick` lets you apply a specific commit (or set of commits) from one branch onto another branch, **without merging** the whole branch.
It takes the changes introduced by that commit and **creates a new commit** on top of your current branch.

- Usage:
  - **Hotfixes** → Apply a critical bug fix from a feature branch to main immediately.
  - **Backporting** → Apply a patch to an older release branch.
  - **Selective integration** → You want only one commit, not a whole merge.

---
