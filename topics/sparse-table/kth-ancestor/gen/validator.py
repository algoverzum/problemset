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

    N = int(next(f).strip())
    assert MIN <= N <= MAX
    Q = int(next(f).strip())
    assert MIN <= Q <= MAX

    for i in range(Q):
        line = next(f).strip()
        parts = list(map(int, line.split()))
        T = parts[0]
        assert 0 <= T <= 2

        if T == 0:
            assert len(parts) == 3
            Y = parts[1]
            assert MIN <= Y <= N
            X = parts[2]
            assert MIN <= X <= N
        elif T == 1:
            assert len(parts) == 2
            X = parts[1]
            assert MIN <= X <= N
        elif T == 2:
            assert len(parts) == 3
            X = parts[1]
            assert MIN <= X <= N
            K = parts[2]
            assert MIN <= K <= MAX

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
