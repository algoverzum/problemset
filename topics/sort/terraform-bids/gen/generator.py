#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
import string
from random import random, randint, choice, sample, shuffle, seed, choices, gauss
from inspect import signature

usage = """Generator for "terraform-bids".

Parameters:
* A (N value)
* B (Type)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MIN,
    MAX,
    0,
    1,
)


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]
    print(A)
    words = set()
    # full random
    if B == 0:
        for i in range(A):
            length = randint(1, 10)

            random_string = "".join(choices(string.ascii_lowercase, k=length))
            while random_string in words:
                length = randint(1, 10)
                random_string = "".join(choices(string.ascii_lowercase, k=length))
            words.add(random_string)
            bid = randint(1, MAX)
            print(random_string, bid)
        next
    # clustered
    elif B == 1:
        num_clusters = randint(1, 10)
        cluster_centers = [randint(1, MAX) for _ in range(num_clusters)]

        for _ in range(A):
            length = randint(1, 10)
            random_string = "".join(choices(string.ascii_lowercase, k=length))
            while random_string in words:
                length = randint(1, 10)
                random_string = "".join(choices(string.ascii_lowercase, k=length))
            words.add(random_string)
            center = choice(cluster_centers)
            bid = int(gauss(center, 5))
            bid = max(1, min(MAX, bid))

            print(random_string, bid)


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
