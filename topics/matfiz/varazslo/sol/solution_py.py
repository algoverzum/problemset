#!/usr/bin/env python3
# @check-accepted: *

A = input().split("+")
A.sort()
print(*A, sep="+")
