#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "shortest-cycle".

Parameters:
* A (minimum value)
* B (maximum value)
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


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]
    unused_nodes = list(range(A))
    edges = set()
    parent = [-1] * (A + 1)
    dist = [-1] * (A + 1)
    root = 1
    dist[root] = 0
    used_nodes = [root]
    unused_nodes.remove(root)
    remaining_edges = B - A
    mindist = 2 * A
    sub_trees = 3
    sub_tree_parents = [] * sub_trees
    for _ in range(sub_trees):
        v = choice(unused_nodes)
        unused_nodes.remove(v)
        used_nodes.append(v)
        sub_tree_parents.append(v)
        dist[v] = 1
        parent[v] = root
        edges.add((min(root, v), max(root, v)))

    shuffle(unused_nodes)  # Shuffle to ensure randomness
    split_points = sorted(sample(range(1, len(unused_nodes)), sub_trees - 1))  # Choose split points
    split_nodes = [unused_nodes[i:j] for i, j in zip([0] + split_points, split_points + [len(unused_nodes)])]
    for i in range(sub_trees):
        used_sub_nodes = [sub_tree_parents[i]]
        for j in range(len(split_nodes[i])):
            cs = choice(split_nodes[i])
            p = choice(used_sub_nodes)
            split_nodes[i].remove(cs)
            used_sub_nodes.append(cs)
            dist[cs] = dist[p] + 1
            parent[cs] = p
            edges.add((min(p, cs), max(cs, p)))


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
