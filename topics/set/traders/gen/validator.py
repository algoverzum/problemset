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
    for _ in range(N):
        fruit = next(f).strip()
        assert MIN2 <= len(fruit) <= MAX2
        for char in fruit:
            assert char.islower()
    M = int(next(f))
    assert MIN <= M <= MAX
    for _ in range(M):
        fruit = next(f).strip()
        assert MIN2 <= len(fruit) <= MAX2
        for char in fruit:
            assert char.islower()
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
