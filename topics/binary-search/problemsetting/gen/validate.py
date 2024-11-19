#!/usr/bin/env python3

from constraints import *

import sys


def usage():
    print("Usage: %s file_input.txt [subtask_number]" % sys.argv[0], file=sys.stderr)
    exit(1)


def run(f, st):
    for k, v in subtasks[st].items():
        globals()[k] = v

    T = int(next(f))
    assert 1 <= T <= MAXT
    S = 0
    for _ in range(T):
        N = int(next(f))
        assert 2 <= N <= MAXN
        S += N
        A = list(map(int, next(f).split()))
        assert len(A) == N
        assert all(0 <= a <= MAXA for a in A)
        B = list(map(int, next(f).split()))
        assert len(B) == N - 1
        assert all(0 <= b <= MAXB for b in B)

    assert S <= MAXN

    assert next(f, None) is None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()

    st = 0

    if len(sys.argv) == 3:
        st = int(sys.argv[2]) + 1

    f = open(sys.argv[1])
    run(f, st)
