#!/usr/bin/env python3
# @check-accepted: *
n, k = map(int, input().split())
m = list(map(int, input().split()))

diffs = [m[i + 1] - m[i] for i in range(n - 1)]

lo = 0
hi = max(diffs)

while hi - lo > 1:
    mid = (lo + hi) // 2

    needed = 0
    for d in diffs:
        needed += (d - 1) // mid

    if needed <= k:
        hi = mid
    else:
        lo = mid

print(hi)
