#!/usr/bin/env python3

from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "varazslo".

Parameters:
* N (length)
* S (seed)

Constraint:
* 1 <= N <= 1000
"""


def run(N):
    print(N)
    titles = set()
    while len(titles) < N:
        title_length = randint(3, 10)
        title = "".join(choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") for _ in range(title_length))
        if title in titles:
            continue

        titles.add(title)
        year = randint(1000, 2024)
        print(f"{title} {year}")


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
