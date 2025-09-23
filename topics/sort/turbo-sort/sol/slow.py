#!/usr/bin/env python3
# @check-accepted: examples
# @check-time-limit-exceeded: all


N = int(input())
nums = []
for i in range(N):
    num = int(input())
    nums.append(num)
nums.sort()
for num in nums:
    print(num)
