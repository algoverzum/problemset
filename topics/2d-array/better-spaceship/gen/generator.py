#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "better-spaceship".

Parameters:
* N (value of N)
* M (value of M)
* I (index of better ship)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= M <= %d
* %d <= I <= %d
""" % (
    MIN_N,
    MAX_N,
    MIN_N,
    MAX_N,
    MIN_I,
    MAX_I,
)


def run(N, M, I):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(*[N, M])
    if I != -1:
        non_sol = []
        pre_sol = []
        sol = []
        nums = []
        for _ in range(4):
            nums.append(randint(1, 1000))
        nums.sort()
        for _ in range(M):
            pre_sol.append(nums[1])
            sol.append(nums[2])
            non_sol.append(nums[3])
        non_sol[0] = nums[0]
        for _ in range(I - 2):
            print(*non_sol)
        print(*pre_sol)
        print(*sol)
        for _ in range(N - I):
            print(*non_sol)
    else:
        non_sol = []
        num = randint(1, 1000)
        for _ in range(M):
            non_sol.append(num)
        for _ in range(N):
            print(*non_sol)


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
