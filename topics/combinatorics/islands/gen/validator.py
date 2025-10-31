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

    for i in range(N):
        line = list(map(int, next(f).split()))
        assert len(line) == line[0] + 1
        assert 0 <= line[0] <= N - 1
        assert len(set(line[1:])) == line[0]
        if len(line) > 1:
            assert 1 <= min(line[1:])
            assert min(line[1:]) <= N

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
