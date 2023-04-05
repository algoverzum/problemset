#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "asteroid-queries".

Parameters:
* N (array length)
* Q (queries)
* V (maximum value)
* S (seed)

Constraint:
* 1 <= N <= %d
* 1 <= Q <= %d
* 0 <= V <= %d
""" % (
    MAX_N,
    MAX_Q,
    MAX_V,
)


def run(N, Q, V):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    V = [randint(0, V) for _ in range(N)]

    print(N, Q)
    print(*V)
    for _ in range(Q):
        T = randint(1, 2)
        if T == 1:
            print(T, randint(1, N))
        else:
            L = randint(1, N)
            print(T, L, randint(L, N))


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
