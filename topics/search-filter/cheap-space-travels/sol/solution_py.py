#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
cheap = []
for i in range(1, n + 1):
    dist, price = [int(x) for x in input().split()]
    if price <= dist * 100:
        cheap.append(i)
print(len(cheap))
print(*cheap)
