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
    match T:
        case "random":
            split_points = sorted(sample(range(1, A), B))
            split_days = [unused_nodes[i:j] for i, j in zip([0] + split_points, split_points + [len(unused_nodes)])]
            for i in range(A):

                next
        case "incremental":
            lastday = 0
            for i in range(A):
                lastday = lastday + 1
                print(lastday)
        case "one_deadline":
            next


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
