#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "spicy-mix".

Parameters:
* N (N value)
* M (M value)
* K (K value)
* maxi (maximum value)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= M <= %d
* %d <= K <= %d
* %d <= maxi <= %d
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
    MINK,
    MAXK,
    MIN,
    MAX,
)


def run(N, M, K, maxi):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    N = randint(1, N)
    A = [randint(1, maxi) for i in range(N)]
    M = randint(1, M)
    B = [randint(1, maxi) for i in range(M)]
    K = randint(1, K)

    print(N, M, K)
    print(*A)
    print(*B)


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
