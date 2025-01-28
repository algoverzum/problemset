#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
numbers = [int(x) for x in input().split()]
numbers.sort(reverse=True)
result = []
for i in range(n):
    if i % 2 == 0:
        result.append(numbers[i])
    else:
        result.insert(0, numbers[i])
print(*result)
