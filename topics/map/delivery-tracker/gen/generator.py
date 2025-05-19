#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "delivery-tracker".

Parameters:
* N (number of deliveries)
* M (number of places)
* C (max coordinates/packages)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= M <= N
* %d <= C <= %d
* %d <= C <= %d
""" % (
    MINN,
    MAXN,
    MINN,
    MINXY,
    MAXXY,
    MINP,
    MAXP,
)


def run(N, M, C):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    if N > 1000:
        N -= randint(0, 10)
        M = min(M, N)
    points = []
    for i in range(M):
        points.append((randint(-C, C), randint(-C, C)))
    print(N)
    for i in range(N):
        x, y = choice(points)
        print(x, y, randint(1, C))


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
