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
* %d <= B <= %d
* %d <= R <= %d
* %d <= C <= %d
""" % (
    MIN,
    MAX,
    MIN_ROAD,
    MAX_ROAD,
    MIN - 1,
    MAX - 1,
    MIN - 1,
    MAX - 1,
)


def run(N, B, R, C):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

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
