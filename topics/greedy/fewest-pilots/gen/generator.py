#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "fewest-pilots".

Parameters:
* N (number of pilots)
* K (distance)
* L (maxlength of intervals)
* T (testcase type ['rand'])
* S (seed)

Constraint:
* %d <= N <= %d
* %d <= K <= %d
* %d <= L <= %d
""" % (
    MINN,
    MAXN,
    MINK,
    MAXK,
    MINK,
    MAXK,
)


def run(N, K, L, T):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]
    if T == "rand":
        if N > 1000:
            N -= randint(1, 100)
        if K > 1000:
            K -= randint(1, 100)
        print(K, N)
        for i in range(N):
            a = randint(0, K)
            b = randint(0, K)
            while a == b or abs(a - b) > L or b > K:
                a = randint(0, K)
                b = randint(a + 1, a + L)
            print(min(a, b), max(a, b))
    if T == "rand2":
        if N > 1000:
            N -= randint(1, 100)
        if K > 1000:
            K -= randint(1, 100)
        print(K, N)
        for i in range(N - 2):
            a = randint(0, K)
            b = randint(0, K)
            while a == b or abs(a - b) > L or b > K:
                a = randint(0, K)
                b = randint(a + L // 2, a + L)
            print(min(a, b), max(a, b))
        print(0, min(L, K))
        print(max(0, K - L), K)
    if T == "rand3":
        assert L < N
        if N > 1000:
            N -= randint(1, 100)
        if K > 1000:
            K -= randint(1, 100)
        print(K, N)
        I = []
        points = {0, K}
        while len(points) < L + 1:
            points.add(randint(0, K))
        points = sorted(points)
        for i in range(L):
            I.append((max(0, points[i] - randint(0, 10)), min(points[i + 1] + randint(0, 10), K)))
        L //= 10
        while len(I) < N:
            a = randint(0, K)
            b = randint(0, K)
            while a == b or abs(a - b) > L or b > K:
                a = randint(0, K)
                b = randint(a + 1, a + L)
            I.append((min(a, b), max(a, b)))
        shuffle(I)
        for interval in I:
            print(*interval)
    if T == "rand4":
        assert L < N
        if N > 1000:
            N -= randint(1, 100)
        if K > 1000:
            K -= randint(1, 100)
        print(K, N)
        I = []
        points = {0, K}
        while len(points) < L + 1:
            points.add(randint(0, K))
        points = sorted(points)
        for i in range(L):
            I.append((max(0, points[i] - randint(0, 10)), min(points[i + 1] + randint(0, 10), K)))
        L //= 10
        shuffle(I)
        A, B = I.pop()
        while len(I) < N:
            a = randint(0, K)
            b = randint(0, K)
            while a == b or abs(a - b) > L or b > K:
                a = randint(0, K)
                b = randint(a + 1, a + L)
            I.append((min(a, b), max(a, b)))
        shuffle(I)
        for interval in I:
            print(*interval)


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
