#!/usr/bin/env python3
# @check-accepted: *

ZAR = 0
NYIT = 1

N = int(input())
cella = [ZAR] * (N + 1)

for rab in range(1, N + 1):
    for szolga in range(1, N + 1):
        if rab % szolga == 0:
            cella[rab] = 1 - cella[rab]

for i in range(1, N + 1):
    if cella[i] == NYIT:
        print(i, end=" ")
