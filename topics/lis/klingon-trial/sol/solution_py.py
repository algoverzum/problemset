#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
T = list(map(int, input().split()))

dp = [1] * n
for i in range(n):
    for j in range(i):
        if T[j] < T[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
