#!/usr/bin/env python3
# @check-accepted: *

N = int(input())
A = [int(x) for x in input().split()]
A.sort()
ans = 0
for i in range(N // 2):
    ans += A[2 * i + 1] - A[2 * i]
print(ans)
