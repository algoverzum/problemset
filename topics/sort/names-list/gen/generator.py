#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
import string
from random import random, choices, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "names-list".

Parameters:
* A (number of words)
* B (maximum word length)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
)


def run(A, B):
    def random_word(max_length):
        length = randint(1, max_length)
        return "".join(choices(string.ascii_lowercase, k=length))

    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(A)
    list1 = list()
    if A == 101:
        letter = choice(string.ascii_lowercase)
        while len(list1) < A:
            list1.append(letter + random_word(B - 1))
    else:
        while len(list1) < A:
            list1.append(random_word(B))
    print(*list1)


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
