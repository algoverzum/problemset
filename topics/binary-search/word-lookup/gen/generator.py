#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "word-lookup".

Parameters:
* A (number of word pairs)
* B (number of words in the translation)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MIN,
    MAX_N,
    MIN,
    MAX_M,
)


def run(A, B):
    def generate_random_string():
        length = randint(1, 10)
        return ''.join(choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))

    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(A)
    english_words = set()
    while len(english_words) < A:
        word = generate_random_string()
        english_words.add(word)
    english_words = list(english_words)
    
    alien_words = set()
    while len(alien_words) < A:
        word = generate_random_string()
        alien_words.add(word)
    alien_words = list(alien_words)
    
    english_words.sort()
    for ew, aw in zip(english_words, alien_words):
        print(ew, aw)
    
    print(B)
    for i in range(B):
        print(choice(english_words))


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
