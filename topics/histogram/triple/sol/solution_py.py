#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
a = [int(x) for x in input().split()]

freq = [0] * (n + 1)

for x in a:
    freq[x] += 1

answer = -1
for num in range(1, n + 1):
    if freq[num] >= 3:
        answer = num
        break

print(answer)
