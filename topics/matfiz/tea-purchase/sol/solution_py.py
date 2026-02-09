#!/usr/bin/env python3
# @check-accepted: *

N = int(input())

max_amount = -1
max_index = -1

for i in range(1, N + 1):
    tea = input()
    amount = int(input())

    if amount > max_amount:
        max_amount = amount
        max_index = i

print(max_index)
