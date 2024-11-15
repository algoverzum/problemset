#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "same-3-letters".

Parameters:
* A (number of different letters in a 3 letter string)
* S (seed)

Constraint:
* %d <= A <= %d
""" % (
    1,
    3,
)


def run(A):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    letters = list(map(chr, range(ord("a"), ord("z") + 1)))
    char1 = choice(letters)
    char2 = choice(letters)
    char3 = choice(letters)
    while len(set([char1, char2, char3])) != A:
        char1 = choice(letters)
        char2 = choice(letters)
        char3 = choice(letters)
    print(char1 + char2 + char3)


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
