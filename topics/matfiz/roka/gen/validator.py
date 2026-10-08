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

    N_line = next(f).split()
    assert MIN_N <= int(N_line[0]) <= MAX_N
    assert MIN_L <= int(N_line[1]) <= MAX_L
    assert MIN_K <= int(N_line[2]) <= MAX_K
    for _ in range(int(N_line[1])):
        DB = int(next(f))
        assert MIN_DB <= DB <= MAX_DB

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
