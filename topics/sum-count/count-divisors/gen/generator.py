#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from inspect import signature

usage = """Generator for "count-divisors".

Parameters:
* N (VALUE BETWEEN 1 AND 10000)

Constraint:
* %d <= N <= %d
""" % (
    MIN,
    MAX,
)


def run(N):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(N)


if __name__ == "__main__":
    num_args = len(signature(run).parameters) + 1
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

    args = tryconv(argv[1])
    run(args)
