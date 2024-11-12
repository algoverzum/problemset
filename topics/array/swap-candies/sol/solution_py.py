#!/usr/bin/env python3
# @check-accepted: *
n = int(input())
candies = [int(x) for x in input().split()]
for i in range(0, len(candies) - 1, 2):
    candies[i], candies[i + 1] = candies[i + 1], candies[i]
print(*candies)
