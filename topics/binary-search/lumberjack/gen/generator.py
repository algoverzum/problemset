#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "lumberjack".

Parameters:
* N (minimum value)
* A (maximum value)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= A <= %d
""" % (
    MIN,
    MAXN,
    MIN,
    MAXA,
)


def run(N, A):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    N = randint (3*N//4, N)
    if N < 1: N = 1

    X = [randint(1,A) for i in range(N)]
    M = randint(1,min(sum(X),MAXM))
    
    print(N, M)
    print(*X)


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
