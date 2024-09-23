#!/usr/bin/env python3
# @check-accepted: *

line = input().split()
n = int(line[0])
k = int(line[1])
maximal = 0
maxindex = 0
p = input().split()
for i in range(n):
    current = int(p[i])
    if current <= k and current > maximal:
        maximal = current
        maxindex = i + 1
print(maxindex)
print(maximal)
