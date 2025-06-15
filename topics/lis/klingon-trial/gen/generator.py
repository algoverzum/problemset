#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "klingon-trial".

Parameters:
* N (N value)
* T (maximum of T value)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= T <= %d
""" % (
    MINN,
    MAXN,
    MINT,
    MAXT,
)


def run(N, T, R):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    if R == "inc":
        print(N)
        print(*range(1, N + 1))
    elif R == "dec":
        print(N)
        print(*range(N, 0, -1))
    elif R == "spec":
        N1 = randint(1, N)
        N2 = N - N1
        T1 = sorted([randint(1, T) for i in range(N1)], reverse=True)
        T2 = sorted([randint(1, T) for i in range(N2)], reverse=True)
        T = []
        while len(T) < N:
            if len(T2) == 0 or len(T1) > 0 and randint(1, N) <= N1:
                T.append(T1.pop())
            else:
                T.append(T2.pop())
        print(N)
        print(*T)
    elif R == "rand":
        if N >= 100:
            N -= randint(0, 10)
        T = [randint(1, T) for i in range(N)]
        print(N)
        print(*T)
    elif R == "rand2":
        root = int(N**0.5)
        a = randint(root // 2, root)
        b = randint(root // 2, root)
        if a > b:
            a, b = b, a
        while a * b * 1.1 < N:
            b = int(b * 1.1)
        print(a * b)
        T = []
        for i in range(a):
            T += list(range((i + 1) * b, i * b, -1))
        print(*T)
    else:
        pass


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
