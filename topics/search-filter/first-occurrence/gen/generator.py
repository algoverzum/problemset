#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
import string
from random import random, randint, choices, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "first-occurrence".

Parameters:
* A (word length)
* B (key letter appearance count)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MIN,
    MAX,
    MIN2,
    MAX2,
)


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]
    random_letter = choice(string.ascii_letters)
    letters = [random_letter] * B
    remaining_letters = [char for char in string.ascii_letters if char != random_letter]
    letters.extend(choices(remaining_letters, k=A - B))
    shuffle(letters)
    random_word = "".join(letters)
    print(random_word)
    print(random_letter)


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
