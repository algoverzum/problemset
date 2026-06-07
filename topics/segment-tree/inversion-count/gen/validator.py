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
    assert MIN <= T <= MAXT

    sumN = 0

    for _ in range(T):
        empty = next(f).strip()
        assert len(empty) == 0
        N = int(next(f))
        sumN += N
        assert MIN <= N <= MAXN
        A = set()
        for i in range(N):
            a = int(next(f))
            assert MIN <= a <= MAXA
            A.add(a)
        assert len(A) == N
    assert MIN <= sumN <= MAXN

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
