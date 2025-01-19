#!/usr/bin/env python3
# @check-accepted: *


def building(cur, n):
    if len(cur) == n:
        print(cur)
        return
    if cur[-1:] != "R":
        building(cur + "R", n)
    building(cur + "W", n)


n = int(input())
building("", n)
