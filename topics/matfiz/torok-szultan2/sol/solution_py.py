#!/usr/bin/env python3
# @check-accepted: *

N = int(input())
cella = [False] * (N + 1)

for szolga in range(1, N + 1):
    for rab in range(szolga, N + 1, szolga):
        cella[rab] = not cella[rab]

for i in range(1, N + 1):
    if cella[i]:
        print(i, end=" ")
