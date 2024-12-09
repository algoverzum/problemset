#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
codes = input().split()
index = -1
for i in range(n - 1):
    if int(codes[i]) == int(codes[i + 1]):
        index = i
print(index + 1)
