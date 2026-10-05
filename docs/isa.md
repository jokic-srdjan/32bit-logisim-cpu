# Instruction Set Architecture

## Overview

The CPU uses a custom **32-bit MIPS-inspired Instruction Set Architecture (ISA)**.

Each machine instruction is 32 bits wide. The architecture uses three primary instruction types:

- R-Type
- I-Type
- J-Type

The ISA defines integer arithmetic, logic, comparison, shift, memory and control-flow instructions. Floating-point instruction encodings are also defined, while the corresponding hardware implementation is still under development.

---

## Instruction Formats

### R-Type

R-Type instructions are primarily used for register-to-register operations.

```text
31          26 25      21 20      16 15      11 10       6 5        0
+-------------+----------+----------+----------+----------+----------+
|   opcode    |    rs    |    rt    |    rd    |  shamt   | function |
+-------------+----------+----------+----------+----------+----------+
     6 bit       5 bit      5 bit      5 bit      5 bit      6 bit
```

For the currently defined R-Type instructions, the opcode is `000000` and the operation is selected using the 6-bit function field.

Example:

```asm
add $t0 $t1 $t2
```

Meaning:

```text
$t0 = $t1 + $t2
```

---

### I-Type

I-Type instructions use a 16-bit immediate value.

```text
31          26 25      21 20      16 15                         0
+-------------+----------+----------+-----------------------------+
|   opcode    |    rs    |    rt    |          immediate          |
+-------------+----------+----------+-----------------------------+
     6 bit       5 bit      5 bit              16 bit
```

Example:

```asm
addi $t0 $t1 10
```

Meaning:

```text
$t0 = $t1 + 10
```

---

### J-Type

J-Type instructions are used for unconditional jumps.

```text
31          26 25                                             0
+-------------+------------------------------------------------+
|   opcode    |                    address                     |
+-------------+------------------------------------------------+
     6 bit                         26 bit
```

Example:

```asm
j loop
```

---

# Integer Instructions

## Arithmetic

| Instruction | Type | Function / Opcode | Syntax | Operation |
|---|---|---|---|---|
| `add` | R | `001000` | `add rd rs rt` | rd = rs + rt |
| `sub` | R | `001001` | `sub rd rs rt` | rd = rs - rt |
| `mul` | R | `001010` | `mul rd rs rt` | Integer multiplication |
| `div` | R | `001011` | `div rd rs rt` | Integer division |
| `mod` | R | `001100` | `mod rd rs rt` | Integer remainder |
| `addi` | I | `001000` | `addi rt rs imm` | rt = rs + immediate |
| `subi` | I | `001001` | `subi rt rs imm` | rt = rs - immediate |
| `muli` | I | `001010` | `muli rt rs imm` | Integer multiplication with immediate |
| `divi` | I | `001011` | `divi rt rs imm` | Integer division with immediate |
| `modi` | I | `001100` | `modi rt rs imm` | Integer remainder with immediate |

---

## Logic

| Instruction | Type | Function / Opcode | Operation |
|---|---|---|---|
| `and` | R | `000001` | Bitwise AND |
| `or` | R | `000011` | Bitwise OR |
| `xor` | R | `000100` | Bitwise XOR |
| `nand` | R | `000101` | Bitwise NAND |
| `nor` | R | `000110` | Bitwise NOR |
| `xnor` | R | `000111` | Bitwise XNOR |
| `andi` | I | `000001` | AND with immediate |
| `ori` | I | `000011` | OR with immediate |
| `xori` | I | `000100` | XOR with immediate |

---

## Comparison

| Instruction | Function | Operation |
|---|---|---|
| `eq` | `010000` | rs == rt |
| `ne` | `010001` | rs != rt |
| `slt` | `010010` | rs < rt |
| `sgt` | `010011` | rs > rt |
| `sle` | `010100` | rs <= rt |
| `sge` | `010101` | rs >= rt |

Comparison instructions use the R-Type `RRR` format. The comparison result is written to the destination register.

---

## Shift Operations

### Register-based

| Instruction | Function | Operation |
|---|---|---|
| `srlv` | `011000` | Variable right shift |
| `sllv` | `011001` | Variable left shift |

### Immediate

| Instruction | Opcode |
|---|---|
| `srl` | `011000` |
| `sll` | `011001` |
| `srr` | `011010` |
| `slr` | `011011` |
| `sra` | `011100` |
| `sla` | `011101` |

---

## Memory Instructions

| Instruction | Opcode | Syntax | Description |
|---|---|---|---|
| `sw` | `011110` | `sw rt rs offset` | Store word |
| `lw` | `011111` | `lw rt rs offset` | Load word |

