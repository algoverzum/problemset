#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "museum".

Parameters:
* N (days)
* M (guards)
* L (max interval length)
* X (non working days at beggining and end)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= M <= %d
* %d <= L <= %d
* 0 <= X <= N//3
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
    MIN,
    MAX,
)


def run(N, M, L, X):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    n = randint(2 * N // 3, N)
    m = randint(2 * M // 3, M)
    while 1 + X >= n - X:
        n = randint(2 * N // 3, N)

    intervalls = set()
    while len(intervalls) < m:
        a = randint(1 + X, n - X)
        b = min(randint(a, a + L), n - X)
        intervalls.add((a, b))

    print(n, m)
    for a, b in intervalls:
        print(a, b)


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
