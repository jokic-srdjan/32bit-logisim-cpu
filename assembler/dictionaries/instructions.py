instructions = {

    # =========================================================
    # R-TYPE INTEGER LOGIC
    # format RRR = rd rs rt
    # =========================================================

    "and": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "000001"
    },

    "or": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "000011"
    },

    "xor": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "000100"
    },

    "nand": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "000101"
    },

    "nor": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "000110"
    },

    "xnor": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "000111"
    },


    # =========================================================
    # R-TYPE INTEGER ARITHMETIC
    # =========================================================

    "add": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "001000"
    },

    "sub": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "001001"
    },

    "mul": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "001010"
    },

    "div": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "001011"
    },

    "mod": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "001100"
    },


    # =========================================================
    # R-TYPE INTEGER COMPARE
    # =========================================================

    "eq": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "010000"
    },

    "ne": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "010001"
    },

    "slt": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "010010"
    },

    "sgt": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "010011"
    },

    "sle": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "010100"
    },

    "sge": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "010101"
    },


    # =========================================================
    # R-TYPE VARIABLE SHIFT
    # =========================================================

    "srlv": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "011000"
    },

    "sllv": {
        "itype": "R",
        "format": "RRR",
        "ifunction": "011001"
    },


    # =========================================================
    # R-TYPE HI / LO
    #
    # RD = destination register only
    # RS = source register only
    # =========================================================

    "mfhi": {
        "itype": "R",
        "format": "RD",
        "ifunction": "011010"
    },

    "mflo": {
        "itype": "R",
        "format": "RD",
        "ifunction": "011011"
    },

    "mthi": {
        "itype": "R",
        "format": "RS",
        "ifunction": "011100"
    },

    "mtlo": {
        "itype": "R",
        "format": "RS",
        "ifunction": "011101"
    },


    # =========================================================
    # R-TYPE FLOAT ARITHMETIC
    #
    # FFF = fd fs ft
    # FF  = fd fs
    # =========================================================

    "fadd": {
        "itype": "R",
        "format": "FFF",
        "ifunction": "101000"
    },

    "fsub": {
        "itype": "R",
        "format": "FFF",
        "ifunction": "101001"
    },

    "fmul": {
        "itype": "R",
        "format": "FFF",
        "ifunction": "101010"
    },

    "fdiv": {
        "itype": "R",
        "format": "FFF",
        "ifunction": "101011"
    },

    "fsqrt": {
        "itype": "R",
        "format": "FF",
        "ifunction": "101100"
    },


    # =========================================================
    # R-TYPE FLOAT COMPARE
    #
    # RFF = integer destination + two float operands
    #
    # Beispiel:
    # flt $t0 $f1 $f2
    # =========================================================

    "feq": {
        "itype": "R",
        "format": "RFF",
        "ifunction": "110000"
    },

    "fne": {
        "itype": "R",
        "format": "RFF",
        "ifunction": "110001"
    },

    "flt": {
        "itype": "R",
        "format": "RFF",
        "ifunction": "110010"
    },

    "fgt": {
        "itype": "R",
        "format": "RFF",
        "ifunction": "110011"
    },

    "fle": {
        "itype": "R",
        "format": "RFF",
        "ifunction": "110100"
    },

    "fge": {
        "itype": "R",
        "format": "RFF",
        "ifunction": "110101"
    },


    # =========================================================
    # R-TYPE FLOAT CONVERSION / TRANSFER
    #
    # FR = Float destination, Integer source
    # RF = Integer destination, Float source
    # =========================================================

    "itof": {
        "itype": "R",
        "format": "FR",
        "ifunction": "111000"
    },

    "ftoi": {
        "itype": "R",
        "format": "RF",
        "ifunction": "111001"
    },

    "mtf": {
        "itype": "R",
        "format": "FR",
        "ifunction": "111010"
    },

    "mff": {
        "itype": "R",
        "format": "RF",
        "ifunction": "111011"
    },

    "fabs": {
        "itype": "R",
        "format": "FF",
        "ifunction": "111100"
    },

    "fneg": {
        "itype": "R",
        "format": "FF",
        "ifunction": "111101"
    },


    # =========================================================
    # I-TYPE LOGIC
    #
    # RRI = target/source register + source/base + immediate
    # =========================================================

    "andi": {
        "itype": "I",
        "format": "RRI",
        "opcode": "000001"
    },

    "ori": {
        "itype": "I",
        "format": "RRI",
        "opcode": "000011"
    },

    "xori": {
        "itype": "I",
        "format": "RRI",
        "opcode": "000100"
    },


    # =========================================================
    # I-TYPE INTEGER ARITHMETIC
    # =========================================================

    "addi": {
        "itype": "I",
        "format": "RRI",
        "opcode": "001000"
    },

    "subi": {
        "itype": "I",
        "format": "RRI",
        "opcode": "001001"
    },

    "muli": {
        "itype": "I",
        "format": "RRI",
        "opcode": "001010"
    },

    "divi": {
        "itype": "I",
        "format": "RRI",
        "opcode": "001011"
    },

    "modi": {
        "itype": "I",
        "format": "RRI",
        "opcode": "001100"
    },


    # =========================================================
    # I-TYPE BRANCH
    # =========================================================

    "beq": {
        "itype": "I",
        "format": "RRI",
        "opcode": "010000"
    },

    "bne": {
        "itype": "I",
        "format": "RRI",
        "opcode": "010001"
    },

    "blt": {
        "itype": "I",
        "format": "RRI",
        "opcode": "010010"
    },

    "bgt": {
        "itype": "I",
        "format": "RRI",
        "opcode": "010011"
    },

    "ble": {
        "itype": "I",
        "format": "RRI",
        "opcode": "010100"
    },

    "bge": {
        "itype": "I",
        "format": "RRI",
        "opcode": "010101"
    },


    # =========================================================
    # I-TYPE LUI
    #
    # RI = destination register + immediate
    # =========================================================

    "lui": {
        "itype": "I",
        "format": "RI",
        "opcode": "010111"
    },


    # =========================================================
    # I-TYPE SHIFT / ROTATE
    # =========================================================

    "srl": {
        "itype": "I",
        "format": "RRI",
        "opcode": "011000"
    },

    "sll": {
        "itype": "I",
        "format": "RRI",
        "opcode": "011001"
    },

    "srr": {
        "itype": "I",
        "format": "RRI",
        "opcode": "011010"
    },

    "slr": {
        "itype": "I",
        "format": "RRI",
        "opcode": "011011"
    },

    "sra": {
        "itype": "I",
        "format": "RRI",
        "opcode": "011100"
    },

    "sla": {
        "itype": "I",
        "format": "RRI",
        "opcode": "011101"
    },


    # =========================================================
    # I-TYPE INTEGER MEMORY
    # =========================================================

    "sw": {
        "itype": "I",
        "format": "RRI",
        "opcode": "011110"
    },

    "lw": {
        "itype": "I",
        "format": "RRI",
        "opcode": "011111"
    },


    # =========================================================
    # I-TYPE FLOAT MEMORY
    #
    # FRI = float register + integer base + immediate
    # =========================================================

    "fsw": {
        "itype": "I",
        "format": "FRI",
        "opcode": "111110"
    },

    "flw": {
        "itype": "I",
        "format": "FRI",
        "opcode": "111111"
    },


    # =========================================================
    # J-TYPE
    # =========================================================

    "j": {
        "itype": "J",
        "format": "J",
        "opcode": "000010"
    }
}