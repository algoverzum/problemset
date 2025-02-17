#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "factory".

Parameters:
* A (length of input)
* B (number of even)
* C (max value)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
* %d <= C <= %d
""" % (
    MINN,
    MAXN,
    0,
    MAXN,
    MINX,
    MAXX,
)


def run(A, B, C):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    N = A
    B = min(A, B)
    odd = []
    even = []
    while len(odd) < N - B:
        num = randint(0, C)
        if num % 2 == 1:
            odd.append(num)
    while len(even) < B:
        num = randint(0, C)
        if num % 2 == 0:
            even.append(num)

    print(N)
    res = odd + even
    shuffle(res)
    print(*res)


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
