#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
hands = [int(x) for x in input().split()]
good_indices = []
for i in range(n):
    if hands[i] <= 4:
        good_indices.append(i + 1)

print(len(good_indices))
print(*good_indices)
