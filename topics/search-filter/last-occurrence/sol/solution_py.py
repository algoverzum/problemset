#!/usr/bin/env python3
# @check-accepted: *
word = input()
key = input()
index = -1
for i in range(len(word) - 1, -1, -1):
    if word[i] == key:
        index = i + 1
        break
print(index)
