#!/usr/bin/env python3
# @check-accepted: *

n, m = [int(x) for x in input().split()]
oxi_levels = [[int(x) for x in input().split()] for i in range(n)]

highdays = []
for i in range(1, m):
    valid = True
    for j in range(n):
        if oxi_levels[j][i] <= oxi_levels[j][i - 1]:
            valid = False
            break
    if valid:
        highdays.append(i + 1)
print(len(highdays))
print(*highdays)
