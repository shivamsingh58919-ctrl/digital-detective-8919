# The Digital Detective: Explore Your Computer • Build a Mini System Report

**Diwali Independent Learning Assignment**

## Student Information

| Field | Details |
| :--- | :--- |
| **Name** | [Student Name] |
| **USN** | [USN - Ending in 8919] |
| **Campus / Section** | Computer Science & Engineering |
| **GitHub Username** | shivamsingh58919-ctrl |
| **GitHub Repository Name** | digital-detective-8919 |
| **GitHub Repository URL** | https://github.com/shivamsingh58919-ctrl/digital-detective-8919 |

> **Privacy Note:** Personal and sensitive identifiers (such as local machine usernames, device serial numbers, network Wi-Fi names, and private IP addresses) have been systematically redacted or omitted in accordance with assignment safety guidelines.

---

## Assignment Overview & Purpose

This repository houses the complete, self-directed exploration of computing fundamentals designed for the *Diwali Independent Learning Assignment: The Digital Detective*. Through nine structured, hands-on missions, this project explores the low-level and system-level operations of modern computers, command-line interfaces, operating system internals, program translation, data representation, distributed version control, and computer networking.

### Core Topics Explored:
1. **Workspace and Environment Architecture:** Initializing Git repositories, configuring development tooling (Python 3, Git), and establishing clean modular project layouts.
2. **Computer Fundamentals & the IPOS Model:** Analyzing data flow across Input, Processing, Output, and Storage, alongside hardware and software classification.
3. **Command-Line Interface Mastery:** Shell navigation, directory operations, non-destructive file editing, flags, and Unix pipelines.
4. **Operating System Internals:** Process lifecycle, Process IDs (PIDs), POSIX file permissions (`rwx`), absolute vs. relative paths, and kernel subsystems.
5. **Program Execution Paradigms:** Source code translation, CPython execution flow, and an architectural comparison of compilers versus interpreters.
6. **Data Representation & Encodings:** Mathematical conversions between decimal (base 10), binary (base 2), and hexadecimal (base 16), verified via Python 3 and ASCII/UTF-8 character encodings.
7. **Version Control & GitHub Collaboration:** Git status inspection, the index/staging area, atomic commits, isolated feature branching (`update-about`), and Pull Request reviews.
8. **Computer Networking & Web Communication:** Network topologies (LAN, MAN, WAN), DNS resolution, routing, protocols, packet switching, and the complete 7-step website request lifecycle.
9. **Final Verification & Auditing:** Comprehensive repository auditing, submission checklist validation, and quality control.

Each mission is documented in its dedicated folder using a consistent 9-point reporting standard. Each mission was completed, verified, and committed sequentially with independent, meaningful commit messages.

---

## Mission Index

| Mission | Focus Area | Status | Folder Link |
| :---: | :--- | :---: | :--- |
| **0** | Repository and workspace setup | Completed | [mission-00-setup](./mission-00-setup/README.md) |
| **1** | Computer fundamentals and IPOS | Completed | [mission-01-computer-basics](./mission-01-computer-basics/README.md) |
| **2** | Terminal and file management | Completed | [mission-02-terminal](./mission-02-terminal/README.md) |
| **3** | Operating system, processes and permissions | Completed | [mission-03-operating-system](./mission-03-operating-system/README.md) |
| **4** | How programs run (Python test & compiler vs. interpreter) | Completed | [mission-04-programs](./mission-04-programs/README.md) |
| **5** | Number systems, Python and text encoding | Completed | [mission-05-numbers-data](./mission-05-numbers-data/README.md) |
| **6** | Git, GitHub, branches and Pull Requests | Completed | [mission-06-git-github](./mission-06-git-github/README.md) |
| **7** | Computer networks | Completed | [mission-07-networking](./mission-07-networking/README.md) |
| **8** | Final review and submission | Completed | [mission-08-final-report](./mission-08-final-report/README.md) |

---

## My Learning

Throughout this assignment, several core computing paradigms have been clarified through hands-on practice:
1. **The Unix Philosophy & Stream Pipeline Power:** Discovered how combining independent single-purpose CLI utilities using pipes (`|`) and redirection (`>`, `>>`) allows flexible data manipulation without graphical overhead.
2. **Operating System Resource Isolation:** Understood how the OS kernel schedules CPU threads, protects memory spaces between distinct processes using PIDs, and enforces POSIX access control permissions (`rwx`).
3. **Low-Level Data Representation:** Gained deep appreciation for how human ideas (text, numbers) are reduced to binary patterns (bits and bytes) and hexadecimal representations, and how standards like UTF-8 allow global text interchange.
4. **Collaborative Software Engineering:** Experienced the power of isolated branching and Pull Requests for peer review, ensuring that master/main branches remain clean and deployable at all times.
5. **Decoupled Network Architecture:** Learned how the internet operates through modular protocol layers (DNS for naming, IP for routing, TCP for transport, HTTPS for presentation), enabling global scale and fault tolerance.

---

## Instructions for Running the Python Number Converter

The interactive number conversion tool is located in `mission-05-numbers-data/`. To execute the program:

```bash
# Navigate to the mission directory
cd mission-05-numbers-data

# Run using Python 3
python3 number_converter.py
```

Follow the on-screen prompt to enter any positive decimal integer. The program will output the binary (`bin()`) and hexadecimal (`hex()`) representations.

---

## Commit & Workflow Policy

- Each mission was executed and documented in strict sequential order.
- Every mission folder includes its own `README.md` adhering to the required 9-point structure.
- Distinct and descriptive Git commit messages record milestones across the repository history.
