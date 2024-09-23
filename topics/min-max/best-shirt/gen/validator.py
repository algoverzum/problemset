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

    LINE = next(f).split()
    N = int(LINE[0])
    K = int(LINE[1])
    assert N_MIN <= N <= N_MAX
    assert MONEY_MIN <= K <= MONEY_MAX

    LINE = next(f).split()
    for i in range(N):
        assert MONEY_MIN <= int(LINE[i]) <= MONEY_MAX

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
