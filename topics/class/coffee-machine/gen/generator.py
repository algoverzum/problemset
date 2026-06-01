#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "coffee-machine".

Parameters:
* T (number of operators)
* S (seed)

Constraint:
* %d <= T <= %d
""" % (
    MIN,
    MAX,
)


def run(T):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print("BRAND" + str(randint(1, 100)))
    for i in range(T - 1):
        cur = randint(2, 6)
        print(cur)
        if cur == 2:
            print(randint(0, 1))
        if cur == 3:
            print(randint(5, 20))
        if cur == 4:
            print(randint(5, 10))
    print(6)
    print(0)


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
