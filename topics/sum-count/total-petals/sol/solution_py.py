#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
sum = 0
for i in range(n):
    petals = int(input())
    if petals % 2 == 1:
        sum += petals

print(sum)
