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
    for _ in range(T):
        A, B, K = map(int, next(f).split())
        assert 1 <= A <= MAXV
        assert 1 <= B <= MAXV
        assert 1 <= K <= MAXV

    assert next(f, None) is None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()

    st = 0

    if len(sys.argv) == 3:
        st = int(sys.argv[2]) + 1

    f = open(sys.argv[1])
    run(f, st)
