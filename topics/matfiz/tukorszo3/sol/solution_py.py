#!/usr/bin/env python3
# @check-accepted: *

word = input().replace(" ", "").replace(",", "").replace(".", "").lower()

if word == word[::-1]:
    print("1")
else:
    print("0")
