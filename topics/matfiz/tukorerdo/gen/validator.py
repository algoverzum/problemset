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

    word1 = next(f).strip()
    assert MIN <= len(word1) <= MAX
    for char in word1:
        assert ord("a") <= ord(char) <= ord("z")

    word2 = next(f).strip()
    assert MIN <= len(word2) <= MAX
    for char in word2:
        assert ord("a") <= ord(char) <= ord("z")

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
