#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
weights = [int(x) for x in input().split()]

pair_count = 0
for i in range(n):
    for j in range(i + 1, n):
        if weights[i] == weights[j]:
            pair_count += 1

print(pair_count)
