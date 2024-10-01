#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "flight-maximums".

Parameters:
* N
* Q
* A (minimum value)
* B (maximum value)
* S (seed)

Constraint:
* 1 <= N <= %d
* 1 <= Q <= %d
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MAXN,
    MAXQ,
    MIN,
    MAX,
    MIN,
    MAX,
)


def run(N, Q, A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]
    print(N, Q)
    H = [randint(A, B) for _ in range(N)]
    print(*H)
    for _ in range(Q):
        S = randint(1, N)
        K = 18
        while S + 2 ** K - 1 > N:
            K = randint(0, 17)
        print(S, K)


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
