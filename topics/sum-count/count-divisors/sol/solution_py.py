#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
divisors = 0
for i in range(1, n + 1):
    if n % i == 0:
        divisors = divisors + 1
print(divisors)
