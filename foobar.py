#! /usr/bin/python3

from printers import printStringNTimes

def printAABBABAB(strs):
    printStringNTimes(strs[0], 2)
    printStringNTimes(strs[1], 2)
    for i in range(0, 2):
        print(strs[0])
        print(strs[1])

strs = ["foo", "bar"]
printAABBABAB(strs)
