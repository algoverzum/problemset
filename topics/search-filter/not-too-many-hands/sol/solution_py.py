#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
arms = input().split()
counter = 0
numerals = []
for i in range(n):
    current = int(arms[i])
    if current <= 4:
        counter += 1
        numerals.append(i + 1)

print(counter)
for i in range(counter):
    print(numerals[i], end=" ")
print("")
