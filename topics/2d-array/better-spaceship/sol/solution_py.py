#!/usr/bin/env python3
# @check-accepted: *

n, m = [int(x) for x in input().split()]
spaceships = []
for _ in range(n):
    spaceships.append([int(x) for x in input().split()])

index = -1
for i in range(n):
    sol = False
    for j in range(n):
        better = True
        for k in range(m):
            better &= spaceships[i][k] > spaceships[j][k]
        if better:
            sol = True
    if sol and index != -1:
        index = i + 1
print(index)
