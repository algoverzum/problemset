#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "most-frequent".

Parameters:
* A (number of numbers (N))
* B (maximum value)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
""" % (
    1,
    MAXN,
    0,
    MAXA,
)


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    x = randint(0, 1)
    if x == 0 or A <= 10:  # random
        X = []
        for i in range(A):
            X.append(randint(0, B))
    else:  # at lest two of the same kind
        X = []
        for i in range(A):
            X.append(randint(0, B))
        d = {}
        for v in X:
            d[v] = d.get(v, 0) + 1
        Y = list(d.values())
        maxi = max(Y)
        while Y.count(maxi) == 1:
            X = []
            for i in range(A):
                X.append(randint(0, B))
            d = {}
            for v in X:
                d[v] = d.get(v, 0) + 1
            Y = list(d.values())
            maxi = max(Y)

    print(A)
    print(*X)


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
