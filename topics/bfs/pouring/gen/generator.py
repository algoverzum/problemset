#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "pouring".

Parameters:
* A (minimum value of A and B)
* B (maximum value of A and B)
* C (Type)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
* %d <= C <= %d
""" % (
    MIN,
    MAX,
    MIN,
    MAX,
    0,
    NUM_TYPES - 1,
)


def get_solution_matrix(a, b):
    distance = [[-1] * (b + 1) for _ in range(a + 1)]
    distance[0][0] = 0
    queue = [(0, 0)]
    idx = 0

    while idx < len(queue):
        x, y = queue[idx]
        idx += 1
        for i in range(6):
            if i == 0:
                nx, ny = a, y
            elif i == 1:
                nx, ny = x, b
            elif i == 2:
                nx, ny = 0, y
            elif i == 3:
                nx, ny = x, 0
            elif i == 4:
                nx, ny = x - min(x, b - y), y + min(x, b - y)
            else:
                nx, ny = x + min(y, a - x), y - min(y, a - x)

            if distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    return distance


def run(A, B, C):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    if C == 0:
        # random testcase
        a = randint(A, B)
        b = randint(A, B)
        n = randint(1, b)
        print(n)
        print(a, b)
    if C == 1:
        # impossible
        impossible = False
        while not impossible:
            a = randint(A, B)
            b = randint(A, B)
            matrix = get_solution_matrix(a, b)
            for j in range(b + 1):
                if all(matrix[i][j] == -1 for i in range(a + 1)):
                    impossible = True
                    n = j
                    break
        print(n)
        print(a, b)
    if C == 2:
        # maximum number of steps
        a = randint(A, B)
        b = randint(A, B)
        matrix = get_solution_matrix(a, b)
        maxval = -1
        for j in range(b + 1):
            if all(matrix[i][j] == -1 for i in range(a + 1)):
                continue
            val = min(filter(lambda x: x != -1, [matrix[i][j] for i in range(a + 1)]))
            if val > maxval:
                maxval = val
                n = j
        print(n)
        print(a, b)
    if C == 3:
        # n larger than a and b
        a = randint(A, B)
        b = randint(A, B)
        n = randint(max(a, b) + 1, MAX)
        print(n)
        print(a, b)


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
