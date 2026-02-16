#!/usr/bin/env python3
# @check-accepted: *

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

def collected_wood(H):
    total = 0
    for a in A:
        if a > H:
            total += a - H
    return total

lo = 0
hi = 10**9

while hi - lo > 1:
    mid = (lo + hi) // 2
    if collected_wood(mid) >= M:
        lo = mid
    else:
        hi = mid

print(lo)
