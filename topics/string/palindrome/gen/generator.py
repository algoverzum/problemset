#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "palindrom".

Parameters:
* N (the length of the word)
* S (seed)

Constraint:
* %d <= N <= %d
""" % (
    MIN,
    MAX,
)


def run(N):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    word = ""
    if randint(1, 10) > 3:
        for _ in range(N - 1):
            word += chr(randint(ord("a"), ord("z")))
    else:
        for _ in range(int((N - 1) / 2)):
            word += chr(randint(ord("a"), ord("z")))
        revword = word[::-1]
        if N - 1 % 2 == 0:
            word += revword
        else:
            word += revword[1::]
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
