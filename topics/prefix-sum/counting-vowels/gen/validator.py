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

    S = next(f).strip()
    assert MINS <= len(S) <= MAXS
    for s in S:
        assert s in "abcdefghijklmnopqrstuvwxyz"

    Q = int(next(f))
    assert MINQ <= Q <= MAXQ

    for _ in range(Q):
        i, j = map(int, next(f).split())
        assert 1 <= i <= j <= len(S)

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
