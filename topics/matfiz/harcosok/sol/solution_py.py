#!/usr/bin/env python3
# @check-accepted: *

N = int(input())
A = [int(x) for x in input().split()]
A.sort()
ans = 0
for i in range(1, N, 2):
    ans += A[i] - A[i - 1]
print(ans)
