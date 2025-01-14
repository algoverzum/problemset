#!/usr/bin/env python3
# @check-accepted: *

word = input()
first = word.find("x")
if first == -1:
    print(-2)
else:
    print(word.find("x", first + 1))
