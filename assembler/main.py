from assembler import assemble
from utils import remove_comments
from utils import create_instruction_list
import os

print(os.getcwd())

instruction_list = []
instruction_list_temp = ["x"]  # starting at index 1

with open("program.asm", "r") as infile:
    with open("program.hex", "w") as outfile:

        remove_comments(instruction_list_temp, infile)
        create_instruction_list(instruction_list_temp, instruction_list)

        for i in range(0, len(instruction_list)):
            instruction_hex = assemble(instruction_list[i])

            if isinstance(instruction_hex, list):
                for code in instruction_hex:
                    outfile.write(code + "\n")
            else:
                outfile.write(instruction_hex + "\n")

print(instruction_list)