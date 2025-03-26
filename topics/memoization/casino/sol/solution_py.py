#!/usr/bin/env python3
# @check-accepted: *

memo = {}
memo[0] = 0


def solve(n):
    if n in memo:
        return memo[n]
    ans = max(n, solve(n // 2) + solve(n // 3) + solve(n // 4))
    memo[n] = ans
    return ans


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
