#!/usr/bin/env python3
# @check-accepted: *

n = int(input())

# Felső rész
for i in range(1, n + 1):
    print("*" * i)

# Alsó rész
for i in range(n - 1, 0, -1):
    print("*" * i)
