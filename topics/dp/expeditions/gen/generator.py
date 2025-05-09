#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed, choices
from inspect import signature

usage = """Generator for "expeditions".

Parameters:
* A (N value)
* B (M value)
* T (Type )
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
* %d <= T <= %d
""" % (
    MINN,
    MAXN,
    MINM,
    MAXM,
    0,
    3,
)


def run(A, B, T):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]
    # T==0 full random
    # T==1 csak egy A és B-t spammelek. Hogy lássam hogy kezeli kód. ha nem éri el az M értéket és hogy hogy kezeli ha két azonos A-B expedíció pár különböző kredit értéket adna.
    # T==2 A csökkenő sorrendbe
    # T==3 konstans kredit/parcella mohó ellen.
    print(A, B)
    if T == 0:
        Endvalues = choices(range(1, B + 1), k=A)
        Endvalues.sort()
        sorted(Endvalues)
        for i in range(A):
            start = randint(1, Endvalues[i])
            print(start, Endvalues[i], randint(1, MAXK))
    elif T == 1:
        konstans = randint(1, B - 1)
        for i in range(A):
            print(konstans, konstans, randint(1, MAXK))
    elif T == 2:
        Endvalues = choices(range(B // 2, B + 1), k=A)
        Endvalues.sort()
        lastA = Endvalues[0]
        for i in range(A):
            start = randint(max(1, lastA - (2000 // A)), lastA)
            lastA = start
            assert start <= Endvalues[i]
            print(start, Endvalues[i], randint(1, MAXK))
    elif T == 3:
        Endvalues = choices(range(1, B + 1), k=A)
        Endvalues.sort()
        for i in range(A):
            start = randint(1, Endvalues[i])
            print(start, Endvalues[i], Endvalues[i] - start + 1)


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
