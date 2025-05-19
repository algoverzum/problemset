#!/usr/bin/env python3
# @check-accepted: *


def holoTowerGame(n):
    dp = [False] * (n + 1)
    # dp[i] = True means the player whose turn it is can win the game of height i

    for i in range(1, n + 1):
        for move in [4, 5, 11]:
            if i - move >= 0 and not dp[i - move]:
                dp[i] = True
                break

    if dp[n]:
        return "R2-D2"
    else:
        return "C-3PO"


T = int(input())
for _ in range(T):
    N = int(input())
    print(holoTowerGame(N))
