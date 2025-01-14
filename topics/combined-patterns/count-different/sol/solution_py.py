#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
numbers = [int(x) for x in input().split()]
unique_numbers = []
for i in numbers:
    if i not in unique_numbers:
        unique_numbers.append(i)
print(len(unique_numbers))
