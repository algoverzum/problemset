#!/usr/bin/env python3
# @check-accepted: *

def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(1, 1001):
    if prime(i):
        print(i, end=" ")
print()
