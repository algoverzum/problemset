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
    assert MIN_N <= int(line[0]) <= MAX_N
    assert MIN_K <= int(line[1]) <= MAX_K
    assert MIN_S <= int(line[2]) <= MAX_S
    line = next(f).split()
    for s in line:
        assert MIN_S <= int(s) <= MAX_S

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
