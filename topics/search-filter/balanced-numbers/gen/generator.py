#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "balanced-numbers".

Parameters:
* A (N : array length)
* B (result, csak kb.)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
* %d <= C <= %d
""" % (
    MINN,
    MAXN,
    0,
    MAXN,
    MINA,
    MAXA,
)


def run(A, B, C):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    assert B <= A - 2 or B == 0
    resindices = set()
    if A > 2:
        while len(resindices) < B:
            resindices.add(randint(1, A - 2))  # 0-based
    indices = sorted(resindices)
    lista = [0] * A
    for i in indices:
        if lista[i - 1] == 0 and lista[i] == 0:
            x = randint(1, C)
            y = randint(1, C)
            while 2 * y - x > C or 2 * y - x < 1:
                x = randint(1, C)
                y = randint(1, C)
            lista[i - 1] = x
            lista[i] = y
            lista[i + 1] = 2 * y - x
        elif lista[i] != 0:
            if 1 <= lista[i] * 2 - lista[i - 1] <= C:
                lista[i + 1] = lista[i] * 2 - lista[i - 1]
            # else: not succeed
        else:  # lista[i-1] != 0, but lista[i] == 0
            x = lista[i - 1]
            y = randint(1, C)
            while 2 * y - x > C or 2 * y - x < 1:
                y = randint(1, C)
            lista[i] = y
            lista[i + 1] = 2 * y - x

    for i in range(len(lista)):
        if lista[i] == 0:
            lista[i] = randint(1, C)

    print(len(lista))
    print(*lista)


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
