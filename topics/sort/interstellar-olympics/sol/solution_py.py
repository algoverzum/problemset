#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
medals = []
for i in range(n):
    gold, silver, bronz = [int(x) for x in input().split()]
    tup = (-gold, -silver, -bronz, i + 1)
    medals.append(tup)

medals.sort()

for line in medals:
    print(line[3], end=" ")
