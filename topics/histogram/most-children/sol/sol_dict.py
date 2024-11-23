#!/usr/bin/env python3
# @check-accepted: *

N, K = [int(x) for x in input().split()]
children_count = {}
for i in range(K):
    parent, child = [int(x) for x in input().split()]
    children_count[parent] = children_count.get(parent, 0) + 1

maxi = next(iter(children_count))
for parent in children_count:
    if children_count[parent] > children_count[maxi]:
        maxi = parent
    elif children_count[parent] == children_count[maxi]:
        if parent < maxi:
            maxi = parent
print(maxi)
