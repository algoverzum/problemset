#!/usr/bin/env python3
# @check-accepted: *

N = int(input())
prim = [True] * (N + 1)
prim[0] = prim[1] = False

for i in range(2, N + 1):
    if prim[i]:
        j = 2
        while i * j <= N:
            prim[i * j] = False
            j += 1

for i in range(2, N + 1):
    if prim[i]:
        print(i, end=" ")
