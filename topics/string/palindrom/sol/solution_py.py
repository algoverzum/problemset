#!/usr/bin/env python3
# @check-accepted: *

word = input()
pal = True
for i in range(len(word)):
    pal &= word[i] == word[len(word) - 1 - i]
if pal:
    print("YES")
else:
    print("NO")
