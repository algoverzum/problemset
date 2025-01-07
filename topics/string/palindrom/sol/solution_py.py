#!/usr/bin/env python3
# @check-accepted: *

word = input()
if word == word[::-1]:
    print("YES")
else:
    print("NO")
