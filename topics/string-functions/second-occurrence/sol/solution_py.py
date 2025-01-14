#!/usr/bin/env python3
# @check-accepted: *

word = input()
if word.count("f") == 0:
    print(-2)
elif word.count("f") == 1:
    print(-1)
else:
    first = word.find("f")
    print(word.find("f", first + 1))
