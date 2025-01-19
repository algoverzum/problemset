#!/usr/bin/env python3
# @check-accepted: *


def reverse():
    x = int(input())
    if x != 0:
        reverse()
        print(x)
        return
    print(0)


reverse()
