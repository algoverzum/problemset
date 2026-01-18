#!/usr/bin/env python3
# @check-accepted: *

mondat = input()
db = 1
for ch in mondat:
    if ch == " ":
        db += 1
print(db)
