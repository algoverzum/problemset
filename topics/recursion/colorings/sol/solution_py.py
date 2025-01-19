#!/usr/bin/env python3
# @check-accepted: *


def colorings(cur, n):
    if len(cur) == n:
        print(cur)
        return
    if cur[-1:] != "R":
        colorings(cur + "R", n)
    colorings(cur + "W", n)


n = int(input())
colorings("", n)
