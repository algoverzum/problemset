#!/usr/bin/env python3
# @check-accepted: *


n, k = [int(x) for x in input().split()]
maxindex = 0
maxvalue = 0
prices = [int(x) for x in input().split()]
for i in range(n):
    if prices[i] <= k and prices[i] > maxvalue:
        maxindex = i + 1
        maxvalue = prices[i]
print(maxindex)
print(maxvalue)
