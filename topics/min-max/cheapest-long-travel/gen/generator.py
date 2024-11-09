#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "cheapest-long-travel".

Parameters:
* N (number of trips)
* K (minimum distance threshold)
* A (maximum light years)
* B (maximum taller)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= K <= %d
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
    MIN,
    MAX,
    MIN,
    MAX,
)


def run(N, K, A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    n = randint(max(1, N // 2), N)
    k = randint(max(1, K // 2), K)

    a = [randint(1, A) for i in range(n)]
    b = [randint(1, B) for i in range(n)]

    print(n, k)
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
