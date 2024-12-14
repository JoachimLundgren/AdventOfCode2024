import os
import re
import time


class Robot:
    def __init__(self, p, v):
        self.p = p
        self.v = v


def parseinput(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        robots = []
        for line in file:
            numbers = re.findall("(-?\d*,-?\d*)", line)

            robots.append(Robot(parseCoordinates(numbers[0]), parseCoordinates(numbers[1])))
        return robots


def parseCoordinates(str):
    l = list(map(int, str.split(',')))
    return (l[0], l[1])


def getSafetyfactor(robots, width, height):
    first = 0
    second = 0
    third = 0
    fourth = 0

    quadrantWidth = int(width / 2)
    quadrantHeight = int(height / 2)
    for robot in robots:
        if robot.p[0] < quadrantWidth and robot.p[1] < quadrantHeight:
            first += 1
        elif robot.p[0] >= width - quadrantWidth and robot.p[1] < quadrantHeight:
            second += 1
        elif robot.p[0] < quadrantWidth and robot.p[1] >= height - quadrantHeight:
            third += 1
        elif robot.p[0] >= width - quadrantWidth and robot.p[1] >= height - quadrantHeight:
            fourth += 1

    return first * second * third * fourth


def printBathroom(robots, width, height, seconds):
    bathroom = "{0} seconds:\n".format(seconds)
    y = 0
    while y < height:
        x = 0
        while x < width:
            bots = len([r for r in robots if r.p == (x, y)])
            if bots == 0:
                bathroom += '.'
            else:
                bathroom += str(bots)
            x += 1
        bathroom += "\n"
        y += 1

    print(bathroom)


def part1(input, width, height):
    robots = parseinput(input)

    seconds = 0
    while seconds < 100:
        for robot in robots:
            robot.p = ((robot.p[0] + robot.v[0]) % width, (robot.p[1] + robot.v[1]) % height)
        seconds += 1

    # printBathroom(robots, width, height, seconds)
    print(getSafetyfactor(robots, width, height))


def part2(_input, width, height):
    robots = parseinput(_input)

    seconds = 0
    while True:
        for robot in robots:
            robot.p = ((robot.p[0] + robot.v[0]) % width, (robot.p[1] + robot.v[1]) % height)

        seconds += 1
        if (seconds % 101) - 27 == 0:  # The bots where clustering every 101s starting at second 27. So just looked at those and eventually found a tree at 8006
            printBathroom(robots, width, height, seconds)
            time.sleep(0.2)


part1("input.txt", 101, 103)
part2("input.txt", 101, 103)
