#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "spice-trails".

Parameters:
* N (max number of verices)
* M (max number of edges)
* W (max weight)
* X (type: random/looplessrandom/?)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= M <= %d
* %d <= W <= %d
* X in ["rand", "loopless", "rand2", "rand3"]
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
            V = randint(1, N - 1)
            edges[(0, V)] = randint(1, W)
        for j in range(3):
            for i in range(M - len(edges)):
                U = randint(0, N - 1)
                V = randint(0, N - 1)
                while U == V:
                    V = randint(0, N - 1)
                if (U, V) not in edges:
                    edges[(U, V)] = randint(1, W)
        print(N, len(edges))
        for (U, V) in edges:
            print(U, V, edges[(U, V)])
    if X == "loopless":
        edges = {}
        X = list(range(1, N))
        shuffle(X)
        X = [0] + X
        for i in range(randint(3, max(3, min(N - 1, M // 10)))):
            V = randint(1, N - 1)
            edges[(0, X[V])] = randint(1, W)
        for j in range(3):
            for i in range(M - len(edges)):
                U = randint(0, N - 1)
                V = randint(0, N - 1)
                while U == V:
                    V = randint(0, N - 1)
                U, V = min(U, V), max(U, V)
                if (X[U], X[V]) not in edges:
                    edges[(X[U], X[V])] = randint(1, W)
        print(N, len(edges))
        for (U, V) in edges:
            print(U, V, edges[(U, V)])
    if X == "rand3":
        edges = {}
        X = list(range(1, N))
        shuffle(X)
        X = [0] + X
        for i in range(len(X) - 1):
            edges[(X[i], X[i + 1])] = 1
        for j in range(3):
            for i in range(M - len(edges)):
                U = randint(0, N - 1)
                V = randint(0, N - 1)
                while U == V:
                    V = randint(0, N - 1)
                if (U, V) not in edges:
                    edges[(U, V)] = randint(2, W)
        print(N, len(edges))
        for (U, V) in edges:
            print(U, V, edges[(U, V)])
    if X == "rand2":
        edges = {}
        last = 0
        for i in range(max(3, min(N // 2, M // 3))):
            V = randint(1, N - 1)
            while V == last:
                V = randint(1, N - 1)
            edges[(last, V)] = 1
            last = V
        for j in range(3):
            for i in range(M - len(edges)):
                U = randint(0, N - 1)
                V = randint(0, N - 1)
                while U == V:
                    V = randint(0, N - 1)
                if (U, V) not in edges:
                    edges[(U, V)] = randint(1, W)
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
