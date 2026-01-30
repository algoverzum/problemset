#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "tukorerdo".

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

    x = randint(1, 6)
    if N == 1:
        x = 1
    s = "".join([chr(randint(ord("a"), ord("z"))) for i in range(N)])
    if x in [1, 2]:
        M = randint(N - 1, N + 1)
        if M < 1:
            M = 1
        if M > N:
            M = N
        t = "".join(chr(randint(ord("a"), ord("z"))) for i in range(M))
    if x in [3, 4]:
        t = s[::-1]
    if x in [5, 6]:
        index = randint(0, len(s))
        t = ""
        for i in range(N):
            if i != index:
                t += s[-i - 1]
            else:
                if s[-1 - 1] != "a":
                    t += "a"
                else:
                    t += "b"

    print(s)
    print(t)


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
