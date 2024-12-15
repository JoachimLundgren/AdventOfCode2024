import os


def parseinput(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        lines = file.readlines()

        parsingMap = True
        items = {}
        walls = []

        moves = []
        for y, line in enumerate(lines):
            if parsingMap:
                if line == "\n":
                    parsingMap = False
                else:
                    for x, c in enumerate(line.strip('\n')):
                        if c == 'O' or c == '@':
                            items[len(items)] = (c, [(y, x)])
                        elif c == '#':
                            walls.append((y, x))
            else:
                moves += line.strip('\n')
        return items, walls, moves


def expandItems(items, walls):
    newItems = dict()
    newWalls = []
    for k, v in items.items():
        location = (v[1][0][0], v[1][0][1]*2)
        if v[0] == '@':
            newItems[k] = (v[0], [location])
        else:
            newItems[k] = (v[0], [location, (location[0], location[1]+1)])

    for wall in walls:
        newWalls.append((wall[0], wall[1]*2))
        newWalls.append((wall[0], wall[1]*2+1))

    return newItems, newWalls


possibleMoves = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}


def canMove(itemKey, items, walls, move):
    currentItem = items[itemKey]
    newPositions = [tuple(map(sum, zip(x, possibleMoves[move]))) for x in currentItem[1]]

    for newPos in [x for x in newPositions if x not in currentItem[1]]:
        if any(newPos == wall for wall in walls):
            return False

        boxesInNewPos = [k for k, v in items.items() if newPos in v[1]]
        for box in boxesInNewPos:
            if not canMove(box, items, walls, move):
                return False

    return True


def doMove(itemKey, items, move):
    currentItem = items[itemKey]
    newPositions = [tuple(map(sum, zip(x, possibleMoves[move]))) for x in currentItem[1]]

    for newPos in [x for x in newPositions if x not in currentItem[1]]:
        boxesInNewPos = [k for k, v in items.items() if newPos in v[1]]
        for box in boxesInNewPos:
            doMove(box, items, move)

    items[itemKey] = (currentItem[0], newPositions)


def getResults(items):
    boxLocations = [x[1][0] for x in items.values() if x[0] == 'O']
    return sum([x[0] * 100 + x[1] for x in boxLocations])


def printItems(items, walls):
    heigt = max([w[0] for w in walls]) + 1
    width = max([w[1] for w in walls]) + 1

    output = ""
    y = 0
    while y < heigt:
        x = 0
        while x < width:
            if (y, x) in walls:
                output += '#'
            else:
                item = [v for k, v in items.items() if any(pos == (y, x) for pos in v[1])]
                if len(item) > 0:
                    output += item[0][0]
                else:
                    output += '.'
            x += 1
        output += "\n"
        y += 1

    print(output)


def part1(input):
    items, walls, moves = parseinput(input)

    [robotIndex] = [i for i in items if items[i][0] == '@']

    for move in moves:
        if canMove(robotIndex, items, walls, move):
            doMove(robotIndex, items, move)

    # printItems(items, walls)
    print(getResults(items))


def part2(input):
    items, walls, moves = parseinput(input)
    items, walls = expandItems(items, walls)

    [robotIndex] = [i for i in items if items[i][0] == '@']
    for move in moves:
        if canMove(robotIndex, items, walls, move):
            doMove(robotIndex, items, move)

    # printItems(items, walls)
    print(getResults(items))


part1("input.txt")
part2("input.txt")
