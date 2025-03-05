#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "ship-rental".

Parameters:
* N (number of ships)
* M (number of days)
* K (number of rentals)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= M <= %d
* %d <= K <= %d
""" % (
    MINN,
    MAXN,
    MINM,
    MAXM,
    MINK,
    MAXK,
)


def run(N, M, K):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    n = randint(N // 2, N)
    m = randint(M // 2, M)

    rentals = []
    histogram = [set() for i in range(m + 1)]

    while len(rentals) < K:
        ID, A, B = randint(1, n), randint(1, m), randint(1, m)
        A, B = min(A, B), max(A, B)
        ok = True
        for i in range(A, B + 1):
            if ID in histogram[i]:
                ok = False
                break
        if ok:
            rentals.append((ID, A, B))
            for i in range(A, B + 1):
                histogram[i].add(ID)

    print(n, m, K)
    for line in rentals:
        print(*line)


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
