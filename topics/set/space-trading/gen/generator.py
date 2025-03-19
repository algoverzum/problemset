#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "space-trading".

Parameters:
* N (value of N)
* M (value of M)
* A (max value of items)
* B (number of items)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= M <= %d
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
    MIN_A,
    MAX_A,
    MIN_A,
    MAX_A,
)


def run(N, M, A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(N, M)
    assert A >= B
    assert B >= N
    assert B >= M

    unique_numbers = sample(range(1, A + 1), B)
    list1 = sample(unique_numbers, N)
    list2 = sample(unique_numbers, M)
    shuffle(list1)
    shuffle(list2)
    print(*list1)
    print(*list2)


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
