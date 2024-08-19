#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
import math
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "fruit-sharing".

Parameters:
* type (spec1/spec2/spec3/rand)
* A (maximum value)
* S (seed)

Constraint:
* %d <= A <= %d
""" % (
    MIN,
    MAX,
)


def run(type, A):
    assert type in ["spec1", "spec2", "spec3", "rand"]
    C = N = 0
    match type:
        case "spec1":
            C = randint(2, A)
            N = 1
        case "spec2":
            C = 1
            N = randint(2, A)
        case "spec3":
            N = randint(2, math.floor(math.sqrt(A)))
            k = randint(2, math.floor(math.sqrt(A)))
            C = N * k
        case "rand":
            C = randint(1, A)
            N = randint(1, A)
    print(C)
    print(N)


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
