#!/usr/bin/env python3
# @check-accepted: *

import sys

input = sys.stdin.readline

n, q = map(int, input().split())
A = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + A[i]

for _ in range(q):
    t, *rest = map(int, input().split())
    if t == 1:
        k = rest[0]
        print(prefix_sum[k])
    else:
        l, r = rest
        print(prefix_sum[r] - prefix_sum[l - 1])
