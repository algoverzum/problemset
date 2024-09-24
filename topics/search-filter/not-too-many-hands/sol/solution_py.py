#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
arms = [int(i) for i in input().split()]
numerals = []
for i in range(n):
    current = int(arms[i])
    if current <= 4:
        numerals.append(i + 1)

print(len(numerals))
print(*numerals)
print("")
