#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
arrivals = [0] * 1000001
leaves = [0] * 1000001
for i in range(n):
    arrival, leave = [int(x) for x in input().split()]
    arrivals[arrival] += 1
    leaves[leave] += 1
result = 0
current = 0
for i in range(1000001):
    current += arrivals[i]
    result = max(result, current)
    current -= leaves[i]
print(result)
