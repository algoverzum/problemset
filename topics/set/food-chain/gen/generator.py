#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
import string
from random import random, choices, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "food-chain".

Parameters:
* A (N)
* B (Carnivore)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MIN,
    MAX,
    MINC,
    MAXC,
)


def random_word(min_length=3, max_length=100):
    """Generate a random word of lowercase letters between min_length and max_length."""
    length = randint(min_length, max_length)
    return "".join(choices(string.ascii_lowercase, k=length))


def unique_names(count):
    """Generate a set of `count` unique random words."""
    names = set()
    while len(names) < count:
        names.add(random_word())
    return names


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(A)
    pairs = set()

    unused_carnivores = unique_names(B)
    used_carnivores = set()
    herbivores = unique_names(60)
    while not unused_carnivores.isdisjoint(herbivores):
        herbivores = unique_names(60)

    plants = unique_names(60)
    while not plants.isdisjoint(unused_carnivores) or not plants.isdisjoint(herbivores):
        plants = unique_names(60)
    herbivores = list(herbivores)
    plants = list(plants)
    remaining_pairs = A - B
    while unused_carnivores:
        current = unused_carnivores.pop()
        target = None
        carnivore_candidates = list(used_carnivores | unused_carnivores)
        used_carnivores.add(current)
        # ha van még remaining pair akkor 50% hogy egy másik húsevőt eszik meg. Ilyenkor a used+unused set-ből választok egyet random. Ha növényevőt eszik akkor meg azonnal generálok egy növényevő-növény párt.
        if (carnivore_candidates and choice([True, False])) or remaining_pairs == 0:
            target = choice(carnivore_candidates)
            pairs.add((current, target))
        else:
            target = choice(herbivores)
            pairs.add((current, target))
            plant = choice(plants)
            pairs.add((target, plant))
            remaining_pairs = remaining_pairs - 1

    for _ in range(remaining_pairs):
        if choice(["carnivore", "herbivore"]) == "carnivore" and used_carnivores:
            left = choice(list(used_carnivores))
            target_pool = list(used_carnivores) + herbivores + plants
            right = choice(target_pool)
        else:
            left = choice(herbivores)
            right = choice(plants)
        attempts = 0
        while (left, right) in pairs and attempts < 10:
            if choice(["carnivore", "herbivore"]) == "carnivore" and used_carnivores:
                left = choice(list(used_carnivores))
                target_pool = list(used_carnivores) + herbivores + plants
                right = choice(target_pool)
            else:
                left = choice(herbivores)
                right = choice(plants)
            attempts += 1
        pairs.add((left, right))

    pairs_list = list(pairs)
    shuffle(pairs_list)

    for left, right in pairs_list:
        print(left, right)


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
