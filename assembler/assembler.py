import struct

from dictionaries.instructions import instructions
from dictionaries.registers import registers
from utils import hexa


def float_register(register):
    """
    $f0 ... $f31 -> 5-Bit Registeradresse
    """
    if not register.startswith("$f"):
        raise ValueError(f"Ungültiges Float-Register: {register}")

    number = int(register[2:])

    if number < 0 or number > 31:
        raise ValueError(f"Ungültiges Float-Register: {register}")

    return format(number, "05b")


def assemble(instruction):
    parts = instruction.split()
    name = parts[0]


    ################# PSEUDO INSTRUCTIONS #################


    # ------------------------- LI -------------------------
    # li $t0 5
    # -> addi $t0 $zero 5
    if name == "li":

        ibinary = (
            instructions["addi"]["opcode"]
            + "00000"                         # $zero
            + registers[parts[1]]             # Zielregister
            + format(int(parts[2], 0) & 0xFFFF, "016b")
        )

        return hexa(ibinary)


    # ------------------------- FLI -------------------------
    # converts to:
    # lui
    # ori
    # mtf
    #
    if name == "fli":

        # read decimal number
        value = float(parts[2])

        # Python float -> IEEE-754 Single Precision (32 Bit)
        ieee = struct.unpack(
            ">I",
            struct.pack(">f", value)
        )[0]

        # 32 Bit in upper / lower 16 Bit
        upper = (ieee >> 16) & 0xFFFF
        lower = ieee & 0xFFFF


        # ---------------- LUI ----------------
        # lui $at upper
        # opcode | rs=00000 | rt=$at | immediate
        lui_binary = (
            instructions["lui"]["opcode"]
            + "00000"
            + registers["$at"]
            + format(upper, "016b")
        )


        # ---------------- ORI ----------------
        # ori $at $at lower
        # opcode | rs=$at | rt=$at | immediate
        ori_binary = (
            instructions["ori"]["opcode"]
            + registers["$at"]
            + registers["$at"]
            + format(lower, "016b")
        )


        # ---------------- MTF ----------------
        mtf_binary = (
            "000000"
            + registers["$at"]
            + "00000"
            + float_register(parts[1])
            + "00000"
            + instructions["mtf"]["ifunction"]
        )

        return [
            hexa(lui_binary),
            hexa(ori_binary),
            hexa(mtf_binary)
        ]


    # ------------------------- NOT -------------------------
    # not $t0 $t1
    # -> nor $t0 $t1 $t1
    if name == "not":

        ibinary = (
            "000000"
            + registers[parts[2]]
            + registers[parts[2]]
            + registers[parts[1]]
            + "00000"
            + instructions["nor"]["ifunction"]
        )

        return hexa(ibinary)


    # ------------------------- NEG -------------------------
    # neg $t0 $t1
    # -> sub $t0 $zero $t1
    if name == "neg":

        ibinary = (
            "000000"
            + "00000"
            + registers[parts[2]]
            + registers[parts[1]]
            + "00000"
            + instructions["sub"]["ifunction"]
        )

        return hexa(ibinary)


    # ------------------------- INC -------------------------
    # inc $t0
    # -> addi $t0 $t0 1
    if name == "inc":

        ibinary = (
            instructions["addi"]["opcode"]
            + registers[parts[1]]
            + registers[parts[1]]
            + format(1, "016b")
        )

        return hexa(ibinary)


    # ------------------------- DEC -------------------------
    # dec $t0
    # -> subi $t0 $t0 1
    if name == "dec":

        ibinary = (
            instructions["subi"]["opcode"]
            + registers[parts[1]]
            + registers[parts[1]]
            + format(1, "016b")
        )

        return hexa(ibinary)



    ################# CHECK INSTRUCTION #################

    if name not in instructions:
        raise ValueError(f"Unbekannte Instruktion: {name}")

    instructiontype = instructions[name]["itype"]
    instructionformat = instructions[name].get("format")


    ################# I-TYPE #################

    if instructiontype == "I":

        # -------------------------------------------------
        # RRI
        # e.g. addi $t0 $t1 5
        # opcode | rs=$t1 | rt=$t0 | immediate
        # -------------------------------------------------
        if instructionformat == "RRI":

            ibinary = (
                instructions[name]["opcode"]
                + registers[parts[2]]                 # rs
                + registers[parts[1]]                 # rt
                + format(int(parts[3], 0) & 0xFFFF, "016b")
            )


        # -------------------------------------------------
        # RI
        # e.g. lui $t0 0x4020
        # opcode | rs=00000 | rt=$t0 | immediate
        # -------------------------------------------------
        elif instructionformat == "RI":

            ibinary = (
                instructions[name]["opcode"]
                + "00000"                             # rs unbenutzt
                + registers[parts[1]]                 # rt
                + format(int(parts[2], 0) & 0xFFFF, "016b")
            )


        # -------------------------------------------------
        # FRI
        # e.g. flw $f0 $t0 4
        # e.g. fsw $f0 $t0 4
        # opcode | rs=$t0 | rt=$f0 | immediate
        # rs = Integer Base Register
        # rt = Float Register
        # -------------------------------------------------
        elif instructionformat == "FRI":

            ibinary = (
                instructions[name]["opcode"]
                + registers[parts[2]]                 # Integer Base
                + float_register(parts[1])            # Float Register
                + format(int(parts[3], 0) & 0xFFFF, "016b")
            )


        else:
            raise ValueError(
                f"Nicht unterstütztes I-Type Format "
                f"'{instructionformat}' für {name}"
            )

        return hexa(ibinary)


    ################# J-TYPE #################

    elif instructiontype == "J":

        ibinary = (
            instructions[name]["opcode"]
            + format(int(parts[1], 0), "026b")
        )

        return hexa(ibinary)


    ################# R-TYPE #################

    elif instructiontype == "R":

        funct = instructions[name]["ifunction"]


        # =================================================
        # RRR
        #
        # Integer:
        # add $t0 $t1 $t2
        #
        # rd = $t0
        # rs = $t1
        # rt = $t2
        # =================================================

        if instructionformat == "RRR":

            ibinary = (
                "000000"
                + registers[parts[2]]                 # rs
                + registers[parts[3]]                 # rt
                + registers[parts[1]]                 # rd
                + "00000"
                + funct
            )


        # =================================================
        # FFF
        #
        # Float:
        # fadd $f0 $f1 $f2
        #
        # rd = $f0
        # rs = $f1
        # rt = $f2
        # =================================================

        elif instructionformat == "FFF":

            ibinary = (
                "000000"
                + float_register(parts[2])             # rs
                + float_register(parts[3])             # rt
                + float_register(parts[1])             # rd
                + "00000"
                + funct
            )


        # =================================================
        # RFF
        #
        # Float Compare:
        #
        # flt $t0 $f1 $f2
        #
        # rd = Integer Destinatiom
        # rs = Float Source 1
        # rt = Float Source 2
        # =================================================

        elif instructionformat == "RFF":

            ibinary = (
                "000000"
                + float_register(parts[2])             # rs
                + float_register(parts[3])             # rt
                + registers[parts[1]]                 # rd Integer
                + "00000"
                + funct
            )


        # =================================================
        # FF
        #
        # Unary Float:
        #
        # fabs  $f0 $f1
        # fneg  $f0 $f1
        # fsqrt $f0 $f1
        #
        # rs = Float Source
        # rt = not used
        # rd = Float Ziel
        # =================================================

        elif instructionformat == "FF":

            ibinary = (
                "000000"
                + float_register(parts[2])             # rs
                + "00000"                              # rt
                + float_register(parts[1])             # rd
                + "00000"
                + funct
            )


        # =================================================
        # FR
        #
        # Integer -> Float
        #
        # itof $f0 $t0
        # mtf  $f0 $t0
        #
        # rs = Integer Source
        # rt = not used
        # rd = Float Ziel
        # =================================================

        elif instructionformat == "FR":

            ibinary = (
                "000000"
                + registers[parts[2]]                 # rs Integer
                + "00000"                              # rt
                + float_register(parts[1])             # rd Float
                + "00000"
                + funct
            )


        # =================================================
        # RF
        #
        # Float -> Integer
        #
        # ftoi $t0 $f0
        # mff  $t0 $f0
        #
        # rs = Float Source
        # rt = not used
        # rd = Integer Ziel
        # =================================================

        elif instructionformat == "RF":

            ibinary = (
                "000000"
                + float_register(parts[2])             # rs Float
                + "00000"                              # rt
                + registers[parts[1]]                 # rd Integer
                + "00000"
                + funct
            )


        # =================================================
        # RD
        #
        # Only Destination
        #
        # mfhi $t0
        # mflo $t0
        #
        # rd = Integer Destination
        # =================================================

        elif instructionformat == "RD":

            ibinary = (
                "000000"
                + "00000"                              # rs
                + "00000"                              # rt
                + registers[parts[1]]                 # rd
                + "00000"
                + funct
            )


        # =================================================
        # RS
        #
        # Only Source
        #
        # mthi $t0
        # mtlo $t0
        #
        # rs = Integer Source
        # =================================================

        elif instructionformat == "RS":

            ibinary = (
                "000000"
                + registers[parts[1]]                 # rs
                + "00000"                              # rt
                + "00000"                              # rd
                + "00000"
                + funct
            )


        else:
            raise ValueError(
                f"Nicht unterstütztes R-Type Format "
                f"'{instructionformat}' für {name}"
            )

        return hexa(ibinary)


    raise ValueError(
        f"Nicht unterstützter Instruktionstyp: {instructiontype}"
    )