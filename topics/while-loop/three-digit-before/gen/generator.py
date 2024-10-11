#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "three-digit-before".

Parameters:
* N (first zero/length of input)
* R (result)
* M (maximum value in lines)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= M <= %d
* 0 <= R <= 900
""" % (
    MINN,
    MAXN,
    MINS,
    MAXS,
)


def run(N, R, M):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    nums = []
    while len(nums) < R:
        X = randint(100, min(M, 999))
        if X not in nums:
            nums.append(X)
    while len(nums) < N - 1:
        X = randint(1, M)
        if X not in nums and (X < 100 or X >= 1000):
            nums.append(X)
    shuffle(nums)
    for num in nums:
        print(num)
    print(0)


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
