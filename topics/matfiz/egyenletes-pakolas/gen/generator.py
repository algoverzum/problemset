#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "egyenletes-pakolas".

Parameters:
* N (minimum value)
* K (maximum value)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= K <= %d
""" % (
    MIN_N,
    MAX_N,
    MIN_K,
    MAX_K,
)


def run(N, K):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(*[N, K])
    cargo = []
    for _ in range(N):
        cargo.append(randint(MIN_S, MAX_S))
    print(*cargo)


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
