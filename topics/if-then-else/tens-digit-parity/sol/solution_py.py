#!/usr/bin/env python3
# @check-accepted: *

a = int(input())
jegy = a // 10 % 10
if jegy % 2 == 0:
    print(1)
else:
    print(0)
