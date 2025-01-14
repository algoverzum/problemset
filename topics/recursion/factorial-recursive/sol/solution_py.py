#!/usr/bin/env python3
# @check-accepted: *


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Do not change anything below
for i in range(1, 16):
    print(factorial(i))
