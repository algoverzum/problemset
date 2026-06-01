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

    name = next(f)

    cur = int(next(f))
    while cur != 0:
        assert cur in [0, 2, 3, 4, 5, 6]
        if cur == 2:
            on = int(next(f))
            assert on in [0, 1]
        if cur in [3, 4]:
            x = int(next(f))
            assert 0 <= x <= 100
        cur = int(next(f))
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
