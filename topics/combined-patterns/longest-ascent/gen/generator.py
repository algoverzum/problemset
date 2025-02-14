#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "longest-ascent".

Parameters:
* A (number of heights)
* B (maximum height)
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


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]
    print(A)
    last = 1
    for i in range(A):
        if A >= 100:
            if last < 0.95 * B:
                chance = randint(1, 10)
                if chance < 9:
                    last = randint(last, int(0.05 * B) + last)
                else:
                    last = randint(1, B)
            else:
                last = randint(1, B)
        else:
            last = randint(1, B)
        print(last)


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
