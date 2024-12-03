#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
i = 1
while i <= n and int(input()) != 0:
    i += 1
if i <= n:
    print(i)
else:
    print(-1)
