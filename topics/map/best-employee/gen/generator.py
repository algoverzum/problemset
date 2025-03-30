#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "best-employee".

Parameters:
* A (N value)
* B (number of different people)
* S (seed)

Constraint:
* %d <= A <= %d
* %d <= B <= %d
""" % (
    MIN,
    MAX,
    MIN,
    MAX // 2,
)


def run(A, B):
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    assert A % 2 == 0
    assert B <= A // 2
    intervals = []
    persons = set()
    while len(persons) < B:
        persons.add(randint(MIN_ID, MAX_ID))
    persons = list(persons)
    shuffle(persons)
    times = [[] for _ in range(B)]
    PER_PERSON = A // B
    # Generate possible times
    for i in range(B):
        t = [randint(MIN_T, MAX_T) for _ in range(PER_PERSON * 2)]
        t.sort()
        for j in range(0, len(t), 2):
            times[i].append((t[j], t[j + 1]))
        shuffle(times[i])
    # Add one interval for each person
    for i in range(B):
        time1, time2 = times[i].pop()
        intervals.append((persons[i], time1, time2))
    # Fill up the rest
    while len(intervals) < A // 2:
        i = randint(0, B - 1)
        if not times[i]:
            continue
        time1, time2 = times[i].pop()
        intervals.append((persons[i], time1, time2))
    # Eliminate duplicate maximums
    shuffle(intervals)
    max_time = 0
    for id, time1, time2 in intervals:
        max_time = max(max_time, time2 - time1)
    first = True
    for item in intervals:
        id, time1, time2 = item
        if time2 - time1 == max_time:
            if first:
                first = False
            else:
                time2 -= randint(1, max_time // 2)
                assert time2 >= time1
                item = (id, time1, time2)
    # Create the input format
    l = []
    for id, time1, time2 in intervals:
        l.append((time1, id, 1))
        l.append((time2, id, 0))
    l.sort(key=lambda x: x[0])
    assert len(l) == A
    print(A)
    print(*[f"{id} {event} {time}" for time, id, event in l], sep="\n")


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
