import os
import re

def parseinput(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()    

def part1():
    str = parseinput("input.txt")
    instructions = re.findall("mul\(\d{1,3},\d{1,3}\)", str)
    
    sum = 0
    for instruction in instructions:
        factors = instruction[4:][:-1].split(",")
        sum = sum + int(factors[0]) * int(factors[1])

    print(sum)


def part2():
    str = parseinput("input.txt")
    instructions = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", str)

    sum = 0
    do = True
    for instruction in instructions:
        if instruction.startswith("don't"):
            do = False
        elif instruction.startswith("do"):
            do = True
        elif do:
            factors = instruction[4:][:-1].split(",")
            sum = sum + int(factors[0]) * int(factors[1])

    print(sum)

part1()
part2()