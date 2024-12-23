import os


def parseinput(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        connections = dict()
        for line in file:
            computers = line.strip().split('-')
            if computers[0] in connections:
                connections[computers[0]].append(computers[1])
            else:
                connections[computers[0]] = [computers[1]]

            if computers[1] in connections:
                connections[computers[1]].append(computers[0])
            else:
                connections[computers[1]] = [computers[0]]

        return connections


def expandSet(connections, lans):
    newLans = set()

    for lan in lans:
        for k, v in connections.items():
            if all(computer in v for computer in lan):
                newLan = list(lan) + [k]
                newLan.sort()
                newLans.add(tuple(newLan))

    return newLans


def part1(input):
    connections = parseinput(input)
    interConnectedWithT = set()
    for first, value in connections.items():
        for second in value:
            for third in connections[second]:
                if first in connections[third] and second in connections[third]:
                    if first.startswith('t') or second.startswith('t') or third.startswith('t'):
                        arr = [first, second, third]
                        arr.sort()
                        interConnectedWithT.add(tuple(arr))

    print(len(interConnectedWithT))


def part2(input):
    connections = parseinput(input)
    interConnected = set()
    for first, value in connections.items():
        for second in value:
            arr = [first, second]
            arr.sort()
            interConnected.add(tuple(arr))

    while len(interConnected) > 1:
        # print(len(interConnected))
        interConnected = expandSet(connections, interConnected)

    print(','.join(interConnected.pop()))


part1("input.txt")
part2("input.txt")
