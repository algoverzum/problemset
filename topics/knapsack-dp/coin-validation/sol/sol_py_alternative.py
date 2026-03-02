#!/usr/bin/env python3
# @check-accepted: *

from sys import stdin, stdout

input = stdin.readline


def solv():
    N, Q = map(int, input().split())
    C = list(map(int, input().split()))

    DP = [True] + [False] * (100000)
    for i in range(1, 100001):
        for c in C:
            x = i - c
            if x >= 0 and DP[x]:
                DP[i] = True
                break

    ans = ["YES" if DP[int(input())] else "NO" for i in range(Q)]
    stdout.write("\n".join(ans))


solv()
