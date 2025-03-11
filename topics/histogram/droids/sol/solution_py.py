#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
droids = [int(x) for x in input().split()]
histogram = [0] * 11
for type in droids:
    histogram[type] += 1
print(max(histogram))
