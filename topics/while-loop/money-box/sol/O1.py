#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
day = int((2 * n) ** 0.5)
if n <= day * (day + 1) // 2:
    print(day)
else:
    print(day + 1)
