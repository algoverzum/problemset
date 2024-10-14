#!/usr/bin/env python3
# @check-accepted: *


def count(word, letter):
    cnt = 0
    for c in word:
        if c == letter:
            cnt += 1
    return cnt


print(count("chocolate", "c"))
print(count("chocolate", "b"))
print(count("tree", "t"))
print(count("tree", "e"))
print(count("", "x"))
print(count("oooooooooo", "o"))
print(count("shshshshshshshsh", "s"))
print(count("pneumonoultramicroscopicsilicovolcanoconiosis", "i"))
