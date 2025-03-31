#!/usr/bin/env python3
# @check-accepted: *

input()
a = set([int(x) for x in input().split()])
b = set([int(x) for x in input().split()])
all = a | b
print(len(all))
print(*sorted(all))
