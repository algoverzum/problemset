#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "tea-purchase".

Parameters:
* N (number of purchases)
* T (force tie)
* S (seed)

Constraint:
* %d <= N <= %d
""" % (
    MIN,
    MAX,
)

brands = [
    "Lipton",
    "Teekanne",
    "Twinings",
    "Pickwick",
    "Greenfield",
    "Dilmah",
    "Tetley",
    "EarlGrey",
    "Saga",
    "SirMorton",
    "Loyd",
    "Gardonyi",
]


def run(N):
    print(N)

    for _ in range(N):
        print(choice(brands))
        print(randint(1, 20000))


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
