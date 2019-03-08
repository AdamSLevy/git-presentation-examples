#! /usr/bin/python3

from printers import printNTimes

def printPattern(strs):
    printNTimes(strs[0], 2)
    printNTimes(strs[1], 2)
    for i in range(0, 2):
        print(strs[0])
        print(strs[1])

strs = ["foo", "bar"]
printPattern(strs)
