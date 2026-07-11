#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
maxi = int(input())
for i in range(n - 1):
    height = int(input())
    if height > maxi:
        maxi = height
print(maxi)
