import os


def parseinput(filename):
    orderingRules = []
    updates = []
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        ordering = True
        for line in file:
            line = line.strip()
            if line == "":
                ordering = False
            elif ordering:
                orderingRules.append(list(map(int, line.split('|'))))
            else:
                updates.append(list(map(int, line.split(','))))

    return orderingRules, updates


def getUpdateValue(update, rules):
    for page in update:
        if any(x[1] == page and x[0] in update for x in rules):
            return 0
        else:
            rules = list(filter(lambda x: not x[0] == page, rules))

    return update[int(len(update) / 2)]


def reorderUpdate(update, rules):
    newUpdate = []
    while len(update) > 0:
        for page in update:
            if not any(x[1] == page and x[0] in update for x in rules):
                newUpdate.append(page)
                update.remove(page)
    return newUpdate


def part1():
    orderingRules, updates = parseinput("input.txt")
    sum = 0
    for update in updates:
        sum = sum + getUpdateValue(update, orderingRules)
    print(sum)


def part2():
    orderingRules, updates = parseinput("input.txt")
    sum = 0
    for update in updates:
        updateValue = getUpdateValue(update, orderingRules)
        if updateValue == 0:
            newUpdate = reorderUpdate(update, orderingRules)
            sum = sum + newUpdate[int(len(newUpdate) / 2)]
    print(sum)


part1()
part2()
