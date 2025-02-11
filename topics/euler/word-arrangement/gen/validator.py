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

    # N = int(next(f))
    # assert MIN1 <= N <= MAX1
    N = 1
    for _ in range(N):
        M = int(next(f))
        assert MIN2 <= M <= MAX2
        for i in range(M):
            W = next(f)
            assert MIN3 <= len(W) <= MAX3 + 1
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
