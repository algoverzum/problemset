#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "class-circle".

Parameters:
* R (maximum radius)
* S (seed)

Constraint:
* %d <= R <= %d
""" % (
    MIN,
    MAX,
)


def run(R):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    rand = randint(1, 3)
    r1 = randint(1, R)
    r2 = randint(1, R)
    if rand == 1:
        r2 = r1
    print(r1)
    print(r2)


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
