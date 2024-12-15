#!/usr/bin/env python3
# @check-accepted: *

S = list(input())
changed = True
while changed:
    changed = False
    for i in range(len(S) - 1):
        if S[i] > S[i + 1]:
            S[i], S[i + 1] = S[i + 1], S[i]
            changed = True
print(*S, sep="")
