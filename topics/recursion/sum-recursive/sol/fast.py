#!/usr/bin/env python3
# @check-accepted: *


def summa(a, b):
    if a == b:
        return a
    mid = (a + b) // 2
    return summa(a, mid) + summa(mid + 1, b)


a, b = map(int, input().split())
print(summa(a, b))
