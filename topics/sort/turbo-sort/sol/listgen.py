#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
nums = [int(input()) for i in range(n)]
nums.sort()
print(*nums, sep="\n")
