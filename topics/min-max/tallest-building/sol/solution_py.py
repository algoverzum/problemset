#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
heights = [int(x) for x in input().split()]
maxi = heights[0]
for height in heights:
    if height > maxi:
        maxi = height
print(maxi)
