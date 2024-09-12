#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
k = 0
day = 0
while k < n:
    day += 1
    k += day
print(day)
