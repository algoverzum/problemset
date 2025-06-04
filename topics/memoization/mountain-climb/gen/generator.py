#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "mountain-climb".

Parameters:
* N (value of n)
* B (intended length of road)
* R (row of start point)
* C (column of start point)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= R <= %d
* %d <= C <= %d
""" % (
    MINN,
    MAXN,
    MINN - 1,
    MAXN - 1,
    MINN - 1,
    MAXN - 1,
)


def run(N, B, R, C):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    if B <= 15:
        print(N)
        array = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                array[i][j] = randint(1, N)

        row_cord = R
        col_cord = C
        for d in range(1, B + 1):
            array[R][C] = d
            if randint(1, 2) == 1:
                if R == 0:
                    R += 1
                elif R == N - 1:
                    R -= 1
                else:
                    R += (randint(0, 1) * 2) - 1
            else:
                if C == 0:
                    C += 1
                elif C == N - 1:
                    C -= 1
                else:
                    C += (randint(0, 1) * 2) - 1
        for i in range(N):
            print(*array[i])
    elif B == 20:
        if N >= 100:
            N -= randint(0, 10)
        print(N)
        for i in range(N):
            line = list(range(i * N + 1, (i + 1) * N + 1))
            if i % 2 == 1:
                print(*line)
            else:
                print(*line[::-1])
    elif B == 30:
        if N >= 100:
            N -= randint(0, 10)
        board = [[-1] * N for i in range(N)]
        i = randint(0, N - 1)
        j = randint(0, N - 1)
        if 0 < i < N - 1 and 0 < j < N - 1:
            if randint(0, 1) == 0:
                i = 0
            else:
                j = 0
        cell = (i, j)
        board[i][j] = randint(1, 10**R)

        def szomsz(cell):
            res = []
            i, j = cell
            if i > 0:
                res.append((i - 1, j))
            if j > 0:
                res.append((i, j - 1))
            if j < N - 1:
                res.append((i, j + 1))
            if i < N - 1:
                res.append((i + 1, j))
            return res

        while True:
            # print(cell,board)
            kov = szomsz(cell)
            # print(cell,kov)
            shuffle(kov)
            # print(cell,kov)
            ok = False
            for row, col in kov:
                if board[row][col] == -1:
                    board[row][col] = board[cell[0]][cell[1]] + 1
                    ok = True
                    cell = (row, col)
                    break
            if not ok:
                break
        for i in range(N):
            for j in range(N):
                if board[i][j] == -1:
                    kov = szomsz((i, j))
                    for row, col in kov:
                        board[i][j] = max(board[i][j], board[row][col] + 1)
                    if board[i][j] <= 0:
                        board[i][j] = randint(1, 10**R)
        print(N)
        for line in board:
            print(*line)
    elif B == 40:
        if N >= 100:
            N -= randint(0, 10)
        board = [[-1] * N for i in range(N)]

        def start(board):
            res = []
            for i in range(N):
                if board[0][i] == -1:
                    res.append((0, i))
                if board[N - 1][i] == -1:
                    res.append((N - 1, i))
            for j in range(1, N - 1):
                if board[j][0] == -1:
                    res.append((j, 0))
                if board[j][N - 1] == -1:
                    res.append((j, N - 1))
            return res

        cur = start(board)
        while cur:
            shuffle(cur)
            cell = cur[0]
            i, j = cell
            board[i][j] = randint(1, 10**R)

            def szomsz(cell):
                res = []
                i, j = cell
                if i > 0:
                    res.append((i - 1, j))
                if j > 0:
                    res.append((i, j - 1))
                if j < N - 1:
                    res.append((i, j + 1))
                if i < N - 1:
                    res.append((i + 1, j))
                return res

            while True:
                # print(cell,board)
                kov = szomsz(cell)
                # print(cell,kov)
                shuffle(kov)
                # print(cell,kov)
                ok = False
                for row, col in kov:
                    if board[row][col] == -1:
                        board[row][col] = board[cell[0]][cell[1]] + 1
                        ok = True
                        cell = (row, col)
                        break
                if not ok:
                    break
            cur = start(board)
        for i in range(N):
            for j in range(N):
                if board[i][j] == -1:
                    kov = szomsz((i, j))
                    for row, col in kov:
                        board[i][j] = max(board[i][j], board[row][col] + 1)
                    if board[i][j] <= 0:
                        board[i][j] = randint(1, 10**R)
        print(N)
        for line in board:
            print(*line)
    else:
        pass


if __name__ == "__main__":
    num_args = len(signature(run).parameters) + 2
    if len(argv) != num_args:
        print("Got %d parameters, expecting %d" % (len(argv), num_args), file=stderr)
        print(usage, file=stderr)
        exit(1)

    def tryconv(x):
        for t in [int, float, str]:
            try:
                return t(x)
            except:
                pass

    *args, S = map(tryconv, argv[1:])
    seed(S)
    run(*args)
