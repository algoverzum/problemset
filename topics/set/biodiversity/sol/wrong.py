#!/usr/bin/env python3
# @check-wrong-answer: *

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if len(a) > len(b):
    print(len(a))
    print(*sorted(a))
else:
    print(len(b))
    print(*sorted(b))
