import os

possibleMoves = [(1, 0), (-1, 0), (0, 1),  (0, -1)]


def parseinput(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        garden = []
        for line in file.readlines():
            garden.append(list(line.strip()))
        return garden


def getRegion(garden, plant, region, plot):
    region.append(plot)

    for move in possibleMoves:
        nextPlot = tuple(map(sum, zip(plot, move)))
        if (nextPlot[0] >= 0 and nextPlot[0] < len(garden) and nextPlot[1] >= 0 and nextPlot[1] < len(garden[0])):
            nextPlant = garden[nextPlot[0]][nextPlot[1]]
            if plant == nextPlant and nextPlot not in region:
                region = getRegion(garden, nextPlant, region, nextPlot)

    return region


def getPerimiter(region):
    perimiter = 0
    for area in region:
        sides = [tuple(map(sum, zip(area, move))) for move in possibleMoves]
        perimiter += 4 - len([side for side in sides if side in region])
    return perimiter


def getSides(region):
    region.sort()
    perimiter = 0
    fences = dict()
    for area in region:
        fences[area] = []
        sides = [tuple(map(sum, zip(area, move))) for move in possibleMoves]
        alreadyCalculatedFences = [fence for key, fence in fences.items() if key in sides]
        sidefences = [sideFence for fence in alreadyCalculatedFences for sideFence in fence]

        for i, side in enumerate(sides):  # i = down, up, right, left
            if side not in region:
                fences[area].append(i)
                if i not in sidefences:
                    perimiter += 1

    return perimiter


def getPrice(garden, region, bulkDiscount):
    if bulkDiscount:
        perimiter = getSides(region)
    else:
        perimiter = getPerimiter(region)

    area = len(region)
    sum = area * perimiter
    # print("A region of ", garden[region[0][0]][region[0][1]], " plants with price ", area, " * ", perimiter, " = ", sum)
    return sum


def part1(input):
    garden = parseinput(input)
    covered = []

    price = 0
    for y, row in enumerate(garden):
        for x, plot in enumerate(row):
            if (y, x) not in covered:
                region = getRegion(garden, plot, [], (y, x))
                covered += region
                price += getPrice(garden, region, False)

    print(price)


def part2(input):
    garden = parseinput(input)
    covered = []

    price = 0
    for y, row in enumerate(garden):
        for x, plot in enumerate(row):
            if (y, x) not in covered:
                region = getRegion(garden, plot, [], (y, x))
                covered += region
                price += getPrice(garden, region, True)

    print(price)


part1("input.txt")
part2("input.txt")
