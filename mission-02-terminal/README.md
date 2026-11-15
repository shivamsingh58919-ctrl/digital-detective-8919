# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The objective of Mission 2 is to develop proficiency with the Unix command-line interface (CLI):
- Execute core navigation and file-management commands inside the repository.
- Practise non-destructive file editing (appending vs. overwriting) and file manipulation inside an isolated `terminal-practice/` directory.
- Explore command-line options/flags and Unix pipelines (`|`) for stream redirection.
- Understand package managers on macOS (Homebrew) and inspect installed packages.

## 2. Work completed
- Explored 9 fundamental terminal operations and documented their execution, syntax, and observed behavior in a structured table.
- Created an isolated practice directory `terminal-practice/`.
- Generated `notes.txt`, appended a second line of text using stream appending (`>>`), confirmed content integrity via `cat`, duplicated it to `notes_backup.txt`, and renamed the backup to `notes_archive.txt`.
- Compared standard directory listings against flags `-l`, `-a`, `-h` (`ls -lah`), analyzing permission bits, inode links, timestamps, hidden dotfiles, and unit-scaled file sizes.
- Constructed a pipeline combining `ls -lah` with `head -n 5` to filter output streams.
- Inspected the local package manager (Homebrew 7.0.12) and cataloged managed packages.

---

### Task 2.1 — Explore basic Terminal operations

| Operation / Command Name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the absolute path of the current working directory from the root filesystem `/`. | Returned the absolute path leading to `/.../digital-detective-8919`. |
| **Directory listing (`ls`)** | Lists the names of visible files and directories inside the current location. | Displayed all mission subdirectories and `README.md` in clean columns. |
| **Detailed listing (`ls -l`)** | Formats the directory listing in long format displaying permissions, links, owner, group, file byte size, and modification timestamp. | Revealed permission strings (e.g. `drwxr-xr-x`), owner/group names, size, and date modified. |
| **Change directory (`cd ..` / `cd -`)** | Shifts the working directory context to the parent directory or prior directory. | Shell prompt updated location indicator; running `pwd` confirmed moving up one level. |
| **Create directory (`mkdir practice-folder`)** | Allocates a new directory node in the filesystem. | Directory was created instantly without output; confirmed presence with `ls`. |
| **Create empty file (`touch practice.txt`)** | Creates an empty 0-byte file or refreshes the access/modification timestamps if it exists. | A new file `practice.txt` appeared with size 0 bytes. |
| **Copy file (`cp practice.txt practice_copy.txt`)** | Reads the source file data and creates an exact clone under a new filename/location. | An identical independent copy was created; changes to the clone did not affect the source. |
| **Move / rename file (`mv practice_copy.txt renamed.txt`)** | Renames a file or moves it to another directory path by updating directory table pointers. | `practice_copy.txt` ceased to exist under that name, appearing as `renamed.txt`. |
| **Display file contents (`cat practice.txt`)** | Reads file data sequentially and streams it directly to standard output (`stdout`). | Printed the textual contents of the file directly into the terminal window. |

---

### Task 2.2 — Practise file changes safely
Conducted within the dedicated `terminal-practice/` subfolder:
```bash
# 1. Create file and add line 1
echo "Line 1: Exploring terminal fundamentals." > notes.txt

# 2. Append line 2 without overwriting line 1
echo "Line 2: Appending data safely with double chevrons." >> notes.txt

# 3. Confirm both lines are present
cat notes.txt

# 4. Make backup copy and rename it
cp notes.txt notes_backup.txt
mv notes_backup.txt notes_archive.txt
```

**Observed Verification Output:**
```text
Line 1: Exploring terminal fundamentals.
Line 2: Appending data safely with double chevrons.
```

