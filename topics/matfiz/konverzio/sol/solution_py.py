#!/usr/bin/env python3
# @check-accepted: *
# Define a function called dec2bin here.


def dec2bin(N):
    return "" if N == 0 else dec2bin(N // 2) + str(N % 2)


# Do not change anything below.

N = int(input())
print(dec2bin(N))
