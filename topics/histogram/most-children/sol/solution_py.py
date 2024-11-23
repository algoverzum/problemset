#!/usr/bin/env python3
# @check-accepted: *

N, K = [int(x) for x in input().split()]
children_count = [0] * (N + 1)
for i in range(K):
    parent, child = [int(x) for x in input().split()]
    children_count[parent] += 1

maxi = 0
for i in range(1, N + 1):
    if children_count[i] > children_count[maxi]:
        maxi = i

print(maxi)
