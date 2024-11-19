#!/usr/bin/env python3
# @check-accepted: *

word = input()
letterCount = 0
for i in range(len(word)):
    if word[i] == "p":
        letterCount += 1

print(letterCount)
