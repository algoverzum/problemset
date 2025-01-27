#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "heroes".

Parameters:
* A (number of heroes)
* B (max date) 
* C (result minimum value)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MIN,
    MAXN,
    MIN,
    MAXAL,
)


def run(A, B, C):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    res = []
    if C == "rand":
        for i in range(A):
            a = randint(1, B)
            b = randint(1, B)
            while a == b:
                a = randint(1, B)
                b = randint(1, B)
            if a > b:
                a, b = b, a
            res.append((a, b))
    else:
        mid = randint(B // 4, 3 * B // 4)
        for i in range(C):
            a = randint(1, mid)
            b = randint(mid, B)
            while a == b:
                a = randint(1, mid)
                b = randint(mid, B)
            res.append((a, b))
        while len(res) < A:
            a = randint(1, B)
            b = randint(1, B)
            while a == b:
                a = randint(1, B)
                b = randint(1, B)
            if a > b:
                a, b = b, a
            res.append((a, b))

    print(A)
    shuffle(res)
    for a, b in res:
        print(a, b)


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
