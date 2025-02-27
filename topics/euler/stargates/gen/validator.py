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

    N, R = map(int, next(f).split())
    assert MIN1 <= N <= MAX1
    assert MIN2 <= R <= MAX2

    edges = set()
    for _ in range(R):
        U, V = map(int, next(f).split())
        assert MIN1 <= U <= MAX1
        assert MIN1 <= V <= MAX1
        edges.add((min(U, V), max(U, V)))
    assert len(edges) == R

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
