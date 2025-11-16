#!/usr/bin/env python3
# @check-accepted: *

dec = int(input())

if dec == 0:
    print(0)
else:
    bin_str = ""
    while dec != 0:
        maradek = dec % 2
        bin_str += str(maradek)
        dec //= 2
    # Megfordítva kiírjuk
    print(bin_str[::-1])
