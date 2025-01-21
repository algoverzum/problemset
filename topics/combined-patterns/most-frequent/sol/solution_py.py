#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
a = [int(x) for x in input().split()]

mostFrequent = a[0]
maxCount = 1

for number in a:
    cnt = a.count(number)
    if cnt > maxCount:
        mostFrequent = number
        maxCount = cnt
    elif cnt == maxCount:
        mostFrequent = min(mostFrequent, number)

print(mostFrequent)
