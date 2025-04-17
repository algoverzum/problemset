#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
droids = list(map(int, input().split()))
index = {}
for i in range(n):
    if droids[i] in index:
        print(index[droids[i]], i + 1)
        exit()
    index[droids[i]] = i + 1
print(-1)
