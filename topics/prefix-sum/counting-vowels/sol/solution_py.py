#!/usr/bin/env python3
# @check-accepted: *

from sys import stdin

input = stdin.readline

S = input()
prefix = [0]
for char in S:
    if char in "aeiou":
        prefix.append(prefix[-1] + 1)
    else:
        prefix.append(prefix[-1])

Q = int(input())
for _ in range(Q):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i - 1])
