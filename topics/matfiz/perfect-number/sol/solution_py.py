#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
szum = 0

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        szum += i

if szum == 2 * n:
    print(1)
else:
    print(0)
