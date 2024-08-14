#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
if n % 15 == 0:
    print("bumm")
elif n % 5 == 0:
    print("bamm")
elif n % 3 == 0:
    print("bimm")
else:
    print(n)
