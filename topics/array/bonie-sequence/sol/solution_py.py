#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
bonie = [0] * (n + 1)
bonie[0] = 1
bonie[1] = 1
for i in range(2, n + 1):
    bonie[i] = bonie[i - 1] + bonie[i - 2]
print(*bonie)
