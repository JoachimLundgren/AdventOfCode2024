import os

def parseinput(filename):
    first = []
    second = []

    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        for line in file:
            row = line.strip().split(" ")
            first.append(int(row[0]))
            second.append(int(row[-1]))
    return first, second

def part1():
    first, second = parseinput("input1.txt")
    first.sort()
    second.sort()

    distance = 0

    for a, b in zip(first, second):
        distance = distance + abs(a - b)

    print(distance)

def part2():
    first, second = parseinput("input1.txt")

    similarity = 0

    for a in first:
        similarity = similarity + a * second.count(a)

    print(similarity)

part1()
part2()