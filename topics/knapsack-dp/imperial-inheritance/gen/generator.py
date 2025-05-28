#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "imperial-inheritance".

Parameters:
* A (N value)
* B (maximum value)
* Type (type)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
* %d <= Type <= %d
""" % (
    MINN,
    MAXN,
    MINV,
    MAXV,
    0,
    4,
)


def run(A, B, Type):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    numbers = []
    current_sum = 0
    # full random type
    if Type == 0:
        for i in range(A):
            val = randint(1, B)
            current_sum += val
            if current_sum > 10000:
                val = val - (current_sum - 10000)
                numbers.append(val)
                break
            numbers.append(val)

    # not partitionable using no the power of 2 trick
    elif Type == 1:
        for _ in range(A):
            next_val = current_sum + randint(1, 10)
            numbers.append(next_val)
            current_sum += next_val
            if current_sum > 5000:
                break
    # power of 2 edgecase
    elif Type == 2:
        B = 10000
        A = 14
        for i in range(13):
            numbers.append(pow(2, i))
    # very small equal partition. again trickery with power of 2.
    elif Type == 3:
        numbers.append(1)
        numbers.append(2)
        numbers.append(3)
        for i in range(3, 13):
            numbers.append(pow(2, i))
    # lot of small cases
    elif Type == 4:
        for i in range(A):
            numbers.append(randint(1, 33))
    print(len(numbers))
    print(*numbers)


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
