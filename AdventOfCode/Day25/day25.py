import os


def parseinput(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        locks = []
        keys = []
        
        lines = file.readlines()
        i = 0
        while i < len(lines):
            if lines[i][0] == '#':
                lock = [0,0,0,0,0]
                l = 0
                while l < 7:
                    for j in range(len(lines[i].strip())):
                        if lines[i+l][j] == '#':
                            lock[j] += 1
                    l += 1
                locks.append(lock)
            elif lines[i][0] == '.':
                key = [0,0,0,0,0]
                k = 0
                while k < 7:
                    for j in range(len(lines[i].strip())):
                        if lines[i+k][j] == '.':
                            key[j] += 1
                    k += 1
                keys.append(key)
            i += 8

        return locks, keys
                    


def canUnlock(lock, key):
    for i in range(5):
        if lock[i] > key[i]:
            return False
        
    return True



def part1(input):
    locks, keys = parseinput(input)
    res = 0
    for lock in locks:
        for key in keys:
            if canUnlock(lock, key):
                res += 1

    print(res)


part1("input.txt")
