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
    assert MIN <= N <= MAX_N
    english_words = []
    alien_words = []
    for i in range(N):
        ew, aw = next(f).split()
        english_words.append(ew)
        alien_words.append(aw)
        assert 1 <= len(ew) <= 10
        assert 1 <= len(aw) <= 10
    M = int(next(f))
    assert MIN <= M <= MAX_M
    word_set = set(english_words)
    for i in range(M):
        word = next(f).strip()
        assert 1 <= len(word) <= 10
        assert word in word_set

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
