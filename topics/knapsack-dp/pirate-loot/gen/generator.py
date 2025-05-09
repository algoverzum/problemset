#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "pirate-loot".

Parameters:
* A (value of N -- types of goodes)
* B (value of S)
* C (max value)
* D (max weight / "spec")
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
* %d <= C <= %d
* D == 'spec' or %d <= D <= %d
""" % (
    MINN,
    MAXN,
    MINS,
    MAXS,
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

    if D == "spec":
        print(A, B)
        for i in range(1, A + 1):
            print(i, i)
    else:
        if A > 200:
            A -= randint(0, 10)
        if B > 500:
            B -= randint(0, 10)
        ladak = set()
        while len(ladak) < A:
            X = randint(1, C)
            Y = randint(1, D)
            ladak.add((X, Y))
        ladak = list(ladak)
        shuffle(ladak)
        print(A, B)
        for X, Y in ladak:
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
