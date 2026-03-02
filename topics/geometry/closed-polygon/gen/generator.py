#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "closed-polygon".

Parameters:
* N (number of points)
* X (maximum value)
* T (type)
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= X <= %d
""" % (
    MINN,
    MAXN,
    0,
    MAXX,
)


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]) == 0


def run(N, X, type):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    N = randint((3 * N) // 4, N)
    if N < 3:
        N = 3
    if type == "rand":
        points = set()
        while len(points) < N:
            x = randint(-X, X)
            y = randint(-X, X)
            points.add((x, y))
        print(N)
        for P in points:
            print(*P)
    if type == "line":
        P1 = (randint(-X // 2, X // 2), randint(-X // 2, X // 2))
        P2 = (randint(-X // 2, X // 2), randint(-X // 2, X // 2))
        P3 = (P2[0] + randint(-50, 50), P2[1] + randint(-50, 50))
        while collinear(P1, P2, P3):
            P2 = (randint(-X // 2, X // 2), randint(-X // 2, X // 2))
            P3 = (P2[0] + randint(-50, 50), P2[1] + randint(-50, 50))
        points = {P1, P2, P3}
        x, y = P3[0] - P2[0], P3[1] - P2[1]
        maxi = max(abs(x), abs(y))
        for i in range(N - 3):
            mult = randint(-MAXX // maxi, MAXX // maxi)
            P = P2[0] + mult * x, P2[1] + mult * y
            while P[0] < -MAXX or P[1] < -MAXX or P[0] > MAXX or P[1] > MAXX:
                mult = randint(-MAXX // maxi, MAXX // maxi)
                P = P2[0] + mult * x, P2[1] + mult * y
            points.add(P)
        print(len(points))
        for P in points:
            print(*P)
    if type == "2lines":
        P1 = (randint(-X // 2, X // 2), randint(-X // 2, X // 2))
        P2 = (P1[0] + randint(-50, 50), P1[1] + randint(-50, 50))
        P3 = (P1[0] + randint(-50, 50), P1[1] + randint(-50, 50))
        while collinear(P1, P2, P3):
            P2 = (P1[0] + randint(-50, 50), P1[1] + randint(-50, 50))
            P3 = (P1[0] + randint(-50, 50), P1[1] + randint(-50, 50))
        points = {P1, P2, P3}
        x, y = P2[0] - P1[0], P2[1] - P1[1]
        xx, yy = P3[0] - P1[0], P3[1] - P1[1]
        maxi = max(abs(x), abs(y), abs(xx), abs(yy))
        for i in range(N - 3):
            mult = randint(-MAXX // maxi, MAXX // maxi)
            P = P1[0] + mult * x, P1[1] + mult * y
            while P[0] < -MAXX or P[1] < -MAXX or P[0] > MAXX or P[1] > MAXX:
                mult = randint(-MAXX // maxi, MAXX // maxi)
                P = P1[0] + mult * x, P1[1] + mult * y
            if len(points) < N:
                points.add(P)
            mult = randint(-MAXX // maxi, MAXX // maxi)
            P = P1[0] + mult * xx, P1[1] + mult * yy
            while P[0] < -MAXX or P[1] < -MAXX or P[0] > MAXX or P[1] > MAXX:
                mult = randint(-MAXX // maxi, MAXX // maxi)
                P = P1[0] + mult * xx, P1[1] + mult * yy
            if len(points) < N:
                points.add(P)
        print(len(points))
        for P in points:
            print(*P)
    if type == "5lines":
        P1 = (randint(-X // 2, X // 2), randint(-X // 2, X // 2))
        dir = []
        for i in range(5):
            dir.append((randint(-100, 100), randint(-100, 100)))
        points = {P1}
        maxi = 100
        for i in range(N - 3):
            for x, y in dir:
                mult = randint(-MAXX // maxi, MAXX // maxi)
                P = P1[0] + mult * x, P1[1] + mult * y
                while P[0] < -MAXX or P[1] < -MAXX or P[0] > MAXX or P[1] > MAXX:
                    mult = randint(-MAXX // maxi, MAXX // maxi)
                    P = P1[0] + mult * x, P1[1] + mult * y
                if len(points) < N:
                    points.add(P)
        print(len(points))
        for P in points:
            print(*P)


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
