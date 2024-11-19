#!/usr/bin/env python3
# @check-accepted: *

N = int(input())
words = input().split()
shortest_word = words[0]
shortest_length = len(words[0])
for word in words[1:]:
    if len(word) < shortest_length:
        shortest_word = word
        shortest_length = len(word)
print(shortest_word)
