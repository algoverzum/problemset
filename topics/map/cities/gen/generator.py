#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
import string
from random import random, randint, choices, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "cities".

Parameters:
* A (N)
* B (M)
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
words = set()


def createword():
    length = randint(1, 10)
    wor = "".join(choices(string.ascii_lowercase, k=length))
    while wor in words:
        length = randint(1, 10)
        wor = "".join(choices(string.ascii_lowercase, k=length))
    words.add(wor)
    return wor


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]
    planets = set()
    cities = set()
    print(A)
    for i in range(A):
        planet_data = []
        word = createword()
        planets.add(word)
        planet_data.append(word)
        wcount = randint(1, 1000)
        for j in range(wcount):
            word = createword()
            cities.add(word)
            planet_data.append(word)
        print(*planet_data)
    print(B)
    queries = choices(list(cities), k=B)
    for k in range(B):
        print(queries[k])


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
