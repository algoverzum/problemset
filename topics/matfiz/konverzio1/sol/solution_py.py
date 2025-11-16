#!/usr/bin/env python3
# @check-accepted: *

binaris = input()
decimalis = 0

for decjegy in binaris:
    decimalis = 2 * decimalis + int(decjegy)

print(decimalis)
