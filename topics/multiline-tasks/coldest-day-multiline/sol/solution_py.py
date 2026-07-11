#!/usr/bin/env python3
# @check-accepted: *

n = int(input())

mintemp = int(input())
minindex = 1

for i in range(2, n + 1):
    curtemp = int(input())
    if curtemp < mintemp:
        minindex = i
        mintemp = curtemp

print(mintemp)
print(minindex)
