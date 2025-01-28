#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
names = input().split()
names.sort()
print(*names)
