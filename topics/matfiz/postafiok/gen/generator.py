#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "postafiok".

Parameters:
* N (length)
* S (seed)

Constraint:
* %d <= N <= %d
""" % (
    MIN,
    MAX,
)

abc = [chr(ord("a") + i) for i in range(26)]


def run(N):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    N = max(3, N)
    a = randint(1, N - 2)
    A = [choice(abc) for i in range(N)]
    A[a] = "@"
    print(*A, sep="")


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
