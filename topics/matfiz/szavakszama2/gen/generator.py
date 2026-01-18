#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "szavakszama2".

Parameters:
* N (number of words)
* S (seed)

Constraint:
* %d <= N <= %d
""" % (
    1,
    10,
)

abc = [chr(ord("a") + i) for i in range(26)]


def run(N):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    szavak = []
    for i in range(N):
        l = randint(1, 10)
        szo = "".join([choice(abc) for j in range(l)])
        szavak.append(szo)

    l = randint(0, 2)
    print(" " * l, end="")
    for szo in szavak:
        l = randint(1, 4)
        print(szo + " " * l, end="")
    print()


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
