#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
import string
from random import random, randint, choices, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "space-signals".

Parameters:
* A (number of signals)
* B (maximum word length)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MIN,
    MAX,
    MIN2,
    MAX2,
)


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(A)
    for i in range(A):
        length = randint(1, B)
        result = "".join(choices(string.ascii_lowercase, k=length))
        print(result)
        print(randint(1, 1000))


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
