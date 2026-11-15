# Mission 6 — Git and GitHub

## 1. Task / objective
The objective of Mission 6 is to understand distributed version control concepts and collaborative workflows using Git and GitHub:
- Master the fundamental Git workflow cycle: status inspection, staging, committing, and log review.
- Understand the technical difference between the staging area (index) and the permanent commit history.
- Create an isolated feature branch (`update-about`), update the root documentation, and commit the changes.
- Simulate and document the GitHub Pull Request (PR) lifecycle, peer review mechanics, and merge procedures.
- Compile a comprehensive, original glossary of core Git operations.

## 2. Work completed
- Inspected the repository status using `git status` across different project states.
- Analyzed the distinction between working directory, staging area (index), and repository database.
- Created and switched to the feature branch `update-about` using `git checkout -b update-about`.
- Added the `"## My Learning"` reflection section to the root `README.md` and committed the update on the branch.
- Merged the feature branch `update-about` back into `main` and verified the combined commit graph.
- Documented the Pull Request review workflow, purpose, and collaboration advantages.
- Authored a nine-part Git command glossary explaining version control commands in clear, practical terms.

---

### Task 6.1 — Understand the basic Git workflow

| Git Operation | What it does in your own words |
| :--- | :--- |
| **Check repository status (`git status`)** | Scans the working directory and index against the latest commit; lists untracked files, modified tracked files, staged changes, and current branch state. |
| **Stage selected changes (`git add <file>`)** | Moves specific modified or newly created files from the working directory into the Git staging area (the index), preparing them to be committed. |
| **Create a commit (`git commit -m "<message>"`)** | Takes a permanent cryptographic snapshot of all currently staged changes, saves it into the local `.git` repository database, and attaches author metadata, timestamp, and an explanatory message. |
| **View commit history (`git log` / `git log --oneline`)** | Outputs the chronological timeline of past commits, displaying commit SHA hashes, commit authors, dates, branch pointers, and commit descriptions. |

#### Difference Between Staging a Change and Committing It
- **Staging (`git add`):** Staging acts as an intentional drafting area or buffer. It allows a developer to hand-pick specific modified files or individual chunks of code that belong together logically for the next milestone, leaving unrelated or unfinished edits in the working directory untouched.
- **Committing (`git commit`):** Committing is the act of permanently recording that staged snapshot into Git's historical database. Once committed, the changes are assigned a permanent SHA-1/SHA-256 hash and cannot be lost accidentally. While staging prepares what *should* be saved, committing actually *saves* the milestone.

---

### Task 6.2 — Create and use a branch
Executed workflow:
```bash
# 1. Create and switch to new branch
git checkout -b update-about

# 2. Add 'My Learning' section to root README.md
# 3. Inspect status to confirm modifications
git status

# 4. Stage and commit on the branch
git add README.md
git commit -m "Add My Learning section to root README"
```

---

### Task 6.3 — Create a Pull Request (PR)
#### Lifecycle of a Pull Request:
1. **Publish Branch:** Push the local feature branch to GitHub (`git push -u origin update-about`).
2. **Open PR:** On the GitHub repository page, navigate to "Pull Requests", select `base: main` $\leftarrow$ `compare: update-about`, and click "New pull request".
3. **Describe Changes:** Provide a clear summary of why the changes were made, what was added (the "My Learning" section), and any relevant testing done.
4. **Peer Review & CI:** Teammates review the visual line-by-line diff (`green` for additions, `red` for deletions), suggest improvements, and automated tests run.
5. **Merge PR:** Once approved, click "Merge pull request" and confirm. The feature branch commits are merged into the `main` branch.
6. **Local Sync:** Switch back to local `main` (`git checkout main`) and pull the merged changes (`git pull origin main`).

#### Why Branches and Pull Requests are Useful:
- **A Branch** is an independent, lightweight pointer to a line of development. It allows developers to work on new features, experiment, or fix bugs in complete isolation without risking the stability of the production-ready `main` codebase.
- **A Pull Request (PR)** is a formal mechanism to notify team members that a feature branch is ready for integration. It fosters code review, prevents regressions, enables constructive feedback, ensures testing compliance, and maintains overall codebase quality before code becomes part of the permanent project history.

---

### Task 6.4 — Git command glossary

1. **Initialise a repository (`git init`):** Creates a new, empty Git repository by generating the hidden `.git` tracking directory in the current folder.
2. **Check status (`git status`):** Displays the working directory and staging area state, indicating modified, staged, or untracked files.
3. **Stage changes (`git add`):** Gathers and registers modified file changes into the staging area index in preparation for the next commit.
4. **Commit changes (`git commit`):** Records a permanent snapshot of the staged files into the Git version history with a descriptive message.
5. **View history (`git log`):** Displays the chronological log of recorded commits with hashes, timestamps, and commit messages.
6. **Create or list branches (`git branch`):** Lists all existing local branches when run bare, or creates a new branch pointer when given a name argument.
7. **Switch branches (`git checkout` / `git switch`):** Updates the working directory files to match the commit tree of the selected target branch.
8. **Publish changes (`git push`):** Uploads local branch commits to a designated remote repository on a hosting platform like GitHub.
9. **Retrieve remote changes (`git pull`):** Fetches the latest commits from the remote repository and immediately merges them into the active local branch.

---

## 3. Commands / tools used
- `git status`: Inspected staging and working tree state.
- `git checkout -b update-about`: Created and switched to the feature branch.
- `git add README.md`: Staged the modified root documentation.
- `git commit -m "..."`: Recorded branch and milestone commits.
- `git checkout main` and `git merge update-about`: Switched branches and integrated feature branch changes.
- `git branch -a`: Verified branch listings and references.

## 4. My understanding
Version control is an indispensable pillar of modern software engineering. Git functions as a distributed content tracker that treats project history as a graph of immutable snapshots. Branching and Pull Requests empower multiple developers to collaborate simultaneously on complex systems without colliding or destabilizing production code.

## 5. Difficulties faced
Understanding fast-forward merges versus 3-way merge commits when merging local branches.

## 6. How I resolved them
Observed Git's output during `git merge update-about` which completed a clean fast-forward merge since `main` had no diverging commits after the branch was created.

## 7. Evidence / files
- Root documentation update: `README.md` (containing "## My Learning")
- Feature branch: `update-about`
- Mission documentation: `mission-06-git-github/README.md`

## 8. Commit details
- Staged file: `mission-06-git-github/README.md`
- Commit message: `Complete Git and GitHub collaboration mission`
- Verification: Confirmed via `git status` and `git log -1`.
