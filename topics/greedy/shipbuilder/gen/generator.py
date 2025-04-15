#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed, choices
from inspect import signature

usage = """Generator for "shipbuilder".

Parameters:
* A (number of orders)
* B (max days)
* C (type)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MINN,
    MAXN,
    MINH,
    MAXH,
)


def run(A, B, T):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(A)
    days = []
    match T:
        case "random":
            bias = 0.9
            for i in range(A):
                if days and random() < bias:
                    day = choice(days)
                else:
                    day = randint(1, B)
                days.append(day)
        case "incremental":
            lastday = 0
            for i in range(A):
                if lastday < B:
                    lastday = lastday + 1
                    days.append(lastday)
                else:
                    days.append(randint(1, B))

        case "one_deadline":
            day = randint(1, B)
            for i in range(A):
                days.append(day)
    days.sort()
    print(*days)


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
