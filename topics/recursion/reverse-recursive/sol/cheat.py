#!/usr/bin/env python3
# @check-accepted: *

A = []
x = 1
while x != 0:
    x = int(input())
    A.append(x)

for a in A[::-1]:
    print(a)
