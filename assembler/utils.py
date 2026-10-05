def hexa(ibinary):
    return format(int(ibinary, 2), "08X")

def remove_comments(instruction_list_temp, infile):
    """
    Remove comments and empty lines from the input file.

    Parameters
    ----------
    instruction_list_temp : list
        List to which the cleaned instructions are appended.
    infile : file object
        Input file containing the instructions.

    Returns
    -------
    None
        The instruction_list_temp list is modified in place.

    """
    #removing comments and/or empty lines
    for line in infile:

        instruction = line.split("#")[0].strip()
        if not instruction:
            continue
        instruction_list_temp.append(instruction)


def create_instruction_list(instruction_list_temp, instruction_list):

    """Replace labels in jump and branch instructions with their
    corresponding instruction addresses and create the final
    instruction list.

    Parameters
    ----------
    instruction_list_temp : list
        Temporary list containing instructions and labels.
    instruction_list : list
        List to which the final instructions are appended.

    Returns
    -------
    None
        The instruction_list list is modified in place."""

    counter = 0

    for i in range(1,len(instruction_list_temp)):
        if instruction_list_temp[i][-1] == ":":

            label = instruction_list_temp[i][:-1]
            counter = counter + 1

            for j in range(1,len(instruction_list_temp)):

                splitted = instruction_list_temp[j].split()

                if instruction_list_temp[j][0] == "j":

                    if splitted[1] == label:
                        instruction_list_temp[j] = "j" + " " + str(i-counter)

                if instruction_list_temp[j][0] == "b":
                
                    if splitted[3] == label:
                        instruction_list_temp[j] = splitted[0] + " " + splitted[1] + " " + splitted[2] + " " + str(i-counter)
    
    for i in range(1,len(instruction_list_temp)):
        if instruction_list_temp[i][-1] == ":":
            instruction_list_temp[i] = "x"
    
    for i in range(0,len(instruction_list_temp)):
        if instruction_list_temp[i] != "x":
            instruction_list.append(instruction_list_temp[i])