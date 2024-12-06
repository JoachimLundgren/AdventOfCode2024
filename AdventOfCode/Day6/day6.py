import os
import time


def parseinput(filename):
    map = []
    startingPos = []
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        for line in file.read().splitlines():
            map.append(list(line))

    y = 0
    while y < len(map):
        if '^' in map[y]:
            startingPos = (y, map[y].index('^'))
        y = y+1

    return map, startingPos, '^'


def getNextPos(pos, direction):
    if direction == '^':
        return (pos[0]-1, pos[1])
    elif direction == '>':
        return (pos[0], pos[1]+1)
    elif direction == '<':
        return (pos[0], pos[1]-1)
    elif direction == 'v':
        return (pos[0]+1, pos[1])


def turn90Degrees(direction):
    directions = ['^', '>', 'v', '<']
    index = directions.index(direction)
    index = (index + 1) % len(directions)
    return directions[index]


def move(map, pos, direction):
    while True:
        nextPos = getNextPos(pos, direction)

        if (nextPos[0] < 0 or nextPos[0] >= len(map)
                or nextPos[1] < 0 or nextPos[1] >= len(map[0])):
            return None, direction

        if map[nextPos[0]][nextPos[1]] == '#':
            direction = turn90Degrees(direction)
        else:
            return nextPos, direction


def getVisitedNodes(map, pos, direction):
    visited = [pos]
    while True:
        pos, direction = move(map, pos, direction)
        if pos == None:
            break
        visited.append(pos)

    return list(set(visited))


def part1():
    map, pos, direction = parseinput("input.txt")
    visited = getVisitedNodes(map, pos, direction)

    print(len(visited))


def part2():
    startingMap, startingPos, startingDirection = parseinput("input.txt")
    possibleObstructions = getVisitedNodes(startingMap, startingPos, startingDirection)
    possibleObstructions.remove(startingPos)

    loops = 0
    for obstruction in possibleObstructions:
        pos = startingPos
        direction = startingDirection
        map = [row[:] for row in startingMap]
        map[obstruction[0]][obstruction[1]] = '#'

        visited = set()
        visited.add((pos, direction))

        while True:
            pos, direction = move(map, pos, direction)
            if pos == None:
                break

            if (pos, direction) in visited:
                loops = loops + 1
                break

            visited.add((pos, direction))

    print(loops)


start = time.time()
part1()
part2()
