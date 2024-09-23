#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
t = [int(x) for x in input().split()]
minindex = 0
for i in range(1, n):
    if t[i] < t[minindex]:
        minindex = i
print(t[minindex])
print(minindex + 1)
