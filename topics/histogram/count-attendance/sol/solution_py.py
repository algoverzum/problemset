#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
attendances = [int(x) for x in input().split()]

histogram = [0] * 11

for attendance in attendances:
    histogram[attendance] += 1

print(*histogram)
