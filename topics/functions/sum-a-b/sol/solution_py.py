#!/usr/bin/env python3
# @check-accepted: *

def sum_between(a, b):
    return sum(range(a, b + 1))

print(sum_between(3, 5))
print(sum_between(0, 10))
print(sum_between(42, 42))
print(sum_between(-1, 1))
print(sum_between(-5, 3))
print(sum_between(100, 1000))
print(sum_between(3141, 5926))
print(sum_between(1, 10000))
