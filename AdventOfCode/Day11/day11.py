import os
import time


def parseinput(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read().split(' ')


def blink(stone, blinks):
    if blinks == 0:
        return 1

    if (stone, blinks) in cache:
        return cache[(stone, blinks)]

    res = 0
    if stone == '0':
        res += blink('1', blinks-1)
    elif len(stone) % 2 == 0:
        half = int(len(stone) / 2)
        res += blink(stone[:half], blinks-1)
        res += blink(str(int(stone[half:])), blinks-1)
    else:
        res += blink(str(int(stone)*2024), blinks-1)

    cache[(stone, blinks)] = res
    return res


def part1(input):
    stones = parseinput(input)

    result = 0
    for stone in stones:
        result += blink(stone, 25)

    print(result)


def part2(input):
    stones = parseinput(input)

    result = 0
    for stone in stones:
        result += blink(stone, 75)

    print(result)


cache = dict()
start_time = time.time()
part1("input.txt")
print("part 1: %s seconds ---" % (time.time() - start_time))
start_time2 = time.time()
part2("input.txt")
print("part 2: %s seconds ---" % (time.time() - start_time2))
