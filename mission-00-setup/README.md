# Mission 0 — Create your GitHub workspace

## 1. Task / objective
The objective of Mission 0 was to establish an organized project repository named according to the course standard (`digital-detective-8919`), verify core developer tooling (Python 3 and Git), construct the full modular directory hierarchy for all nine missions, and write the introductory root documentation.

## 2. Work completed
- Decided the repository naming convention following `digital-detective-<last 4 digits of USN>` (`digital-detective-8919`).
- Created the project folder on the local machine and initialized a Git version-controlled repository on branch `main`.
- Verified installed versions of Python 3 (`Python 3.9.6`) and Git (`git version 2.50.1`).
- Scaffolding the complete directory and file layout required by the assignment specification:
  - `README.md` (root project index and metadata)
  - `mission-00-setup/README.md`
  - `mission-01-computer-basics/README.md`
  - `mission-02-terminal/README.md`
  - `mission-03-operating-system/README.md`
  - `mission-04-programs/README.md`
  - `mission-05-numbers-data/README.md`
  - `mission-05-numbers-data/number_converter.py`
  - `mission-06-git-github/README.md`
  - `mission-07-networking/README.md`
  - `mission-08-final-report/README.md`
  - `evidence/` (directory for privacy-safe logs and outputs)
- Authored the root `README.md` containing student identification, mission index, security/privacy rules, and converter execution instructions.

## 3. Commands / tools used
- `python3 --version`: Verified the Python 3 interpreter installation and version (`Python 3.9.6`).
- `git --version`: Checked that Git version control is installed (`git version 2.50.1`).
- `mkdir -p <folders>`: Created the structured folder layout for all missions simultaneously.
- `git init`: Initialized a new local Git repository in the project root.
- `git branch -M main`: Renamed the initial default branch to `main`.
- `git status`: Inspected the working tree to confirm newly staged and untracked files.

## 4. My understanding
A **Git repository** is a specialized directory managed by the Git version control system that tracks the entire historical timeline of file modifications, additions, and deletions through cryptographically hashed commits. 

Organizing the project into distinct folders by **mission** provides clear modular separation of concerns. Each topic (e.g., terminal operations, process architecture, number encoding, network protocols) remains self-contained with its dedicated documentation, code, and evidence. This ensures that work can be reviewed independently, graded against specific rubrics, and maintained cleanly without cluttering the project root.

## 5. Difficulties faced
Initially, ensuring that no sensitive local paths, operating system usernames, or machine hostnames were exposed required careful file path handling and git configuration review.

## 6. How I resolved them
Adopted standardized relative paths throughout all documentation and verified that private machine credentials and personal usernames were systematically replaced with privacy-safe placeholders (e.g., `[redacted]`).

## 7. Evidence / files
- Root repository documentation: `README.md`
- Mission setup report: `mission-00-setup/README.md`
- Directory hierarchy:
  ```text
  digital-detective-8919/
  ├── README.md
  ├── evidence/
  ├── mission-00-setup/
  │   └── README.md
  ├── mission-01-computer-basics/
  ├── mission-02-terminal/
  ├── mission-03-operating-system/
  ├── mission-04-programs/
  ├── mission-05-numbers-data/
  ├── mission-06-git-github/
  ├── mission-07-networking/
  └── mission-08-final-report/
  ```

## 8. Commit details
- Staged all setup files (`README.md`, `mission-00-setup/README.md`, and project structure).
- Commit message: `Set up Digital Detective mission structure`
- Verification: Verified commit history with `git log --oneline`.
