#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "same-two-times".

Parameters:
* N (number of codes)
* M (index of the pair)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= M <= %d
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
)


def run(N, M):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(N)
    codes = []
    if M == 100:
        for _ in range(N):
            randnum = randint(1, 1000)
            while randnum in codes:
                randnum = randint(1, 1000)
            codes.append(randnum)
    else:
        for _ in range(M - 1):
            randnum = randint(1, 1000)
            while randnum in codes:
                randnum = randint(1, 1000)
            codes.append(randint(1, 1000))
        randnum = randint(1, 1000)
        while randnum in codes:
            randnum = randint(1, 1000)
        codes.append(randnum)
        codes.append(randnum)
        for _ in range(N - M - 1):
            randnum = randint(1, 1000)
            while randnum in codes:
                randnum = randint(1, 1000)
            codes.append(randint(1, 1000))
    print(*codes)


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
