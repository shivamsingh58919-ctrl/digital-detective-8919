# Mission 5 — Numbers and data

## 1. Task / objective
The objective of Mission 5 is to understand data representation in digital systems:
- Perform manual, step-by-step mathematical conversions between decimal (base 10), binary (base 2), and hexadecimal (base 16).
- Programmatically verify each manual conversion using Python's built-in functions.
- Develop, test, and document a working CLI program (`number_converter.py`) that accepts user input and converts decimal integers to binary and hexadecimal.
- Analyze how text characters are digitally stored and encoded via standards like ASCII and UTF-8.

## 2. Work completed
- Worked out all seven manual conversion problems showing complete arithmetic division and positional summation steps.
- Validated all manual calculations in Python 3 using `bin()`, `hex()`, and `int(..., base)`.
- Implemented `mission-05-numbers-data/number_converter.py`, supporting user prompts, error handling, and structured output.
- Tested the converter against four test values (`13`, `25`, `42`, `255`), recording all terminal I/O.
- Explored character encoding, retrieved ASCII code points for `'A'` and `'a'`, and explained why computers require universal character standards like UTF-8 for global symbols.

---

### Task 5.1 — Convert numbers by hand

| Conversion Question | Step-by-Step Working | Final Answer |
| :--- | :--- | :--- |
| **Convert decimal 13 to binary** | Repeated division by 2:<br>• $13 \div 2 = 6$ remainder **1**<br>• $6 \div 2 = 3$ remainder **0**<br>• $3 \div 2 = 1$ remainder **1**<br>• $1 \div 2 = 0$ remainder **1**<br>Reading remainders from bottom to top: `1101`.<br>Check: $8 + 4 + 0 + 1 = 13$. | **`1101₂`** |
| **Convert decimal 25 to binary** | Repeated division by 2:<br>• $25 \div 2 = 12$ remainder **1**<br>• $12 \div 2 = 6$ remainder **0**<br>• $6 \div 2 = 3$ remainder **0**<br>• $3 \div 2 = 1$ remainder **1**<br>• $1 \div 2 = 0$ remainder **1**<br>Reading remainders from bottom to top: `11001`.<br>Check: $16 + 8 + 0 + 0 + 1 = 25$. | **`11001₂`** |
| **Convert binary 1010 to decimal** | Positional expansion (powers of 2):<br>$(1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)$<br>$= 8 + 0 + 2 + 0 = 10$. | **`10₁₀`** |
| **Convert binary 1101 to decimal** | Positional expansion (powers of 2):<br>$(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)$<br>$= 8 + 4 + 0 + 1 = 13$. | **`13₁₀`** |
| **Convert hexadecimal A to decimal** | Hexadecimal digits: $0\text{–}9$, $\text{A}=10$, $\text{B}=11$, $\text{C}=12$, $\text{D}=13$, $\text{E}=14$, $\text{F}=15$.<br>Positional value: $(\text{A} \times 16^0) = 10 \times 1 = 10$. | **`10₁₀`** |
| **Convert hexadecimal 1F to decimal** | Positional expansion (powers of 16):<br>$(1 \times 16^1) + (\text{F} \times 16^0) = (1 \times 16) + (15 \times 1) = 16 + 15 = 31$. | **`31₁₀`** |
| **Convert binary 1111 to hexadecimal** | Grouping 4 bits: `1111`.<br>Summing decimal value: $(1 \times 8) + (1 \times 4) + (1 \times 2) + (1 \times 1) = 15₁₀$.<br>In base 16, decimal value 15 corresponds to the single digit `F`. | **`F₁₆`** (or `0xF`) |

---

### Task 5.2 — Verify using Python

