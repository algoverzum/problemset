#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
A = [int(x) for x in input().split()]
ans = []
for i in range(1, n - 1):
    if 2 * A[i] == A[i - 1] + A[i + 1]:
        ans.append(A[i])
print(*ans)
