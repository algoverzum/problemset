#!/usr/bin/env python3
# @check-accepted: *

n, m, k = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

ans = 0
for a in A:
    for b in B:
        if a + b <= k:
            ans += 1

print(ans)
