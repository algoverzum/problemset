#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
divisor = 2
while n % divisor != 0:
    divisor += 1
print(divisor)
