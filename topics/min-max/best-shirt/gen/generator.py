#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "global-warming".

Parameters:
* A (minimum value)
* B (maximum value)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
* %d <= C <= %d
* %d <= D <= %d
""" % (
    N_MIN,
    N_MAX,
    N_MIN,
    N_MAX,
    MONEY_MIN,
    MONEY_MAX,
    MONEY_MIN,
    MONEY_MAX,
)


def run(A, B, C, D):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    n = randint(A, B)
    print(str(n) + " " + str(randint(C, D)))
    second_line = ""
    for _ in range(n):
        second_line += str(randint(C, D)) + " "
    print(second_line)


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
