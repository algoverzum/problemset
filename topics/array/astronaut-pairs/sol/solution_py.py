#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
weights = input().split(" ")

pair_count = 0
for i in range(n):
    for j in range(i + 1, n):
        if int(weights[i]) == int(weights[j]):
            pair_count += 1

print(pair_count)
