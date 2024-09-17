#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
area = 0
for i in range(n):
    side = int(input())
    area += side ** 2
print(area)
