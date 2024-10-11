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

    line = int(next(f))
    nums = [line]
    while line != 0:
        assert MINS <= line <= MAXS
        line = int(next(f))
        assert line not in nums
        nums.append(line)

    assert MINN <= len(nums) <= MAXN
    assert len(nums) == len(set(nums))
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
