#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "tukorszo2".

Parameters:
* N (the length of the word)
* S (seed)

Constraint:
* %d <= N <= %d
""" % (
    MIN,
    MAX,
)

abc = [chr(ord("a") + i) for i in range(26)] + [" "]


def run(N):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    word = []
    x = randint(1, 10)
    if N == 1:
        x = 1
    if x in [1, 2]:
        for _ in range(N):
            word.append(choice(abc))
    if x in [3, 4, 5, 6]:
        for _ in range(N // 2):
            word.append(choice(abc))
        rev = word[::-1]
        if N % 2 == 0:
            word += rev
        else:
            word.append(choice(abc))
            word += rev
    if x in [7, 8, 9, 10]:
        for _ in range(N // 2):
            word.append(choice(abc))
        rev = word[::-1]
        a = randint(1, 8)
        for i in range(a):
            word[randint(0, len(word) - 1)] = chr(randint(ord("a"), ord("z")))
        if N % 2 == 0:
            word += rev
        else:
            word.append(choice(abc))
            word += rev

    for i in range(1, len(word)):
        if word[i] == " ":
            x = randint(1, 3)
            if x == 1:
                word[i], word[i - 1] = word[i - 1], word[i]

    print(*word, sep="")


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
