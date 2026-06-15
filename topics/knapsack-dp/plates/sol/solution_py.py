#!/usr/bin/env python3
# @check-accepted: *

from sys import stdin

input = stdin.readline

T = int(input())

for _ in range(T):
    N, K, P = map(int, input().split())

    # prefix[i][x] = az i-edik oszlop felső x tányérjának összege
    prefix = []

    for _ in range(N):
        plates = list(map(int, input().split()))

        pref = [0] * (K + 1)
        for i in range(K):
            pref[i + 1] = pref[i] + plates[i]

        prefix.append(pref)

    # dp[i][j] = maximum szépségérték,
    # ha az első i oszlopból összesen j tányért választunk
    dp = [[0] * (P + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(P + 1):
            for x in range(min(j, K) + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - x] + prefix[i - 1][x])

    print(dp[N][P])
