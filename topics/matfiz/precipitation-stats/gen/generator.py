#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "precipitation-stats".

Parameters:
* N (number of rows)
* S (seed)

Constraint:
* %d <= N <= %d
""" % (
    MIN,
    MAX,
)


def run(N):
    print(N)
    for _ in range(N):
        week = [randint(0, 1000) for _ in range(7)]
        print(" ".join(map(str, week)))


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
