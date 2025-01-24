#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
T = [int(x) for x in input().split()]
T.sort()
maxi = T[1] - T[0]
for i in range(2, n):
    maxi = max(maxi, T[i] - T[i - 1])

print(maxi)
