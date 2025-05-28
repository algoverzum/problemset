#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
mountain = [[-1] * (n + 2) for _ in range(n + 2)]
memo = [[-1] * (n + 2) for _ in range(n + 2)]

for i in range(1, n + 1):
    line = input().split()
    for j in range(n):
        mountain[i][j + 1] = int(line[j])


def Rec(i, j):
    if memo[i][j] != -1:
        return memo[i][j]
    else:
        heigth = mountain[i][j]
        ret = 0
        if mountain[i + 1][j] == heigth + 1:
            ret = max(ret, Rec(i + 1, j) + 1)
        if mountain[i - 1][j] == heigth + 1:
            ret = max(ret, Rec(i - 1, j) + 1)
        if mountain[i][j + 1] == heigth + 1:
            ret = max(ret, Rec(i, j + 1) + 1)
        if mountain[i][j - 1] == heigth + 1:
            ret = max(ret, Rec(i, j - 1) + 1)
        memo[i][j] = ret
        return ret


for i in range(1, n + 1):
    for j in range(1, n + 1):
        Rec(i, j)

maxlength = -1
maxi = -1
maxj = -1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(memo[i][j], end=" ")
    print()

for i in range(1, n + 1):
    if maxlength < memo[i][1]:
        maxlength = memo[i][1]
        maxi = i
        maxj = 1

for i in range(1, n + 1):
    if maxlength < memo[i][n]:
        maxlength = memo[i][n]
        maxi = i
        maxj = n

for i in range(1, n + 1):
    if maxlength < memo[1][i]:
        maxlength = memo[1][i]
        maxi = 1
        maxj = i

for i in range(1, n + 1):
    if maxlength < memo[n][i]:
        maxlength = memo[n][i]
        maxi = n
        maxj = i
print(maxlength)
print(maxi, maxj)
