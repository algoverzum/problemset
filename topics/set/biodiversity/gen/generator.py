#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed, randrange
from inspect import signature

usage = """Generator for "biodiversity".

Parameters:
* A (N)
* B (M)
* C (different ids)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
* %d <= C <= %d
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
    MIN,
    MAX2,
)


def run(A, B, C):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(A, B)
    if C < 10**7:
        unique_numbers = set()
        while len(unique_numbers) < C:
            unique_numbers.add(randrange(1, MAX2 + 1))
        unique_numbers = list(unique_numbers)
        list1 = sample(unique_numbers, min(A, C))
        list2 = sample(unique_numbers, min(B, C))
        while len(list1) < A:
            list1.append(choice(unique_numbers))
        while len(list2) < B:
            list2.append(choice(unique_numbers))
    else:
        list1 = sample(range(1, C), A)
        list2 = sample(range(1, C), B)
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
