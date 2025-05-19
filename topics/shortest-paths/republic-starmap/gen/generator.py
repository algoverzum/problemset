#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "republic-starmap".

Parameters:
* N 
* K
* P (probability of a connection)
* T (type)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= K <= %d
* 0 <= P <= 1
* T in ["norm", "spec"]
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
)


def run(N, K, P, T):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    n = N
    k = K
    if K > 10:
        k -= randint(0, 10)
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                if random() < P:
                    M[i][j] = randint(1, MAX_V)
                else:
                    M[i][j] = -1
    if T == "spec":
        # add unavailable shorter paths
        dist = [[-1] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dist[i][j] = M[i][j]
        for mid in range(k):
            for i in range(n):
                for j in range(n):
                    if dist[i][mid] != -1 and dist[mid][j] != -1:
                        if dist[i][j] == -1 or dist[i][j] > dist[i][mid] + dist[mid][j]:
                            dist[i][j] = dist[i][mid] + dist[mid][j]
        for i in range(k):
            for j in range(k):
                if i != j and random() < 0.5:
                    mid = randint(k, n - 1)
                    d = randint(1, MAX_V) if dist[i][j] == -1 else dist[i][j]
                    d1 = randint(1, d - 2)
                    d2 = max(0, d - d1 - randint(1, 1000))
                    M[i][mid] = d1
                    M[mid][j] = d2
    print(n, k)
    for row in M:
        print(*row)


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
