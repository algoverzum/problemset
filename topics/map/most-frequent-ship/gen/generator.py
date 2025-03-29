#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "most-frequent-ship".

Parameters:
* N (length of list)
* M (max number of different numbers in list)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= M <= %d
""" % (
    MIN,
    MAX,
    0,
    MAX,
)


def run(N, M):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    if M == 0:
        # special case for N different numbers
        print(N)
        s = set()
        while len(s) < N:
            s.add(randint(-(10**9), 10**9))
        s = list(s)
        shuffle(s)
        print(*s)
        return

    if N > 1000:
        N -= randint(1, 100)
    numbers = set()
    while len(numbers) < M:
        numbers.add(randint(-(10**9), 10**9))
    numbers = list(numbers)
    A = []
    for i in range(N):
        A.append(choice(numbers))
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
