#!/usr/bin/env python3
# @check-accepted: *

N, M = [int(x) for x in input().split()]
days = [0] * (N + 1)
for i in range(M):
    F, L = [int(x) for x in input().split()]
    for j in range(F, L + 1):
        days[j] += 1
longest = 0
last_at_least_two = 0
start = end = 0
for i in range(1, N + 1):
    if days[i] >= 2:
        last_at_least_two = i
    else:
        if i - last_at_least_two > longest:
            longest = i - last_at_least_two
            start = 1 + last_at_least_two
            end = i

if longest > 0:
    print(start, end)
else:
    print(0)
