#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "intergalactic-contest".

Parameters:
* N
* P (probability of not changing the first number)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= P <= %d
""" % (
    MIN,
    MAX,
    0,
    1,
)


def run(N, P):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(N)
    s = set()
    last = (randint(MIN_V, MAX_V), randint(MIN_V, MAX_V))
    s.add(last)
    while len(s) < N:
        if random() < P:
            first = last[0]
        else:
            first = randint(MIN_V, MAX_V)
        second = randint(MIN_V, MAX_V)
        last = (first, second)
        s.add(last)
    l = list(s)
    shuffle(l)
    for a, b in l:
        print(a, b)


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
