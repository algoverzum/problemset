#!/usr/bin/env python3
# @check-accepted: examples
# @check-time-limit-exceeded: all


def solve(n):
    if n == 0:
        return 0
    return max(n, solve(n // 2) + solve(n // 3) + solve(n // 4))


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
