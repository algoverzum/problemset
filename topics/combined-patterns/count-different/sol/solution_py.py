#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
numbers = [int(x) for x in input().split()]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(len(unique_numbers))
