#!/usr/bin/env python3
# @check-accepted: *

n, m = input().split()
n = int(n)
m = int(m)

oxi_levels = []
for i in range(n):
    line = input().split()
    oxi_levels.append(line)
highdays = []
for i in range(1, m):
    valid = True
    for j in range(n):
        valid &= int(oxi_levels[j][i]) > int(oxi_levels[j][i - 1])
    if valid:
        highdays.append(i + 1)
print(len(highdays))
print(*highdays)
