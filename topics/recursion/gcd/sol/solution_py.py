#!/usr/bin/env python3
# @check-accepted: *
from sys import setrecursionlimit

setrecursionlimit(10**5)


def gcd(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    return gcd(a, b - a)


# Do not change anything below.
a, b = map(int, input().split())
print(gcd(a, b))
