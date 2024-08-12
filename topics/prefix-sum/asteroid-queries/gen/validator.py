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

    N, Q = map(int, next(f).split())
    assert 1 <= N <= MAX_N
    assert 1 <= Q <= MAX_Q

    V = list(map(int, next(f).split()))
    assert len(V) == N
    assert all(0 <= v <= MAX_V for v in V)

    for _ in range(Q):
        T = list(map(int, next(f).split()))
        assert 1 <= T[0] <= 2
        if T[0] == 1:
            assert len(T) == 2
            assert 1 <= T[1] <= N
        else:
            assert len(T) == 3
            assert 1 <= T[1] <= T[2] <= N

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
