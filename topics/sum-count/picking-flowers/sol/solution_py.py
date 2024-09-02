#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
count = 0
for i in range(n):
    inp = int(input())
    if inp % 2 == 0:
        count += 1

print(count)
