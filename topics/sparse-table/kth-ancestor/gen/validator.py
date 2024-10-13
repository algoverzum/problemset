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

    N = int(next(f))
    assert MIN <= N <= MAX
    Q = int(next(f))
    assert MIN <= Q <= MAX
    for i in range(Q):
        T = int(next(f))
        assert 0 <= T <= 2
        if T == 0:
            Y = int(next(f))
            assert MIN <= Y <= N
            X = int(next(f))
            assert MIN <= X <= N
        elif T == 1:
            X = int(next(f))
            assert MIN <= X <= N
        elif T == 2:
            X = int(next(f))
            assert MIN <= X <= N
            K = int(next(f))
            assert MIN <= K <= N
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
