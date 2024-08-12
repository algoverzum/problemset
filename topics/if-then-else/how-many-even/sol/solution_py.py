#!/usr/bin/env python3
# @check-accepted: *

A = int(input())
B = int(input())
result = 0
if A % 2 == 0:
    result += 1
if B % 2 == 0:
    result += 1
print(result)
