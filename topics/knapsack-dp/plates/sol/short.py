#!/usr/bin/env python3
# @check-accepted: *

import sys

input = sys.stdin.readline

for t in range(int(input())):
    n, k, p = map(int, input().split())
    last_dp = [0] * (p + 1)
    for i in range(n):
        dp = last_dp[:]
        a = map(int, input().split())
        s = 0
        for j, x in enumerate(a):
            s += x
            for l in range(p - j - 1, -1, -1):
                dp[l + j + 1] = max(dp[l + j + 1], last_dp[l] + s)
        last_dp = dp
    print(dp[p])
