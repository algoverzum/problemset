#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "intersection".

Parameters:
* A (length of input)
* B (max value)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MINN,
    MAXN,
    MINX,
    MAXX,
)


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    N = randint(max(1, A // 2), A)
    M = randint(max(1, A // 2), A)
    AA = []
    BB = []
    while len(AA) < N:
        num = randint(0, B)
        if num not in AA:
            AA.append(num)
    AA.sort()
    while len(BB) < M:
        num = randint(0, B)
        if num not in BB:
            BB.append(num)
    BB.sort()

    print(N, M)
    print(*AA)
    print(*BB)


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
