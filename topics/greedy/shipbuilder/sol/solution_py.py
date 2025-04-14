#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
deadlines = [int(i) for i in input().split()]
result = []
day = 1
for i, deadline in enumerate(deadlines):
    if day <= deadline:
        result.append(i + 1)
        day += 1
print(len(result))
print(*result)