Memory instructions use an integer register as the base address together with a 16-bit immediate offset.

---

## Branch Instructions

| Instruction | Opcode | Condition |
|---|---|---|
| `beq` | `010000` | Equal |
| `bne` | `010001` | Not equal |
| `blt` | `010010` | Less than |
| `bgt` | `010011` | Greater than |
| `ble` | `010100` | Less than or equal |
| `bge` | `010101` | Greater than or equal |

Example:

```asm
beq $t0 $t1 equal
```

Labels are resolved by the assembler before machine-code generation.

---

## Jump

| Instruction | Type | Opcode |
|---|---|---|
| `j` | J | `000010` |

Example:

```asm
j loop
```

---

## HI / LO Instructions

The ISA provides dedicated instructions for accessing the HI and LO registers.

| Instruction | Function | Description |
|---|---|---|
| `mfhi` | `011010` | Move from HI |
| `mflo` | `011011` | Move from LO |
| `mthi` | `011100` | Move to HI |
| `mtlo` | `011101` | Move to LO |

---

## Load Upper Immediate

```asm
lui $t0 immediate
```

Opcode:

```text
010111
```

`lui` is used to place a 16-bit immediate value into the upper portion of a 32-bit value.

---

# Registers

## Integer Registers

The CPU provides 32 addressable integer registers using 5-bit register addresses.

| Register | Address | Register | Address |
|---|---|---|---|
| `$zero` | `00000` | `$s0` | `10000` |
| `$at` | `00001` | `$s1` | `10001` |
| `$v0` | `00010` | `$s2` | `10010` |
| `$v1` | `00011` | `$s3` | `10011` |
| `$a0` | `00100` | `$s4` | `10100` |
| `$a1` | `00101` | `$s5` | `10101` |
| `$a2` | `00110` | `$s6` | `10110` |
| `$a3` | `00111` | `$s7` | `10111` |
| `$t0` | `01000` | `$t8` | `11000` |
| `$t1` | `01001` | `$t9` | `11001` |
| `$t2` | `01010` | `$k0` | `11010` |
| `$t3` | `01011` | `$k1` | `11011` |
| `$t4` | `01100` | `$gp` | `11100` |
| `$t5` | `01101` | `$sp` | `11101` |
| `$t6` | `01110` | `$fp` | `11110` |
| `$t7` | `01111` | `$ra` | `11111` |

The naming convention is inspired by MIPS, while the instruction set and processor implementation are custom.

---

# Pseudo-Instructions

The assembler provides additional pseudo-instructions that are translated into native machine instructions.

Examples include:

```asm
li $t0 10
not $t0 $t1
neg $t0 $t1
inc $t0
dec $t0
```

These instructions simplify assembly programming without requiring additional hardware instructions.

For example:

```asm
li $t0 10
```

is assembled using an `addi` instruction with `$zero` as the source register.

---

# Floating-Point ISA Extension

> **Status:** ISA and assembler support are under development. Full hardware integration of the Floating-Point Unit is not yet complete.

The architecture reserves 32 floating-point registers:

```text
$f0 - $f31
```

Each floating-point register uses a 5-bit address.

## Floating-Point Arithmetic

| Instruction | Function | Operation |
|---|---|---|
| `fadd` | `101000` | Floating-point addition |
| `fsub` | `101001` | Floating-point subtraction |
| `fmul` | `101010` | Floating-point multiplication |
| `fdiv` | `101011` | Floating-point division |
| `fsqrt` | `101100` | Floating-point square root |

## Floating-Point Comparison

| Instruction | Function |
|---|---|
| `feq` | `110000` |
| `fne` | `110001` |
| `flt` | `110010` |
| `fgt` | `110011` |
| `fle` | `110100` |
| `fge` | `110101` |

Comparison results are written to an integer register.

## Conversion and Data Transfer

| Instruction | Function | Description |
|---|---|---|
| `itof` | `111000` | Integer to floating point |
| `ftoi` | `111001` | Floating point to integer |
| `mtf` | `111010` | Move integer bit pattern to float register |
| `mff` | `111011` | Move float bit pattern to integer register |
| `fabs` | `111100` | Floating-point absolute value |
| `fneg` | `111101` | Floating-point negation |

## Floating-Point Memory

| Instruction | Opcode | Description |
|---|---|---|
| `fsw` | `111110` | Store floating-point word |
| `flw` | `111111` | Load floating-point word |

The assembler also provides:

```asm
fli $f0 2.5
```

as a pseudo-instruction for loading an IEEE-754 single-precision floating-point value into a floating-point register.

The assembler converts the decimal value into its 32-bit IEEE-754 representation and expands the pseudo-instruction into the required native instructions.