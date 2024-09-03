#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
count = 0
for i in range(n):
    petals = int(input())
    if petals % 2 == 0:
        count += 1

print(count)
