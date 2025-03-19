#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
droids = [int(x) for x in input().split()]
cnt = [0] * 11
for type in droids:
    cnt[type] += 1
print(max(cnt))
