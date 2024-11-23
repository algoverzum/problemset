#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
attendances = [int(x) for x in input().split()]

histogram = []
for i in range(11):
    cur = 0
    for a in attendances:
        if a == i:
            cur += 1
    histogram.append(cur)

print(*histogram)
