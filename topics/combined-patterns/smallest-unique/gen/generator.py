#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "smallest-unique".

Parameters:
* A (max value)
* B (number of small duplicates)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= A <= %d
* 0  <= B <= %d
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
    MAX,
)


def run(N, A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(N)
    if B > (N - 1) // 2:
        distincts = sorted(sample(range(1, A + 1), min(A, randint(1, N // 2))))
        nums = distincts * 2
        while len(nums) < N:
            nums.append(choice(distincts))
    else:
        distincts = sorted(sample(range(1, A + 1), min((N + 1) // 2, B + 1)), reverse=True)
        nums = distincts[1:] * 2 + [distincts[0]]
        while len(nums) < N:
            num = randint(1, A)
            while num == distincts[0] or num < distincts[0] and num not in distincts:
                num = randint(1, A)
            nums.append(num)
    shuffle(nums)
    print(*nums)


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
