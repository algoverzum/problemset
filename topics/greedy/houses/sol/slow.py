#!/usr/bin/env python3
# @check-accepted: *

T = int(input())
for _ in range(T):
    N, B = [int(x) for x in input().split()]
    prices = [int(x) for x in input().split()]

    prices.sort()
    count = 0
    total = 0

    for price in prices:
        if total + price <= B:
            total += price
            count += 1
        else:
            break

    print(count)
