#!/usr/bin/env python3
# @check-accepted: *

from math import gcd


def is_power_of_two(x):
    return x & (x - 1) == 0


def solve():
    P = int(input())
    Q = int(input())
    g = gcd(P, Q)
    P //= g
    Q //= g

    if not is_power_of_two(Q):
        return "impossible"

    gen = 0
    while P < Q:
        P *= 2
        gen += 1
    return gen


print(solve())
