#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "coin-validation".

Parameters:
* N (number of coins)
* Q (number of queries)
* X (upper bound)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= Q <= %d
* %d <= X <= %d
""" % (
    MIN,
    MAX_N + 1,
    MIN,
    MAX,
    MIN,
    MAX,
)


def run(N, Q, X):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]
    coins = list(range(2, X + 1))
    shuffle(coins)
    if N == MAX_N + 1:
        N -= 1
        coins[randint(0, N - 1)] = 1
    coins = coins[:N]
    shuffle(coins)
    # this can make python TLE:
    # coins.sort(key = lambda x: -x)
    print(N, Q)
    print(*coins)
    for _ in range(Q):
        print(randint(1, X))


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
