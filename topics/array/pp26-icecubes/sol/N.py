#!/usr/bin/env python3
# @check-accepted: non-zero
# @check-wrong-answer: examples mid no-limits


N = int(input())
C = list(map(int, input().split()))

print(sum(C) - N)
