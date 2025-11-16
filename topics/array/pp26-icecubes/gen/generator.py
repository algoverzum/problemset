#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "pp26-icecubes".

Parameters:
* N (array length)
* A (minimum value)
* B (maximum value)
* S (seed)

Constraint:
* 1 <= N <= %d
* %d <= A <= B <= %d
""" % (
    MAXN,
    MINC,
    MAXC,
)


def run(N, A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    N = randint(1, N)
    C = [randint(A, B) for _ in range(N)]

    print(N)
    print(*C)


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
