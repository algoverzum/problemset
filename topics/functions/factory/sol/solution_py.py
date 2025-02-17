#!/usr/bin/env python3
# @check-accepted: *


def first_even(numbers):
    for i, num in enumerate(numbers):
        if num % 2 == 0:
            return i + 1
    return -1


input()
A = list(map(int, input().split()))
print(first_even(A))
