#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "balanced-loading".

Parameters:
* A (N maximum value)
* B (W maximum value, or "rand" or "spec")
* S (seed)

Constraint:
* %d <= A <= %d
* B == "rand" or B == "spec" or %d <= B <= %d
""" % (
    MINN,
    MAXN,
    MINW,
    MAXW,
)


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    if A > 50:
        A -= randint(0, 5)
    if B == "rand":
        X = []
        while len(X) < A:
            X.append(randint(1, 100))
        print(A)
        print(*X)
    elif B == "spec":
        print(99)
        X = [50] * 2 + [20] * 97
        print(*X)
    else:
        X = []
        while len(X) < A:
            X.append(B * randint(1, 100 // B))
        if B == 1:
            if sum(X) % 2 == 1:
                X[-1] -= 1
                if X[-1] < 1:
                    X[-1] += 2
        else:
            X[-1] -= 1
            if X[-1] < 1:
                X[-1] += B
        print(A)
        print(*X)


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
