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
    assert 1 <= N <= MAXN
    assert 1 <= Q <= MAXQ

    H = list(map(int, next(f).split()))
    assert len(H) == N

    assert all(MIN <= h <= MAX for h in H)

    for _ in range(Q):
        S, K = map(int, next(f).split())
        assert 1 <= S <= N
        assert 0 <= K
        assert S + 2 ** K - 1 <= N

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
