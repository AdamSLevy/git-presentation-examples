#! /usr/bin/python3

def printStrings(strs):
    for i in range(0, 2):
        print(strs[0])
    for i in range(0, 2):
        print(strs[1])
    for i in range(0, 2):
        print(strs[0])
        print(strs[1])

strs = ["foo", "bar"]
printStrings(strs)
