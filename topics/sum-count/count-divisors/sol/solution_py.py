#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
osztok = 0
for i in range(1, n + 1):
    if n % i == 0:
        osztok = osztok + 1
print(osztok)
