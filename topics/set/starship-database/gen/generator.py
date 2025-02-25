#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "starship-database".

Parameters:
* Q (number of queries)
* X (max x)
* S (seed)

Constraint:
* %d <= Q <= %d
* %d <= X <= %d
""" % (
    MINQ,
    MAXQ,
    MINX,
    MAXX,
)


def run(Q, X):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(Q)
    cur = set()
    for i in range(Q):
        y = randint(1, 3)
        if y == 1:
            if cur and randint(1, 10) > 9:
                x = choice(list(cur))
            else:
                x = randint(1, X)
        if y == 2:
            if cur and randint(1, 10) > 6:
                x = choice(list(cur))
            else:
                x = randint(1, X)
        if y == 3:
            if cur and randint(1, 10) > 1:
                x = choice(list(cur))
            else:
                x = randint(1, X)
        print(y, x)


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
