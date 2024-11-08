#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "max-temperature-variation".

Parameters:
* N (days)
* A (minimum temp)
* B (maximum temp)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MINN,
    MAXN,
    MINT,
    MAXT,
    MINT,
    MAXT,
)


def run(N, A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    n = randint(max(1, N // 2), N)
    a = []
    b = []
    for i in range(n):
        t1 = randint(A, B)
        t2 = randint(A, B)
        a.append(min(t1, t2))
        b.append(max(t1, t2))

    print(n)
    print(*a)
    print(*b)


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
