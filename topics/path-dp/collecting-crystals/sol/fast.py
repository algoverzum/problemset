#!/usr/bin/env python3
# @check-accepted: *
from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def solv():
    N, M = map(int, input().split())
    cells = [list(map(int, input().split())) for _ in range(N)]

    for row in range(N - 1, -1, -1):
        for col in range(M - 1, -1, -1):
            if cells[row][col] == -1:
                continue

            if row == N - 1 and col == M - 1:
                continue

            best = -1

            if col + 1 < M:
                best = max(best, cells[row][col + 1])

            if row + 1 < N:
                best = max(best, cells[row + 1][col])

            if best == -1:
                cells[row][col] = -1
            else:
                cells[row][col] += best

    print(str(cells[0][0]) + "\n")

    if cells[0][0] != -1:
        x = y = 0
        for i in range(N + M - 2):
            if y == N - 1:
                x += 1
                print("R")
            elif x == M - 1:
                y += 1
                print("D")
            else:
                if cells[y][x + 1] > cells[y + 1][x]:
                    x += 1
                    print("R")
                else:
                    y += 1
                    print("D")


solv()
