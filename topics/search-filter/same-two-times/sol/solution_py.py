#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
codes = [int(x) for x in input().split()]
i = 0
while i < n - 1 and codes[i] != codes[i + 1]:
    i += 1
if i < n - 1:
    print(i + 1)
else:
    print(0)
