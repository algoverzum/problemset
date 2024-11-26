#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "more-oxygen".

Parameters:
* N (value of N)
* M (value of M)
* A (minimum value)
* B (maximum value)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= M <= %d
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MIN_N,
    MAX_N,
    MIN_M,
    MAX_M,
    MIN_A,
    MAX_A,
    MIN_A,
    MAX_A,
)


def run(N, M, A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(*[N, M])
    days = []
    for _ in range(N):
        days.append([randint(A, B - 2)])
    for i in range(1, M):
        val = randint(1, 10)
        if val < 3:
            for j in range(N):
                days[j].append(randint(days[j][i - 1], B))
        else:
            for j in range(N):
                days[j].append(randint(A, B - 2))

    for ar in days:
        print(*ar)


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
