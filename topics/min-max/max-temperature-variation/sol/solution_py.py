#!/usr/bin/env python3
# @check-accepted: *

N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

maxdiff = B[0] - A[0]

for i in range(1, N):
    current = B[i] - A[i]
    if current > maxdiff:
        maxdiff = current

print(maxdiff)
