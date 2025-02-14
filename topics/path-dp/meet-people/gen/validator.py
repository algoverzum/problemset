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

    N, M = [int(x) for x in next(f).split()]
    assert MIN_DIM <= N <= MAX_DIM
    assert MIN_DIM <= M <= MAX_DIM
    for _ in range(N):
        line = list(map(int, next(f).split()))
        assert len(line) == M
        for e in line:
            assert MIN_P <= e <= MAX_P

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
