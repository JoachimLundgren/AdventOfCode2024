import os


def parseinput(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return list(map(int, [line.strip('\n') for line in file.readlines()]))


def evolveSecret(secret):
    secret = (secret ^ (secret * 64)) % 16777216
    secret = (secret ^ int(secret / 32)) % 16777216
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret


def part1(input):
    sum = 0
    secrets = parseinput(input)
    for secret in secrets:
        i = 0
        while i < 2000:
            secret = evolveSecret(secret)
            i += 1
        sum += secret

    print(sum)


def part2(input):
    secrets = parseinput(input)

    allPrices = dict()
    for secret in secrets:
        monkeyPrice = dict()
        changes = []
        values = []
        for _ in range(2000):
            value = secret % 10
            values.append(value)
            if len(values) >= 2:
                changes.append(values[-1] - values[-2])

            if len(changes) >= 4:
                sequence = tuple(changes[-4:])
                if sequence not in monkeyPrice:
                    monkeyPrice[sequence] = value
                    if sequence not in allPrices:
                        allPrices[sequence] = value
                    else:
                        allPrices[sequence] += value

            secret = evolveSecret(secret)

    winner = max(allPrices, key=allPrices.get)
    print(winner, allPrices[winner])


part1("input.txt")
part2("input.txt")
