#!/usr/bin/env python3
# @check-wrong-answer: *

n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]

for row in dist:
    print(*row)
