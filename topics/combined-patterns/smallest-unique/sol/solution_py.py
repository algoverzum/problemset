#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
numbers = [int(x) for x in input().split()]
unique_numbers = []
for i in numbers:
    if numbers.count(i) == 1:
        unique_numbers.append(i)
if len(unique_numbers) == 0:
    print(-1)
else:
    print(min(unique_numbers))
