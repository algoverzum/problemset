#!/usr/bin/env python3
# @check-accepted: *

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

result = -1

for i in range(N):
    if A[i] >= K:
        if result < B[i]:
            result = B[i]
        if result == -1:
            result = B[i]

print(result)
