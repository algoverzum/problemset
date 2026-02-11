#!/usr/bin/env python3
# @check-accepted: *

# bemenet beolvasása
N, M = map(int, input().split())
lengths = [0] * M
for i in range(M):
    K, V = map(int, input().split())
    lengths[i] = V - K + 1  # hossz km-ben

# minimum hossz keresése
minLen = lengths[0]
for i in range(1, M):
    if lengths[i] < minLen:
        minLen = lengths[i]

print(minLen)
for i in range(M):
    if lengths[i] == minLen:
        print(i + 1)  # sorszám 1-től
