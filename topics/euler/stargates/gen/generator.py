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
    1,
    5,
)

used = set()  # a már felhasznált éleket (rendezett (min, max))
edges = []  # az éleket tartalmazó lista


def can_add_edge(u, v):  # can_add_edge hamis ha hurokél, vagy ha u,v pár már szerepel
    if u == v:
        return False
    a, b = min(u, v), max(u, v)
    if (a, b) in used:
        return False
    return True


from collections import defaultdict


def gen_euler_cycle(vertices, num_edges):
    # nem fut le mindig... akkor a randseed-en kell valtoztatni...
    v1 = choice(vertices)  # ez lesz deg 2
    v2 = choice(vertices)
    while v1 == v2:
        v2 = choice(vertices)
    a, b = min(v1, v2), max(v1, v2)
    deg = defaultdict(int)
    deg[a] += 1
    deg[b] += 1
    used.add((a, b))
    deg = defaultdict(int)
    for ii in range(num_edges - 2):  # -2 mert a végén egy éllel bezárjuk a kört, es elkezdtuk mar...
        v3 = choice(vertices)
        while v3 == v2:
            v3 = choice(vertices)
        while not can_add_edge(v2, v3) or v3 == v1:
            v4 = choice(vertices)
            if ii != num_edges - 3 or deg[v4] < len(vertices) - 2:
                v3 = v4
        a, b = min(v2, v3), max(v2, v3)
        deg[a] += 1
        deg[b] += 1
        used.add((a, b))
        v2 = v3
    # can_add_edge(v1, v3) # ez tuti jo, deg(v2) = 2
    a, b = min(v1, v3), max(v1, v3)
    used.add((a, b))


def gen_euler_path(vertices, num_edges):
    gen_euler_cycle(
        vertices, num_edges - 1
    )  # ugyanaz mint előző csak még hozzáadok egy élt, hogy ne kör hanem séta legyen
    sv1 = choice(
        vertices
    )  # szintén picit csalás,mert így nincs összefüggő egyáltalán nem euler eset. Ugyanakkor nincs szükség a két eset megkülönböztetésére.
    sv2 = choice(vertices)
    while not can_add_edge(sv1, sv2):
        sv1 = choice(vertices)
        sv2 = choice(vertices)
    a, b = min(sv1, sv2), max(sv1, sv2)
    used.add((a, b))


def gen_euler_path2(vertices, num_edges):
    gen_euler_cycle(vertices, num_edges + 1)
    used.pop()


def split(num_vertices, num_edges):
    if num_vertices < 12 or num_edges < 10:
        return [(num_vertices, num_edges)]
    v1 = randint(6, num_vertices - 6)
    v2 = num_vertices - v1
    e1 = randint(3, max(3, min(num_edges - 3, (v1 - 1) * (((v1 - 2) // 2)))))
    e2 = num_edges - e1
    loop = 0
    while e2 > (v2 - 1) * (((v2 - 2) // 2)):
        v1 = randint(6, num_vertices - 6)
        v2 = num_vertices - v1
        e1 = randint(3, max(3, min(num_edges - 3, (v1 - 1) * (((v1 - 2) // 2)))))
        e2 = num_edges - e1
        loop += 1
        if loop > 100:
            return [(num_vertices, num_edges)]
    assert v1 + v2 == num_vertices
    assert e1 + e2 == num_edges
    assert min(v1, v2, e1, e2) >= 3
    return [(v1, e1), (v2, e2)]


def disconnected_graphs(N_vertice, num_edges):
    cur = [(N_vertice, num_edges)]
    for j in range(randint(1, 11)):  # legalabb 1x, max 10x 1-gyel tobb komponens lesz ha lehet
        i = randint(0, len(cur) - 1)
        cur = cur[:i] + split(*cur[i]) + cur[i + 1 :]
    shuffled_vertices = list(range(1, N_vertice + 1))
    # egyenletesen elosztjuk a csúcsokat, így biztos függetlenenk lesznek a generált részgráfok
    shuffle(shuffled_vertices)
    index = 0
    for (v, e) in cur:
        gen_euler_cycle(shuffled_vertices[index : index + v], e)  # a részgráfok mind euler körök
        index += v


def run(A, B, C):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    print(A, B)
    vert = range(1, A + 1)
    if C == 1:
        gen_euler_cycle(vert, B)
    elif C == 2:
        gen_euler_path(vert, B)
    elif C == 3:
        disconnected_graphs(A, B)
    elif C == 4:  # random elek, valoszinu nagyon nem jo...
        while len(used) < B:
            u = randint(1, A)
            v = randint(1, A)
            if u != v:
                used.add((min(u, v), max(u, v)))
    elif C == 5:  # random haromszogek, ha 3|B es B eleg nagy akkor YES
        while len(used) < B:
            u = randint(1, A)
            v = randint(1, A)
            w = randint(1, A)
            if len({u, v, w}) == 3 and can_add_edge(u, v) and can_add_edge(u, w) and can_add_edge(w, v):
                used.add((min(u, v), max(u, v)))
                if len(used) == B:
                    break
                used.add((min(u, w), max(u, w)))
                if len(used) == B:
                    break
                used.add((min(w, v), max(w, v)))

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
