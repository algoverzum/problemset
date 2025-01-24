#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
data = []
for i in range(n):
    arrival, leave = [int(x) for x in input().split()]
    data.append((arrival, 0))
    data.append((leave, 1))
result = 0
current = 0
data.sort()

for (x, y) in data:
    if y == 0:
        current += 1
        result = max(result, current)
    else:
        current -= 1

print(result)
