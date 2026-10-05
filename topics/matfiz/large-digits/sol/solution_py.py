#!/usr/bin/env python3
# @check-accepted: *

a = int(input())
b = int(input())

A = a // 100 + (a // 10) % 10 + a % 10
B = b // 100 + (b // 10) % 10 + b % 10

if A > B:
    print(A)
else:
    print(B)
