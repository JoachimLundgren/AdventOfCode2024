import os


def parseinput(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        lines = file.readlines()
        availablePatterns = lines[0].strip().split(", ")
        desiredDesigns = [line.strip() for line in lines[2:]]
        return availablePatterns, desiredDesigns


def canBeMade(availablePatterns, design):
    if design == "":
        return True

    possibleStartPatterns = [pattern for pattern in availablePatterns if design.startswith(pattern)]
    for pattern in possibleStartPatterns:
        if canBeMade(availablePatterns, design[len(pattern):]):
            return True

    return False


cache = dict()


def getPossibleWays(availablePatterns, design):
    if design == "":
        return 1

    if design in cache:
        return cache[design]

    res = 0
    possibleStartPatterns = [pattern for pattern in availablePatterns if design.startswith(pattern)]
    for pattern in possibleStartPatterns:
        res += getPossibleWays(availablePatterns, design[len(pattern):])

    cache[design] = res
    return res


def part1(input):
    availablePatterns, desiredDesigns = parseinput(input)
    possibleDesigns = [design for design in desiredDesigns if canBeMade(availablePatterns, design)]
    print(len(possibleDesigns))


def part2(input):
    availablePatterns, desiredDesigns = parseinput(input)
    res = 0
    for design in desiredDesigns:
        res += getPossibleWays(availablePatterns, design)

    print(res)


part1("input.txt")
part2("input.txt")
