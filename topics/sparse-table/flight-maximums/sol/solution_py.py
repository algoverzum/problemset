#!/usr/bin/env python3
# @check-accepted: *
from sys import stdin

input = stdin.readline


def solv():
    n, q = map(int, input().split())
    lg = [0] * (n + 1)
    for i in range(2, n + 1):
        lg[i] = lg[i // 2] + 1
    st = [[0] * (n + 1) for _ in range(18)]

    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        st[0][i] = arr[i - 1]

    for i in range(1, lg[n] + 1):
        for j in range(1, n - 2**i + 2):
            st[i][j] = max(st[i - 1][j], st[i - 1][j + 2 ** (i - 1)])

    for _ in range(q):
        s, k = map(int, input().split())
        print(st[k][s])


solv()
