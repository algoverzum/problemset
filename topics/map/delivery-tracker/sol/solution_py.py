#!/usr/bin/env python3
# @check-accepted: *

n = int(input())

deliveries = {}

for line in range(n):
    x, y, p = [int(x) for x in input().split()]
    deliveries[(x, y)] = deliveries.get((x, y), 0) + p

max_packages = max(deliveries.values())

for (x, y) in deliveries:
    if deliveries[(x, y)] == max_packages:
        print(x, y, max_packages)
        break
