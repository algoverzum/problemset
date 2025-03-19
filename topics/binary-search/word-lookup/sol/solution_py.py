#!/usr/bin/env python3
# @check-accepted: *


def binary_search(word, list):
    l = 0
    r = len(list)
    while l + 1 < r:
        mid = (l + r) // 2
        if list[mid] <= word:
            l = mid
        else:
            r = mid
    return l


n = int(input())

english_words = []
alien_words = []
for i in range(n):
    english_word, alien_word = input().split()
    english_words.append(english_word)
    alien_words.append(alien_word)

m = int(input())
for i in range(m):
    word = input()
    idx = binary_search(word, english_words)
    print(alien_words[idx])
