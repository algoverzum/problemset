#!/usr/bin/env python3
# @check-accepted: *

N, M, L = map(int, input().split())
P = []
for i in range(N):
    row = list(map(int, input().split()))
    P.append(row)
# Számoljuk, városonként hány roller töltöttsége < L
lowCount = [0] * N
for i in range(N):
    cnt = 0
    for j in range(M):
        if P[i][j] < L:
            cnt += 1
    lowCount[i] = cnt

# Keressük a maximumot
maxLow = max(lowCount)

print(maxLow)
if maxLow == 0:
    print("NINCS")
else:
    result = []
    for i in range(N):
        if lowCount[i] == maxLow:
            result.append(str(i + 1))  # városok 1-től indexelve
    print(" ".join(result))
