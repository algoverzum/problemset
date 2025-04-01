#!/usr/bin/env python3
# @check-accepted: *


def odd_numbers(numbers):
    odd = []
    for num in numbers:
        if num % 2 == 1:
            odd.append(num)
    return odd


# Do not change anything below.
input()
numbers = [int(x) for x in input().split()]
print(*odd_numbers(numbers))
