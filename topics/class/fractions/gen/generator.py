#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from math import gcd
from inspect import signature

usage = """Generator for "fractions".

Parameters:
* A (maximum value)
* S (seed)

Constraint:
* A <= %d
""" % (
    MAX,
)


def gen4(A):
    a = randint(-A, A)
    b = randint(-A, A)
    c = randint(-A, A)
    d = randint(-A, A)
    while b == 0:
        b = randint(-A, A)
    while c == 0:
        c = randint(-A, A)
    while d == 0:
        d = randint(-A, A)
    return a, b, c, d


def run(A):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    a, b, c, d = gen4(A)
    if gcd(a, b) == 1:
        a, b, c, d = gen4(A)
    print(a, b, c, d)


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
