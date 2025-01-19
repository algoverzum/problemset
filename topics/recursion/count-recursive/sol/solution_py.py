#!/usr/bin/env python3
# @check-accepted: *


def count(string, char):
    if len(string) == 0:
        return 0
    if string[0] == char:
        return 1 + count(string[1:], char)
    else:
        return count(string[1:], char)


# Do not change anything below
S = input()
c = input()
print(count(S, c))
