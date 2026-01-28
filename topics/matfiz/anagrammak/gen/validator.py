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

    abc = {chr(ord("a") + i) for i in range(26)}

    S1 = next(f).strip()
    assert MIN <= len(S1) <= MAX
    for betu in S1:
        assert betu in abc

    S2 = next(f).strip()
    assert MIN <= len(S2) <= MAX
    for betu in S2:
        assert betu in abc

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
