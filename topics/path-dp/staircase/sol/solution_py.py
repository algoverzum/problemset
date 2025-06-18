#!/usr/bin/env python3
# @check-accepted: *

n, k = [int(x) for x in input().split()]

dp = [1]
for i in range(n):
    dp.append(sum(dp[-k:]))

print(dp[-1])
