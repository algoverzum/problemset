#!/usr/bin/env python3
# @check-accepted: *

N, K = [int(x) for x in input().split()]
children_count = []
for i in range(K):
    parent, child = [int(x) for x in input().split()]
    children_count.append(parent)
children_count.sort()
maxi = 0
maxiparent = 0
last = children_count[0] - 1
cur = 0
for parent in children_count:
    if parent == last:
        cur += 1
    else:
        last = parent
        cur = 1
    if cur > maxi:
        maxi = cur
        maxiparent = parent

print(maxiparent)
