#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature
import string

usage = """Generator for "go-to-jail".

Parameters:
* N (number of entries)
* S (seed)

Constraint:
* %d <= N <= %d
""" % (
    MIN,
    MAX,
)


def get_random_name():
    length = randint(3, 8)
    return "".join(choice(string.ascii_lowercase) for _ in range(length))


def run(n_pairs):
    # 1. Decide on the population size based on N
    # We need enough entities to support N edges without too many duplicates
    min_entities = max(4, int(n_pairs / 2))
    num_plants = randint(2, max(2, min_entities // 3))
    num_herbivores = randint(1, max(2, min_entities // 3))
    num_carnivores = max(1, min_entities - num_plants - num_herbivores)

    # 2. Generate unique names
    all_names = set()
    while len(all_names) < (num_plants + num_herbivores + num_carnivores):
        all_names.add(get_random_name())

    all_names_list = list(all_names)
    shuffle(all_names_list)

    # 3. Assign Roles
    plants = all_names_list[:num_plants]
    herbivores = all_names_list[num_plants : num_plants + num_herbivores]
    carnivores = all_names_list[num_plants + num_herbivores :]

    animals = herbivores + carnivores
    pairs = set()

    # 4. Create Mandatory Edges (to define the roles)

    # Every Herbivore MUST eat at least one plant
    for herb in herbivores:
        pairs.add((herb, choice(plants)))

    # Every Carnivore MUST eat at least one animal (herbivore or other carnivore)
    for carn in carnivores:
        # Pick a prey that is an animal (could be herbivore or another carnivore)
        prey = choice(animals)
        # Avoid self-cannibalism for simplicity (though technically allowed by task)
        while prey == carn and len(animals) > 1:
            prey = choice(animals)
        pairs.add((carn, prey))

    # 5. Fill the remaining pairs until we reach N
    # We must respect the rules:
    # - Plants never eat (never on left)
    # - Herbivores only eat plants (left=herb, right=plant)
    # - Carnivores can eat anything (left=carn, right=any)

    attempts = 0
    while len(pairs) < n_pairs and attempts < 1000:
        attempts += 1

        # Pick a random eater type
        eater_type = choice(["herb", "carn"])

        if eater_type == "herb" and herbivores:
            eater = choice(herbivores)
            eaten = choice(plants)
            pairs.add((eater, eaten))

        elif eater_type == "carn" and carnivores:
            eater = choice(carnivores)
            # Carnivores can eat plants (omnivore) or animals
            eaten = choice(all_names_list)
            if eater != eaten:  # Optional: prevent self-eating
                pairs.add((eater, eaten))

    output_lines = []
    output_lines.append(
        str(len(pairs))
    )

    pair_list = list(pairs)
    shuffle(pair_list)

    print(len(pair_list))
    for p1, p2 in pair_list:
        print(f"{p1} {p2}")

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