| Conversion Goal | Python Expression Tested | Interactive Python Result | Matches Manual Calculation? |
| :--- | :--- | :--- | :---: |
| Decimal 13 to binary | `bin(13)` | `'0b1101'` | **Yes** (`1101`) |
| Decimal 25 to binary | `bin(25)` | `'0b11001'` | **Yes** (`11001`) |
| Binary 1010 to decimal | `int('1010', 2)` | `10` | **Yes** (`10`) |
| Binary 1101 to decimal | `int('1101', 2)` | `13` | **Yes** (`13`) |
| Hexadecimal A to decimal | `int('A', 16)` | `10` | **Yes** (`10`) |
| Hexadecimal 1F to decimal | `int('1F', 16)` | `31` | **Yes** (`31`) |
| Binary 1111 to hexadecimal | `hex(int('1111', 2))` | `'0xf'` | **Yes** (`F`) |

---

### Task 5.3 — Build a small number converter
Source file: `mission-05-numbers-data/number_converter.py`

#### Test Execution Table

| Test Number (Decimal) | Binary Output | Hexadecimal Output | Observation / Status |
| :---: | :--- | :--- | :--- |
| **`13`** | `0b1101` | `0XD` | Correctly matched manual & Python verification. |
| **`25`** | `0b11001` | `0X19` | Correctly matched manual & Python verification. |
| **`42`** | `0b101010` | `0X2A` | Standard byte representation validated ($32 + 8 + 2 = 42$). |
| **`255`** | `0b11111111` | `0XFF` | Maximum 8-bit unsigned integer boundary ($2^8 - 1$). |

#### Explanation of Python Conversion Functions
- **`bin(x)`**: Takes an integer argument and returns its binary representation formatted as a string prefixed with `0b`. It operates by evaluating the integer's underlying bit positions.
- **`hex(x)`**: Takes an integer argument and returns its lowercase hexadecimal representation formatted as a string prefixed with `0x`. Each hex digit encapsulates exactly 4 bits (a nibble).

---

### Task 5.4 — How is text stored?
- **ASCII decimal codes:**
  - Uppercase letter **`A`**: **`65`** (Binary: `01000001`)
  - Lowercase letter **`a`**: **`97`** (Binary: `01100001`)
  *(Notice that lowercase letters differ by exactly 32, which toggles bit position 5 from 0 to 1).*
- **Why computers need an encoding standard to store text:**
  Computers cannot directly store symbols, glyphs, or letters; their electronic registers and memory cells only store binary electrical charges (0s and 1s). A standardized character encoding defines a globally agreed dictionary mapping each human character to a unique numeric code so text can be reliably saved, transmitted across networks, and rendered identically on any device.
- **Example of a character not part of basic ASCII:**
  The Indian Rupee currency sign **`₹`** (Unicode code point `U+20B9`, encoded as three bytes `0xE0 0x82 0xB9` in UTF-8) or the rocket emoji **`🚀`** (Unicode `U+1F680`). Basic ASCII is restricted to 7 bits ($0\text{–}127$) and only covers standard unaccented English alphanumeric characters and control codes.

---

## 3. Commands / tools used
- `python3 number_converter.py`: Executed the interactive number converter script.
- Python built-in functions: `bin()`, `hex()`, `int()`, `input()`, `ord()`.
- Interactive Python CLI (`python3 -c "..."`) for verification.

## 4. My understanding
At the silicon level, all computing is numerical and binary. Hexadecimal is used extensively by engineers as a compact, human-readable shorthand for binary, where every 4 bits maps directly to 1 hexadecimal digit. Furthermore, text, images, and audio are simply layered abstractions built on top of numeric encodings, underscoring how universal standards like Unicode UTF-8 enable modern global interoperability.

## 5. Difficulties faced
Understanding the positional weighting difference when transitioning between base 2 and base 16.

## 6. How I resolved them
Grouped binary numbers into 4-bit nibbles, which directly correspond to single hexadecimal digits ($0000_2 = 0_{16}$ up to $1111_2 = \text{F}_{16}$), eliminating confusion during larger conversions.

## 7. Evidence / files
- Python converter script: `mission-05-numbers-data/number_converter.py`
- Mission report: `mission-05-numbers-data/README.md`

## 8. Commit details
- Staged files: `mission-05-numbers-data/number_converter.py`, `mission-05-numbers-data/README.md`
- Commit message: `Build number converter and practise data representation`
- Verification: Confirmed with `git status` and `git log -1`.
