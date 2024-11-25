#!/usr/bin/env python3
# @check-accepted: *

n, k = [int(x) for x in input().split()]
distance = [int(x) for x in input().split()]
price = [int(x) for x in input().split()]

cheapest = -1

for i in range(n):
    if distance[i] >= k:
        if cheapest == -1 or cheapest > price[i]:
            cheapest = price[i]

print(cheapest)
