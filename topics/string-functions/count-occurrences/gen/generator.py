#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "count-occurrences".

Parameters:
* L (word length)
* N (number of "ebo"s)
* S (seed)

Constraint:
* %d <= L <= %d
""" % (
    MIN,
    MAX,
)


def run(L, N):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    word = ""
    if N == 0:
        for _ in range(L):
            word += chr(randint(ord("a"), ord("z")))
    else:
        li = []
        for _ in range(N):
            li.append("ebo")
        for _ in range(L - (3 * N)):
            li.append(chr(randint(ord("a"), ord("z"))))
        shuffle(li)
        word = "".join(li)
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
