#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "dividing-into-two-groups".

Parameters:
* N (value of N)
* A (minimum value)
* B (maximum value)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MINN,
    MAXN,
    MINA,
    MAXA,
    MINA,
    MAXA,
)


def run(N, A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    res = []
    if A > B:
        A, B = B, A
    for i in range(N):
        x = randint(A, B)
        res.append(x)
    print(N)
    print(*res)


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
