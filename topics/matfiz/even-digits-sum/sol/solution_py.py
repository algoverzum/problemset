#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
szum = 0

while n:
    jegy = n % 10
    if jegy % 2 == 0:
        szum += jegy
    n //= 10

print(szum)
