#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
if n % 3 == 0:
    if n % 5 == 0:
        print('bumm')
    else:
        print('bimm')
else:
    if n % 5 == 0:
        print('bamm')
    else:
        print(n)
