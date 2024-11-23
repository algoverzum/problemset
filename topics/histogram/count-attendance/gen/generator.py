#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "count-attendance".

Parameters:
* A (number of days)
* B (non-zeros in ans (B <= A))
* S (seed)

Constraint:
* %d <= A <= %d
* 1 <= B <= 11
* B <= A
""" % (
    MINN,
    MAXN,
)


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(A)

    AA = list(range(11))
    res = sample(AA, B)
    R = res[:]
    while len(res) < A:
        res.append(choice(R))
    shuffle(res)
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
