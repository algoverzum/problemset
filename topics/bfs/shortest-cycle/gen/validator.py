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

    N, M, P = map(int, next(f).split())
    assert MIN <= N <= MAX
    assert MIN2 <= M <= MAX2
    assert MIN <= P <= N
    edges = set()
    # sys.stderr.write(f"edges: {M}\n")
    for i in range(M):
        a, b = map(int, next(f).split())
        assert MIN <= a <= MAX
        assert MIN <= b <= MAX
        edge = (min(a, b), max(a, b))
        assert edge not in edges
        edges.add(edge)
    # sys.stderr.write(f"edges_in_set: {len(edges)}\n")
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
