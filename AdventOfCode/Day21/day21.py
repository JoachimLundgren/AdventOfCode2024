import os
import re
import itertools


def parseinput(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return [line.strip('\n') for line in file.readlines()]


ANumerical = {'A': '', '0': '<',
              '1': '^<<', '2': '<^', '3': '^',
              '4': '^^<<', '5': '^^<', '6': '^^',
              '7': '^^^<<', '8': '^^^<', '9': '^^^'}

Zero = {'A': '>', '0': '',
        '1': '^<', '2': '^', '3': '>^',
        '4': '^^<', '5': '^^', '6': '>^^',
        '7': '^^^<', '8': '^^^', '9': '>^^^'}

One = {'A': '>>v', '0': '>v',
       '1': '', '2': '>', '3': '>>',
       '4': '^', '5': '>^', '6': '>>^',
       '7': '^^', '8': '>^^', '9': '>>^^'}

Two = {'A': '>v', '0': 'v',
       '1': '<', '2': '', '3': '>',
       '4': '<^', '5': '^', '6': '>^',
       '7': '<^^', '8': '^^', '9': '>^^'}

Three = {'A': 'v', '0': '<v',
         '1': '<<', '2': '<', '3': '',
         '4': '<<^', '5': '<^', '6': '^',
         '7': '<<^^', '8': '<^^', '9': '^^'}

Four = {'A': '>>vv', '0': '>vv',
        '1': 'v', '2': '>v', '3': '>>v',
        '4': '', '5': '>', '6': '>>',
        '7': '^', '8': '>^', '9': '>>^'}

Five = {'A': '>vv', '0': 'vv',
        '1': '<v', '2': 'v', '3': '>v',
        '4': '<', '5': '', '6': '>',
        '7': '<^', '8': '^', '9': '>^'}

Six = {'A': 'vv', '0': '<vv',
       '1': '<<v', '2': '<v', '3': 'v',
       '4': '<<', '5': '<', '6': '',
       '7': '<<^', '8': '<^', '9': '^'}

Seven = {'A': '>>vvv', '0': '>vvv',
         '1': 'vv', '2': '>vv', '3': '>>vv',
         '4': 'v', '5': '>v', '6': '>>v',
         '7': '', '8': '>', '9': '>>'}

Eight = {'A': '>vvv', '0': 'vvv',
         '1': '<vv', '2': 'vv', '3': '>vv',
         '4': '<v', '5': 'v', '6': '>v',
         '7': '<', '8': '', '9': '>'}

Nine = {'A': 'vvv', '0': '<vvv',
        '1': '<<vv', '2': '<vv', '3': 'vv',
        '4': '<<v', '5': '<v', '6': 'v',
        '7': '<<', '8': '<', '9': ''}

ADirectional = {'A': '', '^': '<', '>': 'v', 'v': '<v', '<': 'v<<'}
Up = {'A': '>', '^': '', '>': '>v', 'v': 'v', '<': 'v<'}
Down = {'A': '>^', '^': '^', '>': '>', 'v': '', '<': '<'}
Left = {'A': '>>^', '^': '>^', '>': '>>', 'v': '>', '<': ''}
Right = {'A': '^', '^': '<^', '>': '', 'v': '<', '<': '<<'}


AllNumerical = {'A': ANumerical, '0': Zero, '1': One, '2': Two, '3': Three, '4': Four,
                '5': Five, '6': Six, '7': Seven, '8': Eight, '9': Nine}
AllDirectional = {'A': ADirectional, '^': Up, 'v': Down, '<': Left, '>': Right}


def getAllShortest(char, start, numerical=False):
    if numerical:
        oneShortest = AllNumerical[start][char]
    else:
        oneShortest = AllDirectional[start][char]

    allShortest = [''.join(x) + 'A' for x in itertools.permutations(oneShortest)]

    if numerical:
        if start == 'A':
            allShortest = [x for x in allShortest if not x.startswith('<<')]
        elif start == '0':
            allShortest = [x for x in allShortest if not x.startswith('<')]
        elif start == '1':
            allShortest = [x for x in allShortest if not x.startswith('v')]
        elif start == '4':
            allShortest = [x for x in allShortest if not x.startswith('vv')]
        elif start == '7':
            allShortest = [x for x in allShortest if not x.startswith('vvv')]
    else:
        if start == 'A':
            allShortest = [x for x in allShortest if not x.startswith('<<')]
        elif start == '^':
            allShortest = [x for x in allShortest if not x.startswith('<')]
        elif start == '<':
            allShortest = [x for x in allShortest if not x.startswith('^')]

    return allShortest


cache = dict()


def getShortestSequence(char, start, depth, numerical=False):
    if (char, start, depth) in cache:
        return cache[(char, start, depth)]

    allShortest = getAllShortest(char, start, numerical)

    if depth == 1:
        res = len(allShortest[0])
        cache[(char, start, depth)] = res
        return res

    shortest = None
    for sequence in allShortest:
        prev = 'A'
        innerSequence = 0
        for char1 in sequence:
            innerSequence += getShortestSequence(char1, prev, depth-1)
            prev = char1

        if shortest == None or innerSequence < shortest:
            shortest = innerSequence

    cache[(char, start, depth)] = shortest
    return shortest


def part1(input):
    sum = 0
    sequences = parseinput(input)
    for sequence in sequences:
        res = 0
        prev = 'A'
        for char in sequence:
            res += getShortestSequence(char, prev, 3, True)
            prev = char
        number = int(re.findall('\d+', sequence)[0])
        sum += res * number

    print(sum)


def part2(input):
    sum = 0
    sequences = parseinput(input)
    for sequence in sequences:
        res = 0
        prev = 'A'
        for char in sequence:
            res += getShortestSequence(char, prev, 26, True)
            prev = char
        number = int(re.findall('\d+', sequence)[0])
        sum += res * number

    print(sum)


part1("input.txt")
part2("input.txt")
