#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
import math
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


def add_edge(u, v):  # add_edge hamis ha hurokél, vagy ha v1,v2 rendezett pár már szerepel
    if u == v:
        return False
    a, b = min(u, v), max(u, v)
    if (a, b) in used:
        return False
    return True


def gen_euler_cycle(vertices, num_edges):
    v1 = choice(vertices)
    v2 = choice(vertices)
    while not add_edge(v1, v2):  # elkerüljük hurokélt
        v1 = choice(vertices)
        v2 = choice(vertices)
    a, b = min(v1, v2), max(v1, v2)
    used.add((a, b))  # a used set rendezett párokat tartalmaz
    for _ in range(num_edges - 2):  # -2 mert ezelőtt van kezdőél. és a végén egy éllel bezárjuk a kört
        v3 = choice(vertices)
        while (
            not add_edge(v2, v3) or v3 == v1
        ):  # csalok, csak olyan gráfot generálok amiben van legalább egy pont 2 fokszámú csúcs
            v3 = choice(vertices)
        a, b = min(v2, v3), max(v2, v3)
        used.add((a, b))
        v2 = v3
    add_edge(v1, v3)
    a, b = min(v1, v3), max(v1, v3)
    used.add((a, b))


def gen_euler_path(vertices, num_edges):
    v1 = choice(vertices)
    v2 = choice(vertices)
    while not add_edge(v1, v2):
        v1 = choice(vertices)
        v2 = choice(vertices)
    a, b = min(v1, v2), max(v1, v2)
    used.add((a, b))
    for _ in range(num_edges - 3):  # -3 mert a végén elrontom a kör tulajdonságot egy éllel
        v3 = choice(vertices)
        while not add_edge(v2, v3) or v3 == v1:
            v3 = choice(vertices)
        a, b = min(v2, v3), max(v2, v3)
        used.add((a, b))
        v2 = v3
    add_edge(v1, v3)
    a, b = min(v1, v3), max(v1, v3)
    used.add((a, b))  # ugyanaz mint előző csak még hozzáadok egy élt, hogy ne kör hanem séta legyen
    sv1 = choice(
        vertices
    )  # szintén picit csalás,mert így nincs összefüggő egyáltalán nem euler eset. Ugyanakkor nincs szükség a két eset megkülönböztetésére.
    sv2 = choice(vertices)
    while not add_edge(sv1, sv2):
        sv1 = choice(vertices)
        sv2 = choice(vertices)
    a, b = min(sv1, sv2), max(sv1, sv2)
    used.add((a, b))


def disconnected_graphs(N_vertice, num_edges):
    max_components = min(
        N_vertice // int(math.sqrt(num_edges)), num_edges
    )  # Egyszerű gráf ugye max n*(n-1)/2 élt tartalmazhat, de euler köröket generáálok amikben minden csúcs páros fokszám kell legyen
    # stb stb szóval teljesen hasraütés szerűen ezeket a limiteket számontartva.v/sqrt(e) egész jó közelítés felsőértéknek
    components_count = randint(2, max_components)
    cut_points = sorted(
        sample(range(1, num_edges), components_count - 1)
    )  # random választunk vágási pontokat, hogy melyik részgráf mennyi élet tartalmazzon
    distribution = (
        [cut_points[0]]
        + [cut_points[i] - cut_points[i - 1] for i in range(1, len(cut_points))]
        + [num_edges - cut_points[-1]]
    )
    shuffled_vertices = list(range(1, N_vertice))
    # egyenletesen elosztjuk a csúcsokat, így biztos függetlenenk lesznek a generált részgráfok

    shuffle(shuffled_vertices)
    sub_vertices = []
    n_vertices = len(shuffled_vertices)
    base = n_vertices // components_count
    remainder = n_vertices % components_count
    index = 0
    for i in range(components_count):
        count = base + (1 if i < remainder else 0)
        subset = shuffled_vertices[index : index + count]
        sub_vertices.append(subset)
        index += count

    for comp_edges, comp_vertices in zip(distribution, sub_vertices):
        words_sub = gen_euler_cycle(
            comp_vertices, comp_edges
        )  # a részgráfok mind euler körök,mert ha euler séták lennének akkor több csúcs fokszáma se stimmelne ezért nem lenne szükség összefüggés ellenőrzésre.


def run(A, B, C):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(A, B)
    vert = range(1, A + 1)
    match C:
        case 1:
            gen_euler_cycle(vert, B)
        case 2:
            gen_euler_path(vert, B)
        case 3:
            disconnected_graphs(A, B)

    for u, v in used:
        if choice([True, False]):
            edges.append((v, u))
        else:
            edges.append((u, v))
    shuffle(edges)
    for u, v in edges:
        print(u, v)


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
