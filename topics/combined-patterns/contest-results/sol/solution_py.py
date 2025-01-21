#!/usr/bin/env python3
# @check-accepted: *

n, q = map(int, input().split())
result = input().split()
names = input().split()
for name in names:
    if name in result:
        print(result.index(name) + 1, end=" ")
    else:
        print(-1, end=" ")
