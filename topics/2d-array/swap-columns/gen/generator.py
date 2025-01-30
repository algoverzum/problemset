#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "scale-a-matrix".

Parameters:
* A (max N,M value)
* B (maximum matrix value)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MINN,
    MAXN,
    MINA,
    MAXA,
)


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    N = randint(2, A)
    M = randint(2, A)
    I = randint(1, M)
    J = randint(1, M)
    while I >= J:
        I = randint(1, M)
        J = randint(1, M)

    print(N, M)
    for i in range(N):
        print(*[randint(0, B) for i in range(M)])
    print(I, J)


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
