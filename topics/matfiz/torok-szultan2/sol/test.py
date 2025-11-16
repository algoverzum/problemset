#!/usr/bin/env python3

ZAR = 0
NYIT = 1

N = int(input())
cella = [ZAR] * (N + 1)

for rab in range(1, N + 1):
    for szolga in range(1, N + 1):
        if rab % szolga == 0:
            # állapotváltás
            if cella[rab] == NYIT:
                cella[rab] = ZAR
            else:
                cella[rab] = NYIT

res = []
for i in range(1, N + 1):
    if cella[i] == NYIT:
        res.append(i)
print(*res)
