#!/usr/bin/env python3
# @check-accepted: *

import sys

input = sys.stdin.readline

T = int(input())
ans = []

for _ in range(T):
    N, K, P = map(int, input().split())

    prefix = []

    for _ in range(N):
        arr = list(map(int, input().split()))

        pref = [0] * (K + 1)
        s = 0
        for i in range(K):
            s += arr[i]
            pref[i + 1] = s

        prefix.append(pref)

    # dp[j] = max value using processed stacks, picking j plates
    dp = [0] * (P + 1)

    for pref in prefix:
        new_dp = dp[:]  # copy previous state

        for j in range(P + 1):
            limit = min(j, K)
            best = dp[j]

            for x in range(1, limit + 1):
                val = dp[j - x] + pref[x]
                if val > best:
                    best = val

            new_dp[j] = best

        dp = new_dp

    ans.append(str(dp[P]))

print("\n".join(ans))
