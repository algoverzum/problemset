#!/usr/bin/env python3
# @check-accepted: *

N = int(input())
A = int(input())
B = int(input())

maxdiff = B - A

for i in range(N - 1):
    A = int(input())
    B = int(input())
    if B - A > maxdiff:
        maxdiff = B - A

print(maxdiff)
