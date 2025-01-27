#!/usr/bin/env python3
# @check-accepted: *

n, m = [int(x) for x in input().split()]
grid = []
for _ in range(n):
    line = [int(x) for x in input().split()]
    grid.append(line)

dpval = []
dpindex = []

for i in range(n + 2):
    valline = [-100 for _ in range(m)]
    indexline = [-1 for _ in range(m)]
    dpval.append(valline)
    dpindex.append(indexline)

for i in range(1, n + 1):
    dpval[i][0] = grid[i - 1][0]
    dpindex[i][0] = i

for j in range(1, m):
    for i in range(1, n + 1):
        if dpval[i - 1][j - 1] > dpval[i][j - 1] and dpval[i - 1][j - 1] > dpval[i + 1][j - 1]:
            dpindex[i][j] = dpindex[i - 1][j - 1]
            dpval[i][j] = dpval[i - 1][j - 1] + grid[i - 1][j]
        elif dpval[i][j - 1] > dpval[i - 1][j - 1] and dpval[i][j - 1] > dpval[i + 1][j - 1]:
            dpindex[i][j] = dpindex[i][j - 1]
            dpval[i][j] = dpval[i][j - 1] + grid[i - 1][j]
        else:
            dpindex[i][j] = dpindex[i + 1][j - 1]
            dpval[i][j] = dpval[i + 1][j - 1] + grid[i - 1][j]

maximal = dpval[1][m - 1]
maxindex = dpindex[1][m - 1]
for i in range(1, n + 1):
    if dpval[i][m - 1] > maximal:
        maximal = dpval[i][m - 1]
        maxindex = dpindex[i][m - 1]
print(maximal)
print(maxindex)
