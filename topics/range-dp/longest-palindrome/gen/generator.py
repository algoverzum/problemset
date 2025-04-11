#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "longest-palindrome".

Parameters:
* A (string length)
* B (rand or palindrome min length)
* S (seed)

Constraint:
* %d <= A <= %d
""" % (
    MIN,
    MAX,
)


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    if A >= 500:
        x = randint(1, 20)
        A -= x
        if B != "rand" and B > x:
            B -= x

    if B == "rand":
        S = ""
        for i in range(A):
            S += chr(randint(ord("a"), ord("z")))
        print(S)
    else:
        assert B <= A
        S = [chr(randint(ord("a"), ord("z"))) for i in range(A)]
        I = sample(range(0, A), B)
        for i in range(B // 2):
            S[I[i]] = S[I[-i - 1]]
        print("".join(S))


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
