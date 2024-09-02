#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
prod = 1
for i in range(1, n + 1):
    prod *= i
print(prod)
