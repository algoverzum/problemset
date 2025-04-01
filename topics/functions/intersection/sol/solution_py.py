#!/usr/bin/env python3
# @check-accepted: *


def intersection(a, b):
    common = []
    for num in a:
        if num in b:
            common.append(num)
    return common


# Do not change anything below.
input()
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
print(*intersection(a, b))
