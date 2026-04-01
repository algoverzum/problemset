#!/usr/bin/env python3
# @check-accepted: *

M, N = map(int, input().split())
E = []
for i in range(M):
    row = list(map(int, input().split()))
    E.append(row)
result = []
# Minden oszlopra külön-külön meghatározzuk a maxot és az első helyet
for j in range(N):
    maxVal = -1
    bestPark = 1  # 1-től indexelve

    for i in range(M):
        if E[i][j] > maxVal:
            maxVal = E[i][j]
            bestPark = i + 1

    result.append(str(bestPark))
print(" ".join(result))
