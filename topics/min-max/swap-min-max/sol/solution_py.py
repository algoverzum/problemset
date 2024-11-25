#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
candies = [int(x) for x in input().split()]
maxindex = 0
minindex = 0
for i in range(n):
    if candies[i] > candies[maxindex]:
        maxindex = i
    if candies[i] < candies[minindex]:
        minindex = i
candies[minindex], candies[maxindex] = candies[maxindex], candies[minindex]
print(*candies)
