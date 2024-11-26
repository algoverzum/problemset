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

    line = next(f).split()
    N = int(line[0])
    M = int(line[1])
    assert MIN_N <= N <= MAX_N
    assert MIN_M <= M <= MAX_M
    for _ in range(N):
        line = next(f).split()
        for a in line:
            assert MIN_A <= int(a) <= MAX_A

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
