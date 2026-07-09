#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
k = int(input())
maxindex = 0
maxvalue = 0
for i in range(n):
    price = int(input())
    if maxvalue < price <= k:
        maxindex = i + 1
        maxvalue = price
print(maxindex)
print(maxvalue)
