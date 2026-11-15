# Mission 3 — Understand the operating system

## 1. Task / objective
The objective of Mission 3 is to examine the core mechanisms and responsibilities of the operating system:
- Inspect system properties, user environment, and storage capacity using terminal utilities while maintaining privacy standards.
- Understand operating system processes, their lifecycles, and process identifiers (PIDs).
- Differentiate between absolute and relative file paths, and interpret POSIX file permission modes (`r`, `w`, `x`).
- Detail the six primary responsibilities of a modern operating system with practical examples.

## 2. Work completed
- Explored OS details, active user identity, storage metrics, and process tables.
- Analyzed the concept of a process and the function of the Process ID (PID).
- Navigated between directory levels to observe path transformations, defining relative vs. absolute paths with assignment folder references.
- Examined POSIX permissions for `terminal-practice/notes.txt` (`-rw-r--r--`), analyzing owner, group, and world rights.
- Completed an in-depth analytical table detailing the six core operating system management duties.

---

### Task 3.1 — Explore your operating system

| Information Explored | What it tells you | Your Observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Identifies the OS kernel name, kernel architecture, OS distribution, release version, and build identifier. | `macOS 26.6.2 (Darwin arm64, Build 25G83)` running on Apple Silicon architecture. |
| **Current account identity** | Displays the username of the active user session executing commands in the shell. | `[redacted-user]` (POSIX UID 501, Primary Group: `staff`). |
| **Available and used storage** | Shows filesystem partitions, total storage volume capacity, bytes utilized, available disk space, and mount points. | Root volume (`/` on `/dev/disk3s3s1` APFS): Total: `460 GiB`, Used: `12 GiB`, Available: `351 GiB` (4% capacity utilized). |
| **System activity snapshot** | Displays a real-time table of executing system processes, CPU consumption, memory allocation, and process states. | Active scheduler states: ~380 total processes running/sleeping, low overall CPU load, core services managed by `launchd` (PID 1). |

---

### Task 3.2 — Understand processes
- **What is a process?**
  A process is an active instance of a computer program in execution. Unlike passive code residing on storage, a process has an allocated region of memory (address space including code, data, heap, and stack), active program counter registers, execution threads, and operating system resources (such as open file descriptors and network sockets).
- **What does the PID column represent?**
  The **PID (Process Identifier)** is a unique integer value assigned by the operating system kernel whenever a new process is spawned. The kernel uses the PID to track, schedule, prioritize, manage permissions for, and terminate the process.
- **Two examples of processes running on this computer:**
  1. `zsh` (Interactive shell process responsible for parsing and executing terminal commands).
  2. `WindowServer` (macOS compositing engine process responsible for rendering windows, desktop UI, and screen updates).

---

### Task 3.3 — Understand paths and permissions

#### Paths: Absolute vs. Relative
- **Absolute Path:** The complete, unambiguous location of a file or folder starting from the root of the filesystem (`/`). It is independent of the current working directory.
  - *Example:* `/Users/[redacted-user]/.gemini/antigravity/scratch/digital-detective-8919/terminal-practice/notes.txt`
- **Relative Path:** The location of a file or folder defined relative to the shell's current working directory.
  - *Example:* If currently located in `mission-03-operating-system/`, the relative path to the practice file is `../terminal-practice/notes.txt`.

#### Permissions Breakdown
Inspecting `terminal-practice/notes.txt` using `ls -l`:
```text
-rw-r--r--  1 [redacted-user]  staff  93 Nov 15 20:39 notes.txt
```

| Permission Character | Meaning | Applied to `notes.txt` |
| :---: | :--- | :--- |
| `r` (Read) | Grants permission to open, view, or stream file contents. | **Allowed** for Owner (`rw-`), Group (`r--`), and Others (`r--`). |
| `w` (Write) | Grants permission to modify, overwrite, append, or truncate the file. | **Allowed** only for Owner (`rw-`). Denied for Group and Others. |
| `x` (Execute) | Grants permission to run the file as an executable program or traverse a directory. | **Denied** for Owner, Group, and Others (it is a standard text file). |

**Owner Permission Analysis:** The owner has `rw-` permissions, meaning the owner can read and write to `notes.txt`, but cannot execute it.

---

### Task 3.4 — Explain operating-system responsibilities

| OS Responsibility | Your Explanation | Concrete Example |
| :--- | :--- | :--- |
| **Process Management** | Allocates CPU time among concurrent programs using preemptive scheduling algorithms; creates, pauses, resumes, and terminates processes. | Context-switching the CPU rapidly between an active Python script and background music playback so both run smoothly. |
| **Memory Management** | Allocates, tracks, and isolates virtual memory spaces (RAM) for processes, paging unused blocks to swap space and preventing memory corruption. | Preventing a malfunctioning web browser tab from overwriting memory belonging to the terminal shell. |
| **Device Management** | Interfaces with peripheral hardware devices using specialized device drivers, buffering input/output streams, and handling hardware interrupts. | Translating raw USB/Bluetooth mouse optical sensor coordinates into OS cursor position events. |
| **File Management** | Implements the hierarchical filesystem structure, managing directory tables, file creation/deletion, metadata, and disk block allocation. | Organizing directory nodes on an APFS/ext4 drive and mapping filenames to specific storage blocks. |
| **User Interface / Shell** | Delivers an interface for human users to command the system, either via graphical user interfaces (GUI) or command-line shells (CLI). | Providing the `zsh` terminal command interpreter and the graphical desktop window manager. |
| **Security and Permissions** | Enforces user authentication, process isolation, access control lists (ACLs), and filesystem permissions to safeguard resources. | Blocking non-administrative user accounts from altering protected operating system files in `/System` or `/etc`. |

---

## 3. Commands / tools used
- `uname -sm`: Identified kernel name and CPU architecture.
- `sw_vers`: Extracted macOS distribution version and build identifier.
- `df -h /`: Assessed filesystem disk usage and available storage in human-readable gigabytes.
- `ls -l`: Inspected file metadata and POSIX permission bits.
- `cd` and `pwd`: Verified relative vs. absolute directory navigation.

## 4. My understanding
The operating system is the master resource manager of the computer. Without it, software programs would have to directly interface with individual silicon chips, storage blocks, and memory addresses. By abstracting hardware behind standardized system calls, the OS enables concurrent execution (multitasking), sandboxed memory security, structured file persistence, and safe user interactions.

## 5. Difficulties faced
Accessing low-level process tables directly via command-line tools like `ps` and `top` inside sandboxed environments can trigger system access warnings.

## 6. How I resolved them
Consulted standard POSIX diagnostic practices and cross-verified system processes safely using standard macOS environment tools and built-in system inspection documentation while keeping private usernames redacted.

## 7. Evidence / files
- Complete system report: `mission-03-operating-system/README.md`
- Target permission inspection file: `terminal-practice/notes.txt`

## 8. Commit details
- Staged file: `mission-03-operating-system/README.md`
- Commit message: `Document operating system and file management`
- Verification: Confirmed via `git status` and `git log -1`.
