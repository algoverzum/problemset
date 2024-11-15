#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "longer-word".

Parameters:
* A (0: same words, 1: same length words, 2: different lengths words)
* S (seed)

Constraint:
* %d <= A <= %d
""" % (
    0,
    2,
)


def run(A):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]
    words = [
        "kormány",
        "év",
        "ember",
        "törvény",
        "László",
        "úr",
        "szó",
        "ország",
        "elnök",
        "István",
        "mond",
        "kerül",
        "tud",
        "köszön",
        "sikerül",
        "jelent",
        "kap",
        "tart",
        "tesz",
        "hisz",
        "magyar",
        "nagy",
        "új",
        "jó",
        "politika",
        "kis",
        "egész",
        "gazdaság",
        "amerika",
        "nemzetközi",
    ]
    if A == 0:
        word = choice(words)
        print(word)
        print(word)
    elif A == 1:
        word1 = choice(words)
        word2 = choice(words)
        while len(word1) != len(word2) or word1 == word2:
            word1 = choice(words)
            word2 = choice(words)
        print(word1)
        print(word2)
    else:
        word1 = choice(words)
        word2 = choice(words)
        while len(word1) == len(word2):
            word1 = choice(words)
            word2 = choice(words)
        print(word1)
        print(word2)


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
