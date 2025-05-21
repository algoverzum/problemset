#!/usr/bin/env python3
# @check-accepted: *

memo = [[0] * 101 for _ in range(101)]


def winner(x, y):
    if x < 1 or x > 100 or y < 1 or y > 100:
        return 1
    if memo[x][y] != 0:
        return memo[x][y]

    moves = [(-2, -1), (-2, 1), (1, -2), (-1, -2)]
    for stepx, stepy in moves:
        if winner(x + stepx, y + stepy) == 2:
            memo[x][y] = 1
            return 1

    memo[x][y] = 2
    return 2


t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print("Second" if winner(x, y) == 2 else "First")
