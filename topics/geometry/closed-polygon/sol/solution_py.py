#!/usr/bin/env python3
# @check-accepted: *

import sys

input = sys.stdin.readline


def turn(a, b, c):
    s = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    if s > 0:
        return 1
    if s < 0:
        return -1
    return 0


def solve():
    n = int(input())
    points = []

    for i in range(n):
        x, y = map(int, input().split())
        points.append([x, y, i + 1])  # x, y, id

    for i in range(1, n):
        if points[i][0] < points[0][0] or (points[i][0] == points[0][0] and points[i][1] < points[0][1]):
            points[0], points[i] = points[i], points[0]

    center = points[0]

    from functools import cmp_to_key

    def cmp(a, b):
        t = turn(center, a, b)
        if t > 0:
            return -1
        if t < 0:
            return 1
        if a[0] != b[0]:
            return -1 if a[0] < b[0] else 1
        if a[1] != b[1]:
            return -1 if a[1] < b[1] else 1
        return 0

    points[1:] = sorted(points[1:], key=cmp_to_key(cmp))

    i = n - 2
    while i >= 0 and turn(points[0], points[n - 1], points[i]) == 0:
        i -= 1

    points[i + 1 :] = reversed(points[i + 1 :])

    print(*[p[2] for p in points])


solve()
