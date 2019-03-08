#! /usr/bin/python3

from printers import printStringNTimes

# Prints the pattern AABBABAB for two strings in an array, A and B,
# respectively.
def printPattern(strs):
    printStringNTimes(strs[0], 2)
    printStringNTimes(strs[1], 2)
    for i in range(0, 2):
        print(strs[0])
        print(strs[1])

strs = ["foo", "bar"]
printPattern(strs)
