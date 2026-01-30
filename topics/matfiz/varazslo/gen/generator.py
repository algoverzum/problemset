#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "varazslo".

Parameters:
* A (length)
* S (seed)

Constraint:
* %d <= A <= %d
""" % (
    MIN,
    MAX,
)


def run(A):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    N = randint(A // 2, A)
    if N < 1:
        N = 1
    S = str(randint(1, 3))
    while len(S) + 2 <= N:
        S += "+" + str(randint(1, 3))

    print(S)


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
