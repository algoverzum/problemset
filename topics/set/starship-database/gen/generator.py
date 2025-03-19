#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "starship-database".

Parameters:
* Q (number of queries)
* X (max x)
* S (seed)

Constraint:
* %d <= Q <= %d
* %d <= X <= %d
""" % (
    MINQ,
    MAXQ,
    MINX,
    MAXX,
)


def set_choice(cur, X):
    # try 10 iterations then get first element
    for i in range(10):
        x = randint(1, X)
        if x in cur:
            return x
    return next(iter(cur))


def run(Q, X):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    if Q == 199999:
        # spec generator: add many elements then delete from beginning and ask from end
        print(Q)
        cur = set()
        l = []
        for i in range(Q // 2):
            x = randint(1, X)
            if x not in cur:
                cur.add(x)
                l.append(x)
            print(1, x)
        l = l[::-1]
        for i in range(Q // 2, Q):
            t = randint(2, 3)
            if t == 2:
                print(2, l.pop())
            else:
                if randint(1, 10) > 4:
                    print(3, randint(1, X))
                else:
                    print(3, choice(l[:20]))
        return

    print(Q)
    cur = set()
    for i in range(Q):
        t = randint(1, 3)
        if t == 1:
            if cur and randint(1, 10) > 9:
                x = set_choice(cur, X)
                cur.add(x)
            else:
                x = randint(1, X)
                cur.add(x)
        if t == 2:
            if cur and randint(1, 10) > 6:
                x = set_choice(cur, X)
                cur.remove(x)
            else:
                x = randint(1, X)
                cur.discard(x)
        if t == 3:
            if cur and randint(1, 10) > 1:
                x = set_choice(cur, X)
            else:
                x = randint(1, X)
        print(t, x)


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
