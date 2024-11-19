#!/usr/bin/env python3
# @check-accepted: *

S = input()
n = len(S)
print(S[0] + S[-1])
print(S[::-1])
print(S[2::3])
print(S[: n // 2])
print(S[n // 2 :])
