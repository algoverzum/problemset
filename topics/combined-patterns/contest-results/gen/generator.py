#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
import string
from random import random, randint, choices, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "contest-results".

Parameters:
* A (db length)
* B (query length)
* C (max word length)
* D (overlaps)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
* %d <= C <= %d
* %d <= D <= %d
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
    MIN,
    MAX,
    MIN2,
    MAX,
)


def run(A, B, C, D):
    def random_word(max_length):
        length = randint(1, max_length)
        return "".join(choices(string.ascii_lowercase, k=length))

    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]
    print(A, B)
    list1 = set()
    while len(list1) < A:
        list1.add(random_word(C))
    list1 = list(list1)
    list2 = set()
    while len(list2) < (B - D):
        new_word = random_word(C)
        if new_word not in list1:
            list2.add(new_word)
    list2 = list(list2)
    list2.extend(sample(list1, D))
    shuffle(list2)
    print(*list1)
    print(*list2)


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
