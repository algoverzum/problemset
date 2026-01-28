#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "anagrammak".

Parameters:
* A (length)
* B (length)
* T (type)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
* T in ['rand', 'anag', 'almost']
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
)


def run(A, B, T):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    abc = [chr(ord("a") + i) for i in range(26)]

    if T == "rand":
        S1 = [choice(abc) for i in range(A)]
        S2 = [choice(abc) for i in range(B)]
    if T == "anag":
        S1 = [choice(abc) for i in range(A)]
        S2 = S1.copy()
        shuffle(S2)
    if T == "almost":
        S1 = [choice(abc) for i in range(A)]
        S2 = S1.copy()
        shuffle(S2)
        index = randint(0, A - 1)
        new = choice(abc)
        while S2[index] == new:
            new = choice(abc)
        S2[index] = new

    print(*S1, sep="")
    print(*S2, sep="")


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
