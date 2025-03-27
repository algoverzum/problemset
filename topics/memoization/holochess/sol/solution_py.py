#!/usr/bin/env python3
# @check-accepted: *

memo = {}


def solv(x, y):
    if (x, y) in memo:
        return memo[(x, y)]
    for stepx, stepy in [(-2, -1), (-2, 1), (1, -2), (-1, -2)]:
        if 0 < stepx + x and 0 < stepy + y:
            ans = solv(stepx + x, stepy + y)
            if ans == 2:
                memo[(x, y)] = 1
                return 1
    memo[(x, y)] = 2
    return 2


for t in range(int(input())):
    x, y = map(int, input().split())
    ans = solv(x, y)
    if ans == 2:
        print("Second")
    else:
        print("First")
