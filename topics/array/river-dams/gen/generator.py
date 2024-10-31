#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "river-dams".

Parameters:
* A (minimum value for n)
* B (maximum value for n)
* C (minimum value for a_i)
* D (maximum value for a_i)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
* %d <= C <= %d
* %d <= D <= %d
""" % (
    MIN_N,
    MAX_N,
    MIN_N,
    MAX_N,
    MIN_A,
    MAX_A,
    MIN_A,
    MAX_A,
)


def run(A, B, C, D):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]
    n = randint(A, B)
    print(n)

    print(*[randint(C, D) for i in range(n)])


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
