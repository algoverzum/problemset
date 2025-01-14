#!/usr/bin/env python3
# @check-accepted: *

word = input()
if word.count("x") == 0:
    print(-2)
elif word.count("x") == 1:
    print(-1)
else:
    first = word.find("x")
    print(word.find("x", first + 1))
