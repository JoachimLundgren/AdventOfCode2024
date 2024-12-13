import os
import re
import time


class ClawMachine:
    def __init__(self, a, b, prize):
        self.a = a
        self.b = b
        self.prize = prize


class Coordinate:
    def __init__(self, arr):
        self.x = arr[0]
        self.y = arr[1]


def parseinput(filename, extraPrize):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        machines = []
        lines = file.readlines()
        i = 0
        while i < len(lines):
            machines.append(ClawMachine(parse(lines[i], 0), parse(lines[i+1], 0), parse(lines[i+2], extraPrize)))
            i += 4
        return machines


def parse(str, extraPrize):
    numbers = list(map(int, re.findall(r'\d+', str)))
    return Coordinate([i + extraPrize for i in numbers])


# Solved with cramers rule
def solve(machine):
    d = machine.a.x * machine.b.y - machine.a.y * machine.b.x
    dx = machine.prize.x * machine.b.y - machine.prize.y * machine.b.x
    dy = machine.a.x * machine.prize.y - machine.a.y * machine.prize.x

    if dx % d != 0 or dy % d != 0:
        return None

    a = int(dx / d)
    b = int(dy / d)

    return a * 3 + b


def part1(input):
    clawMachines = parseinput(input, 0)

    result = 0
    for machine in clawMachines:
        res = solve(machine)
        # print(res)
        if res != None:
            result += res

    print(result)


def part2(input):
    clawMachines = parseinput(input, 10000000000000)

    result = 0
    for machine in clawMachines:
        res = solve(machine)
        # print(res)
        if res != None:
            result += res

    print(result)


start_time = time.time()
part1("input.txt")
print("part 1: %s seconds ---" % (time.time() - start_time))
start_time2 = time.time()
part2("input.txt")
print("part 2: %s seconds ---" % (time.time() - start_time2))
