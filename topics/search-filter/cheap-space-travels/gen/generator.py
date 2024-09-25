#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "cheap-space-travels".

Parameters:
* N (count of items)
* A (minimum distance)
* B (maximum distance)
* C (minimum price)
* D (maximum price)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= A <= %d
* %d <= B <= %d
* %d <= C <= %d
* %d <= D <= %d
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
    MIN,
    MAX,
    MIN,
    MAXP,
    MIN,
    MAXP,
)


def run(N, A, B, C, D):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(N)
    for i in range(N):
        print(randint(A, B), randint(C, D))


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
