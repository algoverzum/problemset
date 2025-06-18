#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, seed
from inspect import signature

usage = """Generator for "central-shortcut".

Parameters:
* N 
* P (probability of a connection)
* S (seed)

Constraint:
* %d <= N <= %d
* 0 <= P <= 1
""" % (
    MIN,
    MAX,
)


def run(N, P):
    n = N
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                if random() < P:
                    M[i][j] = randint(1, MAX_V)
                else:
                    M[i][j] = -1
    print(n)
    for row in M:
        print(*row)


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
