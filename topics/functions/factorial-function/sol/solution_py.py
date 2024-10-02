#!/usr/bin/env python3
# @check-accepted: *

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

for i in range(1, 16):
    print(factorial(i))
