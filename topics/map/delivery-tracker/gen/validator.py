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
    assert MINN <= N <= MAXN
    deliveries = {}
    for i in range(N):
        x, y, p = map(int, next(f).split())
        deliveries[(x, y)] = deliveries.get((x, y), 0) + p
        assert MINP <= p <= MAXP
        assert MINXY <= x <= MAXXY
        assert MINXY <= y <= MAXXY

    max_packages = max(deliveries.values())
    res = 0
    for (x, y) in deliveries:
        if deliveries[(x, y)] == max_packages:
            res += 1
    assert res == 1

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
