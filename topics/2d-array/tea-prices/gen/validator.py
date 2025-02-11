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

    N, M = map(int, next(f).split())
    assert MIN <= N <= MAXN
    assert MIN <= M <= MAXN

    for i in range(N):
        line = list(map(int, next(f).split()))
        assert len(line) == M
        for v in line:
            assert MIN <= v <= MAXC

    C = int(next(f))
    assert MIN <= C <= MAXC

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
