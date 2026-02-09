#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "varazslo".

Parameters:
* N (length)
* F (fails)
* S (seed)

Constraint:
* %d <= A <= %d
""" % (
    MIN,
    MAX,
)


def run(N, F):
    min_score = 0
    max_score = 49 if F == 0 else 100

    print(N)

    names = set()
    while len(names) < N:
        name_length = randint(3, 10)
        name = "".join(choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") for _ in range(name_length))
        if name in names:
            continue

        names.add(name)
        score = randint(min_score, max_score)
        print(f"{name} {score}")


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
