#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
young_adults = 0
for i in range(n):
    a_i = int(input())
    if a_i >= 18 and a_i < 21:
        young_adults += 1
print(young_adults // 3)
