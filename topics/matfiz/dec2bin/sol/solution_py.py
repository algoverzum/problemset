#!/usr/bin/env python3
# @check-accepted: *
# Define a function called dec2bin here.


def dec2bin(N):
    bin = ""
    while N:
        bin = str(N % 2) + bin
        N //= 2
    return bin


# Do not change anything below.

N = int(input())
print(dec2bin(N))
