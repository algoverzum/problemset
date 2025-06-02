#!/usr/bin/env python3

from limits import *

import sys
import os
import string


def usage():
    print("Usage: %s file_input.txt [subtask_number]" % sys.argv[0], file=sys.stderr)
    exit(1)


def run(f, st):
    for k, v in subtasks[st].items():
        globals()[k] = v

    N = int(next(f))
    assert MIN <= N <= MAX
    for _ in range(N):
        w, v = next(f).split()
        assert 1 <= len(w) <= 10
        assert all(c in string.ascii_lowercase for c in w)
        assert MIN <= int(v) <= MAX
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
