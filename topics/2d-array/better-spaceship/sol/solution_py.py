#!/usr/bin/env python3
# @check-accepted: *

n, m = [int(x) for x in input().split()]
spaceships = [[int(x) for x in input().split()] for _ in range(n)]

index = -1
for i in range(n):
    sol = False
    for j in range(n):
        better = True
        for k in range(m):
            if spaceships[i][k] <= spaceships[j][k]:
                better = False
                break
        if better:
            sol = True
            break
    if sol:
        index = i + 1
        break
print(index)
