#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
ships = [int(x) for x in input().split()]
ships.sort(reverse=True)
formation = [0] * n
for i in range(n):
    if i % 2 == 1:
        formation[n // 2 - (i + 1) // 2] = ships[i]
    else:
        formation[n // 2 + (i + 1) // 2] = ships[i]
print(*formation)
