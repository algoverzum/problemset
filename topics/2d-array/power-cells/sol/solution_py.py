#!/usr/bin/env python3
# @check-accepted: *

n, m = [int(x) for x in input().split()]
powercells = []
for _ in range(n):
    line = [int(x) for x in input().split()]
    powercells.append(line)

maximal = powercells[0][0]
maxindexi = 0
maxindexj = 0
for i in range(n):
    for j in range(m):
        if powercells[i][j] > maximal:
            maximal = powercells[i][j]
            maxindexi = i
            maxindexj = j
print(maxindexi, end=" ")
print(maxindexj)
