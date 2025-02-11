#!/usr/bin/env python3.12

from limits import *
from sys import argv, exit, stderr
import os
import string
from random import random, choices, randint, choice, sample, shuffle, randrange, seed
from inspect import signature

usage = """Generator for "word-arrangement".

Parameters:
* A (type of test cases )
* B (maximum word count)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MIN1,
    MAX1,
    MIN2,
    MAX2,
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


def generate_valid_case(valid_type, num_words: int) -> list:
    # valid_type = choice(["cycle", "path"])
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


def generate_invalid_case(mode, num_words: int) -> list:
    # mode = choice(["degree", "connectivity"])
    valid_type = "path"
    if num_words < 2:
        return ["ablak"]
    if mode == "degree":
        words = generate_valid_case(
            valid_type, num_words - 1
        )  # 1el kissebb méretű euler séta, mert hozzáadunk majd egy élt. num_words==1 eset fentebb megfogva
        invertices = [0] * 26
        outvertices = [0] * 26
        for w in words:
            invertices[ord(w[-1]) - ord("a")] += 1
            outvertices[ord(w[0]) - ord("a")] += 1

        start_nodes = [i for i in range(26) if outvertices[i] - invertices[i] == 1]
        end_nodes = [i for i in range(26) if invertices[i] - outvertices[i] == 1]
        start = start_nodes[0]
        end = end_nodes[0]
        vertices = [
            i for i in range(26) if invertices[i] > 0 or outvertices[i] > 0
        ]  # melyik csúcsok szereplen az euler sétában, hogy véletlen ne hozzunk létre üggetlen gráfot
        while True:
            u = choice(vertices)
            v = choice(vertices)
            if not (
                (u == end and v == start) or (u == v)
            ):  # ha kiegészítenénk euler körré vagy hurokél akkor generáélunk új choicet
                break
        spoiling_word = generate_word(chr(u + ord("a")), chr(v + ord("a")))
        words.append(spoiling_word)
        shuffle(words)
        return words

    else:
        max_components = min(
            5, num_words
        )  # 26 csúcsunk van ugye, egyenlőre be van égetve, hogy max 5 független részgráf
        components_count = randint(2, max_components)
        cut_points = sorted(
            sample(range(1, num_words), components_count - 1)
        )  # random választunk vágási pontokat, hogy melyik részgráf mennyi élet tartalmazzon
        words_distribution = (
            [cut_points[0]]
            + [cut_points[i] - cut_points[i - 1] for i in range(1, len(cut_points))]
            + [num_words - cut_points[-1]]
        )

        shuffled_alphabet = list(
            ALPHABET
        )  # egyenletesen elosztjuk az ábécét, így biztos függetlenenk lesznek a generált részgráfok
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
            words_sub = generate_valid_case_subset(
                comp_words, letters
            )  # a részgráfok mind euler körök,mert ha euler séták lennének akkor több csúcs fokszáma se stimmelne ezért nem lenne szükség összefüggés ellenőrzésre.
            words_all.extend(words_sub)

        shuffle(words_all)
        return words_all


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]
    # print(A)
    num_words = randint(1, B)
    print(num_words)
    mode = ""
    match A:
        case 1:  # euler séta,de nem kör
            mode = "path"
            words = generate_valid_case(mode, num_words)
        case 2:  # euler kör
            mode = "cycle"
            words = generate_valid_case(mode, num_words)
        case 3:  # valid euler sétához hozzá adok egy élet, úgy hogy él ne legyen hurokél vagy egészítse ki a sétát euler körré
            mode = "degree"
            words = generate_invalid_case(mode, num_words)
        case 4:  # valid euler körök generálása független ábécékkel.
            mode = "connectivity"
            words = generate_invalid_case(mode, num_words)

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
