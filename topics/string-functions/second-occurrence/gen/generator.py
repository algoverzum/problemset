#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "second-occurrence".

Parameters:
* L (length of the string)
* N (position of second f)
* S (seed)

Constraint:
* %d <= L <= %d
""" % (
    MIN,
    MAX,
)


def randnotf():
    c = chr(randint(ord("a"), ord("z")))
    while c == "f":
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
            word += randnotf()
    elif N == -1:
        num = randint(0, L - 2)
        for _ in range(num):
            word += randnotf()
        word += "f"
        for _ in range(L - 1 - num):
            word += randnotf()
    else:
        num = randint(0, N - 3)
        for _ in range(num):
            word += randnotf()
        word += "f"
        for _ in range(N - 2 - num):
            word += randnotf()
        word += "f"
        while len(word) < L:
            word += randnotf()
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
