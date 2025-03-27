#!/usr/bin/env python3

from limits import *

import sys
import os


def usage():
    print("Usage: %s file_input.txt [subtask_number]" % sys.argv[0], file=sys.stderr)
    exit(1)


def run(f, st):
    for k, v in subtasks[st].items():
        globals()[k] = v

    N = int(next(f))
    assert MIN <= N <= MAX
    cities = set()
    for i in range(N):
        row = next(f).split()
        assert 2 <= len(row) <= MAXC + 1
        for j in range(len(row)):
            assert 1 <= len(row[j]) <= 10
        for j in range(1, len(row)):
            cities.add(row[j])
    M = int(next(f))
    assert MIN <= M <= MAX
    for i in range(M):
        city = next(f).strip()
        assert 1 <= len(city) <= 10
        assert city in cities
    assert next(f, None) is None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()

    # Di default, ignora i subtask
    st = 0

    if len(sys.argv) == 3:
        st = int(sys.argv[2])

    f = open(sys.argv[1])
    run(f, st)
