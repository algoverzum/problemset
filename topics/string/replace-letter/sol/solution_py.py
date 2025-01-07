#!/usr/bin/env python3
# @check-accepted: *

word = input()
for letter in word:
    if letter == "a":
        print("e", end="")
    else:
        print(letter, end="")
