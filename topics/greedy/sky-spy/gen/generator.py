#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "sky-spy".

Parameters:
* A (number of intervals)
* B (max values of interval edpoints)
* C (max interval length)
* D (type: random / maxOFresult)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
* %d <= C <= %d
""" % (
    MINN,
    MAXN,
    MIN,
    MAX,
    MIN,
    MAX,
)


def run(A, B, C, D):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    if 1000 <= A:
        A -= randint(0, 100)
    if D == "rand":
        print(A)
        for i in range(A):
            X = randint(1, B)
            Y = randint(max(1, X - C), min(B, X + C))
            while X == Y:
                X = randint(1, B)
                Y = randint(max(1, X - C), min(B, X + C))
            print(min(X, Y), max(X, Y))
    else:
        assert D < A
        DD = set()
        while len(DD) < D:
            DD.add(randint(1, B))
        DDD = sorted(DD)
        intervals = []
        for i in range(D):
            center = DDD[i]
            X = randint(max(1, center - C), center)
            Y = randint(center, min(B, center + C))
            while X == Y:
                X = randint(max(1, center - C), center)
                Y = randint(center, min(B, center + C))
            intervals.append((min(X, Y), max(X, Y)))
        while len(intervals) < A:
            center = choice(DDD)
            X = randint(max(1, center - C), center)
            Y = randint(center, min(B, center + C))
            while X == Y:
                X = randint(max(1, center - C), center)
                Y = randint(center, min(B, center + C))
            intervals.append((min(X, Y), max(X, Y)))
        print(A)
        shuffle(intervals)
        for X, Y in intervals:
            print(X, Y)


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
