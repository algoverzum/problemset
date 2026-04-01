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
    assert MIN_N <= int(line[0]) <= MAX_N
    assert MIN_M <= int(line[1]) <= MAX_M
    assert MIN_L <= int(line[2]) <= MAX_L

    for _ in range(N):
        line = next(f).split()
        for i in range(M):
            assert MIN_P <= int(line[i]) <= MAX_P

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
