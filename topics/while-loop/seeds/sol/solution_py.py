#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
seeds = 1
while seeds < n:
    seeds *= 3
print(seeds)
