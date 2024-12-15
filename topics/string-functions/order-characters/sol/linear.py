#!/usr/bin/env python3
# @check-accepted: *
# O(len(S)), linear

S = input()
letters = [0] * 26
for char in S:
    letters[ord(char) - ord("A")] += 1
for i in range(26):
    print(chr(ord("A") + i) * letters[i], end="")
print()
