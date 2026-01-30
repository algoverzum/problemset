#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "x-tulsuly".

Parameters:
* A (length)
* S (seed)

Constraint:
* %d <= A <= %d
""" % (
    MIN,
    MAX,
)
abc = [chr(ord("a") + i) for i in range(26)]


def run(A):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    N = randint(A // 2, A)
    if N < 1:
        N = 1
    S = [choice(abc) for i in range(N)]
    x = randint(1, 3)
    if "x" not in S:
        S[randint(0, N - 1)] = "x"
    if x == 3:
        while S.count("x") < N // 2:
            S[randint(0, N - 1)] = "x"
        for i in range(N // 10):
            S[randint(0, N - 1)] = "x"

    print(*S, sep="")


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
