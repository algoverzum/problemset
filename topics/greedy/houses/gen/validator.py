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

    T = int(next(f))
    assert MINT <= T <= MAXT

    for _ in range(T):
        N, B = map(int, next(f).split())
        assert MINN <= N <= MAXN
        assert MINB <= B <= MAXB
        A = list(map(int, next(f).split()))
        assert len(A) == N
        for a in A:
            assert MINA <= a <= MAXA

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
