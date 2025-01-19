#!/usr/bin/env python3
# @check-accepted: *


def building(cur, n):
    if len(cur) == n:
        print(cur)
        return
    nextR = cur + "R"
    if nextR[-2:] != "RR":
        building(nextR, n)
    building(cur + "W", n)


n = int(input())
building("", n)
