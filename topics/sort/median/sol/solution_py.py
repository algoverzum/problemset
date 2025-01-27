#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
times = [int(x) for x in input().split()]
times.sort()
sol = 0
if n % 2 == 0:
    sol += times[int(n / 2) - 1]
else:
    sol += times[int(n / 2)]
print(sol)
