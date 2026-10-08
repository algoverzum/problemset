#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "k-legnagyobb-elem".

Parameters:
* A (value of n and max value of k)
* B (maximum value of s_i)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MIN_A,
    MAX_A,
    MIN_B,
    MAX_B,
)


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(A, end=" ")
    print(randint(1, A))
    for _ in range(A):
        print(randint(1, B), end=" ")
    print()


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
