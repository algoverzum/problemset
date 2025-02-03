#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
import string
from random import random, choices, randint, choice, sample, shuffle, randrange, seed
from inspect import signature

usage = """Generator for "word-arrangement".

Parameters:
* A (number of test cases )
* B (maximum word count)
* C (valid chance )
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
* %d <= C <= %d
""" % (
    MIN1,
    MAX1,
    MIN2,
    MAX2,
    MIN4,
    MAX4,
)
ALPHABET = string.ascii_lowercase


def generate_word(first, last, max_length=MAX3):
    length = randint(1, max_length)
    if length == 1:
        if first != last:
            length = 2
        else:
            return first
    if length == 2:
        return first + last
    middle = "".join(choices(ALPHABET, k=length - 2))
    return first + middle + last


def generate_valid_case(num_words: int) -> list:
    valid_type = choice(["cycle", "path"])
    vertices = []
    if valid_type == "cycle":
        start = choice(ALPHABET)
        vertices.append(start)
        for i in range(num_words):
            if i == num_words - 1:
                next_letter = start
            else:
                next_letter = choice(ALPHABET)
            vertices.append(next_letter)
    else:
        start = choice(ALPHABET)
        end = choice([c for c in ALPHABET if c != start])
        vertices.append(start)
        for i in range(num_words):
            if i == num_words - 1:
                next_letter = end
            else:
                next_letter = choice(ALPHABET)
            vertices.append(next_letter)
    words = []
    for i in range(num_words):
        word = generate_word(vertices[i], vertices[i + 1])
        words.append(word)
    shuffle(words)
    return words


def generate_valid_case_subset(num_words: int, letters: str) -> list:
    valid_type = "cycle"
    vertices = []
    if valid_type == "cycle":
        start = choice(letters)
        vertices.append(start)
        for i in range(num_words):
            if i == num_words - 1:
                next_letter = start
            else:
                next_letter = choice(letters)
            vertices.append(next_letter)
    words_sub = [generate_word(vertices[i], vertices[i + 1]) for i in range(num_words)]
    shuffle(words_sub)
    return words_sub


def generate_invalid_case(num_words: int) -> list:
    mode = choice(["degree", "connectivity"])
    if num_words < 2:
        mode = "degree"
    if mode == "degree":
        words = generate_valid_case(num_words)
        i = randrange(len(words))
        original_word = words[i]
        new_first = choice([c for c in ALPHABET if c != original_word[0]])
        if len(original_word) == 1:
            words[i] = new_first
        else:
            words[i] = new_first + original_word[1:]
        return words

    else:
        max_components = min(5, num_words)
        components_count = randint(2, max_components)
        # Elosztjuk az num_words-et a komponensek között úgy, hogy mindegyikhez legalább 1 szó tartozzon.
        # Például, ha num_words = N, generálunk components_count-1 "vágási pontot" az [1, N-1] intervallumban,
        # majd a különbségekkel kapjuk az egyes komponensek szó számát.
        cut_points = sorted(sample(range(1, num_words), components_count - 1))
        words_distribution = (
            [cut_points[0]]
            + [cut_points[i] - cut_points[i - 1] for i in range(1, len(cut_points))]
            + [num_words - cut_points[-1]]
        )

        shuffled_alphabet = list(ALPHABET)
        shuffle(shuffled_alphabet)
        sub_alphabets = []
        n_letters = len(shuffled_alphabet)
        base = n_letters // components_count
        remainder = n_letters % components_count
        index = 0
        for i in range(components_count):
            count = base + (1 if i < remainder else 0)
            subset = "".join(shuffled_alphabet[index : index + count])
            sub_alphabets.append(subset)
            index += count
        words_all = []
        for comp_words, letters in zip(words_distribution, sub_alphabets):
            words_sub = generate_valid_case_subset(comp_words, letters)
            words_all.extend(words_sub)

        shuffle(words_all)
        return words_all


def run(A, B, C):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]
    # print(A)
    for _ in range(A):
        num_words = randint(1, B)
        print(num_words)
        if randint(1, 10) < C:
            words = generate_valid_case(num_words)
        else:
            words = generate_invalid_case(num_words)
        for s in words:
            print(s)


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
