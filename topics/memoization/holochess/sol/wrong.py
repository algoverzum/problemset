#!/usr/bin/env python3

T = int(input())
res = {}


def f(x, y):
    if x < 1 or y < 1:
        return 1
    if (x, y) in res:
        return res[(x, y)]
    a = max(f(x - 2, y + 1), f(x - 2, y - 1), f(x - 1, y - 2), f(x + 1, y - 2))
    res[(x, y)] = 3 - a
    return 3 - a


for _ in range(T):
    X, Y = [int(x) for x in input().split()]
    print(["", "First", "Second"][f(X, Y)])
