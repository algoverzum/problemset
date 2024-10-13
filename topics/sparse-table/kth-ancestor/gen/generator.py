#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
import math
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "kth-ancestor".

Parameters:
* Case (type of test case)
* N (number of nodes)
* Q (number of queries)
* A (number of additions to the tree)
* B (number of removals from tree)
* C (number of type 2 queries)
* D (chance of type 2 query being a 0, because of node not in tree or Kth parent not in tree. Also either hapening sets the answer to 0, so the probability of each will be 1-sqrt(1-D))
* S (seed)
A+B+C=Q   fontos
Constraint:
* %d <= N <= %d
* %d <= Q <= %d
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
)


def run(Case, N, Q, A, B, C, D):
    tree = {}
    not_in_tree = list(range(2, N))
    leaf_nodes = [1]
    tree[1] = {"parent": None, "children": 0, "depth": 0}
    for _ in range(A // 2):
        X = random.choice(not_in_tree)
        Y = random.choice(tree)
        print(f"0 {Y} {X}")
        not_in_tree.remove(X)
        tree[X] = {"parent": Y, "children": 0, "depth": tree[Y]["depth"] + 1}
        leaf_nodes.append(X)
        tree[Y]["children"] += 1
        if Y in leaf_nodes:
            leaf_nodes.remove(Y)
    A = A - A // 2
    lst = [0] * A + [1] * B + [2] * C
    random.shuffle(lst)
    for item in lst:
        if item == 0:
            X = random.choice(not_in_tree)
            Y = random.choice(tree)
            print(f"0 {Y} {X}")
            not_in_tree.remove(X)
            tree[X] = {"parent": Y, "children": 0, "depth": tree[Y]["depth"] + 1}
            leaf_nodes.append(X)
            tree[Y]["children"] += 1
            if Y in leaf_nodes:
                leaf_nodes.remove(Y)
        elif item == 1:
            X = random.choice(leaf_nodes)
            print(f"1 {X}")
            leaf_nodes.remove(X)
            parent = tree[X]["parent"]
            tree[parent]["children"] -= 1
            if tree[parent]["children"] == 0:
                leaf_nodes.append(parent)
            del tree[X]
            not_in_tree.append(X)
        elif item == 2:
            E = 1 - math.sqrt(1 - D)
            if random.random() >= E:
                X = random.choice(not_in_tree)
                K = K = random.randint(1, 100)
            else:
                X = random.choice(tree)
                if random.random() >= E:
                    K = random.randint(tree[X][depth], tree[X][depth] * 2)
                else:
                    K = random.randint(1, tree[x][depth])
        print(f"2 {X} {K}")


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
