#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
S = [int(x) for x in input().split()]
S.sort()
length = 0
for si in S:
    if si > length:
        length += 1
print(length)
