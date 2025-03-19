#!/usr/bin/env python3
# @check-accepted: *


def first_even(numbers):
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            return i
    return -1


input()
numbers = [int(x) for x in input().split()]
print(first_even(numbers))
