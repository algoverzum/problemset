#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "longest-substring".

Parameters:
* A (string length)
* B (string length)
* C ("rand" or substring min length)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
)


def run(A, B, C):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    if A >= 100:
        A -= randint(1, 20)
    if B >= 100:
        B -= randint(1, 20)

    if C == "rand":
        S1 = ""
        for i in range(A):
            S1 += chr(randint(ord("a"), ord("z")))
        print(S1)
        S2 = ""
        for i in range(B):
            S2 += chr(randint(ord("a"), ord("z")))
        print(S2)
    elif C == "spec":
        X = randint(min(A, B) // 2, min(A, B) * 9 // 10)
        a = chr(randint(ord("a"), ord("z")))
        b = chr(randint(ord("a"), ord("z")))
        c = chr(randint(ord("a"), ord("z")))
        while a == b or a == c or b == c:
            b = chr(randint(ord("a"), ord("z")))
            c = chr(randint(ord("a"), ord("z")))
        print((A - X) * b + X * a)
        print((B - X) * c + X * a)
    elif C == "spec2":
        a = chr(randint(ord("a"), ord("z")))
        print(A * a)
        print(B * a)
    else:
        if max(A, B) < C:
            C = max(A, B)
        SC = ""
        for i in range(C):
            SC += chr(randint(ord("a"), ord("z")))
        Afront = ""
        Aback = ""
        for i in range(A - C):
            if randint(0, 1):
                Afront += chr(randint(ord("a"), ord("z")))
            else:
                Aback += chr(randint(ord("a"), ord("z")))
        Bfront = ""
        Bback = ""
        for i in range(B - C):
            if randint(0, 1):
                Bfront += chr(randint(ord("a"), ord("z")))
            else:
                Bback += chr(randint(ord("a"), ord("z")))
        print(Afront + SC + Aback)
        print(Bfront + SC + Bback)


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
