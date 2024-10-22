#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
young_adults = 0
for i in range(n):
    age = int(input())
    if age >= 18 and age < 21:
        young_adults += 1
print(young_adults // 3)
