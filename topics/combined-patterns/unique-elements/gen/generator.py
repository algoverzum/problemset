#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "unique-elements".

Parameters:
* N (value of N)
* A (minimum range of codes)
* B (maximum range of codes)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MIN_N,
    MAX_N,
    MIN_A,
    MAX_A,
    MIN_A,
    MAX_A,
)


def run(N, A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(N)
    unique = randint(A, B)
    codes = [unique]

    for i in range(N - 1):
        temp = randint(A, B)
        if temp != unique:
            codes.append(temp)
        elif temp == B:
            codes.append(temp - 1)
        else:
            codes.append(temp + 1)
    shuffle(codes)
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
