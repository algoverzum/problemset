#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature
from words import *

usage = """Generator for "count-words".

Parameters:
* N (number of words)
* R (result)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= R <= %d
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
)


def run(N, R):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    if N >= 1000:
        N -= randint(0, 100)
    W = set()
    for i in range(R):  # not enough words for large R
        word = choice(words)
        if len(word) <= MAXLENGTH:
            W.add(word)
    while len(W) < R:
        cur = ""
        for i in range(10):
            cur += chr(ord("a") + randint(0, 25))
        W.add(cur)
    WW = list(W)
    W = list(W)
    while len(WW) < N:
        word = choice(W)
        if len(word) <= MAXLENGTH:
            WW.append(word)
    shuffle(WW)
    print(N)
    print(*WW)


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
