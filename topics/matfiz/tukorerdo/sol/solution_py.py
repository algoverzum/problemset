#!/usr/bin/env python3
# @check-accepted: *

s = input()
t = input()
if s == t[::-1]:
    print("YES")
else:
    print("NO")
