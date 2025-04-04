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

    N, H = map(int, next(f).split())
    assert MINN <= N <= MAXN
    assert MINH <= H <= MAXH
    A = list(map(int, next(f).split()))
    assert len(A) == N
    assert MINA <= A[0]
    assert A[-1] <= MAXA
    for i in range(1, N):
        assert A[i - 1] < A[i]

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
