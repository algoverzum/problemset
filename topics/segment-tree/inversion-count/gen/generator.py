#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "inversion-count".

Parameters:
* N (maximum value)
* sumN (maximum sum or -1, -2)
* A (maximum value)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= sumN <= %d
* %d <= A <= %d
""" % (
    MIN,
    MAXN,
    -2,
    MAXN,
    MIN,
    MAXA,
)


def run(N, sumN, A):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    if sumN == -1:
        cur = set()
        while len(cur) < N:
            cur.add(randint(1, A))
        cur = sorted(cur)
        print(1)
        print()
        print(len(cur))
        for a in cur:
            print(a)
    elif sumN == -2:
        cur = set()
        while len(cur) < N:
            cur.add(randint(1, A))
        cur = sorted(cur, reverse=True)
        print(1)
        print()
        print(len(cur))
        for a in cur:
            print(a)
    else:
        tests = []
        while len(tests) < 100 and sumN >= N:
            cur = set()
            curN = randint(N // 2, N)
            sumN -= curN
            while len(cur) < curN:
                cur.add(randint(1, A))
            cur = list(cur)
            shuffle(cur)
            tests.append(cur)
        print(len(tests))
        for test in tests:
            print()
            print(len(test))
            for a in test:
                print(a)


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
