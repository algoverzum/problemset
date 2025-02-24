#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "happiness".

Parameters:
* N (length of S)
* M (length of A and B)
* X (max value)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= M <= %d
* %d <= X <= %d
""" % (
    MINN,
    MAXN,
    MINM,
    MAXM,
    MINS,
    MAXS,
)


def run(N, M, X):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    if N >= 1000:
        N -= randint(0, 100)
    if M >= 1000:
        M -= randint(0, 100)
    assert 2 * M <= X
    S = [randint(1, X) for i in range(N)]
    a = randint(0, 100)
    b = randint(0, 100)
    A = set()
    B = set()
    for i in range(int(M * (a + b) / 100)):
        x = choice(S)
        j = randint(1, a + b)
        if x not in A and x not in B:
            if j <= a and len(A) < M:
                A.add(x)
            elif len(B) < M:
                B.add(x)
    while len(A) < M:
        x = randint(1, X)
        if x not in A and x not in B:
            A.add(x)
    while len(B) < M:
        x = randint(1, X)
        if x not in A and x not in B:
            B.add(x)
    assert A.isdisjoint(B)
    A = list(A)
    shuffle(A)
    B = list(B)
    shuffle(B)

    print(N, M)
    print(*S)
    print(*A)
    print(*B)


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
