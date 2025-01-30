#!/usr/bin/env python3
# @check-accepted: *

n, m = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for i in range(n)]
c = int(input())
for i in range(n):
    for j in range(m):
        print(c * A[i][j], end=" ")
    print()
