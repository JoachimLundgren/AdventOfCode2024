import os
import math


def parseinput(filename):
    equations = []
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        for line in file.read().splitlines():
            parts = line.split(':')
            operators = parts[1].strip().split(' ')
            equations.append((int(parts[0]), list(map(int, operators))))
    return equations


def concat(x, y):
    # return int(str(x) + str(y))  #slow?
    digits = math.floor(math.log10(y)) + 1
    return x*10**digits+y


def canBeSolved(value, operators, includeConcat):
    if len(operators) == 1:
        return value == operators[0]
    elif value < operators[0]:
        return False

    valueIfAdd = operators[0] + operators[1]
    valueIfMul = operators[0] * operators[1]
    if includeConcat:
        valueIfConcat = concat(operators[0], operators[1])

    return (canBeSolved(value, [valueIfAdd] + operators[2:], includeConcat)
            or canBeSolved(value, [valueIfMul] + operators[2:], includeConcat)
            or (includeConcat and canBeSolved(value, [valueIfConcat] + operators[2:], includeConcat)))


def part1():
    equations = parseinput("input.txt")
    solvable = [equation[0] for equation in equations if canBeSolved(equation[0], equation[1], includeConcat=False)]

    print(sum(solvable))


def part2():
    equations = parseinput("input.txt")
    solvable = [equation[0] for equation in equations if canBeSolved(equation[0], equation[1], includeConcat=True)]

    print(sum(solvable))


part1()
part2()
