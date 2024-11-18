#!/usr/bin/env python3

from constraints import *
import sys
import os


def usage():
    print("Usage: %s file_input.txt [subtask_number]" % sys.argv[0], file=sys.stderr)
    exit(1)


def run(f, st):
    for k, v in subtasks[st].items():
        globals()[k] = v
    T = int(next(f))
    assert 1 <= T <= MAXT
    sum_n, sum_m = 0, 0
    for tt in range(T):
        assert next(f).strip() == ""
        N, M = map(int, next(f).split())
        assert 1 <= N <= MAXN
        assert 1 <= M <= MAXM
        sum_n += N
        sum_m += M
        assert 1 <= sum_n <= SUMN, str(
            str(sum_n)
            + " "
            + str(T)
            + " "
            + str(MAXN)
            + " "
            + str(SUMN)
            + " "
            + str(MAXM)
            + " "
            + str(st)
            + " "
            + str(N)
            + " "
            + str(M)
        )
        assert 1 <= sum_m <= MAXM
        for i in range(N):
            S = next(f).strip()
            assert len(S) == M
            assert all("0" <= c <= "1" for c in S)
    assert next(f, None) is None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    st = 0
    if len(sys.argv) == 3:
        st = int(sys.argv[2])
    f = open(sys.argv[1])
    run(f, st)
