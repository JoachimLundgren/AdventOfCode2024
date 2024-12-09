import os


def parseinput(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        input = list(map(int, file.read()))
        files = []
        emptySpaces = []
        expandedIndex = 0
        fileIndex = 0
        file = True
        for size in input:
            if file:
                files.append((size, expandedIndex, fileIndex))
                fileIndex += 1
            else:
                emptySpaces.append((size, expandedIndex))
            file = not file
            expandedIndex += size
        return files, emptySpaces


def compact(diskmap):
    return diskmap


def getChecksum(fileSize, expandedIndex, fileId):
    i = 0
    checksum = 0
    while i < fileSize:
        checksum += expandedIndex * fileId
        expandedIndex += 1
        i += 1
    return checksum


def part1(input):
    files, emptySpaces = parseinput(input)

    checksum = 0
    file = None
    freeSpace = None
    while len(files) > 0:
        if file == None:
            file = files.pop()

        if len(emptySpaces) == 0 or (emptySpaces == None or emptySpaces[0][1] > file[1]):
            checksum += getChecksum(file[0], file[1], file[2])  # Don't move
            file = None
        else:
            if freeSpace == None:
                freeSpace = emptySpaces.pop(0)

            if file[0] < freeSpace[0]:
                checksum += getChecksum(file[0], freeSpace[1], file[2])
                freeSpace = (freeSpace[0] - file[0], freeSpace[1] + file[0])
                file = None
            else:
                checksum += getChecksum(freeSpace[0], freeSpace[1], file[2])
                if file[0] == freeSpace[0]:
                    file = None
                else:
                    file = (file[0] - freeSpace[0], file[1], file[2])
                freeSpace = None

    print(checksum)


def part2(input):
    files, emptySpaces = parseinput(input)

    checksum = 0

    while len(files) > 0:
        file = files.pop()

        freeSpace = next((space for space in emptySpaces if space[0] >= file[0]), None)
        if freeSpace == None or freeSpace[1] > file[1]:
            checksum += getChecksum(file[0], file[1], file[2])  # Don't move
        else:
            checksum += getChecksum(file[0], freeSpace[1], file[2])
            updatedFreeSpace = (freeSpace[0] - file[0], freeSpace[1] + file[0])
            if (updatedFreeSpace[0] > 0):
                emptySpaces[emptySpaces.index(freeSpace)] = updatedFreeSpace
            else:
                emptySpaces.remove(freeSpace)

    print(checksum)


part1("input.txt")
part2("input.txt")
