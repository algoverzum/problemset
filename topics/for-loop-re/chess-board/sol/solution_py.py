#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("X", end="")
        else:
            print("Y", end="")
    print()
