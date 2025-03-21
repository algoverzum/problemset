#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
droids = list(map(int, input().split()))
histogram = {}
for i in range(n):
    if droids[i] not in histogram:
        histogram[droids[i]] = i
    else:
        print(histogram[droids[i]], i)
        exit()
print(-1)
