#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "counting-vowels".

Parameters:
* A (type: rand, none, only)
* B (length)
* S (seed)

Constraint:
* A in ['rand', 'none', 'only']
* %d <= B <= %d
""" % (
    MINS,
    MAXS,
)


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    abc = [chr(ord("a") + i) for i in range(26)]
    aaa = "aoiue"
    if A == "rand":
        S = ""
        for i in range(B):
            S += abc[randint(0, 25)]
        print(S)
        if B >= 100:
            B -= randint(0, 20)
        print(B)
        for _ in range(B):
            i = randint(1, len(S))
            j = randint(1, len(S))
            while i == j:
                j = randint(1, len(S))
            print(min(i, j), max(i, j))
    elif A == "only":
        S = ""
        for i in range(B):
            S += aaa[randint(0, 4)]
        print(S)
        if B >= 100:
            B -= randint(0, 20)
        print(B)
        for _ in range(B):
            i = randint(1, len(S))
            j = randint(1, len(S))
            while i == j:
                j = randint(1, len(S))
            print(min(i, j), max(i, j))
    if A == "none":
        S = ""
        for i in range(B):
            betu = abc[randint(0, 25)]
            while betu in aaa:
                betu = abc[randint(0, 25)]
            S += betu
        print(S)
        if B >= 100:
            B -= randint(0, 20)
        print(B)
        for _ in range(B):
            i = randint(1, len(S))
            j = randint(1, len(S))
            while i == j:
                j = randint(1, len(S))
            print(min(i, j), max(i, j))


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
