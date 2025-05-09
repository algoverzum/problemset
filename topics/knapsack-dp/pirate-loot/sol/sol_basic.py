#!/usr/bin/env python3
# @check-accepted: *

n, s = map(int, input().split())
cargo = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] + [float("inf")] * s

for value, weight in cargo:
    for i in range(weight, s + 1):
        if dp[i - weight] + value < dp[i]:
            dp[i] = dp[i - weight] + value

print(dp[s])
