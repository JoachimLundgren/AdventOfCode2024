import os


def parseinput(filename):
    global maxY
    global maxX
    antennas = {}
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        lines = file.read().splitlines()
        maxY = len(lines)
        maxX = len(lines[0])
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char != '.':
                    if char not in antennas:
                        antennas[char] = []
                    antennas[char].append((y, x))
    return antennas


def getAntinodes(antenna, antennas, resonance):
    if len(antennas) == 0:
        return []

    antinodes = []
    for other in antennas:
        antinodes += getPointsPerfectlyInLine(antenna, other, resonance)

    antinodes += getAntinodes(antennas[0], antennas[1:], resonance)
    return antinodes


def getPointsPerfectlyInLine(first, second, resonance):
    points = []

    i = 1
    while True:
        newY = first[0] + (first[0] - second[0]) * i
        newX = first[1] + (first[1] - second[1]) * i
        if (newY >= 0 and newY < maxY
                and newX >= 0 and newX < maxX):
            points.append((newY, newX))
            i += 1
        else:
            break

        if not resonance:
            break

    i = 1
    while True:
        newY = second[0] + (second[0] - first[0]) * i
        newX = second[1] + (second[1] - first[1]) * i
        if (newY >= 0 and newY < maxY
                and newX >= 0 and newX < maxX):
            points.append((newY, newX))
            i += 1
        else:
            break

        if not resonance:
            break

    return points


def filterNodes(nodes):
    filteredNodes = [node for node in nodes if (node[0] >= 0 and node[0] < maxY
                                                and node[1] >= 0 and node[1] < maxX)]
    return list(set(filteredNodes))


def printCity(city, antinodes):
    y = 0
    while y < maxY:
        str = ""
        x = 0
        while x < maxX:
            antenna = next((freq for freq, nodes in city.items() if (y, x) in nodes), None)
            if antenna != None:
                str += antenna
            elif (y, x) in antinodes:
                str += '#'
            else:
                str += '.'
            x += 1
        print(str)
        y += 1


def part1():
    city = parseinput("input.txt")
    antinodes = []
    for frequency in city.values():
        antinodes += getAntinodes(frequency[0], frequency[1:], False)

    filteredNodes = filterNodes(antinodes)
    print(len(filteredNodes))


def part2():
    city = parseinput("input.txt")
    antinodes = []
    for frequency in city.values():
        antinodes += getAntinodes(frequency[0], frequency[1:], True)
        antinodes += frequency

    filteredNodes = filterNodes(antinodes)
    # printCity(city, filteredNodes)
    print(len(filteredNodes))


part1()
part2()
