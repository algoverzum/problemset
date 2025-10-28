#!/usr/bin/env python3
# @check-accepted: *

a = int(input())
b = int(input())

while b:
    a, b = b, a % b

print(a)
