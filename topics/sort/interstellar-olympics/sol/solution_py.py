#!/usr/bin/env python3
# @check-accepted: *

import functools


def compare(a, b):
    if a[0] != b[0]:
        return b[0] - a[0]
    elif a[1] != b[1]:
        return b[1] - a[1]
    elif a[2] != b[2]:
        return b[2] - a[2]
    else:
        return a[3] - b[3]


n = int(input())
medals = []
for i in range(n):
    medal = [int(x) for x in input().split()]
    tup = (medal[0], medal[1], medal[2], i + 1)
    medals.append(tup)

medals = sorted(medals, key=functools.cmp_to_key(compare))

for i in medals:
    print(i[3], end=" ")
print()
