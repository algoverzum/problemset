#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "stargates".

Parameters:
* A (N value)
* B (R value)
* C (Type)
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
    MIN3,
    MAX3,
)

used = set()  # a már felhasznált éleket (rendezett (min, max))
edges = []  # az éleket tartalmazó lista
v1 = 0


def add_edge(u, v):
    if u == v or v == v1:
        return False
    a, b = min(u, v), max(u, v)
    if (a, b) in used:
        return False
    used.add((a, b))
    if random.choice([True, False]):
        edges.append((v, u))
    else:
        edges.append((u, v))
    return True


def gen_euler_cycle(vertices, num_edges):

    v1 = choice(vertices)
    v2 = choice(vertices)
    while not add_edge(v1, v2):
        v1 = choice(vertices)
        v2 = choice(vertices)

    for _ in range(num_edges - 2):
        v3 = choice(vertices)
        while not add_edge(v2, v3):
            v3 = choice(vertices)
        v2 = v3
    add_edge(v1, v3)


def gen_euler_path(vertices, num_edges):
    v1 = choice(vertices)
    v2 = choice(vertices)
    while not add_edge(v1, v2):
        v1 = choice(vertices)
        v2 = choice(vertices)

    for _ in range(num_edges - 3):
        v3 = choice(vertices)
        while not add_edge(v2, v3):
            v3 = choice(vertices)
        v2 = v3
    add_edge(v1, v3)
    sv1 = choice(vertices)
    sv2 = choice(vertices)
    while not add_edge(sv1, sv2):
        sv1 = choice(vertices)
        sv2 = choice(vertices)


def disconnected_graphs(vertices, num_edges):
    max_components = min(
        5, num_edges
    )  # 26 csúcsunk van ugye, egyenlőre be van égetve, hogy max 5 független részgráf !ÁTÍRANDÓ
    components_count = randint(2, max_components)
    cut_points = sorted(
        sample(range(1, num_edges), components_count - 1)
    )  # random választunk vágási pontokat, hogy melyik részgráf mennyi élet tartalmazzon
    distribution = (
        [cut_points[0]]
        + [cut_points[i] - cut_points[i - 1] for i in range(1, len(cut_points))]
        + [num_edges - cut_points[-1]]
    )
    shuffled_vertices = (
        vertices  # egyenletesen elosztjuk a csúcsokat, így biztos függetlenenk lesznek a generált részgráfok
    )
    shuffle(shuffled_vertices)
    sub_vertices = []
    n_vertices = len(shuffled_vertices)
    base = n_vertices // components_count
    remainder = n_vertices % components_count
    index = 0


def run(A, B, C):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(A, B)


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
