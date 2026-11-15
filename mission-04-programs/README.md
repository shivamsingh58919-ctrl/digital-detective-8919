# Mission 4 — How programs run

## 1. Task / objective
The objective of Mission 4 is to investigate software translation and execution models:
- Author and execute a minimal Python script (`hello.py`) displaying `"Hello from Python"`.
- Analyze and contrast the architectural differences between **compilers** and **interpreters**.
- Summarize how modern programming languages translate human-readable source code into machine-executable CPU instructions.

## 2. Work completed
- Authored `mission-04-programs/hello.py` containing:
  ```python
  print("Hello from Python")
  ```
- Executed the program using `python3 hello.py` and validated the expected standard output.
- Formulated an in-depth comparative table across four essential dimensions: translation/execution timing, typical artifacts/output, representative languages, and core runtime advantages.
- Provided a clear synthesis explaining program execution pipelines in modern computing.

---

### Task 4.1 — Create and run a Python program
Execution log:
```bash
$ python3 hello.py
Hello from Python
```
The Python 3 runtime successfully parsed the file, compiled the abstract syntax tree into Python bytecode, executed the bytecode in the CPython virtual machine, and emitted the string to the terminal console stream.

---

### Task 4.2 — Compare compiler and interpreter

| Comparison Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translation happens **ahead of time** during a distinct compilation phase before the program can ever run. | Translation occurs **at runtime**, reading, parsing, and carrying out instructions line-by-line or statement-by-statement dynamically. |
| **Typical output** | Produces a standalone, architecture-specific machine code binary executable (e.g., ELF, Mach-O, `.exe`) or intermediate bytecode container (`.class`). | Emits direct program execution side effects and outputs to memory/console without producing a standalone native binary file. |
| **One example** | **C / C++** (compiled via `gcc`/`clang` directly into machine instructions). | **Python (CPython)** or **Ruby** (translates and executes scripts dynamically). |
| **One advantage** | **Maximum execution performance and hardware optimization:** The CPU executes pre-compiled native machine instructions directly with zero translation overhead during runtime. | **High developer agility and rapid prototyping:** Developers can instantly run and test code changes without waiting for time-consuming compile and link cycles. |

---

### Synthesis: The Difference Between Compilers and Interpreters
A compiler transforms the entirety of a programmer's source code into low-level machine code before any execution takes place, creating an independent executable file tailored to the target CPU architecture. In contrast, an interpreter processes instructions directly at runtime, reading and evaluating statements on the fly without generating a standalone native binary. 

While compiled programs offer superior execution speed and lower memory footprints during production, interpreted environments excel during development because code can be tested immediately across multiple operating systems with easier debugging. Modern language engines (such as Python's CPython or Java's JVM) often blend both approaches by compiling source into intermediate bytecode, which is then executed or Just-In-Time (JIT) compiled by an underlying runtime engine.

---

## 3. Commands / tools used
- `python3 hello.py`: Invoked the CPython interpreter to parse, execute, and display the script output.
- Text editor / file tools: Authored source code and structured markdown.

## 4. My understanding
Computer processors only understand sequences of binary electrical signals representing machine opcodes (such as ARM or x86 instructions). Because humans write code in expressive, high-level languages like Python or C, a translation mechanism is mandatory. 

Understanding whether a language is compiled or interpreted clarifies key trade-offs in software engineering: compilation optimizes for raw execution speed and resource efficiency at the cost of build time and platform dependency, whereas interpretation prioritizes flexibility, cross-platform portability, and fast developer feedback loops.

## 5. Difficulties faced
Distinguishing how Python utilizes internal bytecode (`.pyc`) despite being classified primarily as an interpreted language.

## 6. How I resolved them
Researched CPython's execution model and clarified that while Python performs an internal compile step to bytecode, it does not produce standalone CPU machine code; instead, the CPython virtual machine interprets that bytecode line-by-line at runtime, placing it conceptually within interpreted language systems.

## 7. Evidence / files
- Python program: `mission-04-programs/hello.py`
- Documentation and comparative analysis: `mission-04-programs/README.md`

## 8. Commit details
- Staged files: `mission-04-programs/hello.py`, `mission-04-programs/README.md`
- Commit message: `Compare compilers and interpreters`
- Verification: Confirmed via `git status` and `git log -1`.
