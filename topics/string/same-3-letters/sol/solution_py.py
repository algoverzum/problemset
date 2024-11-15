#!/usr/bin/env python3
# @check-accepted: *

word = input()
if word[0] == word[1] and word[1] == word[2]:
    print("NO")
else:
    print("YES")
