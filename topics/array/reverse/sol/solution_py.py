#!/usr/bin/env python3
# @check-accepted: *

numbers = [int(x) for x in input().split()]
for i in range(13):
    print(numbers[i], end=" ")
print()
for i in range(12, -1, -1):
    print(numbers[i], end=" ")
