#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "go-to-jail".

Parameters:
* A (minimum value)
* B (maximum value)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
)


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    N = randint(A, B)
    elso = [randint(1, 6) for i in range(N)]
    masodik = [randint(1, 6) for i in range(N)]

    if N > 5:
        if randint(1, 3) == 2:
            index = randint(2, N - 2)
            for i in range(index - 1, index + 2):
                x = randint(1, 6)
                elso[i] = x
                masodik[i] = x

    print(N)
    for i in range(N):
        print(elso[i], masodik[i])


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
