#!/usr/bin/env python3


abc = [chr(ord("a") + i) for i in range(26)]


def common_letters(s, t):
    common = ""
    for letter in abc:
        if letter in s and letter in t:
            common += letter
    return common


print(common_letters("apple", "leaves"))
print(common_letters("chocolate", "catching"))
print(common_letters("chocolate", "chocolate"))
print(common_letters("chocolate", "banana"))
# print(common_letters("chocolate", "drums"))
print(common_letters("tree", "e"))
print(common_letters("", "x"))
print(common_letters("oooooooooo", "ooo"))
print(common_letters("shshshshshshshsh", "shake"))
print(common_letters("pneumonoultramicroscopicsilicovolcanoconiosis", "methylenedioxymethamphetamine"))
