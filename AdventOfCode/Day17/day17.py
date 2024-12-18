import os
import re


def parseinput(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        lines = file.readlines()
        [regA] = [int(s) for s in lines[0].split() if s.isdigit()]
        [regB] = [int(s) for s in lines[1].split() if s.isdigit()]
        [regC] = [int(s) for s in lines[2].split() if s.isdigit()]

        program = [int(s) for s in re.findall("\d", lines[4])]

        return regA, regB, regC, program


def run(regA, regB, regC, program, breakAfterFirstOutput=False):
    ip = 0
    output = []

    while ip < len(program):
        instruction = program[ip]
        operand = program[ip+1]
        jumped = False
        match instruction:
            case 0:  # adv
                regA = int(regA / (2 ** getComboOperand(operand, regA, regB, regC)))
            case 1:  # bxl
                regB = regB ^ operand
            case 2:  # bst
                regB = getComboOperand(operand, regA, regB, regC) % 8
            case 3:  # jnz
                if regA != 0:
                    ip = operand
                    jumped = True
            case 4:  # bxc
                regB = regB ^ regC
            case 5:  # out
                output.append(getComboOperand(operand, regA, regB, regC) % 8)
                if breakAfterFirstOutput:
                    return output
            case 6:  # bdv
                regB = int(regA / (2 ** getComboOperand(operand, regA, regB, regC)))
            case 7:  # cdv
                regC = int(regA / (2 ** getComboOperand(operand, regA, regB, regC)))

        if not jumped:
            ip += 2

    return output


def getComboOperand(operand, regA, regB, regC):
    if operand > 6:
        raise Exception("Error")

    match operand:
        case 4:
            return regA
        case 5:
            return regB
        case 6:
            return regC
        case _:
            return operand


def part1(input):
    regA, regB, regC, program = parseinput(input)
    output = run(regA, regB, regC, program)
    res = ','.join([str(i) for i in output])
    print(res)


def part2(input):
    _, _, _, program = parseinput(input)

    # I analyzed the program and realized that I didn't need to check all potential A.
    # Also it doesn't matter what B and C where so those can be whatever at start of each run.
    # For every output, A was divided by 8 and converted to int, and the output was depending on the last 3 bits.
    # So I worked backwards, finding potential A's and multiplying with 8, then checking all possible last 3 bits.
    potentialA = [0]
    for desiredOutput in reversed(program):
        newPotentialA = []
        for a in potentialA:
            for lastABits in range(8):
                hypotheticalA = a * 8 + lastABits
                output = run(hypotheticalA, 0, 0, program, breakAfterFirstOutput=True)

                if output[0] == desiredOutput:
                    newPotentialA.append(hypotheticalA)

            potentialA = newPotentialA

    print(min(potentialA))


part1("input.txt")
part2("input.txt")
