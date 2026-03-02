#!/usr/bin/env python3

from limits import *

import sys
import os


def usage():
    print("Usage: %s file_input.txt [subtask_number]" % sys.argv[0], file=sys.stderr)
    exit(1)


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]) == 0


def run(f, st):
    for k, v in subtasks[st].items():
        globals()[k] = v

    N = int(next(f))
    assert MINN <= N <= MAXN

    points = []
    for i in range(N):
        X, Y = map(int, next(f).split())
        assert MINX <= X <= MAXX
        assert MINX <= Y <= MAXX
        points.append((X, Y))

    collin = True
    for i in range(2, N):
        if not collinear(points[0], points[1], points[i]):
            collin = False
            break
    assert not collin

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
