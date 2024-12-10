import os


def parseinput(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        topographicMap = []
        for line in file:
            row = line.strip()
            topographicMap.append(list(map(int, row)))
        return topographicMap


def getScore(current, visited, topographicMap, canRevisit):
    value = topographicMap[current[0]][current[1]]
    if value == 9:
        return 1

    score = 0
    for move in getMoves(current, visited, topographicMap, canRevisit):
        visited.append(move)
        score += getScore(move, visited, topographicMap, canRevisit)

    return score


def getMoves(current, visited, topographicMap, canRevisit):
    possibleMoves = [(1, 0), (-1, 0), (0, 1),  (0, -1)]
    moves = []
    value = topographicMap[current[0]][current[1]]
    for move in possibleMoves:
        next = tuple(map(sum, zip(current, move)))
        if next[0] >= 0 and next[0] < len(topographicMap) and next[1] >= 0 and next[1] < len(topographicMap[0]) and (canRevisit or next not in visited):
            nextValue = topographicMap[next[0]][next[1]]
            if nextValue == value + 1:
                moves.append(next)

    return moves


def part1(input):
    topographicMap = parseinput(input)
    score = 0
    for y, line in enumerate(topographicMap):
        for x, value in enumerate(line):
            if value == 0:
                score += getScore((y, x), [], topographicMap, False)

    print(score)


def part2(input):
    topographicMap = parseinput(input)
    score = 0
    for y, line in enumerate(topographicMap):
        for x, value in enumerate(line):
            if value == 0:
                newScore = getScore((y, x), [], topographicMap, True)
                print(newScore)
                score += newScore

    print(score)


part1("input.txt")
part2("input.txt")
