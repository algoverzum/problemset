#!/usr/bin/env python3
# @check-accepted: *

word = input()
key = input()
i = 0
while word[i] != key:
    if i == len(word) - 1:
        print(-1)
        exit(0)
    i += 1
print(i + 1)
