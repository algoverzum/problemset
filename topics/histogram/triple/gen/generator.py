#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "triple".

Parameters:
* A (minimum value)
* B (maximum value)
* T (type)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
* T in ['rand','dist','onetwo','onlythree']
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
)


def run(A, B, T):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    if T == "rand":
        N = randint(A, B)
        A = [randint(1, N) for i in range(N)]
        print(N)
        print(*A)
    if T == "dist":
        N = randint(A, B)
        A = list(range(1, N + 1))
        shuffle(A)
        print(N)
        print(*A)
    if T == "onetwo":
        N = randint(A, B)
        hist = [0] * (N + 1)
        A = []
        while len(A) < N:
            x = randint(1, N)
            if hist[x] < 2:
                A.append(x)
                hist[x] += 1
        print(N)
        print(*A)
    if T == "onlythree":
        N = randint(A, B)
        hist = [0] * (N + 1)
        A = []
        while len(A) < N:
            x = randint(1, N)
            if hist[x] < 2:
                A.append(x)
                hist[x] += 1
        num = N - hist[::-1].index(max(hist))
        for i in range(N - 1, -1, -1):
            if A[i] != num:
                A[i] = num
                break
        print(N)
        print(*A)


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
