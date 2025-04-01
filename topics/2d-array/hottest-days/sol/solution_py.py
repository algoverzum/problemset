#!/usr/bin/env python3
# @check-accepted: *

n, m = [int(x) for x in input().split()]
t = [[int(x) for x in input().split()] for i in range(n)]
maxi = max([max(row) for row in t])
for i in range(n):
    print(t[i].count(maxi))
