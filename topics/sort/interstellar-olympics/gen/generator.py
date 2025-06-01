#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "interstellar-olympics".

Parameters:
* N (value of n)
* M (maximum value of medal count)
* R (random type ["rand1","rand2"])
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= M <= %d
* R in ["rand1","rand2"]
""" % (
    MIN_N,
    MAX_N,
    MIN_M,
    MAX_M,
)


def run(N, M, R):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    if R == "rand1":
        print(N)
        for _ in range(N):
            print(randint(1, M), randint(1, M), randint(1, M))
    if R == "rand2":
        lista = []
        N -= randint(0, 10)
        while len(lista) < N:
            a, b, c = randint(1, M), randint(1, M), randint(1, M)
            for i in range(randint(1, 6)):
                lista.append((a, b, c))
        shuffle(lista)
        print(N)
        for i in range(N):
            print(*lista[i])


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
