import os


def parseinput(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        values = dict()
        gates = {}
        gates2 = {}
        parsingValues = True
        for line in file:
            if line == '\n':
                parsingValues = False
            elif parsingValues:
                parts = line.strip().split(': ')
                values[parts[0]] = int(parts[1])
            else:
                a, op, b, _, c = line.strip().split()
                a, b = sort(a, b)
                gates[a, b, op] = c
                gates2[c] = a, b, op

        return values, gates, gates2


def sort(a, b):
    return (a, b) if a <= b else (b, a)


def calc(gate, in1, in2):
    if in1 == None or in2 == None:
        return None

    if gate == 'AND':
        return int(in1 and in2)
    elif gate == 'OR':
        return int(in1 or in2)
    elif gate == 'XOR':
        return int(in1 != in2)


def getInt(bitlist):
    out = 0
    for bit in reversed(bitlist):
        out = (out << 1) | bit

    return out


def resolveGate(gateName, values, gates):
    a, b, op = gates[gateName]
    if a in values:
        in1 = values[a]
    else:
        in1 = resolveGate(a, values, gates)

    if b in values:
        in2 = values[b]
    else:
        in2 = resolveGate(b, values, gates)

    return calc(op, in1, in2)


def part1(input):
    values, gates, gates2 = parseinput(input)
    output = dict()
    for gate in [gate for gate in gates2 if gate.startswith('z')]:
        output[gate] = resolveGate(gate, values, gates2)

    print(getInt([v for k, v in sorted(output.items())]))


def part2(input):
    _, gates, gates2 = parseinput(input)

    def swap(a, b):
        gates2[a], gates2[b] = gates2[b], gates2[a]
        gates[gates2[a]], gates[gates2[b]] = gates[gates2[b]], gates[gates2[a]]

    # Full adder
    output = set()
    c = ''
    for i in range(int(max(gates2)[1:])):
        x = f'x{i:02}'
        y = f'y{i:02}'
        z = f'z{i:02}'
        xxy = gates[x, y, 'XOR']
        xay = gates[x, y, 'AND']
        if not c:
            c = xay
        else:
            a, b = sort(c, xxy)
            k = a, b, 'XOR'
            if k not in gates:
                a, b = list(set(gates2[z][:2]) ^ set(k[:2]))
                output.add(a)
                output.add(b)
                swap(a, b)
            elif gates[k] != z:
                output.add(gates[k])
                output.add(z)
                swap(z, gates[k])
            k = gates2[z]
            xxy = gates[x, y, 'XOR']
            xay = gates[x, y, 'AND']
            c = gates[*sort(c, xxy), 'AND']
            c = gates[*sort(c, xay), 'OR']

    print(','.join(sorted(output)))


part1("input.txt")
part2("input.txt")
