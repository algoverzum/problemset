#!/usr/bin/env python3
# @check-accepted: *

import sys

input = sys.stdin.readline  # faster than built-in input()

N = int(input())
nums = [int(input()) for i in range(N)]
nums.sort()
print(*nums, sep="\n")
