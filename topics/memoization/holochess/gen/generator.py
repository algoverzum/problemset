#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "holochess".

Parameters:
* T (number of testcases)
* N (maximum value)
* S (seed)

Constraint:
* %d <= T <= %d
* %d <= N <= %d
""" % (
    MINT,
    MAXT,
    MIN,
    MAX,
)


def run(T, N):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    tests = set()
    while len(tests) < T:
        x = randint(1, N)
        y = randint(1, N)
        tests.add((x, y))
    print(T)
    for (x, y) in tests:
        print(x, y)


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
