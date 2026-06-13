#!/usr/bin/env python3
# @check-accepted: *
from sys import stdin

input = stdin.readline


def f(cen):
    x = m[0]
    res = 0
    for y in m[1:]:
        res += (y - x - 1) // cen
        x = y
    return res


n, k = map(int, input().split())
m = list(map(int, input().split()))
beg, end = 1, m[-1]
while beg < end:
    cen = (beg + end) // 2
    res = f(cen)
    if res > k:
        beg = cen + 1
    else:
        end = cen
print(beg)
