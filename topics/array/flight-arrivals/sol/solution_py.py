#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
flights = [int(x) for x in input().split()]
for i in range(0, n, 2):
    print(flights[i], end=" ")
print()
print(*[flights[i] for i in range(1, n, 2)])
