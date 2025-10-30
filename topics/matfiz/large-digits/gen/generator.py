#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "large-digits".

Parameters:
* A (minimum value)
* B (maximum value)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
)


def digsum(s):
    res = 0
    while s:
        res += s % 10
        s //= 10
    return res


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    X = randint(A, B)
    Y = randint(A, B)
    R = randint(1, 4)
    if R == 1:
        while digsum(X) != digsum(Y):
            X = randint(A, B)
            Y = randint(A, B)
    print(X)
    print(Y)


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
