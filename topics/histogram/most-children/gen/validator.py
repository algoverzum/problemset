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

    N, K = map(int, next(f).split())
    assert MINN <= N <= MAXN
    assert MINK <= K <= MAXK

    data = []
    szulo = {}
    gyerek = {}
    for i in range(K):
        Sz, Gy = map(int, next(f).split())
        assert 1 <= Sz <= N
        assert 1 <= Gy <= N
        data.append((Sz, Gy))
        try:
            gyerek[Gy].append(Sz)
        except:
            gyerek[Gy] = [Sz]
        try:
            szulo[Sz].append(Gy)
        except:
            szulo[Sz] = [Gy]

    assert max([len(gyerek[x]) for x in gyerek]) <= 2

    assert len(data) == len(set(data))

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
