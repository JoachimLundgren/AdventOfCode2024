import os

def parseinput(filename):
    reports = []

    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        for line in file:
            row = line.strip().split(" ")
            reports.append(list(map(int, row)))
    return reports

def isSafe(report):
    i = 0
    
    increasing = None
    while i < len(report) - 1:
        if increasing is None:
            increasing = report[i] < report[i+1]
        elif increasing and report[i] > report[i+1]:
            return False
        elif not increasing and report[i] < report[i+1]:
            return False

        diff = abs(report[i] - report[i+1])
        if (diff == 0 or diff > 3):
            return False
        
        i = i + 1
        
    return True

def isSafeWithTolerance(report):
    i = 0
    while i < len(report):
        duplicateReport = report.copy()
        duplicateReport.pop(i)
        if isSafe(duplicateReport):
            return True
        i = i + 1

    return False
    

def part1():
    reports = parseinput("input.txt")
    result = sum(isSafe(report) for report in reports)

    print(result)

def part2():
    reports = parseinput("input.txt")
    result = sum(isSafeWithTolerance(report) for report in reports)

    print(result)

part1()
part2()