**Conceptual Analysis:**
- **Replacing vs. Appending (`>` vs. `>>`):** The single greater-than operator (`>`) redirects `stdout` by truncating (clearing) any existing file content before writing, effectively replacing the file. The double greater-than operator (`>>`) opens the file in append mode, preserving existing contents and seeking to the end of the file before writing new bytes.
- **Copying vs. Moving (`cp` vs. `mv`):** `cp` duplicates data blocks, creating a new inode and distinct storage footprint. `mv` on the same filesystem simply updates directory entry pointers and file names without re-copying the underlying data blocks on disk; the original filename disappears.
- **Current-directory display utility (`pwd`):** Provides the user and executing scripts with the exact absolute location within the hierarchical filesystem, preventing accidental modifications to files in unintended directories.
- **Directory listing utility (`ls`):** Enables visual verification of filesystem structure, file existence, permissions, file size, and recent changes before executing destructive or modifying operations.

---

### Task 2.3 — Understand flags and pipes
**Comparison of `ls` vs. `ls -lah`:**
- `ls`: Outputs only visible file and directory names in alphabetical columns with no metadata.
- `ls -lah`:
  - `-l`: Displays long format (file permissions, link count, owner, group, size, date/time).
  - `-a`: Includes hidden files (entries whose names start with `.`, such as `.git` and `..`).
  - `-h`: Scales file sizes into human-readable units (`K`, `M`, `G`) rather than raw byte counts.

**Pipeline Execution:**
```bash
ls -lah | head -n 5
```
**Privacy-Safe Output:**
```text
total 8
drwxr-xr-x@ 15 [redacted-user]  staff   480B Nov 15 20:39 .
drwxr-xr-x@  3 [redacted-user]  staff    96B Nov 15 20:38 ..
drwxr-xr-x@ 12 [redacted-user]  staff   384B Nov 15 20:39 .git
-rw-r--r--@  1 [redacted-user]  staff   3.8K Nov 15 20:38 README.md
```

**Explanation of the Pipe (`|`):**
The Unix pipe (`|`) connects the standard output (`stdout`) of the command on its left directly to the standard input (`stdin`) of the command on its right via an operating-system kernel buffer. 
- Left side (`ls -lah`): Generates a complete, detailed stream of all directory entries.
- Right side (`head -n 5`): Reads the incoming stream and filters it, passing only the first 5 lines to terminal display and terminating the pipe cleanly.

---

### Task 2.4 — Understand package managers
**Inspection of Local Package Manager:**
- Package Manager: Homebrew (`brew`)
- Installed Version: `Homebrew 7.0.12` (at `/opt/homebrew/bin/brew`)
- Managed Formulae / Packages: `flac`, `libogg`, `portaudio`
- Managed Casks: `vorssaint`

**Why Package Managers are Useful:**
A package manager acts as a centralized software coordinator for an operating system. Instead of manually downloading archived binaries, resolving missing shared library dependencies, and compiling source code, a package manager automates dependency resolution, integrity checking, installation, version upgrading, and uninstallation through single declarative commands. This ensures reproducible environments, consistent path configurations, and secure updates across system software.

---

## 3. Commands / tools used
- `pwd`, `ls`, `ls -l`, `ls -lah`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`: Standard POSIX file navigation and stream manipulation commands.
- `>` and `>>`: Output redirection operators for writing and appending.
- `|` and `head -n 5`: Stream piping and line-limiting filter.
- `brew --version`, `brew list`: Inspected macOS Homebrew package manager and installed packages.

## 4. My understanding
The terminal is a powerful text interface to the operating system kernel and filesystem. Mastering basic commands allows rapid inspection and automation without relying on visual file managers. Understanding Unix streams (`stdin`, `stdout`, `stderr`), redirection (`>`, `>>`), and pipelines (`|`) demonstrates the Unix philosophy of combining small, focused tools to build complex data processing workflows.

## 5. Difficulties faced
Accidental overwriting of files can occur if `>` is used instead of `>>`.

## 6. How I resolved them
Always verify destination files before redirection, utilize `cat` to inspect results, and employ backup copies (`cp`) before undertaking non-trivial file modifications.

## 7. Evidence / files
- Mission documentation: `mission-02-terminal/README.md`
- Practice directory: `terminal-practice/notes.txt`, `terminal-practice/notes_archive.txt`

## 8. Commit details
- Staged files: `mission-02-terminal/README.md`, `terminal-practice/notes.txt`, `terminal-practice/notes_archive.txt`
- Commit message: `Complete Terminal and file management mission`
- Verification: Confirmed via `git status` and `git log -1`.
