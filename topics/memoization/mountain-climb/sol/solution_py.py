#!/usr/bin/env python3
# @check-accepted: *

from sys import setrecursionlimit

setrecursionlimit(10**6)

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def rec(i, j):
    if memo[i][j] != -1:
        return memo[i][j]
    height = mountain[i][j]
    ret = 0
    for di, dj in moves:
        if mountain[i + di][j + dj] == height + 1:
            ret = max(ret, rec(i + di, j + dj) + 1)
    memo[i][j] = ret
    return ret


n = int(input())
mountain = [[-1] * (n + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        mountain[i][j] = row[j - 1]

memo = [[-1] * (n + 2) for _ in range(n + 2)]

maxlength = -1
maxi = -1
maxj = -1
for i in range(1, n + 1):
    for j in [1, n]:
        rec(i, j)
        if memo[i][j] > maxlength:
            maxlength = memo[i][j]
            maxi, maxj = i, j
for i in [1, n]:
    for j in range(1, n + 1):
        rec(i, j)
        if memo[i][j] > maxlength:
            maxlength = memo[i][j]
            maxi, maxj = i, j

print(maxlength)
print(maxi, maxj)
