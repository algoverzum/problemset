#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "no-arrivals".

Parameters:
* A (minimum value)
* B (maximum value)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MIN_N,
    MAX_N,
    MIN_A,
    MAX_A,
    MIN_A,
    MAX_A,
)


def run(N, A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(N)
    index = randint(0, N - 1)
    for i in range(N):
        if index == i:
            print(0)
        else:
            print(randint(A, B))


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
