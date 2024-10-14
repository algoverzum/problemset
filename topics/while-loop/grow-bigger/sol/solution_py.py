#!/usr/bin/env python3
# @check-accepted: *

a = int(input())
b = int(input())

years = 0
while b >= a:
    a *= 3
    b *= 2
    years += 1

print(years)
