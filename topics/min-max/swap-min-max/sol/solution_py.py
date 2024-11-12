#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
candies = [int(x) for x in input().split()]
min_index = candies.index(min(candies))
max_index = candies.index(max(candies))
candies[min_index], candies[max_index] = candies[max_index], candies[min_index]
print(*candies)
