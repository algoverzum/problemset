#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
squarecounter = 1
while squarecounter * squarecounter < n:
    print(squarecounter * squarecounter)
    squarecounter += 1
