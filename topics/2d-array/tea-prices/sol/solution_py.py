#!/usr/bin/env python3
# @check-accepted: *

n, m = [int(x) for x in input().split()]
T = [[int(x) for x in input().split()] for i in range(n)]
k = int(input())
for i in range(n):
    for j in range(m):
        print(k * T[i][j], end=" ")
    print()
