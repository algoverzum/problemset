#!/usr/bin/env python3
# @check-accepted: *

n, m = [int(x) for x in input().split()]
dp = [[int(x) for x in input().split()] for _ in range(n)]

dpindex = [[i] + [0] * (m - 1) for i in range(n)]

for j in range(1, m):
    for i in range(n):
        cur = []
        for k in [-1, 0, 1]:
            if 0 <= i + k < n:
                cur.append((dp[i + k][j - 1], -dpindex[i + k][j - 1]))
        dp[i][j] += max(cur)[0]
        dpindex[i][j] = -max(cur)[1]

maximal = dp[0][m - 1]
maxindex = dpindex[0][m - 1]
for i in range(1, n):
    if dp[i][m - 1] > maximal:
        maximal = dp[i][m - 1]
        maxindex = dpindex[i][m - 1]
print(maximal)
print(maxindex + 1)
