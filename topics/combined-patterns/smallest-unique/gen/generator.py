#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "smallest-unique".

Parameters:
* A (N value)
* B (how many different numbers)
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

    print(A)
    remaining = A
    distincts = sample(range(1, A + 1), B)
    lista = []
    for i in range(B):
        c = randint(0, A // B)
        remaining = remaining - c
        lista = lista + [distincts[i]] * c
    lista = lista + [distincts[0]] * remaining
    if A == 1000:
        lista = list(range(1, 1001))
    shuffle(lista)
    print(*lista)


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
