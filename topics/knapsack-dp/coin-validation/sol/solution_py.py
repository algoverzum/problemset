#!/usr/bin/env python3
# @check-accepted: *
import sys

input = sys.stdin.readline
print = sys.stdout.write
MAX_X = 100_000

n, q = map(int, input().split())
coins = list(map(int, input().split()))

DP = [False for _ in range(MAX_X + 1)]
DP[0] = True
for i in range(MAX_X + 1):
    for coin in coins:
        if i - coin >= 0:
            DP[i] = DP[i] or DP[i - coin]
            if DP[i]:
                break

for _ in range(q):
    x = int(input())
    print("YES\n" if DP[x] else "NO\n")
