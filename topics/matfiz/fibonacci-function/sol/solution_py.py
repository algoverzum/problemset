#!/usr/bin/env python3
# @check-accepted: *


def fibonacci(t, n):
    t.append(0)
    t.append(1)
    for i in range(2, n):
        t.append(t[i - 1] + t[i - 2])


n = int(input())
t = []
fibonacci(t, n)
print(" ".join(str(x) for x in t))
