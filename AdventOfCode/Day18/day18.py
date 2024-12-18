import os


def parseinput(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        bytes = []
        for line in file.readlines():
            c = line.split(',')
            bytes.append((int(c[0]), int(c[1])))
        return bytes


possibleMoves = [(1, 0), (-1, 0), (0, 1),  (0, -1)]


def findPath(bytes, size):
    evaluatedSpaces = dict()
    newSpaces = {(0, 0): 0}

    while True:
        if len(newSpaces) == 0:
            return -1

        nextSpace = min(newSpaces, key=newSpaces.get)
        path = newSpaces.pop(nextSpace)

        for space in [tuple(map(sum, zip(nextSpace, move))) for move in possibleMoves]:
            if space not in evaluatedSpaces and space not in newSpaces and space not in bytes:
                if space[0] >= 0 and space[0] <= size and space[1] >= 0 and space[1] <= size:
                    if space == (size, size):
                        return path + 1
                    else:
                        newSpaces[space] = path + 1

        evaluatedSpaces[nextSpace] = path


def part1(input, size, fallenBytes):
    bytes = parseinput(input)
    path = findPath(bytes[:fallenBytes], size)
    print(path)


def part2(input, size):
    bytes = parseinput(input)

    low = 0
    high = len(bytes)
    while high - low > 1:
        next = low + int((high - low) / 2)
        path = findPath(bytes[:next], size)
        if path == -1:
            high = next
        else:
            low = next

    print(bytes[high-1])


# part1("testinput.txt", 6, 12)
part1("input.txt", 70, 1024)
# part2("testinput.txt", 6)
part2("input.txt", 70)
