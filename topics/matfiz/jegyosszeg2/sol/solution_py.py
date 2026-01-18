#!/usr/bin/env python3
# @check-accepted: *

n = input()
sum = 0

for digit in n:
    sum += int(digit)

print(sum)
