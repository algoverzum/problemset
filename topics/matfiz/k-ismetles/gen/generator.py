#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "k-ismetles".

Parameters:
* A (minimum K value)
* B (maximum K value)
* N (length of S)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
* -2 <= N <= %d
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
    MAX,
)

abc = "abcdefghijklmnopqrstuvwxyz"


def run(A, B, N):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    K = randint(A, B)
    K = randint(A, K)
    if N == -1:
        s = [abc[randint(0, 25)] for i in range(90)]
        print(K)
        print("".join(s))
    elif N == -2:
        X = 1000 // K
        s = [abc[randint(0, 25)] for i in range(X)]
        S = s * K
        print(K)
        shuffle(S)
        S[-1] = "z"
        print("".join(S))
    else:
        X = N // K
        s = [abc[randint(0, 25)] for i in range(X)]
        S = s * K
        print(K)
        shuffle(S)
        print("".join(S))


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
