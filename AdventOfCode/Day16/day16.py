import os
from sortedcontainers import SortedList


class Record(object):
    def __init__(self, tile, direction, score, path):
        self.tile = tile
        self.direction = direction
        self.score = score
        self.path = path

    def __eq__(self, other):
        return self.tile == other.tile and self.direction == other.direction


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


def printPath(path, walls):
    heigt = max([w[0] for w in walls]) + 1
    width = max([w[1] for w in walls]) + 1

    output = ""
    y = 0
    while y < heigt:
        x = 0
        while x < width:
            if (y, x) in walls:
                output += '#'
            elif (y, x) in path:
                output += 'O'
            else:
                output += '.'
            x += 1
        output += "\n"
        y += 1
    with open("output.txt", "w") as text_file:
        text_file.write(output)
        text_file.close()
    # print(output)


possibleMoves = {'E': (0, 1), 'S': (1, 0), 'W': (0, -1), 'N': (-1, 0)}
possibleRotations = {'E': ['N', 'S'], 'S': ['E', 'W'], 'W': ['N', 'S'], 'N': ['E', 'W']}


def part1(input):
    walls, start, end = parseinput(input)
    def get_score(record): return record.score
    unhandled = SortedList([Record(start, 'E', 0, [(start, 'E')])], key=get_score)
    visited = set()

    while True:
        record = unhandled.pop(0)
        newTile = tuple(map(sum, zip(record.tile, possibleMoves[record.direction])))

        if newTile == end:
            print(record.score+1)
            break

        if newTile not in walls:
            unhandled.add(Record(newTile, record.direction, record.score +
                          1, record.path + [(newTile, record.direction)]))
            visited.add((newTile, record.direction))

        for newDirection in possibleRotations[record.direction]:
            if (record.tile, newDirection) not in visited:
                unhandled.add(Record(record.tile, newDirection, record.score +
                              1000, record.path + [(record.tile, newDirection)]))
                visited.add((record.tile, newDirection))


def part2(input):
    walls, start, end = parseinput(input)
    def get_score(record): return record.score
    unhandled = SortedList([Record(start, 'E', 0, [(start, 'E')])], key=get_score)
    visited = dict()

    bestpath = None
    tilesOnBestPath = set()
    while True:
        record = unhandled.pop(0)
        newTile = tuple(map(sum, zip(record.tile, possibleMoves[record.direction])))

        if bestpath != None and record.score > bestpath:
            # printPath(tilesOnBestPath, walls)
            print(len(tilesOnBestPath))
            break

        if newTile == end:
            score = record.score+1

            if bestpath == None:
                bestpath = score

            if bestpath == score:
                path = [p[0] for p in record.path] + [end]
                tilesOnBestPath.update(path)

            # print(score)

        if newTile not in walls:
            score = record.score + 1
            if (newTile, record.direction) not in visited:
                unhandled.add(Record(newTile, record.direction, score, record.path + [(newTile, record.direction)]))
                visited[(newTile, record.direction)] = score
            elif visited[(newTile, record.direction)] == score:
                unhandled.add(Record(newTile, record.direction, score, record.path + [(newTile, record.direction)]))

        for newDirection in possibleRotations[record.direction]:
            score = record.score + 1000

            if (record.tile, newDirection) not in visited:
                visited[(record.tile, newDirection)] = score
                unhandled.add(Record(record.tile, newDirection, score, record.path + [(record.tile, newDirection)]))
            elif visited[(record.tile, newDirection)] == score:
                unhandled.add(Record(record.tile, newDirection, score, record.path + [(record.tile, newDirection)]))


part1("input.txt")
part2("input.txt")
