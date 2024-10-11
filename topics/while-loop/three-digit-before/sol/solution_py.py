#!/usr/bin/env python3
# @check-accepted: *

count = 0
current = -1
while current != 0:
    current = int(input())
    if 100 <= current <= 999:
        count += 1
print(count)
