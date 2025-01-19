#!/usr/bin/env python3
# @check-accepted: examples
# @check-time-limit-exceeded: all

n = int(input())
for i in range(2**n - 1, -1, -1):
    x = bin(2**n + i)[3:]
    if "11" not in x:
        y = x.replace("1", "R")
        print(y.replace("0", "W"))
