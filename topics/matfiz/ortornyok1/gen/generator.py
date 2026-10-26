#!/usr/bin/env python3

from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "metro-tickets".

Parameters:
* T (number of test cases)
* N (number of coins in the left pocket)
* M (number of coins in the right pocket)
* S (seed)
"""


def run(T, N, M):
    print(T)
    for _ in range(T):
        K = randint(1, 2000)
        left_pocket = [randint(1, 1000) for _ in range(N)]
        right_pocket = [randint(1, 1000) for _ in range(M)]
        print(f"{N} {M} {K}")
        print(" ".join(map(str, left_pocket)))
        print(" ".join(map(str, right_pocket)))


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
