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
    ID_map = {}
    last_time = 0
    max_time = 0
    max_cnt = 0
    for i in range(N):
        ID, event, time = map(int, next(f).split())
        assert MIN_ID <= ID <= MAX_ID
        assert MIN_T <= time <= MAX_T
        assert event in (0, 1)
        assert time >= last_time
        if ID in ID_map:
            prev_event, prev_time = ID_map[ID]
            assert event != prev_event, f"{event} {prev_event} {time} {prev_time}"
            assert prev_time <= time
            if event == 0:
                if time - prev_time == max_time:
                    max_cnt += 1
                if time - prev_time > max_time:
                    max_time = time - prev_time
                    max_cnt = 1
        else:
            assert event == 1
        ID_map[ID] = (event, time)
        last_time = time
    for event, _ in ID_map.values():
        assert event == 0
    assert max_cnt == 1

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
