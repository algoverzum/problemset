#!/usr/bin/env python3
# @check-accepted: *

n, m = map(int, input().split())
ids = set(map(int, input().split()))

ids.update(map(int, input().split()))
print(len(ids))
print(*sorted(ids))
