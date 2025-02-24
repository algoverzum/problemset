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

    N, M = map(int, next(f).split())
    assert MIN <= N <= MAX
    assert MIN <= M <= MAX
    ids1 = list(map(int, next(f).split()))
    assert len(ids1) == N
    for i in range(N):
        assert MIN2 <= ids1[i] <= MAX2
    ids2 = list(map(int, next(f).split()))
    assert len(ids2) == M
    for j in range(M):
        assert MIN2 <= ids2[j] <= MAX2
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
