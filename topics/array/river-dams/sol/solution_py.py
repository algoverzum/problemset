#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
width = [int(x) for x in input().split()]

count = 0
for i in range(1, n - 1):
    if width[i - 1] < width[i] and width[i] > width[i + 1]:
        count += 1

print(count)
