#!/usr/bin/env python3
# @check-accepted: *

n, m = [int(x) for x in input().split()]
powercells = [[int(x) for x in input().split()] for _ in range(n)]

maxi = 0
maxj = 0
for i in range(n):
    for j in range(m):
        if powercells[i][j] > powercells[maxi][maxj]:
            maxi = i
            maxj = j
print(maxi + 1, maxj + 1)
