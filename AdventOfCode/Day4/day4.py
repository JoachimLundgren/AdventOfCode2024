import os


def parseinput(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read().splitlines()


def getScore1(y, x, input):
    if input[y][x] != 'X':
        return 0

    score = 0
    # Horizontal
    if x+3 < len(input) and input[y][x+1] == 'M' and input[y][x+2] == 'A' and input[y][x+3] == 'S':
        score = score + 1
    # Horizontal backwards
    if x-3 >= 0 and input[y][x-1] == 'M' and input[y][x-2] == 'A' and input[y][x-3] == 'S':
        score = score + 1
    # Vertical
    if y+3 < len(input[y]) and input[y+1][x] == 'M' and input[y+2][x] == 'A' and input[y+3][x] == 'S':
        score = score + 1
    # Vertical backwards
    if y-3 >= 0 and input[y-1][x] == 'M' and input[y-2][x] == 'A' and input[y-3][x] == 'S':
        score = score + 1

    # Diagonal
    if y+3 < len(input) and x+3 < len(input[y]) and input[y+1][x+1] == 'M' and input[y+2][x+2] == 'A' and input[y+3][x+3] == 'S':
        score = score + 1
    # Diagonal backwards
    if y+3 < len(input) and x-3 >= 0 and input[y+1][x-1] == 'M' and input[y+2][x-2] == 'A' and input[y+3][x-3] == 'S':
        score = score + 1
    # Diagonal upwards
    if y-3 >= 0 and x+3 < len(input[y]) and input[y-1][x+1] == 'M' and input[y-2][x+2] == 'A' and input[y-3][x+3] == 'S':
        score = score + 1
    # Diagonal backwards upwards
    if y-3 >= 0 and x-3 >= 0 and input[y-1][x-1] == 'M' and input[y-2][x-2] == 'A' and input[y-3][x-3] == 'S':
        score = score + 1

    return score


def getScore2(y, x, input):
    if input[y][x] != 'A':
        return 0

    score = 0

    if (input[y-1][x-1] == 'M' and input[y-1][x+1] == 'S' and
            input[y+1][x-1] == 'M' and input[y+1][x+1] == 'S'):
        score = score + 1

    # Backwards
    if (input[y-1][x-1] == 'S' and input[y-1][x+1] == 'M' and
            input[y+1][x-1] == 'S' and input[y+1][x+1] == 'M'):
        score = score + 1

    # Vertical
    if (input[y-1][x-1] == 'M' and input[y-1][x+1] == 'M' and
            input[y+1][x-1] == 'S' and input[y+1][x+1] == 'S'):
        score = score + 1

    # Vertical upwards
    if (input[y-1][x-1] == 'S' and input[y-1][x+1] == 'S' and
            input[y+1][x-1] == 'M' and input[y+1][x+1] == 'M'):
        score = score + 1

    return score


def part1():
    input = parseinput("input.txt")
    score = 0
    y = 0
    while y < len(input):
        x = 0
        while x < len(input[y]):
            score = score + getScore1(y, x, input)
            x = x + 1
        y = y + 1

    print(score)


def part2():
    input = parseinput("input.txt")
    score = 0
    y = 1
    while y < len(input) - 1:
        x = 1
        while x < len(input[y]) - 1:
            score = score + getScore2(y, x, input)
            x = x + 1
        y = y + 1

    print(score)


part1()
part2()
