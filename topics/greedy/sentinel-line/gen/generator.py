#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "sentinel-line".

Parameters:
* N (no of stations)
* H (generator radius)
* X (max distange)
* T (generator type)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= H <= %d
* %d <= X <= %d
""" % (
    MINN,
    MAXN,
    MINH,
    MAXH,
    MINA,
    MAXA,
)


def run(N, H, X, T):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    if T == "rand":
        if N > 1000:
            N -= randint(0, 100)
        if H > 500:
            H -= randint(0, 10)
        print(N, H)
        stations = set()
        while len(stations) < N:
            stations.add(randint(0, X))
        print(*sorted(stations))
    if T == "uniform":
        if N > 1000:
            N -= randint(0, 100)
        if H > 500:
            H -= randint(0, 10)
        print(N, H)
        stations = set()
        x = H // randint(3, 5)
        y = x
        while len(stations) < N and y < X:
            stations.add(y)
            y += x
        while len(stations) < N:
            stations.add(randint(0, X))
        print(*sorted(stations))
    if T == "cluster":
        if N > 1000:
            N -= randint(0, 100)
        if H > 500:
            H -= randint(0, 10)
        print(N, H)
        stations = set()
        while len(stations) < N:
            center = randint(0, X)
            size = randint(3, 20)
            for i in range(size):
                stations.add(min(X, max(0, center + randint(-3 * H, 3 * H))))
                if len(stations) == N:
                    break
        print(*sorted(stations))


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
