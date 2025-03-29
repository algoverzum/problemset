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
    citynames = set()
    for i in range(N):
        planet, city_count = next(f).split()
        cities = next(f).split()
        assert len(cities) == int(city_count)
        assert 1 <= len(cities) <= MAXC
        assert 1 <= len(planet) <= 10
        for varos in cities:
            assert 1 <= len(varos) <= 10
            citynames.add(varos)
    M = int(next(f))
    assert MIN <= M <= MAX
    for i in range(M):
        city = next(f).strip()
        assert 1 <= len(city) <= 10
        assert city in citynames
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
