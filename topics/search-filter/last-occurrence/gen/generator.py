#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
import string
from random import random, randint, choices, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "last-occurrence".

Parameters:
* A (minimum value)
* B (maximum value)
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
    random_letter = choice(string.ascii_lowercase)
    chance = 1
    if B == 1:
        chance = randint(1, 3)
    if A > 1 and chance > 1:
        B = B - 1
        A = A - 1
    letters = [random_letter] * B
    remaining_letters = [char for char in string.ascii_lowercase if char != random_letter]
    letters.extend(choices(remaining_letters, k=A - B))
    shuffle(letters)
    random_word = "".join(letters)
    if chance == 2:
        random_word = random_word + random_letter
    if chance == 3:
        random_word = random_letter + random_word
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
