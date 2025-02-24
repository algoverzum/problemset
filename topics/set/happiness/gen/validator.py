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
    assert MINN <= N <= MAXN
    assert MINM <= M <= MAXM
    S = list(map(int, next(f).split()))
    assert len(S) == N
    for s in S:
        assert MINS <= s <= MAXS
    A = list(map(int, next(f).split()))
    assert len(A) == M
    A = set(A)
    assert len(A) == M
    for a in A:
        assert MINS <= a <= MAXS
    B = list(map(int, next(f).split()))
    assert len(B) == M
    B = set(B)
    assert len(B) == M
    for b in B:
        assert MINS <= b <= MAXS
    assert A.isdisjoint(B)

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
