import os


def parseinput(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        lines = file.readlines()
        start = (-1, -1)
        end = (-1, -1)
        walls = []
        for y, line in enumerate(lines):
            for x, c in enumerate(line.strip('\n')):
                if c == 'S':
                    start = (y, x)
                elif c == 'E':
                    end = (y, x)
                elif c == '#':
                    walls.append((y, x))
        return walls, start, end


possibleMoves = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def race(walls, start, end):
    toBeEvaluated = {start: 0}
    evaluated = dict()
    current = start
    while len(toBeEvaluated) > 0:
        current = min(toBeEvaluated, key=toBeEvaluated.get)
        currentScore = toBeEvaluated.pop(current)

        if current != end:
            for next in [tuple(map(sum, zip(current, move))) for move in possibleMoves]:
                if next not in evaluated and next not in toBeEvaluated and next not in walls:
                    toBeEvaluated[next] = currentScore + 1

        evaluated[current] = currentScore

    return evaluated


def getSave(path, first, second):
    if first in path and second in path:
        return abs(path[first] - path[second]) - 2

    return 0


def getPossibleEnds(start, path, cheatingRule=20):
    distancesToStart = [(p, abs(p[0]-start[0]) + abs(p[1]-start[1])) for p in path]
    return [p for p in distancesToStart if p[1] <= cheatingRule and p[1] > 0]


def part1(input):
    walls, start, end = parseinput(input)
    path = race(walls, start, end)

    res = 0
    for wall in walls:
        temp = [tuple(map(sum, zip(wall, move))) for move in possibleMoves]
        if getSave(path, temp[0], temp[2]) >= 100:
            res += 1
        elif getSave(path, temp[1], temp[3]) >= 100:
            res += 1

    print(res)


def part2(input):
    walls, start, end = parseinput(input)
    path = race(walls, start, end)

    res = 0
    cheatsCalculated = set()
    for start in path:
        possibleEnds = getPossibleEnds(start, path, 20)
        for end in possibleEnds:
            if (start, end[0]) not in cheatsCalculated and (end[0], start) not in cheatsCalculated:
                cheatsCalculated.add((start, end[0]))
                save = abs(path[start] - path[end[0]]) - end[1]
                if save >= 100:
                    res += 1
    print(res)


part1("input.txt")
part2("input.txt")
