#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "second-occurrence".

Parameters:
* L (length of the string)
* N (position of second x)
* S (seed)

Constraint:
* %d <= L <= %d
* 1 <= L < %d
""" % (
    MIN,
    MAX,
    MAX,
)


def randnotx():
    c = chr(randint(ord("a"), ord("z")))
    while c == "x":
        c = chr(randint(ord("a"), ord("z")))
    return c


def run(L, N):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    word = ""
    if N == -2:
        for _ in range(L):
            word += randnotx()
    elif N == -1:
        num = randint(0, L - 2)
        for _ in range(num):
            word += randnotx()
        word += "x"
        for _ in range(L - 1 - num):
            word += randnotx()
    else:
        num = randint(0, N - 3)
        for _ in range(num):
            word += randnotx()
        word += "x"
        for _ in range(N - 2 - num):
            word += randnotx()
        word += "x"
        while len(word) < L:
            word += randnotx()
    print(word)


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
