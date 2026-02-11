#!/usr/bin/env python3

from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "shortest-road-renovation".

Parameters:
* N (length of the road)
* M (number of renovations)
* TIES (1 to force multiple shortest renovations, 0 for pure random)
* S (seed)

Constraint:
* 1 <= N <= 100000
* 1 <= M <= 100
* TIES in [0, 1]
"""


def run(N, M, TIES):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    pairs = []

    if TIES == 1 and M >= 2:
        min_len = randint(0, max(0, N - 1))
        num_ties = randint(2, M)

        tie_indices = set(sample(range(M), num_ties))

        for i in range(M):
            if i in tie_indices:
                k = randint(0, N - min_len)
                v = k + min_len
                pairs.append((k, v))
            else:
                if min_len >= N:
                    k, v = 0, N
                else:
                    length = randint(min_len + 1, N)
                    k = randint(0, N - length)
                    v = k + length
                pairs.append((k, v))
    else:
        for _ in range(M):
            k = randint(0, N)
            v = randint(k, N)
            pairs.append((k, v))

    print(f"{N} {M}")
    for k, v in pairs:
        print(f"{k} {v}")


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
