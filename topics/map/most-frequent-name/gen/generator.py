#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "most-frequent-name".

Parameters:
* N (length of the list (number of ships))
* M (max number of different ships in list)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= M <= %d
""" % (
    MIN,
    MAX,
    1,
    MAX,
)

abc = list(map(chr, range(97, 123)))


def run(N, M):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    if N > 1000:
        N -= randint(1, 100)
    ships = set()
    while len(ships) < M:
        l = randint(1, MAXA)
        l = randint(1, l)  # shorten expected length to MAXA/4
        ship = ""
        while len(ship) < l:
            ship += choice(abc)
        ships.add(ship)
    ships = list(ships)
    A = []
    for i in range(N):
        A.append(choice(ships))
    print(N)
    for a in A:
        print(a)


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
