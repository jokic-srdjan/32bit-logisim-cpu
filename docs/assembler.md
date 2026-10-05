# Python Assembler

## Overview

The project includes a custom Python assembler for the CPU's MIPS-inspired instruction set.

The assembler translates assembly source code into 32-bit hexadecimal machine instructions that can be loaded into the instruction ROM of the Logisim CPU.

The complete workflow is:

```text
program.asm
     │
     ▼
   main.py
     │
     ├── Preprocessing
     │     ├── Remove comments
     │     ├── Remove empty lines
     │     └── Resolve labels
     │
     ▼
 assembler.py
     │
     ├── instructions.py
     └── registers.py
     │
     ▼
32-bit instruction encoding
     │
     ▼
 program.hex
     │
     ▼
Logisim Instruction ROM
     │
     ▼
CPU execution
```

---

## Project Structure

The assembler consists of the following files:

```text
assembler/
├── main.py
├── assembler.py
├── utils.py
├── program.asm
├── program.hex
└── dictionaries/
    ├── instructions.py
    └── registers.py
```

### `main.py`

`main.py` is the entry point of the assembler.

It:

1. opens `program.asm`
2. removes comments and empty lines
3. resolves labels
4. passes each instruction to the assembler
5. writes the generated machine code to `program.hex`

### `assembler.py`

`assembler.py` performs the actual instruction encoding.

It parses each instruction and generates the corresponding 32-bit machine instruction according to the custom ISA.

It supports:

- R-Type instructions
- I-Type instructions
- J-Type instructions
- pseudo-instructions
- integer registers
- floating-point register encodings

### `utils.py`

`utils.py` contains preprocessing functions used before instruction encoding.

These functions handle:

- comments
- empty lines
- labels
- creation of the final instruction list
- conversion of binary instructions to hexadecimal representation

### `instructions.py`

This file defines the instruction set.

Each instruction contains information such as:

```text
instruction type
operand format
opcode
function code
```

Example conceptually:

```python
"add": {
    "itype": "R",
    "format": "RRR",
    "ifunction": "001000"
}
```

### `registers.py`

This file maps symbolic register names to their 5-bit addresses.

For example:

```text
$zero → 00000
$at   → 00001
$t0   → 01000
$t1   → 01001
...
$ra   → 11111
```

---

# Using the Assembler

## 1. Write the Assembly Program

The program to be assembled is written in:

```text
assembler/program.asm
```

For example:

```asm
li $t0 10
li $t1 20

add $t2 $t0 $t1
```

The file can contain comments and labels.

Example:

```asm
# Initialize counter
li $t0 10

loop:
    dec $t0
    bne $t0 $zero loop
```

---

## 2. Open a Terminal

Navigate to the assembler directory.

From the project root:

```bash
cd assembler
```

The working directory should contain:

```text
main.py
assembler.py
utils.py
program.asm
dictionaries/
```

---

## 3. Run the Assembler

Execute:

```bash
python main.py
```

`main.py` reads the contents of `program.asm` and passes the instructions through the assembler.

No external Python packages are required.

---

## 4. Machine-Code Generation

For every native instruction, the assembler generates a 32-bit binary instruction according to the ISA.

The binary instruction is then converted into an 8-digit hexadecimal representation.

For example, a 32-bit instruction may be written as:

```text
2008000A
```

Each line in `program.hex` represents one 32-bit machine instruction.

---

## 5. Output File

Running the assembler creates or overwrites:

```text
program.hex
```

A generated file may look like:

```text
5C014020
0C210000
0020003A
2008000A
F9000000
FD010000
```

The assembly source remains in `program.asm`, while `program.hex` represents the program in the machine-code format required by the CPU.

---

# Loading the Program into the CPU

After assembly, the generated machine code must be loaded into the instruction ROM in Logisim Evolution.

The workflow is:

```text
program.asm
      ↓
python main.py
      ↓
program.hex
      ↓
Instruction ROM
      ↓
CPU
```

After the machine code has been loaded into ROM, the CPU can execute the program.

The Program Counter selects the current ROM address, and the corresponding 32-bit instruction is passed to the Control Unit.

The Control Unit decodes the instruction and generates the signals required for the register file, execution units, RAM and Program Counter.

---

# Pseudo-Instructions

The assembler provides pseudo-instructions to make programs easier to write.

Pseudo-instructions do not necessarily correspond directly to a single instruction implemented in hardware.

For example:

```
li $t0 10
```

is translated using an immediate arithmetic instruction with `$zero` as its source.

Other pseudo-instructions include:

```
not
neg
inc
dec
fli
```

Some pseudo-instructions generate one machine instruction, while others may expand into multiple machine instructions.

---

# Floating-Point Immediate Values

The assembler already contains support for converting decimal floating-point constants into IEEE-754 single-precision representations.

For example:

```asm
fli $f0 2.5
```

The assembler:

1. converts `2.5` into its IEEE-754 32-bit representation
2. separates the value into upper and lower 16-bit parts
3. generates instructions to construct the 32-bit value
4. transfers the bit pattern into the floating-point register

Therefore, one assembly pseudo-instruction can generate multiple machine instructions.

---

# Example

The current example program:

```asm
fli $f0 2.5
li $t0 10

fsw $f0 $t0 0
flw $f1 $t0 0
```

is translated into:

```text
5C014020
0C210000
0020003A
2008000A
F9000000
FD010000
```

Notice that four assembly instructions result in six machine instructions because `fli` expands into multiple native instructions.

---

# Important Notes

`program.asm` is currently the fixed input filename used by `main.py`.

`program.hex` is currently the fixed output filename.

Running:

```bash
python main.py
```

therefore overwrites the existing `program.hex`.

The source program should always be preserved in `program.asm` or as a separate `.asm` example file.

For the exact syntax and semantics of the assembly language, see:

```text
assembly-language.md
```

For instruction encodings, opcodes and function codes, see:

```text
isa.md
```

For the processor hardware, see:

```text
architecture.md
```