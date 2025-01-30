#!/usr/bin/env python3
# @check-accepted: *

n, m = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for i in range(n)]
i, j = [int(x) for x in input().split()]

i -= 1
j -= 1

for row in range(n):
    A[row][i], A[row][j] = A[row][j], A[row][i]

for row in A:
    print(*row)
