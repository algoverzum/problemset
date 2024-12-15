#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
import string
from random import random, choices, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "fragment".

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
    random_letter = choice(string.ascii_lowercase)
    chance = 1
    state = 0
    if B == 1:
        chance = randint(1, 3)
    if B == 2:
        chance = randint(1, 2)
    if A > 1 and B == 1 and chance > 1:
        B = B - 1
        A = A - 1
        state = 1
    elif A > 1 and B == 2 and chance == 2:
        B = B - 2
        A = A - 2
        state = 2
    letters = [random_letter] * B
    remaining_letters = [char for char in string.ascii_lowercase if char != random_letter]
    letters.extend(choices(remaining_letters, k=A - B))
    shuffle(letters)
    random_word = "".join(letters)
    if state == 2 and chance == 2:
        random_word = random_letter + random_word + random_letter
    if state == 1 and chance == 2:
        random_word = random_word + random_letter
    if state == 1 and chance == 3:
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
