#!/usr/bin/env python3
# @check-accepted: *

sz = int(input())
ered = int(input())
N = int(input())
while sz > 0 and ered > N:
    sz -= 1
    ered = ered - 2
    print(sz)
