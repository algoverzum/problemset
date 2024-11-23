#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "most-children".

Parameters:
* A (people)
* B (edges)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MINN,
    MAXN,
    MINK,
    MAXK,
)


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    emberek = list(range(1, A + 1))
    shuffle(emberek)
    edges = []
    for i in range(A - 1):
        deg = choice([0, 0, 1, 1, 1, 1, 2, 2, 2, 2])  # rand number of parents
        if i == A - 2:
            deg = min(1, deg)
        szulok = set()
        while len(szulok) < deg:
            j = randint(i + 1, A - 1)
            szulok.add(j)
            # print(A,i,j,szulok,deg,edges)
        for sz in szulok:
            edges.append((emberek[sz], emberek[i]))
        if len(edges) >= B:
            break
    print(A, len(edges))
    # edges.sort()
    shuffle(edges)
    for x, y in edges:
        print(x, y)


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
