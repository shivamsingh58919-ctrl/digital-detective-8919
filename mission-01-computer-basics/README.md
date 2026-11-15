# Mission 1 — Know your computer

## 1. Task / objective
The objective of Mission 1 is to investigate and articulate the fundamental principles of computing:
- Trace a real-world computer task using the **IPOS (Input, Processing, Output, Storage)** cycle.
- Identify and classify common hardware components and software categories (operating systems, application software, and utility software).
- Analyze three embedded or specialized computer-based systems encountered in everyday life outside of standard personal laptops and smartphones.

## 2. Work completed
- Analyzed the complete IPOS cycle for the activity of **"Composing and Saving a Research Document"**.
- Completed a detailed classification table containing four key hardware components and four distinct software systems with their categorization and operational purposes.
- Analyzed three real-world embedded computer systems (Automated Teller Machine, Smart Traffic Signal, and Modern Smart Television) by identifying their core function, primary input mechanisms, and primary output interfaces.
- Formulated clear, original explanations describing the data flow from physical input transducers to volatile memory, processor arithmetic/logic, display visualization, and non-volatile secondary storage.

---

### Task 1.1 — Trace one activity using IPOS
**Chosen Activity:** Composing and saving an academic report in a text processor.

| Stage | What happens in this activity? | Hardware / Component involved |
| :--- | :--- | :--- |
| **Input** | The user presses mechanical keys on the keyboard to enter alphanumeric characters and clicks the mouse/trackpad to select formatting and the "Save" icon. | Keyboard, Trackpad / Optical Mouse |
| **Processing** | The keyboard controller sends electrical scan codes to the CPU via interrupts. The CPU decodes the keystrokes, converts them into character glyph representations (ASCII/Unicode), calculates layout margins, and buffers the updated document state inside fast volatile RAM. | Central Processing Unit (CPU), Primary Memory (RAM) |
| **Output** | The graphics processor (GPU) and display engine render the buffered document characters and cursor onto the monitor in real time, providing immediate visual feedback to the user. | Display Panel / Retina Screen, GPU |
| **Storage** | When the user triggers the "Save" command, the operating system file system converts the document data in RAM into structured filesystem blocks and writes them persistently onto the solid-state drive (SSD). | NVMe Solid-State Drive (SSD) / Flash Memory |

**Detailed Data Flow Description:**
1. Keystrokes generate electrical signals detected by the keyboard controller microcontroller.
2. The operating system kernel receives hardware interrupt requests (IRQs), reads the scan codes, translates them into UTF-8 characters, and pushes them to the active text editor process.
3. The CPU updates the document model residing in volatile RAM.
4. The compositor renders the visual text buffer to the screen at high refresh rates.
5. On executing the write operation, the OS coordinates with the storage controller to commit the data blocks from RAM to non-volatile NAND flash storage cells on the SSD, ensuring the document persists even after powering down.

---

### Task 1.2 — Identify hardware and software

| Item / Software Name | Hardware or Software? | Software Type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| **Mechanical Keyboard** | Hardware | Not applicable | Captures physical user keypresses and converts them to binary scan codes. |
| **Retina Display Monitor** | Hardware | Not applicable | Emits color-calibrated pixels to visually present application GUIs and command text. |
| **Central Processing Unit (Apple M-Series/Intel CPU)** | Hardware | Not applicable | Fetches, decodes, and executes program instructions; conducts arithmetic and logical computations. |
| **Solid-State Drive (SSD)** | Hardware | Not applicable | Stores persistent system files, application packages, and user documents permanently using flash memory. |
| **macOS (Darwin Kernel)** | Software | Operating System Software | Manages hardware abstractions, CPU thread scheduling, memory paging, file systems, and user privileges. |
| **Google Chrome / Safari** | Software | Application Software | Renders HTML/CSS/JavaScript web applications and allows users to browse information across the internet. |
| **Terminal (zsh shell)** | Software | Application / Shell Software | Provides a text-based command-line interface for direct interaction with the OS shell and utility binaries. |
| **Disk Utility (fsck / First Aid)** | Software | Utility Software | Diagnoses file system health, formats partitions, repairs volume structures, and monitors disk integrity. |

---

### Task 1.3 — Computer systems around you

| System | Main Purpose | One Input | One Output |
| :--- | :--- | :--- | :--- |
| **Automated Teller Machine (ATM)** | Dispenses banking cash securely, checks account balances, and accepts cash/check deposits. | Numeric encryption PIN pad (EPP) or chip card reader. | Motorized cash dispenser shutter or thermal receipt printer. |
| **Intelligent Traffic Signal Controller** | Regulates intersection traffic flows safely and manages pedestrian crossing cycles. | Sub-surface inductive electromagnetic vehicle detection loop or pedestrian push-button. | Multi-aspect high-brightness Red/Yellow/Green LED signal heads. |
| **Smart Television System** | Decodes digital streaming video feeds, runs media apps, and reproduces high-fidelity audio/video. | Infrared (IR) / Bluetooth remote control or far-field voice microphone. | 4K HDR display panel and multi-channel integrated soundbar/speakers. |

---

## 3. Commands / tools used
- Text editor / Markdown authoring tools for structured analysis and tabulation.
- Terminal commands (`sw_vers`, `system_profiler`) used conceptually to observe installed hardware and OS specifications.

## 4. My understanding
A computer is fundamentally an automated data-processing machine built on the interplay between hardware and software:
- The **IPOS model** cleanly captures how computers operate: data enters through input peripherals, is manipulated in volatile memory by the processor, is presented via output devices, and is preserved in persistent non-volatile storage.
- Software acts as the instructional intelligence that brings hardware to life:
  - **Operating systems** act as intermediaries managing raw hardware resources and process sandboxing.
  - **Applications** solve specific end-user problems (writing, calculating, browsing).
  - **Utilities** maintain and optimize hardware and OS health.
- Modern life is surrounded by specialized embedded computers that perform targeted real-time tasks using dedicated microcontrollers, sensors, and actuators without resembling a typical PC.

## 5. Difficulties faced
Distinguishing clearly between utility software and application software can sometimes be confusing when applications include internal maintenance features.

## 6. How I resolved them
Clarified the distinction by verifying that application software serves user-centric productivity or entertainment goals, whereas utility software specifically targets the management, optimization, diagnosis, or maintenance of system hardware, files, or operating system infrastructure.

## 7. Evidence / files
- Complete tabular documentation: `mission-01-computer-basics/README.md`
- Referenced architectural model: IPOS Flow Diagram and Hardware/Software Matrix.

## 8. Commit details
- Target file: `mission-01-computer-basics/README.md`
- Commit message: `Complete computer basics and IPOS mission`
- Verification: Confirmed with `git status` and `git log -1`.
