#!/usr/bin/env python3
# @check-accepted: *
from sys import setrecursionlimit

setrecursionlimit(10**7)


def summa(a, b):
    if a == b:
        return a
    return b + summa(a, b - 1)


# Do not change anything below.
a, b = map(int, input().split())
print(summa(a, b))
