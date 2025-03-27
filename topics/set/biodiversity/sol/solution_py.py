#!/usr/bin/env python3
# @check-accepted: *

n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
all = a | b
print(len(all))
print(*sorted(all))
