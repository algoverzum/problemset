#!/usr/bin/env python3
# @check-accepted: *

word = input()
key = input()
i = 0
while i < len(word) and word[i] != key:
    i += 1
if i < len(word):
    print(i + 1)
else:
    print(-1)
