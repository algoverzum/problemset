#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "route-optimizer".

Parameters:
* N (max number of verices)
* M (max number of edges)
* W (max weight)
* X (type: random/looplessrandom/...)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= M <= %d
* %d <= W <= %d
* X in ["rand", "loopless", "rand2", "rand3", "break_dijkstra"]
""" % (
    MINN,
    MAXN,
    MINM,
    MAXM,
    MINW,
    MAXW,
)


def run(N, M, W, X):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    if X == "rand":
        edges = {}
        for i in range(randint(3, max(3, min(N - 1, M // 10)))):
            V = randint(2, N)
            weight = randint(-W // 2, W)
            while weight == 0:
                weight = randint(-W, W)
            edges[(1, V)] = weight
        for j in range(3):
            for i in range(M - len(edges)):
                U = randint(1, N)
                V = randint(1, N)
                while U == V:
                    V = randint(1, N)
                if (U, V) not in edges:
                    edges[(U, V)] = randint(1, W)
        print(N, len(edges))
        for (U, V) in edges:
            print(U, V, edges[(U, V)])
    if X == "loopless":
        edges = {}
        X = list(range(2, N + 1))
        shuffle(X)
        X = [1] + X
        for i in range(randint(3, max(3, min(N - 1, M // 10)))):
            V = randint(1, N - 1)
            weight = randint(-W, W)
            while weight == 0:
                weight = randint(-W, W)
            edges[(1, X[V])] = weight
        for j in range(3):
            for i in range(M - len(edges)):
                U = randint(0, N - 1)
                V = randint(0, N - 1)
                while U == V:
                    V = randint(0, N - 1)
                U, V = min(U, V), max(U, V)
                if (X[U], X[V]) not in edges:
                    weight = randint(-W, W)
                    while weight == 0:
                        weight = randint(-W, W)
                    edges[(X[U], X[V])] = weight
        print(N, len(edges))
        for (U, V) in edges:
            print(U, V, edges[(U, V)])
    if X == "rand3":
        edges = {}
        X = list(range(2, N + 1))
        shuffle(X)
        X = [1] + X
        for i in range(len(X) - 1):
            edges[(X[i], X[i + 1])] = -1
        for j in range(3):
            for i in range(M - len(edges)):
                U = randint(1, N)
                V = randint(1, N)
                while U == V:
                    V = randint(1, N)
                if (U, V) not in edges:
                    weight = randint(20, W)
                    edges[(U, V)] = weight
        print(N, len(edges))
        for (U, V) in edges:
            print(U, V, edges[(U, V)])
    if X == "rand2":
        edges = {}
        last = 1
        seen = {1}
        for i in range(max(3, min(N // 2, M // 3))):
            V = randint(2, N)
            while V in seen:
                V = randint(2, N)
            edges[(last, V)] = choice([-1, 1])
            last = V
            seen.add(V)
        for j in range(3):
            for i in range(M - len(edges)):
                U = randint(1, N)
                V = randint(1, N)
                while U == V:
                    V = randint(1, N)
                if (U, V) not in edges:
                    edges[(U, V)] = randint(5, W)
        print(N, len(edges))
        tmp = []
        for (U, V) in edges:
            tmp.append((U, V))
        shuffle(tmp)
        for (U, V) in tmp:
            print(U, V, edges[(U, V)])


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
