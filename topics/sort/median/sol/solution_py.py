#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
times = [int(x) for x in input().split()]
times.sort()
print(times[(n - 1) // 2])
