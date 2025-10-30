#!/usr/bin/env python3
# @check-accepted: *

A = int(input())
B = int(input())
SA = 0
SB = 0
for i in range(3):
    SA += A % 10
    A //= 10
    SB += B % 10
    B //= 10
if SA >= SB:
    print(SA)
else:
    print(SB)
