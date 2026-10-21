#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "szallitas".

Parameters:
* N (value of N)
* K (value of K)
* Sa (value of S)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= K <= %d
* %d <= Sa <= %d
""" % (
    MIN_N,
    MAX_N,
    MIN_K,
    MAX_K,
    MIN_S,
    MAX_S,
)


def run(N, K, Sa):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(*[N, K, Sa])
    objects = []
    for _ in range(N):
        objects.append(randint(1, Sa))
    print(*objects)


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
