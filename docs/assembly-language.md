# Assembly Language

## Overview

The CPU uses a custom assembly language based on the project's MIPS-inspired ISA.

Assembly programs are written in:

```text
assembler/program.asm
```

The Python assembler translates the source code into 32-bit machine instructions stored in:

```text
assembler/program.hex
```

The generated machine code can then be loaded into the instruction ROM of the CPU.

---

## Basic Syntax

Each instruction is written on a separate line.

Operands are separated by spaces.

```asm
instruction operand1 operand2 operand3
```

For example:

```asm
add $t0 $t1 $t2
```

means:

```text
$t0 = $t1 + $t2
```

No commas are required between operands.

---

## Comments

Comments begin with `#`.

Everything following `#` on the same line is ignored by the assembler.

Example:

```asm
li $t0 10      # Load 10 into $t0
inc $t0        # Increment $t0
```

Empty lines are also ignored.

---

## Registers

Integer registers use MIPS-inspired symbolic names.

Examples:

```text
$zero
$at

$v0
$v1

$a0 - $a3

$t0 - $t9

$s0 - $s7

$k0
$k1

$gp
$sp
$fp
$ra
```

Example:

```asm
add $t0 $t1 $t2
```

The first register is the destination:

```text
$t0 = $t1 + $t2
```

---

## Immediate Values

Immediate values are written directly after the register operands.

Example:

```asm
addi $t0 $t1 10
```

means:

```text
$t0 = $t1 + 10
```

Integer literals can also be written using Python-compatible prefixes where supported by the assembler.

For example:

```asm
li $t0 10
li $t1 0xFF
```

---

# Arithmetic

## Addition

```asm
add $t0 $t1 $t2
```

```text
$t0 = $t1 + $t2
```

With an immediate value:

```asm
addi $t0 $t1 10
```

---

## Subtraction

```asm
sub $t0 $t1 $t2
```

```text
$t0 = $t1 - $t2
```

Immediate version:

```asm
subi $t0 $t1 10
```

---

## Multiplication

```asm
mul $t0 $t1 $t2
```

Immediate version:

```asm
muli $t0 $t1 10
```

Multiplication is executed by the dedicated combinational multiplier in the Integer Unit.

---

## Division

```asm
div $t0 $t1 $t2
```

Immediate version:

```asm
divi $t0 $t1 10
```

Division is executed by the dedicated combinational divider.

---

## Modulo

```asm
mod $t0 $t1 $t2
```

calculates the remainder of an integer division.

The immediate version is:

```asm
modi $t0 $t1 10
```

---

# Logical Operations

The assembly language supports bitwise operations.

```asm
and  $t0 $t1 $t2
or   $t0 $t1 $t2
xor  $t0 $t1 $t2
nand $t0 $t1 $t2
nor  $t0 $t1 $t2
xnor $t0 $t1 $t2
```

Immediate variants are available for selected operations:

```asm
andi $t0 $t1 0xFF
ori  $t0 $t1 0xFF
xori $t0 $t1 0xFF
```

---

# Comparisons

Comparison instructions write their result to the destination register.

Examples:

```asm
eq  $t0 $t1 $t2
ne  $t0 $t1 $t2
slt $t0 $t1 $t2
sgt $t0 $t1 $t2
sle $t0 $t1 $t2
sge $t0 $t1 $t2
```

For example:

```asm
slt $t0 $t1 $t2
```

tests whether:

```text
$t1 < $t2
```

and writes the comparison result to `$t0`.

---

# Shift Operations

Register-based shifts:

```asm
srlv $t0 $t1 $t2
sllv $t0 $t1 $t2
```

Immediate shift and rotate operations include:

```asm
srl $t0 $t1 4
sll $t0 $t1 4
srr $t0 $t1 4
slr $t0 $t1 4
sra $t0 $t1 4
sla $t0 $t1 4
```

---

# Memory Access

The CPU supports load and store operations for accessing data RAM.

## Load Word

```asm
lw $t0 $t1 4
```

uses `$t1` as the base register and `4` as the immediate offset.

The loaded value is written to `$t0`.

## Store Word

```asm
sw $t0 $t1 4
```

stores the value from `$t0` using `$t1` as the base register and `4` as the immediate offset.

---

# Labels

Labels can be used to identify positions in a program.

A label is written using a name followed by `:`.

Example:

```asm
loop:
    dec $t0
    bne $t0 $zero loop
```

Labels themselves do not generate machine instructions.

The assembler resolves labels into instruction addresses before generating the final machine code.

---

# Branches

Conditional branches have the general form:

```asm
branch register1 register2 label
```

Available branch instructions include:

```asm
beq
bne
blt
bgt
ble
bge
```

Example:

```asm
beq $t0 $t1 equal
```

A more complete example:

```asm
li $t0 10
li $t1 10

beq $t0 $t1 equal

li $t2 0
j end

equal:
li $t2 1

end:
```

---

# Jumps

An unconditional jump is written as:

```asm
j label
```

Example:

```asm
loop:
    inc $t0
    j loop
```

---

# Pseudo-Instructions

The assembler implements several convenience instructions that are translated into native instructions.

## Load Immediate

```asm
li $t0 10
```

is translated using `addi` with `$zero` as the source register.

---

## NOT

```asm
not $t0 $t1
```

is implemented using a native `nor` operation.

---

## Negation

```asm
neg $t0 $t1
```

is implemented as subtraction from zero.

---

## Increment

```asm
inc $t0
```

is equivalent to:

```asm
addi $t0 $t0 1
```

---

## Decrement

```asm
dec $t0
```

is equivalent to:

```asm
subi $t0 $t0 1
```

---

# Example Program

A simple loop can be written as:

```asm
li $t0 10
li $t1 0

loop:
    add $t1 $t1 $t0
    dec $t0
    bne $t0 $zero loop
```

The assembler removes comments and labels and converts the remaining instructions into their corresponding 32-bit machine instructions.

---

# Floating-Point Syntax

> **Status:** Floating-point ISA and assembler support are under development together with the FPU hardware.

Floating-point registers use the names:

```text
$f0 - $f31
```

Floating-point arithmetic follows the same destination-first convention.

Example:

```asm
fadd $f0 $f1 $f2
```

represents:

```text
$f0 = $f1 + $f2
```

Defined floating-point operations include:

```asm
fadd
fsub
fmul
fdiv
fsqrt

feq
fne
flt
fgt
fle
fge

fabs
fneg

itof
ftoi
mtf
mff

flw
fsw
```

---

## Floating-Point Immediate

The assembler provides the pseudo-instruction:

```asm
fli $f0 2.5
```

The decimal number is converted into its 32-bit IEEE-754 single-precision representation.

The assembler then expands `fli` into multiple native instructions required to construct the 32-bit value and transfer it into the floating-point register.

---

## Floating-Point Memory Access

Floating-point values can use the defined load/store syntax:

```asm
flw $f0 $t0 0
fsw $f0 $t0 0
```

Here `$t0` is an integer base-address register and `$f0` is a floating-point register.

---

# Source and Machine-Code Files

The assembly source program is stored in:

```text
program.asm
```

After running the assembler, the generated machine code is written to:

```text
program.hex
```

For example, assembly source such as:

```asm
fli $f0 2.5
li $t0 10

fsw $f0 $t0 0
flw $f1 $t0 0
```

is translated into a sequence of 32-bit hexadecimal machine instructions.

The generated `program.hex` is then used as the program for the CPU's instruction ROM.