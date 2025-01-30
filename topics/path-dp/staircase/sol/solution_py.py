#!/usr/bin/env python3
# @check-accepted: *

n, k = [int(x) for x in input().split()]

res = [1]
for i in range(n):
    res.append(sum(res[-k:]))

print(res[-1])
