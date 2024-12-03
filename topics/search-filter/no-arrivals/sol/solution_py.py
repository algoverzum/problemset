#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
index = -1
for i in range(n):
    day = int(input())
    if day == 0:
        index = i + 1
print(index)
