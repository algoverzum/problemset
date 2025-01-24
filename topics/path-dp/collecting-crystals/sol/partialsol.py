#!/usr/bin/env python3
from sys import setrecursionlimit

setrecursionlimit(10**4)

N, M = [int(x) for x in input().split()]
cells = [[int(x) for x in input().split()] for _ in range(N)]
memo = {(N - 1, M - 1): cells[N - 1][M - 1]}


def dp(y, x):
    if (y, x) in memo:
        return memo[(y, x)]
    if cells[y][x] == -1:
        return -1
    if y == N - 1:
        ans = dp(y, x + 1)
        if ans == -1:
            memo[(y, x)] = -1
            return -1
        ans += cells[y][x]
        memo[(y, x)] = ans
        return ans
    if x == M - 1:
        ans = dp(y + 1, x)
        if ans == -1:
            memo[(y, x)] = -1
            return -1
        ans += cells[y][x]
        memo[(y, x)] = ans
        return ans
    ansy = dp(y + 1, x)
    ansx = dp(y, x + 1)
    if ansx == -1 and ansy == -1:
        memo[(y, x)] = -1
        return -1
    ans = cells[y][x] + max(ansx, ansy)
    memo[(y, x)] = ans
    return ans


print(dp(0, 0))
