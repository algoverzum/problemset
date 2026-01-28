#!/usr/bin/env python3
# @check-accepted: *
# Define a function called anagramma here.


def anagramma(S1, S2):
    if sorted(S1) == sorted(S2):
        return True
    return False


# Do not change anything below.

S1 = input()
S2 = input()
if anagramma(S1, S2):
    print(1)
else:
    print(0)
