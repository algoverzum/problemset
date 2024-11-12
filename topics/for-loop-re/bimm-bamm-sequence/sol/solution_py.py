#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
for i in range(1, n + 1):
    if i % 15 == 0:
        print("bumm")
    elif i % 3 == 0:
        print("bimm")
    elif i % 5 == 0:
        print("bamm")
    else:
        print(i)
