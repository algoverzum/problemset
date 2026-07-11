#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
k = int(input())

cheapest = -1

for i in range(n):
    distance = int(input())
    price = int(input())
    if distance >= k:
        if cheapest == -1 or cheapest > price:
            cheapest = price

print(cheapest)
